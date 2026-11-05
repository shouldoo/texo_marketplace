---
type: "Reference"
title: "Models & ORM — Delta Odoo 18"
description: "Models & ORM — Delta Odoo 18: i cambi di Odoo 18 rispetto alla versione prima, da leggere con le lesson del tag models e con il codice della versione."
tags: ["models", "v18"]
---

# Models & ORM — Delta Odoo 18

> Per i progetti su Odoo 18, insieme alle lesson del hub con il tag `models` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-18` (`.texo/THREADS.md`). Breaking change 17→18 ed errori specifici della versione.

## Changed in 18.0

| What Changed | Before (17.0) | Now (18.0) | Impact |
|-------------|---------------|------------|--------|
| `states=` parameter | Allowed on field definitions (though discouraged) | **REMOVED** entirely | **Breaking** -- field definitions with `states=` cause errors |
| `group_operator=` | Correct name for aggregation | Renamed to `aggregator=` | **Silent failure** -- aggregation stops working if using old name |
| `_name_search()` | Override for custom search | Replaced by `_search_display_name()` | **Breaking** -- custom `_name_search()` overrides are ignored |
| `name_get()` | Override for display name | Deprecated -- use `display_name` compute field | **Deprecation** -- still works but will be removed |
| `check_access_rights()` + `check_access_rule()` | Separate methods | Consolidated into `record.check_access()` | **Breaking** -- old methods deprecated |
| `numbercall` on `ir.cron` | Field available for limiting cron runs | **REMOVED** from `ir.cron` model | **Breaking** -- data files with `numbercall` cause errors |

### `states=` parameter REMOVED

**WRONG (causes error in 18.0):**
```python
amount = fields.Float(
    string="Amount",
    states={"posted": [("readonly", True)]},
)
```

**CORRECT (18.0):**
```python
amount = fields.Float(string="Amount")
# Handle conditional readonly in XML view:
# <field name="amount" readonly="state == 'posted'"/>
```

**Why:** Odoo 18 completely removed the `states` parameter from Python field definitions. Conditional field behavior must be handled entirely in XML views using inline modifier expressions.

### `group_operator` renamed to `aggregator`

**WRONG (silent failure in 18.0):**
```python
quantity = fields.Float(string="Quantity", group_operator="avg")
```

**CORRECT (18.0):**
```python
quantity = fields.Float(string="Quantity", aggregator="avg")
```

**Why:** Renamed for clarity. The `group_operator` parameter is silently ignored in 18.0, causing aggregation in list views to stop working.

### `_name_search()` replaced by `_search_display_name()`

**WRONG (ignored in 18.0):**
```python
@api.model
def _name_search(self, name, domain=None, operator='ilike', limit=100, order=None):
    ...
```

**CORRECT (18.0):**
```python
@api.model
def _search_display_name(self, name, domain=None, operator='ilike', limit=100, order=None):
    ...
```

**Why:** The method was replaced to support broader search capabilities. Custom `_name_search()` overrides are silently ignored in 18.0.
