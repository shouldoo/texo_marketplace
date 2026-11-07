# lista_civica

A Texo skill pack. Civic lists, politically neutral: positions and facts, personal data, campaign rules in drafts, signatures and candidacies, spending, method references, the skill comunicato-stampa, the hub seed of the sector.

| Part | What |
|---|---|
| Skills | `comunicato-stampa`, `lista-civica-guida` |
| Seed (`seed.toml`) | activities `campaign`, `press`, `programme`, `election`; sections none; 6 rules of the organisation; templates: Campagna per le comunali (template), Raccolta firme (template) |
| Suggested threads | `normativa`, `rassegna`, `social` |
| Working folders | none |
| `demo/` | «Terni 2027», an invented civic list with its press review (the cards of `texo_sources`), and its question sets (A, B, the 30 questions of a person, the questions on the external sources), loaded by `<core>/setup/load-demo.sh lista_civica scenario-lista [--create]` into a test database whose hub has `texo_sources` and `texo_sources_vector` |

The rules that must always hold arrive in the hub through the seed; the guide skill holds how to work and the reading
map, with its references in `skills/*-guida/references/`.

## Changelog

### v1.3.1

- The code questions of the demo (`demo/questions-codici.json`, 22 questions): each is only a rare
  act number or acronym of the demo, the expected records those whose text holds it. They measure what only
  the words find, which no other set asked; the act numbers in the titles need texo_hub 20.0.1.8.0 or later.

### v1.3.0

- The demo of the pack: «Terni 2027», the civic list of the scenario S3 of the measures of the memory, as its curated layer (a searchable session note on every task, keywords, summaries) with the verified public facts, the public acts converted with Docling (`demo/texts/`), 45 press and video cards as cards of the external sources (`SOURCES`, read by the loader of the core from v2.3.0) and the four question sets in one file (`demo/questions.json`, a `set` key per question), so the search of the memory can be measured on it with `eval_memoria.py`.

### v1.2.0

- Method only: the references and playbooks say which kind of source to read, which questions to answer there and
  which fact or task to write in the hub; no article, numbered act, summary of a provision, term or threshold.
- The skills no longer restate the rules of the seed: they send the agent to the rules of the hub (`texo rules`,
  the context pack), which its leads may change.

### v1.1.0

- Italian, as everything an agent reads: the skills (their descriptions too), the references, the texts of the seed
  (`lang = "it_IT"`) and the guides of the threads.

### v1.0.0

- First release.
