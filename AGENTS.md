# AGENTS.md — Texo marketplace

Rules for any AI assistant that edits this repository: the skill packs of the sectors, installed by the `texo` CLI
and as Claude Code plugins.

- **Method only.** A pack says how to work and where to read: which act and article governs a matter, what to check,
  which fact the organisation writes in its hub. Thresholds, amounts, deadlines, percentages and tables of a law are
  never written here: they are facts of the hub of each organisation, with the article read, the date of the check
  and an expiry. The version deltas of a software (a version does not change after its release) are the exception.
- **No names.** No organisation, customer, person, place, outlet or record that exists: examples are generic or
  invented. No specific source or provider is named as a thread: a pack suggests the kind of thread, the
  organisation chooses the provider.
- **Every pack is self-contained.** `packs/<name>/` holds `pack.toml`, `.claude-plugin/plugin.json`, `seed.toml`,
  `skills/` (each skill with its `references/`), and for some packs `scripts/`, `demo/`, `tests/`. A pack never reads
  a file of another pack.
- **Rules that must always hold go in the seed** (`seed.toml`, rules of the organisation in the hub); a skill holds
  how to work and the reading map. The same rule never stands in both.
- **Skills are portable.** Frontmatter `name` (the folder) and `description` only; actions named by what they do,
  never by one assistant's tool names; the texo CLI is `texo`, the core is `<core>` (`texo where`).
- **Language.** What an agent reads at work is Italian: `SKILL.md` (its `description` too, with the requests a
  person types), references, playbooks, the texts of `seed.toml` (`lang = "it_IT"`) and the `why` and `guide` of the
  threads. Code, comments, commit messages, pull requests, READMEs and this file are English. One file, one language.
- **Versions.** A change bumps `version` in `pack.toml` and in `plugin.json` together (and in
  `.claude-plugin/marketplace.json`), with a line in the changelog of the pack's README. A release is the tag
  `<name>-<version>`, after the checks are green.
- No commit or pull request names an AI assistant as author.
