---
name: lista-civica-guida
description: >-
  Come lavora con questo pacchetto una lista civica, in modo politicamente neutrale: dove sono le regole, come si leggono gli atti della tornata e si scrivono come fatti del hub, firme, candidature, propaganda, dati personali e spese, e la mappa di lettura dei reference di metodo e dei playbook. Usala per il lavoro di campagna di una lista civica. Trigger: "lista civica", "campagna elettorale", "raccolta firme", "candidature", "par condicio", "silenzio elettorale", "spese elettorali", "organizziamo un banchetto", "prepara un volantino", "come si presentano le candidature", "rendiconto delle spese elettorali", "possiamo pubblicare un sondaggio".
---

# lista-civica-guida

Il modo di lavorare del pacchetto lista_civica. I file nominati sotto sono in `references/`, accanto a questo file.

## Le regole e questa skill

Le regole del settore sono regole dell'organizzazione nel suo hub: sono arrivate dal seed di questo pacchetto e i lead
possono cambiarle. Leggile con `texo rules` o nel pacchetto di contesto (`texo context`), con l'attività della
sessione: vincolano. Questa skill dice come lavorare e che cosa leggere.

## Come lavori

- Prima di una bozza, apri il pacchetto di contesto del progetto della campagna: i fatti della tornata (date,
  calendario dei divieti, firme, limiti di spesa) e le procedure della lista. Un fatto della tornata scaduto o non
  verificato si ricontrolla con la persona prima di usarlo.
- Una citazione che deve ancora arrivare si segna `[citazione da confermare]`. Una persona privata non si nomina in un
  testo destinato a uscire; una persona pubblica solo nel suo ruolo pubblico.
- Ciò che dipende dalla tornata o dalla dimensione del comune (date, firme, limiti, spazi) non si scrive mai a
  memoria: si legge sugli atti della tornata nei fili della lista, si scrive come fatto del hub, e si dice quando non
  è stato verificato.
- Ogni materia ha il suo reference: che cosa è, quale fonte leggere, quali domande farle, quale fatto o task
  scrivere. Le risposte stanno nei fatti del hub, mai nei file del pacchetto.
- Firme e candidature: `references/playbooks/raccolta-firme-e-candidature.md`. Spese e contributi:
  `references/reference/spese-elettorali.md`. Contatti di elettori e sostenitori:
  `references/reference/privacy-propaganda.md`.

## Il fatto della tornata

Ciò che leggi negli atti della tornata diventa un fatto del progetto della campagna, uno per argomento:

- titolo chiaro (per esempio «Calendario dei divieti della tornata», «Firme per la presentazione della lista»,
  «Limiti di spesa della campagna»);
- sezione `compliance`, parole chiave con sinonimi;
- l'atto e l'articolo letti, la data della verifica, chi l'ha fatta;
- scadenza alla fine della tornata.

Le scadenze che ne derivano diventano task con la loro data.

## Mappa di lettura

> Prima le regole del hub, poi questa skill. Le norme si leggono sul filo `normativa` della lista e si citano
> nei fatti per atto e articolo; ciò che dipende dalla tornata si verifica sugli atti di quell'anno.

### Per lavoro

| Lavoro | Leggi | Attività del hub |
|---|---|---|
| Firme, candidature, consegna delle liste | `references/playbooks/raccolta-firme-e-candidature.md`, `references/reference/candidature-e-firme.md` | `election` |
| Manifesti, volantini, silenzio elettorale | `references/reference/propaganda-e-silenzio-elettorale.md` | `campaign`, `press` |
| Stampa, emittenti locali, sondaggi, social | `references/reference/par-condicio.md` | `press` |
| Un comunicato stampa | skill `comunicato-stampa` | `press`, `communication` |
| Rassegna stampa e fonti esterne | `references/playbooks/rassegna-stampa-e-schede.md`, skill del core `memoria-fonti` | `press` |
| Eventi, banchetti, volontari | `references/playbooks/evento-o-banchetto.md` | `campaign` |
| Spese, contributi, mandatario, rendiconto | `references/reference/spese-elettorali.md` | `election` |
| Contatti di elettori, sostenitori, firmatari | `references/reference/privacy-propaganda.md` | tutte |
| Il programma e i gruppi tematici | i fatti e le procedure della lista nel hub, sezione `sector` | `programme` |

### Fuori da questo pacchetto

- Le decisioni, le posizioni, il programma e le persone della lista: nel suo hub, mai in git.
- Le norme regionali e i regolamenti comunali (suolo pubblico, affissioni, consiglio comunale): fatti della lista con
  la loro fonte, perché cambiano da un comune all'altro.
