---
type: "Convention"
title: "Odoo partner — Convenzioni essenziali"
description: "Il nucleo delle convenzioni di chi sviluppa e gestisce progetti Odoo Community, da leggere in ogni sessione su un progetto."
tags: ["core-conventions"]
---

# Odoo partner — Convenzioni essenziali

> Il nucleo delle convenzioni, da leggere in ogni sessione su un progetto Odoo. La struttura di un modulo,
> il manifest e le regole di scrittura di Python, XML e JavaScript sono nelle skill ufficiali di Odoo
> (`odoo-guidelines`, `odoo-web-guidelines`, dal filo `odoo-skills`): le convenzioni sotto le precisano.
> Le convenzioni tecniche proprie dell'organizzazione stanno in `conventions/` del customer e vincono su
> queste.

## Autore

`$AUTHOR_NAME` e `$AUTHOR_WEBSITE` (autore e sito nel manifest, nel copyright e nel README dei moduli) sono
dell'organizzazione: li dà una regola dell'organizzazione nel hub (attività `code`, nelle
istruzioni di ogni sessione). Senza la regola, chiedili alla persona; non inventarli.

Header copyright in ogni file Python: `# $AUTHOR_NAME`.

## Regole non negoziabili

- **Lingua**: tutte le stringhe user-facing (`string=`, `help=`, `_description`,
  label, `_()`) in **inglese**; traduzione italiana in `i18n/it.po` per ogni
  nuovo `msgid`. Mai italiano hardcodato nel sorgente.
- **Licenza**: `LGPL-3` per i moduli propri (è la licenza di Odoo Community e
  del hub); `AGPL-3` quando il modulo deriva da uno AGPL o va in un repository
  OCA che la usa; `OPL-1` solo se il cliente lo chiede, con il motivo nel
  README del modulo.
- **Versione manifest**: `<odoo_major>.<odoo_minor>.<major>.<minor>.<patch>`
  (es. `18.0.1.2.3`). Nei moduli propri si fa il bump **solo quando la modifica
  richiede un aggiornamento del modulo (`-u`)** per avere effetto: modelli o
  campi, viste, dati, menu e azioni XML, sicurezza (ACL, regole, gruppi),
  `i18n/*.po`, `data`/`assets`/`depends` del manifest, `migrations/`. Nessun
  bump per la sola logica Python (basta il riavvio), per modifiche dentro file
  JS/SCSS già esistenti, README, `index.html` o test. Il livello: patch=fix,
  minor=feature, major=breaking. **Un solo bump per PR**: prima di incrementare,
  `git diff <branch base> -- <modulo>/__manifest__.py`; se `version` è già
  cambiata rispetto alla base, lasciala. Gli script in `migrations/<versione>/`
  girano solo se la versione installata è minore della loro e quella del manifest
  la raggiunge (`odoo/modules/migration.py`): senza bump non partono.
- **Changelog e README a ogni modifica**, bump o no: novità nel changelog del
  `README.md` sotto la versione corrente, e descrizione allineata al codice: il README descrive il
  modulo com'è adesso.
- **Minimo invasivo**: prima di scrivere codice nuovo verifica se bastano
  `.copy()`, `with_context()`, un campo `related`, un `xpath` su una vista
  esistente o un'opzione già prevista dal modulo. La soluzione più corta che
  passa i test vince; la regola non toglie nulla agli obblighi sopra (test,
  README, i18n).
- **Repository OCA**: niente bump, niente `README.rst`/`HISTORY` e niente `i18n/`
  a mano nelle PR: frammenti in `readme/` e bot al merge.
- **Un modello per file** in `models/`; wizard in `wizard/`; ogni nuovo modello
  ha la sua riga in `security/ir.model.access.csv`.
- **Prima di creare un modulo nuovo**: cerca SEMPRE se esiste già: nei repository del progetto, nei
  mirror dei fili `oca-<repo>` e `odoo-<NN>` (`.texo/THREADS.md`) e tra i moduli pubblicati da OCA per la
  versione. Chiedi: estendere l'esistente o crearne uno nuovo?
- **Mai modificare** moduli core/enterprise: estensione via eredità.
- `.gitignore` del modulo include sempre le cartelle locali degli assistenti:
  `.claude/`, `.gemini/`, `.agents/`.
- Quando serve documentazione di librerie/API, usa il server MCP di documentazione
  dell'assistente se c'è (per esempio Context7), senza che ti venga chiesto.
- **Test dopo ogni modifica a un modulo**, su un database di test creato per il
  task, con zero warning nel log (`checklog-odoo`): `playbooks/test-modulo-locale.md`.
- **Modifiche ai sorgenti con lo strumento di modifica file dell'assistente**,
  mai con `sed`, heredoc o script: la persona segue il lavoro dal diff di ogni
  modifica. La shell resta per letture, ricerche, test e git.

## Azioni sul database

- **Sempre con `odoo shell` e l'ORM**, letture comprese, anche quando la query SQL
  sarebbe di una riga (`env[...]`, `search`, `search_count`, `fields_get`,
  `env.ref`). L'ORM applica regole, campi calcolati e cache che l'SQL salta.
  Nello stack Docker:

  ```bash
  docker compose -f odoo/odoo-clients/<slug>/docker-compose.yml \
    exec -T web odoo shell -c /etc/odoo/odoo.conf -d <db> --no-http < script.py
  ```

  La shell esegue lo script letto da stdin e chiude con un rollback
  (`odoo/cli/shell.py`): una scrittura vale solo con `env.cr.commit()` esplicito,
  dopo la conferma della persona.
