---
name: odoo-progetto
description: >-
  La parte Odoo dell'avvio e della chiusura del lavoro su un progetto Odoo Community, dopo la
  skill del core texo-sessione (ruolo, task, pacchetto di contesto, regole, fili, ricerca,
  chiusura): trova il repository del progetto in `progetti/<slug>/` e i suoi submodule, la
  versione Odoo dell'istanza dalla description del progetto, i reference e le lezioni
  dell'area, il codice upstream di quella versione nei fili (nomi di campi, metodi e viste
  si cercano lì), l'istanza locale e i test del modulo, secondo le regole del settore nel
  hub. Usala con texo-sessione
  all'inizio di ogni sessione su un progetto Odoo. Trigger: "lavoriamo su <progetto>",
  "task <n>", "apri il progetto", "start work on <project>", "modifica il modulo",
  "il modulo non installa", "riprendiamo il progetto Odoo", "cosa c'è da fare sul modulo".
---

# odoo-progetto

La sessione in sé (chi sei, il task, il pacchetto di contesto, le regole, i fili, la ricerca,
il riepilogo, e alla fine la nota, le ore, l'aggiornamento, fatti, procedure, lezioni e regole)
è la skill del core `texo-sessione`: seguila per prima. Questa skill aggiunge ciò che serve a
un progetto Odoo tra il riepilogo e la prima modifica, e alla fine.

I comandi `texo` si lanciano dalla cartella di lavoro. I percorsi `odoo-partner-guida/...` sono quelli della skill guida
del pacchetto, collegata tra le skill della cartella di lavoro.

| Che cosa | Dove | Come |
|---|---|---|
| Il repository del progetto: codice, submodule OCA e dei fornitori, workflow di deploy | `progetti/<slug>/` (una cartella di lavoro: la crea `texo mount`, fuori da git) | git |
| I repository di moduli autonomi | `modules/V<N>/<repo>/` | git |
| Le istanze locali | `odoo/odoo-clients/<slug>/` | Docker |
| Il codice upstream di una versione, OCA, OpenUpgrade | i mirror dei fili `odoo-<NN>`, `oca-<repo>`, `openupgrade` | `rg`, percorsi in `.texo/THREADS.md` |
| Le skill ufficiali di Odoo (`odoo-guidelines`, `odoo-web-guidelines`, `odoo-review`, `odoo-security`, `odoo-git`) | il filo `odoo-skills`, portato dal pacchetto | collegate da `texo mount` |
| Che cosa è cambiato tra versioni | `odoo-partner-guida/references/reference/v<N>/`; le lezioni del hub con i tag della versione e dell'area; `.texo/ontology/` | lettura |

## 1. La versione dell'istanza

La description del progetto dice la versione e l'edizione di Odoo, gli ambienti e i moduli
installati (custom, OCA, dei fornitori, con i loro repository e branch). Se la versione manca,
chiedila: tutto quello che segue dipende da lei. Dilla nel riepilogo.

## 2. Repository e submodule

1. Se `progetti/<slug>/` manca: chiedi l'URL del repository e **proponi**
   `git clone --recurse-submodules <url> progetti/<slug>` e
   `bash <core>/setup/install-git-hooks.sh progetti/<slug>` (non eseguirli senza OK).
2. Annota il branch corrente e le modifiche non committate
   (`git -C progetti/<slug> status --short --branch`): non lavorare mai sulle modifiche non
   committate di qualcun altro senza chiedere.
3. I submodule (`git -C progetti/<slug> submodule status`) sono i repository OCA e dei
   fornitori dell'istanza: un modulo viene da lì, mai da una copia altrove.

## 3. Codice upstream e reference

1. `.texo/THREADS.md` elenca il filo `odoo-<NN>` della versione del progetto e il suo mirror.
   Se manca, dillo e proponi il filo per la configurazione nel hub (il pacchetto lo suggerisce);
   `texo doctor` dice se il mirror è al ref fissato. I nomi di campi, metodi e viste si
   cercano con `rg` in quel mirror e nei mirror `oca-<repo>` (la regola del hub sui nomi).
2. Leggi la «Mappa di lettura» della skill `odoo-partner-guida`: le convenzioni, il delta della
   versione per l'area, il playbook dell'operazione. Cerca le lezioni dell'area prima di
   scrivere codice: `texo search "<words>" --terms <synonyms> --scope lessons --applies-to <NN>.0`.
3. Per un nome che può essere cambiato tra versioni, l'ontologia che
   `$(texo where --pack odoo_partner)/scripts/build_ontology.py` genera in `.texo/ontology/`.
4. Prima di aggiungere una voce a `depends`, confrontala con i moduli installati nella
   description del progetto (la regola del hub sulle dipendenze).
5. Prima di creare un modulo, cercane uno che esiste già (il progetto, i mirror OCA, i moduli
   che OCA pubblica per la versione): chiedi se estenderlo.

## 4. Lavoro e test

- Il codice segue `odoo-partner-guida/references/conventions/core-conventions.md`
  e le skill ufficiali. Le convenzioni dell'organizzazione e del cliente sono loro procedure
  nel hub (il pacchetto di contesto, `texo search "<parole>" --scope procedures`) e vincono su
  `core-conventions.md`.
- I test di un modulo e il controllo del log, come chiede la regola del hub sui test:
  `odoo-partner-guida/references/playbooks/test-modulo-locale.md`.
- Le letture e le scritture sul database con `odoo shell`:
  `odoo-partner-guida/references/conventions/core-conventions.md`, «Azioni sul database».
- Modifiche alla UI (JavaScript, Owl, viste, azioni): skill `browser-test`, solo istanza locale
  a meno che una regola attiva del progetto abiliti un host di stage.

## 5. Alla fine

Oltre alla chiusura di `texo-sessione`:

- La nota sul task nomina la causa tecnica in termini Odoo (modulo, modello, campo, flusso,
  errore) e i commit; le parole chiave aggiungono i nomi italiani e inglesi della funzione.
- Una lezione porta la versione in `--applies-to` (`<NN>.0`) e il modulo o l'area nei suoi
  tag, con le parole con cui sono etichettati i progetti.
- Ricorda di citare l'id del task nei commit e nel corpo della PR; commit, push e creazione
  della PR solo dopo la conferma della persona.

## Sicurezza

- Le regole del hub sulla produzione e sulle copie dei database valgono in ogni passo: una
  modifica arriva in produzione con il workflow di deploy del progetto.
- Non modificare mai il core di Odoo né i submodule OCA di un progetto: estendili da un modulo
  del progetto.
- Niente del progetto va nei repository di Texo o nel repository del progetto oltre al suo
  codice: fatti, decisioni e lezioni vivono nel hub.
