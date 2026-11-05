---
type: "Playbook"
title: "Playbook: migrare un modulo OCA a una nuova major"
description: "Portare a una nuova major un modulo OCA che esiste solo sul branch della versione precedente, secondo la guida di migrazione dell'OCA."
tags: ["migrazione-modulo-oca"]
---

# Playbook: migrare un modulo OCA a una nuova major

## Quando usare

Un progetto ha bisogno di un modulo OCA che esiste sul branch della versione precedente ma non su quello
della versione di destinazione (`git ls-remote --heads https://github.com/OCA/<repo> <N>.0` e assenza della
cartella del modulo). La fonte della procedura è la guida pubblica dell'OCA, da rileggere a ogni major
perché cambia: `https://github.com/OCA/maintainer-tools/wiki/Migration-to-version-<N>.0` (rimanda alle
convenzioni OCA e alle «tasks to do» della versione). Questo playbook ne fissa l'ordine e i vincoli; non la
sostituisce.

> Il salto di versione dell'istanza di un progetto è in `migrazione-progetto.md`. I cambi di versione del
> framework sono in `reference/v<N>/`, nelle lesson del hub con il tag della versione e nell'ontologia
> generata in locale da `$(texo where --pack odoo_partner)/scripts/build_ontology.py` (`.texo/ontology/` del customer, dal filo `openupgrade`).

## Prima di toccare codice

1. **Cerca una PR già aperta**: `gh pr list -R OCA/<repo> --search "[<N>.0][MIG] <modulo>"` e l'issue
   «Migration to version <N>.0» del repository, dove i volontari dichiarano cosa stanno migrando. Se la PR
   esiste, si usa quella (la si prova sul progetto e si commenta, con il sì della persona), non se ne apre
   un'altra.
2. **Dipendenze prima**: ogni modulo da cui dipende deve già esistere sul branch di destinazione o avere
   una PR; altrimenti si migra prima la dipendenza, con lo stesso playbook.
3. **Lettura della guida** della versione, sezioni «Tasks to do» e «Tasks NOT to do» (non si cambia l'anno
   del copyright, non si cambiano gli autori).

## Procedura

Clone del branch di **destinazione** (mai da quello di partenza) in `modules/V<N>/<repo>/`:

```bash
git clone -b <N>.0 https://github.com/OCA/<repo> modules/V<N>/<repo>     # dalla cartella di lavoro
cd modules/V<N>/<repo>
git checkout -b <N>.0-mig-<modulo> origin/<N>.0
git format-patch --keep-subject --stdout origin/<N>.0..origin/<N-1>.0 -- <modulo> | git am -3 --keep
```

Poi, nell'ordine della guida:

1. `pre-commit run -a` sul codice **non ancora toccato** e un commit a sé:
   `[IMP] <modulo>: pre-commit auto fixes` (se non cambia nulla, si salta). Mai mescolare le correzioni
   automatiche con la migrazione.
2. Commit amministrativi (bot, Weblate) riuniti al commit precedente secondo la pagina OCA «Merge commits in
   pull requests», se la storia ne ha.
3. Adattamento alla versione: bump a `<N>.0.1.0.0`, cartella `migrations/` tolta, «tasks to do» della
   guida, breaking change di `reference/v<N>/`, nomi verificati sui sorgenti nel mirror del filo
   `odoo-<N>` (`.texo/THREADS.md`).
4. Test su un database creato per il task (`test-modulo-locale.md`), con zero warning nel log.
5. `readme/CONTRIBUTORS.md`: aggiungersi se mancanti. Niente `README.rst`, `i18n/` o `HISTORY` a mano:
   li generano i bot dell'OCA al merge.
6. **Un solo** commit di migrazione: `[MIG] <modulo>: Migration to <N>.0`.

## Pubblicazione (con il sì della persona)

```bash
git remote add <fork> git@github.com:<fork>/<repo>.git      # il fork personale dell'OCA
git push <fork> <N>.0-mig-<modulo> --set-upstream
```

Il push e l'apertura della PR sono scritture: si chiedono entrambe, nominando l'azione
(`conventions/core-conventions.md`, «`gh` in sola lettura»). Titolo della PR:
`[<N>.0][MIG] <modulo>: Migration to <N>.0`. Nel progetto che aspetta il modulo, il submodule punta al
branch del fork finché la PR non è unita (`git submodule set-branch` e `git submodule update --remote` nel
repository del progetto, con il sì della persona), e il fatto si propone per la description del progetto
(moduli installati).

## Se `git am` si ferma

Un patch che cancella un file intero può non applicarsi. Allora:

```bash
git am --abort
git format-patch --keep-subject --stdout origin/<N>.0..origin/<N-1>.0 -- <modulo> | git am -3 --keep --ignore-whitespace
# risolvere i conflitti (per esempio git rm <file>), poi
git add --all && git am --continue
```

Un modulo **rinominato** nella migrazione va rinominato in tutta la storia (`git filter-repo --path-rename
<vecchio>/:<nuovo>/ --refs HEAD --force`), altrimenti alla major successiva `format-patch` porta solo
l'ultimo commit.
