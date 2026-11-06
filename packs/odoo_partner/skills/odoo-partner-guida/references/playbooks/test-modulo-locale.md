---
type: "Playbook"
title: "Playbook: testare un modulo sull'istanza locale di un progetto"
description: "Come eseguire i test di un modulo sull'istanza locale del progetto, su un database dedicato, e controllarne il log con checklog-odoo."
tags: ["test-modulo-locale"]
---

# Playbook: testare un modulo sull'istanza locale di un progetto

## Quando usare
Quando la regola del hub sui test e sul log pulito lo chiede: dopo una modifica a un modulo in
`modules/V<N>/<repo>/` o nel repository del progetto, prima di proporre commit o PR. Serve anche
per verificare il comportamento del modulo sull'istanza locale.

## Come funziona

Lo stack locale del progetto (`odoo/odoo-clients/<slug>/`) monta la cartella
`modules/V<N>/` (dove N corrisponde alla versione Odoo del progetto) come `/mnt/modules`.
Con `/mnt/modules` nell'addons_path, qualsiasi modulo clonato in `modules/V<N>/` è
immediatamente visibile a Odoo — nessun symlink manuale necessario.

Per i **repo multi-modulo** (cartelle che non hanno `__manifest__.py` alla radice), aggiungi anche
`/mnt/modules/<nome-repo>/` all'addons_path in `odoo.conf`, così tutti i sotto-moduli sono disponibili.

**Nota:** se lo stack non ha il mount di `/mnt/modules`, aggiungilo a mano in
`docker-compose.yml` e `odoo.conf`, poi `docker compose up -d`.

I comandi sotto usano:

```bash
C="docker compose -f odoo/odoo-clients/<slug>/docker-compose.yml"     # dalla cartella di lavoro
ODOO="$C run --rm -T --no-deps --entrypoint odoo web"   # container usa-e-getta
CONF=/etc/odoo/odoo.conf
```

`$ODOO` avvia un container nuovo dello stesso servizio `web` (stessi volumi, stessa rete,
stesso `odoo.conf`, che contiene `db_host`, `db_user` e `db_password`).
I test girano lì e non nel container del server: gli `HttpCase` aprono un server HTTP
interno sulla porta di `odoo.conf`, che nel container del server è già occupata.

`--entrypoint odoo` scavalca l'entrypoint dell'immagine ufficiale, che accoda
`--db_host`/`--db_port`/... a ogni comando `odoo`: il sottocomando `db` non li accetta dopo
i suoi argomenti e fallisce con `unrecognized arguments: --db_port 5432` (verificato su
`odoo:19.0`).

## Prerequisiti
- Container del progetto up: `$C ps`
- Il modulo è in `modules/V<N>/<repo>/`
- `checklog-odoo` disponibile sull'host: `uvx checklog-odoo --help` (o
  `pipx install checklog-odoo`)

## Il database di test

**Il database di test è tuo: lo crei per il task, non ne usi uno esistente.** Il server
Postgres dello stack può ospitare la copia neutralizzata della produzione, database di
altri task o di un'altra versione: un database non creato da te non si usa, non si
aggiorna e non si cancella.

- **Nome**: `test_<slug-del-task><N>` (es. `test_sale_discount19`): dice a cosa serve e per
  quale versione.
- **Riuso**: le esecuzioni successive riusano lo stesso database con `-u <modulo>`, non con
  `-i`.
- **Ricrealo da zero** solo quando serve: prima installazione di un modulo nuovo, script in
  `migrations/`, modifiche a file `data/` o `demo/` (quelli con `noupdate` non si ricaricano),
  ACL o registry corrotti, un'esecuzione precedente che ha lasciato il database rotto.
- **Cancellalo** a fine task con `odoo db drop`, che elimina anche il filestore
  (`odoo/service/db.py`, `exp_drop`). `dropdb` o `DROP DATABASE` lasciano la cartella del
  filestore orfana sul volume.

### Creare il database

| Versione | Comando | Dati demo |
|---|---|---|
| 19, 20 | `$ODOO db -c $CONF init <db>` (lingua, paese, demo, credenziali admin), poi `-i <modulo>` | **non** caricati di default: `--with-demo` a `db init` (o al primo `-i`) se i test li usano |
| 16–18 | nessun `db init`: il server crea il database alla prima installazione, `$ODOO -c $CONF -d <db> -i <modulo> --stop-after-init` | caricati di default: `--without-demo=all` per escluderli |

