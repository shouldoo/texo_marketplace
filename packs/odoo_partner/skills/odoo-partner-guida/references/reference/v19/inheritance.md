---
type: "Reference"
title: "Ereditarietà — Delta Odoo 19"
description: "Ereditarietà — Delta Odoo 19: i cambi di Odoo 19 rispetto alla versione prima, da leggere con le lezioni del tag inheritance e con il codice della versione."
tags: ["inheritance", "v19"]
---

# Ereditarietà — Delta Odoo 19

> Per i progetti su Odoo 19, insieme alle lezioni del hub con il tag `inheritance` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-19` (`.texo/THREADS.md`). Breaking change 18→19 ed errori specifici della versione.

## Cambiato in 19.0

Nessun breaking change nei meccanismi di ereditarietà in 19.0. L'estensione dei modelli (`_inherit`), la
delega (`_inherits`), l'ereditarietà delle viste (`inherit_id` + xpath) e la priorità funzionano come in 18.0.
Attenzione: in 19.0 l'override di `name_get()` sui modelli ereditati fallisce -- usare invece
`_compute_display_name()` (vedi `reference/v19/models.md`).
