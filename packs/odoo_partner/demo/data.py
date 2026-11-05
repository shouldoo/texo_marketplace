# Copyright 2026 Daniele Lucarelli
# License CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/).
"""The demo of the pack odoo_partner: «Spola Informatica srl», an invented Odoo Community partner.

Everything is invented: the company, its people, its three customers, their projects, tasks, chatter and hours,
the rules, facts, procedures, documents and lessons. Loaded by core/setup/load-demo.sh through
core/scripts/load_demo.py, only into the databases of DATABASES.
"""

DATABASES = ("demo-odoo-partner", "demo-odoo-partner-test")
TOKEN_NAME = "Spola demo"
TOKEN_DAYS = 30

COMPANY = {"name": "Spola Informatica srl", "street": "Via delle Spole 3", "zip": "40100", "city": "Bologna",
           "email": "info@spola.example", "website": "https://spola.example"}

# role: (name, login, hub group); "norole" is an internal user without a hub role (403 on every route).
USERS = {
    "admin": ("Amministratore Spola", None, "texo.group_texo_admin"),
    "lead": ("Elena Lead", "lead@spola.example", "texo.group_texo_lead"),
    "member": ("Matteo Member", "member@spola.example", "texo.group_texo_member"),
    "senior": ("Silvia Senior", "senior@spola.example", "texo.group_texo_member"),
    "dev": ("Davide Dev", "dev@spola.example", "texo.group_texo_member"),
    "norole": ("Nicola Senzaruolo", "norole@spola.example", None),
}
WORK_GROUPS = ("project.group_project_user", "hr_timesheet.group_hr_timesheet_user")
TEAM = ("lead", "member", "senior", "dev")

# The stages of the projects: the last one of each list is folded (done).
DELIVERY_STAGES = ["Da fare", "In corso", "In attesa", "Completato"]
TICKET_STAGES = ["Aperto", "In lavorazione", "In attesa del cliente", "Risolto", "Chiuso"]
HOME_STAGES = ["New", "In Progress", "Done", "Cancelled"]
TICKET_TAG = "ticket"
ASSISTANCE = "Supporto {name}"

SOURCES_FOLDER = "https://files.spola.example/procedure"

# the generated PDFs: the organisation's own procedure and a report attached to a task
RELEASE_PDF = ("rilascio-in-produzione.pdf", "Procedura di rilascio in produzione", [
    "1. Il rilascio parte da un task con la spec nella description e i test verdi.",
    "2. Prima lo stage: aggiornamento dei moduli, prova con un utente del cliente, conferma scritta.",
    "3. Backup del database di produzione verificato prima di ogni aggiornamento.",
    "4. Aggiornamento in produzione in una finestra concordata, mai il venerdi pomeriggio.",
    "5. Controllo del log dopo il riavvio: nessun errore, nessun avviso nuovo.",
    "6. Nota di esito sul task con versione rilasciata e ore impiegate.",
])
ATTACHMENTS = {
    "test_report": ("verbale-collaudo-checkout.pdf", "Verbale di collaudo del checkout (fittizio)", [
        "Collaudo del checkout sullo stage del partner.",
        "Ordine con carta di prova, ordine con bonifico, ordine con ritiro in negozio: esito positivo.",
        "Email di conferma ricevuta in tutti e tre i casi.",
    ]),
}

