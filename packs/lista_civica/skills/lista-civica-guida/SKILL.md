---
name: lista-civica-guida
description: >-
  Come lavora con questo pacchetto una lista civica, in modo politicamente neutrale: posizioni, citazioni e fatti, dati personali, le regole della campagna nelle bozze, firme, candidature e spese, e la mappa di lettura dei reference di metodo e dei playbook. Usala per il lavoro di campagna di una lista civica. Trigger: "lista civica", "campagna elettorale", "raccolta firme", "candidature", "par condicio", "silenzio elettorale", "spese elettorali", "organizziamo un banchetto", "prepara un volantino", "come si presentano le candidature", "rendiconto delle spese elettorali", "possiamo pubblicare un sondaggio".
---

# lista-civica-guida

Il modo di lavorare del pacchetto lista_civica. Le regole che ogni sessione dell'organizzazione deve seguire
arrivano dal hub (il seed di questo pacchetto le ha rese regole dell'organizzazione): questa skill aggiunge come
lavorare e che cosa leggere. I file nominati sotto sono in `references/`, accanto a questo file.

## Posizioni, citazioni e fatti

- Non inventare mai una posizione, una dichiarazione, una citazione o un evento di una persona, un partito, una
  lista o un ente reali. Una citazione va tra «» solo come la dà la persona, parola per parola; una citazione che
  deve ancora arrivare si segna `[citazione da confermare]`.
- Un fatto su altri (un voto, un atto, una dichiarazione, una cifra) si scrive solo con la sua fonte pubblica e la
  sua data: una scheda delle fonti esterne, un atto, un documento della memoria. Ciò che altri sostengono si
  attribuisce, mai presentato come un fatto.
- Una persona privata non si nomina mai in un testo destinato a uscire; una persona pubblica solo nel suo ruolo
  pubblico.
- L'agente redige; non pubblica, non invia, non posta, non manda per e-mail e non programma mai nulla rivolto alla
  stampa, agli account social, agli elettori o ad altre liste. Lo fa una persona, dopo aver letto la bozza.

## Dati personali

- I dati di elettori, sostenitori, firmatari, volontari e donatori stanno solo nel hub, con i suoi permessi: mai in
  git, in un documento della cartella di lavoro, in una chat o in un prompt inviato a un filo di classe `public`.
- Un'opinione politica è una categoria particolare di dati personali (Regolamento UE 2016/679, art. 9, come
  richiamato dal provvedimento del Garante del 18 aprile 2019, § 2): l'elenco di chi sostiene la lista o ha firmato
  per essa lo è. I contatti raccolti in un'iniziativa (una petizione, un banchetto, una raccolta firme) si usano per
  la propaganda solo con il consenso o la base che il Garante descrive (`references/reference/privacy-propaganda.md`).
- Le anagrafi della popolazione e le liste già usate ai seggi non sono mai una fonte di contatti (Garante 2019, § 5).

## Le regole della campagna nelle bozze

Le bozze seguono gli atti che il pacchetto ha letto (`references/reference/`): il silenzio del giorno prima e dei
giorni del voto (L. 4 aprile 1956, n. 212, art. 9), i manifesti solo negli spazi del comune (L. 212/1956, art. 1),
il nome del committente responsabile su ogni materiale di propaganda (L. 10 dicembre 1993, n. 515, art. 3, comma 2),
nessun risultato di sondaggi nei quindici giorni prima del voto (L. 22 febbraio 2000, n. 28, art. 8). Date, soglie e
limiti che dipendono dalla tornata o dalla dimensione del comune si controllano sugli atti di quella tornata, e si
dice quando non lo sono stati.

## Firme, candidature e spese

- Firme e moduli di candidatura seguono le istruzioni che il Ministero dell'Interno pubblica per la tornata e le leggi
  che richiamano: `references/playbooks/raccolta-firme-e-candidature.md`. Una cifra a memoria non basta mai.
- Ogni spesa e ogni contributo della campagna si registra nel hub come fatto con il suo documento (fattura,
  ricevuta, estratto conto), così il rendiconto delle spese si scrive dalla memoria
  (`references/reference/spese-elettorali.md`).

## Mappa di lettura

> Prima le regole: quelle del core e del hub, poi questa skill. Le norme si leggono sul filo `normativa`
> della cartella di lavoro e si citano per atto e articolo; ciò che dipende dalla tornata si verifica sugli atti di quell'anno.

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
