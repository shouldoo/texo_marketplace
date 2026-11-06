---
type: "Reference"
title: "Viste — Delta Odoo 18"
description: "Viste — Delta Odoo 18: i cambi di Odoo 18 rispetto alla versione prima, da leggere con le lezioni del tag views e con il codice della versione."
tags: ["views", "v18"]
---

# Viste — Delta Odoo 18

> Per i progetti su Odoo 18, insieme alle lezioni del hub con il tag `views` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-18` (`.texo/THREADS.md`). Breaking change 17→18 ed errori specifici della versione.

| Cosa cambia | Prima (17.0) | Ora (18.0) | Impatto |
|-------------|---------------|------------|--------|
| Tag `<tree>` | Valido per le viste lista | **RIMOSSO** -- usare solo `<list>` | **Incompatibile** -- `ValueError: Wrong value for ir.ui.view.type: 'tree'` |
| `view_mode="tree,form"` | Corretto per le azioni | Usare `view_mode="list,form"` | **Incompatibile** -- le azioni finestra non mostrano la vista lista |
| Forma breve `<chatter/>` | Funziona (funziona anche la forma estesa) | **Preferita** (la forma estesa funziona ancora) | **Stile** -- la forma estesa non serve |
| Tipo `tree` di `ir.ui.view` | Tipo di vista valido | **RIMOSSO** dal registro | **Incompatibile** -- non si possono creare viste di tipo `tree` |

### Tag `<tree>` RIMOSSO -- usare `<list>`

**SBAGLIATO (errore bloccante in 18.0):**
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

**CORRETTO (18.0):**
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

**Perché:** Odoo 18 ha rimosso del tutto il tipo di vista `tree` dal registro. Usare `<tree>` causa
`ValueError: Wrong value for ir.ui.view.type: 'tree'`. È un errore bloccante, non un avviso.

### Va cambiato anche `view_mode` nelle azioni

**SBAGLIATO (18.0):**
```xml
<field name="view_mode">tree,form</field>
```

**CORRETTO (18.0):**
```xml
<field name="view_mode">list,form</field>
```

**Perché:** il valore `tree` in `view_mode` non è più riconosciuto. Se si usa `tree`, le azioni non mostrano
la vista lista.

### Forma breve `<chatter/>` preferita

**Forma estesa 17.0 (funziona ancora in 18.0 ma non serve):**
```xml
<div class="oe_chatter">
    <field name="message_follower_ids"/>
    <field name="activity_ids"/>
    <field name="message_ids"/>
</div>
```

**Forma preferita in 18.0:**
```xml
<chatter/>
```

**Perché:** la forma breve `<chatter/>` mostra automaticamente tutti i componenti di mail. In 18.0 la forma
estesa non serve e aggiunge solo rumore all'XML.
