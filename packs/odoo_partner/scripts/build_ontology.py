#!/usr/bin/env python3
"""Build the Odoo ontology (what changed per version step) from OCA OpenUpgrade, as Markdown.

Reads a checkout of OpenUpgrade per target version (one directory per branch, e.g. <root>/19.0) and parses:
  - openupgrade_scripts/apriori.py               renamed/merged modules and models
  - scripts/<module>/<ver>/upgrade_analysis*.txt  models and fields added/removed/changed, removed xmlids,
                                                  with the maintainers' comments ("DONE: renamed in pre-migration")
  - scripts/<module>/<ver>/pre-migration.py      renamed fields declared as (model, table, old, new)
Only Odoo Community is covered (OpenUpgrade does not migrate Enterprise). Each version file is rewritten in
full at every run.

Writes one Markdown file per version step (<from>-<to>.md) into .texo/ontology/ of the working folder: the
ontology is generated on the machine from public data and never committed. The checkouts are the mirrors of the
threads openupgrade-<NN> of the organisation (texo mount, in $TEXO_SHARED_DIR/mirrors), or any folder with one checkout
per version named <NN>.0 or openupgrade-<NN>:

  python3 $(texo where --pack odoo_partner)/scripts/build_ontology.py [--root <root>] [--versions 17.0 18.0 19.0]
                                                          [--out <dir>] [--dry-run]

Standard library only.
"""
import argparse
import ast
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

FIELD_LINE = re.compile(r"^(?P<module>[\w.]+)\s*/\s*(?P<model>[\w.]+)\s*/\s*(?P<field>\w+)\s*"
                        r"\((?P<type>[^)]*)\)\s*:\s*(?P<detail>.+)$")
MODEL_LINE = re.compile(r"^(?P<what>new|obsolete) model (?P<model>[\w.]+)")
XMLID_LINE = re.compile(r"^(?P<what>NEW|DEL) (?P<model>[\w.]+): (?P<xmlid>[\w.]+)")
SELECTION_REMOVED = re.compile(r"selection_keys removed: \[(?P<keys>[^\]]*)\]")
# Removed/added records that break a port (inherit_id, groups=, ref() in code); data records are left out.
XMLID_MODELS = ("ir.ui.view", "res.groups", "ir.actions.", "ir.ui.menu", "ir.rule", "ir.model.access", "ir.cron")


@dataclass
class Change:
    to_version: str
    kind: str
    name: str
    change: str
    module: str | None = None
    model: str | None = None
    new_name: str | None = None
    field_type: str | None = None
    detail: str | None = None
    note: str | None = None
    source: str = "openupgrade:analysis"
    source_ref: str | None = None

    @property
    def from_version(self) -> str:
        return f"{int(float(self.to_version)) - 1}.0"


def parse_analysis(text: str, to_version: str, source_ref: str) -> list[Change]:
    """Models, fields and xmlids of one upgrade_analysis(_work).txt. A comment applies to the lines above it."""
    changes: list[Change] = []
    block: list[Change] = []  # entries waiting for the comment that follows them
    module = None
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("---") and "module '" in line:
            module = line.split("module '", 1)[1].split("'", 1)[0]
            continue
        if line.startswith("#"):
            note = line.lstrip("# ").strip()
            for c in block:
                c.note = f"{c.note} {note}" if c.note else note
            continue
        if block and block[-1].note:
            block = []  # a new group starts after a commented one
        new: list[Change] = []
        if m := FIELD_LINE.match(line):
            detail = m["detail"].strip()
            change = "removed" if detail.startswith("DEL") else "added" if detail.startswith("NEW") else "changed"
            new.append(Change(to_version, "field", m["field"], change, m["module"], m["model"],
                              field_type=m["type"].strip(), detail=detail, source_ref=source_ref))
            if sel := SELECTION_REMOVED.search(detail):
                for key in (k.strip().strip("'\"") for k in sel["keys"].split(",") if k.strip()):
                    new.append(Change(to_version, "selection", f"{m['field']}:{key}", "removed", m["module"],
                                      m["model"], detail=detail, source_ref=source_ref))
        elif m := MODEL_LINE.match(line):
            new.append(Change(to_version, "model", m["model"], "added" if m["what"] == "new" else "removed",
                              module, m["model"], detail=line, source_ref=source_ref))
        elif m := XMLID_LINE.match(line):  # filtered in collect(), which knows the removed models
            new.append(Change(to_version, "xmlid", m["xmlid"], "added" if m["what"] == "NEW" else "removed",
                              module, m["model"], detail=line, source_ref=source_ref))
        changes += new
        block += new
    return changes


