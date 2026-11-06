---
type: "Reference"
title: "Modelli e ORM — Delta Odoo 18"
description: "Modelli e ORM — Delta Odoo 18: i cambi di Odoo 18 rispetto alla versione prima, da leggere con le lezioni del tag models e con il codice della versione."
tags: ["models", "v18"]
---

# Modelli e ORM — Delta Odoo 18

> Per i progetti su Odoo 18, insieme alle lezioni del hub con il tag `models` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-18` (`.texo/THREADS.md`). Breaking change 17→18 ed errori specifici della versione.

## Cambiato in 18.0

| Cosa cambia | Prima (17.0) | Ora (18.0) | Impatto |
|-------------|---------------|------------|--------|
| Parametro `states=` | Ammesso nelle definizioni dei campi (anche se sconsigliato) | **RIMOSSO** del tutto | **Incompatibile** -- le definizioni di campo con `states=` danno errore |
| `group_operator=` | Nome corretto per l'aggregazione | Rinominato `aggregator=` | **Errore silenzioso** -- con il vecchio nome l'aggregazione smette di funzionare |
| `_name_search()` | Override per la ricerca custom | Sostituito da `_search_display_name()` | **Incompatibile** -- gli override custom di `_name_search()` vengono ignorati |
| `name_get()` | Override per il nome visualizzato | Deprecato -- usare il campo compute `display_name` | **Deprecazione** -- funziona ancora ma sarà rimosso |
| `check_access_rights()` + `check_access_rule()` | Metodi separati | Riuniti in `record.check_access()` | **Incompatibile** -- i vecchi metodi sono deprecati |
| `numbercall` su `ir.cron` | Campo disponibile per limitare le esecuzioni del cron | **RIMOSSO** dal modello `ir.cron` | **Incompatibile** -- i file dati con `numbercall` danno errore |

### Parametro `states=` RIMOSSO

**SBAGLIATO (errore in 18.0):**
```python
amount = fields.Float(
    string="Amount",
    states={"posted": [("readonly", True)]},
)
```

**CORRETTO (18.0):**
```python
amount = fields.Float(string="Amount")
# Il readonly condizionale si gestisce nella vista XML:
# <field name="amount" readonly="state == 'posted'"/>
```

**Perché:** Odoo 18 ha rimosso del tutto il parametro `states` dalle definizioni Python dei campi. Il
comportamento condizionale dei campi va gestito interamente nelle viste XML con espressioni inline nei
modificatori.

### `group_operator` rinominato `aggregator`

**SBAGLIATO (errore silenzioso in 18.0):**
```python
quantity = fields.Float(string="Quantity", group_operator="avg")
```

**CORRETTO (18.0):**
```python
quantity = fields.Float(string="Quantity", aggregator="avg")
```

**Perché:** rinominato per chiarezza. In 18.0 il parametro `group_operator` viene ignorato senza avvisi, e
l'aggregazione nelle viste lista smette di funzionare.

### `_name_search()` sostituito da `_search_display_name()`

**SBAGLIATO (ignorato in 18.0):**
```python
@api.model
def _name_search(self, name, domain=None, operator='ilike', limit=100, order=None):
    ...
```

**CORRETTO (18.0):**
```python
@api.model
def _search_display_name(self, name, domain=None, operator='ilike', limit=100, order=None):
    ...
```

**Perché:** il metodo è stato sostituito per supportare capacità di ricerca più ampie. In 18.0 gli override
custom di `_name_search()` vengono ignorati senza avvisi.
