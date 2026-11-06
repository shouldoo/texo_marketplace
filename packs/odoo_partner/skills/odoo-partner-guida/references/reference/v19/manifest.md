---
type: "Reference"
title: "Manifest — Delta Odoo 19"
description: "Manifest — Delta Odoo 19: i cambi di Odoo 19 rispetto alla versione prima, da leggere con le lezioni del tag manifest e con il codice della versione."
tags: ["manifest", "v19"]
---

# Manifest — Delta Odoo 19

> Per i progetti su Odoo 19, insieme alle lezioni del hub con il tag `manifest` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-19` (`.texo/THREADS.md`). Breaking change 18→19 ed errori specifici della versione.

## Cambiato in 19.0

| Cosa cambia | Prima (18.0) | Ora (19.0) | Impatto |
|-------------|---------------|------------|--------|
| Prefisso di versione | `18.0.X.Y.Z` | `19.0.X.Y.Z` | Da aggiornare nella migrazione |
| Formato strutturale | Nessun cambiamento | Stessa struttura del manifest | Nessun breaking change |

### Il prefisso di versione è `19.0.X.Y.Z`

**SBAGLIATO (modulo 19.0 con prefisso 18.0):**
```python
"version": "18.0.1.0.0",
```

**CORRETTO (19.0):**
```python
"version": "19.0.1.0.0",
```

**Perché:** il prefisso di versione deve corrispondere alla versione di Odoo di destinazione. Gli strumenti OCA
usano il prefisso per capire a quale versione di Odoo è destinato il modulo. Un prefisso non corrispondente
impedisce la pubblicazione e può causare avvisi di compatibilità.

### Nessun cambiamento strutturale del manifest in 19.0

Il formato di `__manifest__.py` è identico tra 18.0 e 19.0. Tutte le chiavi richieste (`name`, `version`,
`license`, `depends`, `data`, `installable`) restano le stesse. L'unico cambiamento è il numero del prefisso di
versione.

## Moduli tecnici rinominati in 19.0 (verificato sul codice di Odoo 19)

Se un `depends` elenca uno di questi nomi tecnici (18.0 o precedente), va
aggiornato prima di installare su 19.0 -- il modulo con il vecchio nome non
esiste più come directory:

| Modulo (≤18.0) | Modulo (19.0) | Nota |
|---|---|---|
| `web_editor` | `html_builder` | Rinomina completa, verificata: dir `web_editor` assente, `html_builder` presente |
| `membership` | `partnership` | Rinomina completa, verificata: dir `membership` assente, `partnership` presente |
| `bus` (per `bus.presence`) | `mail` (`mail.presence`) | Il modello `bus.presence` è stato assorbito in `addons/mail/models/mail_presence.py` |
| `hr_contract` | `hr` | Vedi `v19/hr.md` -- assorbito nel modulo `hr` base |

Bassa priorità operativa per la maggior parte dei clienti custom (moduli
tecnici raramente referenziati direttamente in `depends` custom, eccetto
`hr_contract`, molto più comune), ma utile per non trovarsi un `depends`
"morto" a metà migrazione.
