---
type: "Reference"
title: "Security — Delta Odoo 19"
description: "Security — Delta Odoo 19: i cambi di Odoo 19 rispetto alla versione prima, da leggere con le lesson del tag security e con il codice della versione."
tags: ["security", "v19"]
---

# Security — Delta Odoo 19

> Per i progetti su Odoo 19, insieme alle lesson del hub con il tag `security` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-19` (`.texo/THREADS.md`). Breaking change 18→19 ed errori specifici della versione.

## Changed in 19.0

| What Changed | Before (18.0) | Now (19.0) | Impact |
|-------------|---------------|------------|--------|
| Security groups `category_id` | Used to associate groups with module categories | **Replaced** by `privilege_id` | **Breaking** -- group XML using `category_id` must use `privilege_id` instead |
| `res.groups.users` | M2m to users | **Renamed** to `user_ids` | **Breaking** -- `Invalid field 'users' in 'res.groups'` |
| `ir.actions.act_window.groups_id` | Group restriction on actions | **Renamed** to `group_ids` | **Breaking** -- `Invalid field 'groups_id' in 'ir.actions.act_window'` |
| `res.users.groups_id` | M2m to `res.groups` on the user record | **Renamed** to `group_ids` | **Breaking** -- distinct field from the `ir.actions.act_window` one above (different model, same old/new names): `self.env.user.groups_id` → `self.env.user.group_ids` |
| `documents.document` folder access | `documents.folder` model | Unificato in `documents.document` (`type='folder'`); richiede `access_internal` esplicito | **Breaking** -- default `access_internal='none'` blocca utenti interni con `Documents.document: global read rule` |
| ACLs and record rules | Same format | Same, unchanged | No breaking changes |

### Security groups: new `res.groups.privilege` intermediate model

In Odoo 19, a new model `res.groups.privilege` sits between `ir.module.category` and `res.groups`:

```
ir.module.category  →  res.groups.privilege  →  res.groups
```

**WRONG (19.0) — `category_id` directly on `res.groups`:**
```xml
<record id="module_category_library" model="ir.module.category">
    <field name="name">Library</field>
</record>
<record id="group_library_user" model="res.groups">
    <field name="name">User</field>
    <field name="category_id" ref="module_category_library"/>  <!-- does not exist in 19 -->
</record>
```

**CORRECT (19.0) — three-level chain:**
```xml
<!-- 1. Module category (unchanged) -->
<record id="module_category_library" model="ir.module.category">
    <field name="name">Library</field>
    <field name="sequence">100</field>
    <field name="visible">True</field>
</record>

<!-- 2. Privilege (new in 19.0): groups within this privilege share a selection -->
<record id="privilege_library" model="res.groups.privilege">
    <field name="name">Library</field>
    <field name="category_id" ref="module_category_library"/>
</record>

<!-- 3. Groups reference privilege_id, not category_id -->
<record id="group_library_user" model="res.groups">
    <field name="name">User</field>
    <field name="privilege_id" ref="privilege_library"/>
</record>
<record id="group_library_manager" model="res.groups">
    <field name="name">Manager</field>
    <field name="privilege_id" ref="privilege_library"/>
    <field name="implied_ids" eval="[(4, ref('group_library_user'))]"/>
</record>
```

**Why:** Odoo 19 introduced `res.groups.privilege` to decouple privilege grouping from module categories. `res.groups.category_id` no longer exists; `res.groups.privilege_id` is the new FK. The privilege's `name` is what appears as the section header in the user form. Group names within a privilege must be unique (`UNIQUE(privilege_id, name)` SQL constraint).

### Accounting: `account.group_account_user` is a feature toggle, NOT the accountant role

In 19.0 `account.group_account_user` is "Show Full Accounting Features" (implies
`group_account_basic` + `group_account_readonly`): a technical switch that, once the full
accounting features are enabled, ends up on every internal user. The roles are
`account.group_account_invoice` ("Invoicing") and `account.group_account_manager`
("Administrator", implies `group_account_invoice` but **not** `group_account_user`; verified on
`account/security/account_security.xml`). Using `group_account_user` for "accounting users" in
`groups=`, ACLs or code (`has_group`) either excludes the real accountants or opens the feature to
everybody.

**WRONG:** `groups="account.group_account_user"` / `has_group('account.group_account_user')` to mean "accountant".
**CORRECT:** `account.group_account_invoice` (the manager implies it).

Native consequence to remember: `hr_expense` gives the "see every employee's expense" record rule
(`ir_rule_hr_expense_manager`) to `account.group_account_user` and
`hr_expense.group_hr_expense_user`, not to `group_account_invoice`. An Invoicing-only user sees just
the expenses of the employees they manage: a module whose accounting users must read other
employees' expenses has to add its own `ir.rule` for `account.group_account_invoice` (restrict the
domain, e.g. to approved expenses).

### Odoo 19 Enterprise Documents: `documents.document` e `access_internal` (Enterprise, fuori ambito)

In Odoo 19 il modello `documents.folder` è stato rimosso e unificato in `documents.document` (`type='folder'`). Il nuovo motore dei permessi applica la regola globale:
- `Documents.document: global read rule`: `[('user_permission', '!=', 'none')]`
- `Documents.document: global create rule`: `['|', ('folder_id.user_permission', '=', 'edit'), ('folder_id', '=', False)]`

**Regola essenziale per cartelle definite via XML o via codice**:
1. **Nei file dati XML**: quando si definisce un record cartella radice (`model="documents.document"`), specificare sempre esplicitamente `access_internal`:
   ```xml
   <record id="folder_custom_root" model="documents.document">
       <field name="name">Mia Cartella</field>
       <field name="type">folder</field>
       <field name="folder_id" eval="False"/>
       <field name="access_internal">edit</field> <!-- OBBLIGATORIO: altrimenti default 'none' -->
   </record>
   ```
   Senza `access_internal="edit"` (o `"view"`), il default è `'none'` e nessun utente interno (neanche Admin) avrà permessi di lettura/scrittura sulla cartella e sulle relative sotto-cartelle figlie (che ereditano `access_internal` dal genitore).
2. **Nei metodi Python di integrazione** (es. creazione automatica cartella legata a un record):
   - Creare la cartella con `.sudo()`, impostando esplicitamente `'access_internal': 'edit'`.
   - In questo modo gli utenti con permessi di business sul modello padre non vengono bloccati dalla record rule di `documents.document` durante il salvataggio.

