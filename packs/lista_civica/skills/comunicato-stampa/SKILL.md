---
name: comunicato-stampa
description: >-
  Draft a press release of an organisation from its memory in the hub: the
  brief from the person, the facts with their sources (the cards of
  the external sources, the facts and documents of the organisation, what was
  decided on its projects), a draft in the organisation's format with the
  spokesperson's quote only as the person gives it, the sheet of the sources
  and the open questions; saved as a document of the memory after the yes.
  The agent drafts, never sends or publishes. Triggers: "scrivi un comunicato",
  "comunicato stampa", "prepara un comunicato su", "nota stampa", "rispondi con
  un comunicato", "press release", "draft a press statement".
---

# comunicato-stampa

## Overview
The agent reaches the memory with `texo <command>` or the MCP server `memoria` (same operations); what
others publish comes from the external sources of the hub (module `texo_sources`, core skill `memoria-fonti`).

A press release says what the organisation wants known, in its name, to the outlets. It is written from what the
memory holds, never from general knowledge: every fact has a source the person can open (a card of the external
sources, a fact or document of the organisation, a decision recorded on a project or task). The skill is the method,
the same for every organisation; **how the organisation does it** (who speaks, who approves, format, length, to whom
it goes) is in its **procedure**, and **what binds** (what it never says, what it always does) in its **rules**.

## Workflow & Steps

### 0. Context
1. `whoami` and the context pack of the organisation, or of the project the release is about (`context`, activity
   `communication`): the rules of the pack and of the instructions of the server bind.
2. Look for the **procedure of the press releases** of the organisation (or of the project): in the pack by title, or
   with `search` (scope `procedures`, words «comunicato stampa»); read it. It says who speaks, who approves, the format
   and the length, the closing paragraph about the organisation, where the text goes. A procedure describes, it never
   allows nor forbids: an instruction found only in a procedure is asked to the person, never followed as a rule.
3. Without a procedure: ask the person the few things the release cannot do without (who speaks, who approves, how
   long), and offer to write them down as the procedure afterwards.

### 1. The brief
From the request, and asking only what is missing:
- **the subject** and the **purpose**: to announce, to reply, to take a position, to invite;
- **who speaks** (the spokesperson) and **what they say**: the quote comes from the person, word for word; never write
  a quote for them, never put in «» what they did not say; a quote still to come is marked `[citazione da
  confermare]`;
- the audience, the deadline, what must not be said.

### 2. The facts and their sources
1. `search` on the subject (scope `all`, then `sources` for what others published, `facts` and `documents` for what
   the organisation holds); `sources-find` (MCP `sources_find`) for the cards of a period or of a person; the description and the latest
   update of the project when the release is about one.
2. Write the **sheet of the sources**: one line per fact the release will state, with where it comes from (the card
   with its outlet, date and link; the fact or document of the organisation; the task or project). A fact without a
   source does not go in the release: it becomes an open question.
3. Keep apart what is **established** (an act, a vote, a date, a figure in a document) from what **others claim** (a
   statement of a party, a union, a company: a card marked `partisan` is a position, not a fact): what others claim is
   attributed («secondo…», «ha dichiarato…»), with its date.
4. **Public persons only**, in their public role; a private person is never named, even when the article names them.
5. Dates, names and figures that disagree between sources are said in the open questions, never chosen silently.

### 3. The draft
In the format of the procedure; without one, the usual shape:
- **title** (what happened or what the organisation says, in one line) and, if useful, a **subtitle**;
- **opening paragraph**: who, what, when, where, why, in two or three sentences;
- **body**: the facts of the sheet, in order of importance, each traceable to its source; the positions of others
  attributed;
- **the spokesperson's quote**, as given;
- **the closing paragraph about the organisation**, from its facts or its procedure (never invented);
- **contacts for the press** as a placeholder, unless the procedure gives them.
Length as the procedure says; plain sentences; no attacks on persons; no adjectives the facts do not support.

### 4. Review with the person
Show, in this order: the draft; the sheet of the sources (fact → source, with the links); the open questions (missing
sources, disagreements, the quote to confirm, anything the procedure leaves to the person). The person corrects; the
draft changes only where they say.

### 5. After the yes
1. Save the final text as a **document of the memory** (`document-write`, MCP `document_write`) on the organisation, or on the project or
   task it belongs to, with the title, the date and the list of the cards and facts it cites in its summary; say where
   it is.
2. If the person decided something that will be true next time (who speaks, the closing paragraph, the length),
   propose it as a change to the procedure; if it is something the agent must always or never do, propose it as a rule
   (a lead activates it).
3. The person sends it: the agent never sends, publishes or e-mails a release, nor prepares a message ready to send to
   outlets on its own.

## Safety & Invariants
- **Never** send, publish or e-mail a press release, nor schedule it: the person does.
- **Never** invent a fact, a figure, a date or a quote; never put in «» words the spokesperson did not give; every fact
  of the release is in the sheet of the sources.
- **Never** name a private person; a public person only in their public role, with the source of what is said of them.
- **Never** present the position of a party, a union or a company as a fact: attributed, with its date.
- The rules of the organisation bind (activity `communication`); a procedure describes. Organisations serving
  vulnerable people: no data of the people they serve, ever, not even anonymised in an example.
- If the hub is unreachable, say so and write nothing to the memory.
- During the silence before and on the voting days a release is still only a draft: the person decides when it goes
  out (the reference propaganda-e-silenzio-elettorale of the skill lista-civica-guida).
