---
type: "Reference"
title: "Inventory — Delta Odoo 18"
description: "Inventory — Delta Odoo 18: i cambi di Odoo 18 rispetto alla versione prima, da leggere con le lesson del tag inventory e con il codice della versione."
tags: ["inventory", "v18"]
---

# Inventory — Delta Odoo 18

> Per i progetti su Odoo 18, insieme alle lesson del hub con il tag `inventory` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-18` (`.texo/THREADS.md`). Breaking change 17→18 ed errori specifici della versione.

## Changed in 18.0

- `stock.move` field `quantity_done` renamed to `quantity`. Use `quantity` for Odoo 18.0+.
- `stock.move.line` field `qty_done` renamed to `quantity`. Use `quantity` for Odoo 18.0+.
- `stock.move.line` field `reserved_uom_qty` **removed**. In V17 this was the reserved/demanded quantity on a move line, separate from `qty_done`. In V18 the two concepts are merged into `quantity`: after `action_assign()`, `quantity` already holds the reserved amount. Any code that copied `ml.reserved_uom_qty` into `ml.qty_done` before calling `button_validate()` must drop the loop entirely.
- `stock.immediate.transfer` wizard removed: Odoo 18.0 no longer prompts to fill done quantities before validation. The `skip_immediate` context key is ignored — remove it from `button_validate()` calls. Use `skip_backorder=True` instead to suppress the backorder wizard.

### Package model: nessun cambiamento in 18.0

Verificato sulla sorgente 18: il modello resta `stock.quant.package`, `stock.package_level`
esiste ancora (`stock_package_level.py`) e `move_ids_without_package` è ancora su
`stock.picking`. Il rename in `stock.package`, la rimozione di `stock.package_level` e di
`move_ids_without_package` sono cambiamenti della **19.0** — vedi `reference/v19/inventory.md`.
`product_packaging_id` su `stock.move`/SO/PO è ancora presente in 18 (rimosso in 19, fuso nelle UoM).

### Auto-validation pattern for fully-assigned pickings (V18)

**WRONG (V17 pattern — crashes in V18):**
```python
for ml in picking.move_line_ids:
    ml.quantity = ml.reserved_uom_qty   # AttributeError: no such field
result = picking.with_context(skip_backorder=True, skip_immediate=True).button_validate()
```

**CORRECT (V18):**
```python
# quantity on move lines is already the reserved amount after action_assign()
result = picking.with_context(skip_backorder=True).button_validate()
```
