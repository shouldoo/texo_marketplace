---
name: odoo-partner-guida
description: >-
  Come lavora un partner Odoo con questo pacchetto: come si lavora sul codice e sulle istanze (le regole del settore sono nel hub), la mappa di lettura dei delta di versione, delle convenzioni e dei playbook, i fili del codice upstream. Usala quando il lavoro tocca un progetto Odoo Community, un modulo, un'istanza, una migrazione. Trigger: "modulo Odoo", "progetto Odoo", "migrazione", "istanza locale", "Odoo 19", "Odoo 20", "OCA", "scrivi un modulo", "modifica il modulo", "porta il modulo alla nuova versione", "che cosa cambia nella 19".
---

# odoo-partner-guida

Il modo di lavorare del pacchetto odoo_partner. Le regole del settore (la produzione, le copie dei database,
i nomi controllati nel sorgente, i test e il log, il database e l'ORM, le dipendenze) sono regole
dell'organizzazione nel suo hub: le ha seminate questo pacchetto e i lead possono cambiarle. Leggile con
`texo rules` o nel pacchetto di contesto: vincolano. Questa skill dice come lavorare e che cosa leggere. I file
citati sotto sono in `references/`, accanto a questo file.

## Prima di scrivere codice

- Conosci la versione Odoo dell'istanza: dalla description del progetto, dal prefisso della `version` nel
  manifest dei suoi moduli o dalla persona. Ogni reference e ogni lezione si legge per quella versione.
- Leggi la mappa (sotto) per l'area che tocchi, poi cerca le lezioni del hub per quell'area e quella versione
  (`texo search "<words>" --scope lessons`, con i tag dell'area). Un delta di `references/reference/v<NN>/`
  contiene solo ciò che cambia in quella versione.
- I nomi si cercano con `rg` nel mirror del filo `odoo-<NN>` (`.texo/THREADS.md`) e nei mirror `oca-<repo>`;
  per un cambio tra versioni, nell'ontologia che `$(texo where --pack odoo_partner)/scripts/build_ontology.py`
  scrive in `.texo/ontology/` da OpenUpgrade.
- Prima di creare un modulo, cercane uno esistente (prima OCA) e di' che cosa hai trovato.
- I moduli installati sull'istanza sono nella description del progetto: leggila prima di aggiungere una voce a
  `depends`.
- Il core di Odoo e i repository OCA sono codice di terzi: estendili per ereditarietà da un modulo del
  progetto, mai modificandoli.

## Durante il lavoro

- I test di un modulo e il controllo del log: `references/playbooks/test-modulo-locale.md`.
- Le letture e le scritture con `odoo shell`: `references/conventions/core-conventions.md`, «Azioni sul
  database».
- Quando proponi una modifica a un modello, di' che cosa segue: riavvio, `-u <module>`, test.
- Niente `print()` né log di debug nel codice finale.
- Per neutralizzare o anonimizzare una copia di un database: `$(texo where --pack odoo_partner)/scripts/neutralize-db.sh`
  e `$(texo where --pack odoo_partner)/scripts/anonymize-db.sh`.

## Che cosa tiene la memoria per questo settore

- I moduli installati, la versione, gli ambienti e il flusso di rilascio di un progetto sono fatti del
  progetto nel hub, non file della cartella di lavoro.
- Ciò che un progetto ha imparato su Odoo diventa una lezione del hub, con i tag dell'area e della versione,
  senza il cliente. Una lezione che si dimostra vera su più progetti si propone a questo pacchetto come delta
  di reference, riscritta e controllata sul sorgente pubblico, con una pull request revisionata.

## Mappa di lettura

> Nessun file di questo pacchetto è precaricato: si legge quello che il compito tocca. I percorsi sono
> relativi a questo pacchetto (`$(texo where --pack odoo_partner)` dalla cartella di lavoro). Prima di scrivere
> codice su un'area leggi il delta della versione del progetto, le lezioni del hub di quell'area e il codice
> upstream di quella versione.

### Prima di tutto

| Che cosa | Dove |
|---|---|
| Le convenzioni di codice e di lavoro su Odoo | `references/conventions/core-conventions.md` |
| Le convenzioni dell'organizzazione e del cliente | le loro procedure nel hub: il pacchetto di contesto, `texo search "<parole>" --scope procedures`; vincono su `core-conventions.md` |
| L'avvio e la chiusura del lavoro su un progetto | skill `texo-sessione` (core), poi skill `odoo-progetto` |
| La versione dell'istanza, gli ambienti, i moduli installati | la description del progetto nel hub (`texo project <id>`) |
| Il codice upstream della versione | il mirror del filo `odoo-<NN>` (`.texo/THREADS.md`): `rg`, mai la memoria |
| I moduli OCA in uso | i mirror dei fili `oca-<repo>`, dai `.gitmodules` dei progetti |

### Aree: delta per versione, lezioni e codice

I reference di base delle aree non sono in questo pacchetto: per ogni area valgono le lezioni del hub con il
tag dell'area e della versione (`texo search "<parole>" --terms <sinonimi> --scope lessons
--applies-to <NN>.0`) e il codice della versione nel mirror del suo filo. I reference di base si
ricostruiscono qui nel tempo, dalle lezioni verificate su fonti pubbliche (il codice di Odoo e di OCA).
I delta dicono che cosa cambia in una versione rispetto alla precedente.

| Area (modelli toccati) | Tag delle lezioni | Odoo 18 | Odoo 19 | Odoo 20 |
|---|---|---|---|---|
| Modelli, ORM, campi, CRUD | `models` | `references/reference/v18/models.md` | `references/reference/v19/models.md` | `references/reference/v20/README.md` |
| Viste XML | `views` | `references/reference/v18/views.md` | `references/reference/v19/views.md` | `references/reference/v20/README.md` |
| Ereditarietà di modelli e viste | `inheritance` | — | `references/reference/v19/inheritance.md` | — |
| File dati XML/CSV | `data` | — | `references/reference/v19/data.md` | — |
| Wizard | `wizards` | — | `references/reference/v19/wizards.md` | — |
| Sicurezza: ACL, regole, gruppi | `security` | — | `references/reference/v19/security.md` | `references/reference/v20/README.md` |
| `__manifest__.py`, versioni, dipendenze | `manifest` | `references/reference/v18/manifest.md` | `references/reference/v19/manifest.md` | — |
| Magazzino, prodotti (`stock.*`, `product.*`) | `inventory` | `references/reference/v18/inventory.md` | `references/reference/v19/inventory.md` | — |
| Produzione (`mrp.*`) | `manufacturing` | `references/reference/v18/manufacturing.md` | `references/reference/v19/manufacturing.md` | — |
| Contabilità (`account.*`) | `accounting` | `references/reference/v18/accounting.md` | `references/reference/v19/accounting.md` | — |
| Vendite, CRM, acquisti, progetti, helpdesk, HR, controller, test, report, OWL, i18n, performance | il nome dell'area | — | — | — |

`references/reference/v20/README.md` dice che cosa è verificato su Odoo 20.0, gli strumenti (`upgrade_code`) e i cambi
di framework noti. Un nome di modello, campo o xmlid che può essere cambiato tra due versioni si controlla
nell'ontologia che `$(texo where --pack odoo_partner)/scripts/build_ontology.py` genera in locale dal filo `openupgrade`, in
`.texo/ontology/` dell'organizzazione: non è versionata qui.

### Operazioni

| Operazione | Dove |
|---|---|
| Prendere in carico un progetto (hub, repository, istanza locale) | `references/playbooks/onboard-progetto.md` |
| Testare un modulo sull'istanza locale e controllarne il log | `references/playbooks/test-modulo-locale.md` |
| Portare un progetto a una nuova versione | `references/playbooks/migrazione-progetto.md` |
| Portare un modulo OCA a una nuova major | `references/playbooks/migrazione-modulo-oca.md` |
| Provare l'interfaccia di un'istanza locale o di uno stage abilitato | skill `browser-test` |
| Neutralizzare e anonimizzare una copia di un database | `$(texo where --pack odoo_partner)/scripts/neutralize-db.sh`, `$(texo where --pack odoo_partner)/scripts/anonymize-db.sh` |
| Un pattern riusato tra progetti diversi | `references/conventions/patterns/README.md` |

### Skill

| Skill | Da dove | Quando |
|---|---|---|
| `odoo-progetto` | questo pacchetto | dopo `texo-sessione`, su ogni progetto Odoo |
| `browser-test` | questo pacchetto | prova della UI dopo JavaScript, Owl, viste, azioni |
| `odoo-guidelines`, `odoo-web-guidelines`, `odoo-review`, `odoo-security`, `odoo-git` | le skill ufficiali di Odoo, dal filo `odoo-skills` che il pacchetto porta (mirror di `odoo/odoo`, cartella `skills/`), collegate da `texo mount` | scrittura e revisione di codice, sicurezza, git |
| `texo-sessione`, `memoria-consolidamento`, `memoria-ingestione`, `memoria-fonti` | il core | la sessione, la revisione della memoria, i documenti, le fonti |

Un assistente che non carica le skill da solo apre il `SKILL.md` quando il compito corrisponde.

### Fili suggeriti

| Filo | Tipo, driver | Che cosa |
|---|---|---|
| `odoo-<NN>` | source, `git-mirror` di `github.com/odoo/odoo` al ref della versione | il codice di Odoo Community di ogni versione dei progetti |
| `oca-<repo>` | source, `git-mirror` di `github.com/OCA/<repo>` | i repository OCA in uso, dai `.gitmodules` dei progetti |
| `openupgrade` | source, `git-mirror` di `github.com/OCA/OpenUpgrade` | facoltativo: le analisi dei cambi tra versioni, per l'ontologia e le migrazioni |

L'organizzazione li dichiara tra i fili del hub (Texo Threads) con il ref fissato; `texo mount` li monta,
`texo doctor` li controlla.

Il pacchetto porta il filo `odoo-skills` (`git-mirror` di `github.com/odoo/odoo`, cartella `skills/`, al commit che
la versione del pacchetto fissa): le skill ufficiali di Odoo arrivano con il pacchetto. Un filo del hub con lo stesso
id lo sostituisce, per esempio con un commit più recente.
