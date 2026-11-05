---
type: "Playbook"
title: "Playbook: gestire una migrazione di versione di un progetto"
description: "Portare un progetto a una nuova versione di Odoo facendo coesistere in locale l'ambiente attuale e quello di destinazione, con una sola memoria."
tags: ["migrazione-progetto"]
---

# Playbook: gestire una migrazione di versione di un progetto

## Quando usare

Quando un progetto esistente va portato a una nuova versione Odoo e ti serve far
coesistere, in locale, l'ambiente **attuale** (produzione) e quello di
**destinazione** (di solito il branch v<N> del repository del progetto, provato
sullo stage), senza duplicare il progetto.

> Questo playbook copre l'**organizzazione del lavoro** (ambienti locali + memoria). Un modulo OCA che
> manca nella versione di arrivo si porta con `migrazione-modulo-oca.md`; il salto di versione del
> **database** si fa con OCA/OpenUpgrade (filo `openupgrade`, la sua documentazione). Le breaking change
> per versione stanno in `reference/v<N>/` e nelle lesson del hub con il tag della versione; i modelli e
> i campi rinominati o tolti nell'ontologia che `$(texo where --pack odoo_partner)/scripts/build_ontology.py` genera in `.texo/ontology/`.

## Principio: un progetto, più ambienti

Un progetto resta **un solo repository** (`progetti/<slug>/`) con una sola
memoria (il progetto nell'Odoo di coordinamento). L'asse che varia è la
versione, non il progetto. Quindi, nella description del progetto:

- identità stabile + ambiente della versione **corrente** + versione di
  destinazione durante la migrazione;
- un ambiente per ogni versione, con ruolo (`production` · `migration-target`
  · `legacy`), perimetro funzionale **to-be** e inventario moduli v<N>.

Spec e analisi della migrazione si allegano al task di migrazione; le scelte si
scrivono nel chatter del task (`texo task-note <id> "<testo>" --yes`) e, quando
cambiano lo stato del progetto, nell'update (`texo update <project_id> ...
--yes`); quelle stabili si propongono per la description, che modifica la persona
in Odoo. Un fatto tecnico riusabile altrove diventa una lezione senza cliente
(`texo lesson ... --yes`). Tutto si prepara, si mostra alla persona e si scrive
solo dopo la sua conferma (`conventions/core-conventions.md` § «Dati dei
progetti»). Lo stack locale non è descritto nella description: porte, URL e nomi
DB si leggono da `docker-compose.yml`/`docker ps`.

## Passi

### 1. Replica in locale l'ambiente di destinazione

Crea un secondo stack locale in `odoo/odoo-clients/<slug>-v<N>/` con:

- **Slug**: lo stesso di oggi (es. `acme`) — *non* aggiungere suffissi.
- **Versione**: quella di arrivo (es. `19`) → stack `<slug>-v<N>`, con porte proprie, l'immagine
  ufficiale di Odoo della versione e `modules/V<N>/` montato.
- **Repository**: il clone esistente in `progetti/<slug>/`, con un `git worktree` del branch di
  destinazione in `odoo/odoo-clients/<slug>-v<N>/repo`.
- **Branch base**: il branch di destinazione v<N> (es. `19.0`), quello che
  va sullo stage.
- **Dev branch**: es. `dev-migration-v<N>`, locale e non pushato.

Lo stack attuale resta intatto. Proponi per la description del progetto (gli
ambienti) il nuovo ambiente con ruolo `migration-target`.

> **Nomi container version-scoped.** I `container_name` sono `<slug>-v<N>-web`
> / `<slug>-v<N>-db`, così i due ambienti coesistono. Se l'ambiente attuale ha
> container senza versione (`<slug>-web` / `<slug>-db`), allinealo a mano
> in `docker-compose.yml` per evitare `Conflict. The container name is already
> in use` all'avvio del secondo.

### 2. Avvia e prepara il DB v<N>

Avvia lo stack (`docker compose up -d`). Il DB v<N> si ottiene migrando una
copia del DB attuale con OpenUpgrade, oppure restorando da `/web/database/manager` un dump già migrato
dello stage (spunta **Neutralize**, poi `$(texo where --pack odoo_partner)/scripts/neutralize-db.sh`; per gli enti che
seguono persone fragili anche `anonymize-db.sh`).

### 3. Riclassifica i moduli

Partendo dai moduli installati elencati nella description del progetto (versione
attuale), per ogni modulo custom/OCA decidi la categoria e proponila nella nota
del task di migrazione; le categorie decise vanno nell'update del progetto e
l'inventario v<N> risultante si propone per la description, nell'ambiente v<N>:

- **Nativo in v<N>** → si droppa il custom (verifica con `reference/v<N>/` e
  `rg` nel mirror del filo `odoo-<N>`, `.texo/THREADS.md`).
- **Da portare** → migrazione del codice in `modules/V<N>/<repo>` (un modulo OCA con
  `migrazione-modulo-oca.md`; un modulo proprio nello stesso ordine: correzioni automatiche, adattamento,
  test con zero warning).
- **Da rivedere / sostituire** → cambi funzionali.

### 4. Definisci il perimetro funzionale to-be

Aree/flussi/app **nuovi o diversi** rispetto alla versione attuale (es.
contabilità, soci e quote, eventi): si propone per la description, nell'ambiente
v<N>.
L'ambiente corrente resta l'as-is.

### 5. Lavora e sincronizza

Sviluppi i moduli portati in `modules/V<N>/` (montati in automatico sullo stack
v<N>). Per assorbire i commit dei colleghi sul branch di destinazione:

```bash
cd odoo/odoo-clients/<slug>-v<N>/repo     # dalla cartella di lavoro
git pull origin <branch-base>   # nel dev branch locale, poi risolvi
```

### 6. Go-live: promozione

Quando la v<N> va in produzione:

1. Nella description l'ambiente v<N> passa a ruolo `production` e la vecchia
   versione a `legacy` (l'agente propone il testo, la persona lo scrive); le
   regole del progetto che non valgono più passano a `superseded` verso la
   nuova (`texo state superseded --note <vecchia> --superseded-by <nuova>
   --yes`, lead; mai cancellarle).
2. La versione di Odoo nella description diventa la v<N>, nessuna versione di
   destinazione aperta; il go-live si registra come update del progetto e la
   milestone di migrazione si chiude.
3. Ritira lo stack della vecchia versione quando non serve più (senza
   `docker compose down -v` senza conferma; niente operazioni su `filestore/`
   o `backups/` senza conferma).

## Collegamenti

- `migrazione-modulo-oca.md` — un modulo OCA che manca nella versione di arrivo.
- `test-modulo-locale.md` — test dei moduli portati.
- `reference/v<N>/` — breaking change della versione di arrivo.
- `$(texo where --pack odoo_partner)/scripts/build_ontology.py` — modelli, campi e xmlid rinominati o tolti tra versioni, in `.texo/ontology/`.