def _literals(tree: ast.AST):
    """(variable name, literal value) of every module-level assignment that is a plain literal."""
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            try:
                yield node.targets[0].id, ast.literal_eval(node.value)
            except ValueError:
                continue


def parse_pre_migration(text: str, module: str, to_version: str, source_ref: str) -> list[Change]:
    """Renamed fields declared as (model, table, old, new) tuples, wherever they are assigned."""
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return []
    changes = []
    for _name, value in _literals(tree):
        if not isinstance(value, (list, tuple)):
            continue
        for item in value:
            if (isinstance(item, tuple) and len(item) == 4 and all(isinstance(x, str) for x in item)
                    and "." in item[0] and item[2].isidentifier() and item[3].isidentifier()):
                changes.append(Change(to_version, "field", item[2], "renamed", module, item[0], new_name=item[3],
                                      detail=f"rename_fields {item[0]}.{item[2]} -> {item[3]}",
                                      source="openupgrade:pre-migration", source_ref=source_ref))
    return changes


def parse_apriori(text: str, to_version: str, source_ref: str) -> list[Change]:
    kinds = {"renamed_modules": ("module", "renamed"), "merged_modules": ("module", "merged"),
             "renamed_models": ("model", "renamed"), "merged_models": ("model", "merged")}
    changes = []
    for name, value in _literals(ast.parse(text)):
        if name in kinds and isinstance(value, dict):
            kind, change = kinds[name]
            for old, new in value.items():
                changes.append(Change(to_version, kind, old, change, model=old if kind == "model" else None,
                                      module=old if kind == "module" else None, new_name=new,
                                      detail=f"{name}: {old} -> {new}", source="openupgrade:apriori",
                                      source_ref=source_ref))
    return changes


def keep_xmlid(c: Change, removed_models: set[str]) -> bool:
    """Records that break a port: views, groups, actions... and data records of a model that is gone
    (e.g. uom.product_uom_categ_kgm when uom.category is removed: env.ref() in code fails)."""
    return c.kind != "xmlid" or c.model.startswith(XMLID_MODELS) or (c.change == "removed" and c.model in removed_models)


