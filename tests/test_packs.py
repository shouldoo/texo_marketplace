"""Every pack of the marketplace against the contract of the texo CLI and the rules of the hub (no hub needed).

The core is the folder named by TEXO_CORE, or the checkout CI puts in .core/.

    TEXO_CORE=<core> python3 -m unittest discover -s tests
"""
import json
import os
import re
import sys
import tomllib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORE = Path(os.environ.get("TEXO_CORE") or ROOT / ".core")
sys.path.insert(0, str(CORE))
from texo import mount, packs, threads  # noqa: E402

CODE = re.compile(r"^[a-z][a-z0-9_]*$")
SKILL_NAME = re.compile(r"^[a-z][a-z0-9-]*$")
HUB_ACTIVITIES = {"analysis", "communication"}
HUB_SECTIONS = {"profile", "operations", "compliance", "sector", "offer"}
SEED_TABLES = {"lang", "activities", "sections", "rules", "project_templates"}
PACK_ENTRIES = {"pack.toml", "seed.toml", "README.md", ".claude-plugin", "skills", "scripts", "demo", "tests"}
LINK = re.compile(r"`(references/[^`]+\.md)`|\]\((references/[^)]+\.md)\)")
PACKS = sorted(p for p in (ROOT / "packs").iterdir() if p.is_dir())
# The state of a law is a fact of the hub of each organisation, never text of a pack: no article, no numbered act, no
# date of an act, no term, amount or percentage. The deltas of a software version are the exception (a version does
# not change after its release).
MONTHS = "gennaio|febbraio|marzo|aprile|maggio|giugno|luglio|agosto|settembre|ottobre|novembre|dicembre"
NUMBER_WORDS = "due|tre|quattro|cinque|sei|sette|otto|nove|dieci|quindici|venti|trenta|quarantacinque|sessanta|novanta"
LAW = [re.compile(p, re.I) for p in (
    r"\bartt?\.\s*\d", r"\barticol[oi]\s+\d", r"\bcomm[ai]\s+\d", r"\ballegat[oi]\s+[IVXL]+\b",
    r"\b(?:d\.\s?lgs|d\.\s?p\.\s?r|d\.\s?m|d\.\s?l|l)\.?\s*(?:n\.\s*)?\d+\s*/\s*\d{2,4}\b",
    r"\bn\.\s*\d+\b", r"\b(?:19|20)\d{2}/\d+\b", r"\b\d+/(?:19|20)\d{2}\b",
    rf"\b\d{{1,2}}\s+(?:{MONTHS})\s+(?:19|20)\d{{2}}\b",
    rf"\b(?:\d+|{NUMBER_WORDS})\s+(?:giorni|settimane|mesi|anni)\b",
    r"€\s*\d|\b\d[\d.,]*\s*(?:euro|€)", r"\b\d+(?:,\d+)?\s*%",
)]
SOFTWARE_DELTAS = re.compile(r"/references/reference/v\d+/")


def frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    keys = {}
    for line in text[4:end].splitlines():
        if (m := re.match(r"([A-Za-z_-]+):\s*(.*)", line)):
            keys[m.group(1)] = m.group(2)
    return keys


