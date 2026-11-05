---
type: "Playbook"
title: "Apertura di una commessa"
description: "Dalla firma dell'incarico al primo giorno di lavoro: il progetto nel hub dal template, i fatti della commessa, i documenti, la riservatezza e l'informativa sull'uso dell'AI."
tags: ["commessa", "apertura", "progetto"]
---

# Apertura di una commessa

> Lo esegue l'agente con la persona responsabile della commessa; ogni scrittura nel hub dopo il suo sì.

1. **Il progetto nel hub.** Una commessa è un progetto, creato dal template «Commission (template)» (seed
   del pack); le fasi che l'incarico non comprende si archiviano. Il partner del progetto è il committente.
2. **La descrizione del progetto** dice in poche righe che cosa si progetta, per chi, in quale fase si entra (PFTE,
   esecutivo, direzione dei lavori, esercizio) e i vincoli del contratto (scadenze, importo per le soglie della
   gestione informativa, requisiti del capitolato informativo). Le milestone sono le scadenze del contratto.
3. **I fatti della commessa** (note di tipo fatto sul progetto), uno per voce:
   - persone e ruoli: socio responsabile, team, committente o RUP, coordinatori, come ruoli;
   - riservatezza della commessa (normale, riservata, segreta) e conservazione dei dati;
   - ruolo privacy dello studio (titolare o responsabile del trattamento) e dati personali presenti, senza
     riportarli;
   - classificazione degli usi di AI previsti secondo il Reg. UE 2024/1689, con data e autore
     (`../reference/compliance-ai.md`);
   - data dell'informativa al committente sull'uso dell'AI (L. 132/2025, art. 13).
4. **I documenti** che arrivano con l'incarico (disciplinare, capitolato informativo, documento di indirizzo della
   progettazione, rilievi) entrano nella memoria come documenti del progetto, con sommario e data di lettura
   (skill `memoria-ingestione` del core); il testo si conserva solo se la riservatezza lo permette.
5. **Il registro AI** della commessa si apre come procedura del progetto (`registro-decisioni-e-ai.md`).
6. **Le regole della commessa** che il committente o il socio responsabile pongono (per esempio «nessun file
   fuori dal CDE del committente») si scrivono come regole del progetto, attive dopo la conferma di un lead.
7. **Il primo aggiornamento** del progetto dice lo stato iniziale, i rischi e i prossimi passi.
