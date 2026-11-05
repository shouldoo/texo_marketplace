---
type: "Reference"
title: "Manifest — Delta Odoo 19"
description: "Manifest — Delta Odoo 19: i cambi di Odoo 19 rispetto alla versione prima, da leggere con le lesson del tag manifest e con il codice della versione."
tags: ["manifest", "v19"]
---

# Manifest — Delta Odoo 19

> Per i progetti su Odoo 19, insieme alle lesson del hub con il tag `manifest` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-19` (`.texo/THREADS.md`). Breaking change 18→19 ed errori specifici della versione.

## Changed in 19.0

| What Changed | Before (18.0) | Now (19.0) | Impact |
|-------------|---------------|------------|--------|
| Version prefix | `18.0.X.Y.Z` | `19.0.X.Y.Z` | Update on migration |
| Structural format | No changes | Same manifest structure | No breaking changes |

### Version prefix is `19.0.X.Y.Z`

**WRONG (19.0 module with 18.0 prefix):**
```python
"version": "18.0.1.0.0",
```

**CORRECT (19.0):**
```python
"version": "19.0.1.0.0",
```

**Why:** The Odoo version prefix must match the target Odoo version. OCA tools use the prefix to identify which Odoo version the module targets. Mismatched prefixes prevent publishing and may cause compatibility warnings.

### No structural manifest changes in 19.0

The `__manifest__.py` format is identical between 18.0 and 19.0. All required keys (`name`, `version`, `license`, `depends`, `data`, `installable`) remain the same. The only change is the version prefix number.

## Moduli tecnici rinominati in 19.0 (verificato sul codice di Odoo 19)

Se un `depends` elenca uno di questi nomi tecnici (18.0 o precedente), va
aggiornato prima di installare su 19.0 -- il modulo con il vecchio nome non
esiste più come directory:

| Modulo (≤18.0) | Modulo (19.0) | Nota |
|---|---|---|
| `web_editor` | `html_builder` | Rename completo, verificato: dir `web_editor` assente, `html_builder` presente |
| `membership` | `partnership` | Rename completo, verificato: dir `membership` assente, `partnership` presente |
| `bus` (per `bus.presence`) | `mail` (`mail.presence`) | Il modello `bus.presence` è stato assorbito in `addons/mail/models/mail_presence.py` |
| `hr_contract` | `hr` | Vedi `v19/hr.md` -- assorbito nel modulo `hr` base |

Bassa priorità operativa per la maggior parte dei clienti custom (moduli
tecnici raramente referenziati direttamente in `depends` custom, eccetto
`hr_contract`, molto più comune), ma utile per non trovarsi un `depends`
"morto" a metà migrazione.
