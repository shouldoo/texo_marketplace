---
type: "Reference"
title: "Produzione — Delta Odoo 19"
description: "Produzione — Delta Odoo 19: i cambi di Odoo 19 rispetto alla versione prima, da leggere con le lezioni del tag manufacturing e con il codice della versione."
tags: ["manufacturing", "v19"]
---

# Produzione — Delta Odoo 19

> Per i progetti su Odoo 19, insieme alle lezioni del hub con il tag `manufacturing` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-19` (`.texo/THREADS.md`). Breaking change 18→19 ed errori specifici della versione.

## Cambiato in 19.0

### `procurement.group` → `stock.reference` (vedi anche `v19/inventory.md`)

Il modello su cui vivono `_get_rule`/`_get_rule_domain` (instradamento del procurement,
scelta tra Buy e Manufacture) è stato rinominato da `procurement.group` a
`stock.reference` — verificato sul codice di Odoo 19 (filo `odoo-19`)
(`addons/stock/models/stock_reference.py`).

**Impatto sui pattern di questo pacchetto:** il pattern documentato in
`v18/manufacturing.md` ("`_get_rule`/`_get_rule_domain` vivono su
`procurement.group`, non su `stock.rule`" — derivato da un incidente reale
su un cliente con rotte dual-route Buy+Manufacture) va riportato tal quale
ma con il nuovo nome modello. Chi migra un cliente con quell'override a 19
deve:

1. Cambiare `_inherit = 'procurement.group'` → `_inherit = 'stock.reference'`
   sull'override di `_get_rule`/`_get_rule_domain`.
2. Cambiare ogni `self.env["procurement.group"]` (chiamate a `.run()`,
   `.Procurement(...)`) in `self.env["stock.reference"]`.
3. Verificare `project_id` e altri procurement values custom: la convenzione
   "sempre id, mai recordset" (vedi `v18/manufacturing.md`) resta valida
   indipendentemente dal rename del modello.

Nessun altro breaking change diretto su `mrp.*` noto per 19.0 al momento
della scrittura di questa voce.
