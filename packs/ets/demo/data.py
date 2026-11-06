# Copyright 2026 Daniele Lucarelli
# License CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/).
"""The demo of the pack ets: «Ginestra APS», an invented association of the third sector.

Everything is invented: the association, its people (staff and volunteers only), its funders' applications,
amounts and outcomes, its projects, tasks, chatter, hours, rules, facts, procedures, internal documents and
lessons. The structure (a help desk against violence, a shelter house, a communication campaign, volunteering)
is modelled on the kinds of services of a real association, read only for the kinds of services; no name,
wording or event is copied. The obligations of a small APS towards the RUNTS (deposit of the cash statement,
changes of officers, members data, own PEC, 5 per mille, public contributions on the website) follow the public
texts on the registry; what Ginestra did about them is invented. The funders are real institutions acting as
institutions (Regione Umbria, the Otto per mille of the Tavola valdese, the Comune), plus an invented foundation
(«Fondazione Valle Verde»). The public acts and the ministerial pages in demo/texts/*.md (converted with Docling)
are real and public; what Ginestra did about them is not.

Absolute constraints of the demo: no data about women hosted or helped, no cases, no stories, not even
invented ones; the address of the shelter house appears nowhere; the town is never named.

Two layers in one file. The raw layer is written as volunteers and staff of a small association write, not
for search: short task descriptions, colloquial chatter with internal jargon («la casa», «lo sportello», «il
magazzino di sopra», «la stanza blu», «8x1000», «rendic.»), uneven facts and procedures. The curated layer is
what an agent following the writing strategies of the memory added afterwards, without seeing the questions:
the searchable session note of each task, as the last note of its chatter, with the keywords it gives the task;
the keywords of rules, facts, procedures, lessons and documents; the summaries of the documents. The questions
of demo/questions.json were measured on this curated layer (scenario S1 of the memory scenarios).

Loaded by <core>/setup/load-demo.sh through <core>/scripts/load_demo.py, only into the databases of DATABASES;
the texts of the documents that name a text_file come from demo/texts/<stem>.md. Days are relative to the day
of the load.
"""

DATABASES = ("scenario-ets",)
TOKEN_NAME = "Ginestra demo"
TOKEN_DAYS = 30

COMPANY = {"name": "Ginestra APS", "email": "info@ginestra.example", "website": "https://ginestra.example"}

# role: (name, login, hub group). The coordinatrice is the lead; operatrice, tesoriera, comunicazione and a
# volunteer are members. The presidente has no account: she appears by first name in the chatter.
USERS = {
    "admin": ("Amministratore Ginestra", None, "texo.group_texo_admin"),
    "lead": ("Marta Ceccarelli", "coordinamento@ginestra.example", "texo.group_texo_lead"),
    "member": ("Elisa Fiorucci", "sportello@ginestra.example", "texo.group_texo_member"),
    "treasurer": ("Paola Rossetti", "tesoreria@ginestra.example", "texo.group_texo_member"),
    "comms": ("Giulia Menichetti", "comunicazione@ginestra.example", "texo.group_texo_member"),
    "volunteer": ("Sara Bartolini", "volontarie@ginestra.example", "texo.group_texo_member"),
}
WORK_GROUPS = ("project.group_project_user", "hr_timesheet.group_hr_timesheet_user")
TEAM = ("lead", "member", "treasurer", "comms", "volunteer")

# The stages: the last one of each list is folded (done).
DELIVERY_STAGES = ["Da fare", "In corso", "In attesa", "Fatto"]
TICKET_STAGES = ["Nuovo", "In lavorazione", "In attesa", "Risolto", "Chiuso"]
HOME_STAGES = ["Da fare", "In corso", "Fatto", "Annullato"]
HOUSE_STAGES = ["Segnalato", "In carico", "In attesa ditta", "Risolto"]
TICKET_TAG = "ticket"
ASSISTANCE = "Assistenza {name}"

# -- the documents of the organisation ----------------------------------------------------------------------
SOURCES_FOLDER = "https://drive.ginestra.example/procedure"

# the generated PDFs: the organisation's own vademecum and a report attached to a task of the house
VADEMECUM_PDF = ("vademecum-turno-sportello.pdf", "Vademecum del turno allo sportello", [
    "1. Si apre in due, mai da sole. Se manca la collega si chiama la coordinatrice prima di aprire.",
    "2. Il quaderno del turno resta nell'armadio chiuso della stanza blu: niente nomi, solo orari e note di servizio.",
    "3. Le schede dei colloqui le compilano solo le operatrici, non le volontarie.",
    "4. Telefonate di giornalisti: si prende il recapito e si gira alla coordinatrice.",
    "5. A fine turno: luci, finestre, allarme, chiavi nella cassetta a codice.",
    "6. Guasti e mancanze: si scrivono subito nel progetto Casa o nel gruppo, non a voce.",
])
ATTACHMENTS = {
    "stage_report": ("verbale-sopralluogo-caldaia.pdf", "Rapporto di intervento caldaia (fittizio)", [
        "Intervento su chiamata per blocco caldaia.",
        "Sostituita la sonda NTC del circuito sanitario; pressione impianto riportata a 1,3 bar.",
        "Consigliata la pulizia dello scambiatore entro la primavera.",
    ]),
}

URL_ULS2 = "https://www.regione.umbria.it/la-regione/bandi?codBando=2026-002-10389"
URL_APS = "https://www.regione.umbria.it/la-regione/bandi?codBando=2026-001-03832"

# -- the organisation ----------------------------------------------------------------------------------------
P_CAMPAGNA = "Campagna «Ci riguarda» 2026"
P_CASA = "Casa"
P_VOLONTARIATO = "Volontariato 2026-2027"
P_RUNTS = "Registro RUNTS 2026"

