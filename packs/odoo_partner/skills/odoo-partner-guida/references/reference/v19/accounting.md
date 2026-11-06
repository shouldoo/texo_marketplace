---
type: "Reference"
title: "Contabilità — Delta Odoo 19"
description: "Contabilità — Delta Odoo 19: i cambi di Odoo 19 rispetto alla versione prima, da leggere con le lezioni del tag accounting e con il codice della versione."
tags: ["accounting", "v19"]
---

# Contabilità — Delta Odoo 19

> Per i progetti su Odoo 19, insieme alle lezioni del hub con il tag `accounting` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-19` (`.texo/THREADS.md`). Breaking change 18→19 ed errori specifici della versione.

## Cambiato in 19.0

| Cosa cambia | Prima (18.0) | Ora (19.0) | Impatto |
|-------------|---------------|------------|--------|
| Creazione di `account.move.line` | `create()` diretto sulle righe ammesso in alcuni casi | **Bloccata** -- creare sempre le righe tramite `account.move` con `Command` | **Incompatibile** -- `account.move.line.create()` da solo solleva un errore |
| `name_get()` su `account.move` | Deprecato | **Rimosso** -- usare `_compute_display_name()` | **Incompatibile** -- vedi models.md |
| Data di blocco IVA | `tax_lock_date` sull'azienda | Spostata nell'ambito di `account.fiscal.year` | **Incompatibile** -- il codice che legge `company.tax_lock_date` va aggiornato |
| Token di pagamento | Modello `payment.token` | Rifatto con l'integrazione di `payment.provider` | **Miglioria** -- metodi di pagamento salvati semplificati |
| `read_group()` sui modelli contabili | `read_group()` standard | Usare `_read_group()` o `formatted_read_group()` | **Incompatibile** -- vedi models.md |
| Ambito aziendale di `account.account` | `company_id` (Many2one) | `company_ids` (Many2many) | **Incompatibile** -- i conti ora possono essere condivisi tra aziende; ogni domain/ricerca su `company_id` deve passare a `company_ids` |

## Errori comuni

### `UserError: You cannot create a move line directly`

In Odoo 19.0 i record di `account.move.line` non si possono creare da soli. Crearli sempre tramite
`account.move`, con `Command.create()` nel campo `line_ids` o `invoice_line_ids`.

### `ValueError: Invalid field account.account.company_id in condition`

**Contesto:** ricerche/domain su `account.account` scritti per V17/V18 (es.
`search([('company_id', '=', company.id)])` per trovare un conto per tipo).

**Causa:** in Odoo 19 `account.account` supporta la multi-company: il campo
`company_id` (Many2one) è stato sostituito da `company_ids` (Many2many).

**Soluzione:** sostituire `('company_id', '=', company.id)` con
`('company_ids', 'in', company.id)`.

```python
# SBAGLIATO (V17/V18):
env['account.account'].search([('account_type', '=', 'asset_current'), ('company_id', '=', company.id)])

# CORRETTO (V19):
env['account.account'].search([('account_type', '=', 'asset_current'), ('company_ids', 'in', company.id)])
```
