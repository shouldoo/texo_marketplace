---
type: "Reference"
title: "Data Files — Delta Odoo 19"
description: "Data Files — Delta Odoo 19: i cambi di Odoo 19 rispetto alla versione prima, da leggere con le lesson del tag data e con il codice della versione."
tags: ["data", "v19"]
---

# Data Files — Delta Odoo 19

> Per i progetti su Odoo 19, insieme alle lesson del hub con il tag `data` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-19` (`.texo/THREADS.md`). Breaking change 18→19 ed errori specifici della versione.

## Changed in 19.0

The plain data file *format* (XML/CSV, `noupdate`, `ref=`, `eval=`) is unchanged, but
several record types that live in data files had **field/model changes** in 19.0:

| What Changed | Before (18.0) | Now (19.0) | Impact |
|-------------|---------------|------------|--------|
| `<report>` shortcut element | Valid | **Removed** | **Breaking** -- `Element odoo has extra content: report`; use `<record model="ir.actions.report">` |
| `ir.cron.numbercall` / `doall` | `numbercall` already gone in 18.0 | `doall` also **removed** | **Breaking** -- drop both fields from cron data |
| `mail.template.report_name` | Field present | **Removed** | **Breaking** -- drop field |
| `mail.template.report_template` (M2o) | Single report | **Renamed** to `report_template_ids` (M2m) | **Breaking** |
| `mail.template` body Jinja `${expr}` | Jinja2 | QWeb `{{ expr }}` | **Breaking** -- old `${...}` no longer interpolated |
| `base.automation` `state` / `code` | Fields on `base.automation` | **Split out** to separate `ir.actions.server` records, linked via M2m `action_server_ids` | **Breaking** -- `Invalid field 'state' in 'base.automation'` |
| `res.config.settings` view | `<div id="X">` anchors | `<setting id="X">` blocks (new settings layout) | **Breaking** -- old anchors fail xpath |
| `documents.document` folder records | Model `documents.folder` | Unificato in `documents.document` (`type='folder'`); richiede `<field name="access_internal">edit</field>` | **Breaking** -- senza `access_internal`, default `'none'` blocca lettura/scrittura a tutti gli utenti interni (`global read rule`) |

### `base.automation` model split

In 19.0 the automation rule no longer carries `state`/`code` directly. Create the
server action separately and link it:

```xml
<record id="server_action_x" model="ir.actions.server">
    <field name="name">Do X</field>
    <field name="model_id" ref="model_my_model"/>
    <field name="state">code</field>
    <field name="code">records.do_x()</field>
</record>
<record id="automation_x" model="base.automation">
    <field name="name">On create do X</field>
    <field name="model_id" ref="model_my_model"/>
    <field name="trigger">on_create</field>
    <field name="action_server_ids" eval="[(4, ref('server_action_x'))]"/>
</record>
```

### `static/description/index.html` must not start with an XML declaration

A leading `<?xml version="1.0"?>` in `static/description/index.html` makes lxml raise
`Unicode strings with encoding declaration are not supported`. Drop the declaration —
start the file with the HTML content directly.