ORGANISATION = {
    "documents": [
        {"key": "vademecum", "name": "Vademecum del turno allo sportello",
         "summary": "Documento interno dell'associazione con le regole pratiche del turno allo sportello "
                    "antiviolenza. Riguarda il turno in due, il quaderno del turno, la chiusura dello sportello e "
                    "come gestire le telefonate dei giornalisti.",
         "keywords": "vademecum turno, regole del turno, sportello antiviolenza, turno in due, quaderno dei turni, "
                     "chiusura sportello, telefonate giornalisti, istruzioni volontarie",
         "pdf": VADEMECUM_PDF, "keep_text": True},
        {"key": "verbale_assemblea", "name": "Verbale assemblea dei soci aprile 2026",
         "summary": "Verbale dell'assemblea ordinaria dei soci di aprile 2026 (21 presenti su 34, di cui 4 per "
                    "delega). Approva all'unanimità il bilancio 2025 (rendiconto per cassa e relazione di missione) "
                    "da depositare al RUNTS entro il 30 giugno, rinnova il direttivo e conferma la quota associativa "
                    "a 20 euro (10 per studenti). Decide di non partecipare a bandi con cofinanziamento oltre il 20% "
                    "senza delibera specifica del direttivo e chiede di rifare il regolamento delle volontarie entro "
                    "l'estate.",
         "keywords": "verbale assemblea, assemblea ordinaria soci, approvazione bilancio 2025, rinnovo direttivo, "
                     "quota associativa, cofinanziamento 20%, regolamento volontarie, deposito RUNTS",
         "url": "https://drive.ginestra.example/assemblee/2026-04-verbale", "keep_text": True,
         "text": "## Verbale dell'assemblea ordinaria dei soci\n\n"
                 "Presenti 21 socie e soci su 34, di cui 4 per delega. Presiede Anna, verbalizza Paola.\n\n"
                 "1. Bilancio 2025: la tesoriera illustra rendiconto per cassa e relazione di missione. Approvato "
                 "all'unanimità. Da depositare al RUNTS entro il 30 giugno.\n"
                 "2. Rinnovo del direttivo: confermate Anna presidente, Marta, Paola; entra Giulia al posto di "
                 "Franca che lascia per motivi di lavoro.\n"
                 "3. Quota associativa: resta 20 euro, 10 per studenti.\n"
                 "4. Varie: si decide di non partecipare più a bandi che chiedono cofinanziamento oltre il 20% "
                 "senza una delibera specifica del direttivo. Si chiede di rifare il regolamento delle volontarie "
                 "entro l'estate.\n"},
        {"key": "regolamento_volontarie", "name": "Regolamento interno delle volontarie (rev. luglio 2026)",
         "summary": "Regolamento interno delle volontarie approvato dal direttivo a luglio 2026. Disciplina ingresso "
                    "(colloquio, registro volontari e assicurazione prima di ogni attività), formazione (corso base "
                    "di 40 ore obbligatorio, modulo specifico per la casa, supervisione mensile), turni (almeno uno a "
                    "settimana o quattro al mese, mai da sole allo sportello), riservatezza (patto valido anche dopo "
                    "l'uscita, indirizzo della casa mai comunicato) e uscita (restituzione di chiavi e badge).",
         "keywords": "regolamento volontarie, regolamento interno, ingresso volontarie, corso base 40 ore, "
                     "supervisione mensile, turni, patto di riservatezza, uscita volontarie",
         "url": "https://drive.ginestra.example/regolamenti/volontarie-2026", "keep_text": True,
         "text": "## Regolamento interno delle volontarie\n\n"
                 "Art. 1 Ingresso. Colloquio con la coordinatrice e una operatrice. Iscrizione al registro dei "
                 "volontari e copertura assicurativa prima di qualsiasi attività.\n\n"
                 "Art. 2 Formazione. Il corso base (40 ore) è obbligatorio prima dei turni allo sportello; per "
                 "la casa serve anche il modulo specifico. Supervisione mensile obbligatoria per chi fa turni.\n\n"
                 "Art. 3 Turni. Almeno un turno a settimana o quattro al mese. I cambi si concordano nel gruppo "
                 "turni e si avvisa la coordinatrice. Allo sportello mai da sole.\n\n"
                 "Art. 4 Riservatezza. Il patto di riservatezza vale anche dopo l'uscita dall'associazione. Non si "
                 "parla delle attività dello sportello e della casa fuori dagli spazi dell'associazione, né sui "
                 "social. L'indirizzo della casa non si comunica a nessuno.\n\n"
                 "Art. 5 Uscita. Chi lascia restituisce chiavi e badge e viene tolta dai gruppi.\n"},
        {"key": "cts_runts", "name": "Codice del Terzo settore (D.Lgs. 117/2017), articoli scelti",
         "summary": "Estratto del Codice del Terzo settore (D.Lgs. 3 luglio 2017, n. 117), testo vigente al 1° "
                    "novembre 2026 da normattiva.it, con gli articoli su enti, APS, volontari, scritture contabili, "
                    "RUNTS, norme transitorie e fiscali. Fissa tra l'altro il rendiconto per cassa per gli enti senza "
                    "personalità giuridica sotto 300.000 euro, il minimo di 7 soci per le APS (da reintegrare entro "
                    "un anno), i rimborsi ai volontari, l'obbligo di assicurazione e il deposito degli atti.",
         "keywords": "Codice del Terzo settore, CTS, D.Lgs. 117/2017, ETS Enti del Terzo settore, APS, volontari, "
                     "rendiconto per cassa, RUNTS",
         "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2017-07-03;117",
         "text_file": "cts-articoli-runts"},
        {"key": "dm_106_2020", "name": "DM 106/2020 - il RUNTS (testo GU)",
         "summary": "Decreto del Ministro del Lavoro e delle Politiche sociali 15 settembre 2020, n. 106, pubblicato "
                    "in Gazzetta Ufficiale, che istituisce le regole del Registro unico nazionale del Terzo settore. "
                    "Definisce le procedure di iscrizione degli enti, il deposito degli atti, gli aggiornamenti, la "
                    "diffida e la cancellazione. È stato modificato dal DM 2/2026.",
         "keywords": "DM 106/2020, RUNTS, Registro unico nazionale del Terzo settore, decreto ministeriale, "
                     "iscrizione, deposito atti, diffida, cancellazione",
         "url": "https://www.gazzettaufficiale.it/eli/id/2020/10/21/20A05821/sg", "text_file": "dm-106-2020-runts"},
        {"key": "dm_bilancio_ets", "name": "DM 5 marzo 2020 - modelli di bilancio ETS",
         "summary": "Decreto del Ministro del Lavoro e delle Politiche sociali 5 marzo 2020 (GU n. 102 del 18-4-2020) "
                    "che adotta la modulistica di bilancio degli enti del Terzo settore. Approva stato patrimoniale "
                    "(Mod. A), rendiconto gestionale (Mod. B), relazione di missione (Mod. C) e rendiconto per cassa "
                    "(Mod. D), quest'ultimo per gli enti con entrate inferiori alla soglia allora fissata a 220.000 "
                    "euro.",
         "keywords": "DM 5 marzo 2020, modelli di bilancio, schemi di bilancio ETS, Modello D, rendiconto per cassa, "
                     "stato patrimoniale, relazione di missione, 220.000 euro",
         "url": "https://www.gazzettaufficiale.it/eli/id/2020/04/18/20A02158/sg",
         "text_file": "dm-5-marzo-2020-bilancio-ets"},
        {"key": "dm_2_2026", "name": "DM 2/2026 - modifiche al DM 106/2020 (notizia del Ministero)",
         "summary": "Notizia del Ministero del Lavoro del 23 marzo 2026 sul DM n. 2 del 13 gennaio 2026 (GU n. 66 del "
                    "20 marzo 2026), che modifica il DM 106/2020 sul RUNTS. Introduce il delegato del legale "
                    "rappresentante, con delega alla sola compilazione e invio o anche alla sottoscrizione, porta il "
                    "deposito del bilancio a 180 giorni, chiede i dati di soci e volontari una volta l'anno entro il "
                    "30 giugno solo se cambiati e rende obbligatoria la PEC propria dell'ente. Operativo dal 9 aprile "
                    "2026.",
         "keywords": "DM 2/2026, modifiche DM 106/2020, delega telematica, delegato del legale rappresentante, PEC "
                     "obbligatoria, 180 giorni, dati soci 30 giugno, RUNTS",
         "url": "https://www.lavoro.gov.it/notizie/runts-pubblicato-in-gazzetta-ufficiale-il-dm-2-2026",
         "text_file": "mlps-dm-2-2026-modifiche-runts"},
        {"key": "deposito_bilanci", "name": "Deposito dei bilanci nel RUNTS (Ministero)",
         "summary": "Pagina del Ministero del Lavoro sul deposito dei bilanci nel RUNTS. Il bilancio (o rendiconto "
                    "per cassa) va depositato con i rendiconti delle raccolte fondi entro 180 giorni dalla chiusura "
                    "dell'esercizio, esclusivamente dal portale RUNTS con una pratica di deposito bilancio; gli invii "
                    "via PEC non sono validi. Gli enti sopra 1 milione di entrate depositano anche il bilancio "
                    "sociale.",
         "keywords": "deposito bilanci, RUNTS, 180 giorni, portale RUNTS, pratica deposito bilancio, raccolte fondi, "
                     "invio PEC non valido, bilancio sociale",
         "url": "https://www.lavoro.gov.it/notizie/runts-deposito-dei-bilanci",
         "text_file": "mlps-deposito-bilanci-runts"},
        {"key": "circolare_6_2026", "name": "Circolare 6/2026 - rendiconto per cassa aggregato",
         "summary": "Notizia del Ministero del Lavoro sulla circolare n. 6 del 17 aprile 2026, che chiarisce l'uso "
                    "del rendiconto per cassa in forma aggregata (Modello E, DM 18 febbraio 2026) per gli ETS con "
                    "ricavi non superiori a 60.000 euro. Per chi ha l'esercizio sull'anno solare il Modello E si usa "
                    "dal rendiconto chiuso al 31/12/2026; gli enti con personalità giuridica sotto 60.000 euro con "
                    "esercizio già chiuso possono usare il Modello D.",
         "keywords": "circolare 6/2026, Modello E, rendiconto per cassa aggregato, bilancino semplificato, 60.000 "
                     "euro, 31/12/2026, Modello D, Ministero del Lavoro",
         "url": "https://www.lavoro.gov.it/notizie/codice-terzo-settore-chiarimenti-rendiconto-cassa-forma-aggregata",
         "text_file": "mlps-circolare-6-2026-rendiconto-cassa"},
        {"key": "manuale_runts", "name": "Manuale utente del portale RUNTS",
         "summary": "Manuale utente del portale di Front Office del RUNTS del Ministero del Lavoro (release 3, "
                    "versione del 26/06/2023). Spiega accesso al portale, home page e le pratiche di iscrizione, "
                    "variazione, deposito bilancio, cancellazione e cinque per mille, con allegati, firma e invio, "
                    "oltre alla lista pratiche e ai messaggi.",
         "keywords": "manuale RUNTS, portale Front Office, guida utente, pratica di variazione, pratica deposito "
                     "bilancio, pratica cinque per mille, invio pratica, istruzioni portale",
         "url": "https://servizi.lavoro.gov.it/runts/it-it/Manuale-utente-front-office",
         "text_file": "mlps-manuale-portale-runts"},
        {"key": "dd_8521", "name": "DD 8521/2026 Regione Umbria - indicazioni operative RUNTS",
         "summary": "Determinazione dirigenziale n. 8521 del 25/08/2026 del Servizio regionale terzo settore della "
                    "Regione Umbria che approva le «Indicazioni operative per la corretta gestione degli adempimenti "
                    "sul RUNTS». Richiama il DM 2/2026 con la delega telematica operativa dal 9 aprile 2026, il "
                    "Modello E e la circolare 6/2026. È la «lettera della Regione» arrivata via PEC a settembre a "
                    "tutti gli enti, non una diffida.",
         "keywords": "DD 8521/2026, determina dirigenziale, Regione Umbria, indicazioni operative RUNTS, ufficio "
                     "RUNTS regionale, lettera della Regione, PEC settembre, adempimenti",
         "url": "https://www.regione.umbria.it/sociale/terzo-settore/runts?atto=dd-8521-2026",
         "text_file": "dd-8521-2026-runts-umbria"},
        {"key": "dd_8521_allegato", "name": "Indicazioni operative RUNTS Umbria (allegato DD 8521/2026)",
         "summary": "Allegato 1 alla DD 8521/2026: indicazioni operative dell'ufficio RUNTS della Regione Umbria per "
                    "gli enti del Terzo settore. Ricorda gli obblighi (variazioni entro 30 giorni, dati di soci e "
                    "volontari entro il 30 giugno, deposito del bilancio e dei rendiconti delle raccolte fondi entro "
                    "180 giorni), chi può presentare le istanze (legale rappresentante, amministratori, delegato "
                    "telematico, commercialista solo per il bilancio), la classificazione dei documenti, la "
                    "quadratura cassa e banca, le comunicazioni solo via PEC, i ticket per i problemi del portale e "
                    "il rinvio al CSV.",
         "keywords": "indicazioni operative RUNTS, allegato DD 8521/2026, Regione Umbria, delega telematica, "
                     "variazioni 30 giorni, quadratura cassa e banca, classificazione documenti, CSV centro servizi "
                     "volontariato",
         "url": "https://www.regione.umbria.it/sociale/terzo-settore/runts?atto=dd-8521-2026-allegato-1",
         "text_file": "dd-8521-2026-allegato-indicazioni-operative"},
    ],
    "rules": [
        {"name": "L'indirizzo della casa non compare mai", "severity": "never", "activities": [],
         "section": "compliance",
         "keywords": "indirizzo casa rifugio, luogo segreto, riservatezza indirizzo, indirizzo sportello, consegne, "
                     "ditte, sicurezza ospiti, vicino a",
         "body": "L'indirizzo della casa rifugio non si scrive da nessuna parte: né qui, né nei documenti, nei "
                 "post, nelle mail ai finanziatori, nei preventivi. Per consegne e ditte si usa l'indirizzo dello "
                 "sportello e si accompagna di persona. Nemmeno indicazioni tipo «vicino a»."},
        {"name": "Nessun dato delle donne nella memoria", "severity": "never", "activities": [],
         "section": "compliance",
         "keywords": "privacy, ospiti, dati personali, donne accolte, anonimato, dati sensibili, archivio cartaceo, "
                     "GDPR",
         "body": "Qui non vanno nomi, iniziali, età, provenienza, situazioni o qualsiasi cosa che riguardi le "
                 "donne che si rivolgono allo sportello o sono ospiti della casa. Nemmeno numeri piccoli che "
                 "permettono di riconoscerle. Le schede stanno solo nell'archivio cartaceo chiuso."},
        {"name": "Riservatezza dello sportello", "severity": "never", "activities": ["communication", "reporting"],
         "section": "compliance",
         "keywords": "riservatezza, segreto, confidenzialità, gruppi whatsapp, note dei turni, sportello "
                     "antiviolenza, non raccontare",
         "body": "Quello che succede allo sportello non si racconta: né nei gruppi whatsapp, né in questa "
                 "memoria, né alle amiche. Nelle note dei turni solo cose di servizio (orari, guasti, mancanze)."},
        {"name": "Con la stampa parlano solo presidente e coordinatrice", "severity": "must",
         "activities": ["communication"], "section": "operations",
         "keywords": "rapporti con la stampa, giornalisti, interviste, media, dichiarazioni, portavoce, tv radio",
         "body": "Giornalisti, tv, radio: si prende il contatto e si gira alla coordinatrice. Interviste e "
                 "dichiarazioni le fanno solo la presidente o la coordinatrice. Vale anche agli eventi."},
        {"name": "Foto: mai la casa, mai persone senza liberatoria", "severity": "never",
         "activities": ["communication"], "section": "compliance",
         "keywords": "foto, fotografie, casa rifugio, liberatoria, social, controllo foto, immagini, furgone",
         "body": "Non si fotografa la casa, né dentro né fuori, né il furgone davanti. Agli eventi si "
                 "pubblicano persone solo con liberatoria firmata. Dopo il post di settembre ogni foto passa da "
                 "Giulia prima di uscire."},
        {"name": "Spese dei progetti solo tracciabili", "severity": "must", "activities": ["reporting"],
         "section": "operations",
         "keywords": "tracciabilità, pagamenti tracciabili, bonifico, carta associazione, niente contanti, spese di "
                     "progetto, cassa contanti",
         "body": "Le spese dei progetti finanziati si pagano solo con bonifico o carta dell'associazione, mai "
                 "in contanti, nemmeno piccole. La cassa contanti è solo per spese minute fuori progetto."},
    ],
    "notes": [
        {"kind": "fact", "section": "profile", "name": "Chi è Ginestra",
         "keywords": "APS, Associazione di promozione sociale, sportello antiviolenza, casa rifugio, centro "
                     "antiviolenza, soci, volontarie, operatrici, laboratori nelle scuole, profilo associazione",
         "body": "APS nata nel 2013. Gestisce lo sportello antiviolenza (in convenzione con il Comune) e la casa "
                 "rifugio. 34 soci, una ventina di volontarie attive, tre operatrici part time. Fa anche "
                 "laboratori nelle scuole e una campagna all'anno intorno al 25 novembre."},
        {"kind": "fact", "section": "operations", "name": "Orari sportello",
         "keywords": "orari sportello, orario di apertura, apertura sabato, reperibilità telefonica, fuori orario, "
                     "turni operatrici, quando siamo aperte",
         "body": "lun 15-19, mer 9-13, ven 15-19, sab 10-12 (dal 2026 col progetto regionale). Fuori orario "
                 "c'è la reperibilità telefonica delle operatrici, a rotazione."},
        {"kind": "fact", "section": "operations", "name": "Chiavi del magazzino di sopra",
         "keywords": "chiavi magazzino, magazzino di sopra, cambio serratura, cassetta a codice, codice cassetta, "
                     "copie chiavi, mazzo smarrito",
         "body": "Dopo il cambio della serratura (14 ottobre, il mazzo di Bea non si trovava più) le chiavi "
                 "nuove sono tre: Marta, Paola, e la cassetta a codice dello sportello. Le vecchie non aprono più. "
                 "Il codice della cassetta lo sanno solo operatrici e chi ha il turno, non si scrive."},
        {"kind": "fact", "section": "compliance", "name": "Firma digitale presidente",
         "keywords": "firma digitale, PEC, rinnovo firma digitale, firma scaduta, legale rappresentante, posta "
                     "elettronica certificata, PEC associazione",
         "body": "La firma digitale di Anna era scaduta a settembre (ce ne siamo accorte preparando la domanda "
                 "regionale). Rinnovata l'8 ottobre, vale tre anni. La PEC dell'associazione la gestisce Paola (fino "
                 "a luglio sul registro c'era la pec della commercialista)."},
        {"kind": "fact", "section": "compliance", "name": "RUNTS",
         "keywords": "RUNTS, Registro unico nazionale del Terzo settore, iscrizione sezione APS, deposito bilancio, "
                     "aggiornamento cariche, registro, 30 giugno",
         "body": "Iscritte al RUNTS sezione APS dal 2023. Ogni anno: deposito del bilancio approvato entro il 30 "
                 "giugno e aggiornamento delle cariche se cambiano. Lo fa Paola con la commercialista."},
        {"kind": "fact", "section": "compliance", "name": "Assicurazione volontarie",
         "keywords": "assicurazione volontarie, polizza infortuni, RC responsabilità civile, rinnovo 31 gennaio, "
                     "comunicazione nominativo, copertura assicurativa, nuove volontarie",
         "body": "Polizza infortuni e RC volontari, rinnovo al 31 gennaio. Una volontaria nuova è coperta solo "
                 "dal giorno dopo la comunicazione del nominativo all'assicurazione: prima niente turni."},
        {"kind": "fact", "section": "operations", "name": "Conto e pagamenti",
         "keywords": "conto corrente, home banking, doppia autorizzazione, carta prepagata, cassa contanti, "
                     "pagamenti, bonifici, banca",
         "body": "Un conto corrente, home banking con doppia autorizzazione sopra 1.500 euro (Paola + Anna). "
                 "Carta prepagata per acquisti online, la tiene Marta. Cassa contanti max 150 euro."},
        {"kind": "procedure", "section": "operations", "name": "Nuova volontaria",
         "keywords": "volontaria, ingresso, formazione, nuova volontaria, ingresso volontarie, colloquio, registro "
                     "volontari, patto di riservatezza, corso base 40 ore, affiancamento, onboarding",
         "body": "colloquio (Marta + un'operatrice)\nregistro volontari + comunicazione all'assicurazione\n"
                 "patto di riservatezza firmato\ncorso base 40 ore\n3 turni in affiancamento\n"
                 "poi entra nel gruppo turni. chiavi solo dopo il primo mese"},
        {"kind": "procedure", "section": "operations", "name": "Donazioni in natura",
         "keywords": "donazioni in natura, beni donati, foglio donazioni, ricevuta donazione, cosa si accetta, "
                     "magazzino di sopra, Caritas, regali materiali",
         "body": "1. Si accetta solo roba nuova o in ottimo stato: niente materassi e cuscini usati, niente "
                 "vestiti non lavati, niente alimenti aperti o scaduti.\n2. Si scrive nel foglio donazioni (data, "
                 "cosa, quantità, chi ha portato se vuole essere ringraziato).\n3. Se il donatore vuole la "
                 "ricevuta la fa Paola (valore dichiarato dal donatore, non lo stimiamo noi).\n4. Etichetta con "
                 "la data e su nel magazzino di sopra. Alla casa ci va solo chi ci deve andare.\n5. Quello che non "
                 "serve va alla Caritas o allo scambio del mercoledì."},
        {"kind": "procedure", "section": "operations", "name": "Caldaia in blocco",
         "keywords": "caldaia in blocco, reset caldaia, pressione impianto, riscaldamento guasto, ditta caldaia, "
                     "stufette elettriche, tecnico, procedura caldaia",
         "body": "Se la caldaia della casa va in blocco: una volta sola il tasto reset. Guardare la pressione, deve "
                 "stare tra 1 e 1,5. Se è sotto, si carica dal rubinetto sotto (solo le operatrici). Se ri-blocca "
                 "non si insiste: si chiama la ditta Bastianelli (numero nella cassetta e nel gruppo casa), si "
                 "avvisa Marta e si apre il task in Casa. Le stufette elettriche sono nel magazzino di sopra. "
                 "Il tecnico si accompagna, non gli si dà l'indirizzo per telefono."},
        {"kind": "procedure", "section": "operations", "name": "Cambio turno",
         "keywords": "cambio turno, sostituzione turno, gruppo turni, scambio turno, sportello chiuso, cartello "
                     "chiusura, mai da sola",
         "body": "si chiede nel gruppo turni, chi prende il turno risponde, si avvisa Marta. Mai lasciare lo "
                 "sportello con una sola persona: se non si trova il cambio si chiude e si mette il cartello"},
        {"kind": "procedure", "section": "operations", "name": "Comunicati e post",
         "keywords": "comunicato, social, comunicato stampa, post social, approvazione post, controllo foto, "
                     "liberatoria, logo finanziatore, pubblicazione, comunicazione",
         "body": "Bozza di Giulia, la legge Marta, se è un comunicato lo firma Anna. Foto sempre controllate "
                 "(niente casa, niente targhe, niente volti senza liberatoria). Per i progetti finanziati il "
                 "logo del finanziatore."},
        {"kind": "fact", "section": "profile", "name": "Assemblea e direttivo",
         "keywords": "assemblea soci, consiglio direttivo, organi sociali, presidente, componenti direttivo, cambio "
                     "presidenza, approvazione bilancio 30 aprile",
         "body": "Assemblea ordinaria entro il 30 aprile per il bilancio. Direttivo di 5: Anna (presidente), "
                 "Marta, Paola, Giulia, Lucia. Si riunisce il primo martedì del mese.\n\nagg. 20/10: Anna lascia la "
                 "presidenza (resta nel direttivo), presidente Lucia."},
        {"kind": "fact", "section": "operations", "name": "Cartella documenti standard",
         "keywords": "documenti standard, cartella documenti, statuto, atto costitutivo, bilancio con verbale, visura "
                     "RUNTS, CV dell'ente, documenti per bandi",
         "body": "Dopo il pulmino (bando Valle Verde perso) c'è la cartella «documenti standard» sul drive: "
                 "statuto, atto costitutivo, ultimo bilancio approvato con verbale, CV dell'ente, documento e "
                 "codice fiscale di Anna, visura RUNTS. Paola la aggiorna a maggio dopo l'assemblea."},
        {"kind": "procedure", "section": "compliance", "name": "Caricare il bilancio sul registro",
         "keywords": "deposito bilancio, RUNTS, bilancino PDF unico, rendiconto raccolte fondi, quadratura cassa e "
                     "banca, pratica deposito bilanci, verbale classificato, annualità",
         "body": "- bilancino in un solo PDF: rendiconto per cassa + rendiconti delle raccolte fondi (anche se a "
                 "pareggio) DENTRO lo stesso file\n- controllare cassa e banca: quella dell'anno prima +/- avanzo = "
                 "quella di quest'anno, sennò lo rimandano\n- pratica «deposito bilanci», non variazione. annualità "
                 "= anno chiuso, non anno del deposito\n- verbale dell'assemblea a parte, classificato VERBALE\n"
                 "- firma la presidente o chi ha la delega\n- poi guardare la pec dell'associazione per gli esiti"},
        {"kind": "procedure", "section": "compliance", "name": "Cambio cariche sul registro",
         "keywords": "cariche, presidente, variazione, variazione cariche, cambio presidente, titolari delle cariche, "
                     "istanza di variazione, legale rappresentante, RUNTS, entro 30 giorni, verbale di nomina",
         "body": "Entro 30 giorni dalla nomina: istanza di variazione sul portale, sezione titolari delle cariche "
                 "con le date di nomina, numero dei componenti del direttivo uguale allo statuto, verbale "
                 "allegato. Niente documenti d'identità (non li vogliono). Poi banca, PEC e 5x1000 se cambia il "
                 "legale rappresentante."},
        {"kind": "procedure", "section": "operations", "name": "Rimborsi spese volontarie",
         "keywords": "rimborsi spese, rimborso volontarie, autocertificazione, scontrini, 10 euro al giorno, 150 euro "
                     "al mese, rimborso forfettario, delibera direttivo",
         "body": "con gli scontrini si rimborsa tutto quello che è autorizzato. senza scontrini: autocertificazione "
                 "(modulo in drive) max 10 euro al giorno e 150 al mese, e deve deciderlo il direttivo che tipo "
                 "di spese. mai rimborsi forfettari fissi. Paola paga con bonifico a fine mese"},
        {"kind": "fact", "section": "compliance", "name": "Scadenze del registro",
         "keywords": "scadenze RUNTS, scadenzario, deposito bilancio 180 giorni, dati soci 30 giugno, variazioni 30 "
                     "giorni, contributi pubblici, 5x1000 elenco permanente, diffida e cancellazione",
         "body": "bilancio: 180 gg dalla chiusura, per noi 30 giugno\nsoci/volontari/dipendenti: entro 30/6 solo "
                 "se cambiati (al 31/12)\ncariche, sede, statuto, pec: 30 gg\ncontributi pubblici sul sito: 30/6\n"
                 "5x1000: siamo nell'elenco permanente, si rifà solo se cambia il legale rappresentante o l'iban "
                 "(da verificare)\nse non depositi ti diffidano (da 30 a 180 giorni) e poi ti cancellano"},
        {"kind": "fact", "section": "compliance", "name": "Contributi pubblici sul sito",
         "keywords": "contributi pubblici, obbligo di trasparenza, pubblicazione sito, sovvenzioni pubbliche, 10.000 "
                     "euro, sanzione 1%, scadenza 30 giugno, pagina trasparenza",
         "body": "Siccome prendiamo più di 10.000 euro l'anno da enti pubblici (convenzione Comune, Fili, prima "
                 "Passi) entro il 30 giugno pubblichiamo sul sito l'elenco dei contributi dell'anno prima. Se non "
                 "lo fai la sanzione è l'1% di quello che hai preso, minimo 2.000. La pagina la tiene Giulia, i "
                 "numeri li dà Paola."},
        {"kind": "fact", "section": "compliance", "name": "Bilancino: rendiconto per cassa",
         "keywords": "rendiconto per cassa, bilancino, Modello D, Modello E aggregato, soglia 60.000 euro, soglia "
                     "300.000 euro, titolo X fiscale, Cesvol",
         "body": "Non abbiamo personalità giuridica e stiamo molto sotto i 300.000 (prima erano 220.000) quindi "
                 "rendiconto per cassa, Mod. D. Il Mod. E aggregato è per chi sta sotto 60.000 di entrate, dal "
                 "bilancio 2026. Dal 2026 vale anche la parte fiscale del codice (titolo X): la commercialista "
                 "dice che per noi cambia poco ma le raccolte fondi vanno rendicontate bene. Per dubbi c'è il "
                 "Cesvol."},
    ],
    "home_tasks": [
        {"name": "Assemblea soci aprile", "who": "lead", "stage": "Fatto",
         "description": "convocazione 15 gg prima, bilancio, rinnovo direttivo",
         "notes": [("lead", 200, "convocazione mandata per mail e whatsapp. sala parrocchia prenotata"),
                   ("treasurer", 186, "bilancio approvato, verbale in drive. ora deposito RUNTS"),
                   ("lead", 186, "Sintomo: entro aprile l'assemblea dei soci doveva approvare il bilancio e rinnovare "
                                 "il direttivo. Causa / contesto: assemblea ordinaria con convocazione 15 giorni "
                                 "prima; approvazione del bilancio 2025 (rendiconto per cassa) da depositare poi sul "
                                 "RUNTS. Intervento e stato: convocazione inviata per mail e whatsapp, sala della "
                                 "parrocchia prenotata; bilancio approvato, verbale nel drive; segue il deposito al "
                                 "registro. Fatto.",
                                 ["assemblea soci", "assemblea ordinaria", "convocazione", "approvazione bilancio",
                                  "rinnovo direttivo", "verbale assemblea", "deposito RUNTS"])]},
        {"name": "Bilancio sociale 2025", "who": "lead", "stage": "In corso", "deadline": 30,
         "description": "Non siamo obbligate ma lo chiede la Fondazione e serve per l'8x1000.",
         "notes": [("lead", 21, "bozza al 60%. mancano i numeri delle attività scuole e la parte volontariato"),
                   ("comms", 9, "grafica: uso il modello dell'anno scorso, cambio solo i colori"),
                   ("lead", 9, "Sintomo: la Fondazione chiede il bilancio sociale e serve anche per l'8x1000, anche "
                               "se l'associazione non è obbligata. Causa / contesto: bilancio sociale volontario "
                               "(obbligatorio solo sopra 1 milione di entrate); documento di rendicontazione delle "
                               "attività. Intervento e stato: bozza al 60%; mancano i numeri delle attività nelle "
                               "scuole e la parte sul volontariato; grafica sul modello dell'anno scorso con colori "
                               "nuovi. In corso.",
                               ["bilancio sociale", "rendicontazione sociale", "report attività", "Fondazione",
                                "8x1000", "documento volontario", "grafica"])]},
        {"name": "Rinnovo firma digitale Anna", "who": "treasurer", "stage": "Fatto",
         "description": "scaduta!!",
         "notes": [("treasurer", 30, "scaduta a settembre, nessuno se n'era accorto. appuntamento in CCIAA"),
                   ("treasurer", 24, "rinnovata. scade ottobre 2029, messo promemoria"),
                   ("treasurer", 11, "beffa: Anna lascia la presidenza, la firma rinnovata per le cariche sul "
                                     "registro non ci serve più e Lucia la firma digitale non ce l'ha. vedi "
                                     "RUNTS/cambio presidente"),
                   ("treasurer", 11, "Sintomo: la firma digitale della presidente era scaduta a settembre senza che "
                                     "nessuno se ne accorgesse. Causa / contesto: dispositivo di firma digitale del "
                                     "legale rappresentante, rinnovo su appuntamento in CCIAA (Camera di commercio). "
                                     "Intervento e stato: rinnovata, scade a ottobre 2029, promemoria impostato. Poi "
                                     "la presidente ha lasciato la carica e la nuova non ha la firma digitale: vedi "
                                     "la variazione cariche sul RUNTS. Fatto.",
                                     ["firma digitale", "rinnovo firma", "firma scaduta", "CCIAA",
                                      "Camera di commercio", "legale rappresentante", "promemoria scadenza"])]},
        {"name": "Rinnovo assicurazione volontari", "who": "treasurer", "stage": "Da fare", "deadline": 91,
         "description": "scade 31/1. aggiornare elenco nominativi",
         "notes": [("treasurer", 0, "Sintomo: la polizza delle volontarie scade il 31 gennaio e va rinnovata. Causa / "
                                    "contesto: assicurazione infortuni e RC (responsabilità civile) dei volontari "
                                    "obbligatoria per gli ETS; l'elenco dei nominativi va aggiornato, incluse le "
                                    "nuove volontarie del corso. Una volontaria nuova è coperta solo dal giorno dopo "
                                    "la comunicazione del nominativo: prima niente turni. Intervento e stato: da fare "
                                    "entro il 31/1.",
                                    ["assicurazione volontari", "rinnovo polizza", "polizza infortuni",
                                     "RC responsabilità civile", "elenco nominativi", "scadenza 31 gennaio"])]},
        {"name": "Registro trattamenti privacy", "who": "lead", "stage": "In corso",
         "description": "rifare il registro dei trattamenti, sportello e casa separati. chiesto aiuto a un "
                        "avvocato socio",
         "notes": [("lead", 45, "l'avvocato ci risponde dopo metà novembre"),
                   ("lead", 45, "Sintomo: il registro dei trattamenti dei dati è da rifare, separando lo sportello e "
                                "la casa. Causa / contesto: registro delle attività di trattamento previsto dal GDPR "
                                "(Regolamento generale sulla protezione dei dati); dati particolarmente delicati "
                                "delle donne seguite. Le schede delle donne stanno solo nell'archivio cartaceo "
                                "chiuso. Intervento e stato: chiesto aiuto a un avvocato socio, che risponderà dopo "
                                "metà novembre. In corso.",
                                ["registro dei trattamenti", "privacy", "GDPR",
                                 "Regolamento generale protezione dati", "protezione dati personali",
                                 "trattamento dati", "avvocato"])]},
        {"name": "Sito: pagina sostienici", "who": "comms", "stage": "Da fare",
         "description": "IBAN, 5x1000, donazioni in natura (cosa sì cosa no)",
         "notes": [("comms", 0, "Sintomo: sul sito manca una pagina che spieghi come sostenere l'associazione. Causa "
                                "/ contesto: pagina «sostienici» con IBAN per le donazioni, codice per il 5x1000 e "
                                "indicazioni sulle donazioni in natura (cosa si accetta e cosa no). Le donazioni in "
                                "natura si accettano solo nuove o in ottimo stato: niente materassi e cuscini usati, "
                                "vestiti non lavati, alimenti aperti o scaduti. Intervento e stato: da fare.",
                                ["pagina sostienici", "donazioni", "come donare", "IBAN", "5x1000",
                                 "donazioni in natura", "sito web"])]},
        {"name": "Rendiconto 5x1000", "who": "treasurer", "stage": "Da fare", "deadline": 60,
         "description": "contributo incassato a ottobre, rendiconto entro un anno ma meglio subito",
         "notes": [("treasurer", 0, "Sintomo: il contributo del cinque per mille è stato incassato a ottobre e va "
                                    "rendicontato. Causa / contesto: rendiconto obbligatorio dell'utilizzo del 5x1000 "
                                    "entro un anno dall'incasso. Il contributo è arrivato sul conto vecchio dopo il "
                                    "cambio di banca, e l'IBAN del 5x1000 è da aggiornare sul portale; il 5x1000 "
                                    "compare anche nella pagina dei contributi pubblici. Intervento e stato: da fare; "
                                    "meglio prepararlo subito invece di aspettare la scadenza.",
                                    ["rendiconto 5x1000", "cinque per mille", "rendicontazione",
                                     "utilizzo contributo", "entro un anno", "incasso ottobre"])]},
    ],
    "projects": [
        {"name": P_CAMPAGNA, "tags": ["comunicazione", "campagna"],
         "description": "<p>Campagna annuale intorno al 25 novembre: social, evento in piazza, premio delle "
                        "scuole, video.</p>",
         "milestones": [("Piano editoriale", -40, 38), ("Evento 25 novembre", 24, None),
                        ("Premio: proclamazione", 40, None)],
         "tasks": [
             {"name": "Piano editoriale ott-dic", "who": "comms", "stage": "Fatto", "milestone": "Piano editoriale",
              "description": "3 post a settimana, 1 reel. temi: consenso, linguaggio, numeri regionali",
              "notes": [("comms", 40, "piano fatto, approvato da Marta. foglio nel drive comunicazione"),
                        ("comms", 40, "Sintomo: la comunicazione voleva sapere cosa pubblicare sui social da ottobre "
                                      "a dicembre per la campagna «Ci riguarda», senza improvvisare un post alla "
                                      "volta. Causa / contesto: piano editoriale della campagna 2026 intorno al 25 "
                                      "novembre; ritmo di tre post a settimana più un reel; temi: consenso, "
                                      "linguaggio, numeri regionali sulla violenza. Intervento e stato: piano "
                                      "preparato e approvato dal direttivo; il foglio con il calendario dei post è "
                                      "nel drive della comunicazione. Fatto.",
                                      ["piano editoriale", "calendario post", "social media", "Instagram reel",
                                       "campagna Ci riguarda", "consenso", "linguaggio",
                                       "programmazione contenuti"])]},
             {"name": "Post furgone donazioni - rimosso", "who": "comms", "stage": "Fatto",
              "description": "post del ringraziamento per i mobili donati. tolto.",
              "notes": [("comms", 52, "post tolto dopo 40 minuti: nella foto del carico dei mobili si vedeva la "
                                      "facciata e il portone della casa. La foto me l'aveva mandata una "
                                      "volontaria, non l'ho guardata bene. 3 condivisioni, ho scritto a tutte e "
                                      "tre per toglierla, fatto."),
                        ("lead", 51, "parlato in direttivo. nessun danno visibile per ora ma da adesso ogni foto "
                                     "passa da Giulia e niente foto alla casa, mai. regola scritta."),
                        ("comms", 50, "ripubblicato il ringraziamento con la foto del divano in magazzino"),
                        ("comms", 50, "Sintomo: un post di ringraziamento per i mobili donati mostrava, nella foto "
                                      "del carico mandata da una volontaria, la facciata e il portone della casa "
                                      "rifugio; condiviso tre volte. Causa / contesto: foto pubblicata senza "
                                      "controllo; violazione della riservatezza del luogo protetto (indirizzo e "
                                      "immagini della casa mai pubblici). Intervento e stato: post tolto dopo 40 "
                                      "minuti, chieste e ottenute le rimozioni delle tre condivisioni, discusso in "
                                      "direttivo; nuova regola scritta: ogni foto passa dalla responsabile "
                                      "comunicazione, mai foto della casa. Ringraziamento ripubblicato con la foto "
                                      "del divano in magazzino. Fatto.",
                                      ["foto casa rifugio", "post rimosso", "luogo protetto",
                                       "facciata riconoscibile", "riservatezza", "controllo foto social",
                                       "condivisioni cancellate", "donazione mobili"])]},
             {"name": "Evento in piazza 25/11", "who": "comms", "stage": "In corso", "milestone": "Evento 25 novembre",
              "deadline": 24, "description": "permesso suolo pubblico, gazebo, panchina rossa, musica",
              "notes": [("comms", 20, "domanda suolo pubblico fatta al Comune, ci serve entro il 15"),
                        ("volunteer", 6, "gazebo lo prestano gli scout, ritiro venerdì 21"),
                        ("comms", 2, "chiedere a Lucia se fa lei il banchetto materiali"),
                        ("comms", 2, "Sintomo: per la Giornata contro la violenza sulle donne serve organizzare "
                                     "l'evento in piazza: gazebo, panchina rossa, musica, banchetto materiali. Causa "
                                     "/ contesto: occupazione di suolo pubblico da chiedere al Comune (autorizzazione "
                                     "necessaria entro il 15); gazebo in prestito dagli scout, ritiro venerdì 21; "
                                     "banchetto materiali da affidare a una socia. Intervento e stato: domanda di "
                                     "suolo pubblico presentata al Comune, gazebo concordato; in corso.",
                                     ["25 novembre", "Giornata internazionale contro la violenza sulle donne",
                                      "evento in piazza", "permesso suolo pubblico", "occupazione suolo pubblico",
                                      "gazebo", "panchina rossa", "banchetto"])]},
             {"name": "Premio racconti scuole superiori", "who": "lead", "stage": "In corso",
              "milestone": "Premio: proclamazione", "deadline": 40,
              "description": "seconda edizione. racconti brevi sul tema del rispetto. giuria 3 persone",
              "notes": [("lead", 33, "bando mandato alle 5 superiori. scadenza racconti 30 novembre"),
                        ("lead", 8, "arrivati 11 racconti finora, 2 dallo stesso istituto"),
                        ("lead", 8, "Sintomo: seconda edizione del concorso di racconti brevi per gli studenti delle "
                                    "superiori sul tema del rispetto, con una giuria di tre persone. Causa / "
                                    "contesto: attività di prevenzione nelle scuole collegata alla campagna «Ci "
                                    "riguarda»; bando inviato alle cinque scuole superiori, scadenza per i racconti "
                                    "il 30 novembre. Intervento e stato: arrivati finora 11 racconti, due dallo "
                                    "stesso istituto; raccolta in corso fino alla scadenza.",
                                    ["premio racconti", "concorso letterario", "scuole superiori", "studenti",
                                     "rispetto", "bando concorso", "giuria", "prevenzione scuole"])]},
             {"name": "Video campagna", "who": "comms", "stage": "In attesa",
              "description": "30 secondi, voci delle volontarie (non volti). aspetta il preventivo del video maker",
              "notes": [("comms", 0, "Sintomo: la campagna vuole un video breve con le voci delle volontarie, senza "
                                     "mostrare i volti. Causa / contesto: spot di 30 secondi per «Ci riguarda» 2026; "
                                     "tutela dell'anonimato delle volontarie (voci, non volti); produzione affidata a "
                                     "un video maker esterno. Coerente con il piano editoriale: reel con voci e non "
                                     "volti, niente persone riconoscibili senza liberatoria. Intervento e stato: in "
                                     "attesa del preventivo del video maker prima di decidere; nessun altro passo "
                                     "registrato.",
                                     ["video campagna", "spot 30 secondi", "videomaker", "preventivo video",
                                      "voci senza volti", "anonimato volontarie", "Ci riguarda"])]},
             {"name": "Volantini e manifesti", "who": "comms", "stage": "Da fare", "deadline": 12,
              "description": "200 manifesti A3, 1000 volantini. logo Comune patrocinio",
              "notes": [("comms", 0, "Sintomo: servono i materiali stampati della campagna da distribuire e "
                                     "affiggere. Causa / contesto: stampa di 200 manifesti formato A3 e 1000 "
                                     "volantini per «Ci riguarda» 2026; obbligo di inserire il logo del Comune per il "
                                     "patrocinio concesso. Materiali della campagna e dell'evento patrocinati dal "
                                     "Comune; le bozze seguono il percorso dei comunicati (bozza della comunicazione, "
                                     "lettura della coordinatrice). Intervento e stato: da fare; quantità e formato "
                                     "definiti, stampa non ancora ordinata.",
                                     ["volantini", "manifesti A3", "flyer", "stampa materiali", "tipografia",
                                      "logo patrocinio Comune", "affissione"])]},
             {"name": "Patrocinio Comune", "who": "lead", "stage": "Fatto",
              "description": "richiesta patrocinio gratuito per evento e campagna",
              "notes": [("lead", 25, "arrivato il patrocinio, logo da mettere su tutto"),
                        ("lead", 25, "Sintomo: l'associazione voleva il sostegno ufficiale del Comune per l'evento "
                                     "del 25 novembre e per la campagna. Causa / contesto: richiesta di patrocinio "
                                     "gratuito (non oneroso) al Comune; il patrocinio obbliga a riportare il logo del "
                                     "Comune sui materiali. Collegato ai volantini e ai manifesti, che devono "
                                     "riportare il logo. Intervento e stato: patrocinio concesso; il logo va messo su "
                                     "tutti i materiali della campagna (manifesti, volantini, post). Fatto.",
                                     ["patrocinio gratuito", "patrocinio non oneroso", "Comune", "logo Comune",
                                      "concessione patrocinio", "evento 25 novembre", "campagna"])]},
             {"name": "Reel numeri violenza Umbria", "who": "comms", "stage": "Da fare",
              "description": "dati pubblici ISTAT/regione, citare la fonte",
              "notes": [("comms", 0, "Sintomo: la comunicazione vuole un reel con i numeri della violenza sulle donne "
                                     "in Umbria per la campagna. Causa / contesto: contenuto social basato su dati "
                                     "pubblici ISTAT e della Regione; obbligo di citare sempre la fonte, come "
                                     "previsto dal piano editoriale (lunedì: numeri e fonti). Il piano editoriale "
                                     "prevede un reel ogni due settimane, con voci e non volti. Intervento e stato: "
                                     "da fare; nessun dato ancora raccolto.",
                                     ["reel", "statistiche violenza", "dati ISTAT",
                                      "Istituto nazionale di statistica", "numeri regionali Umbria",
                                      "citare la fonte", "video social"])]},
         ],
         "updates": [
             ("Ottobre", "on_track", 35, 30, "piano editoriale partito. post furgone tolto (vedi task), nuova "
                                             "regola sulle foto. evento: manca il suolo pubblico."),
             ("Verso il 25", "at_risk", 50, 3, "suolo pubblico non ancora arrivato, video fermo sul preventivo. "
                                               "premio ok, racconti in arrivo."),
         ]},
        {"name": P_CASA, "tags": ["casa", "struttura"], "stages": HOUSE_STAGES,
         "description": "<p>Guasti, manutenzioni, scorte, inventario, donazioni della casa e del magazzino di "
                        "sopra.</p>",
         "milestones": [("Inventario annuale", -20, 18), ("Revisione estintori", 45, None)],
         "tasks": [
             {"name": "Caldaia in blocco (E10)", "who": "member", "stage": "Risolto",
              "description": "la caldaia è andata in blocco giovedì sera",
              "notes": [("member", 12, "giovedì sera blocco E10, reset fatto una volta, riblocca. pressione 0,6. "
                                       "messe le stufette, chiamata la ditta"),
                        ("lead", 11, "venuto il tecnico venerdì: sonda NTC + pressione. 180 euro, fattura alla "
                                     "tesoriera. da fare pulizia scambiatore in primavera"),
                        ("treasurer", 9, "pagata con bonifico. NON è spesa di progetto, va su bilancio ordinario"),
                        ("member", 9, "Sintomo: giovedì sera la caldaia della casa è andata in blocco, niente "
                                      "riscaldamento; dopo un reset si è ribloccata, pressione a 0,6. Causa / "
                                      "contesto: codice errore E10, pressione impianto bassa e sonda NTC guasta. "
                                      "Intervento e stato: messe le stufette, chiamata la ditta di manutenzione; il "
                                      "tecnico venerdì ha sostituito la sonda NTC e ripristinato la pressione, 180 "
                                      "euro, fattura alla tesoriera pagata con bonifico su bilancio ordinario (non "
                                      "spesa di progetto). Da fare in primavera la pulizia dello scambiatore. "
                                      "Risolto.",
                                      ["caldaia in blocco", "errore E10", "riscaldamento", "pressione bassa",
                                       "sonda NTC", "stufette", "tecnico caldaia", "scambiatore"])],
              "attachment": "stage_report"},
             {"name": "Lavatrice perde acqua", "who": "volunteer", "stage": "In attesa ditta",
              "description": "perde dallo sportello sotto",
              "notes": [("volunteer", 5, "messa la bacinella. guarnizione? il tecnico viene martedì forse"),
                        ("volunteer", 5, "Sintomo: la lavatrice della casa perde acqua dallo sportello in basso. "
                                         "Causa / contesto: probabile guarnizione dell'oblò usurata (da confermare); "
                                         "serve l'intervento di un tecnico. Guasto del progetto Casa. Il tecnico si "
                                         "accompagna di persona e per le ditte si usa l'indirizzo dello sportello, "
                                         "mai quello della casa. Intervento e stato: messa una bacinella sotto; in "
                                         "attesa della ditta, il tecnico dovrebbe venire martedì.",
                                         ["lavatrice", "perdita acqua", "guarnizione oblò", "sportello lavatrice",
                                          "elettrodomestico guasto", "tecnico lavatrice", "bacinella"])]},
             {"name": "Infiltrazione stanza blu", "who": "lead", "stage": "In carico",
              "description": "macchia sul soffitto della stanza blu (sportello), dal piano di sopra",
              "notes": [("lead", 16, "scritto all'amministratore di condominio"),
                        ("lead", 4, "sopralluogo fatto, è il terrazzo. lavori a carico del condominio, tempi lunghi"),
                        ("lead", 4, "Sintomo: è comparsa una macchia sul soffitto della stanza blu dello sportello, "
                                    "dal piano di sopra. Causa / contesto: infiltrazione d'acqua dal terrazzo "
                                    "condominiale; competenza dell'amministratore di condominio, lavori a carico del "
                                    "condominio. La stanza blu è un locale dello sportello, non della casa. "
                                    "Intervento e stato: scritto all'amministratore, sopralluogo fatto e causa "
                                    "individuata nel terrazzo; i lavori spettano al condominio, tempi lunghi. In "
                                    "carico.",
                                    ["infiltrazione", "macchia soffitto", "umidità", "stanza blu",
                                     "terrazzo condominiale", "amministratore di condominio", "sopralluogo"])]},
             {"name": "Inventario materiale 2026", "who": "volunteer", "stage": "Risolto",
              "milestone": "Inventario annuale",
              "description": "contare tutto il magazzino di sopra + casa. foglio inventario",
              "notes": [("volunteer", 20, "fatto sabato con Lucia e Bea. file aggiornato in drive (riservato)"),
                        ("lead", 18, "ok. mancano lenzuola singole e asciugamani grandi"),
                        ("volunteer", 18, "Sintomo: bisognava sapere cosa c'è davvero nel magazzino di sopra e nella "
                                          "casa, per capire cosa manca. Causa / contesto: inventario annuale 2026 sul "
                                          "foglio inventario (file riservato nel drive). Il foglio è riservato: in "
                                          "memoria è tenuto senza testo (elenco del materiale per stanza). Intervento "
                                          "e stato: conteggio fatto un sabato da tre volontarie, file aggiornato. "
                                          "Mancano lenzuola singole e asciugamani grandi (aperto task dedicato). "
                                          "Risolto.",
                                          ["inventario", "conta magazzino", "magazzino di sopra", "foglio inventario",
                                           "scorte", "lenzuola", "asciugamani", "materiale casa"])],
              "worklog": [("volunteer", 20, 4.0, "inventario magazzino di sopra")]},
             {"name": "Scorte igiene e pulizia", "who": "volunteer", "stage": "In carico",
              "description": "detersivi, kit igiene, pannolini taglia 4-5",
              "notes": [("volunteer", 7, "ordinato su amazon con la prepagata. pannolini li porta la farmacia"),
                        ("volunteer", 7, "Sintomo: alla casa servono detersivi, kit igiene e pannolini taglia 4-5. "
                                         "Causa / contesto: riordino delle scorte minime (kit igiene, detersivi per "
                                         "un mese, pannolini); acquisti online con la carta prepagata "
                                         "dell'associazione. Scorte minime previste: almeno 2 kit igiene completi, 4 "
                                         "set lenzuola, detersivi per un mese e una scorta di pannolini 4-5. "
                                         "Intervento e stato: ordinato online con la prepagata; i pannolini li porta "
                                         "la farmacia. In carico.",
                                         ["scorte", "kit igiene", "detersivi", "prodotti pulizia",
                                          "pannolini taglia 4-5", "carta prepagata", "acquisto online",
                                          "farmacia"])]},
             {"name": "Lenzuola e asciugamani", "who": "volunteer", "stage": "Segnalato",
              "description": "dall'inventario: mancano lenzuola singole e asciugamani grandi. chiedere donazioni?",
              "notes": [("volunteer", 0, "Sintomo: dall'inventario risulta che mancano lenzuola singole e asciugamani "
                                         "grandi per la casa. Causa / contesto: sotto la scorta minima di biancheria "
                                         "(almeno 4 set lenzuola); ipotesi di chiedere donazioni in natura, che si "
                                         "accettano solo nuove o in ottimo stato. Le donazioni si etichettano con la "
                                         "data e vanno nel magazzino di sopra. Intervento e stato: segnalato; da "
                                         "decidere se acquistare o lanciare una richiesta di donazioni.",
                                         ["lenzuola singole", "asciugamani", "biancheria", "scorta minima",
                                          "richiesta donazioni", "donazioni in natura", "inventario"])]},
             {"name": "Serratura magazzino di sopra", "who": "lead", "stage": "Risolto",
              "description": "il mazzo di Bea non si trova",
              "notes": [("lead", 22, "non si trova da settimane. cambiamo la serratura"),
                        ("lead", 18, "cambiata il 14. tre chiavi: io, Paola, cassetta sportello"),
                        ("lead", 18, "Sintomo: un mazzo di chiavi del magazzino di sopra non si trovava più da "
                                     "settimane. Causa / contesto: chiavi smarrite, rischio di accesso non "
                                     "controllato al magazzino; si decide di sostituire la serratura. Intervento e "
                                     "stato: serratura cambiata il 14; le chiavi nuove sono tre: due a persone del "
                                     "direttivo e una nella cassetta a codice dello sportello; le vecchie non aprono "
                                     "più. Risolto.",
                                     ["serratura", "cambio serratura", "chiavi smarrite", "mazzo perso",
                                      "magazzino di sopra", "cassetta a codice", "copie chiavi"])]},
             {"name": "Divano e due letti donati", "who": "treasurer", "stage": "Risolto",
              "description": "donazione privata, ritiro col furgone",
              "notes": [("treasurer", 53, "ritirati sabato, registrati nel foglio donazioni. ricevuta fatta, "
                                          "valore dichiarato dal donatore"),
                        ("treasurer", 53, "Sintomo: un privato ha offerto un divano e due letti per la casa. Causa / "
                                          "contesto: donazione in natura; ritiro con il furgone; registrazione nel "
                                          "foglio donazioni e ricevuta con valore dichiarato dal donatore (non "
                                          "stimato dall'associazione). Le donazioni si etichettano con la data e "
                                          "vanno nel magazzino di sopra; il furgone non si fotografa davanti alla "
                                          "casa. Intervento e stato: mobili ritirati il sabato, registrati nel foglio "
                                          "donazioni, ricevuta fatta. Risolto.",
                                          ["donazione in natura", "mobili donati", "divano", "letti",
                                           "ritiro furgone", "foglio donazioni", "ricevuta donazione",
                                           "valore dichiarato"])]},
             {"name": "Revisione estintori", "who": "lead", "stage": "Segnalato", "milestone": "Revisione estintori",
              "deadline": 45, "description": "semestrale. ditta solita",
              "notes": [("lead", 0, "Sintomo: è in scadenza il controllo periodico degli estintori. Causa / contesto: "
                                    "revisione semestrale obbligatoria dei presidi antincendio, affidata alla ditta "
                                    "di sempre. Il task è nel progetto Casa: per le ditte si usa l'indirizzo dello "
                                    "sportello e il tecnico si accompagna di persona, senza dare l'indirizzo per "
                                    "telefono. Nessuna data di scadenza registrata. Intervento e stato: segnalato; da "
                                    "prenotare con la ditta abituale.",
                                    ["estintori", "revisione semestrale", "antincendio", "controllo periodico",
                                     "sicurezza", "manutenzione estintori"])]},
             {"name": "Wifi sportello lento", "who": "member", "stage": "Segnalato",
              "description": "router vecchio? il pc delle schede non si collega",
              "notes": [("member", 0, "Sintomo: allo sportello internet va lento, il wifi cade e il pc delle schede "
                                      "non riesce a collegarsi alla rete, rallentando il lavoro del turno. Causa / "
                                      "contesto: connessione wifi della sede dello sportello; il sospetto è un router "
                                      "vecchio, da verificare ed eventualmente sostituire; nessuna diagnosi tecnica "
                                      "ancora fatta. Intervento e stato: segnalato nel progetto Casa; nessuna "
                                      "verifica né acquisto registrati finora.",
                                      ["wifi lento", "connessione internet", "router vecchio", "rete sportello",
                                       "pc non si collega", "computer schede", "linea internet"])]},
         ],
         "updates": [
             ("Ottobre", "on_track", 0, 10, "caldaia sistemata, serratura magazzino cambiata, inventario fatto. "
                                            "aperti: lavatrice, infiltrazione stanza blu (condominio)."),
         ]},
        {"name": P_VOLONTARIATO, "tags": ["volontariato", "formazione"],
         "description": "<p>Ingressi, corso base, turni, supervisione.</p>",
         "milestones": [("Corso base autunno", 20, None), ("Nuove volontarie in turno", 75, None)],
         "tasks": [
             {"name": "Corso base autunno 2026", "who": "lead", "stage": "In corso", "milestone": "Corso base autunno",
              "deadline": 20, "description": "40 ore, martedì e giovedì sera, 8 iscritte",
              "notes": [("lead", 35, "8 iscritte dopo i colloqui, 2 rinviate a primavera"),
                        ("lead", 14, "lezione sul quadro normativo fatta dall'avvocata. presenze ok"),
                        ("member", 3, "giovedì tocca a me: accoglienza telefonica, simulazioni"),
                        ("lead", 3, "Sintomo: le nuove aspiranti volontarie devono fare la formazione obbligatoria "
                                    "prima dei turni. Causa / contesto: corso base di 40 ore, martedì e giovedì sera, "
                                    "previsto dal regolamento delle volontarie; 8 iscritte dopo i colloqui, 2 "
                                    "rinviate a primavera. Dopo il corso: tre turni in affiancamento. Intervento e "
                                    "stato: lezione sul quadro normativo tenuta dall'avvocata, presenze regolari; "
                                    "prossima lezione su accoglienza telefonica con simulazioni. In corso.",
                                    ["corso base", "formazione volontarie", "40 ore", "corso autunno",
                                     "accoglienza telefonica", "simulazioni", "quadro normativo",
                                     "nuove volontarie"])],
              "worklog": [("member", 14, 2.0, "lezione corso base")]},
             {"name": "Colloqui nuove candidate", "who": "lead", "stage": "Fatto",
              "description": "dopo l'open day di settembre",
              "notes": [("lead", 38, "11 colloqui, 8 al corso. 1 la indirizziamo ad altro (cerca lavoro, non "
                                     "volontariato)"),
                        ("lead", 38, "Sintomo: dopo l'open day di settembre diverse persone hanno chiesto di "
                                     "diventare volontarie. Causa / contesto: colloquio di ingresso, primo passo "
                                     "della procedura per le nuove volontarie (prima del corso base). Seguono "
                                     "registro volontari, assicurazione, patto di riservatezza, corso base di 40 ore "
                                     "e tre turni in affiancamento. Intervento e stato: fatti 11 colloqui; 8 ammesse "
                                     "al corso, una indirizzata altrove perché cercava lavoro e non volontariato. "
                                     "Fatto.",
                                     ["colloqui", "candidate volontarie", "selezione", "open day",
                                      "ingresso volontarie", "reclutamento", "corso base"])]},
             {"name": "Turni sportello novembre-dicembre", "who": "volunteer", "stage": "In corso",
              "description": "griglia turni. sabato scoperto due volte",
              "notes": [("volunteer", 4, "sabato 15 e 29 scoperti. chiesto nel gruppo"),
                        ("volunteer", 1, "il 15 lo prende Franca anche se è uscita dal direttivo, il 29 ancora no"),
                        ("volunteer", 1, "Sintomo: nella griglia dei turni dello sportello di novembre-dicembre due "
                                         "sabati restano scoperti. Causa / contesto: turnazione delle volontarie; "
                                         "sabato 15 e 29 senza copertura; lo sportello non può restare con una sola "
                                         "persona. Se il cambio non si trova, lo sportello si chiude e si mette il "
                                         "cartello. Intervento e stato: chiesto nel gruppo turni; il 15 è coperto da "
                                         "una ex componente del direttivo, il 29 ancora scoperto. In corso.",
                                         ["turni sportello", "griglia turni", "turnazione", "sabato scoperto",
                                          "copertura turni", "gruppo turni", "calendario volontarie"])]},
             {"name": "Supervisione mensile", "who": "lead", "stage": "In corso",
              "description": "con la psicologa esterna, primo lunedì del mese. pagata dal progetto regionale",
              "notes": [("treasurer", 15, "la fattura della supervisione deve avere il CUP del progetto Fili!"),
                        ("lead", 15, "Sintomo: le volontarie e le operatrici fanno la supervisione con la psicologa "
                                     "esterna il primo lunedì del mese. Causa / contesto: supervisione obbligatoria "
                                     "per chi fa turni, pagata dal progetto regionale «Fili»; la fattura della "
                                     "psicologa deve riportare il CUP (Codice unico di progetto) per essere "
                                     "rendicontabile. Intervento e stato: in corso; da ricordare il CUP su ogni "
                                     "fattura della supervisione.",
                                     ["supervisione", "psicologa esterna", "supervisione mensile", "CUP",
                                      "Codice unico di progetto", "fattura", "progetto Fili", "rendicontazione"])]},
             {"name": "Patto di riservatezza nuove", "who": "lead", "stage": "Da fare", "deadline": 21,
              "description": "farlo firmare a tutte le 8 prima dell'affiancamento",
              "notes": [("lead", 0, "Sintomo: le 8 nuove volontarie devono firmare l'impegno alla riservatezza prima "
                                    "di iniziare i turni in affiancamento. Causa / contesto: patto di riservatezza "
                                    "previsto dalla procedura di ingresso e dal regolamento interno (vale anche dopo "
                                    "l'uscita dall'associazione). Fa parte della procedura nuova volontaria insieme a "
                                    "registro volontari e comunicazione all'assicurazione, prima dei tre turni in "
                                    "affiancamento. Intervento e stato: da fare; firma da raccogliere da tutte prima "
                                    "dell'affiancamento.",
                                    ["patto di riservatezza", "accordo di confidenzialità", "segreto",
                                     "nuove volontarie", "affiancamento", "privacy", "firma impegno"])]},
             {"name": "Registro volontari e assicurazione nuove", "who": "treasurer", "stage": "Da fare",
              "deadline": 25, "description": "comunicare i nominativi prima dei turni in affiancamento",
              "notes": [("treasurer", 0, "Sintomo: le nuove volontarie stanno per iniziare i turni in affiancamento e "
                                         "devono essere coperte. Causa / contesto: iscrizione nel registro dei "
                                         "volontari e comunicazione dei nominativi all'assicurazione (polizza "
                                         "infortuni e RC); la copertura parte solo dal giorno dopo la comunicazione. "
                                         "Lezione già scritta: comunicare i nominativi alla fine del corso, insieme "
                                         "al patto di riservatezza. Intervento e stato: da fare prima dei turni in "
                                         "affiancamento.",
                                         ["registro volontari", "assicurazione volontarie", "polizza infortuni",
                                          "responsabilità civile RC", "comunicazione nominativi",
                                          "copertura assicurativa", "affiancamento"])]},
             {"name": "Cena di fine anno", "who": "volunteer", "stage": "Da fare",
              "description": "metà dicembre, da Rita come l'anno scorso?",
              "notes": [("volunteer", 0, "Sintomo: volontarie e soci vogliono ritrovarsi per la cena di fine anno a "
                                         "metà dicembre, come l'anno scorso. Causa / contesto: cena sociale natalizia "
                                         "del gruppo volontariato 2026-2027; proposta di tornare nello stesso "
                                         "ristorante dell'anno precedente, da confermare; da raccogliere le adesioni "
                                         "e prenotare. Nessun costo o numero di partecipanti registrato. Intervento e "
                                         "stato: da fare; data e locale non ancora fissati.",
                                         ["cena di fine anno", "cena sociale", "cena di Natale", "festa dicembre",
                                          "ristorante", "prenotazione"])]},
         ],
         "updates": [
             ("Autunno", "on_track", 40, 6, "corso base a metà, 8 iscritte. turni di sabato scoperti. "
                                            "da fare patto e assicurazione prima dell'affiancamento."),
         ]},
        {"name": P_RUNTS, "tags": ["RUNTS", "adempimenti"],
         "description": "<p>Tutto quello che va fatto sul registro: bilancio, cariche, dati soci, pec, 5x1000, "
                        "pagina contributi.</p>",
         "milestones": [("Bilancio 2025 caricato", -124, 117), ("Cariche aggiornate sul registro", 18, None),
                        ("Bilancio 2026 sul registro", 241, None)],
         "tasks": [
             {"name": "Caricare il bilancio 2025", "who": "treasurer", "stage": "Fatto",
              "milestone": "Bilancio 2025 caricato", "description": "entro 30/6. lo carica la commercialista",
              "notes": [("treasurer", 128, "pratica respinta dal portale: errore sul file, il rendiconto della "
                                           "cena di primavera era allegato a parte e non dentro il PDF del "
                                           "bilancino. rifacciamo"),
                        ("treasurer", 122, "rimandato il 2/7 ma la notifica è andata sulla pec della "
                                           "commercialista che era in ferie, nessuno l'ha vista. mancava la "
                                           "quadratura cassa e banca"),
                        ("treasurer", 117, "caricato e accettato il 7 luglio. una settimana di ritardo. speriamo "
                                           "bene"),
                        ("treasurer", 117, "Sintomo: il bilancio 2025 doveva essere caricato sul registro entro il 30 "
                                           "giugno; la pratica è stata respinta e caricata in ritardo. Causa / "
                                           "contesto: deposito bilancio sul portale RUNTS (Registro unico nazionale "
                                           "del Terzo settore): rendiconto della raccolta fondi della cena di "
                                           "primavera allegato a parte invece che nello stesso PDF del bilancino; "
                                           "mancava la quadratura cassa e banca; notifica arrivata sulla PEC della "
                                           "commercialista in ferie. Intervento e stato: rifatto, caricato e "
                                           "accettato il 7 luglio, una settimana oltre la scadenza. Fatto.",
                                           ["deposito bilancio", "RUNTS", "Registro unico nazionale Terzo settore",
                                            "pratica respinta", "rendiconto raccolta fondi",
                                            "quadratura cassa e banca", "bilancino PDF", "ritardo deposito"])]},
             {"name": "La pec dell'associazione sul registro", "who": "treasurer", "stage": "Fatto",
              "description": "sul registro c'è la pec della commercialista. ora ci vuole la nostra (DM 2/2026)",
              "notes": [("treasurer", 109, "attivata la pec dell'associazione, variazione fatta sul portale"),
                        ("lead", 108, "la password ce l'hanno Paola e Marta. NON nel gruppo whatsapp"),
                        ("treasurer", 108, "Sintomo: sul registro risultava la PEC della commercialista invece di "
                                           "quella dell'associazione, e le notifiche finivano a lei. Causa / "
                                           "contesto: il DM 2/2026 (modifica al DM 106/2020) rende obbligatoria la "
                                           "PEC propria dell'ente sul RUNTS; variazione da fare entro 30 giorni. "
                                           "Intervento e stato: attivata la PEC dell'associazione e fatta la "
                                           "variazione sul portale; credenziali a due persone del direttivo, mai nel "
                                           "gruppo whatsapp. Fatto.",
                                           ["PEC", "posta elettronica certificata", "PEC dell'ente",
                                            "variazione RUNTS", "DM 2/2026", "notifiche registro",
                                            "credenziali PEC"])]},
             {"name": "Lettera della Regione di settembre", "who": "treasurer", "stage": "Fatto",
              "description": "arrivata una pec dall'ufficio RUNTS regionale. diffida per il ritardo?",
              "notes": [("treasurer", 58, "panico: pec dall'ufficio del registro, pensavo fosse la diffida per "
                                          "il bilancio caricato tardi"),
                        ("treasurer", 57, "no!! era la mail mandata a tutti gli enti con le indicazioni operative "
                                          "(DD 8521). nessuna diffida. salvata in drive"),
                        ("lead", 57, "meno male. leggiamola però, c'è la storia del verbale classificato a parte"),
                        ("treasurer", 57, "Sintomo: è arrivata una PEC dall'ufficio RUNTS regionale e si temeva fosse "
                                          "una diffida per il bilancio caricato in ritardo. Causa / contesto: era la "
                                          "comunicazione inviata a tutti gli enti con le indicazioni operative "
                                          "approvate dalla determina DD 8521/2026 della Regione Umbria; contiene "
                                          "anche la classificazione del verbale come documento separato. Intervento e "
                                          "stato: nessuna diffida; PEC salvata nel drive, da leggere con attenzione. "
                                          "Fatto.",
                                          ["PEC Regione", "diffida", "DD 8521/2026", "indicazioni operative RUNTS",
                                           "ufficio RUNTS regionale", "Regione Umbria", "verbale classificato",
                                           "lettera di settembre"])]},
             {"name": "Cambio presidente: variazione cariche", "who": "treasurer", "stage": "In corso",
              "milestone": "Cariche aggiornate sul registro", "deadline": 18,
              "description": "Lucia presidente dal 20/10. entro 30 gg sul registro",
              "notes": [("lead", 12, "direttivo del 20: Anna lascia, Lucia presidente. verbale firmato"),
                        ("treasurer", 11, "Lucia non ha la firma digitale. o la fa, o mi fa la delega sul portale "
                                          "(compilazione, firma e invio)"),
                        ("treasurer", 8, "al Cesvol mi hanno detto che dal 15 ottobre le pratiche si possono "
                                         "firmare anche con SPID o CIE senza firma digitale. non ho trovato "
                                         "l'atto, chiedo meglio prima di fidarmi"),
                        ("treasurer", 3, "intanto cambiare anche le firme in banca (fuori Anna, dentro Lucia)"),
                        ("treasurer", 3, "Sintomo: con il direttivo del 20 ottobre è cambiata la presidente e il "
                                         "registro va aggiornato entro 30 giorni. Causa / contesto: istanza di "
                                         "variazione delle cariche sociali sul portale RUNTS con verbale; la nuova "
                                         "legale rappresentante non ha la firma digitale: serve rinnovarla o "
                                         "conferire la delega telematica (compilazione, firma e invio, DM 2/2026); "
                                         "voce non verificata su firma con SPID o CIE. Intervento e stato: verbale "
                                         "firmato; delega in preparazione; da cambiare anche le firme in banca. In "
                                         "corso.",
                                         ["cambio presidente", "variazione cariche", "legale rappresentante", "RUNTS",
                                          "firma digitale", "delega telematica", "SPID", "firme in banca"])]},
             {"name": "Delega sul portale a Paola", "who": "treasurer", "stage": "In attesa",
              "description": "delega del legale rappresentante, la conferisce Lucia online",
              "notes": [("treasurer", 6, "per conferirla Lucia deve entrare col suo SPID. appuntamento giovedì"),
                        ("treasurer", 6, "Sintomo: la nuova presidente non ha la firma digitale e le pratiche del "
                                         "registro devono comunque partire. Causa / contesto: delega telematica del "
                                         "legale rappresentante sul portale RUNTS, introdotta dal DM 2/2026 e "
                                         "operativa dal 9 aprile 2026; la conferisce online la presidente entrando "
                                         "con il proprio SPID, a favore di chi segue il registro. Intervento e stato: "
                                         "appuntamento fissato per il giovedì per l'accesso con SPID; in attesa.",
                                         ["delega telematica", "delegato del legale rappresentante", "portale RUNTS",
                                          "SPID", "DM 2/2026", "firma digitale mancante", "conferire delega"])]},
             {"name": "Dati soci e volontari al 31/12", "who": "treasurer", "stage": "Fatto",
              "description": "entro 30/6 se cambiati",
              "notes": [("treasurer", 135, "sul registro c'erano 28 soci, al 31/12 eravamo 31 in regola con la "
                                           "quota. volontari del registro 19. aggiornato"),
                        ("volunteer", 134, "ma quelle che non hanno pagato la quota 2025 contano? -> no, solo in "
                                           "regola"),
                        ("treasurer", 134, "Sintomo: sul registro il numero di soci e volontari non era più quello "
                                           "reale. Causa / contesto: aggiornamento annuale sul RUNTS dei dati di "
                                           "soci, volontari e dipendenti al 31/12, entro il 30 giugno solo se "
                                           "cambiati; contano solo i soci in regola con la quota associativa. "
                                           "Intervento e stato: soci aggiornati da 28 a 31 (in regola con la quota), "
                                           "volontari 19. Chiarito che chi non ha pagato la quota 2025 non va "
                                           "contato. Fatto.",
                                           ["numero soci", "volontari", "aggiornamento annuale RUNTS", "31 dicembre",
                                            "quota associativa", "soci in regola", "scadenza 30 giugno"])]},
             {"name": "Bilancino 2026: Mod. D o Mod. E?", "who": "treasurer", "stage": "In corso",
              "milestone": "Bilancio 2026 sul registro",
              "description": "Giulia dice che da quest'anno basta il modello semplice",
              "notes": [("comms", 20, "ho letto che per il 2026 c'è il modello E più semplice, il bilancino "
                                      "aggregato"),
                        ("treasurer", 18, "solo sotto i 60.000 di entrate. con convenzione + anticipo Fili + "
                                          "8x1000 il 2026 lo superiamo di sicuro. resta il D"),
                        ("treasurer", 16, "la commercialista conferma D, anche per il confronto con l'anno prima"),
                        ("treasurer", 16, "Sintomo: dalla comunicazione arrivava l'idea che da quest'anno basti il "
                                          "bilancino semplificato. Causa / contesto: Modello E, rendiconto per cassa "
                                          "aggregato (DM 18 febbraio 2026, circolare 6/2026), utilizzabile solo da "
                                          "chi ha entrate sotto i 60.000 euro, dal rendiconto 2026; con convenzione, "
                                          "anticipo «Fili» e 8x1000 il 2026 supera la soglia. Intervento e stato: "
                                          "resta il Modello D, rendiconto per cassa integrale; la commercialista "
                                          "conferma, anche per il confronto con l'anno precedente. In corso.",
                                          ["bilancino", "Modello D", "Modello E", "rendiconto per cassa",
                                           "rendiconto aggregato", "soglia 60.000 euro", "circolare 6/2026",
                                           "schema di bilancio"])]},
             {"name": "Pagina contributi pubblici sul sito", "who": "comms", "stage": "Fatto",
              "description": "entro 30/6, contributi pubblici 2025",
              "notes": [("comms", 126, "pubblicata il 28/6 nella pagina trasparenza: Comune, 5x1000, quota "
                                       "Passi"),
                        ("treasurer", 125, "dubbio: i soldi di Passi li riceviamo dalla capofila, vanno lo "
                                           "stesso? li abbiamo messi, meglio abbondare"),
                        ("lead", 40, "per il 2026 ci va anche Fili. promemoria a giugno"),
                        ("comms", 40, "Sintomo: entro il 30 giugno sul sito andava pubblicato l'elenco dei contributi "
                                      "pubblici ricevuti nel 2025. Causa / contesto: obbligo di trasparenza per chi "
                                      "riceve più di 10.000 euro l'anno da enti pubblici (sanzione 1%, minimo 2.000 "
                                      "euro); dubbio sui fondi «Passi» ricevuti tramite capofila. Intervento e stato: "
                                      "pubblicata il 28/6 nella pagina trasparenza: Comune, 5x1000, quota Passi "
                                      "(inserita per prudenza). Per il 2026 aggiungere anche «Fili»; promemoria a "
                                      "giugno. Fatto.",
                                      ["contributi pubblici", "obbligo di trasparenza", "pagina trasparenza",
                                       "sito web", "sovvenzioni", "5x1000", "scadenza 30 giugno", "sanzione"])]},
             {"name": "IBAN cinque per mille", "who": "treasurer", "stage": "Da fare", "deadline": 40,
              "description": "abbiamo cambiato banca a settembre. aggiornare l'iban sul portale",
              "notes": [("treasurer", 30, "il cinque per mille di ottobre è arrivato sul conto vecchio, per "
                                          "fortuna ancora aperto. il conto vecchio si chiude a dicembre"),
                        ("treasurer", 30, "Sintomo: il cinque per mille di ottobre è arrivato sul conto vecchio, dopo "
                                          "il cambio di banca di settembre. Causa / contesto: l'IBAN per l'accredito "
                                          "del 5x1000 registrato sul portale RUNTS non è stato aggiornato; il conto "
                                          "vecchio si chiude a dicembre. Il cambio di IBAN è uno dei casi in cui va "
                                          "rifatta la pratica 5x1000 sul registro (da verificare). Intervento e "
                                          "stato: da fare l'aggiornamento dell'IBAN sul portale prima della chiusura "
                                          "del conto vecchio.",
                                          ["IBAN", "cinque per mille", "5x1000", "cambio banca",
                                           "conto corrente vecchio", "accredito", "portale RUNTS",
                                           "coordinate bancarie"])]},
             {"name": "Libri sociali e registro volontari", "who": "volunteer", "stage": "Da fare",
              "description": "libro soci, verbali assemblea e direttivo, registro volontari. mettere in ordine",
              "notes": [("volunteer", 15, "il libro verbali del direttivo si ferma a marzo, gli altri sono "
                                          "fogli sparsi in drive. da stampare e incollare"),
                        ("volunteer", 15, "Sintomo: i libri dell'associazione sono incompleti: il libro verbali del "
                                          "direttivo si ferma a marzo, il resto sono fogli sparsi nel drive. Causa / "
                                          "contesto: libri sociali obbligatori degli ETS (Enti del Terzo settore): "
                                          "libro soci, verbali di assemblea e direttivo, registro dei volontari. "
                                          "Intervento e stato: da fare; stampare i verbali e incollarli nei libri, "
                                          "mettere in ordine i registri.",
                                          ["libri sociali", "libro soci", "libro verbali", "verbali direttivo",
                                           "verbali assemblea", "registro volontari",
                                           "ETS Enti del Terzo settore"])]},
             {"name": "Modulo rimborsi volontarie", "who": "treasurer", "stage": "Fatto",
              "description": "autocertificazione fino a 10 al giorno / 150 al mese",
              "notes": [("treasurer", 70, "modulo fatto, delibera del direttivo sui tipi di spesa "
                                          "(benzina per la casa, materiale laboratori)"),
                        ("treasurer", 70, "Sintomo: le volontarie chiedevano come farsi rimborsare piccole spese "
                                          "senza scontrino. Causa / contesto: rimborso con autocertificazione "
                                          "previsto dal Codice del Terzo settore: massimo 10 euro al giorno e 150 "
                                          "euro al mese, solo per i tipi di spesa decisi dal direttivo; mai rimborsi "
                                          "forfettari. Intervento e stato: modulo di autocertificazione preparato; "
                                          "delibera del direttivo sui tipi di spesa ammessi (benzina per la casa, "
                                          "materiale laboratori). Fatto.",
                                          ["rimborso spese", "autocertificazione", "10 euro al giorno",
                                           "150 euro al mese", "delibera direttivo", "spese volontarie",
                                           "senza scontrino", "modulo rimborsi"])]},
             {"name": "Rendiconto raccolta fondi 25 novembre", "who": "treasurer", "stage": "Da fare",
              "deadline": 40, "description": "il banchetto dell'evento è una raccolta fondi occasionale: "
                                             "rendiconto da mettere nel bilancino 2026",
              "notes": [("treasurer", 0, "Sintomo: il banchetto dell'evento del 25 novembre raccoglie offerte e va "
                                         "rendicontato. Causa / contesto: raccolta fondi occasionale degli ETS: il "
                                         "rendiconto specifico va inserito nello stesso PDF del bilancino 2026 da "
                                         "depositare sul RUNTS (errore già costato un deposito respinto). Dal 2026 "
                                         "vale anche la parte fiscale del Codice del Terzo settore (titolo X) e la "
                                         "commercialista raccomanda di rendicontare bene le raccolte fondi. "
                                         "Intervento e stato: da fare dopo l'evento.",
                                         ["raccolta fondi occasionale", "rendiconto raccolta fondi", "banchetto",
                                          "offerte", "bilancino 2026", "deposito RUNTS", "25 novembre"])]},
         ],
         "updates": [
             ("Situazione registro", "at_risk", 55, 4, "bilancio 2025 caricato con una settimana di ritardo, "
                                                       "nessuna diffida (la pec di settembre erano le "
                                                       "indicazioni operative). pec nostra attiva. cambio "
                                                       "presidente da comunicare entro il 19/11: Lucia senza "
                                                       "firma digitale, si va di delega. iban 5x1000 da "
                                                       "aggiornare."),
         ]},
    ],
    "project_rules": [
        {"name": "Chiavi solo dopo il primo mese", "where": "project:" + P_VOLONTARIATO, "severity": "prefer",
         "activities": [], "section": "operations",
         "keywords": "chiavi, consegna chiavi, nuove volontarie, primo mese, accesso sportello, magazzino",
         "body": "Alle volontarie nuove le chiavi (sportello e magazzino) si danno solo dopo il primo mese di "
                 "turni."},
    ],
    "project_documents": [
        {"key": "inventario_casa", "where": "project:" + P_CASA, "name": "Inventario casa e magazzino 2026",
         "summary": "Foglio dell'inventario di ottobre 2026 della casa e del magazzino di sopra, con l'elenco del "
                    "materiale per stanza. Documento riservato, conservato in memoria senza il testo.",
         "keywords": "inventario, foglio inventario, magazzino di sopra, materiale casa, riservato, elenco materiale",
         "url": "https://drive.ginestra.example/casa/inventario-2026", "keep_text": False,
         "text": "Testo che non viene salvato: elenco del materiale per stanza."},
        {"key": "piano_editoriale", "where": "task:" + P_CAMPAGNA + "/Piano editoriale ott-dic",
         "name": "Piano editoriale ottobre-dicembre",
         "summary": "Calendario dei post della campagna fino a dicembre. Lunedì numeri e fonti (dati pubblici sempre "
                    "con la fonte), mercoledì parole (consenso, linguaggio, stereotipi), venerdì le attività senza "
                    "foto della casa; un reel ogni due settimane con voci e non volti; dal 18 novembre countdown "
                    "all'evento del 25.",
         "keywords": "piano editoriale, calendario post, social media, reel, consenso, stereotipi, countdown 25 "
                     "novembre, campagna",
         "url": "https://drive.ginestra.example/comunicazione/piano-ott-dic", "keep_text": True,
         "text": "## Piano editoriale ott-dic\n\n"
                 "Lunedì: numeri e fonti (dati pubblici, sempre con la fonte).\n"
                 "Mercoledì: parole (consenso, linguaggio, stereotipi).\n"
                 "Venerdì: cosa facciamo (corso volontarie, laboratori, evento) senza foto della casa.\n"
                 "Reel: uno ogni due settimane, voci e non volti.\n"
                 "Dal 18 novembre countdown all'evento del 25.\n"},
    ],
    "project_notes": [
        {"kind": "fact", "where": "project:" + P_CASA, "who": "lead", "section": "operations",
         "name": "Ditta caldaia",
         "keywords": "ditta caldaia, manutenzione caldaia, contratto di manutenzione, uscita urgente, tecnico "
                     "caldaia, costo intervento, fornitore",
         "body": "Ditta Bastianelli, contratto di manutenzione annuale fino a giugno 2027. Uscita urgente fuori "
                 "contratto 80 euro + pezzi."},
        {"kind": "fact", "where": "project:" + P_CASA, "who": "volunteer", "section": "operations",
         "name": "Scorte minime",
         "keywords": "scorte minime, kit igiene, lenzuola, detersivi, pannolini 4-5, dotazione casa, riordino",
         "body": "sempre almeno: 2 kit igiene completi, 4 set lenzuola, detersivi per un mese, una scorta di "
                 "pannolini 4-5"},
        {"kind": "fact", "where": "project:" + P_CAMPAGNA, "who": "comms", "section": "operations",
         "name": "Liberatorie foto evento",
         "keywords": "liberatoria foto, consenso immagini, diritti immagine, foto evento, modulo liberatoria, privacy "
                     "foto, panchina rossa",
         "body": "modulo liberatoria nella cartellina dell'evento. chi non firma non va nelle foto, si "
                 "fotografano mani, oggetti, la panchina."},
    ],
}

