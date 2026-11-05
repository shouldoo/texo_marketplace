---
type: "Playbook"
title: "Decisioni e registro AI di una commessa"
description: "Come si scrive una decisione della commessa con il documento da cui viene, e come si tiene il registro degli output prodotti con l'AI."
tags: ["commessa", "decisioni", "registro-ai", "l132-2025"]
---

# Decisioni e registro AI di una commessa

## Una decisione

Una decisione presa sulla commessa si scrive, dopo il sì della persona, come nota interna sul task della fase e,
quando resta valida per la commessa, come fatto del progetto che cita il documento e la revisione da cui viene:

| Parte | Che cosa |
|---|---|
| Titolo | la decisione detta come una frase |
| Contesto | il problema, i vincoli, i riferimenti: revisione del modello, segnalazione, norma letta con articolo e data |
| Opzioni considerate | ciascuna con pro e contro |
| Decisione | che cosa si fa, perché, chi ha deciso |
| Conseguenze | che cosa cambia nel modello, negli elaborati, nei tempi, nei costi |

Una decisione che cambia non si cancella: la nuova sostituisce la vecchia (stato `superseded`). Una decisione
stabile che riguarda l'intera commessa va nella descrizione del progetto: la si propone alla persona, che la
modifica.

## Il registro AI

Ogni output prodotto con un sistema di AI che confluisce in un elaborato, un calcolo, uno script o una
comunicazione verso l'esterno si registra. Il registro mostra la prevalenza del lavoro del professionista
(L. 132/2025, art. 13). Si tiene come procedura del progetto, una riga per output, aggiunta con
`texo note-append` dopo la verifica:

| Data | Output | Sistema o modello | Per chi | Dove è confluito | Verificato da | Esito della verifica |
|---|---|---|---|---|---|---|

- «Verificato da» è il professionista che ne risponde, non l'agente.
- Un errore rilevante dovuto all'AI si registra con l'esito «respinto» o «corretto» e diventa una lezione del hub,
  senza il committente.
