---
type: "Reference"
title: "File dati — Delta Odoo 19"
description: "File dati — Delta Odoo 19: i cambi di Odoo 19 rispetto alla versione prima, da leggere con le lezioni del tag data e con il codice della versione."
tags: ["data", "v19"]
---

# File dati — Delta Odoo 19

> Per i progetti su Odoo 19, insieme alle lezioni del hub con il tag `data` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-19` (`.texo/THREADS.md`). Breaking change 18→19 ed errori specifici della versione.

## Cambiato in 19.0

Il *formato* dei file dati in sé (XML/CSV, `noupdate`, `ref=`, `eval=`) non cambia, ma diversi tipi di record
che vivono nei file dati hanno avuto **cambi di campi/modelli** in 19.0:

| Cosa cambia | Prima (18.0) | Ora (19.0) | Impatto |
|-------------|---------------|------------|--------|
| Elemento abbreviato `<report>` | Valido | **Rimosso** | **Incompatibile** -- `Element odoo has extra content: report`; usare `<record model="ir.actions.report">` |
| `ir.cron.numbercall` / `doall` | `numbercall` già sparito in 18.0 | **Rimosso** anche `doall` | **Incompatibile** -- togliere entrambi i campi dai dati dei cron |
| `mail.template.report_name` | Campo presente | **Rimosso** | **Incompatibile** -- togliere il campo |
| `mail.template.report_template` (M2o) | Un solo report | **Rinominato** `report_template_ids` (M2m) | **Incompatibile** |
| Corpo Jinja `${expr}` di `mail.template` | Jinja2 | QWeb `{{ expr }}` | **Incompatibile** -- il vecchio `${...}` non viene più interpolato |
| `state` / `code` di `base.automation` | Campi su `base.automation` | **Separati** in record `ir.actions.server` distinti, collegati tramite il M2m `action_server_ids` | **Incompatibile** -- `Invalid field 'state' in 'base.automation'` |
| Vista di `res.config.settings` | Ancore `<div id="X">` | Blocchi `<setting id="X">` (nuovo layout delle impostazioni) | **Incompatibile** -- gli xpath sulle vecchie ancore falliscono |
| Record cartella di `documents.document` | Modello `documents.folder` | Unificato in `documents.document` (`type='folder'`); richiede `<field name="access_internal">edit</field>` | **Incompatibile** -- senza `access_internal`, il default `'none'` blocca lettura/scrittura a tutti gli utenti interni (`global read rule`) |

### Separazione del modello `base.automation`

In 19.0 la regola di automazione non porta più direttamente `state`/`code`. Creare a parte l'azione server e
collegarla:

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

### `static/description/index.html` non deve iniziare con una dichiarazione XML

Un `<?xml version="1.0"?>` iniziale in `static/description/index.html` fa sollevare a lxml
`Unicode strings with encoding declaration are not supported`. Togliere la dichiarazione e iniziare il file
direttamente con il contenuto HTML.