ORGANISATION = {
    "documents": [
        {"key": "release", "name": "Procedura di rilascio in produzione",
         "summary": "I passi di un rilascio: dal task con i test verdi allo stage, al backup, alla produzione e "
                    "alla nota di esito.",
         "keywords": "rilascio, deploy, produzione, stage, backup, aggiornamento moduli",
         "pdf": RELEASE_PDF, "keep_text": True},
        {"key": "glossary", "name": "Glossario interno",
         "url": "https://files.spola.example/procedure/glossario.md",
         "summary": "Le parole che usiamo con i clienti e i loro equivalenti in Odoo.",
         "keywords": "glossario, termini, SAL, preventivo, offerta",
         "text_file": "glossario", "keep_text": True},
    ],
    "rules": [
        {"name": "Mai prove in produzione", "severity": "never", "activities": ["deploy", "code"],
         "section": "operations",
         "body": "Nessun test, nessuna installazione di prova e nessun aggiornamento di moduli sul database di "
                 "produzione di un cliente: si prova in locale o sullo stage.",
         "keywords": "produzione, prove, test, stage, aggiornamento", "document": "release"},
        {"name": "Backup prima di aggiornare", "severity": "must", "activities": ["deploy"], "section": "operations",
         "body": "Prima di aggiornare la produzione si verifica che l'ultimo backup si ripristini.",
         "keywords": "backup, ripristino, restore, aggiornamento", "document": "release"},
        {"name": "Dati dei clienti solo neutralizzati", "severity": "never", "activities": ["data"],
         "section": "compliance",
         "body": "Una copia del database di un cliente sulla macchina di lavoro e' sempre neutralizzata: niente "
                 "email in uscita, niente pagamenti, niente cron verso servizi esterni.",
         "keywords": "neutralizzazione, copia database, dati personali, privacy"},
        {"name": "Segreti fuori dal codice", "severity": "never", "activities": [], "section": "compliance",
         "body": "Password, chiavi API e token non vanno mai in un repository, in una nota o in un messaggio.",
         "keywords": "segreti, password, token, credenziali"},
        {"name": "Codice e commit in inglese", "severity": "must", "activities": ["code"], "section": "operations",
         "body": "Nomi, commenti e messaggi di commit in inglese; le stringhe per l'utente tradotte in it.po.",
         "keywords": "lingua del codice, inglese, traduzioni, i18n"},
        {"name": "Test verdi e log pulito", "severity": "must", "activities": ["code"], "section": "operations",
         "body": "Un modulo toccato si consegna con i suoi test verdi su un database di prova creato per il task "
                 "e senza avvisi nel log.",
         "keywords": "test, log, avvisi, warning, consegna"},
        {"name": "Prima lo standard", "severity": "prefer", "activities": ["analysis", "code"],
         "section": "operations",
         "body": "Davanti a una richiesta si verifica prima la configurazione standard, poi un modulo OCA, solo "
                 "alla fine un modulo nostro.",
         "keywords": "standard, configurazione, OCA, modulo custom"},
        {"name": "Domande chiuse al cliente", "severity": "prefer", "activities": ["communication"],
         "section": "operations",
         "body": "Una decisione del cliente si chiede come domanda chiusa, con la nostra proposta e le "
                 "conseguenze di ciascuna risposta.",
         "keywords": "domande, cliente, decisione, comunicazione"},
        {"name": "Nessun invio al cliente senza la persona", "severity": "never", "activities": ["communication"],
         "section": "operations",
         "body": "Un agente prepara la bozza di un messaggio al cliente; lo invia sempre una persona.",
         "keywords": "invio, email, bozza, cliente"},
        {"name": "Ore dalla persona", "severity": "must", "activities": [], "section": "operations",
         "body": "Le ore di un task le dice la persona che ha lavorato: mai stimate dall'agente.",
         "keywords": "ore, timesheet, rendicontazione"},
    ],
    "notes": [
        {"kind": "fact", "section": "profile", "name": "Chi e' Spola Informatica",
         "body": "Partner Odoo Community di sei persone a Bologna: analisi, sviluppo di moduli, migrazioni e "
                 "assistenza per piccole e medie imprese.",
         "keywords": "azienda, profilo, chi siamo, partner"},
        {"kind": "fact", "section": "profile", "name": "Ruoli del gruppo",
         "body": "Un lead che decide e rivede, una contabile senior, un analista e uno sviluppatore. Il lead "
                 "approva le regole e le lezioni.",
         "keywords": "ruoli, lead, senior, team"},
        {"kind": "fact", "section": "sector", "name": "Versioni seguite",
         "body": "Seguiamo Odoo Community dalla 17.0 alla 20.0; i progetti nuovi partono dall'ultima versione "
                 "con i moduli OCA necessari gia' migrati.",
         "keywords": "versioni, 17.0, 18.0, 19.0, 20.0, OCA"},
        {"kind": "fact", "section": "offer", "name": "Pacchetti di assistenza",
         "body": "L'assistenza si vende a pacchetti di ore prepagate; un ticket consuma le ore del pacchetto del "
                 "cliente.",
         "keywords": "pacchetti, ore prepagate, assistenza, ticket"},
        {"kind": "procedure", "section": "operations", "name": "Come si apre un ticket",
         "body": "1. Il ticket nasce nel progetto di supporto del cliente.\n2. Si riporta la richiesta con le "
                 "parole del cliente.\n3. Si classifica: errore, domanda, richiesta di modifica.\n4. Si assegna e "
                 "si risponde entro un giorno lavorativo.",
         "keywords": "ticket, supporto, apertura, assistenza"},
        {"kind": "procedure", "section": "operations", "name": "Come si chiude una sessione di lavoro",
         "body": "1. Nota interna sul task: cosa e' stato fatto e perche'.\n2. Ore dette dalla persona.\n3. "
                 "Aggiornamento del progetto se lo stato e' cambiato.\n4. Lezione se si e' imparato qualcosa che "
                 "vale per altri progetti.",
         "keywords": "chiusura sessione, nota, ore, aggiornamento"},
        {"kind": "procedure", "section": "operations", "name": "Rilascio in produzione",
         "body": "Si segue la procedura di rilascio: test verdi, stage, conferma del cliente, backup verificato, "
                 "aggiornamento in finestra, controllo del log, nota di esito.",
         "keywords": "rilascio, produzione, deploy", "document": "release"},
        {"kind": "fact", "section": "compliance", "name": "Trattamento dei dati dei clienti",
         "body": "Siamo responsabili del trattamento per i dati dei clienti che vediamo in assistenza: accesso "
                 "solo per il ticket aperto, copie locali neutralizzate, nessun dato in lezioni o repository.",
         "keywords": "GDPR, responsabile del trattamento, dati personali"},
    ],
    "home_tasks": [
        {"name": "Revisione mensile della memoria", "who": "lead", "hours": 2, "stage": "In Progress",
         "description": "Regole in bozza, fatti da verificare, lezioni duplicate.",
         "notes": [("lead", 3, "Due lezioni simili sulle traduzioni: da fondere alla prossima revisione.")],
         "worklog": [("lead", 3, 1, "Revisione delle bozze di regola")]},
        {"name": "Formazione interna sulla 20.0", "who": "dev", "hours": 6, "stage": "New",
         "description": "Le novita' della 20.0 per i moduli che manteniamo."},
    ],
}

