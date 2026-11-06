---
name: ets-guida
description: >-
  How a third sector organisation (ETS: APS, ODV) works with this pack: the rules for the people served, members and volunteers, funding and reporting, the registry, and the reading map of the method references and playbooks. Use it for calls, reports, RUNTS duties, volunteers, financial statements of an ETS. Triggers: "bando", "rendicontazione", "RUNTS", "bilancio ETS", "volontari", "5 per mille".
---

# ets-guida

The way of working of the pack ets. The rules every session of the organisation must follow arrive from the hub
(the seed of this pack made them rules of the organisation): this skill adds how to work and what to read. The
files named below are in `references/` next to this file.

## The people served

- Never write data about the people the organisation serves (people helped, hosted, assisted, their families)
  in the memory, in git, in a commit, in a conversation or in a document you draft: not their names, stories,
  situations or contacts, not even an invented example. The work is described by activities, numbers and
  outcomes, never by persons.
- The address of a protected facility (a shelter, a safe house) is never written anywhere: not in the memory,
  not in a project, not in a text for the public.
- A document that concerns a person served is never read or brought into the memory; if one reaches you, stop
  and say so.
- Communication about the services (a report, a post, a press release, a call for volunteers) never makes a
  person recognisable, directly or by the combination of details.

## Members, volunteers, staff

- Personal data of members, volunteers and staff live only in the hub, on the records Odoo protects with its
  permissions, never in git or in a text you draft for others.
- What the law requires of them (the register of volunteers, their insurance, the reimbursement of expenses) is
  a procedure of the organisation in the hub; the reference says what the law requires.

## Funding and reporting

- The rules of a funder (eligible costs, co-financing, deadlines, reporting format, publicity obligations) are
  facts of the project they fund, taken from the call or the agreement and citing it.
- The deadlines of the registry and of each grant are tasks or facts of the hub with their date; never rely on
  remembering them.
- Figures in an application or a report come from the accounting and the documents of the organisation, never
  estimated or rounded to fit; a missing figure is asked to the person.
- An application or a report is submitted by the person, never by the agent.

## The law

- An answer on an obligation cites the act and the article read in the thread `normativa`, in force on the day;
  a reference of this pack is a map, not a substitute for the text.
- What a reference marks «da verificare sul testo vigente» is checked on the text before relying on it.

## Mappa di lettura

> Nessun file è precaricato: si legge quello che il compito tocca. I percorsi sono relativi a questo pack
> (`$(texo where --pack ets)` dalla cartella di lavoro). Prima di rispondere su un obbligo: il reference, poi l'articolo
> vigente nel filo `normativa`, poi le lezioni del hub con lo stesso tag.

### Per compito

| Compito | Reference | Playbook |
|---|---|---|
| Registro unico nazionale: iscrizione, depositi, variazioni, PEC | `references/reference/runts.md` | `references/playbooks/adempimenti-runts-annuali.md` |
| Bilancio o rendiconto per cassa, relazione di missione, libri sociali | `references/reference/bilancio-e-rendiconto.md` | `references/playbooks/adempimenti-runts-annuali.md` |
| Volontari, associati, lavoratori, rimborsi, assicurazione | `references/reference/volontari-e-associati.md` | — |
| Un avviso, una domanda di finanziamento | `references/reference/bandi-e-rendicontazione.md` | `references/playbooks/domanda-di-finanziamento.md` |
| La rendicontazione di un progetto finanziato | `references/reference/bandi-e-rendicontazione.md` | `references/playbooks/rendicontazione-di-un-progetto.md` |
| Pubblicazioni sul sito, dati delle persone servite | `references/reference/trasparenza-e-dati.md` | — |

### Fonti che non sono qui

| Fonte | Dove |
|---|---|
| I testi delle leggi e dei decreti in vigore | il filo `normativa` dell'organizzazione |
| Gli avvisi che l'organizzazione segue | il filo `bandi` e le fonti esterne del hub |
| Statuto, verbali, domande, rendiconti dell'organizzazione | il filo `documenti` e i documenti della memoria |
| Scadenze, cariche, soglie dell'ente | i fatti e i task del hub |

### Skill

questo pack non ha skill proprie: valgono quelle del core (`texo-sessione`, `memoria-consolidamento`,
`memoria-ingestione`, `memoria-fonti`).