# -- the funders and partners ---------------------------------------------------------------------------------
P_FILI = "Programma regionale APS - «Fili»"
P_ULS2 = "Umbria legale e sicura 2 - valutazione"
P_PASSI = "«Passi» FSE+ - chiusura e rendiconto"

REGIONE = {
    "ref": "GIN-REGIONE", "name": "Regione Umbria", "city": "Perugia",
    "projects": [
        {"name": P_FILI, "tags": ["bandi", "regione", "rendicontazione"],
         "description": "<p>Programma regionale per ODV/APS (avviso DD 3832/2026, quota 2024). Il nostro: «Fili», "
                        "sportello aperto anche il sabato, formazione volontarie, supervisione. 18 mesi da "
                        "settembre 2026. Contributo 38.500, cofinanziamento 10% (valorizzazione volontariato).</p>",
         "milestones": [("Domanda inviata", -160, 161), ("Avvio attività", -60, 61),
                        ("Rendiconto intermedio", 75, None), ("Fine attività", 485, None)],
         "tasks": [
             {"name": "Domanda e formulario", "who": "lead", "stage": "Fatto", "milestone": "Domanda inviata",
              "description": "A.1 domanda, A.2 formulario, A.3 piano finanziario",
              "notes": [("lead", 175, "letto l'avviso. ci stiamo dentro come APS, area contrasto violenza"),
                        ("lead", 162, "formulario chiuso. piano finanziario con Paola"),
                        ("treasurer", 161, "inviato tutto. ricevuta in drive"),
                        ("lead", 161, "Sintomo: l'associazione voleva candidarsi al programma regionale per APS con "
                                      "un progetto sul contrasto alla violenza. Causa / contesto: avviso regionale "
                                      "per programmi di ODV e APS (DD 3832/2026, accordo di programma); allegati A.1 "
                                      "domanda, A.2 formulario, A.3 piano finanziario. Intervento e stato: avviso "
                                      "letto, requisiti presenti come APS (Associazione di promozione sociale); "
                                      "formulario e piano finanziario completati; tutto inviato, ricevuta nel drive. "
                                      "Fatto.",
                                      ["domanda di finanziamento", "formulario", "piano finanziario",
                                       "avviso regionale APS", "DD 3832/2026", "progetto Fili", "candidatura",
                                       "Associazione di promozione sociale"])]},
             {"name": "Accordo con partner e atto unilaterale", "who": "lead", "stage": "Fatto",
              "description": "A.6 con la coop delle formatrici, A.7 atto unilaterale dopo l'ammissione",
              "notes": [("lead", 70, "atto unilaterale firmato digitalmente e mandato via PEC"),
                        ("lead", 70, "Sintomo: per il progetto «Fili» servivano l'accordo con il partner e l'impegno "
                                     "formale verso la Regione. Causa / contesto: allegato A.6 accordo di "
                                     "partenariato con la cooperativa delle formatrici; allegato A.7 atto unilaterale "
                                     "d'obbligo da firmare dopo l'ammissione al finanziamento. Il progetto «Fili» è "
                                     "finanziato dall'avviso regionale per programmi di ODV e APS. Intervento e "
                                     "stato: atto unilaterale firmato digitalmente e inviato via PEC. Fatto.",
                                     ["atto unilaterale d'obbligo", "accordo di partenariato", "partner",
                                      "cooperativa formatrici", "allegato A.7", "firma digitale", "PEC"])]},
             {"name": "Graduatoria", "who": "lead", "stage": "Fatto",
              "description": "uscita a luglio",
              "notes": [("lead", 110, "AMMESSE! 38.500, decurtate le spese di comunicazione (troppo alte "
                                      "secondo la commissione)"),
                        ("lead", 110, "Sintomo: si aspettava di sapere se il progetto «Fili» fosse stato finanziato. "
                                      "Causa / contesto: graduatoria dell'avviso regionale APS uscita a luglio; la "
                                      "commissione ha giudicato troppo alte le spese di comunicazione. Lezione: "
                                      "tenere la comunicazione in quota modesta e legata ad attività precise. "
                                      "Intervento e stato: progetto ammesso con 38.500 euro, decurtate le spese di "
                                      "comunicazione; seguono atto unilaterale e variazione di budget. Fatto.",
                                      ["graduatoria", "ammissione finanziamento", "progetto ammesso",
                                       "contributo ridotto", "taglio comunicazione", "commissione valutazione",
                                       "Fili"])]},
             {"name": "Avvio sabato allo sportello", "who": "member", "stage": "Fatto", "milestone": "Avvio attività",
              "description": "sab 10-12 con una operatrice + una volontaria",
              "notes": [("member", 58, "primo sabato fatto. cartello orari aggiornato"),
                        ("member", 58, "Sintomo: le donne potevano rivolgersi allo sportello solo nei giorni feriali; "
                                       "con il progetto si apre anche il sabato. Causa / contesto: nuova apertura del "
                                       "sabato 10-12 finanziata dal progetto regionale «Fili», con un'operatrice e "
                                       "una volontaria in turno. Orari attuali: lunedì 15-19, mercoledì 9-13, venerdì "
                                       "15-19, sabato 10-12; fuori orario reperibilità telefonica. Intervento e "
                                       "stato: primo sabato fatto, cartello degli orari aggiornato. Fatto.",
                                       ["apertura sabato", "orari sportello", "sabato mattina", "nuovo orario",
                                        "cartello orari", "progetto Fili", "turno operatrice"])]},
             {"name": "Timesheet mensili operatrici", "who": "treasurer", "stage": "In corso",
              "description": "ogni mese, firmati da operatrice e coordinatrice. NON a fine progetto",
              "notes": [("treasurer", 31, "settembre fatto e firmato"),
                        ("treasurer", 2, "ottobre: manca la firma di Elisa"),
                        ("treasurer", 2, "Sintomo: ogni mese bisogna raccogliere i fogli ore delle operatrici "
                                         "firmati, non tutti a fine progetto. Causa / contesto: timesheet mensili per "
                                         "la rendicontazione del personale sul progetto regionale «Fili», firmati da "
                                         "operatrice e coordinatrice; lezione dai tagli del controllo su «Passi». "
                                         "Regola: firma entro il 5 del mese successivo. Intervento e stato: settembre "
                                         "fatto e firmato; ottobre manca ancora una firma. In corso.",
                                         ["timesheet", "foglio ore", "registro presenze", "rendicontazione personale",
                                          "firma coordinatrice", "mensile", "progetto Fili"])]},
             {"name": "Registro ore volontarie (cofinanziamento)", "who": "volunteer", "stage": "In corso",
              "description": "le ore delle volontarie valgono come cofinanziamento. foglio presenze firmato",
              "notes": [("volunteer", 10, "il foglio di ottobre del sabato non è stato firmato da tutte. "
                                          "recuperare"),
                        ("volunteer", 10, "Sintomo: le ore delle volontarie servono a coprire la quota di "
                                          "cofinanziamento del progetto, ma vanno documentate. Causa / contesto: "
                                          "valorizzazione del lavoro volontario come cofinanziamento del progetto "
                                          "regionale «Fili»; foglio presenze firmato dalle volontarie. I fogli vanno "
                                          "firmati da tutte le presenti al turno. Intervento e stato: il foglio del "
                                          "sabato di ottobre non è stato firmato da tutte; firme da recuperare. In "
                                          "corso.",
                                          ["cofinanziamento", "ore volontarie", "valorizzazione volontariato",
                                           "foglio presenze", "firme mancanti", "progetto Fili",
                                           "rendicontazione"])]},
             {"name": "Rendiconto intermedio", "who": "treasurer", "stage": "Da fare",
              "milestone": "Rendiconto intermedio", "deadline": 75,
              "description": "spese sett-dic. modulistica regionale ancora non uscita",
              "notes": [("treasurer", 12, "chiesto alla Regione quando esce la modulistica, nessuna risposta"),
                        ("treasurer", 12, "Sintomo: vanno rendicontate alla Regione le spese di settembre-dicembre "
                                          "del progetto «Fili». Causa / contesto: rendiconto intermedio con scadenza "
                                          "15 gennaio 2027 (spese fino al 31/12); la modulistica regionale non è "
                                          "ancora stata pubblicata. Il rendiconto finale è dovuto 60 giorni dopo la "
                                          "fine; l'ufficio regionale si contatta via PEC, meglio telefonare il "
                                          "martedì mattina. Intervento e stato: chiesto alla Regione quando esce la "
                                          "modulistica, nessuna risposta. Da fare.",
                                          ["rendiconto intermedio", "rendicontazione spese", "modulistica regionale",
                                           "scadenza 15 gennaio", "progetto Fili", "Regione Umbria"])]},
             {"name": "Logo e CUP su materiali", "who": "comms", "stage": "Fatto",
              "description": "logo Regione + Ministero + dicitura sul cartello del sabato e sui volantini",
              "notes": [("comms", 0, "Sintomo: sul cartello del sabato e sui volantini dovevano comparire i loghi dei "
                                     "finanziatori. Causa / contesto: obblighi di pubblicità del progetto regionale "
                                     "«Fili»: logo della Regione e del Ministero, dicitura del programma e CUP "
                                     "(Codice unico di progetto). Il CUP va chiesto al fornitore già nell'ordine. "
                                     "Intervento e stato: loghi e dicitura inseriti sul cartello del sabato e sui "
                                     "volantini. Fatto.",
                                     ["loghi finanziatori", "CUP", "Codice unico di progetto", "dicitura programma",
                                      "obblighi di pubblicità", "visibilità", "cartello", "volantini"])]},
             {"name": "Variazione budget comunicazione", "who": "lead", "stage": "In attesa",
              "description": "dopo il taglio sulla comunicazione spostare 1.200 da materiali a supervisione? serve "
                             "autorizzazione",
              "notes": [("lead", 20, "mandata la richiesta di variazione via PEC. aspettiamo"),
                        ("lead", 20, "Sintomo: dopo il taglio delle spese di comunicazione si vuole spostare denaro "
                                     "tra le voci del progetto. Causa / contesto: variazione del piano finanziario di "
                                     "«Fili»: 1.200 euro da materiali a supervisione; le variazioni oltre la soglia "
                                     "vanno autorizzate prima dalla Regione. Nella procedura di rendicontazione "
                                     "regionale, le variazioni oltre il 10% di una voce vanno autorizzate prima di "
                                     "spendere. Intervento e stato: richiesta di variazione inviata via PEC; in "
                                     "attesa di autorizzazione.",
                                     ["variazione di budget", "rimodulazione piano finanziario", "spostamento voci",
                                      "autorizzazione Regione", "supervisione", "PEC", "progetto Fili"])]},
         ],
         "updates": [
             ("Avvio", "on_track", 15, 55, "progetto partito a settembre, sabato aperto. timesheet impostati "
                                           "mensili dopo la lezione di Passi."),
             ("Fine ottobre", "at_risk", 25, 2, "timesheet ok ma firme in ritardo, foglio volontarie di ottobre "
                                                 "incompleto. variazione budget chiesta, nessuna risposta. "
                                                 "modulistica del rendiconto intermedio non ancora uscita."),
         ]},
        {"name": P_ULS2, "tags": ["bandi", "regione", "FSE+"],
         "description": "<p>Avviso DD 9321/2026 (rettificato DD 10004): selezione max 5 ETS per co-progettare "
                        "«Umbria legale e sicura 2», PN Inclusione FSE+, sfruttamento lavorativo dei cittadini "
                        "di paesi terzi. Scadenza PEC 12/10. Abbiamo deciso di non candidarci.</p>",
         "milestones": [("Decisione direttivo", -29, 29), ("Scadenza candidature", -20, 20),
                        ("Graduatoria", -9, 9)],
         "tasks": [
             {"name": "Lettura avviso", "who": "lead", "stage": "Fatto",
              "description": "avviso + 5 allegati",
              "notes": [("lead", 38, "letto. è su sfruttamento lavorativo e caporalato, destinatari cittadini "
                                     "paesi terzi. noi c'entriamo solo per la parte donne. requisito: 3 anni "
                                     "negli ultimi 5 negli ambiti dell'avviso, non li abbiamo"),
                        ("lead", 38, "Sintomo: si doveva capire se l'avviso regionale «Umbria legale e sicura 2» "
                                     "facesse per l'associazione. Causa / contesto: avviso di co-progettazione su "
                                     "sfruttamento lavorativo e caporalato per cittadini di paesi terzi (PN "
                                     "Inclusione FSE+), con cinque allegati; requisito di 3 anni di esperienza negli "
                                     "ultimi 5 negli ambiti dell'avviso. Intervento e stato: avviso letto; "
                                     "l'associazione rientra solo per la parte donne e non ha il requisito di "
                                     "esperienza. Fatto.",
                                     ["avviso Umbria legale e sicura 2", "co-progettazione",
                                      "sfruttamento lavorativo", "caporalato", "cittadini paesi terzi",
                                      "requisito esperienza triennale", "FSE+"])]},
             {"name": "Verifica requisiti e firma digitale", "who": "treasurer", "stage": "Fatto",
              "description": "RUNTS ok, sede in Umbria ok, firma digitale??",
              "notes": [("treasurer", 31, "firma digitale di Anna SCADUTA. comunque la rinnoviamo"),
                        ("treasurer", 31, "Sintomo: prima di candidarsi andavano verificati i requisiti formali "
                                          "dell'avviso «Umbria legale e sicura 2». Causa / contesto: iscrizione al "
                                          "RUNTS, sede in Umbria, firma digitale del legale rappresentante per la "
                                          "domanda. La firma digitale serve per la domanda di partecipazione "
                                          "(allegato 1, con marca da bollo da 16 euro). Intervento e stato: RUNTS e "
                                          "sede a posto; la firma digitale della presidente risultava scaduta, "
                                          "rinnovata comunque. Fatto.",
                                          ["verifica requisiti", "requisiti di ammissione", "iscrizione RUNTS",
                                           "sede in Umbria", "firma digitale scaduta", "legale rappresentante"])]},
             {"name": "Decisione: partecipare?", "who": "lead", "stage": "Fatto", "milestone": "Decisione direttivo",
              "description": "direttivo del 2 ottobre",
              "notes": [("lead", 29, "direttivo: NON partecipiamo. motivi: requisito dei 3 anni su "
                                     "sfruttamento lavorativo che non abbiamo, nel raggruppamento solo la "
                                     "capofila è partner della Regione e centro di costo, e non abbiamo forze per "
                                     "una co-progettazione con scadenza ministeriale al 3 novembre. diamo la "
                                     "lettera di adesione a chi ce la chiede"),
                        ("lead", 29, "Sintomo: il direttivo doveva decidere se candidarsi a «Umbria legale e sicura "
                                     "2». Causa / contesto: requisito triennale su sfruttamento lavorativo assente; "
                                     "in raggruppamento solo la capofila è partner della Regione e centro di costo; "
                                     "co-progettazione con scadenza ministeriale al 3 novembre e forze insufficienti. "
                                     "Intervento e stato: direttivo del 2 ottobre: non si partecipa; si dà la lettera "
                                     "di adesione a chi la chiede. Fatto.",
                                     ["decisione direttivo", "rinuncia candidatura", "non partecipare",
                                      "raggruppamento", "capofila", "centro di costo", "co-progettazione",
                                      "lettera di adesione"])]},
             {"name": "Lettera di adesione rete territoriale", "who": "lead", "stage": "Fatto",
              "description": "lettera di adesione alla rete di secondo livello per una candidatura",
              "notes": [("lead", 23, "una coop di Perugia ci ha chiesto la lettera. firmata da Anna "
                                     "(firma nuova) e mandata il 9"),
                        ("lead", 22, "la scadenza è slittata dal 9 al 12 ottobre (DD 10004), avevano ancora "
                                     "tempo"),
                        ("lead", 22, "Sintomo: una cooperativa di Perugia ha chiesto all'associazione una lettera di "
                                     "sostegno alla propria candidatura. Causa / contesto: lettera di adesione alla "
                                     "rete territoriale di secondo livello per l'avviso «Umbria legale e sicura 2»; "
                                     "scadenza prorogata dal 9 al 12 ottobre dalla DD 10004/2026. Intervento e stato: "
                                     "lettera firmata dalla presidente con la firma digitale rinnovata e inviata il "
                                     "9. Fatto.",
                                     ["lettera di adesione", "lettera di sostegno", "rete territoriale",
                                      "rete di secondo livello", "cooperativa Perugia", "proroga scadenza",
                                      "DD 10004/2026"])]},
             {"name": "Graduatoria uscita", "who": "lead", "stage": "Fatto", "milestone": "Graduatoria",
              "description": "DD 10735",
              "notes": [("lead", 9, "solo 2 candidature arrivate, ammesse entrambe alla co-progettazione. la "
                                    "coop della nostra lettera c'è"),
                        ("lead", 9, "Sintomo: si voleva sapere com'era finita la selezione di «Umbria legale e sicura "
                                    "2». Causa / contesto: graduatoria approvata con la determina DD 10735/2026 della "
                                    "Regione Umbria. L'associazione aveva scelto di non candidarsi e di dare solo la "
                                    "lettera di adesione. Intervento e stato: arrivate solo 2 candidature, entrambe "
                                    "ammesse alla co-progettazione; c'è anche la cooperativa a cui l'associazione "
                                    "aveva dato la lettera di adesione. Fatto.",
                                    ["graduatoria", "DD 10735/2026", "esito selezione", "candidature ammesse",
                                     "co-progettazione", "Umbria legale e sicura 2", "determina"])]},
             {"name": "Chiedere di partecipare al tavolo", "who": "lead", "stage": "In attesa",
              "description": "art. 10: la Regione può invitare altri soggetti al tavolo senza budget",
              "notes": [("lead", 7, "scritto al servizio terzo settore per la parte donne vittime di "
                                    "sfruttamento. nessuna risposta"),
                        ("lead", 7, "Sintomo: pur senza candidarsi, l'associazione vorrebbe partecipare ai lavori di "
                                    "«Umbria legale e sicura 2» per la parte sulle donne vittime di sfruttamento. "
                                    "Causa / contesto: l'art. 10 dell'avviso consente alla Regione di invitare altri "
                                    "soggetti al tavolo di co-progettazione, senza budget. L'ufficio regionale "
                                    "risponde lento; meglio telefonare il martedì mattina. Intervento e stato: "
                                    "scritto al servizio regionale terzo settore; nessuna risposta, in attesa.",
                                    ["tavolo di co-progettazione", "art. 10 avviso", "invito senza budget",
                                     "donne vittime di sfruttamento", "servizio terzo settore", "Regione Umbria",
                                     "partecipazione al tavolo"])]},
             {"name": "Archiviare avviso e allegati", "who": "volunteer", "stage": "Fatto",
              "description": "in drive cartella bandi/2026",
              "notes": [("volunteer", 0, "Sintomo: l'avviso «Umbria legale e sicura 2» e i suoi allegati andavano "
                                         "conservati per riferimento futuro, anche se l'associazione non ha "
                                         "partecipato. Causa / contesto: archivio dei bandi sul drive, cartella "
                                         "bandi/2026: avviso (allegato A alla DD 9321/2026) e modulistica degli "
                                         "allegati 1-5. Allegati: domanda di partecipazione, proposta progettuale, "
                                         "piano dei costi, curriculum ETS, autodichiarazione del raggruppamento. "
                                         "Intervento e stato: documenti archiviati nella cartella. Fatto.",
                                         ["archivio bandi", "cartella bandi 2026", "avviso", "allegati",
                                          "modulistica", "drive", "DD 9321/2026"])]},
         ],
         "updates": [
             ("Chiuso per noi", "on_hold", 100, 8, "non ci siamo candidate (decisione del 2/10). data la lettera "
                                                   "di adesione. graduatoria con due ammessi. resta aperta la "
                                                   "richiesta di partecipare al tavolo."),
         ]},
        {"name": P_PASSI, "tags": ["bandi", "regione", "FSE+", "rendicontazione"],
         "description": "<p>Progetto «Passi» (PR FSE+ Umbria, percorsi di inclusione lavorativa), noi partner "
                        "dell'ATS, capofila una cooperativa. Attività finite il 30 giugno 2026. Rendiconto finale "
                        "con tagli: integrazioni mandate.</p>",
         "milestones": [("Fine attività", -124, 124), ("Rendiconto finale", -80, 80),
                        ("Integrazioni", -10, 10), ("Saldo", 60, None)],
         "tasks": [
             {"name": "Rendiconto finale", "who": "treasurer", "stage": "Fatto", "milestone": "Rendiconto finale",
              "description": "caricare tutto in piattaforma tramite la capofila",
              "notes": [("treasurer", 82, "caricati: buste paga, F24, quietanze, timesheet, fatture formatrici"),
                        ("treasurer", 80, "inviato alla capofila"),
                        ("treasurer", 80, "Sintomo: a fine progetto «Passi» andava consegnata tutta la documentazione "
                                          "delle spese. Causa / contesto: rendiconto finale di un progetto FSE+ "
                                          "(Fondo sociale europeo Plus) in ATS: da partner, i giustificativi si "
                                          "caricano in piattaforma tramite la capofila; buste paga, F24, quietanze, "
                                          "timesheet, fatture delle formatrici. Tutti i documenti si conservano 5 "
                                          "anni. Intervento e stato: documenti caricati e inviati alla capofila. "
                                          "Fatto.",
                                          ["rendiconto finale", "FSE+", "Fondo sociale europeo",
                                           "giustificativi di spesa", "buste paga F24", "quietanze", "capofila",
                                           "piattaforma regionale"])]},
             {"name": "Esito controllo: spese tagliate", "who": "treasurer", "stage": "Fatto",
              "description": "verbale di controllo con tagli",
              "notes": [("treasurer", 37, "TAGLI 3.870 euro su 41.000. motivi: 1) timesheet di Elisa di "
                                          "gennaio-marzo compilati a fine progetto, non mensili e senza firma "
                                          "della coordinatrice 2) formatrice pagata in contanti (450) 3) due "
                                          "fatture senza CUP e senza dicitura del programma"),
                        ("lead", 36, "che rabbia. il punto 2 è perso, sugli altri si può fare integrazione "
                                     "entro 30 giorni"),
                        ("treasurer", 36, "Sintomo: il verbale di controllo del progetto «Passi» ha tagliato 3.870 "
                                          "euro su 41.000. Causa / contesto: controllo di primo livello FSE+: "
                                          "timesheet di gennaio-marzo compilati a fine progetto, non mensili e senza "
                                          "firma della coordinatrice; formatrice pagata in contanti (450 euro), spesa "
                                          "non tracciabile; due fatture senza CUP e senza dicitura del programma. "
                                          "Intervento e stato: il contante è perso; per gli altri punti integrazioni "
                                          "possibili entro 30 giorni. Fatto.",
                                          ["spese non ammissibili", "tagli rendiconto", "verbale di controllo",
                                           "controllo di primo livello", "timesheet non mensili",
                                           "pagamento in contanti", "fatture senza CUP", "decurtazione"])]},
             {"name": "Integrazioni al controllo", "who": "treasurer", "stage": "Fatto", "milestone": "Integrazioni",
              "description": "30 gg",
              "notes": [("treasurer", 25, "le fatture senza CUP: chiesto al fornitore nota di credito e "
                                          "rifattura con CUP e dicitura"),
                        ("treasurer", 12, "timesheet: dichiarazione sostitutiva della coordinatrice + agenda "
                                          "del sportello come prova. vediamo"),
                        ("treasurer", 10, "mandate le integrazioni alla capofila"),
                        ("treasurer", 10, "Sintomo: entro 30 giorni si potevano recuperare parte delle spese tagliate "
                                          "al controllo di «Passi». Causa / contesto: integrazioni documentali: per "
                                          "le fatture senza CUP nota di credito e rifattura del fornitore con CUP e "
                                          "dicitura; per i timesheet dichiarazione sostitutiva della coordinatrice e "
                                          "agenda dello sportello come prova. Intervento e stato: integrazioni "
                                          "inviate alla capofila; esito non ancora noto. Fatto.",
                                          ["integrazioni documentali", "controdeduzioni", "nota di credito",
                                           "rifatturazione", "CUP", "dichiarazione sostitutiva", "timesheet",
                                           "30 giorni"])]},
             {"name": "Saldo", "who": "treasurer", "stage": "In attesa", "milestone": "Saldo",
              "description": "il saldo arriva alla capofila che poi gira a noi",
              "notes": [("treasurer", 0, "Sintomo: l'associazione aspetta l'ultima quota del contributo del progetto "
                                         "«Passi». Causa / contesto: in ATS il saldo del finanziamento FSE+ viene "
                                         "erogato alla capofila, che poi lo trasferisce ai partner. L'importo dipende "
                                         "dall'esito del controllo, che ha tagliato 3.870 euro, e delle integrazioni "
                                         "inviate; nessuna data di erogazione è nota. Intervento e stato: in attesa "
                                         "dell'erogazione alla capofila e del successivo trasferimento.",
                                         ["saldo", "erogazione finale", "contributo", "capofila",
                                          "trasferimento ai partner", "ATS", "FSE+"])]},
             {"name": "Riunione ATS chiusura", "who": "lead", "stage": "Fatto",
              "description": "con la capofila e gli altri partner",
              "notes": [("lead", 120, "chiusura attività ok. la capofila vuole i documenti entro fine luglio"),
                        ("lead", 120, "Sintomo: la capofila ha convocato i partner per chiudere il progetto «Passi». "
                                      "Causa / contesto: riunione dell'ATS (Associazione temporanea di scopo) con la "
                                      "capofila e gli altri partner per la chiusura delle attività e la raccolta dei "
                                      "documenti di rendiconto. Il rendiconto finale è poi stato caricato tramite la "
                                      "capofila. Intervento e stato: chiusura delle attività confermata; la capofila "
                                      "vuole i documenti entro fine luglio. Fatto.",
                                      ["ATS", "Associazione temporanea di scopo", "riunione partner", "capofila",
                                       "chiusura progetto", "scadenza documenti", "Passi"])]},
             {"name": "Lezione per Fili", "who": "lead", "stage": "Fatto",
              "description": "cosa cambiamo nel progetto regionale dopo i tagli di Passi",
              "notes": [("lead", 34, "da ora: timesheet mensili firmati, CUP in ogni ordine e fattura, zero "
                                     "contanti. detto a tutte in riunione"),
                        ("lead", 34, "Sintomo: dopo i tagli subiti su «Passi» non si vogliono ripetere gli stessi "
                                     "errori nel progetto regionale «Fili». Causa / contesto: cause dei tagli: "
                                     "timesheet non mensili, fatture senza CUP, pagamenti in contanti non "
                                     "tracciabili. Valgono per ogni progetto regionale finanziato. Intervento e "
                                     "stato: nuove regole comunicate a tutte in riunione: timesheet mensili firmati, "
                                     "CUP su ogni ordine e fattura, zero contanti. Fatto.",
                                     ["lezioni apprese", "timesheet mensili", "CUP su fatture", "zero contanti",
                                      "tracciabilità pagamenti", "rendicontazione", "progetto Fili"])]},
         ],
         "updates": [
             ("Tagli", "off_track", 80, 35, "controllo con tagli per 3.870 euro (timesheet, contanti, CUP)."),
             ("Integrazioni mandate", "on_track", 90, 9, "integrazioni inviate: rifatture con CUP e "
                                                          "dichiarazione sui timesheet. il contante è perso. "
                                                          "attesa saldo."),
         ]},
    ],
    "rules": [
        {"name": "Timesheet mensili firmati", "where": "customer", "who": "lead", "state": "active",
         "severity": "must", "activities": ["reporting"], "section": "operations",
         "keywords": "timesheet, foglio ore, registro presenze, firma mensile, entro il 5, operatrici, progetto "
                     "regionale, rendicontazione personale",
         "body": "Su ogni progetto regionale le ore delle operatrici si scrivono nel timesheet ogni mese e si "
                 "firmano (operatrice e coordinatrice) entro il 5 del mese dopo."},
        {"name": "CUP e dicitura su ogni giustificativo", "where": "customer", "who": "lead", "state": "active",
         "severity": "must", "activities": ["reporting"], "section": "operations",
         "keywords": "CUP, Codice unico di progetto, dicitura programma, giustificativi, fatture, ordini, ricevute, "
                     "fornitore",
         "body": "Ordini, fatture, ricevute di un progetto finanziato riportano il CUP e la dicitura del "
                 "programma. Si chiede al fornitore prima, quando si ordina."},
    ],
    "documents": [
        {"key": "avviso_uls2", "where": "project:" + P_ULS2,
         "name": "Avviso «Umbria legale e sicura 2» (Allegato A alla DD 9321/2026)",
         "summary": "Avviso pubblico della Regione Umbria per selezionare al massimo cinque ETS come partner nella "
                    "co-progettazione e attuazione dell'intervento «Umbria legale e sicura 2», sul PN Inclusione e "
                    "lotta alla povertà 2021-2027 (FSE+) e sul FAMI: contrasto al lavoro sommerso, al caporalato e "
                    "allo sfruttamento lavorativo dei cittadini di paesi terzi. Importo FSE+ di 583.124,44 euro; "
                    "requisiti di esperienza; candidature via PEC entro il 12 ottobre dopo la proroga; criteri su 100 "
                    "punti con soglia 60.",
         "keywords": "Umbria legale e sicura 2, avviso co-progettazione, PN Inclusione FSE+, FAMI, caporalato, "
                     "sfruttamento lavorativo, cittadini paesi terzi, DD 9321/2026",
         "url": URL_ULS2 + "#avviso-umbria-legale-sicura-2", "text_file": "avviso-umbria-legale-sicura-2"},
        {"key": "allegato_1", "where": "project:" + P_ULS2, "name": "Allegato 1 - Domanda di partecipazione",
         "summary": "Modello di istanza di candidatura all'avviso «Umbria legale e sicura 2», indirizzata al Servizio "
                    "terzo settore della Regione Umbria, con marca da bollo da 16 euro. Contiene la dichiarazione "
                    "sostitutiva (DPR 445/2000) del legale rappresentante sui requisiti soggettivi, la sede in Umbria "
                    "e l'assenza di cause di esclusione.",
         "keywords": "domanda di partecipazione, istanza di candidatura, marca da bollo 16 euro, dichiarazione "
                     "sostitutiva, DPR 445/2000, cause di esclusione, legale rappresentante, allegato 1",
         "url": URL_ULS2 + "#allegato-1-domanda-partecipazione", "text_file": "allegato-1-domanda-partecipazione"},
        {"key": "allegato_2", "where": "project:" + P_ULS2, "name": "Allegato 2 - Proposta progettuale",
         "summary": "Formulario della proposta progettuale per l'avviso «Umbria legale e sicura 2» (PN Inclusione "
                    "FSE+, obiettivo ESO4.9). Chiede dati identificativi e partenariato, analisi del contesto, "
                    "obiettivi, destinatari, attività, indicatori, piano e cronoprogramma.",
         "keywords": "proposta progettuale, formulario, allegato 2, partenariato, cronoprogramma, indicatori, "
                     "destinatari, ESO4.9",
         "url": URL_ULS2 + "#allegato-2-proposta-progettuale", "text_file": "allegato-2-proposta-progettuale"},
        {"key": "allegato_3", "where": "project:" + P_ULS2, "name": "Allegato 3 - Piano dei costi",
         "summary": "Modello di piano finanziario della candidatura all'avviso «Umbria legale e sicura 2» (PN "
                    "Inclusione FSE+). Prevede le voci di costo diretto A-H (dal personale ai viaggi) e i costi "
                    "indiretti forfettari al 15% del personale o al 7% dei costi diretti.",
         "keywords": "piano dei costi, piano finanziario, budget, costi diretti, costi indiretti, forfettario 15%, "
                     "allegato 3, voci di spesa",
         "url": URL_ULS2 + "#allegato-3-piano-dei-costi", "text_file": "allegato-3-piano-dei-costi"},
        {"key": "allegato_4", "where": "project:" + P_ULS2, "name": "Allegato 4 - Curriculum ETS",
         "summary": "Modello di curriculum dell'ente proponente per l'avviso «Umbria legale e sicura 2», reso come "
                    "dichiarazione sostitutiva (DPR 445/2000). Chiede le tabelle dei progetti con fondi europei "
                    "2021-2027 gestiti come capofila e come partner diretto (centro di imputazione di costo) nel "
                    "settore dell'avviso.",
         "keywords": "curriculum ETS, esperienze pregresse, progetti fondi europei, capofila, partner diretto, centro "
                     "di costo, allegato 4, requisito esperienza",
         "url": URL_ULS2 + "#allegato-4-curriculum-ets", "text_file": "allegato-4-curriculum-ets"},
        {"key": "allegato_5", "where": "project:" + P_ULS2,
         "name": "Allegato 5 - Autodichiarazione enti del raggruppamento",
         "summary": "Modello di autodichiarazione per ciascun ente di un raggruppamento che si candida all'avviso "
                    "«Umbria legale e sicura 2». Attesta i requisiti di onorabilità e gestionali, a firma del legale "
                    "rappresentante.",
         "keywords": "autodichiarazione, raggruppamento, requisiti di onorabilità, requisiti gestionali, allegato 5, "
                     "legale rappresentante, partenariato",
         "url": URL_ULS2 + "#allegato-5-autodichiarazione-raggruppamento",
         "text_file": "allegato-5-autodichiarazione-raggruppamento"},
        {"key": "dd_9321", "where": "project:" + P_ULS2, "name": "DD 9321/2026 - approvazione avviso",
         "summary": "Determinazione dirigenziale n. 9321 del 21/09/2026 della Regione Umbria che, in attuazione della "
                    "DGR 1001/2026, approva l'avviso «Umbria legale e sicura 2» e la relativa modulistica per "
                    "selezionare ETS partner nella co-progettazione (art. 55 del Codice del Terzo settore). La "
                    "commissione di valutazione si nomina dopo la scadenza.",
         "keywords": "DD 9321/2026, approvazione avviso, determina dirigenziale, DGR 1001/2026, co-progettazione art. "
                     "55, Umbria legale e sicura 2, modulistica, commissione",
         "url": URL_ULS2 + "#dd-9321-2026", "text_file": "dd-9321-2026"},
        {"key": "dd_10004", "where": "project:" + P_ULS2, "name": "DD 10004/2026 - rettifica e proroga",
         "summary": "Determinazione dirigenziale n. 10004 del 06/10/2026 della Regione Umbria che corregge un errore "
                    "materiale dell'art. 1 dell'avviso «Umbria legale e sicura 2» (tipologie di soggetti ammessi nel "
                    "raggruppamento, come ONG, organismi senza fini di lucro, imprese sociali, fondazioni) e proroga "
                    "la scadenza delle candidature dal 9 al 12 ottobre 2026.",
         "keywords": "DD 10004/2026, rettifica avviso, errore materiale, proroga scadenza, 12 ottobre, "
                     "raggruppamento, Umbria legale e sicura 2",
         "url": URL_ULS2 + "#dd-10004-2026", "text_file": "dd-10004-2026"},
        {"key": "dd_10735", "where": "task:" + P_ULS2 + "/Graduatoria uscita",
         "name": "DD 10735/2026 - graduatoria",
         "summary": "Determinazione dirigenziale n. 10735 del 22/10/2026 della Regione Umbria che approva la "
                    "graduatoria delle candidature all'avviso «Umbria legale e sicura 2» (DD 9321/2026, rettificato "
                    "con DD 10004/2026). Sono arrivate due candidature, entrambe ammesse alla co-progettazione.",
         "keywords": "DD 10735/2026, graduatoria, esito avviso, candidature ammesse, co-progettazione, Umbria legale "
                     "e sicura 2, determina dirigenziale",
         "url": URL_ULS2 + "#dd-10735-2026", "text_file": "dd-10735-2026"},
        {"key": "dd_3832", "where": "project:" + P_FILI,
         "name": "DD 3832/2026 - avviso programmi regionali ODV/APS quota 2024",
         "summary": "Determinazione dirigenziale del 22/04/2026 della Regione Umbria che approva l'avviso per "
                    "programmi regionali di attività di interesse generale (art. 5 del Codice del Terzo settore) di "
                    "ODV, APS e Fondazioni del Terzo settore, sull'accordo di programma 2022-2024, quota 2024. "
                    "Dotazione di 675.964 euro e modulistica negli allegati A.1-A.7; è l'avviso da cui nasce il "
                    "progetto «Fili».",
         "keywords": "DD 3832/2026, avviso programmi regionali, ODV Organizzazioni di volontariato, APS, accordo di "
                     "programma 2022-2024, attività di interesse generale, allegati A.1-A.7, progetto Fili",
         "url": URL_APS + "#dd-3832-2026", "text_file": "dd-3832-2026"},
    ],
    "notes": [
        {"kind": "procedure", "where": "customer", "who": "treasurer", "section": "operations",
         "name": "Rendicontare un progetto FSE+",
         "keywords": "rendicontazione FSE+, Fondo sociale europeo Plus, timesheet mensili, busta paga F24 quietanza, "
                     "CUP, niente contanti, variazione piano 10%, conservazione 5 anni",
         "body": "- timesheet mensili firmati (non a fine progetto!)\n- per il personale: busta paga + F24 + "
                 "quietanza del bonifico\n- fatture con CUP e dicitura del programma, pagate con bonifico\n"
                 "- niente contanti\n- tutto caricato in piattaforma (se siamo partner lo carica la "
                 "capofila)\n- variazioni del piano oltre il 10% di una voce: autorizzazione prima\n"
                 "- tenere tutto 5 anni"},
        {"kind": "fact", "where": "project:" + P_FILI, "who": "lead", "section": "operations",
         "name": "Scadenze Fili",
         "keywords": "scadenze Fili, rendiconto intermedio, 15 gennaio 2027, rendiconto finale, 60 giorni, accordo di "
                     "programma, proroga 2028, progetto regionale APS",
         "body": "rendiconto intermedio entro il 15 gennaio 2027 (spese fino al 31/12), finale 60 giorni dopo la "
                 "fine. l'accordo di programma regionale è prorogato al 30 giugno 2028"},
        {"kind": "fact", "where": "project:" + P_ULS2, "who": "lead", "section": "operations",
         "name": "Perché non abbiamo partecipato a Umbria legale e sicura 2",
         "keywords": "decisione, requisiti, Umbria legale e sicura 2, rinuncia candidatura, requisito esperienza "
                     "triennale, sfruttamento lavorativo, cittadini paesi terzi, raggruppamento capofila, "
                     "co-progettazione, decisione direttivo",
         "body": "Requisito di esperienza triennale negli ambiti dell'avviso (sfruttamento lavorativo, "
                 "cittadini di paesi terzi) che non abbiamo; in raggruppamento solo la capofila è partner diretto; "
                 "tempi strettissimi. Decisione del direttivo del 2 ottobre."},
        {"kind": "fact", "where": "customer", "who": "lead", "section": "profile",
         "name": "Ufficio regionale di riferimento",
         "keywords": "ufficio regionale, Servizio terzo settore, Regione Umbria, contatti Regione, PEC Regione, "
                     "telefonare martedì, inclusione sociale",
         "body": "Servizio politiche di contrasto alla povertà, integrazione e inclusione sociale, terzo settore. "
                 "Si scrive solo via PEC. Rispondono lenti, meglio telefonare il martedì mattina."},
    ],
}