SHOP = {
    "ref": "DEM-ARNO", "name": "Ceramiche Arno snc", "city": "Firenze",
    "size": "small", "odoo": "19.0", "hosting": "VPS del partner",
    "projects": [
        {"name": "Arno - Negozio online", "tags": ["website_sale", "19.0"],
         "description": "<p>Negozio online delle ceramiche su Odoo 19.0 Community: catalogo, carrello, pagamento "
                        "con carta e bonifico, ritiro in negozio. Vincolo: listino unico per sito e negozio.</p>",
         "milestones": [("Catalogo pronto", -20, 22), ("Go live", 10, None)],
         "tasks": [
             {"name": "Import del catalogo", "who": "member", "hours": 8, "stage": "Completato",
              "milestone": "Catalogo pronto", "tags": ["import"],
              "description": "Duecento articoli dal foglio del cliente, con varianti di colore.",
              "notes": [("member", 25, "Le varianti di colore arrivano come colonne: le trasformo in attributi.")],
              "worklog": [("member", 25, 5, "Preparazione e import del catalogo")]},
             {"name": "Pagamento con carta", "who": "dev", "hours": 10, "stage": "In corso",
              "milestone": "Go live", "tags": ["payment"],
              "description": "Provider di pagamento in modalita' di prova sullo stage.",
              "notes": [("dev", 4, "Il webhook del provider deve raggiungere lo stage: aperto l'indirizzo pubblico.")],
              "worklog": [("dev", 4, 3, "Configurazione del provider in prova")]},
             {"name": "Ritiro in negozio", "who": "member", "hours": 4, "stage": "In corso", "milestone": "Go live",
              "description": "Metodo di consegna gratuito con indirizzo del negozio.",
              "notes": [("member", 2, "Il cliente vuole il ritiro solo per gli ordini sotto i 30 kg.")]},
             {"name": "Collaudo del checkout", "who": "lead", "hours": 3, "stage": "In attesa", "milestone": "Go live",
              "description": "Tre ordini di prova con il cliente sullo stage.", "attachment": "test_report",
              "notes": [("lead", 1, "Collaudo positivo, aspettiamo la conferma scritta del cliente.")],
              "worklog": [("lead", 1, 2, "Collaudo con il cliente")]},
         ],
         "updates": [("Settimana 1", "on_track", 40, 14, "Catalogo importato, pagamento in configurazione."),
                     ("Settimana 3", "on_track", 75, 1, "Collaudo del checkout fatto; go live tra dieci giorni.")]},
    ],
    "tickets": [
        {"name": "Email di conferma ordine non arriva", "who": "member", "hours": 1, "stage": "Risolto", "days": 6,
         "description": "Il cliente non riceve la conferma di un ordine di prova.",
         "notes": [("member", 6, "Il server di posta in uscita dello stage era disattivato dalla neutralizzazione."),
                   ("member", 5, "Spiegato al cliente: in produzione le email partono.")],
         "worklog": [("member", 6, 1, "Analisi della posta in uscita")]},
        {"name": "Foto prodotto sgranate", "who": "dev", "hours": 1, "stage": "In lavorazione", "days": 2,
         "description": "Le immagini caricate appaiono sfocate nella scheda prodotto.",
         "notes": [("dev", 2, "Le foto originali sono piccole: chiedo al cliente le immagini in alta risoluzione.")]},
    ],
    "rules": [
        {"where": "customer", "name": "Listino unico", "severity": "must", "activities": ["analysis", "code"],
         "body": "Sito e negozio usano lo stesso listino: nessun prezzo diverso per il canale online.",
         "keywords": "listino, prezzi, sito, negozio"},
        {"where": "project:Arno - Negozio online", "name": "Nessuna modifica al tema senza bozza",
         "severity": "prefer", "activities": ["code"],
         "body": "Una modifica grafica del sito si mostra prima al cliente su una bozza.",
         "keywords": "tema, grafica, sito"},
    ],
    "documents": [
        {"where": "project:Arno - Negozio online", "key": "shop_brief", "name": "Brief del negozio online",
         "url": "https://files.spola.example/clienti/arno/brief.md",
         "summary": "Che cosa vende il negozio, come spedisce, quali pagamenti accetta.",
         "keywords": "brief, negozio online, spedizioni, pagamenti",
         "text": "## Brief\n\nCeramiche artigianali. Spedizione con corriere, ritiro in negozio. Carta e bonifico."},
    ],
    "notes": [
        {"where": "customer", "kind": "fact", "section": "profile", "name": "Chi decide in Ceramiche Arno",
         "body": "Decide la titolare; il figlio segue il sito e fa le prove.",
         "keywords": "decisioni, referente"},
    ],
}