def collect(version_dir: Path, to_version: str) -> list[Change]:
    try:
        sha = subprocess.run(["git", "-C", str(version_dir), "rev-parse", "--short", "HEAD"],
                             capture_output=True, text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        sha = "unknown"
    base = version_dir / "openupgrade_scripts"
    ref = lambda p: f"OpenUpgrade@{sha}:{p.relative_to(version_dir)}"  # noqa: E731
    changes = []
    if (apriori := base / "apriori.py").exists():
        changes += parse_apriori(apriori.read_text(encoding="utf-8"), to_version, ref(apriori))
    for mod_dir in sorted(p for p in (base / "scripts").iterdir() if p.is_dir()):
        for ver_dir in sorted(p for p in mod_dir.iterdir() if p.is_dir() and p.name.startswith(to_version)):
            analysis = ver_dir / "upgrade_analysis_work.txt"
            if not analysis.exists():
                analysis = ver_dir / "upgrade_analysis.txt"
            if analysis.exists():
                changes += parse_analysis(analysis.read_text(encoding="utf-8", errors="replace"), to_version,
                                          ref(analysis))
            if (pre := ver_dir / "pre-migration.py").exists():
                changes += parse_pre_migration(pre.read_text(encoding="utf-8", errors="replace"), mod_dir.name,
                                               to_version, ref(pre))
    removed_models = {c.model for c in changes if c.kind == "model" and c.change == "removed"}
    return [c for c in changes if keep_xmlid(c, removed_models)]


KIND_ORDER = {"module": 0, "model": 1, "field": 2, "xmlid": 3}


def line(c: Change) -> str:
    """One grep-friendly line per change: the name is always written in full (model.field, module.xmlid)."""
    if c.kind == "field":
        name = f"{c.model}.{c.name}"
    elif c.kind == "xmlid":
        name = c.name if "." in c.name else f"{c.module}.{c.name}"
    else:
        name = c.name
    text = f"- `{name}`"
    if c.field_type:
        text += f" ({c.field_type})"
    text += f": {c.change}"
    if c.new_name:
        text += f" → `{c.new_name}`"
    if c.detail and c.detail != c.change:
        text += f" — {c.detail}"
    if c.note:
        text += f" ({c.note})"
    return text


def render(to_version: str, changes: list[Change], sha_note: str) -> str:
    """The Markdown file of one version step, grouped by module, then by kind."""
    from_version = f"{int(float(to_version)) - 1}.0"
    title = f"Cambi da Odoo {from_version} a {to_version} (Community)"
    generated = (f"Generato da `build_ontology.py` dalle analisi di OCA/OpenUpgrade {to_version} ({sha_note}): "
                 "non modificare a mano, si rigenera.")
    # an OKF concept, like every Markdown file of the pack
    meta = {"type": "Ontology", "title": title, "description": generated,
            "tags": [f"{from_version}-{to_version}", "ontology"]}
    out = ["---"] + [f"{key}: {json.dumps(value, ensure_ascii=False)}" for key, value in meta.items()] + ["---", "",
           f"# {title}", "", generated,
           "Una riga per cambio, con il nome completo (`modello.campo`, `modulo.xmlid`): cercare con `rg`.", ""]
    removed_models = {c.model for c in changes if c.kind == "model" and c.change == "removed"}
    by_module: dict[str, list[Change]] = {}
    for c in changes:
        by_module.setdefault(c.module or "(generale)", []).append(c)
    for module in sorted(by_module):
        out += [f"## {module}", ""]
        rows = sorted(by_module[module], key=lambda c: (KIND_ORDER.get(c.kind, 9), c.model or "", c.name))
        # Data records of a model that is gone (e.g. every account.tax.template of a localisation) are summarised
        # with their count: listing each one would bury the changes that matter.
        gone: dict[str, int] = {}
        lines: list[str] = []
        for c in rows:
            if (c.kind == "xmlid" and c.change == "removed" and c.model in removed_models
                    and not c.model.startswith(XMLID_MODELS)):
                gone[c.model] = gone.get(c.model, 0) + 1
                continue
            text = line(c)
            if text not in lines:
                lines.append(text)
        lines += [f"- {n} record di `{m}` rimossi insieme al modello" for m, n in sorted(gone.items())]
        out += lines
        out.append("")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="Write the version-changes ontology from OpenUpgrade into Markdown.")
    mirrors = Path(os.environ.get("TEXO_SHARED_DIR", "~/.local/share/texo")).expanduser() / "mirrors"
    ap.add_argument("--root", default=str(mirrors),
                    help="directory with one OpenUpgrade checkout per version: <NN>.0 or openupgrade-<NN> "
                         "(default: the mirrors of the threads)")
    ap.add_argument("--versions", nargs="+", default=["17.0", "18.0", "19.0"])
    ap.add_argument("--out", default=".texo/ontology", help="where to write <from>-<to>.md")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    for v in args.versions:
        version_dir = Path(args.root) / v
        if not version_dir.is_dir():
            version_dir = Path(args.root) / f"openupgrade-{v.split('.')[0]}"
        if not (version_dir / "openupgrade_scripts").is_dir():
            print(f"{v}: no OpenUpgrade checkout in {version_dir}, skipped", file=sys.stderr)
            continue
        changes = collect(version_dir, v)
        counts: dict[str, int] = {}
        for c in changes:
            counts[f"{c.kind}:{c.change}"] = counts.get(f"{c.kind}:{c.change}", 0) + 1
        print(f"{v}: {len(changes)} changes " + ", ".join(f"{k} {n}" for k, n in sorted(counts.items())))
        if args.dry_run:
            continue
        sha = changes[0].source_ref.split(":")[0] if changes and changes[0].source_ref else "OpenUpgrade"
        target = Path(args.out) / f"{int(float(v)) - 1}.0-{v}.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render(v, changes, sha), encoding="utf-8")
        print(f"  -> {target}")


if __name__ == "__main__":
    main()
