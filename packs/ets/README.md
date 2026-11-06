# ets

A Texo skill pack. Third sector organisations (ETS): the way of working with the people served, volunteers, funding, reporting and the registry, method references and playbooks, the hub seed of the sector and a demo.

| Part | What |
|---|---|
| Skills | `ets-guida` |
| Seed (`seed.toml`) | activities `funding`, `reporting`, `volunteers`, `services`; sections `governance`; 7 rules of the organisation; templates: Domanda di finanziamento (template), Progetto finanziato (template) |
| Suggested threads | `normativa`, `bandi`, `documenti` |
| Working folders | none |
| `demo/` | an invented association of the third sector («Ginestra APS») and its question sets, loaded by `<core>/setup/load-demo.sh ets <database> [--create]` into a test database |

The rules that must always hold arrive in the hub through the seed; the guide skill holds how to work and the reading
map, with its references in `skills/*-guida/references/`.

## Changelog

### v1.3.0

- The demo of the pack (`demo/`): «Ginestra APS», an invented association with a help desk against violence, a
  shelter house, a campaign, volunteering, the obligations towards the registry and its funders; the public acts
  and ministerial pages it reads (`demo/texts/`); its question sets (`demo/questions.json`: set A written knowing
  the data, set B written blind from the titles, the passages of the long acts), so the search of the memory is
  measured on it with `<core>/scripts/eval_memoria.py`. The demo is the curated layer of the scenario: the
  session note of every task with its keywords, the keywords of rules, facts, procedures, lessons and documents,
  the summaries of the documents.

### v1.2.0

- Method only: the references and playbooks say which kind of source to read, which questions to answer there and
  which fact or task to write in the hub; no article, numbered act, summary of a provision, term or threshold.
- The skills no longer restate the rules of the seed: they send the agent to the rules of the hub (`texo rules`,
  the context pack), which its leads may change.

### v1.1.0

- Italian, as everything an agent reads: the skills (their descriptions too), the references, the texts of the seed
  (`lang = "it_IT"`) and the guides of the threads.

### v1.0.1

- The reading map of the guide names the folder of the pack (`texo where --pack ets`).

### v1.0.0

- First release.