DISTRIBUTOR = {
    "ref": "DEM-TREBBIA", "name": "Distribuzioni Valtrebbia spa", "city": "Piacenza",
    "size": "medium", "odoo": "17.0", "hosting": "server del cliente",
    "projects": [
        {"name": "Valtrebbia - Migrazione alla 19.0", "tags": ["migration", "17.0", "19.0", "stock", "OCA"],
         "description": "<p>Migrazione da Odoo 17.0 a 19.0 Community con OpenUpgrade: magazzino, acquisti, "
                        "vendite e sei moduli OCA. Vincolo: fermo massimo di un fine settimana.</p>",
         "milestones": [("Analisi dei moduli", -30, 31), ("Prova completa sullo stage", 15, None),
                        ("Migrazione in produzione", 40, None)],
         "tasks": [
             {"name": "Inventario dei moduli installati", "who": "senior", "hours": 6, "stage": "Completato",
              "milestone": "Analisi dei moduli", "tags": ["analysis"],
              "description": "Elenco dei moduli installati e del loro stato di migrazione alla 19.0.",
              "notes": [("senior", 33, "Su sei moduli OCA, cinque hanno gia' il ramo 19.0; uno solo una PR aperta.")],
              "worklog": [("senior", 33, 4, "Inventario e verifica dei rami OCA")]},
             {"name": "Modulo OCA senza ramo 19.0", "who": "dev", "hours": 16, "stage": "In corso",
              "milestone": "Prova completa sullo stage", "tags": ["OCA"],
              "description": "Partire dalla PR di migrazione aperta, applicarla, completare i test.",
              "notes": [("dev", 8, "La PR esistente copre il codice ma non le viste: completo le viste."),
                        ("dev", 3, "Test del modulo verdi su un database di prova, log pulito.")],
              "worklog": [("dev", 8, 6, "Migrazione del modulo dalla PR"), ("dev", 3, 4, "Viste e test")]},
             {"name": "Prova di migrazione del database", "who": "senior", "hours": 12, "stage": "In corso",
              "milestone": "Prova completa sullo stage",
              "description": "Copia neutralizzata del database, OpenUpgrade 17.0 -> 18.0 -> 19.0.",
              "notes": [("senior", 5, "Il salto a 18.0 passa; a 19.0 si ferma su un campo rinominato di un "
                                      "modulo nostro: serve uno script pre-migrazione.")],
              "worklog": [("senior", 5, 5, "Prima prova di migrazione")]},
             {"name": "Script di pre-migrazione", "who": "dev", "hours": 4, "stage": "Da fare",
              "milestone": "Prova completa sullo stage", "parent": "Prova di migrazione del database",
              "description": "Rinominare la colonna prima dell'aggiornamento del modulo."},
             {"name": "Piano del fine settimana di migrazione", "who": "lead", "hours": 3, "stage": "Da fare",
              "milestone": "Migrazione in produzione",
              "description": "Orari, backup, punti di controllo, ritorno indietro."},
         ],
         "updates": [("Analisi chiusa", "on_track", 25, 28, "Moduli censiti, un solo modulo OCA da migrare."),
                     ("Prima prova", "at_risk", 45, 4, "La migrazione a 19.0 si ferma su un campo rinominato: "
                                                       "script in preparazione, prova completa a rischio di una "
                                                       "settimana.")]},
    ],
    "rules": [
        {"where": "customer", "name": "Fermo solo nel fine settimana", "severity": "never",
         "activities": ["deploy", "migration"],
         "body": "Nessun fermo del gestionale nei giorni lavorativi: gli interventi lunghi solo nel fine settimana.",
         "keywords": "fermo, downtime, fine settimana"},
        {"where": "project:Valtrebbia - Migrazione alla 19.0", "name": "Ogni prova su copia neutralizzata",
         "severity": "must", "activities": ["migration", "data"],
         "body": "Ogni prova di migrazione parte da una copia del database neutralizzata il giorno stesso.",
         "keywords": "copia, neutralizzazione, prova di migrazione"},
    ],
    "documents": [],
    "notes": [
        {"where": "customer", "kind": "fact", "section": "operations", "name": "Magazzini di Valtrebbia",
         "body": "Due magazzini con ubicazioni, consegne in due passaggi.",
         "keywords": "magazzini, ubicazioni, consegne"},
        {"where": "project:Valtrebbia - Migrazione alla 19.0", "kind": "procedure", "section": "operations",
         "name": "Prova di migrazione con OpenUpgrade",
         "body": "1. Copia neutralizzata.\n2. Un salto di versione alla volta.\n3. Dopo ogni salto: log, "
                 "controllo dei moduli, prova di tre flussi di magazzino.",
         "keywords": "OpenUpgrade, salto di versione, migrazione"},
    ],
}

