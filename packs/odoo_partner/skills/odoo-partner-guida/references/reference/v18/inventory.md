---
type: "Reference"
title: "Magazzino — Delta Odoo 18"
description: "Magazzino — Delta Odoo 18: i cambi di Odoo 18 rispetto alla versione prima, da leggere con le lezioni del tag inventory e con il codice della versione."
tags: ["inventory", "v18"]
---

# Magazzino — Delta Odoo 18

> Per i progetti su Odoo 18, insieme alle lezioni del hub con il tag `inventory` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-18` (`.texo/THREADS.md`). Breaking change 17→18 ed errori specifici della versione.

## Cambiato in 18.0

- Il campo `quantity_done` di `stock.move` è rinominato `quantity`. Usare `quantity` da Odoo 18.0 in poi.
- Il campo `qty_done` di `stock.move.line` è rinominato `quantity`. Usare `quantity` da Odoo 18.0 in poi.
- Il campo `reserved_uom_qty` di `stock.move.line` è **rimosso**. In V17 era la quantità riservata/richiesta su una
  move line, distinta da `qty_done`. In V18 i due concetti sono fusi in `quantity`: dopo `action_assign()`,
  `quantity` contiene già la quantità riservata. Il codice che copiava `ml.reserved_uom_qty` in `ml.qty_done`
  prima di chiamare `button_validate()` deve eliminare del tutto il ciclo.
- Il wizard `stock.immediate.transfer` è rimosso: Odoo 18.0 non chiede più di compilare le quantità fatte prima
  della validazione. La chiave di context `skip_immediate` viene ignorata: toglierla dalle chiamate a
  `button_validate()`. Per sopprimere il wizard del backorder usare invece `skip_backorder=True`.

### Modello dei colli (package): nessun cambiamento in 18.0

Verificato sulla sorgente 18: il modello resta `stock.quant.package`, `stock.package_level`
esiste ancora (`stock_package_level.py`) e `move_ids_without_package` è ancora su
`stock.picking`. Il rename in `stock.package`, la rimozione di `stock.package_level` e di
`move_ids_without_package` sono cambiamenti della **19.0** — vedi `reference/v19/inventory.md`.
`product_packaging_id` su `stock.move`/SO/PO è ancora presente in 18 (rimosso in 19, fuso nelle UoM).

### Pattern di validazione automatica dei picking interamente riservati (V18)

**SBAGLIATO (pattern V17 — va in errore in V18):**
```python
for ml in picking.move_line_ids:
    ml.quantity = ml.reserved_uom_qty   # AttributeError: campo inesistente
result = picking.with_context(skip_backorder=True, skip_immediate=True).button_validate()
```

**CORRETTO (V18):**
```python
# dopo action_assign() quantity sulle move line è già la quantità riservata
result = picking.with_context(skip_backorder=True).button_validate()
```
