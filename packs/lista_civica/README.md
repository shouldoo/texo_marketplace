# lista_civica

A Texo skill pack. Civic lists, politically neutral: positions and facts, personal data, campaign rules in drafts, signatures and candidacies, spending, method references, the skill comunicato-stampa, the hub seed of the sector.

| Part | What |
|---|---|
| Skills | `comunicato-stampa`, `lista-civica-guida` |
| Seed (`seed.toml`) | activities `campaign`, `press`, `programme`, `election`; sections none; 6 rules of the organisation; templates: Campagna per le comunali (template), Raccolta firme (template) |
| Suggested threads | `normativa`, `rassegna`, `social` |
| Working folders | none |

The rules that must always hold arrive in the hub through the seed; the guide skill holds how to work and the reading
map, with its references in `skills/*-guida/references/`.

## Changelog

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