SERVICES = {
    "ref": "DEM-BRENTA", "name": "Studio Grafico Brenta", "city": "Padova",
    "size": "small", "odoo": "18.0", "hosting": "Docker presso un provider",
    "projects": [
        {"name": "Brenta - Ore e fatturazione", "tags": ["hr_timesheet", "sale_timesheet", "18.0"],
         "description": "<p>Fogli ore dei grafici e fatturazione a tempo e materiali su Odoo 18.0 Community. "
                        "Vincolo: fattura mensile per cliente.</p>",
         "milestones": [("Fogli ore in uso", -10, 12), ("Prima fattura mensile", 20, None)],
         "tasks": [
             {"name": "Configurazione dei servizi a ore", "who": "senior", "hours": 4, "stage": "Completato",
              "milestone": "Fogli ore in uso",
              "notes": [("senior", 14, "Servizi fatturati sulle ore registrate, non su quelle ordinate.")],
              "worklog": [("senior", 14, 3, "Configurazione dei prodotti servizio")]},
             {"name": "Formazione sui fogli ore", "who": "member", "hours": 2, "stage": "Completato",
              "milestone": "Fogli ore in uso",
              "worklog": [("member", 11, 2, "Formazione dei grafici")]},
             {"name": "Fattura mensile raggruppata", "who": "dev", "hours": 8, "stage": "In corso",
              "milestone": "Prima fattura mensile",
              "description": "Una fattura al mese per cliente con tutte le ore dei suoi ordini.",
              "notes": [("dev", 2, "Lo standard raggruppa per cliente se gli ordini condividono condizioni di "
                                   "pagamento e indirizzo di fatturazione: niente codice.")],
              "worklog": [("dev", 2, 2, "Verifica del raggruppamento standard")]},
             {"name": "Report delle ore non fatturate", "who": "member", "hours": 3, "stage": "Da fare",
              "milestone": "Prima fattura mensile"},
         ],
         "updates": [("Avvio", "on_track", 50, 2, "Fogli ore in uso; la fattura mensile usa lo standard.")]},
    ],
    "rules": [
        {"where": "customer", "name": "Fattura mensile per cliente", "severity": "must", "activities": ["analysis"],
         "body": "Ogni cliente dello studio riceve una sola fattura al mese.",
         "keywords": "fattura mensile, raggruppamento"},
    ],
    "documents": [],
    "notes": [],
}

