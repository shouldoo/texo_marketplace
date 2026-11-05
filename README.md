# texo_marketplace

Texo — workspace and memory for AI agents at work. This repository holds the **skill packs** of the sectors: what
every organisation of a sector shares, and nothing of any of them. The core (`texo_core`) installs them; the hub
(`texo_hub`) keeps which packs, at which version, each organisation uses.

| Pack | For | Skills |
|---|---|---|
| [`odoo_partner`](packs/odoo_partner/README.md) | organisations that develop and run Odoo Community projects | `odoo-partner-guida`, `odoo-progetto`, `browser-test` |
| [`ets`](packs/ets/README.md) | third sector organisations (APS, ODV) | `ets-guida` |
| [`studio_progettazione`](packs/studio_progettazione/README.md) | engineering and architecture firms | `studio-guida` |
| [`lista_civica`](packs/lista_civica/README.md) | civic lists, politically neutral | `lista-civica-guida`, `comunicato-stampa` |

## What a pack contains

```text
packs/<name>/
├── pack.toml                    name, version, the core it needs, working folders, suggested threads
├── .claude-plugin/plugin.json   the same pack as a Claude Code plugin
├── seed.toml                    the activities, sections, rules and project templates of the sector, for the hub
├── skills/<skill>/SKILL.md      the skills; the guide skill of the pack carries references/ (method, reading map)
└── scripts/, demo/, tests/      where the pack needs them
```

A pack carries **method only**: which act and article governs a matter, what to check and when, where to read it
(a thread of the organisation, for instance `normativa`) and which fact to write in the hub. The values of a law
(thresholds, amounts, deadlines) are facts of the hub of each organisation, verified with a date and an expiry, so
they never age silently here.

## Installing

With the texo CLI: an administrator lists the packs of the organisation in its hub (*Texo Skill Packs*, or the
route `admin/config`); `texo mount` in a working folder checks out `packs/<name>` at the tag `<name>-<version>` of
this repository, links its skills for every assistant, and `texo seed` brings its seed into the hub after a dry run.

As Claude Code plugins, without the hub:

```text
/plugin marketplace add shouldoo/texo_marketplace
/plugin install odoo_partner@texo_marketplace
```

## Releasing

A change bumps the version in `pack.toml`, `plugin.json` and `.claude-plugin/marketplace.json`, with a line in the
changelog of the pack's README. After the checks are green the release is the tag `<name>-<version>` (for instance
`ets-v1.1.0`); an organisation moves to it by changing the version in its hub.

The workflow `checks` runs, with `texo_core`: the layout and the manifests of every pack, the seed against the rules
of the hub, the skills, independence from any one assistant, isolation, the demo data, `ruff`, `shellcheck`,
gitleaks and attribution.

## Licence

The content (Markdown, seeds, data) is licensed CC BY-SA 4.0 (`LICENSE`); the scripts LGPL-3.0-or-later
(`LICENSE-LGPL-3.0`).
