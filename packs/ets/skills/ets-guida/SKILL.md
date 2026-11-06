---
name: ets-guida
description: >-
  Come lavora con questo pacchetto un ente del Terzo settore (ETS: APS, ODV): le regole sulle persone servite, su associati e volontari, su finanziamenti e rendicontazione e sul registro, e la mappa di lettura dei reference di metodo e dei playbook. Usala per bandi, rendiconti, adempimenti RUNTS, volontari e bilanci di un ETS. Trigger: "bando", "rendicontazione", "RUNTS", "bilancio ETS", "volontari", "5 per mille", "prepara la domanda per il bando", "cosa dobbiamo depositare al RUNTS", "rendiconta il progetto", "registro dei volontari", "relazione di missione".
---

# ets-guida

Il modo di lavorare del pacchetto ets. Le regole che ogni sessione dell'organizzazione deve seguire arrivano dal
hub (il seed di questo pacchetto le ha rese regole dell'organizzazione): questa skill aggiunge come lavorare e che
cosa leggere. I file nominati sotto sono in `references/`, accanto a questo file.

## Le persone servite

- Non scrivere mai dati delle persone che l'organizzazione serve (persone aiutate, accolte, assistite, le loro
  famiglie) nella memoria, in git, in un commit, in una conversazione o in un documento che redigi: né nomi, né
  storie, né situazioni, né contatti, neppure in un esempio inventato. Il lavoro si descrive con attività, numeri
  ed esiti, mai con persone.
- L'indirizzo di una struttura protetta (una casa rifugio, un alloggio protetto) non si scrive mai da nessuna
  parte: né nella memoria, né in un progetto, né in un testo per il pubblico.
- Un documento che riguarda una persona servita non si legge e non entra nella memoria; se ti arriva, fermati e
  dillo.
- La comunicazione sui servizi (un report, un post, un comunicato stampa, un appello per volontari) non rende mai
  riconoscibile una persona, né direttamente né per la combinazione dei dettagli.

## Associati, volontari, personale

- I dati personali di associati, volontari e personale stanno solo nel hub, sui record che Odoo protegge con i suoi
  permessi; mai in git o in un testo che redigi per altri.
- Ciò che la legge chiede per loro (il registro dei volontari, la loro assicurazione, il rimborso delle spese) è una
  procedura dell'organizzazione nel hub; il reference dice che cosa chiede la legge.

## Finanziamenti e rendicontazione

- Le regole di un finanziatore (costi ammissibili, cofinanziamento, scadenze, formato della rendicontazione, obblighi
  di pubblicità) sono fatti del progetto che finanzia, presi dall'avviso o dalla convenzione e con la loro citazione.
- Le scadenze del registro e di ogni contributo sono task o fatti del hub con la loro data; non affidarti mai al
  ricordo.
- Le cifre di una domanda o di un rendiconto vengono dalla contabilità e dai documenti dell'organizzazione, mai
  stimate o arrotondate per farle tornare; una cifra che manca si chiede alla persona.
- Una domanda o un rendiconto li presenta la persona, mai l'agente.

## La norma

- Una risposta su un obbligo cita l'atto e l'articolo letti nel filo `normativa`, vigenti alla data; un reference di
  questo pacchetto è una mappa, non sostituisce il testo.
- Ciò che un reference segna «da verificare sul testo vigente» si controlla sul testo prima di farci affidamento.

## Mappa di lettura

> Nessun file è precaricato: si legge quello che il compito tocca. I percorsi sono relativi a questo pacchetto
> (`$(texo where --pack ets)` dalla cartella di lavoro). Prima di rispondere su un obbligo: il reference, poi l'articolo
> vigente nel filo `normativa`, poi le lezioni del hub con lo stesso tag.

### Per compito

| Compito | Reference | Playbook |
|---|---|---|
| Registro unico nazionale: iscrizione, depositi, variazioni, PEC | `references/reference/runts.md` | `references/playbooks/adempimenti-runts-annuali.md` |
| Bilancio o rendiconto per cassa, relazione di missione, libri sociali | `references/reference/bilancio-e-rendiconto.md` | `references/playbooks/adempimenti-runts-annuali.md` |
| Volontari, associati, lavoratori, rimborsi, assicurazione | `references/reference/volontari-e-associati.md` | — |
| Un avviso, una domanda di finanziamento | `references/reference/bandi-e-rendicontazione.md` | `references/playbooks/domanda-di-finanziamento.md` |
| La rendicontazione di un progetto finanziato | `references/reference/bandi-e-rendicontazione.md` | `references/playbooks/rendicontazione-di-un-progetto.md` |
| Pubblicazioni sul sito, dati delle persone servite | `references/reference/trasparenza-e-dati.md` | — |

### Fonti che non sono qui

| Fonte | Dove |
|---|---|
| I testi delle leggi e dei decreti in vigore | il filo `normativa` dell'organizzazione |
| Gli avvisi che l'organizzazione segue | il filo `bandi` e le fonti esterne del hub |
| Statuto, verbali, domande, rendiconti dell'organizzazione | il filo `documenti` e i documenti della memoria |
| Scadenze, cariche, soglie dell'ente | i fatti e i task del hub |

### Skill

questo pacchetto non ha skill proprie: valgono quelle del core (`texo-sessione`, `memoria-consolidamento`,
`memoria-ingestione`, `memoria-fonti`).