CUSTOMERS = [SHOP, DISTRIBUTOR, SERVICES]

LESSONS = [
    {"key": "neutralized_mail", "title": "Una copia neutralizzata non invia email",
     "finding": "Dopo la neutralizzazione di un database il server di posta in uscita e' disattivato: le email di "
                "conferma di un ordine di prova non partono e sembra un errore del modulo.",
     "solution": "Prima di aprire un'analisi si controlla il server di posta in uscita; per provare un invio si "
                 "usa un server di prova che cattura i messaggi.",
     "tags": ["website_sale", "mail"], "applies_to": "17.0, 18.0, 19.0, 20.0", "state": "active", "who": "member",
     "activities": ["analysis"], "keywords": "email, posta in uscita, neutralizzazione, conferma ordine"},
    {"key": "payment_webhook", "title": "Il webhook del provider di pagamento deve raggiungere lo stage",
     "finding": "In modalita' di prova il pagamento resta in attesa se il provider non riesce a chiamare "
                "l'indirizzo di ritorno dello stage.",
     "solution": "Lo stage deve essere raggiungibile all'indirizzo pubblico configurato in web.base.url, con il "
                 "parametro bloccato.",
     "tags": ["payment", "website_sale"], "applies_to": "18.0, 19.0", "state": "active", "who": "dev",
     "activities": ["deploy"], "keywords": "webhook, pagamento, carta, web.base.url"},
    {"key": "variants_import", "title": "Le varianti si importano come attributi, non come prodotti",
     "finding": "Un foglio con una colonna per colore crea un prodotto per riga se importato cosi' com'e'.",
     "solution": "Si trasformano le colonne in valori di attributo e si importa il modello del prodotto con le "
                 "righe degli attributi; le varianti nascono da sole.",
     "tags": ["import", "product"], "applies_to": "17.0, 18.0, 19.0, 20.0", "state": "active", "who": "member",
     "activities": ["data"], "keywords": "varianti, attributi, import, colori"},
    {"key": "oca_open_pr", "title": "Un modulo OCA senza ramo si migra dalla PR aperta",
     "finding": "Un modulo OCA che non ha ancora il ramo della versione di arrivo ha spesso una PR di migrazione "
                "aperta, completa nel codice e incompleta nelle viste o nei test.",
     "solution": "Si parte dalla PR (non da zero), si completano viste e test, si propone il completamento nella "
                 "PR stessa.",
     "tags": ["OCA", "migration"], "applies_to": "OCA", "state": "active", "who": "dev",
     "activities": ["migration", "code"], "keywords": "OCA, pull request, migrazione modulo, ramo"},
    {"key": "renamed_column", "title": "Un campo rinominato tra due versioni ferma OpenUpgrade",
     "finding": "Se un modulo proprio rinomina un campo nella versione di arrivo, l'aggiornamento crea una colonna "
                "nuova vuota o si ferma su un vincolo.",
     "solution": "Uno script pre-migrazione rinomina la colonna prima che il modulo si aggiorni; i dati restano.",
     "tags": ["migration", "OpenUpgrade"], "applies_to": "17.0 -> 19.0", "state": "active", "who": "senior",
     "activities": ["migration"], "keywords": "pre-migrazione, colonna, rinomina campo"},
    {"key": "one_jump", "title": "Una migrazione si prova un salto di versione alla volta",
     "finding": "Saltare due versioni in una prova rende impossibile capire quale salto ha rotto i dati.",
     "solution": "Si migra una versione alla volta e dopo ogni salto si controllano log, moduli e tre flussi.",
     "tags": ["migration", "OpenUpgrade"], "applies_to": "OpenUpgrade", "state": "active", "who": "senior",
     "activities": ["migration"], "keywords": "salto di versione, prova, OpenUpgrade"},
    {"key": "invoice_grouping", "title": "Il raggruppamento delle fatture e' standard",
     "finding": "Le fatture di piu' ordini dello stesso cliente si raggruppano gia' se condividono condizioni di "
                "pagamento e indirizzo di fatturazione.",
     "solution": "Prima di scrivere codice si allineano condizioni e indirizzi degli ordini e si fattura insieme.",
     "tags": ["sale", "account"], "applies_to": "17.0, 18.0, 19.0, 20.0", "state": "active", "who": "dev",
     "activities": ["analysis", "code"], "keywords": "fattura unica, raggruppare fatture, fatturazione mensile"},
    {"key": "timesheet_delivered", "title": "Servizi a ore fatturati sulle ore registrate",
     "finding": "Un servizio con politica di fatturazione sulle quantita' ordinate fattura le ore previste, non "
                "quelle lavorate.",
     "solution": "Per il tempo e materiali la politica e' sulle quantita' consegnate, con le ore dai fogli ore.",
     "tags": ["sale_timesheet"], "applies_to": "17.0, 18.0, 19.0, 20.0", "state": "active", "who": "senior",
     "activities": ["analysis"], "keywords": "fogli ore, tempo e materiali, quantita' consegnate"},
    {"key": "image_resolution", "title": "Le immagini di prodotto vanno caricate grandi",
     "finding": "Odoo ridimensiona le immagini di prodotto: un originale piccolo resta sfocato nella scheda.",
     "solution": "Si chiede l'originale ad alta risoluzione, almeno full HD sul lato lungo.",
     "tags": ["website_sale", "product"], "applies_to": "17.0, 18.0, 19.0, 20.0", "state": "active",
     "who": "dev", "activities": ["analysis"], "keywords": "immagini, foto, risoluzione, sfocate"},
    {"key": "translations_export", "title": "I termini di traduzione si esportano, non si scrivono a mano",
     "finding": "Un msgid scritto a mano diverge da quello che Odoo estrae e la traduzione non si applica.",
     "solution": "Si esporta il file .pot dal database con il modulo aggiornato e si riempiono solo i msgstr.",
     "tags": ["i18n"], "applies_to": "17.0, 18.0, 19.0, 20.0", "state": "active", "who": "dev",
     "activities": ["code"], "keywords": "traduzioni, po, pot, msgid"},
    {"key": "translations_export_dup", "title": "Non scrivere i msgid a mano nei file po",
     "finding": "Scrivendo a mano le voci di un file di traduzione le stringhe non coincidono con quelle estratte.",
     "solution": "Esportare il template e tradurre solo le stringhe mancanti.",
     "tags": ["i18n"], "applies_to": "19.0", "state": "draft", "who": "member",
     "activities": ["code"], "keywords": "traduzioni, it.po"},
    {"key": "one_jump_dup", "title": "Migrare una versione per volta",
     "finding": "Una prova che salta due versioni nasconde dove nasce un errore.",
     "solution": "Un salto per prova, con i controlli dopo ciascuno.",
     "tags": ["migration"], "applies_to": "OpenUpgrade", "state": "draft", "who": "member",
     "activities": ["migration"], "keywords": "migrazione, versioni"},
    {"key": "pickup_weight", "title": "Un metodo di consegna si limita per peso con le regole del metodo",
     "finding": "Un ritiro o una spedizione disponibile solo sotto un certo peso non richiede codice.",
     "solution": "Si usa un metodo di consegna basato su regole con la condizione sul peso dell'ordine.",
     "tags": ["delivery", "website_sale"], "applies_to": "17.0, 18.0, 19.0, 20.0", "state": "active",
     "who": "member", "activities": ["analysis"], "keywords": "consegna, peso, ritiro, regole"},
]