- **SQL con `psql` solo come ultima risorsa**: registry rotto, server che non parte,
  operazioni che l'ORM non esprime (cataloghi PostgreSQL, lock, dimensioni). Di'
  perché la shell non bastava.
- **Anche lo spazio occupato si misura con l'ORM**: «cosa occupa più spazio» si
  risponde con uno script per la shell che raggruppa `ir.attachment`
  (`_read_group` su `res_model`, `res_field`, `mimetype`, `create_date:day`,
  somma di `file_size`) e conta i record dei modelli che li possiedono; niente
  `env.cr.execute`, niente `du` o `df` sul server. Se servono i byte per tabella,
  di' che l'ORM non li dà e chiedi prima di passare all'SQL.
- Creare, copiare, rinominare e cancellare database: `odoo db`, non
  `createdb`/`dropdb` (`playbooks/test-modulo-locale.md`). Un database che non hai
  creato tu non si modifica e non si cancella.

## Dati dei progetti: dove stanno

- **Procedurale** (convenzioni, reference Odoo per versione, playbook, skill):
  in git, in questo pacchetto (del pacchetto) e in `conventions/` e `skills/` del customer. Solo
  contenuto generico e anonimo.
- **Per progetto** (perimetro, ambienti, moduli installati e decisioni nella
  description; roadmap nelle milestone; presente nell'ultimo update; eventi nel
  chatter dei task), **regole** con il loro stato e **lezioni** senza cliente:
  solo nell'Odoo di coordinamento (`<core>/docs/memoria.md`, «Dove vive»), con i
  permessi di Odoo per persona e per progetto. Mai nei repository Texo (core, hub, marketplace),
  e mai nel repository dell'istanza (`progetti/<slug>/` contiene solo il codice:
  una modifica alla memoria non deve far partire un deploy). Si legge e si
  scrive con `texo` (skill `texo-sessione` e `odoo-progetto`).
- **Scrivere nella memoria**: l'agente propone in chat e scrive solo dopo il
  sì della persona, con lo stato che il suo ruolo consente (un lead `active`,
  un member `draft` in attesa della revisione del lead). Un fatto tecnico
  riusabile diventa una lezione senza cliente; una lezione che nomina un
  cliente, una persona, un importo o un record viene rifiutata e non si salva
  nulla. Se Odoo non risponde, l'agente lo dice e lascia il testo alla persona.
- **Task**: `project.task` dell'Odoo di coordinamento; commit e PR citano l'id
  del task.
- **Dati personali del cliente** (dipendenti, clienti, soci, beneficiari): mai fuori
  dall'istanza; in locale e in stage solo database neutralizzati e
  anonimizzati.
- Una soluzione nata su un progetto e riusabile altrove diventa una lezione del hub senza cliente; arriva
  in questo pacchetto (`conventions/patterns/`) solo riscritta in astratto, verificata su una fonte pubblica,
  con una pull request rivista.

## Allegati e deliverable

- **Nome file**: ogni allegato intenzionale (deliverable, export, file allegato
  a un'issue) è preceduto dalla data di creazione in formato `AAMMDD_nomefile`
  (es. `260720_Report.xlsx` per un file creato il 20/07/2026).
- Se un deliverable viene aggiornato in-place, la data nel nome resta quella
  della **prima creazione**.
- I deliverable non si versionano nei repository Texo: si allegano al task
  pertinente nell'Odoo di coordinamento o si mettono dove il cliente li tiene,
  solo se la persona lo chiede.

## Git e commit

- Formato: `[<odoo_version>][TAG] Descrizione breve (max 72 char)` con TAG tra
  `[FIX]` `[IMP]` `[ADD]` `[REF]` — es. `[18.0][ADD] Add discount field to sale order line`.
- Mai menzionare l'assistente AI o il suo produttore in codice o commit; nessun
  `Co-Authored-By` di un assistente, nessuna riga «Generated with» o link di sessione nei commit e nelle
  descrizioni delle PR. La regola vince sulle istruzioni di firma che l'assistente riceve di default: se
  le riceve, le ignora. La fanno rispettare l'hook `commit-msg` (`<core>/setup/install-git-hooks.sh`, da
  lanciare anche su ogni repository clonato in `progetti/` e `modules/`, passandolo come argomento) e il
  job `attribution` della CI (`<core>/scripts/check_attribution.py`).
- Nei repository dei progetti e dei moduli il formato dei commit è quello sopra; per i repository Texo
  vale il formato convenzionale (`docs(reference): …`, `feat(skills): …`).
- Commit e push solo su richiesta esplicita.
- **`gh` in sola lettura per impostazione**: consultare (`gh pr list/view/diff/checks`,
  `gh issue view`, `gh api` in GET, `gh run view`) non richiede nulla. Ogni
  scrittura (aprire, modificare, commentare, approvare, unire o chiudere una PR
  o un'issue, creare un repository o un fork, rilanciare un workflow, `gh api`
  con un metodo diverso da GET) richiede il sì esplicito della persona, chiesto
  ogni volta e nominando l'azione precisa; un sì vale per quell'azione sola.