P_8X1000 = "Otto per mille 2026 - laboratori nelle scuole"
OTTOXMILLE = {
    "ref": "GIN-OPM", "name": "Tavola valdese - Otto per mille", "city": "Roma",
    "projects": [
        {"name": P_8X1000, "tags": ["bandi", "8x1000", "scuole"],
         "description": "<p>Bando ordinario 2026: laboratori «Parole che contano» in 4 scuole medie e 2 "
                        "superiori, gen-mag 2027. Approvato a settembre 2026.</p>",
         "milestones": [("Domanda su Juno", -270, 272), ("Approvazione", -45, 45),
                        ("Inizio laboratori", 75, None), ("Rendiconto", 270, None)],
         "tasks": [
             {"name": "Domanda su Juno", "who": "lead", "stage": "Fatto", "milestone": "Domanda su Juno",
              "description": "registrazione piattaforma Juno + domanda",
              "notes": [("lead", 280, "registrate su Juno. le linee guida dicono che si può anche in inglese, "
                                      "noi in italiano"),
                        ("lead", 272, "inviata"),
                        ("lead", 272, "Sintomo: per finanziare i laboratori nelle scuole si voleva presentare domanda "
                                      "all'Otto per mille valdese. Causa / contesto: bando 8x1000 della Tavola "
                                      "valdese: domanda solo online sulla piattaforma Juno, previa registrazione; le "
                                      "linee guida ammettono anche l'inglese. L'8x1000 valdese finanzia associazioni "
                                      "per scopi assistenziali, culturali, umanitari, non lucrativi; l'elenco dei "
                                      "progetti approvati esce a settembre. Intervento e stato: registrazione su Juno "
                                      "fatta, domanda compilata in italiano e inviata. Fatto.",
                                      ["Juno", "piattaforma Juno", "Otto per mille", "8x1000", "Tavola valdese",
                                       "domanda online", "laboratori scuole", "registrazione"])]},
             {"name": "Approvazione e accettazione", "who": "lead", "stage": "Fatto", "milestone": "Approvazione",
              "description": "elenco progetti approvati pubblicato a settembre",
              "notes": [("lead", 45, "ci siamo nell'elenco! 14.000 su 18.000 chiesti"),
                        ("treasurer", 40, "accettazione firmata, IBAN comunicato"),
                        ("lead", 40, "Sintomo: si aspettava l'esito della domanda 8x1000 per i laboratori nelle "
                                     "scuole. Causa / contesto: elenco dei progetti approvati dalla Tavola valdese "
                                     "pubblicato a settembre; dopo l'approvazione servono l'accettazione firmata e la "
                                     "comunicazione dell'IBAN. Seguono la rimodulazione del budget sui 14.000 euro e "
                                     "il rendiconto con i moduli caricati su Juno. Intervento e stato: progetto "
                                     "approvato con 14.000 euro su 18.000 chiesti; accettazione firmata e IBAN "
                                     "comunicato. Fatto.",
                                     ["progetto approvato", "Otto per mille", "8x1000", "Tavola valdese",
                                      "accettazione contributo", "IBAN", "contributo ridotto"])]},
             {"name": "Rimodulare budget su 14.000", "who": "lead", "stage": "In corso",
              "description": "togliamo una superiore o riduciamo gli incontri?",
              "notes": [("lead", 30, "proposta: 4 medie + 1 superiore, incontri da 4 a 3 per classe"),
                        ("member", 28, "3 incontri sono pochi per il modulo sul consenso, meglio togliere una "
                                       "media"),
                        ("lead", 28, "Sintomo: il contributo 8x1000 è inferiore al richiesto e il progetto dei "
                                     "laboratori va ridimensionato. Causa / contesto: rimodulazione del budget da "
                                     "18.000 a 14.000 euro: ridurre le scuole o gli incontri per classe. Intervento e "
                                     "stato: prima proposta 4 medie più 1 superiore con incontri da 4 a 3; obiezione: "
                                     "3 incontri sono pochi per il modulo sul consenso, meglio togliere una scuola "
                                     "media. In corso.",
                                     ["rimodulazione budget", "riduzione progetto", "laboratori scuole",
                                      "incontri per classe", "scuole medie", "modulo consenso", "8x1000"])]},
             {"name": "Calendario con le scuole", "who": "member", "stage": "In corso",
              "milestone": "Inizio laboratori", "deadline": 45, "description": "referenti delle scuole, date, aule",
              "notes": [("member", 15, "2 scuole hanno già dato le date, le altre dopo i consigli di classe"),
                        ("member", 15, "Sintomo: i laboratori del progetto 8x1000 vanno fissati con ciascuna scuola. "
                                       "Causa / contesto: calendario degli incontri con i docenti referenti: date e "
                                       "aule; le scuole decidono dopo i consigli di classe. Il progetto prevede "
                                       "laboratori in scuole medie e superiori, con il numero di incontri ancora in "
                                       "discussione nella rimodulazione. Intervento e stato: due scuole hanno già "
                                       "dato le date, le altre dopo i consigli di classe. In corso.",
                                       ["calendario laboratori", "referenti scuole", "date incontri", "aule",
                                        "consigli di classe", "programmazione scuole", "8x1000"])]},
             {"name": "Consenso genitori", "who": "member", "stage": "Da fare", "deadline": 60,
              "description": "modulo informativa per i genitori, lo distribuisce la scuola",
              "notes": [("member", 0, "Sintomo: per far partecipare gli studenti ai laboratori serve informare i "
                                      "genitori e raccogliere il loro consenso. Causa / contesto: modulo di "
                                      "informativa e consenso per i genitori dei minori, distribuito tramite la "
                                      "scuola. I laboratori coinvolgono studenti minorenni: nelle foto della "
                                      "relazione finale 8x1000 mai i ragazzi in volto. Il modulo va pronto prima "
                                      "dell'avvio degli incontri. Intervento e stato: da fare; modulo da preparare.",
                                      ["consenso genitori", "informativa genitori", "autorizzazione minori",
                                       "liberatoria", "modulo scuola", "laboratori scuole", "privacy minori"])]},
             {"name": "Regole di visibilità 8x1000", "who": "comms", "stage": "Da fare",
              "description": "logo e dicitura su tutto: slide, volantini, post",
              "notes": [("comms", 0, "Sintomo: su tutti i materiali del progetto dei laboratori deve comparire il "
                                     "finanziatore. Causa / contesto: regole di visibilità della Tavola valdese: logo "
                                     "e dicitura dell'Otto per mille su slide, volantini e post; senza, il rendiconto "
                                     "può avere problemi. È anche una regola del progetto Otto per mille: logo e "
                                     "dicitura su tutti i materiali e i post del progetto finanziato. Intervento e "
                                     "stato: da fare.",
                                     ["regole di visibilità", "logo Otto per mille", "dicitura 8x1000",
                                      "Tavola valdese", "slide", "volantini", "post social"])]},
             {"name": "Linee guida bando 2027", "who": "lead", "stage": "Da fare", "deadline": 20,
              "description": "escono a novembre. leggere e decidere se ripresentarsi (casa?)",
              "notes": [("lead", 0, "Sintomo: a novembre escono le nuove linee guida dell'Otto per mille e va deciso "
                                    "se ripresentarsi, forse per la casa. Causa / contesto: bando 8x1000 della Tavola "
                                    "valdese 2027, linee guida pubblicate ogni anno a novembre, domanda su Juno. "
                                    "Possono chiedere associazioni per scopi assistenziali, culturali, umanitari, non "
                                    "lucrativi. Intervento e stato: da fare la lettura delle linee guida e la "
                                    "decisione.",
                                    ["linee guida 8x1000", "bando 2027", "Otto per mille", "Tavola valdese",
                                     "nuova domanda", "Juno", "progetto casa"])]},
         ],
         "updates": [
             ("Approvato", "on_track", 10, 40, "approvato a 14.000. da rimodulare il budget e fissare il "
                                               "calendario con le scuole."),
         ]},
    ],
    "rules": [
        {"name": "Visibilità del contributo Otto per mille", "where": "customer", "who": "lead", "state": "active",
         "severity": "must", "activities": ["communication"], "section": "operations",
         "keywords": "visibilità, logo Otto per mille, 8x1000, dicitura finanziatore, materiali progetto, post, "
                     "Tavola valdese",
         "body": "Su tutti i materiali e i post del progetto finanziato va il logo e la dicitura dell'Otto per "
                 "mille, secondo le loro regole di visibilità. Senza, il rendiconto può avere problemi."},
    ],
    "documents": [],
    "notes": [
        {"kind": "fact", "where": "customer", "who": "lead", "section": "operations",
         "name": "Bando 8x1000 come funziona",
         "keywords": "Otto per mille, 8x1000, Tavola valdese, Chiesa valdese, piattaforma Juno, linee guida novembre, "
                     "elenco approvati settembre, bando",
         "body": "Linee guida ogni anno a novembre, domanda solo sulla piattaforma Juno. Possono chiedere "
                 "associazioni per scopi assistenziali, culturali, umanitari, non lucrativi. Elenco approvati a "
                 "settembre. Ufficio riceve solo su appuntamento."},
        {"kind": "procedure", "where": "project:" + P_8X1000, "who": "treasurer", "section": "operations",
         "name": "Rendiconto 8x1000",
         "keywords": "rendiconto 8x1000, Otto per mille, Juno, relazione finale, fatture intestate, foto laboratori, "
                     "Tavola valdese",
         "body": "moduli del rendiconto sul sito, si carica su Juno. fatture intestate a noi con il titolo del "
                 "progetto, relazione finale con foto (dei laboratori, mai dei ragazzi in volto)."},
    ],
}

