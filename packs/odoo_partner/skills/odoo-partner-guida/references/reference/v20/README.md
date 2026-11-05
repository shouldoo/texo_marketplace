---
type: "Reference"
title: "Odoo 20.0: delta di versione"
description: "Odoo 20.0: che cosa è verificato sui sorgenti, gli strumenti e i cambi noti ancora da verificare; i delta per area arrivano dopo la verifica."
tags: ["v20"]
---

# Odoo 20.0: delta di versione

> Il branch `20.0` di `odoo/odoo` esiste. I delta per area (`v20/<area>.md`) si scrivono solo dopo
> averli verificati sui sorgenti della versione, nel mirror del filo `odoo-20` (`.texo/THREADS.md`, montato da
> `texo mount`): nulla qui viene dalla
> memoria del modello. Stato al 2026-10-27: le righe sotto sono verificate con `rg` sui sorgenti di
> `20.0-20260926` (l'immagine `odoo:20.0` usata dall'Odoo di coordinamento); il percorso letto è nella
> colonna «Fonte».

## Strumenti

- **`upgrade_code`** (`odoo/upgrade_code/` in `odoo/odoo`, branch 20.0): codemod che portano un modulo da
  una versione intermedia alla successiva. Quelli oltre la 19.0 sono `19.1-00-t-call`,
  `19.3-00-account-groups`, `19.3-00-account-report-foldable`, `19.3-00-base64-in-xml`,
  `19.4-00-ir-access`, `19.4-00-ormcache-on-transaction`, `19.5-00-material-symbols-icons`,
  `19.5-00-tuple-rec_names_search`, `20.0-00-search-date-filters`, più `owl3-migration`. Si lanciano
  sul modulo e si rivede il diff; non sostituiscono la lettura del delta.
- **Ontologia 19.0 → 20.0**: non ancora generabile. Il branch `20.0` di `OCA/OpenUpgrade` non ha ancora
  le analisi (`openupgrade_scripts/` assente al 2026-10-25). Quando arrivano,
  il filo `openupgrade` a un ref che le contiene e `$(texo where --pack odoo_partner)/scripts/build_ontology.py` producono
  `.texo/ontology/19.0-20.0.md`.

## Cambi di framework noti

| Area | Cambio | Fonte |
|---|---|---|
| Sicurezza | ACL (`ir.model.access.csv`) e regole di record si fondono nel modello `ir.access`, caricato da `security/ir.access.csv`; conversione quasi automatica con `upgrade_code/19.4-00-ir-access.py` | `odoo/addons/base/models/ir_access.py`, `odoo/addons/base/security/ir.access.csv`; guida OCA 20.0; `odoo/odoo#166359` |
| Test | con `BaseCommon` (core, non OCA) i test girano come utente interno con i soli `_test_user_groups = ('base.group_user',)`; `_test_user_groups = None` sulla classe ripristina l'amministratore, oppure si elencano i gruppi necessari | `odoo/addons/base/tests/common.py` |
| Viste | il widget `selection_badge` non è più registrato: al suo posto `badges_selection` (campi `selection`) e `badges_many2one` (campi `many2one`) | `addons/web/static/src/views/fields/badges_selection/`, `.../badges_many2one/` |
| Frontend | Owl 3: codemod `owl3-migration` | `odoo/upgrade_code/owl3-migration.py` |
| Icone | Material Symbols al posto delle icone precedenti (`19.5-00-material-symbols-icons`) | `odoo/upgrade_code/19.5-00-material-symbols-icons.py` |
| Configurazione | `without_demo` è un booleano dalla 19.0 (`--with-demo` per installare i dati demo; il default è senza): il vecchio `without_demo = all` scrive un WARNING a ogni avvio | `odoo/tools/config.py` |
| Configurazione | `http_interface` vale `127.0.0.1` per default: in un container serve `http_interface = 0.0.0.0`, con la porta pubblicata solo su loopback dal compose | `odoo/tools/config.py` |
| Database | PostgreSQL 16 o successivo (`MIN_PG_VERSION = 16`) | `odoo/release.py` |
| Comandi | `odoo db {init,load,dump,duplicate,rename,drop}` gestisce i database con il filestore, senza il database manager web | `odoo db --help` sull'immagine `odoo:20.0` |
| ORM | `ir.config_parameter.get_param` non esiste più: `get_str`, `get_bool`, `get_int`, `get_float` (e `set_*`); per l'URL di un record `record.get_base_url()` | `odoo/addons/base/models/ir_config_parameter.py`, `odoo/orm/models.py` (`get_base_url`) |
| Sicurezza | l'operatore di dominio `access` (`('task_id', 'access', 'read')`) vale solo per many2one e `id`: su un x2many si scrive `('project_ids', 'any', [('id', 'access', 'read')])`. Negli `ir.access` i permessi di gruppo si sommano (OR), le restrizioni globali (senza gruppo) si applicano tutte (AND) | `odoo/orm/domains.py` (operatore `access`), `odoo/addons/base/models/ir_access.py` (`_get_failed_accesses`) |
| Allegati | `ir.attachment.raw` è un `BinaryValue` caricato pigramente (`.content` per i byte, `.open()`, `.size`), non `bytes`; `datas` non c'è più. `index_content` è in sola lettura e derivato: `_index` lo calcola solo per `text/*` (PDF e Office con `attachment_indexation`, alla scrittura), per un `type=url` resta vuoto. Un allegato senza record collegato è leggibile solo dal creatore e dagli amministratori (`_compute_res_access`): ogni allegato va agganciato a un record | `odoo/addons/base/models/ir_attachment.py`, `odoo/tools/binary.py`; verificato il 2026-10-27 sui sorgenti di Odoo 20.0 e con i test di `texo_memory` |
| Comandi | `--i18n-export` e `--i18n-import` non esistono più: `odoo i18n export -d <db> -l pot -o <file> <modulo>` (`-l it_IT` per un `.po`), `odoo i18n import -d <db> -l <lingua> <file>` | `odoo/cli/i18n.py`; prova del 2026-10-27 |
| Strumenti | `upgrade_code --from 19.0` si ferma su `19.3-00-account-groups` fuori dai moduli contabili (`KeyError`); `--script 19.4-00-ir-access` con `--glob` su un solo modulo fallisce (`NoneType`): si lanciano gli script uno per uno e la sicurezza si converte a mano, con un test per ruolo | prova del 2026-10-27 sull'immagine `odoo:20.0` (`20.0-20260926`), migrazione di `document_page_approval` |

## Da fare quando i sorgenti sono scaricati

1. Un `v20/<area>.md` per ogni area toccata da un progetto reale, non prima: lo scheletro è
   `reference/v19/`.
2. Ogni nuova riga della tabella sopra si verifica con `rg` sui sorgenti, con il percorso del file letto
   (fatto per le righe al 2026-10-25).
3. Il playbook di migrazione dei moduli OCA (`playbooks/migrazione-modulo-oca.md`) rimanda alla guida
   OCA della versione: rileggerla, cambia nel tempo.
