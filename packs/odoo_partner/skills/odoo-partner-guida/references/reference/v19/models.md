---
type: "Reference"
title: "Models & ORM — Delta Odoo 19"
description: "Models & ORM — Delta Odoo 19: i cambi di Odoo 19 rispetto alla versione prima, da leggere con le lesson del tag models e con il codice della versione."
tags: ["models", "v19"]
---

# Models & ORM — Delta Odoo 19

> Per i progetti su Odoo 19, insieme alle lesson del hub con il tag `models` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-19` (`.texo/THREADS.md`). Breaking change 18→19 ed errori specifici della versione.

## Changed in 19.0

| What Changed | Before (18.0) | Now (19.0) | Impact |
|-------------|---------------|------------|--------|
| `name_get()` | Deprecated (still works) | **Fully removed** | **Breaking** -- any `name_get()` override causes `AttributeError` |
| `read_group()` | Public API method | **Replaced** by `_read_group()` and `formatted_read_group()` | **Breaking** -- direct `read_group()` calls fail |
| `@api.returns` | Available (deprecated) | **Removed** | **Breaking** -- decorator causes `AttributeError` |
| `_sql_constraints` | Standard list of tuples | `models.Constraint` class **required** | **Breaking** -- old attribute is only logged as a warning and the constraint is silently never created (no SQL constraint ends up on the DB) |
| Domain expressions | `from odoo.osv import expression` + `expression.OR(...)` | `from odoo.fields import Domain` + `Domain(...) \| Domain(...)` | **New API** -- old import still works but new `Domain` class preferred |
| `self.user_has_groups('xmlid')` | Method on models | **Removed** | **Breaking** -- `AttributeError`; use `self.env.user.has_group('xmlid')` |
| `@api.depends('id')` | Tolerated | **Prohibited** -- raises `NotImplementedError` | **Breaking** -- a compute cannot depend on `id` |
| `from odoo.addons.http_routing.models.ir_http import slug` | Importable | **Removed** | **Breaking** -- use `IrHttp._slug` (see below) |
| `from odoo.addons.base.models.res_partner import WARNING_MESSAGE` | Importable | **Removed** | **Breaking** -- drop the import |

### `user_has_groups` removed → `has_group`

```python
# WRONG (≤18.0):
if self.user_has_groups('stock.group_stock_manager'):
    ...
# CORRECT (19.0): singular has_group on res.users is the public API
if self.env.user.has_group('stock.group_stock_manager'):
    ...
```

### `slug` import moved

```python
# WRONG (≤18.0):
from odoo.addons.http_routing.models.ir_http import slug
# CORRECT (19.0):
from odoo.addons.base.models.ir_http import IrHttp
slug = IrHttp._slug
```

### Never `@classmethod` on ORM CRUD overrides

`create()`, `write()`, `default_get()` are **instance** methods. A leftover/bogus
`@classmethod` (sometimes inherited from old code or scaffolding) breaks the signature:
`TypeError: BaseModel.<method>() missing 1 required positional argument`. Always drop it.

### `name_get()` fully removed -- use `_compute_display_name()`

**WRONG (causes error in 19.0):**
```python
def name_get(self):
    result = []
    for record in self:
        result.append((record.id, f"[{record.code}] {record.name}"))
    return result
```

**CORRECT (19.0):**
```python
@api.depends("code", "name")
def _compute_display_name(self):
    for record in self:
        record.display_name = f"[{record.code}] {record.name}"
```

**Why:** `name_get()` was deprecated in 18.0 and fully removed in 19.0. Use the `display_name` computed field with `_compute_display_name()` instead. This method is a standard compute method decorated with `@api.depends`.

### `read_group()` replaced by `_read_group()` and `formatted_read_group()`

**WRONG (fails in 19.0):**
```python
results = self.env["sale.order"].read_group(
    domain=[("state", "=", "sale")],
    fields=["partner_id", "amount_total:sum"],
    groupby=["partner_id"],
)
```

**CORRECT (19.0):**
```python
results = self.env["sale.order"]._read_group(
    domain=[("state", "=", "sale")],
    groupby=["partner_id"],
    aggregates=["amount_total:sum"],
)
```

**Why:** The public `read_group()` method was replaced. Use `_read_group()` for internal Python code or `formatted_read_group()` when you need the legacy dict-style output format.

### `models.Constraint` required for SQL constraints (`_sql_constraints` is silently dead)

**WRONG (fails silently in 19.0 -- no error, no constraint):**
```python
_sql_constraints = [
    ("code_unique", "UNIQUE(code)", "The code must be unique."),
]
```

**CORRECT (19.0):** the attribute name IS the constraint name.
```python
from odoo import models

