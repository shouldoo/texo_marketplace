---
type: "Reference"
title: "Accounting — Delta Odoo 19"
description: "Accounting — Delta Odoo 19: i cambi di Odoo 19 rispetto alla versione prima, da leggere con le lesson del tag accounting e con il codice della versione."
tags: ["accounting", "v19"]
---

# Accounting — Delta Odoo 19

> Per i progetti su Odoo 19, insieme alle lesson del hub con il tag `accounting` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-19` (`.texo/THREADS.md`). Breaking change 18→19 ed errori specifici della versione.

## Changed in 19.0

| What Changed | Before (18.0) | Now (19.0) | Impact |
|-------------|---------------|------------|--------|
| `account.move.line` creation | Direct `create()` on move lines allowed in some cases | **Blocked** -- always create lines via `account.move` with `Command` | **Breaking** -- standalone `account.move.line.create()` raises error |
| `name_get()` on `account.move` | Deprecated | **Removed** -- use `_compute_display_name()` | **Breaking** -- see models.md |
| Tax lock date | `tax_lock_date` on company | Moved to `account.fiscal.year` scope | **Breaking** -- code reading `company.tax_lock_date` needs update |
| Payment tokens | `payment.token` model | Refactored with `payment.provider` integration | **Enhancement** -- stored payment methods streamlined |
| `read_group()` on accounting models | Standard `read_group()` | Use `_read_group()` or `formatted_read_group()` | **Breaking** -- see models.md |
| `account.account` company scoping | `company_id` (Many2one) | `company_ids` (Many2many) | **Breaking** -- accounts can now be shared across companies; any domain/search on `company_id` must switch to `company_ids` |

## Common Errors

### `UserError: You cannot create a move line directly`

In Odoo 19.0, `account.move.line` records cannot be created independently. Always create them via `account.move` using `Command.create()` in the `line_ids` or `invoice_line_ids` field.

### `ValueError: Invalid field account.account.company_id in condition`

**Contesto:** ricerche/domain su `account.account` scritti per V17/V18 (es.
`search([('company_id', '=', company.id)])` per trovare un conto per tipo).

**Causa:** in Odoo 19 `account.account` supporta la multi-company: il campo
`company_id` (Many2one) è stato sostituito da `company_ids` (Many2many).

**Fix:** sostituire `('company_id', '=', company.id)` con
`('company_ids', 'in', company.id)`.

```python
# SBAGLIATO (V17/V18):
env['account.account'].search([('account_type', '=', 'asset_current'), ('company_id', '=', company.id)])

# CORRETTO (V19):
env['account.account'].search([('account_type', '=', 'asset_current'), ('company_ids', 'in', company.id)])
```