P_ARREDI = "Arredi della casa - Fondazione Valle Verde"
VALLEVERDE = {
    "ref": "GIN-VALLEVERDE", "name": "Fondazione Valle Verde", "city": "",
    "projects": [
        {"name": P_ARREDI, "tags": ["bandi", "fondazione", "casa"],
         "description": "<p>Contributo di 6.000 euro per letti, armadi e cucina della casa. Fine acquisti 30 "
                        "settembre, rendiconto entro 90 giorni.</p>",
         "milestones": [("Contributo concesso", -140, 140), ("Acquisti", -32, 31), ("Rendiconto", 58, None)],
         "tasks": [
             {"name": "Tre preventivi", "who": "treasurer", "stage": "Fatto",
              "description": "obbligatori sopra 1.000 euro",
              "notes": [("treasurer", 120, "3 preventivi per letti e armadi. scelto il secondo (consegna "
                                           "inclusa)"),
                        ("treasurer", 120, "Sintomo: per comprare letti e armadi per la casa con il contributo della "
                                           "Fondazione servivano tre offerte. Causa / contesto: regola della "
                                           "Fondazione Valle Verde: tre preventivi obbligatori per ogni acquisto "
                                           "sopra 1.000 euro, da allegare al rendiconto. I preventivi vanno allegati "
                                           "al rendiconto alla Fondazione. Intervento e stato: raccolti tre "
                                           "preventivi per letti e armadi; scelto il secondo, consegna inclusa. "
                                           "Fatto.",
                                           ["tre preventivi", "offerte fornitori", "comparazione prezzi",
                                            "sopra 1.000 euro", "letti e armadi", "Fondazione Valle Verde",
                                            "arredi"])]},
             {"name": "Acquisto e consegna", "who": "lead", "stage": "Fatto", "milestone": "Acquisti",
              "description": "consegna allo sportello, poi portiamo noi",
              "notes": [("lead", 33, "consegna allo sportello come sempre, NON alla casa. portato col furgone "
                                     "in due giri"),
                        ("lead", 33, "Sintomo: i nuovi letti e armadi acquistati con il contributo della Fondazione "
                                     "dovevano arrivare alla casa senza rivelarne l'indirizzo. Causa / contesto: "
                                     "regola di riservatezza: consegne e ditte usano solo l'indirizzo dello "
                                     "sportello. L'indirizzo della casa non si scrive mai, nemmeno nei preventivi o "
                                     "negli ordini. Intervento e stato: consegna allo sportello, non alla casa; "
                                     "trasporto fatto dall'associazione con il furgone in due giri. Fatto.",
                                     ["consegna arredi", "acquisto mobili", "indirizzo sportello", "furgone",
                                      "trasporto", "riservatezza indirizzo", "Fondazione Valle Verde"])]},
             {"name": "Montaggio armadi", "who": "volunteer", "stage": "Fatto",
              "description": "", "worklog": [("volunteer", 30, 5.0, "montaggio armadi con Lucia")],
              "notes": [("volunteer", 0, "Sintomo: gli armadi nuovi acquistati con il contributo della Fondazione "
                                         "Valle Verde andavano montati. Causa / contesto: arredi della casa forniti "
                                         "smontati; montaggio fatto da volontarie dell'associazione, registrato nel "
                                         "worklog. Gli arredi (letti e armadi) sono stati scelti con tre preventivi e "
                                         "consegnati allo sportello, poi portati alla casa con il furgone. Seguono il "
                                         "rendiconto alla Fondazione e il ringraziamento pubblico. Intervento e "
                                         "stato: armadi montati. Fatto.",
                                         ["montaggio armadi", "arredi casa", "mobili", "assemblaggio", "volontarie",
                                          "Fondazione Valle Verde"])]},
             {"name": "Rendiconto Valle Verde", "who": "treasurer", "stage": "Da fare", "milestone": "Rendiconto",
              "deadline": 58, "description": "fatture, bonifici, relazione breve. foto?",
              "notes": [("treasurer", 6, "chiedono foto degli arredi: solo interni, niente finestre o vista "
                                         "fuori. chiedere a Marta chi le fa"),
                        ("treasurer", 6, "Sintomo: la Fondazione chiede il rendiconto dell'acquisto degli arredi, con "
                                         "foto. Causa / contesto: rendiconto alla Fondazione Valle Verde entro 90 "
                                         "giorni dalla fine, pena la revoca: fatture, bonifici, breve relazione, tre "
                                         "preventivi; foto solo degli interni, niente finestre né vista esterna. Le "
                                         "spese di progetto si pagano con bonifico, mai in contanti. Intervento e "
                                         "stato: da fare; da decidere chi scatta le foto.",
                                         ["rendiconto Fondazione", "Valle Verde", "fatture e bonifici",
                                          "relazione finale", "foto arredi", "solo interni", "90 giorni"])]},
             {"name": "Bando Valle Verde 2026 seconda sessione (pulmino)", "who": "lead", "stage": "Fatto",
              "description": "per il pulmino. scadenza 30/9",
              "notes": [("lead", 33, "non siamo riuscite: il form chiedeva il bilancio approvato con verbale "
                                     "firmato e il verbale non era scansionato, Paola in ferie. scaduto alle 12"),
                        ("lead", 31, "da ora cartella documenti standard sempre aggiornata. riprovare nel 2027"),
                        ("lead", 31, "Sintomo: la domanda per il pulmino al bando della Fondazione non è partita in "
                                     "tempo. Causa / contesto: il form del portale chiedeva il bilancio approvato con "
                                     "verbale firmato; il verbale non era scansionato e chi lo aveva era in ferie; "
                                     "scadenza 30/9 alle 12. Intervento e stato: scadenza persa; creata la cartella "
                                     "documenti standard sempre aggiornata; riprovare nel 2027. Fatto.",
                                     ["pulmino", "bando Valle Verde", "scadenza persa", "verbale non scansionato",
                                      "bilancio approvato", "documenti standard", "seconda sessione"])]},
             {"name": "Ringraziamento pubblico", "who": "comms", "stage": "Da fare",
              "description": "post di ringraziamento alla Fondazione. senza foto della casa!",
              "notes": [("comms", 0, "Sintomo: si vuole ringraziare pubblicamente la Fondazione Valle Verde per gli "
                                     "arredi della casa. Causa / contesto: post di ringraziamento al finanziatore, "
                                     "senza alcuna foto della casa, nel rispetto della regola sulle foto e della "
                                     "riservatezza del luogo. Le foto passano sempre dalla responsabile comunicazione "
                                     "prima di uscire; si fotografano oggetti, mai luoghi. Il post porta il logo del "
                                     "finanziatore. Intervento e stato: da fare.",
                                     ["ringraziamento pubblico", "post ringraziamento", "Fondazione Valle Verde",
                                      "finanziatore", "niente foto casa", "social"])]},
         ],
         "updates": [
             ("Acquisti fatti", "on_track", 70, 30, "arredi comprati e montati. resta il rendiconto entro fine "
                                                    "dicembre. persa la seconda sessione (pulmino)."),
         ]},
    ],
    "rules": [
        {"name": "Tre preventivi sopra i 1.000 euro", "where": "customer", "who": "lead", "state": "active",
         "severity": "must", "activities": ["reporting"], "section": "operations",
         "keywords": "tre preventivi, offerte, comparazione preventivi, 1.000 euro, acquisti, Fondazione Valle Verde, "
                     "rendiconto",
         "body": "Per la Fondazione ogni acquisto sopra i 1.000 euro ha tre preventivi, da allegare al "
                 "rendiconto."},
    ],
    "documents": [],
    "notes": [
        {"kind": "fact", "where": "customer", "who": "treasurer", "section": "operations",
         "name": "Valle Verde: come funziona",
         "keywords": "Fondazione Valle Verde, bando fondazione, sessioni marzo settembre, portale fondazione, "
                     "rendiconto 90 giorni, revoca contributo, fondazione privata",
         "body": "due sessioni l'anno (marzo e settembre). si fa tutto sul loro portale. rendiconto entro 90 gg "
                 "dalla fine, sennò revocano."},
    ],
}

