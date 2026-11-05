---
name: studio-guida
description: >-
  How an engineering and architecture firm works with this pack: the professional decides and signs, commissions and their documents, AI use and data, and the reading map of glossary, BIM, public contracts, site safety and playbooks. Use it for a commission, a tender, works accounting, BIM, safety coordination. Triggers: "commessa", "gara", "SAL", "BIM", "CSE", "PSC", "progetto esecutivo".
---

# studio-guida

The way of working of the pack studio_progettazione. The rules every session of the organisation must follow arrive from the hub
(the seed of this pack made them rules of the organisation): this skill adds how to work and what to read. The
files named below are in `references/` next to this file.

## The professional decides, signs and sends

- The agent prepares, checks and proposes; the responsible professional decides, signs and sends. Never sign,
  stamp, file or send anything to a public body, a client or a contractor.
- A calculation, a structural, energy or acoustic check and a safety judgement written by the agent are proposals
  until the responsible professional has verified them.
- A requirement taken from a code, a decree or a technical standard is cited with act, article and the day the
  text in force was read. A rule recalled from memory is not a source; if the text cannot be read, say so.

## A commission and its documents

- Models, drawings and reports stay in the archive or in the common data environment. The memory keeps their
  reference (container, discipline, revision, state) and what the archive does not have: why, who decided, what
  was learned, what the AI produced.
- A decision of a commission is written as a note that cites the document and the revision it comes from; a newer
  decision supersedes it, nothing is deleted.
- Versions and revisions of documents, the phase of the design, the permits obtained and the deadlines of the
  contract are facts of the commission in the hub.
- The documents a client or a public body sends are documents of the memory with their summary; their text is
  kept only when the commission allows it.

## AI and data

- Every output of an AI system that reaches a drawing, a calculation, a script or a communication outside the
  studio is recorded in the AI register of the commission with who verified it (`references/playbooks/registro-decisioni-e-ai.md`):
  the use of AI is instrumental and the intellectual work stays the professional's, and the client is informed of
  the systems used (`references/reference/compliance-ai.md`).
- Personal data of private clients, of people on site and of the people of contractors live only in the hub, on
  the commission, and only as much as the commission needs; special categories (health, disability for the
  accessibility of a home) never enter the memory.
- Data of a commission never leave it: what the studio learns becomes a lesson without the client.
- The memory and the registers serve the commission, never to evaluate the people who work in the studio.

## Mappa di lettura

> Le regole del settore sono sopra e nel hub. Prima di un lavoro si legge il file della riga, poi si cercano le
> lesson del hub sull'argomento (`texo search "<parole>" --scope lessons`, con i termini del glossario).

### Per lavoro

| Lavoro | Leggi |
|---|---|
| Aprire una commessa | `references/playbooks/apertura-commessa.md` |
| Scrivere una decisione, registrare un output dell'AI | `references/playbooks/registro-decisioni-e-ai.md` |
| Direzione dei lavori: SAL, contabilità, riserve | `references/playbooks/sal-e-contabilita-lavori.md`, `references/reference/contratti-pubblici.md` |
| Gara o incarico pubblico: procedure, livelli di progettazione, corrispettivi | `references/reference/contratti-pubblici.md` |
| Coordinamento della sicurezza, PSC, fascicolo | `references/reference/sicurezza-cantieri.md` |
| Modelli, capitolato informativo, pGI, CDE | `references/reference/gestione-informativa-bim.md` |
| Gemello digitale, modello in esercizio | `references/reference/gemello-digitale.md`, `references/reference/compliance-ai.md` |
| Uso dell'AI, informativa al committente, dati personali | `references/reference/compliance-ai.md` |
| Una sigla o un termine del settore, i sinonimi per cercare | `references/reference/glossario.md` |

### Fonti

- Le norme si leggono dal filo `normativa` della cartella di lavoro (`.texo/THREADS.md`): si cita l'atto, l'articolo e la data
  di lettura del testo vigente. Le date e le soglie scritte nei reference valgono alla data di lettura indicata.
- Modelli ed elaborati si leggono dal filo `progettazione` o `documenti`, se la cartella di lavoro li monta; altrimenti la
  persona li indica.

### Skill

Le skill del core: `texo-sessione` all'inizio e alla fine di ogni lavoro, `memoria-ingestione` per i documenti di
una commessa, `memoria-consolidamento` per la revisione della memoria, `memoria-fonti` per i bandi e le novità
normative che lo studio segue.
