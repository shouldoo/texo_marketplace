---
type: "Reference"
title: "Views — Delta Odoo 18"
description: "Views — Delta Odoo 18: i cambi di Odoo 18 rispetto alla versione prima, da leggere con le lesson del tag views e con il codice della versione."
tags: ["views", "v18"]
---

# Views — Delta Odoo 18

> Per i progetti su Odoo 18, insieme alle lesson del hub con il tag `views` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-18` (`.texo/THREADS.md`). Breaking change 17→18 ed errori specifici della versione.

| What Changed | Before (17.0) | Now (18.0) | Impact |
|-------------|---------------|------------|--------|
| `<tree>` tag | Valid for list views | **REMOVED** -- use `<list>` exclusively | **Breaking** -- `ValueError: Wrong value for ir.ui.view.type: 'tree'` |
| `view_mode="tree,form"` | Correct for actions | Use `view_mode="list,form"` | **Breaking** -- action windows show no list view |
| `<chatter/>` shorthand | Works (verbose form also works) | **Preferred** (verbose form still works) | **Style** -- verbose form is unnecessary |
| `ir.ui.view` type `tree` | Valid view type | **REMOVED** from the registry | **Breaking** -- cannot create views with type `tree` |

### `<tree>` tag REMOVED -- use `<list>`

**WRONG (causes hard error in 18.0):**
```xml
<record id="my_model_view_tree" model="ir.ui.view">
    <field name="name">my.model.tree</field>
    <field name="model">my.model</field>
    <field name="arch" type="xml">
        <tree>
            <field name="name"/>
            <field name="state"/>
        </tree>
    </field>
</record>
```

**CORRECT (18.0):**
```xml
<record id="my_model_view_list" model="ir.ui.view">
    <field name="name">my.model.list</field>
    <field name="model">my.model</field>
    <field name="arch" type="xml">
        <list>
            <field name="name"/>
            <field name="state"/>
        </list>
    </field>
</record>
```

**Why:** Odoo 18 completely removed the `tree` view type from the registry. Using `<tree>` causes `ValueError: Wrong value for ir.ui.view.type: 'tree'`. This is a hard error, not a warning.

### `view_mode` in actions must also change

**WRONG (18.0):**
```xml
<field name="view_mode">tree,form</field>
```

**CORRECT (18.0):**
```xml
<field name="view_mode">list,form</field>
```

**Why:** The `tree` value in `view_mode` is no longer recognized. Actions will not display a list view if `tree` is used.

### `<chatter/>` shorthand preferred

**17.0 verbose form (still works in 18.0 but unnecessary):**
```xml
<div class="oe_chatter">
    <field name="message_follower_ids"/>
    <field name="activity_ids"/>
    <field name="message_ids"/>
</div>
```

**18.0 preferred form:**
```xml
<chatter/>
```

**Why:** The `<chatter/>` shorthand renders all mail components automatically. In 18.0, the verbose form is unnecessary and adds XML noise.