class PacksTest(unittest.TestCase):

    def test_the_marketplace_lists_every_pack_at_its_version(self):
        listed = {p["name"]: p for p in json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())["plugins"]}
        self.assertEqual(sorted(listed), [p.name for p in PACKS])
        for pack in PACKS:
            plugin = json.loads((pack / ".claude-plugin" / "plugin.json").read_text())
            info = tomllib.loads((pack / "pack.toml").read_text())["pack"]
            self.assertEqual(listed[pack.name]["source"], f"./packs/{pack.name}")
            self.assertEqual((plugin["name"], info["name"]), (pack.name, pack.name))
            self.assertEqual(mount.version_tuple(info["version"]), mount.version_tuple(plugin["version"]), pack.name)
            self.assertEqual(listed[pack.name]["version"], plugin["version"], pack.name)

    def test_every_pack_fits_the_core_and_keeps_its_layout(self):
        for pack in PACKS:
            info = tomllib.loads((pack / "pack.toml").read_text())["pack"]
            self.assertRegex(pack.name, CODE)
            self.assertTrue(mount.satisfies(mount.__version__, info["core"]), f"{pack.name}: core {info['core']}")
            for folder in info.get("work_dirs") or []:
                self.assertNotIn("..", Path(folder).parts)
            unexpected = {e.name for e in pack.iterdir()} - PACK_ENTRIES
            self.assertEqual(unexpected, set(), pack.name)
            self.assertTrue((pack / "README.md").read_text().count("## Changelog") == 1, pack.name)

    def test_the_suggested_threads_are_valid(self):
        for pack in PACKS:
            for thread in tomllib.loads((pack / "pack.toml").read_text()).get("suggested_thread") or []:
                self.assertTrue(thread.get("id") and thread.get("why"), pack.name)
                if thread.get("driver"):
                    errors = [m for level, m in threads.check(thread) if level == "error"]
                    self.assertEqual(errors, [], f"{pack.name}: {thread['id']}")
                else:
                    self.assertIn(thread["type"], threads.TYPES, f"{pack.name}: {thread['id']}")
                    self.assertIn(thread["data_class"], threads.DATA_CLASSES, f"{pack.name}: {thread['id']}")

    def test_the_threads_a_pack_carries_are_public_sources_at_a_pinned_ref(self):
        for pack in PACKS:
            for thread in tomllib.loads((pack / "pack.toml").read_text()).get("thread") or []:
                thread = dict(thread, origin=f"pack {pack.name}")
                errors = [m for level, m in threads.check(thread) + packs.thread_problems(thread) if level == "error"]
                self.assertEqual(errors, [], f"{pack.name}: {thread['id']}")
                self.assertRegex(thread["ref"], r"^[0-9a-f]{40}$|^v?\d", f"{pack.name}: {thread['id']} is pinned")

    def test_every_seed_follows_the_rules_of_the_hub(self):
        for pack in PACKS:
            seed = tomllib.loads((pack / "seed.toml").read_text())
            self.assertLessEqual(set(seed), SEED_TABLES, pack.name)
            for table, key in (("activities", "code"), ("sections", "code"), ("rules", "key"),
                               ("project_templates", "key")):
                keys = [item[key] for item in seed.get(table, [])]
                self.assertEqual(len(keys), len(set(keys)), f"{pack.name}: {table}")
                for value in keys:
                    self.assertRegex(value, CODE, f"{pack.name}: {table}")
            activities = HUB_ACTIVITIES | {a["code"] for a in seed.get("activities", [])}
            sections = HUB_SECTIONS | {s["code"] for s in seed.get("sections", [])}
            for rule in seed.get("rules", []):
                self.assertIn(rule.get("severity", "must"), ("never", "must", "prefer"), rule["key"])
                self.assertLessEqual(set(rule.get("activities", [])), activities, rule["key"])
                self.assertIn(rule.get("section", "operations"), sections, rule["key"])
                self.assertTrue(rule["body"].strip() and len(rule["name"]) <= 200, rule["key"])
            for template in seed.get("project_templates", []):
                self.assertTrue(template["tasks"] and all(t["name"].strip() for t in template["tasks"]))

    def test_a_pack_holds_method_not_the_state_of_a_law(self):
        for pack in PACKS:
            for path in [pack / "seed.toml", *sorted((pack / "skills").rglob("*.md"))]:
                if SOFTWARE_DELTAS.search(path.as_posix()):
                    continue
                text = re.sub(r"```.*?```", "", path.read_text(), flags=re.S)
                for number, line in enumerate(text.splitlines(), 1):
                    hits = [p.pattern for p in LAW if p.search(line)]
                    self.assertEqual(hits, [], f"{path.relative_to(ROOT)}:{number}: {line.strip()[:120]}")

    def test_a_skill_never_restates_a_rule_of_the_seed(self):
        def grams(text, size=7):
            words = re.findall(r"[a-zà-ù0-9']+", text.lower())
            return {tuple(words[i:i + size]) for i in range(len(words) - size + 1)}
        for pack in PACKS:
            rules = tomllib.loads((pack / "seed.toml").read_text()).get("rules") or []
            for skill in sorted((pack / "skills").rglob("*.md")):
                text = grams(skill.read_text())
                for rule in rules:
                    shared = grams(rule["body"]) & text
                    self.assertFalse(shared, f"{skill.relative_to(ROOT)} restates the rule {rule['key']}: "
                                             f"{' '.join(next(iter(shared))) if shared else ''}")

    def test_every_skill_is_portable_and_its_references_exist(self):
        for pack in PACKS:
            skills = sorted((pack / "skills").iterdir())
            self.assertTrue(any(s.name.endswith("-guida") for s in skills), f"{pack.name}: a guide skill")
            for skill in skills:
                text = (skill / "SKILL.md").read_text()
                keys = frontmatter(text)
                self.assertIsNotNone(keys, skill)
                self.assertEqual(set(keys), {"name", "description"}, skill)
                self.assertEqual(keys["name"], skill.name)
                self.assertRegex(skill.name, SKILL_NAME)
                for match in LINK.finditer(text):
                    target = skill / (match.group(1) or match.group(2))
                    self.assertTrue(target.is_file(), f"{skill.name}: {target.relative_to(pack)}")


if __name__ == "__main__":
    unittest.main()
