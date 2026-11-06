---
name: odoo-partner-guida
description: >-
  How an Odoo partner works with this pack: the rules of the sector for code and instances, the reading map of the version deltas, conventions and playbooks, the threads of the upstream code. Use it when the work touches an Odoo Community project, a module, an instance, a migration. Triggers: "modulo Odoo", "progetto Odoo", "migrazione", "istanza locale", "Odoo 19", "Odoo 20", "OCA".
---

# odoo-partner-guida

The way of working of the pack odoo_partner. The rules every session of the organisation must follow arrive from the hub
(the seed of this pack made them rules of the organisation): this skill adds how to work and what to read. The
files named below are in `references/` next to this file.

## Before writing code

- Know the Odoo version of the instance: the description of the project, the manifest `version` prefix of its
  modules, or the person. Every reference and lesson is read for that version.
- Read the map (below) for the area you touch, then search the lessons of the hub for that area and version
  (`texo search "<words>" --scope lessons`, with the tags of the area). A delta of `references/reference/v<NN>/` holds only
  what changes in that version.
- Check every field, method, view and xmlid in the source of that version (the thread `odoo-<NN>`) or of the OCA
  module; for a change between versions, the ontology that `$(texo where --pack odoo_partner)/scripts/build_ontology.py`
  writes in `.texo/ontology/` from OpenUpgrade.
- Before creating a module, look for an existing one (OCA first) and say what you found.
- A dependency on a module is proposable only if the description of the project lists it as installed.
- Odoo core and the OCA repositories are third-party code: extend them by inheritance from a module of the
  project, never by editing them.

## While working

- Tests are mandatory after creating or changing a module: run its tests and add tests for what you changed, on
  a test database created for the task, with zero warnings in the log (`checklog-odoo`):
  `references/playbooks/test-modulo-locale.md`.
- Act on a database through `odoo shell` and the ORM; raw SQL only as a last resort, saying why.
- When you propose a change to a model, say what follows: restart, `-u <module>`, tests.
- No `print()` or debug logging in final code.
- A copy of a production database is neutralised before an instance starts on it, and anonymised for an
  organisation that serves vulnerable people (`$(texo where --pack odoo_partner)/scripts/neutralize-db.sh`, `$(texo where --pack odoo_partner)/scripts/anonymize-db.sh`).
- Production is never a test target: stage first, then the customer's acceptance, then production through the
  release of the project.

## What the memory keeps for this sector

- The installed modules, the version, the environments and the release flow of a project are facts of the
  project in the hub, not files of the working folder.
- What a project learned about Odoo becomes a lesson of the hub, tagged with the area and the version, without
  the customer. A lesson that proves true on several projects is proposed to this pack as a reference delta,
  rewritten and checked against the public source, through a reviewed pull request.

## Mappa di lettura

> Nessun file di questo pack è precaricato: si legge quello che il compito tocca. I percorsi sono
> relativi a questo pack (`$(texo where --pack odoo_partner)` dalla cartella di lavoro). Regola: prima di scrivere
> codice su un'area si leggono il delta della versione del progetto, le lesson del hub di quell'area e il
> codice upstream di quella versione.

### Prima di tutto

