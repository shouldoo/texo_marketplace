---
type: "Reference"
title: "Modelli e ORM — Delta Odoo 19"
description: "Modelli e ORM — Delta Odoo 19: i cambi di Odoo 19 rispetto alla versione prima, da leggere con le lezioni del tag models e con il codice della versione."
tags: ["models", "v19"]
---

# Modelli e ORM — Delta Odoo 19

> Per i progetti su Odoo 19, insieme alle lezioni del hub con il tag `models` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-19` (`.texo/THREADS.md`). Breaking change 18→19 ed errori specifici della versione.

## Cambiato in 19.0

| Cosa cambia | Prima (18.0) | Ora (19.0) | Impatto |
|-------------|---------------|------------|--------|
| `name_get()` | Deprecato (funziona ancora) | **Rimosso del tutto** | **Incompatibile** -- qualsiasi override di `name_get()` causa `AttributeError` |
| `read_group()` | Metodo dell'API pubblica | **Sostituito** da `_read_group()` e `formatted_read_group()` | **Incompatibile** -- le chiamate dirette a `read_group()` falliscono |
| `@api.returns` | Disponibile (deprecato) | **Rimosso** | **Incompatibile** -- il decoratore causa `AttributeError` |
| `_sql_constraints` | Lista standard di tuple | Classe `models.Constraint` **obbligatoria** | **Incompatibile** -- il vecchio attributo produce solo un avviso nel log e il vincolo non viene mai creato, senza avvisi (sul DB non finisce nessun vincolo SQL) |
| Espressioni di dominio | `from odoo.osv import expression` + `expression.OR(...)` | `from odoo.fields import Domain` + `Domain(...) \| Domain(...)` | **Nuova API** -- il vecchio import funziona ancora ma è preferita la nuova classe `Domain` |
| `self.user_has_groups('xmlid')` | Metodo sui modelli | **Rimosso** | **Incompatibile** -- `AttributeError`; usare `self.env.user.has_group('xmlid')` |
| `@api.depends('id')` | Tollerato | **Vietato** -- solleva `NotImplementedError` | **Incompatibile** -- un compute non può dipendere da `id` |
| `from odoo.addons.http_routing.models.ir_http import slug` | Importabile | **Rimosso** | **Incompatibile** -- usare `IrHttp._slug` (vedi sotto) |
| `from odoo.addons.base.models.res_partner import WARNING_MESSAGE` | Importabile | **Rimosso** | **Incompatibile** -- togliere l'import |

### `user_has_groups` rimosso → `has_group`

```python
# SBAGLIATO (≤18.0):
if self.user_has_groups('stock.group_stock_manager'):
    ...
# CORRETTO (19.0): has_group (singolare) su res.users è l'API pubblica
if self.env.user.has_group('stock.group_stock_manager'):
    ...
```

### Import di `slug` spostato

```python
# SBAGLIATO (≤18.0):
from odoo.addons.http_routing.models.ir_http import slug
# CORRETTO (19.0):
from odoo.addons.base.models.ir_http import IrHttp
slug = IrHttp._slug
```

### Mai `@classmethod` sugli override CRUD dell'ORM

`create()`, `write()`, `default_get()` sono metodi **di istanza**. Un `@classmethod` rimasto o errato (a volte
ereditato da codice vecchio o da uno scaffolding) rompe la firma:
`TypeError: BaseModel.<method>() missing 1 required positional argument`. Toglierlo sempre.

### `name_get()` rimosso del tutto -- usare `_compute_display_name()`

**SBAGLIATO (errore in 19.0):**
```python
def name_get(self):
    result = []
    for record in self:
        result.append((record.id, f"[{record.code}] {record.name}"))
    return result
```

**CORRETTO (19.0):**
```python
@api.depends("code", "name")
def _compute_display_name(self):
    for record in self:
        record.display_name = f"[{record.code}] {record.name}"
```

**Perché:** `name_get()` era deprecato in 18.0 ed è stato rimosso del tutto in 19.0. Usare invece il campo
calcolato `display_name` con `_compute_display_name()`. Questo metodo è un normale metodo compute decorato con
`@api.depends`.

### `read_group()` sostituito da `_read_group()` e `formatted_read_group()`

**SBAGLIATO (fallisce in 19.0):**
```python
results = self.env["sale.order"].read_group(
    domain=[("state", "=", "sale")],
    fields=["partner_id", "amount_total:sum"],
    groupby=["partner_id"],
)
```

**CORRETTO (19.0):**
```python
results = self.env["sale.order"]._read_group(
    domain=[("state", "=", "sale")],
    groupby=["partner_id"],
    aggregates=["amount_total:sum"],
)
```

**Perché:** il metodo pubblico `read_group()` è stato sostituito. Usare `_read_group()` nel codice Python
interno, oppure `formatted_read_group()` quando serve il vecchio formato di output a dict.

### `models.Constraint` obbligatorio per i vincoli SQL (`_sql_constraints` è morto senza avvisi)

**SBAGLIATO (fallisce senza avvisi in 19.0 -- nessun errore, nessun vincolo):**
```python
_sql_constraints = [
    ("code_unique", "UNIQUE(code)", "The code must be unique."),
]
```

**CORRETTO (19.0):** il nome dell'attributo È il nome del vincolo.
```python
from odoo import models

