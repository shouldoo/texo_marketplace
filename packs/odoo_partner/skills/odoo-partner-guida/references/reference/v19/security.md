---
type: "Reference"
title: "Sicurezza — Delta Odoo 19"
description: "Sicurezza — Delta Odoo 19: i cambi di Odoo 19 rispetto alla versione prima, da leggere con le lezioni del tag security e con il codice della versione."
tags: ["security", "v19"]
---

# Sicurezza — Delta Odoo 19

> Per i progetti su Odoo 19, insieme alle lezioni del hub con il tag `security` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-19` (`.texo/THREADS.md`). Breaking change 18→19 ed errori specifici della versione.

## Cambiato in 19.0

| Cosa cambia | Prima (18.0) | Ora (19.0) | Impatto |
|-------------|---------------|------------|--------|
| `category_id` dei gruppi di sicurezza | Usato per associare i gruppi alle categorie di modulo | **Sostituito** da `privilege_id` | **Incompatibile** -- l'XML dei gruppi che usa `category_id` deve usare invece `privilege_id` |
| `res.groups.users` | M2m verso gli utenti | **Rinominato** `user_ids` | **Incompatibile** -- `Invalid field 'users' in 'res.groups'` |
| `ir.actions.act_window.groups_id` | Restrizione per gruppo sulle azioni | **Rinominato** `group_ids` | **Incompatibile** -- `Invalid field 'groups_id' in 'ir.actions.act_window'` |
| `res.users.groups_id` | M2m verso `res.groups` sul record dell'utente | **Rinominato** `group_ids` | **Incompatibile** -- campo distinto da quello di `ir.actions.act_window` sopra (modello diverso, stessi nomi vecchio/nuovo): `self.env.user.groups_id` → `self.env.user.group_ids` |
| Accesso alle cartelle di `documents.document` | Modello `documents.folder` | Unificato in `documents.document` (`type='folder'`); richiede `access_internal` esplicito | **Incompatibile** -- il default `access_internal='none'` blocca gli utenti interni con `Documents.document: global read rule` |
| ACL e regole di record | Stesso formato | Uguali, nessun cambiamento | Nessun breaking change |

### Gruppi di sicurezza: nuovo modello intermedio `res.groups.privilege`

In Odoo 19 un nuovo modello, `res.groups.privilege`, si colloca tra `ir.module.category` e `res.groups`:

```
ir.module.category  →  res.groups.privilege  →  res.groups
```

**SBAGLIATO (19.0) — `category_id` direttamente su `res.groups`:**
```xml
<record id="module_category_library" model="ir.module.category">
    <field name="name">Library</field>
</record>
<record id="group_library_user" model="res.groups">
    <field name="name">User</field>
    <field name="category_id" ref="module_category_library"/>  <!-- non esiste in 19 -->
</record>
```

**CORRETTO (19.0) — catena a tre livelli:**
```xml
<!-- 1. Categoria del modulo (invariata) -->
<record id="module_category_library" model="ir.module.category">
    <field name="name">Library</field>
    <field name="sequence">100</field>
    <field name="visible">True</field>
</record>

<!-- 2. Privilegio (nuovo in 19.0): i gruppi di questo privilegio condividono una selezione -->
<record id="privilege_library" model="res.groups.privilege">
    <field name="name">Library</field>
    <field name="category_id" ref="module_category_library"/>
</record>

<!-- 3. I gruppi fanno riferimento a privilege_id, non a category_id -->
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

**Perché:** Odoo 19 ha introdotto `res.groups.privilege` per separare il raggruppamento dei privilegi dalle
categorie di modulo. `res.groups.category_id` non esiste più; `res.groups.privilege_id` è la nuova FK. Il
`name` del privilegio è ciò che compare come intestazione di sezione nel form dell'utente. I nomi dei gruppi
all'interno di un privilegio devono essere unici (vincolo SQL `UNIQUE(privilege_id, name)`).

### Contabilità: `account.group_account_user` è un interruttore di funzionalità, NON il ruolo del contabile

In 19.0 `account.group_account_user` è "Show Full Accounting Features" (implica `group_account_basic` +
`group_account_readonly`): un interruttore tecnico che, una volta attivate tutte le funzionalità contabili,
finisce su ogni utente interno. I ruoli sono `account.group_account_invoice` ("Invoicing") e
`account.group_account_manager` ("Administrator", implica `group_account_invoice` ma **non**
`group_account_user`; verificato su `account/security/account_security.xml`). Usare `group_account_user` per
gli "utenti della contabilità" in `groups=`, nelle ACL o nel codice (`has_group`) o esclude i veri contabili o
apre la funzionalità a tutti.

**SBAGLIATO:** `groups="account.group_account_user"` / `has_group('account.group_account_user')` per dire "contabile".
**CORRETTO:** `account.group_account_invoice` (il manager lo implica).

Conseguenza nativa da ricordare: `hr_expense` dà la regola di record "vede le note spese di ogni dipendente"
(`ir_rule_hr_expense_manager`) a `account.group_account_user` e `hr_expense.group_hr_expense_user`, non a
`group_account_invoice`. Un utente con il solo Invoicing vede solo le note spese dei dipendenti che gestisce:
un modulo i cui utenti della contabilità devono leggere le note spese degli altri dipendenti deve aggiungere
una propria `ir.rule` per `account.group_account_invoice` (restringendo il domain, es. alle note spese
approvate).

### Documents di Odoo 19 Enterprise: `documents.document` e `access_internal` (Enterprise, fuori ambito)

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
   - In questo modo gli utenti con permessi di business sul modello padre non vengono bloccati dalla regola di record di `documents.document` durante il salvataggio.

