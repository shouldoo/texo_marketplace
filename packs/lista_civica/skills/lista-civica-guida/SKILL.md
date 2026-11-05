---
name: lista-civica-guida
description: >-
  How a civic list works with this pack, politically neutral: positions, quotes and facts, personal data, the rules of the campaign in drafts, signatures, candidacies and spending, and the reading map of the method references and playbooks. Use it for campaign work of a civic list. Triggers: "lista civica", "campagna elettorale", "raccolta firme", "candidature", "par condicio", "silenzio elettorale", "spese elettorali".
---

# lista-civica-guida

The way of working of the pack lista_civica. The rules every session of the organisation must follow arrive from the hub
(the seed of this pack made them rules of the organisation): this skill adds how to work and what to read. The
files named below are in `references/` next to this file.

## Positions, quotes and facts

- Never invent a position, a statement, a quote or an event of a real person, party, list or body. A quote goes in
  «» only as the person gives it, word for word; a quote still to come is marked `[citazione da confermare]`.
- A fact about others (a vote, an act, a statement, a figure) is written only with its public source and its date: a
  card of the external sources, an act, a document of the memory. What others claim is attributed, never presented as
  a fact.
- A private person is never named in a text meant to go out; a public person only in their public role.
- The agent drafts; it never publishes, sends, posts, e-mails or schedules anything addressed to the press, to the
  social accounts, to the voters or to other lists. A person does, after reading the draft.

## Personal data

- The data of voters, supporters, signatories, volunteers and donors live only in the hub, with its permissions:
  never in git, in a document of the working folder, in a chat or in a prompt sent to a thread of class `public`.
- A political opinion is a special category of personal data (Regolamento UE 2016/679, art. 9, as recalled by the
  provision of the Garante of 18 April 2019, § 2): the list of who supports the list or signed for it is one.
  Contacts collected at an initiative (a petition, a stall, a signature collection) are used for propaganda only with
  the consent or the basis the Garante describes (`references/reference/privacy-propaganda.md`).
- The registers of the population and the lists already used at the polling stations are never a source of contacts
  (Garante 2019, § 5).

## The rules of the campaign in drafts

Drafts follow the acts the pack has read (`references/reference/`): the silence of the day before and of the voting days
(L. 4 aprile 1956, n. 212, art. 9), the posters only in the spaces of the municipality (L. 212/1956, art. 1), the
name of the client responsible on every piece of propaganda (L. 10 dicembre 1993, n. 515, art. 3, comma 2), no poll
results in the fifteen days before the vote (L. 22 febbraio 2000, n. 28, art. 8). Dates, thresholds and limits that
depend on the round or on the size of the municipality are checked on the acts of that round, and said when they are
not.

## Signatures, candidacies and spending

- Signatures and candidacy forms follow the instructions the Ministry of the Interior publishes for the round and the
  laws they recall: `references/playbooks/raccolta-firme-e-candidature.md`. A figure from memory is never enough.
- Every expense and every contribution of the campaign is recorded in the hub as a fact with its document (invoice,
  receipt, statement), so the statement of the spending can be written from the memory
  (`references/reference/spese-elettorali.md`).

## Mappa di lettura

> Prima le regole: quelle del core e del hub, poi questa skill. Le norme si leggono sul filo `normativa`
> della cartella di lavoro e si citano per atto e articolo; ciò che dipende dalla tornata si verifica sugli atti di quell'anno.

### Per lavoro

| Lavoro | Leggi | Attività del hub |
|---|---|---|
| Firme, candidature, consegna delle liste | `references/playbooks/raccolta-firme-e-candidature.md`, `references/reference/candidature-e-firme.md` | `election` |
| Manifesti, volantini, silenzio elettorale | `references/reference/propaganda-e-silenzio-elettorale.md` | `campaign`, `press` |
| Stampa, emittenti locali, sondaggi, social | `references/reference/par-condicio.md` | `press` |
| Un comunicato stampa | skill `comunicato-stampa` | `press`, `communication` |
| Rassegna stampa e fonti esterne | `references/playbooks/rassegna-stampa-e-schede.md`, skill del core `memoria-fonti` | `press` |
| Eventi, banchetti, volontari | `references/playbooks/evento-o-banchetto.md` | `campaign` |
| Spese, contributi, mandatario, rendiconto | `references/reference/spese-elettorali.md` | `election` |
| Contatti di elettori, sostenitori, firmatari | `references/reference/privacy-propaganda.md` | tutte |
| Il programma e i gruppi tematici | i fatti e le procedure della lista nel hub, sezione `sector` | `programme` |

### Fuori da questo pack

- Le decisioni, le posizioni, il programma e le persone della lista: nel suo hub, mai in git.
- Le norme regionali e i regolamenti comunali (suolo pubblico, affissioni, consiglio comunale): fatti della lista con
  la loro fonte, perché cambiano da un comune all'altro.
