# AGENTS.md — Texo marketplace

Rules for any AI assistant that edits this repository: the skill packs of the sectors, installed by the `texo` CLI
and as Claude Code plugins.

- **Method only.** A pack says how to work: for a matter, which kind of act or document to read in the threads of
  the organisation (its `normativa` thread, the call of a funder, the instructions of a ministry for an election),
  which questions to answer there, and which fact, procedure or task the organisation writes in its hub (with the
  article it read, the date of the check and an expiry). The state of a law never stands here: no article or
  paragraph number, no numbered or dated act, no summary of what a provision prescribes, no term, threshold, amount or
  percentage. A reform then changes the facts of each hub, never a pack. The deltas of a software version are the
  exception (a version does not change after its release). The check `test_a_pack_holds_method_not_the_state_of_a_law`
  enforces it.
- **No names.** No organisation, customer, person, place, outlet or record that exists: examples are generic or
  invented. No specific source or provider is named as a thread: a pack suggests the kind of thread, the
  organisation chooses the provider.
- **Every pack is self-contained.** `packs/<name>/` holds `pack.toml`, `.claude-plugin/plugin.json`, `seed.toml`,
  `skills/` (each skill with its `references/`), and for some packs `scripts/`, `demo/`, `tests/`. A pack never reads
  a file of another pack.
- **Rules that must always hold go in the seed** (`seed.toml`, rules of the organisation in the hub, which its leads
  may change or supersede); a skill holds how to work and the reading map, and sends the agent to the rules of the
  hub (`texo rules`, the context pack) instead of restating them. The same rule never stands in both: the check
  `test_a_skill_never_restates_a_rule_of_the_seed` catches a copied rule, a paraphrase is caught in review.
- **The context of an organisation lives in its hub.** Its conventions, procedures and facts are notes of its hub,
  never files of its working folder that a pack would read.
- **Skills are portable.** Frontmatter `name` (the folder) and `description` only; actions named by what they do,
  never by one assistant's tool names; the texo CLI is `texo`, the core is `<core>` (`texo where`).
- **Language.** What an agent reads at work is Italian: `SKILL.md` (its `description` too, with the requests a
  person types), references, playbooks, the texts of `seed.toml` (`lang = "it_IT"`) and the `why` and `guide` of the
  threads. Code, comments, commit messages, pull requests, READMEs and this file are English. One file, one language.
- **Versions.** A change bumps `version` in `pack.toml` and in `plugin.json` together (and in
  `.claude-plugin/marketplace.json`), with a line in the changelog of the pack's README. A release is the tag
  `<name>-<version>`, after the checks are green.
- No commit or pull request names an AI assistant as author.
