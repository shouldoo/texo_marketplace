---
type: "Playbook"
title: "Rassegna stampa e schede delle fonti esterne"
description: "Come la lista segue testate locali ed enti pubblici con la skill memoria-fonti del core: canali, smistamento, schede con fonte e data, domande sulla rassegna."
tags: ["rassegna stampa", "fonti esterne", "playbook"]
---

# Rassegna stampa e schede delle fonti esterne

> Il metodo è la skill del core `memoria-fonti` (modulo `texo_sources` del hub): questo playbook dice come lo usa una
> lista civica. Gli strumenti sono neutrali: la rassegna registra ciò che altri pubblicano, con fonte e data, senza
> giudizi aggiunti.

## 1. I canali

1. Le testate locali, gli albi e le pagine degli enti che contano per la campagna (comune, consiglio comunale,
   prefettura, enti del territorio) diventano **canali** del hub: un lead li aggiunge, o li dichiara come filo
   `rassegna` con `hub_channel` tra i fili del hub (Texo Threads) e li registra `texo seed`.
2. Per ogni canale: che cosa cercare (il nome della città, i temi del programma, gli atti del consiglio), ogni quanti
   giorni leggerlo.

## 2. Lo smistamento

1. `sources-collect` legge i canali in scadenza; `sources-inbox` mostra i candidati.
2. La persona decide: tenere (con i temi), tenere come proposto, scartare. L'agente propone, non decide.
3. Un link incollato da un volontario entra con `sources-link`.

## 3. Le schede

1. La scheda di un articolo tenuto ha l'abstract con parole dell'agente (60-120 parole: chi, che cosa, dove, quali
   atti), le citazioni tra «» solo se presenti parola per parola nella pagina, le persone pubbliche, gli enti, i luoghi,
   i temi, la data dell'evento.
2. Una scheda che nomina persone aspetta l'approvazione di un lead.
3. Nessun testo dell'articolo viene copiato oltre le citazioni brevi; nessuna persona privata compare in una scheda.
4. La posizione di un partito, di un'altra lista o di un'associazione è una posizione attribuita, con la sua data,
   mai un fatto.

## 4. Usare la rassegna

- Domande sulla rassegna («che cosa è uscito sul tema dei parcheggi nell'ultimo mese?»): `sources-find` con i filtri,
  poi la risposta con le schede citate (testata, data, link).
- Un comunicato che risponde a un articolo parte dalle sue schede: skill `comunicato-stampa`.
- Un fatto pubblico che la lista userà più volte (un voto del consiglio, una delibera, una data) diventa un fatto della
  lista nel hub che cita la scheda o l'atto.
