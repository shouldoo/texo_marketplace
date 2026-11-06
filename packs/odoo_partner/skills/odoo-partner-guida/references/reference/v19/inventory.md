---
type: "Reference"
title: "Magazzino — Delta Odoo 19"
description: "Magazzino — Delta Odoo 19: i cambi di Odoo 19 rispetto alla versione prima, da leggere con le lezioni del tag inventory e con il codice della versione."
tags: ["inventory", "v19"]
---

# Magazzino — Delta Odoo 19

> Per i progetti su Odoo 19, insieme alle lezioni del hub con il tag `inventory` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-19` (`.texo/THREADS.md`). Breaking change 18→19 ed errori specifici della versione.

## Cambiato in 19.0

- Le API principali di valorizzazione e quant sono stabili: `stock.quant` e `stock.valuation.layer` non cambiano
  rispetto alla 18.0.
- I campi di configurazione del magazzino (`reception_steps`, `delivery_steps`) e i riferimenti ai tipi di
  picking (`in_type_id`, `out_type_id`, `int_type_id`) non cambiano.
- Usare `quantity` (non `quantity_done` / `qty_done`) su `stock.move` e `stock.move.line`, come stabilito in 18.0.
- **Però** il modello dei colli, il modello `product.packaging` e diversi campi e viste di stock **sono**
  cambiati in 19.0 — vedi sotto.

### `procurement.group` rinominato `stock.reference`

Verificato sul codice di Odoo 19 (filo `odoo-19`) (`addons/stock/models/stock_reference.py`,
`class StockReference` / `_name = 'stock.reference'`): il modello
`procurement.group` non esiste più, è stato rinominato `stock.reference`.

**Impatto diretto sui pattern di questo pacchetto:** ogni
override `_inherit = 'procurement.group'` (vedi `v18/manufacturing.md`,
sezione "`_get_rule`/`_get_rule_domain` vivono su `procurement.group`, non su
`stock.rule`") va riscritto su `_inherit = 'stock.reference'` in un cliente
che migra a 19 — comprese le chiamate `self.env["procurement.group"].run(...)`
nei moduli che lanciano un approvvigionamento, che diventano
`self.env["stock.reference"].run(...)`.

**SBAGLIATO (≤18.0, non funziona più in 19.0):**
```python
class ProcurementGroup(models.Model):
    _inherit = 'procurement.group'

    def _get_rule(self, product_id, location_id, values): ...
```

**CORRETTO (19.0):**
```python
class StockReference(models.Model):
    _inherit = 'stock.reference'

    def _get_rule(self, product_id, location_id, values): ...
```

### Modello `product.packaging` RIMOSSO — fuso nelle UoM

Il modello autonomo `product.packaging` non esiste più. Gli imballaggi ora si esprimono come unità di misura:

- `product.template.uom_ids` — Many2many verso `uom.uom` ("Packagings").
- nuovo modello `product.uom` — collegamento per variante `(product_id, uom_id, barcode)`.
- `uom.uom.product_uom_ids` — One2many inverso.
- Su `stock.move`: `product_packaging_id` / `product_packaging_qty` → `packaging_uom_id` / `packaging_uom_qty`.
- `product.product_uom_form_view` **non** esiste: `product.uom` ha solo una lista modificabile inline. Se serve
  una vista form, crearla nel proprio modulo.

### `stock.move.name` RIMOSSO

| Campo | Sostituto |
|-------|-------------|
| `stock.move.name` | `description_picking` (`Text` scrivibile) o `reference` (`Char` calcolato) |

Riguarda ogni `env['stock.move'].create({'name': ...})`.

### `stock.package` (era `stock.quant.package` fino alla 18.0, `stock.package` dalla 19.0)

In 19.0 il modello è rinominato; `stock.package_level` e `move_ids_without_package` su `stock.picking`
sono rimossi (usa `move_ids` e `move_line.result_package_id`). `_inherit = 'stock.quant.package'`
e `env['stock.quant.package']` falliscono. In 18.0 tutto questo esiste ancora.

Rinomina dei campi:

| Prima (≤18.0) | Ora (19.0) |
|----------------|-----------|
| `parent_id` | `parent_package_id` |
| `child_ids` | `child_package_ids` |

Riguarda i compute Python (`mapped('result_package_id.parent_id')`), i report QWeb (`package.parent_id`) e i
test — sintomo tipico `KeyError: 'parent_id'`.

### `stock.picking.package_ids` RIMOSSO

`package_ids` e `package_dest_id` non ci sono più su `stock.picking`. Ricavare i colli dalle move line:

- tutti i colli: `picking.move_line_ids.result_package_id`
- solo quelli di primo livello: `picking.move_line_ids.result_package_id.outermost_package_id`

### Rinomine di campi, viste e categorie

| Cosa | Prima (≤18.0) | Ora (19.0) |
|------|----------------|-----------|
| `stock.move.line.reserved_qty` | campo della quantità riservata | usare `quantity` |
| `show_operations` / `show_reserved` del tipo di picking | presenti | **rimossi** (`use_create_components_lots` presente per MRP) |
| `detailed_type == 'product'` | indicatore di prodotto stoccabile | `is_storable` (`type` ora è solo `consu` / `service`) |
| Vista `stock.view_quant_package_form` | — | `stock.stock_package_view_form` |
| Vista `stock.view_quant_package_tree` | — | `stock.stock_package_view_list` |
| Vista `stock.view_quant_package_kanban` | — | `stock.stock_package_view_kanban` |
| Menu `stock.menu_stock_configuration` | — | `stock.menu_stock_config_settings` |
| Categoria `base.module_category_inventory_inventory` | — | `base.module_category_supply_chain` |

### Il widget barcode di QWeb è rigoroso in 19.0

`<span t-out="x" t-options="{'widget':'barcode'}">` solleva
`TypeError: expected string or bytes-like object` quando `x` è numerico (la v18 lo tollerava).
Convertire i numeri: `t-out="str(quantity)"`.
