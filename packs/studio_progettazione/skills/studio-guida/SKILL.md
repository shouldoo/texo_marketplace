---
name: studio-guida
description: >-
  Come lavora con questo pacchetto uno studio di ingegneria e architettura: il professionista decide e firma, le commesse e i loro documenti, l'uso dell'AI e i dati, e la mappa di lettura di glossario, BIM, contratti pubblici, sicurezza nei cantieri e playbook. Usala per una commessa, una gara, la contabilità dei lavori, il BIM, il coordinamento della sicurezza. Trigger: "commessa", "gara", "SAL", "BIM", "CSE", "PSC", "progetto esecutivo", "apri una commessa", "prepariamo l'offerta per la gara", "registra l'output dell'AI", "capitolato informativo", "direzione dei lavori".
---

# studio-guida

Il modo di lavorare del pacchetto studio_progettazione. Le regole che ogni sessione dell'organizzazione deve seguire
arrivano dal hub (il seed di questo pacchetto le ha rese regole dell'organizzazione): questa skill aggiunge come
lavorare e che cosa leggere. I file nominati sotto sono in `references/`, accanto a questo file.

## Il professionista decide, firma e invia

- L'agente prepara, controlla e propone; il professionista responsabile decide, firma e invia. Non firmare, timbrare,
  depositare o inviare mai nulla a un ente pubblico, a un committente o a un'impresa.
- Un calcolo, una verifica strutturale, energetica o acustica e un giudizio sulla sicurezza scritti dall'agente sono
  proposte finché il professionista responsabile non li ha verificati.
- Un requisito preso da un codice, un decreto o una norma tecnica si cita con atto, articolo e il giorno in cui si è
  letto il testo vigente. Una regola ricordata a memoria non è una fonte; se il testo non si può leggere, dillo.

## Una commessa e i suoi documenti

- Modelli, elaborati e relazioni restano nell'archivio o nell'ambiente di condivisione dei dati. La memoria tiene il
  loro riferimento (contenitore, disciplina, revisione, stato) e ciò che l'archivio non ha: perché, chi ha deciso, che
  cosa si è imparato, che cosa ha prodotto l'AI.
- Una decisione di una commessa si scrive come nota che cita il documento e la revisione da cui viene; una decisione
  più recente la sostituisce, non si cancella nulla.
- Versioni e revisioni dei documenti, la fase della progettazione, i titoli abilitativi ottenuti e le scadenze del
  contratto sono fatti della commessa nel hub.
- I documenti che manda un committente o un ente pubblico sono documenti della memoria con il loro riassunto; il loro
  testo si tiene solo quando la commessa lo consente.

## AI e dati

- Ogni output di un sistema di AI che arriva in un elaborato, un calcolo, uno script o una comunicazione fuori dallo
  studio si registra nel registro AI della commessa con chi l'ha verificato
  (`references/playbooks/registro-decisioni-e-ai.md`): l'uso dell'AI è strumentale e l'opera intellettuale resta del
  professionista, e il committente è informato dei sistemi usati (`references/reference/compliance-ai.md`).
- I dati personali dei committenti privati, delle persone in cantiere e delle persone delle imprese stanno solo nel
  hub, sulla commessa, e solo quanto serve alla commessa; le categorie particolari (salute, disabilità per
  l'accessibilità di un'abitazione) non entrano mai nella memoria.
- I dati di una commessa non ne escono mai: ciò che lo studio impara diventa una lezione senza il cliente.
- La memoria e i registri servono la commessa, mai a valutare le persone che lavorano nello studio.

## Mappa di lettura

> Le regole del settore sono sopra e nel hub. Prima di un lavoro si legge il file della riga, poi si cercano le
> lezioni del hub sull'argomento (`texo search "<parole>" --scope lessons`, con i termini del glossario).

### Per lavoro

| Lavoro | Leggi |
|---|---|
| Aprire una commessa | `references/playbooks/apertura-commessa.md` |
| Scrivere una decisione, registrare un output dell'AI | `references/playbooks/registro-decisioni-e-ai.md` |
| Direzione dei lavori: SAL, contabilità, riserve | `references/playbooks/sal-e-contabilita-lavori.md`, `references/reference/contratti-pubblici.md` |
| Gara o incarico pubblico: procedure, livelli di progettazione, corrispettivi | `references/reference/contratti-pubblici.md` |
| Coordinamento della sicurezza, PSC, fascicolo | `references/reference/sicurezza-cantieri.md` |
| Modelli, capitolato informativo, pGI, CDE | `references/reference/gestione-informativa-bim.md` |
| Gemello digitale, modello in esercizio | `references/reference/gemello-digitale.md`, `references/reference/compliance-ai.md` |
| Uso dell'AI, informativa al committente, dati personali | `references/reference/compliance-ai.md` |
| Una sigla o un termine del settore, i sinonimi per cercare | `references/reference/glossario.md` |

### Fonti

- Le norme si leggono dal filo `normativa` della cartella di lavoro (`.texo/THREADS.md`): si cita l'atto, l'articolo e la data
  di lettura del testo vigente. Le date e le soglie scritte nei reference valgono alla data di lettura indicata.
- Modelli ed elaborati si leggono dal filo `progettazione` o `documenti`, se la cartella di lavoro li monta; altrimenti la
  persona li indica.

### Skill

Le skill del core: `texo-sessione` all'inizio e alla fine di ogni lavoro, `memoria-ingestione` per i documenti di
una commessa, `memoria-consolidamento` per la revisione della memoria, `memoria-fonti` per i bandi e le novità
normative che lo studio segue.