P_CONVENZIONE = "Convenzione sportello 2026-2027"
COMUNE = {
    "ref": "GIN-COMUNE", "name": "Comune (servizi sociali)", "city": "",
    "projects": [
        {"name": P_CONVENZIONE, "tags": ["sportello", "comune", "convenzione"],
         "description": "<p>Convenzione biennale per lo sportello antiviolenza: rimborso spese 22.000 l'anno, "
                        "relazione semestrale, partecipazione al tavolo della rete territoriale.</p>",
         "milestones": [("Firma convenzione", -300, 300), ("Relazione 1° semestre", -93, 93),
                        ("Relazione 2° semestre", 91, None), ("Rinnovo", 425, None)],
         "tasks": [
             {"name": "Firma convenzione", "who": "lead", "stage": "Fatto", "milestone": "Firma convenzione",
              "description": "", "notes": [("lead", 300, "firmata. 2 anni"),
                                           ("lead", 300, "Sintomo: per il 2026-2027 doveva essere rinnovato l'accordo "
                                                         "con il Comune per lo sportello antiviolenza. Causa / "
                                                         "contesto: convenzione con i servizi sociali del Comune, "
                                                         "durata due anni, con rimborso spese in due tranche dopo "
                                                         "ogni relazione semestrale. Rimborso spese di 22.000 euro "
                                                         "l'anno; il Comune paga di solito con 3-4 mesi di ritardo. "
                                                         "Intervento e stato: convenzione firmata, durata 2 anni. "
                                                         "Fatto.",
                                                         ["convenzione", "Comune", "servizi sociali",
                                                          "sportello antiviolenza", "accordo biennale", "2026-2027",
                                                          "rimborso spese"])]},
             {"name": "Relazione primo semestre", "who": "member", "stage": "Fatto",
              "milestone": "Relazione 1° semestre",
              "description": "solo dati aggregati",
              "notes": [("member", 95, "relazione pronta, dati aggregati come da modello del Comune. il file sta "
                                       "nell'archivio dello sportello, non qui"),
                        ("lead", 93, "mandata via PEC il 31/7"),
                        ("member", 93, "Sintomo: il Comune chiede la relazione del primo semestre della convenzione. "
                                       "Causa / contesto: relazione semestrale con soli dati aggregati secondo il "
                                       "modello del Comune, mai dati di singole persone; condizione per il rimborso "
                                       "della prima tranche. Nessun dato di singole persone o situazioni, come da "
                                       "regola. Intervento e stato: relazione preparata, file conservato "
                                       "nell'archivio dello sportello, inviata via PEC il 31/7. Fatto.",
                                       ["relazione semestrale", "primo semestre", "dati aggregati", "modello Comune",
                                        "convenzione", "PEC", "rendicontazione attività"])]},
             {"name": "Rimborso primo semestre", "who": "treasurer", "stage": "In attesa",
              "description": "fattura/nota di debito mandata ad agosto",
              "notes": [("treasurer", 60, "mandata la nota di debito"),
                        ("treasurer", 14, "ancora niente. sollecito al servizio"),
                        ("treasurer", 14, "Sintomo: il rimborso del primo semestre della convenzione non è ancora "
                                          "arrivato. Causa / contesto: la nota di debito al Comune è stata inviata ad "
                                          "agosto; il Comune paga di solito con 3-4 mesi di ritardo. Il rimborso "
                                          "della convenzione è di 22.000 euro l'anno in due tranche, dopo ciascuna "
                                          "relazione semestrale: tenere la cassa. Intervento e stato: inviato un "
                                          "sollecito al servizio; in attesa del pagamento.",
                                          ["rimborso convenzione", "nota di debito", "pagamento in ritardo",
                                           "sollecito", "prima tranche", "Comune", "liquidità"])]},
             {"name": "Tavolo rete antiviolenza", "who": "lead", "stage": "In corso",
              "description": "ogni secondo giovedì, servizi sociali, consultorio, pronto soccorso, forze dell'ordine",
              "notes": [("lead", 18, "tavolo: si rifà il protocollo di rete entro marzo. ci chiedono una "
                                     "proposta sulla parte accoglienza notturna"),
                        ("lead", 18, "Sintomo: ogni secondo giovedì del mese si riunisce il tavolo della rete "
                                     "antiviolenza con servizi sociali, consultorio, pronto soccorso e forze "
                                     "dell'ordine. Causa / contesto: protocollo di rete territoriale antiviolenza da "
                                     "rinnovare entro marzo. Il tavolo è seguito nell'ambito della convenzione "
                                     "sportello con il Comune. Intervento e stato: all'associazione è stata chiesta "
                                     "una proposta sulla parte di accoglienza notturna. In corso.",
                                     ["tavolo rete antiviolenza", "protocollo di rete", "rete territoriale",
                                      "accoglienza notturna", "servizi sociali", "consultorio", "pronto soccorso",
                                      "forze dell'ordine"])]},
             {"name": "Relazione secondo semestre", "who": "member", "stage": "Da fare",
              "milestone": "Relazione 2° semestre", "deadline": 91, "description": "entro 31/1",
              "notes": [("member", 0, "Sintomo: va preparata la relazione del secondo semestre per il Comune. Causa / "
                                      "contesto: relazione semestrale della convenzione sportello con soli dati "
                                      "aggregati sul modello del Comune; scadenza 31 gennaio; sblocca la seconda "
                                      "tranche del rimborso. Nelle relazioni e nelle mail al Comune mai dati di "
                                      "singole persone o situazioni. La relazione del primo semestre è stata inviata "
                                      "via PEC il 31/7. Intervento e stato: da fare.",
                                      ["relazione semestrale", "secondo semestre", "dati aggregati", "convenzione",
                                       "Comune", "scadenza 31 gennaio", "seconda tranche"])]},
             {"name": "Orari sportello nel sito del Comune", "who": "comms", "stage": "Da fare",
              "description": "sul sito del Comune c'è ancora l'orario vecchio senza il sabato",
              "notes": [("comms", 0, "Sintomo: sul sito del Comune c'è ancora l'orario vecchio dello sportello, senza "
                                     "l'apertura del sabato. Causa / contesto: dal 2026 lo sportello apre anche il "
                                     "sabato 10-12 con il progetto regionale; l'informazione pubblica del Comune non "
                                     "è aggiornata. Orari completi: lunedì 15-19, mercoledì 9-13, venerdì 15-19, "
                                     "sabato 10-12. Intervento e stato: da fare; chiedere al Comune di aggiornare la "
                                     "pagina.",
                                     ["orari sportello", "sito del Comune", "orario vecchio", "apertura sabato",
                                      "aggiornamento pagina", "informazioni pubbliche"])]},
         ],
         "updates": [
             ("Ottobre", "on_track", 40, 15, "relazione 1° semestre inviata, rimborso non ancora arrivato "
                                             "(sollecitato). tavolo: protocollo di rete da rifare entro marzo."),
         ]},
    ],
    "rules": [
        {"name": "Al Comune solo dati aggregati", "where": "customer", "who": "lead", "state": "active",
         "severity": "never", "activities": ["communication", "reporting"], "section": "compliance",
         "keywords": "dati aggregati, relazione al Comune, anonimato, privacy, modello del Comune, statistiche, "
                     "nessun dato personale",
         "body": "Nelle relazioni e nelle mail al Comune mai dati di singole persone o situazioni: solo i numeri "
                 "aggregati del modello del Comune."},
    ],
    "documents": [],
    "notes": [
        {"kind": "fact", "where": "customer", "who": "lead", "section": "profile",
         "name": "Convenzione sportello",
         "keywords": "convenzione sportello, Comune, servizi sociali, rimborso spese 22.000, tranche semestrali, "
                     "ritardo pagamenti, liquidità",
         "body": "2026-2027, rimborso spese 22.000/anno in due tranche dopo ogni relazione semestrale. Il "
                 "Comune paga di solito con 3-4 mesi di ritardo: tenere la cassa."},
    ],
}

