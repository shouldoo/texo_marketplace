---
name: studio-guida
description: >-
  Come lavora con questo pacchetto uno studio di ingegneria e architettura: le commesse e i loro documenti, le decisioni, il registro AI, le fonti da leggere, e la mappa di lettura di glossario, BIM, contratti pubblici, sicurezza nei cantieri e playbook. Usala per una commessa, una gara, la contabilità dei lavori, il BIM, il coordinamento della sicurezza. Trigger: "commessa", "gara", "SAL", "BIM", "CSE", "PSC", "progetto esecutivo", "apri una commessa", "prepariamo l'offerta per la gara", "registra l'output dell'AI", "capitolato informativo", "direzione dei lavori".
---

# studio-guida

Il modo di lavorare del pacchetto studio_progettazione. I file nominati sotto sono in `references/`, accanto a
questo file.

## Le regole stanno nel hub

Le regole del settore sono regole dell'organizzazione nel suo hub: sono arrivate dal seed di questo pacchetto e i
lead possono cambiarle o sostituirle. Leggile con `texo rules` o nel pacchetto di contesto (`texo context`): ti
vincolano. Questa skill dice come lavorare, non le ripete.

## Una commessa e i suoi documenti

- Una commessa è un progetto del hub. Dei modelli e degli elaborati scrivi il riferimento (contenitore, disciplina,
  revisione, stato) e ciò che l'archivio non ha: perché, chi ha deciso, che cosa si è imparato.
- Una decisione di una commessa è una nota che cita il documento e la revisione da cui viene; una decisione più
  recente la sostituisce, non cancelli nulla (`references/playbooks/registro-decisioni-e-ai.md`).
- Versioni e revisioni dei documenti, la fase della progettazione, i titoli abilitativi ottenuti e le scadenze del
  contratto sono fatti della commessa nel hub.
- I documenti che manda un committente o un ente pubblico sono documenti della memoria con il loro riassunto; il
  loro testo si tiene solo quando la commessa lo consente.
- Ciò che lo studio impara su una commessa diventa una lezione senza il cliente.
- La memoria e i registri servono la commessa, mai a valutare le persone che lavorano nello studio.

## Una norma, un fatto

Quando una commessa dipende da una norma (una soglia, un termine, un obbligo), non rispondere a memoria: leggi il
testo vigente nel filo `normativa`, rispondi alla domanda della commessa e proponi un fatto del hub con la sezione,
le parole chiave, l'atto e l'articolo letti, la data di lettura e una scadenza. Un termine che corre diventa un
task con la sua data. I reference sotto dicono quale tipo di fonte leggere e quali domande farle; le risposte
stanno nei fatti del hub, che una riforma cambia.

## Mappa di lettura

> Prima di un lavoro leggi il file della riga, poi cerca le lezioni del hub sull'argomento
> (`texo search "<parole>" --scope lessons`, con i termini del glossario).

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

- Le norme si leggono dal filo `normativa` della cartella di lavoro (`.texo/THREADS.md`). Se il testo non si può
  leggere, dillo.
- Il bando, il disciplinare e il contratto della commessa sono documenti della memoria della commessa.
- Modelli ed elaborati si leggono dal filo `progettazione` o `documenti`, se la cartella di lavoro li monta;
  altrimenti la persona li indica.

### Skill

Le skill del core: `texo-sessione` all'inizio e alla fine di ogni lavoro, `memoria-ingestione` per i documenti di
una commessa, `memoria-consolidamento` per la revisione della memoria, `memoria-fonti` per i bandi e le novità
normative che lo studio segue.