Verifica sui sorgenti: il sottocomando `init` esiste in `odoo/cli/db.py` solo da 19.0;
`--with-demo` (default falso) sostituisce il vecchio default di 16–18 in
`odoo/tools/config.py`. Anche in 19 e 20 il primo `-i` su un database inesistente lo crea:
`db init` serve quando vuoi scegliere paese e lingua prima dell'installazione.

```bash
# 19, 20
$ODOO db -c $CONF init test_sale_discount19 --country it
# cancellare (tutte le versioni dalla 16)
$ODOO db -c $CONF drop test_sale_discount19
# elencare i database dello stack (solo lettura)
$C exec -T db psql -U odoo -lqt | cut -d'|' -f1
```

## Passi

### 1. Verifica che il modulo sia visibile dentro il container
```bash
$C exec web ls /mnt/modules/<modulo>
```

### 2. Esegui i test e salva il log
```bash
LOG=<dir-temporanea>/<modulo>-$(date +%H%M).log
# prima volta: -i; poi -u
$ODOO -c $CONF -d <db> -u <modulo> --test-tags /<modulo> --http-interface=127.0.0.1 \
  --stop-after-init 2>&1 | tee "$LOG"
```

- `--http-interface=127.0.0.1` come nella CI OCA (`oca_run_tests`): il server interno dei
  test resta nel container e, in 19, sparisce il `WARNING` «missing
  --http-interface/http_interface» che altrimenti fa fallire `checklog-odoo`.
- `--test-tags /<modulo>` attiva da solo i test (`test_enable` deriva da `test_tags` in
  `odoo/tools/config.py`) e li limita al modulo; in 17+ esiste anche la forma breve `-t`.
  Per un solo file o una classe: `--test-tags /<modulo>:<NomeClasse>`.
- Il log va in un file fuori dai repository (cartella di lavoro temporanea dell'assistente, o
  `mktemp -d`): può contenere dati del database.

### 3. Leggi il risultato
Cerca nel log la riga finale `<n> failed, <n> error(s) of <n> tests`. Ogni `FAIL`, `ERROR`
o traceback si risolve nel modulo prima di andare avanti.

### 4. Zero warning: `checklog-odoo`
`0 failed` non basta. La CI dei repository OCA fallisce su qualunque record `WARNING` o
`ERROR` del log: nel template OCA `enable_checklog_odoo` è attivo di default da 18.0 e
`oca_run_tests` passa il log dei test a `checklog-odoo`. La regola del hub sui test chiede lo
stesso ai moduli dei progetti:

```bash
uvx checklog-odoo --no-echo "$LOG"     # deve uscire con 0
```

Se il repository ha un `checklog-odoo.cfg` (generato dal template OCA), usalo con
`-c <repo>/checklog-odoo.cfg`: contiene solo i rumori noti dei test (`0 failed, 0 error(s)`,
la chiusura di Chrome). Un warning del tuo modulo si corregge nel modulo, **mai**
aggiungendo un `ignore`.

### 5. Prova sull'istanza
Per vedere la modifica nell'interfaccia (database del progetto, non quello di test):

```bash
$C exec web odoo -c $CONF -d <db-istanza> -u <modulo> --stop-after-init
$C restart web
$C logs --tail 80 web
```

Segnala qualsiasi riga `ERROR`, `WARNING` o traceback, anche se l'operazione
sembra completata. Per la UI: skill `browser-test`.

## Repo multi-modulo

Se il tuo modulo fa parte di un repo multi-modulo, è disponibile una volta che
`/mnt/modules/<nome-repo>/` è nell'addons_path.

Per verificare che un sub-modulo specifico sia visibile:
```bash
$C exec web ls /mnt/modules/<nome-repo>/<sotto-modulo>
```

## Rollback
- Se l'upgrade fallisce, NON forzare con `--init` o `--uninstall`.
- Mostra il traceback completo e attendi istruzioni.
- Un database di test rotto si ricrea (`db drop` e di nuovo `init` o `-i`); quello
  dell'istanza no: si ripristina dal backup, previa conferma.