CUSTOMERS = [REGIONE, OTTOXMILLE, VALLEVERDE, COMUNE]

# -- the lessons: findings without funder, people, amounts or record numbers ------------------------------------
LESSONS = [
    {"key": "timesheet_mensili", "who": "lead", "state": "active", "tags": ["rendicontazione", "FSE+"],
     "activities": ["reporting"], "title": "Timesheet compilati a fine progetto vengono tagliati",
     "applies_to": "progetti finanziati con fondi europei", "verified": "ottobre 2026",
     "keywords": "timesheet, foglio ore, spese non ammissibili, controllo di primo livello, costi del personale, "
                 "firma responsabile, compilazione mensile, dichiarazione sostitutiva",
     "finding": "In un controllo di primo livello le ore del personale con timesheet compilati tutti insieme a "
                "fine progetto, senza firma del responsabile, sono state considerate non ammissibili.",
     "solution": "Timesheet ogni mese, firmati dalla persona e dalla coordinatrice entro i primi giorni del mese "
                 "dopo. Se è già successo: dichiarazione sostitutiva e agende come prova, ma non è garantito."},
    {"key": "contanti", "who": "lead", "state": "active", "tags": ["rendicontazione"], "activities": ["reporting"],
     "title": "Le spese in contanti non si rendicontano",
     "applies_to": "bandi pubblici", "verified": "ottobre 2026",
     "keywords": "tracciabilità, contanti, pagamento in contanti, spesa non ammissibile, bonifico, carta, "
                 "rendicontazione, compenso",
     "finding": "Un compenso pagato in contanti, con ricevuta regolare, è stato escluso dal rendiconto perché il "
                "pagamento non era tracciabile. Non è recuperabile con integrazioni.",
     "solution": "Solo bonifico o carta per qualsiasi spesa di progetto, anche piccola."},
    {"key": "cup_fatture", "who": "treasurer", "state": "draft", "tags": ["rendicontazione"],
     "activities": ["reporting"], "title": "Fatture senza CUP",
     "applies_to": "", "verified": None,
     "keywords": "CUP, Codice unico di progetto, fatture, dicitura programma, nota di credito, rifatturazione, ordine "
                 "fornitore, spese tagliate",
     "finding": "fatture senza CUP e senza dicitura del programma tagliate al controllo",
     "solution": "chiedere al fornitore il CUP già nell'ordine. se manca: nota di credito e rifattura"},
    {"key": "documenti_standard", "who": "lead", "state": "active", "tags": ["bandi"], "activities": ["funding"],
     "title": "Una scadenza persa per un verbale non scansionato",
     "applies_to": "domande di contributo online", "verified": "settembre 2026",
     "keywords": "scadenza persa, verbale non scansionato, documenti standard, bilancio approvato, cartella "
                 "condivisa, domanda online, bando",
     "finding": "Una domanda online non è partita perché il portale chiedeva il bilancio approvato con il "
                "verbale firmato e la persona che lo aveva era assente il giorno della scadenza.",
     "solution": "Una cartella condivisa di documenti standard (statuto, bilancio e verbale, curriculum "
                 "dell'ente, documento del legale rappresentante) aggiornata subito dopo l'assemblea."},
    {"key": "firma_digitale", "who": "lead", "state": "active", "tags": ["bandi"], "activities": ["funding"],
     "title": "Controllare la firma digitale prima di un bando",
     "applies_to": "bandi con invio via PEC", "verified": "ottobre 2026",
     "keywords": "firma digitale, PEC, firma scaduta, legale rappresentante, promemoria scadenza, candidatura, bando, "
                 "rinnovo",
     "finding": "La firma digitale del legale rappresentante era scaduta da settimane e ce ne siamo accorte "
                "solo preparando una candidatura: rinnovarla richiede un appuntamento.",
     "solution": "Promemoria un mese prima della scadenza della firma; verificarla appena esce un bando."},
    {"key": "requisito_esperienza", "who": "lead", "state": "active", "tags": ["bandi"], "activities": ["funding"],
     "title": "Leggere i requisiti di esperienza prima di tutto",
     "applies_to": "avvisi di co-progettazione con enti del terzo settore", "verified": "ottobre 2026",
     "keywords": "requisiti di esperienza, co-progettazione, raggruppamento, capofila, centro di costo, lettera di "
                 "adesione, rete territoriale, avviso pubblico",
     "finding": "Negli avvisi di co-progettazione il requisito di esperienza pluriennale negli ambiti precisi "
                "dell'avviso esclude chi lavora su temi vicini; in un raggruppamento solo la capofila diventa "
                "partner e centro di costo.",
     "solution": "Valutare subito requisiti di esperienza e ruolo nel raggruppamento; se non ci sono, offrire una "
                 "lettera di adesione alla rete territoriale di chi si candida."},
    {"key": "foto_casa", "who": "lead", "state": "active", "tags": ["comunicazione", "casa"],
     "activities": ["communication"], "title": "Una foto di ringraziamento può mostrare un luogo protetto",
     "applies_to": "social", "verified": "settembre 2026",
     "keywords": "foto, luogo protetto, casa rifugio, post social, riservatezza, controllo foto, rimozione "
                 "condivisioni, donazioni",
     "finding": "Una foto di un carico di donazioni, mandata da una volontaria, mostrava la facciata di un luogo "
                "che deve restare riservato. Tolta in meno di un'ora, ma era già stata condivisa.",
     "solution": "Ogni foto passa da una sola persona prima della pubblicazione; si fotografano oggetti in "
                 "magazzino, mai luoghi; chiedere subito a chi ha condiviso di rimuovere."},
    {"key": "volontarie_assicurazione", "who": "lead", "state": "active", "tags": ["volontariato"],
     "activities": [], "title": "Volontarie nuove: assicurazione prima dell'affiancamento",
     "applies_to": "", "verified": None,
     "keywords": "assicurazione volontarie, copertura assicurativa, comunicazione nominativi, affiancamento, nuove "
                 "volontarie, patto di riservatezza, polizza infortuni",
     "finding": "La copertura assicurativa di una volontaria parte solo dal giorno dopo la comunicazione del "
                "nominativo: i turni in affiancamento prima di quella data sono scoperti.",
     "solution": "Comunicare i nominativi alla fine del corso, prima del primo turno, insieme al patto di "
                 "riservatezza."},
    {"key": "caldaia", "who": "member", "state": "draft", "tags": ["casa"], "activities": [],
     "title": "caldaia: non resettare più volte",
     "applies_to": "", "verified": None,
     "keywords": "caldaia, reset, blocco caldaia, pressione bassa, tecnico, riscaldamento, guasto",
     "finding": "resettare la caldaia più volte non serve se la pressione è bassa, rischi di peggiorare",
     "solution": "un reset, controllare la pressione, poi tecnico"},
    {"key": "taglio_comunicazione", "who": "lead", "state": "active", "tags": ["bandi", "rendicontazione"],
     "activities": ["funding"], "title": "Le commissioni tagliano le spese di comunicazione alte",
     "applies_to": "programmi regionali per il terzo settore", "verified": "luglio 2026",
     "keywords": "spese di comunicazione, taglio contributo, graduatoria, piano finanziario, variazione di budget, "
                 "autorizzazione, commissione di valutazione",
     "finding": "In una graduatoria il contributo è stato ridotto togliendo la parte di comunicazione, "
                "giudicata sproporzionata rispetto alle attività.",
     "solution": "Tenere la comunicazione sotto una quota modesta del piano e legarla ad attività precise; dopo "
                 "un taglio, una variazione di budget va chiesta e autorizzata prima di spendere."},
    {"key": "pec_registro", "who": "lead", "state": "active", "tags": ["RUNTS", "adempimenti"],
     "activities": ["reporting"], "title": "Gli esiti del registro arrivano sulla PEC registrata",
     "applies_to": "enti iscritti al registro unico del terzo settore", "verified": "luglio 2026",
     "keywords": "pec, notifiche, PEC, posta elettronica certificata, notifiche RUNTS, deposito bilancio respinto, "
                 "PEC dell'ente, scadenza, commercialista, raccolte fondi",
     "finding": "Un deposito del bilancio respinto per un errore del file è stato rifatto tardi perché la "
                "notifica era arrivata sulla PEC di una professionista esterna, assente in quel periodo; il "
                "deposito è andato oltre la scadenza.",
     "solution": "Registrare la PEC propria dell'ente (ora obbligatoria) e caricare il bilancio qualche settimana "
                 "prima della scadenza, con rendiconti delle raccolte fondi nello stesso file e la quadratura "
                 "di cassa e banca controllata."},
    {"key": "cambio_legale_rappresentante", "who": "treasurer", "state": "draft", "tags": ["RUNTS"],
     "activities": [], "title": "cambio presidente senza firma digitale",
     "applies_to": "", "verified": None,
     "keywords": "cambio presidente, firma digitale, delega telematica, legale rappresentante, variazione cariche, "
                 "SPID, trenta giorni, centro servizi volontariato",
     "finding": "la nuova presidente non ha la firma digitale e la variazione delle cariche va fatta entro trenta "
                "giorni",
     "solution": "delega telematica del legale rappresentante a chi segue il registro, conferita online; "
                 "verificare con il centro servizi se basta lo SPID"},
]

# The question sets live in demo/questions.json (sets A, B and passaggi): the loader resolves their titles.
EVAL = []
