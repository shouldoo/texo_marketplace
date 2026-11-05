---
type: "Reference"
title: "Inheritance — Delta Odoo 19"
description: "Inheritance — Delta Odoo 19: i cambi di Odoo 19 rispetto alla versione prima, da leggere con le lesson del tag inheritance e con il codice della versione."
tags: ["inheritance", "v19"]
---

# Inheritance — Delta Odoo 19

> Per i progetti su Odoo 19, insieme alle lesson del hub con il tag `inheritance` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-19` (`.texo/THREADS.md`). Breaking change 18→19 ed errori specifici della versione.

## Changed in 19.0

No breaking changes to inheritance mechanisms in 19.0. Model extension (`_inherit`), delegation (`_inherits`), view inheritance (`inherit_id` + xpath), and priority all work the same as in 18.0. Note that overriding `name_get()` on inherited models will fail in 19.0 -- use `_compute_display_name()` instead (see `reference/v19/models.md`).