| Che cosa | Dove |
|---|---|
| Le convenzioni di codice e di lavoro su Odoo | `references/conventions/core-conventions.md` (quelle dell'organizzazione, in `references/conventions/` alla sua radice, vincono) |
| L'avvio e la chiusura del lavoro su un progetto | skill `texo-sessione` (core), poi skill `odoo-progetto` |
| La versione dell'istanza, gli ambienti, i moduli installati | la description del progetto nel hub (`texo project <id>`) |
| Il codice upstream della versione | il mirror del filo `odoo-<NN>` (`.texo/THREADS.md`): `rg`, mai la memoria |
| I moduli OCA in uso | i mirror dei fili `oca-<repo>`, dai `.gitmodules` dei progetti |

### Aree: delta per versione, lesson e codice

I reference di base delle aree non sono in questo pack: per ogni area valgono le lesson del hub con il
tag dell'area e della versione (`texo search "<parole>" --terms <sinonimi> --scope lessons
--applies-to <NN>.0`) e il codice della versione nel mirror del suo filo. I reference di base si
ricostruiscono qui nel tempo, dalle lesson verificate su fonti pubbliche (il codice di Odoo e di OCA).
I delta dicono che cosa cambia in una versione rispetto alla precedente.

| Area (modelli toccati) | Tag delle lesson | Odoo 18 | Odoo 19 | Odoo 20 |
|---|---|---|---|---|
| Modelli, ORM, campi, CRUD | `models` | `references/reference/v18/models.md` | `references/reference/v19/models.md` | `references/reference/v20/README.md` |
| Viste XML | `views` | `references/reference/v18/views.md` | `references/reference/v19/views.md` | `references/reference/v20/README.md` |
| Ereditarietà di modelli e viste | `inheritance` | — | `references/reference/v19/inheritance.md` | — |
| File dati XML/CSV | `data` | — | `references/reference/v19/data.md` | — |
| Wizard | `wizards` | — | `references/reference/v19/wizards.md` | — |
| Sicurezza: ACL, regole, gruppi | `security` | — | `references/reference/v19/security.md` | `references/reference/v20/README.md` |
| `__manifest__.py`, versioni, dipendenze | `manifest` | `references/reference/v18/manifest.md` | `references/reference/v19/manifest.md` | — |
| Magazzino, prodotti (`stock.*`, `product.*`) | `inventory` | `references/reference/v18/inventory.md` | `references/reference/v19/inventory.md` | — |
| Produzione (`mrp.*`) | `manufacturing` | `references/reference/v18/manufacturing.md` | `references/reference/v19/manufacturing.md` | — |
| Contabilità (`account.*`) | `accounting` | `references/reference/v18/accounting.md` | `references/reference/v19/accounting.md` | — |
| Vendite, CRM, acquisti, progetti, helpdesk, HR, controller, test, report, OWL, i18n, performance | il nome dell'area | — | — | — |

`references/reference/v20/README.md` dice che cosa è verificato su Odoo 20.0, gli strumenti (`upgrade_code`) e i cambi
di framework noti. Un nome di modello, campo o xmlid che può essere cambiato tra due versioni si controlla
nell'ontologia che `$(texo where --pack odoo_partner)/scripts/build_ontology.py` genera in locale dal filo `openupgrade`, in
`.texo/ontology/` dell'organizzazione: non è versionata qui.

### Operazioni

| Operazione | Dove |
|---|---|
| Prendere in carico un progetto (hub, repository, istanza locale) | `references/playbooks/onboard-progetto.md` |
| Testare un modulo sull'istanza locale, zero warning nel log | `references/playbooks/test-modulo-locale.md` |
| Portare un progetto a una nuova versione | `references/playbooks/migrazione-progetto.md` |
| Portare un modulo OCA a una nuova major | `references/playbooks/migrazione-modulo-oca.md` |
| Provare l'interfaccia di un'istanza locale o di uno stage abilitato | skill `browser-test` |
| Neutralizzare e anonimizzare una copia di un database | `$(texo where --pack odoo_partner)/scripts/neutralize-db.sh`, `$(texo where --pack odoo_partner)/scripts/anonymize-db.sh` |
| Un pattern riusato tra progetti diversi | `references/conventions/patterns/README.md` |

### Skill

| Skill | Da dove | Quando |
|---|---|---|
| `odoo-progetto` | questo pack | dopo `texo-sessione`, su ogni progetto Odoo |
| `browser-test` | questo pack | prova della UI dopo JavaScript, Owl, viste, azioni |
| `odoo-guidelines`, `odoo-web-guidelines`, `odoo-review`, `odoo-security`, `odoo-git` | le skill ufficiali di Odoo, dal filo `odoo-skills` che il pacchetto porta (mirror di `odoo/odoo`, cartella `skills/`), collegate da `texo mount` | scrittura e revisione di codice, sicurezza, git |
| `texo-sessione`, `memoria-consolidamento`, `memoria-ingestione`, `memoria-fonti` | il core | la sessione, la revisione della memoria, i documenti, le fonti |

Un assistente che non carica le skill da solo apre il `SKILL.md` quando il compito corrisponde.

### Fili suggeriti

| Filo | Tipo, driver | Che cosa |
|---|---|---|
| `odoo-<NN>` | source, `git-mirror` di `github.com/odoo/odoo` al ref della versione | il codice di Odoo Community di ogni versione dei progetti |
| `oca-<repo>` | source, `git-mirror` di `github.com/OCA/<repo>` | i repository OCA in uso, dai `.gitmodules` dei progetti |
| `openupgrade` | source, `git-mirror` di `github.com/OCA/OpenUpgrade` | facoltativo: le analisi dei cambi tra versioni, per l'ontologia e le migrazioni |

L'organizzazione li dichiara tra i fili del hub (Texo Threads) con il ref fissato; `texo mount` li monta,
`texo doctor` li controlla.

Il pacchetto porta il filo `odoo-skills` (`git-mirror` di `github.com/odoo/odoo`, cartella `skills/`, al commit che
la versione del pacchetto fissa): le skill ufficiali di Odoo arrivano con il pacchetto. Un filo del hub con lo stesso
id lo sostituisce, per esempio con un commit più recente.
