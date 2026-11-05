---
type: "Reference"
title: "Wizards — Delta Odoo 19"
description: "Wizards — Delta Odoo 19: i cambi di Odoo 19 rispetto alla versione prima, da leggere con le lesson del tag wizards e con il codice della versione."
tags: ["wizards", "v19"]
---

# Wizards — Delta Odoo 19

> Per i progetti su Odoo 19, insieme alle lesson del hub con il tag `wizards` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-19` (`.texo/THREADS.md`). Breaking change 18→19 ed errori specifici della versione.

## Changed in 19.0

No breaking changes to wizards in 19.0. `TransientModel`, `default_get` patterns, `target="new"`, `special="cancel"`, and `ensure_one()` all work the same as in 18.0. Wizard views should adopt 19.0 QWeb changes where applicable (use `t-out` instead of `t-esc`).
