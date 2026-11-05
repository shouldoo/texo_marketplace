---
type: "Reference"
title: "Manifest — Delta Odoo 18"
description: "Manifest — Delta Odoo 18: i cambi di Odoo 18 rispetto alla versione prima, da leggere con le lesson del tag manifest e con il codice della versione."
tags: ["manifest", "v18"]
---

# Manifest — Delta Odoo 18

> Per i progetti su Odoo 18, insieme alle lesson del hub con il tag `manifest` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-18` (`.texo/THREADS.md`). Breaking change 17→18 ed errori specifici della versione.

## Changed in 18.0

| What Changed | Before (17.0) | Now (18.0) | Impact |
|-------------|---------------|------------|--------|
| Version prefix | `17.0.X.Y.Z` | `18.0.X.Y.Z` | Update on migration |
| Structural format | No changes | Same manifest structure | No breaking changes |

### Version prefix is `18.0.X.Y.Z`

**WRONG (18.0 module with 17.0 prefix):**
```python
"version": "17.0.1.0.0",
```

**CORRECT (18.0):**
```python
"version": "18.0.1.0.0",
```

**Why:** The Odoo version prefix must match the target Odoo version. OCA tools use the prefix to identify which Odoo version the module targets. Mismatched prefixes prevent publishing and may cause compatibility warnings.

### No structural manifest changes in 18.0

The `__manifest__.py` format is identical between 17.0 and 18.0. All required keys (`name`, `version`, `license`, `depends`, `data`, `installable`) remain the same. The only change is the version prefix number.
