---
type: "Reference"
title: "Viste — Delta Odoo 19"
description: "Viste — Delta Odoo 19: i cambi di Odoo 19 rispetto alla versione prima, da leggere con le lezioni del tag views e con il codice della versione."
tags: ["views", "v19"]
---

# Viste — Delta Odoo 19

> Per i progetti su Odoo 19, insieme alle lezioni del hub con il tag `views` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-19` (`.texo/THREADS.md`). Breaking change 18→19 ed errori specifici della versione.

| Cosa cambia | Prima (18.0) | Ora (19.0) | Impatto |
|-------------|---------------|------------|--------|
| Template della card kanban | `t-name="kanban-box"` | `t-name="card"` | **Incompatibile** -- le viste kanban con il vecchio nome di template non vengono mostrate |
| `t-esc` di QWeb | Disponibile | **Deprecato** -- usare `t-out` | **Avviso di deprecazione** -- `t-esc` funziona ancora ma genera avvisi |
| Tag `<list>` | Valido (introdotto in 18.0) | Uguale, nessun cambiamento | Nessun cambiamento rispetto alla 18.0 |
| Forma breve `<chatter/>` | Preferita | Uguale, nessun cambiamento | Nessun cambiamento rispetto alla 18.0 |

### Template della card kanban: `kanban-box` sostituito da `card`

**SBAGLIATO (fallisce in 19.0):**
```xml
<kanban>
    <templates>
        <t t-name="kanban-box">
            <div class="oe_kanban_card">
                <field name="name"/>
            </div>
        </t>
    </templates>
</kanban>
```

**CORRETTO (19.0):**
```xml
<kanban>
    <templates>
        <t t-name="card">
            <field name="name"/>
        </t>
    </templates>
</kanban>
```

**Perché:** Odoo 19 ha rinominato il template della card kanban da `kanban-box` a `card` e ne ha semplificato
la struttura. Il `<div class="oe_kanban_card">` che avvolgeva la card non serve più -- il contenitore della
card viene fornito automaticamente.

### QWeb: `t-esc` deprecato -- usare `t-out`

**SBAGLIATO (genera un avviso di deprecazione in 19.0):**
```xml
<span t-esc="record.name.value"/>
```

**CORRETTO (19.0):**
```xml
<span t-out="record.name.value"/>
```

**Perché:** `t-out` è il sostituto moderno sia di `t-esc` (output con escape) sia di `t-raw` (output HTML
grezzo). In 19.0 `t-esc` genera avvisi di deprecazione. `t-out` applica l'escape per default e supporta
`Markup()` per l'HTML sicuro.

### Validare l'XML delle viste con lo schema RNG -- nessun `form_view.rng`, e `tree_view.rng` sparito dalla 18.0

Se si valida a mano l'arch di una vista con gli schemi RelaxNG di Odoo (`odoo/addons/base/rng/` nei sorgenti
di destinazione), tenere presenti due cose (verificate direttamente sui sorgenti di Odoo dalla 16.0 alla 19.0):

- **`form_view.rng` non è mai esistito** dalla 16.0 alla 19.0 -- le viste form non sono validate affatto con
  uno schema RNG; non cercarlo.
- **`tree_view.rng` esisteva fino alla 17.0**, è stato **rimosso in 18.0** (non in 19.0) quando è stato
  introdotto `list_view.rng` insieme alla rinomina dell'arch `<tree>`→`<list>`, e resta assente in 19.0.

| File di schema | 16.0/17.0 | 18.0/19.0 |
|---|---|---|
| `common.rng`, `search_view.rng`, `graph_view.rng`, `pivot_view.rng`, `calendar_view.rng`, `activity_view.rng` | presente | presente |
| `tree_view.rng` | presente | **rimosso** (già in 18.0) |
| `list_view.rng` | assente | presente |
| `form_view.rng` | mai esistito | mai esistito |

Uno script di validazione v19 che punta a `form_view.rng`/`tree_view.rng` fallisce con file non trovato, non
con un vero errore di schema -- per le viste `<list>` validare con `list_view.rng`; per `<form>` non esiste
validazione a livello di schema in nessuna di queste versioni.
