---
type: "Reference"
title: "Wizard — Delta Odoo 19"
description: "Wizard — Delta Odoo 19: i cambi di Odoo 19 rispetto alla versione prima, da leggere con le lezioni del tag wizards e con il codice della versione."
tags: ["wizards", "v19"]
---

# Wizard — Delta Odoo 19

> Per i progetti su Odoo 19, insieme alle lezioni del hub con il tag `wizards` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-19` (`.texo/THREADS.md`). Breaking change 18→19 ed errori specifici della versione.

## Cambiato in 19.0

Nessun breaking change nei wizard in 19.0. `TransientModel`, i pattern di `default_get`, `target="new"`,
`special="cancel"` e `ensure_one()` funzionano come in 18.0. Le viste dei wizard dovrebbero adottare i cambi
QWeb della 19.0 dove servono (usare `t-out` al posto di `t-esc`).
