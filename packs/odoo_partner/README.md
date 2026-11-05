# odoo_partner

A Texo skill pack. Odoo Community partners: the way of working on Odoo projects, version deltas, conventions, playbooks, the skills odoo-progetto and browser-test, the hub seed of the sector and a demo.

| Part | What |
|---|---|
| Skills | `browser-test`, `odoo-partner-guida`, `odoo-progetto` |
| Seed (`seed.toml`) | activities `code`, `deploy`, `data`, `migration`; sections none; 6 rules of the organisation; templates: Odoo project (template), Odoo version migration (template) |
| Suggested threads | `odoo-skills`, `odoo-20`, `openupgrade-20` |
| Working folders | `progetti/`, `modules/V17/`, `modules/V18/`, `modules/V19/`, `modules/V20/`, `odoo/odoo-clients/` |
| `scripts/` | `anonymize-db.sh`, `anonymize-db.sql`, `build_ontology.py`, `neutralize-db.sh` (`$(texo where --pack odoo_partner)/scripts/`) |
| `demo/` | an invented organisation and its question set, loaded by `<core>/setup/load-demo.sh odoo_partner <database> [--create]` into a test database |

The rules that must always hold arrive in the hub through the seed; the guide skill holds how to work and the reading
map, with its references in `skills/*-guida/references/`.

## Changelog

### v1.0.1

- The v18 accounting delta names no commercial connector: the external transmission connectors in general.
- The question set of the demo has eleven paraphrases more, on facts, procedures, documents and tasks: the
  hybrid search is measurable against the lexical one (`demo/questions.json`).

### v1.0.0

- First release.
