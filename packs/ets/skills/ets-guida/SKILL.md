---
name: ets-guida
description: >-
  Come lavora con questo pacchetto un ente del Terzo settore (ETS: APS, ODV): dove leggere le regole del settore, che cosa scrivere nel hub su persone servite, associati e volontari, finanziamenti, rendicontazione e registro, e la mappa di lettura dei reference di metodo e dei playbook. Usala per bandi, rendiconti, adempimenti RUNTS, volontari e bilanci di un ETS. Trigger: "bando", "rendicontazione", "RUNTS", "bilancio ETS", "volontari", "5 per mille", "prepara la domanda per il bando", "cosa dobbiamo depositare al RUNTS", "rendiconta il progetto", "registro dei volontari", "relazione di missione".
---

# ets-guida

Il modo di lavorare del pacchetto ets. I file nominati sotto sono in `references/`, accanto a questo file.

Le regole del settore sono regole dell'organizzazione nel suo hub: sono arrivate dal seed di questo pacchetto e i
lead possono cambiarle. Leggile con `texo rules` o nel context pack (`texo context`): ti vincolano. Questa skill
dice come lavorare.

## Le persone servite

- Un documento che riguarda una persona servita non si legge e non entra nella memoria: se ti arriva, fermati e
  dillo alla persona.
- Le decisioni sul trattamento dei dati (informative, conservazione, misure) le prende chi ne risponde nell'ente:
  sono procedure del hub nella sezione `compliance`, non le stabilisci tu.

## Associati, volontari, personale

- I loro dati personali stanno solo nel hub, sui record che Odoo protegge con i suoi permessi.
- Ciò che la norma chiede per loro (registro dei volontari, assicurazione, rimborsi) è una procedura
  dell'organizzazione nel hub; il reference dice dove leggerlo e che cosa scrivere.

## Finanziamenti e rendicontazione

- Le regole di un finanziatore (costi ammissibili, cofinanziamento, scadenze, formato del rendiconto, pubblicità)
  sono fatti del progetto che finanzia, presi dall'avviso o dalla convenzione, con la loro citazione.
- Non affidarti al ricordo per una data: cercala nei task e nei fatti del hub.

## La norma

- Leggi l'atto nel filo `normativa`, nel testo vigente alla data; un reference di questo pacchetto dice quale
  domanda farti, non la risposta.
- Ciò che leggi diventa un fatto del hub con l'articolo letto, la data della verifica e una scadenza.

## Mappa di lettura

> Nessun file è precaricato: si legge quello che il compito tocca. I percorsi sono relativi a questo pacchetto
> (`$(texo where --pack ets)` dalla cartella di lavoro). Prima di rispondere su un obbligo: il reference, poi il
> fatto del hub, poi il testo vigente nel filo `normativa` se il fatto manca o è scaduto, poi le lezioni del hub
> con lo stesso tag.

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
