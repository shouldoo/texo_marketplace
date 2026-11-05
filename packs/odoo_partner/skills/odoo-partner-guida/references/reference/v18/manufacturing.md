---
type: "Reference"
title: "Manufacturing — Delta Odoo 18"
description: "Manufacturing — Delta Odoo 18: i cambi di Odoo 18 rispetto alla versione prima, da leggere con le lesson del tag manufacturing e con il codice della versione."
tags: ["manufacturing", "v18"]
---

# Manufacturing — Delta Odoo 18

> Per i progetti su Odoo 18, insieme alle lesson del hub con il tag `manufacturing` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-18` (`.texo/THREADS.md`). Breaking change 17→18 ed errori specifici della versione.

## V18 — breaking changes nell'area

Nessun breaking change diretto su `mrp.*` in V18.
I breaking change WMS (es. `reserved_uom_qty` rimosso) si applicano anche ai picking
generati dalla produzione — vedi `reference/v18/inventory.md`.

## Errori ricorrenti già incontrati

### `AttributeError: 'stock.move.line' object has no attribute 'reserved_uom_qty'` (V18)

**Contesto:** override di `button_mark_done` su `mrp.production` che copiava
`ml.reserved_uom_qty` in `ml.quantity` prima di chiamare `button_validate()`.

**Causa:** `reserved_uom_qty` è stato rimosso in V18. Dopo `action_assign()`,
`quantity` sulla move line contiene già la quantità riservata.

**Fix:** eliminare il loop e rimuovere `skip_immediate=True`:

```python
# SBAGLIATO (V17):
for ml in picking.move_line_ids:
    ml.quantity = ml.reserved_uom_qty
result = picking.with_context(skip_backorder=True, skip_immediate=True).button_validate()

# CORRETTO (V18):
result = picking.with_context(skip_backorder=True).button_validate()
```

### `_get_rule`/`_get_rule_domain` vivono su `procurement.group`, non su `stock.rule` (V18)

**Contesto:** override del procurement per forzare la regola (make→manufacture,
buy→buy) in base a una decisione di commessa, su prodotti con rotte multiple
(Buy + Manufacture).

**Sintomo:** `UserError` "Nessun prezzo fornitore corrispondente per generare
l'ordine di acquisto del prodotto X" su un componente che doveva essere prodotto.
Con dual-route la selezione nativa sceglie per priorità rotta → Buy → `_run_buy`
→ nessun seller → errore.

**Causa:** in Odoo 18 `_get_rule` e `_get_rule_domain` sono definiti su
**`procurement.group`** (`addons/stock/models/stock_rule.py`, classe
`ProcurementGroup`), NON su `stock.rule`. Un override con `_inherit='stock.rule'`
è **codice morto**: non viene mai invocato dal cascade. Insidioso perché non dà
errore — semplicemente non scatta. Può sembrare funzionante finché i prodotti
hanno una rotta singola; emerge solo sul primo prodotto dual-route.

**Fix:** ereditare il modello giusto:

```python
class ProcurementGroup(models.Model):
    _inherit = 'procurement.group'   # NON 'stock.rule'

    def _get_rule(self, product_id, location_id, values): ...
    def _get_rule_domain(self, locations, values): ...
```

### `project_id` nei procurement values va come id (int), non recordset (V18)

**Contesto:** override di `stock.move._prepare_procurement_values` che propaga il
`project_id` di commessa al cascade.

**Sintomo:** nel cascade (non al primo livello) compaiono
`AssertionError: Invalid value project.project(N,) in domain term ('project_id', '=', ...)`
in `_bom_find`/`_bom_find_domain` e poi `ProgrammingError: can't adapt type
'project.project'` alla create del sub-MO.

**Causa:** un override metteva `values['project_id'] = project` (recordset). La
convenzione Odoo per i procurement values è l'**id** (`project_mrp` stesso fa
`res['project_id'] = ...project_id.id`). Un recordset si propaga in domini e SQL
a valle. Mascherato quando il top MO riceve `project_id` come int dal context del
wizard (`with_context(project_id=project.id)`): il recordset emerge solo nel cascade.

**Fix:** sempre `.id`:

```python
if project:
    values['project_id'] = project.id   # NON: project
```

Difensivamente, coercere recordset→id in ogni helper che riceve `project_id` dai
values e lo usa in un domain (`if hasattr(project_id, 'id'): project_id = project_id.id`).

### Rotta MTO a livello prodotto → buy-to-stock non agganciato al confirm (V18)

**Contesto:** lancio di commessa che pre-approvvigiona i componenti (riserva + PO), poi
conferma il MO top con cascade nativo. Una foglia consumata (`buy`/raw) porta la rotta
"Replenish on Order (MTO)" sul **template prodotto** (configurata o ereditata da lanci
precedenti — le rotte sono globali sul template).

**Sintomo:** alla conferma del MO compare un **secondo PO** per quel componente, duplicando
quello già creato in fase di approvvigionamento. Il PO duplicato è in stato `draft` e
**senza stock.move collegata** (`move_dest_ids` vuoto).

**Causa:** la rotta MTO di prodotto è `make_to_order` puro: alla conferma il cascade lancia
un rifornimento buy-to-stock **non agganciato** che **ignora sia lo stock sia l'incoming**
(ordina il fabbisogno pieno). Accade anche se il PO di approvvigionamento è già **confermato**
con ricezione attesa: l'MTO non netta contro l'incoming.

**Fix:** non forzare `make_to_stock` sulla *raw move* (vedi voce sotto). Riconciliazione a
valle: al confirm, per le sole foglie consumate (decisione non make/subcontract) over-coperte,
annullare l'eccesso prendendo **solo PO `draft`**, newest-first (così cade il duplicato appena
creato dal cascade, non il PO precedente), mai PO confermati/ricevuti.

### Forzare `make_to_stock` sulla raw move di un MO rompe il PBM (V18)

**Contesto:** per impedire al cascade di ri-comprare una foglia consumata, si è provato a
override `stock.move._adjust_procure_method` forzando `procure_method='make_to_stock'` sulle
`move_raw_ids` del MO.

**Sintomo:** nessun **Pick Components** generato, staging assente, e
`_release_stock_reservations` non scatta (nessun picking PBM in cui rilasciare la riserva).

**Causa:** in magazzino PBM la raw move (`pre-production → production`) deve restare
`make_to_order`: è il suo MTO che **tira** il Pick Components (`stock → pre-production`).
Forzandola `make_to_stock` il pull non parte.

**Fix:** la raw move resta MTO. La neutralizzazione dell'acquisto va fatta a livello di
**selezione regola / pick** o per **riconciliazione a valle** (annullo dell'eccesso), mai
sulla raw.

### `mrp.bom._bom_subcontract_find(product)` è project-aware via context (V18)

**Contesto:** esplodere la distinta **subcontract di commessa** di un componente (per
accantonare i materiali da inviare al terzista).

**Nota:** `_bom_subcontract_find(product, …, bom_type='subcontract')` passa per
`_bom_find_domain`, che `bom_find_project` (override #1) rende project-aware. Quindi
`self.env['mrp.bom'].with_context(project_id=<id>)._bom_subcontract_find(product)` restituisce
la BOM subcontract **del progetto**, coerente col lookup del cascade. Utile per un walk di
esplosione che ricorre anche sui nodi subcontract.
