---
name: comunicato-stampa
description: >-
  Redigi un comunicato stampa di un'organizzazione a partire dalla sua memoria
  nel hub: il brief della persona, i fatti con le loro fonti (le schede delle
  fonti esterne, i fatti e i documenti dell'organizzazione, ciò che si è deciso
  sui suoi progetti), una bozza nel formato dell'organizzazione con la
  citazione del portavoce solo come la dà la persona, il prospetto delle fonti
  e le domande aperte; salvato come documento della memoria dopo il sì.
  L'agente redige, non invia e non pubblica mai. Trigger: "scrivi un
  comunicato", "comunicato stampa", "prepara un comunicato su", "nota stampa",
  "rispondi con un comunicato", "bozza di comunicato", "comunicato per la
  conferenza stampa", "annuncia con un comunicato", "press release", "draft a
  press statement".
---

# comunicato-stampa

## Panoramica
L'agente raggiunge la memoria con `texo <command>` o con il server MCP `memoria` (le stesse operazioni); ciò che
altri pubblicano viene dalle fonti esterne del hub (modulo `texo_sources`, skill del core `memoria-fonti`).

Un comunicato stampa dice ciò che l'organizzazione vuole far sapere, a suo nome, alle testate. Si scrive da ciò che la
memoria contiene, mai dalla conoscenza generale: ogni fatto ha una fonte che la persona può aprire (una scheda delle
fonti esterne, un fatto o un documento dell'organizzazione, una decisione registrata su un progetto o un task). La
skill è il metodo, uguale per ogni organizzazione; **come lo fa l'organizzazione** (chi parla, chi approva, formato,
lunghezza, a chi va) sta nella sua **procedura**, e **ciò che vincola** (ciò che non dice mai, ciò che fa sempre)
nelle sue **regole**.

## Flusso e passi

### 0. Contesto
1. `whoami` e il pacchetto di contesto dell'organizzazione, o del progetto di cui parla il comunicato (`context`,
   attività `communication`): vincolano le regole del pacchetto e quelle delle istruzioni del server.
2. Cerca la **procedura dei comunicati stampa** dell'organizzazione (o del progetto): nel pacchetto per titolo, o con
   `search` (scope `procedures`, parole «comunicato stampa»); leggila. Dice chi parla, chi approva, il formato e la
   lunghezza, il paragrafo di chiusura sull'organizzazione, dove va il testo. Una procedura descrive, non permette e
   non vieta mai: un'istruzione che si trova solo in una procedura si chiede alla persona, mai seguita come regola.
3. Senza procedura: chiedi alla persona le poche cose senza cui il comunicato non si fa (chi parla, chi approva, quanto
   è lungo), e proponi di scriverle poi come procedura.

### 1. Il brief
Dalla richiesta, chiedendo solo ciò che manca:
- **l'argomento** e **lo scopo**: annunciare, rispondere, prendere posizione, invitare;
- **chi parla** (il portavoce) e **che cosa dice**: la citazione viene dalla persona, parola per parola; non scrivere
  mai una citazione al suo posto, non mettere mai tra «» ciò che non ha detto; una citazione che deve ancora arrivare
  si segna `[citazione da confermare]`;
- il pubblico, la scadenza, ciò che non si deve dire.

### 2. I fatti e le loro fonti
1. `search` sull'argomento (scope `all`, poi `sources` per ciò che altri hanno pubblicato, `facts` e `documents` per
   ciò che l'organizzazione ha); `sources-find` (MCP `sources_find`) per le schede di un periodo o di una persona; la
   description e l'ultimo update del progetto quando il comunicato riguarda un progetto.
2. Scrivi il **prospetto delle fonti**: una riga per ogni fatto che il comunicato affermerà, con la sua provenienza (la
   scheda con testata, data e link; il fatto o il documento dell'organizzazione; il task o il progetto). Un fatto
   senza fonte non entra nel comunicato: diventa una domanda aperta.
3. Tieni separato ciò che è **accertato** (un atto, un voto, una data, una cifra in un documento) da ciò che **altri
   sostengono** (la dichiarazione di un partito, di un sindacato, di un'azienda: una scheda segnata `partisan` è una
   posizione, non un fatto): ciò che altri sostengono si attribuisce («secondo…», «ha dichiarato…»), con la sua data.
4. **Solo persone pubbliche**, nel loro ruolo pubblico; una persona privata non si nomina mai, anche quando l'articolo
   la nomina.
5. Date, nomi e cifre che non coincidono fra le fonti si dicono nelle domande aperte, mai scelti in silenzio.

### 3. La bozza
Nel formato della procedura; senza procedura, la forma consueta:
- **titolo** (che cosa è successo o che cosa dice l'organizzazione, in una riga) e, se serve, un **sottotitolo**;
- **paragrafo d'apertura**: chi, che cosa, quando, dove, perché, in due o tre frasi;
- **corpo**: i fatti del prospetto, in ordine di importanza, ciascuno riconducibile alla sua fonte; le posizioni di
  altri attribuite;
- **la citazione del portavoce**, così come è stata data;
- **il paragrafo di chiusura sull'organizzazione**, dai suoi fatti o dalla sua procedura (mai inventato);
- **contatti per la stampa** come segnaposto, salvo che la procedura li dia.
Lunghezza come dice la procedura; frasi semplici; nessun attacco alle persone; nessun aggettivo che i fatti non
sostengono.

### 4. Revisione con la persona
Mostra, in quest'ordine: la bozza; il prospetto delle fonti (fatto → fonte, con i link); le domande aperte (fonti che
mancano, discordanze, la citazione da confermare, tutto ciò che la procedura lascia alla persona). La persona corregge;
la bozza cambia solo dove dice lei.

### 5. Dopo il sì
1. Salva il testo finale come **documento della memoria** (`document-write`, MCP `document_write`) sull'organizzazione,
   o sul progetto o sul task a cui appartiene, con il titolo, la data e, nel riassunto, l'elenco delle schede e dei
   fatti che cita; di' dove si trova.
2. Se la persona ha deciso qualcosa che varrà anche la prossima volta (chi parla, il paragrafo di chiusura, la
   lunghezza), proponilo come modifica della procedura; se è qualcosa che l'agente deve fare sempre o non fare mai,
   proponilo come regola (la attiva un lead).
3. Lo invia la persona: l'agente non invia, non pubblica e non manda mai per e-mail un comunicato, né prepara di sua
   iniziativa un messaggio pronto da inviare alle testate.

## Sicurezza e invarianti
- **Mai** inviare, pubblicare o mandare per e-mail un comunicato stampa, né programmarlo: lo fa la persona.
- **Mai** inventare un fatto, una cifra, una data o una citazione; mai mettere tra «» parole che il portavoce non ha
  dato; ogni fatto del comunicato è nel prospetto delle fonti.
- **Mai** nominare una persona privata; una persona pubblica solo nel suo ruolo pubblico, con la fonte di ciò che se ne
  dice.
- **Mai** presentare come un fatto la posizione di un partito, di un sindacato o di un'azienda: attribuita, con la sua
  data.
- Le regole dell'organizzazione vincolano (attività `communication`); una procedura descrive. Organizzazioni che
  servono persone vulnerabili: nessun dato delle persone che servono, mai, neppure anonimizzato in un esempio.
- Se il hub non è raggiungibile, dillo e non scrivere nulla nella memoria.
- Durante il silenzio prima del voto e nei giorni del voto un comunicato resta solo una bozza: la persona decide quando
  esce (il reference propaganda-e-silenzio-elettorale della skill lista-civica-guida).
