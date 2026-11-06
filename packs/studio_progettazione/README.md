# studio_progettazione

A Texo skill pack. Engineering and architecture firms: the professional decides and signs, commissions and documents, BIM, public contracts, site safety, a glossary, method references and playbooks, the hub seed of the sector.

| Part | What |
|---|---|
| Skills | `studio-guida` |
| Seed (`seed.toml`) | activities `design`, `site`, `tender`, `bim`; sections none; 6 rules of the organisation; templates: Commessa (template), Gara pubblica (template) |
| Suggested threads | `normativa`, `progettazione`, `documenti` |
| Working folders | none |
| `demo/` | an invented engineering and architecture firm (Studio Tre Archi) with its question sets, loaded by `<core>/setup/load-demo.sh studio_progettazione <database> [--create]` into a test database |

The rules that must always hold arrive in the hub through the seed; the guide skill holds how to work and the reading
map, with its references in `skills/*-guida/references/`.

## Changelog

### v1.3.0

- The demo of the pack: «Studio Tre Archi», an invented engineering and architecture firm with five customers,
  their commissions, chatter full of acronyms, and sixteen public acts as documents (`demo/texts/`); the curated
  layer of the memory (searchable session notes with keywords, keywords of rules, facts, procedures, lessons and
  documents, summaries) merged in. Its three question sets in `demo/questions.json` (set A, the blind set B, the
  set on the passages of long acts), so the search of the memory is measurable on it with
  `<core>/scripts/eval_memoria.py`.

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