_code_unique = models.Constraint(
    "UNIQUE(code)",
    "The code must be unique.",
)
```

**Il nome dell'attributo DEVE iniziare con `_`** (verificato su `odoo/orm/table_objects.py`, build 19.0
2026-08): `code_unique = models.Constraint(...)` (senza underscore) fallisce all'import con
`AssertionError: Names of SQL objects in a model must start with '_'` / `Error calling __set_name__
on 'Constraint' instance '...'`, cioè l'intero modulo non si carica. Il vincolo sul DB si chiama
`<tabella>_<nome senza il _ iniziale>` (es. `res_company_expense_bill_reminder_days_positive`).
La stessa regola vale per `models.Index` (vedi sotto, già con il prefisso `_..._idx`).

**Perché:** verificato su `odoo/orm/model_classes.py` nei sorgenti 19.0: quando trova `_sql_constraints` il
loader si limita a
`_logger.warning("Model attribute '_sql_constraints' is no longer supported, please define models.Constraint on the model.")`
: l'attributo non viene mai trasformato in un vero vincolo SQL. Un modulo migrato da ≤18.0 che dichiara ancora
`_sql_constraints` si installa senza errori (solo un avviso nel log) ma il vincolo di unicità/check **non è
presente sul DB**, e i dati non validi che ci si aspettava fossero respinti passano. È una regressione
dell'integrità dei dati, non una deprecazione cosmetica -- portare sempre a `models.Constraint` quando si tocca
un modello v19.

### `models.Index` (19.0) -- il compagno di `models.Constraint`

```python
from odoo import models

_journal_id_company_id_idx = models.Index("(journal_id, company_id)")
```

Stesso pattern di `models.Constraint`: il nome dell'attributo è libero (per convenzione con il prefisso
`_..._idx`), il valore è l'espressione grezza dell'indice.

### Costruzione dei domini — composizione OR/AND

SBAGLIATO (Odoo 19.0 — deprecato):
```python
from odoo.osv.expression import OR, AND
domain = OR([[('state', '=', 'draft')], [('state', '=', 'sent')]])
combined = AND([domain, [('active', '=', True)]])
```

CORRETTO (Odoo 19.0):
```python
from odoo.fields import Domain
domain = Domain("state", "=", "draft") | Domain("state", "=", "sent")
combined = domain & Domain("active", "=", True)
```

CORRETTO (Odoo 17.0-18.0 — il modulo expression è ancora disponibile):
```python
from odoo.osv import expression
domain = expression.OR([[('state', '=', 'draft')], [('state', '=', 'sent')]])
```

Nota: la semplice sintassi a lista `[('field', 'op', value)]` resta valida in tutte le versioni.
Usare la classe `Domain` solo quando si compone logica OR/AND in Odoo 19.0 e successive.

### @api.private (Odoo 19.0 e successive)

Marca i metodi come non richiamabili via RPC. Impedisce l'accesso alla logica interna dall'API esterna.

**SBAGLIATO (Odoo 19.0 -- metodo interno esposto a RPC):**
```python
def _prepare_invoice_values(self):
    return {'partner_id': self.partner_id.id}
```

**CORRETTO (Odoo 19.0 -- metodo interno protetto):**
```python
@api.private
def _prepare_invoice_values(self):
    return {'partner_id': self.partner_id.id}
```

**Perché:** senza `@api.private`, qualsiasi metodo che inizia con `_` può ancora essere chiamato via XML-RPC o
JSON-RPC dalle integrazioni esterne. `@api.private` blocca del tutto l'accesso RPC e protegge la logica
interna dalle chiamate esterne non autorizzate.

**NON usare `@api.private` su:**
- override dell'ORM: `create()`, `write()`, `unlink()`
- metodi dei campi calcolati con `@api.depends`
- metodi di vincolo con `@api.constrains`
- metodi onchange con `@api.onchange`
- metodi decorati con `@api.model` o `@api.model_create_multi`
- metodi chiamati da azioni XML o da pulsanti (hanno bisogno dell'accesso RPC)
- hook dell'ORM: `_search_display_name()`, `_compute_display_name()`
- metodi in cache con `@tools.ormcache`

**Usare `@api.private` su:**
- metodi di supporto `_prepare_*`
- lettura interna di dati `_get_*`
- metodi di supporto interni per l'audit `_audit_*`
- punti di estensione interni `_webhook_*`
- hook interni di elaborazione `_post_*`
- qualsiasi validatore `_check_*` a sé stante non decorato con `@api.constrains`