_code_unique = models.Constraint(
    "UNIQUE(code)",
    "The code must be unique.",
)
```

**The attribute name MUST start with `_`** (verified on `odoo/orm/table_objects.py`, 19.0
build 2026-08): `code_unique = models.Constraint(...)` (without underscore) fails at import with
`AssertionError: Names of SQL objects in a model must start with '_'` / `Error calling __set_name__
on 'Constraint' instance '...'`, i.e. the whole module fails to load. The DB constraint is named
`<table>_<name without the leading _>` (e.g. `res_company_expense_bill_reminder_days_positive`).
The same rule applies to `models.Index` (see below, already prefixed `_..._idx`).

**Why:** verified against `odoo/orm/model_classes.py` in the 19.0 source: the loader only does
`_logger.warning("Model attribute '_sql_constraints' is no longer supported, please define models.Constraint on the model.")`
when it sees `_sql_constraints` -- it is never parsed into an actual SQL constraint. A module
migrated from ≤18.0 that still declares `_sql_constraints` installs cleanly (only a log
warning) but the uniqueness/check constraint is **not present on the DB**, so invalid data
you expected to be rejected passes through. This is a data-integrity regression, not a
cosmetic deprecation -- always port to `models.Constraint` when touching a v19 model.

### `models.Index` (19.0) -- companion to `models.Constraint`

```python
from odoo import models

_journal_id_company_id_idx = models.Index("(journal_id, company_id)")
```

Same pattern as `models.Constraint`: the attribute name is arbitrary (by convention prefixed
`_..._idx`), the value is the raw index expression.

### Domain Construction — OR/AND Composition

WRONG (Odoo 19.0 — deprecated):
```python
from odoo.osv.expression import OR, AND
domain = OR([[('state', '=', 'draft')], [('state', '=', 'sent')]])
combined = AND([domain, [('active', '=', True)]])
```

CORRECT (Odoo 19.0):
```python
from odoo.fields import Domain
domain = Domain("state", "=", "draft") | Domain("state", "=", "sent")
combined = domain & Domain("active", "=", True)
```

CORRECT (Odoo 17.0-18.0 — expression module still available):
```python
from odoo.osv import expression
domain = expression.OR([[('state', '=', 'draft')], [('state', '=', 'sent')]])
```

Note: Simple list syntax `[('field', 'op', value)]` remains valid in all versions.
Use `Domain` class only when composing OR/AND logic in Odoo 19.0+.

### @api.private (Odoo 19.0+)

Marks methods as non-RPC-callable. Prevents external API access to internal logic.

**WRONG (Odoo 19.0 -- internal method exposed to RPC):**
```python
def _prepare_invoice_values(self):
    return {'partner_id': self.partner_id.id}
```

**CORRECT (Odoo 19.0 -- internal method protected):**
```python
@api.private
def _prepare_invoice_values(self):
    return {'partner_id': self.partner_id.id}
```

**Why:** Without `@api.private`, any method starting with `_` can still be called via XML-RPC or JSON-RPC by external integrations. `@api.private` blocks RPC access entirely, hardening internal logic against unauthorized external calls.

**Do NOT use `@api.private` on:**
- ORM overrides: `create()`, `write()`, `unlink()`
- Computed field methods with `@api.depends`
- Constraint methods with `@api.constrains`
- Onchange methods with `@api.onchange`
- Methods decorated with `@api.model` or `@api.model_create_multi`
- Methods called by XML actions or buttons (these need RPC access)
- ORM hooks: `_search_display_name()`, `_compute_display_name()`
- Cached methods with `@tools.ormcache`

**Use `@api.private` on:**
- `_prepare_*` helper methods
- `_get_*` internal data retrieval
- `_audit_*` internal audit helpers
- `_webhook_*` internal extension points
- `_post_*` internal processing hooks
- Any standalone `_check_*` validator not decorated with `@api.constrains`
