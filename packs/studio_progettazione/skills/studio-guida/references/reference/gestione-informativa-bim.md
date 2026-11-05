---
type: "Reference"
title: "Gestione informativa (BIM) in una commessa"
description: "Norme di riferimento, documenti della gestione informativa e stati del CDE: che cosa ne tiene la memoria e che cosa resta nell'ambiente di condivisione."
tags: ["bim", "cde", "ifc", "gestione-informativa"]
---

# Gestione informativa (BIM) in una commessa

> Riferimenti da verificare sul testo vigente prima dell'uso: si cita l'articolo letto e la data di lettura.

## Riferimenti

- UNI EN ISO 19650 (serie): gestione delle informazioni lungo il ciclo di vita del costruito.
- UNI 11337 (serie): gestione digitale dei processi informativi delle costruzioni.
- D.Lgs. 36/2023, art. 43 e allegato I.9: metodi e strumenti di gestione informativa digitale negli appalti
  pubblici. Dal 1° gennaio 2025 le stazioni appaltanti li adottano per nuove costruzioni e interventi su
  costruzioni esistenti oltre la soglia di importo fissata dal comma 1 (testo vigente letto il 2026-11-01); sotto
  soglia possono adottarli e premiarli nella gara (comma 2). Le piattaforme sono interoperabili, con formati aperti
  non proprietari (comma 3).
- Formati aperti: IFC (ISO 16739) per i modelli, BCF per le segnalazioni, IDS per i requisiti informativi
  verificabili.

## I documenti e il loro posto

| Documento | Chi lo produce | Nella memoria |
|---|---|---|
| Capitolato informativo (CI) | committente | documento della commessa, con il sommario dei requisiti |
| Offerta di gestione informativa (oGI) | studio, in gara | documento della commessa (gara) |
| Piano di gestione informativa (pGI) | studio, dopo l'affidamento | documento della commessa; le scelte che contiene diventano fatti |
| Modelli ed elaborati | team | solo il riferimento: contenitore, disciplina, revisione, stato |
| Segnalazioni di coordinamento (BCF) | team, coordinatore | restano nel CDE; nella memoria solo le decisioni che ne nascono |

## Stati del CDE

| Stato (ISO 19650) | Significato | Nella memoria |
|---|---|---|
| WIP, in lavorazione | lavoro della singola disciplina | non si cita fuori dal team della disciplina |
| Shared, condiviso | disponibile al coordinamento | riferimento con stato «condiviso» |
| Published, pubblicato | approvato per l'uso | riferimento con stato «pubblicato»; le decisioni ne citano la revisione |
| Archived, archiviato | storico | le note che lo citavano si sostituiscono con quelle sulla revisione nuova |
