---
type: "Reference"
title: "Inventory — Delta Odoo 19"
description: "Inventory — Delta Odoo 19: i cambi di Odoo 19 rispetto alla versione prima, da leggere con le lesson del tag inventory e con il codice della versione."
tags: ["inventory", "v19"]
---

# Inventory — Delta Odoo 19

> Per i progetti su Odoo 19, insieme alle lesson del hub con il tag `inventory` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-19` (`.texo/THREADS.md`). Breaking change 18→19 ed errori specifici della versione.

## Changed in 19.0

- Core valuation/quant APIs stable: `stock.quant` and `stock.valuation.layer` are unchanged from 18.0.
- Warehouse configuration fields (`reception_steps`, `delivery_steps`) and picking type references (`in_type_id`, `out_type_id`, `int_type_id`) are unchanged.
- Use `quantity` (not `quantity_done` / `qty_done`) on `stock.move` and `stock.move.line` as established in 18.0.
- **But** the package model, the `product.packaging` model and several stock fields/views **did** change in 19.0 — see below.

### `procurement.group` renamed to `stock.reference`

Verificato sul codice di Odoo 19 (filo `odoo-19`) (`addons/stock/models/stock_reference.py`,
`class StockReference` / `_name = 'stock.reference'`): il modello
`procurement.group` non esiste più, è stato rinominato `stock.reference`.

**Impatto diretto sui pattern di questo pack:** ogni
override `_inherit = 'procurement.group'` (vedi `v18/manufacturing.md`,
sezione "`_get_rule`/`_get_rule_domain` vivono su `procurement.group`, non su
`stock.rule`") va riscritto su `_inherit = 'stock.reference'` in un cliente
che migra a 19 — comprese le chiamate `self.env["procurement.group"].run(...)`
nei moduli che lanciano un approvvigionamento, che diventano
`self.env["stock.reference"].run(...)`.

**WRONG (≤18.0, non funziona più in 19.0):**
```python
class ProcurementGroup(models.Model):
    _inherit = 'procurement.group'

    def _get_rule(self, product_id, location_id, values): ...
```

**CORRECT (19.0):**
```python
class StockReference(models.Model):
    _inherit = 'stock.reference'

    def _get_rule(self, product_id, location_id, values): ...
```

### `product.packaging` model REMOVED — merged into UoM

The standalone `product.packaging` model no longer exists. Packagings are now expressed
as units of measure:

- `product.template.uom_ids` — Many2many to `uom.uom` ("Packagings").
- new `product.uom` model — per-variant link `(product_id, uom_id, barcode)`.
- `uom.uom.product_uom_ids` — inverse One2many.
- On `stock.move`: `product_packaging_id` / `product_packaging_qty` → `packaging_uom_id` / `packaging_uom_qty`.
- `product.product_uom_form_view` does **not** exist: `product.uom` has an inline-editable
  list only. Create your own form view if you need one.

### `stock.move.name` REMOVED

| Field | Replacement |
|-------|-------------|
| `stock.move.name` | `description_picking` (writable `Text`) or `reference` (computed `Char`) |

Affects every `env['stock.move'].create({'name': ...})`.

### `stock.package` (was `stock.quant.package` until 18.0, `stock.package` from 19.0)

In 19.0 il modello è rinominato; `stock.package_level` e `move_ids_without_package` su `stock.picking`
sono rimossi (usa `move_ids` e `move_line.result_package_id`). `_inherit = 'stock.quant.package'`
e `env['stock.quant.package']` falliscono. In 18.0 tutto questo esiste ancora.

Rinomina dei campi:

| Before (≤18.0) | Now (19.0) |
|----------------|-----------|
| `parent_id` | `parent_package_id` |
| `child_ids` | `child_package_ids` |

Affects Python compute (`mapped('result_package_id.parent_id')`), QWeb reports
(`package.parent_id`), and tests — typical symptom `KeyError: 'parent_id'`.

### `stock.picking.package_ids` REMOVED

`package_ids` and `package_dest_id` are gone on `stock.picking`. Derive packages from move lines:

- all packages: `picking.move_line_ids.result_package_id`
- top-level only: `picking.move_line_ids.result_package_id.outermost_package_id`

### Field / view / category renames

| What | Before (≤18.0) | Now (19.0) |
|------|----------------|-----------|
| `stock.move.line.reserved_qty` | reserved qty field | use `quantity` |
| Picking type `show_operations` / `show_reserved` | present | **removed** (`use_create_components_lots` present for MRP) |
| `detailed_type == 'product'` | storable flag | `is_storable` (`type` is now only `consu` / `service`) |
| View `stock.view_quant_package_form` | — | `stock.stock_package_view_form` |
| View `stock.view_quant_package_tree` | — | `stock.stock_package_view_list` |
| View `stock.view_quant_package_kanban` | — | `stock.stock_package_view_kanban` |
| Menu `stock.menu_stock_configuration` | — | `stock.menu_stock_config_settings` |
| Category `base.module_category_inventory_inventory` | — | `base.module_category_supply_chain` |

### QWeb barcode widget is strict in 19.0

`<span t-out="x" t-options="{'widget':'barcode'}">` raises
`TypeError: expected string or bytes-like object` when `x` is numeric (v18 was tolerant).
Wrap numerics: `t-out="str(quantity)"`.
