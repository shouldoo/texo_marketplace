---
type: "Reference"
title: "Manifest — Delta Odoo 18"
description: "Manifest — Delta Odoo 18: i cambi di Odoo 18 rispetto alla versione prima, da leggere con le lezioni del tag manifest e con il codice della versione."
tags: ["manifest", "v18"]
---

# Manifest — Delta Odoo 18

> Per i progetti su Odoo 18, insieme alle lezioni del hub con il tag `manifest` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-18` (`.texo/THREADS.md`). Breaking change 17→18 ed errori specifici della versione.

## Cambiato in 18.0

| Cosa cambia | Prima (17.0) | Ora (18.0) | Impatto |
|-------------|---------------|------------|--------|
| Prefisso di versione | `17.0.X.Y.Z` | `18.0.X.Y.Z` | Da aggiornare nella migrazione |
| Formato strutturale | Nessun cambiamento | Stessa struttura del manifest | Nessun breaking change |

### Il prefisso di versione è `18.0.X.Y.Z`

**SBAGLIATO (modulo 18.0 con prefisso 17.0):**
```python
"version": "17.0.1.0.0",
```

**CORRETTO (18.0):**
```python
"version": "18.0.1.0.0",
```

**Perché:** il prefisso di versione deve corrispondere alla versione di Odoo di destinazione. Gli strumenti OCA
usano il prefisso per capire a quale versione di Odoo è destinato il modulo. Un prefisso non corrispondente
impedisce la pubblicazione e può causare avvisi di compatibilità.

### Nessun cambiamento strutturale del manifest in 18.0

Il formato di `__manifest__.py` è identico tra 17.0 e 18.0. Tutte le chiavi richieste (`name`, `version`,
`license`, `depends`, `data`, `installable`) restano le stesse. L'unico cambiamento è il numero del prefisso di
versione.