# The search questions of the loader, resolved to the ids of the database it writes (<core>/scripts/eval_memoria.py).
EVAL = [
    {"query": "email di conferma che non partono su una copia", "scope": "lessons",
     "expected": [{"lesson": "neutralized_mail"}], "related_terms": ["posta in uscita", "neutralizzazione"]},
    {"query": "pagamento con carta resta in attesa sullo stage", "scope": "lessons",
     "expected": [{"lesson": "payment_webhook"}]},
    {"query": "importare prodotti con colori diversi", "scope": "lessons",
     "expected": [{"lesson": "variants_import"}], "related_terms": ["varianti", "attributi"]},
    {"query": "modulo OCA senza versione nuova", "scope": "lessons", "expected": [{"lesson": "oca_open_pr"}]},
    {"query": "campo rinominato blocca l'aggiornamento", "scope": "lessons",
     "expected": [{"lesson": "renamed_column"}]},
    {"query": "una sola fattura per piu' ordini", "scope": "lessons", "expected": [{"lesson": "invoice_grouping"}]},
    {"query": "si puo' fare una prova in produzione", "scope": "rules",
     "expected": [{"note": "Mai prove in produzione"}]},
    {"query": "backup prima dell'aggiornamento", "scope": "rules",
     "expected": [{"note": "Backup prima di aggiornare"}]},
    {"query": "come si apre un ticket", "scope": "procedures", "expected": [{"procedure": "Come si apre un ticket"}]},
    {"query": "chi e' l'azienda", "scope": "facts", "expected": [{"fact": "Chi e' Spola Informatica"}]},
    {"query": "passi del rilascio", "scope": "documents", "expected": [{"document": "release"}]},
]
