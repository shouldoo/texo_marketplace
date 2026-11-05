---
type: "Reference"
title: "Views — Delta Odoo 19"
description: "Views — Delta Odoo 19: i cambi di Odoo 19 rispetto alla versione prima, da leggere con le lesson del tag views e con il codice della versione."
tags: ["views", "v19"]
---

# Views — Delta Odoo 19

> Per i progetti su Odoo 19, insieme alle lesson del hub con il tag `views` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-19` (`.texo/THREADS.md`). Breaking change 18→19 ed errori specifici della versione.

| What Changed | Before (18.0) | Now (19.0) | Impact |
|-------------|---------------|------------|--------|
| Kanban card template | `t-name="kanban-box"` | `t-name="card"` | **Breaking** -- kanban views using old template name fail to render |
| QWeb `t-esc` | Available | **Deprecated** -- use `t-out` | **Deprecation warning** -- `t-esc` still works but triggers warnings |
| `<list>` tag | Valid (introduced in 18.0) | Same, unchanged | No change from 18.0 |
| `<chatter/>` shorthand | Preferred | Same, unchanged | No change from 18.0 |

### Kanban card template: `kanban-box` replaced by `card`

**WRONG (fails in 19.0):**
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

**CORRECT (19.0):**
```xml
<kanban>
    <templates>
        <t t-name="card">
            <field name="name"/>
        </t>
    </templates>
</kanban>
```

**Why:** Odoo 19 renamed the kanban card template from `kanban-box` to `card` and simplified the card structure. The wrapping `<div class="oe_kanban_card">` is no longer needed -- the card container is provided automatically.

### QWeb: `t-esc` deprecated -- use `t-out`

**WRONG (triggers deprecation in 19.0):**
```xml
<span t-esc="record.name.value"/>
```

**CORRECT (19.0):**
```xml
<span t-out="record.name.value"/>
```

**Why:** `t-out` is the modern replacement for both `t-esc` (escaped output) and `t-raw` (raw HTML output). In 19.0, `t-esc` triggers deprecation warnings. `t-out` escapes by default and supports `Markup()` for safe HTML.

### Validating view XML against the RNG schema -- no `form_view.rng`, and `tree_view.rng` gone since 18.0

If you validate a view's arch by hand against Odoo's RelaxNG schemas
(`odoo/addons/base/rng/` in the target source), be aware of two things (verified directly
against the sources of Odoo 16.0 through 19.0):

- **`form_view.rng` has never existed** in 16.0 through 19.0 -- form views are not
  RNG-schema-validated at all; do not look for it.
- **`tree_view.rng` existed through 17.0**, was **removed in 18.0** (not 19.0) when
  `list_view.rng` was introduced alongside the `<tree>`→`<list>` arch rename, and stays
  absent in 19.0.

| Schema file | 16.0/17.0 | 18.0/19.0 |
|---|---|---|
| `common.rng`, `search_view.rng`, `graph_view.rng`, `pivot_view.rng`, `calendar_view.rng`, `activity_view.rng` | present | present |
| `tree_view.rng` | present | **removed** (already in 18.0) |
| `list_view.rng` | absent | present |
| `form_view.rng` | never existed | never existed |

A v19 validation script pointed at `form_view.rng`/`tree_view.rng` fails with file-not-found,
not a real schema error -- for `<list>` views validate against `list_view.rng`; there is no
schema-level validation available for `<form>` on any of these versions.
