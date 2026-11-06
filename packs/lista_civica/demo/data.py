# Copyright 2026 Daniele Lucarelli
# License CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/).
"""The demo of the pack lista_civica: «Terni 2027», an invented civic list of Terni, with its press review.

Everything is invented except the public acts and the verified public facts. Invented: the list itself, its people
(coordinator, spokesperson, press office, leads of the thematic groups, stall volunteers, the election agent), their
meetings, programme drafts, events, stalls, social media, signature collection, the committees and associations they
deal with, the internal minutes of the coalition table (with invented delegates, never named real politicians), the
press about the list's own activity (only invented outlets, each marked «testata fittizia»), the rules, lessons and
internal documents. Real places of Terni appear as places only. No person served, no case, no address.

The verified layer (research of 2026-11-01) is the only real content: public facts about the municipal crisis, the
Regione and the local issues, each written neutrally with its source link and date, as facts of the organisation and
as press and video cards. Real persons appear only as those facts state; no event, quotation, position or opinion
of a real person or party is invented. The four councillors who left the majority are a group, never named. Press
cards keep the outlet, the date, the headline and the link, with no copied article text; video cards keep link,
channel and title, with no transcript (the segments are left to fill: the videos were not watched). The normative
texts (demo/texts/*.md, public acts converted with Docling: the Interior Ministry 2026 instructions for municipal
candidacies, L. 81/1993, L. 53/1990, L. 515/1993, L. 96/2012, L. 28/2000, L. 212/1956, AGCOM 122/24/CONS and its
2026 notice, the Garante 2019 provision on political propaganda) are real and public.

Two layers of writing live together here. The raw one is how political volunteers write in a hurry, not for search:
WhatsApp-like chatter, nicknames («il sindaco», «il patron», «quelli di Dimensione», «i quattro», «la Regione», «il
tavolo»), abbreviations, first names, days of the week, missing context. The curated one was written by an agent
that did not see the questions, following the writing strategies of the memory: a searchable session note on every
task, with its keywords, the keywords of rules, facts, procedures, lessons and documents (synonyms, aliases, the
Italian and the English term), the summaries of the documents, and the cards of the external sources (SOURCES: the
channels the list follows, the labels, one card per clipping). The questions of demo/questions.json were written
against this material (the sets A, B, "persona" and "fonti"), and the demo is the layer that measured best.

Loaded by <core>/setup/load-demo.sh through <core>/scripts/load_demo.py, only into the databases of DATABASES; the
hub needs texo_sources and texo_sources_vector for the cards. Days are relative to the day of the load.
"""

DATABASES = ("scenario-lista",)
TOKEN_NAME = "Terni 2027 demo"
TOKEN_DAYS = 30

COMPANY = {"name": "Terni 2027", "email": "info@terni2027.example", "website": "https://terni2027.example"}

# role: (name, login, hub group). The coordinator is the lead; the spokesperson is a hub lead too; everybody else
# (press office, leads of the thematic groups, the stall coordinator, the election agent) is a member.
USERS = {
    "admin": ("Amministratore Terni 2027", None, "texo.group_texo_admin"),
    "lead": ("Francesca Ottaviani", "coordinamento@terni2027.example", "texo.group_texo_lead"),
    "portavoce": ("Michele Santarelli", "portavoce@terni2027.example", "texo.group_texo_lead"),
    "stampa": ("Giada Pernazza", "stampa@terni2027.example", "texo.group_texo_member"),
    "sociale": ("Luisa Pacifici", "luisa.pacifici@terni2027.example", "texo.group_texo_member"),
    "ambiente": ("Tommaso Borghetti", "tommaso.borghetti@terni2027.example", "texo.group_texo_member"),
    "sanita": ("Annamaria Corradi", "annamaria.corradi@terni2027.example", "texo.group_texo_member"),
    "lavoro": ("Sergio Tiberi", "sergio.tiberi@terni2027.example", "texo.group_texo_member"),
    "banchetti": ("Matteo Coletti", "volontari@terni2027.example", "texo.group_texo_member"),
    "mandatario": ("Paolo Antonelli", "mandatario@terni2027.example", "texo.group_texo_member"),
}
WORK_GROUPS = ("project.group_project_user", "hr_timesheet.group_hr_timesheet_user")
TEAM = ("lead", "portavoce", "stampa", "sociale", "ambiente", "sanita", "lavoro", "banchetti", "mandatario")

# The stages: the last one of each list is folded (done).
DELIVERY_STAGES = ["Da fare", "In corso", "In attesa", "Fatto"]
TICKET_STAGES = ["Nuovo", "In lavorazione", "In attesa", "Risolto", "Chiuso"]
HOME_STAGES = ["Da fare", "In corso", "Fatto", "Annullato"]
RASSEGNA_STAGES = ["Da schedare", "In lavorazione", "Schedato"]
TICKET_TAG = "ticket"
ASSISTANCE = "Assistenza {name}"

# -- the cloud folder of the procedures and the generated PDFs ----------------------------------------------
SOURCES_FOLDER = "https://drive.terni2027.example/procedure"
# the organisation's own vademecum, a generated PDF (the document "vademecum_gazebo")
PROCEDURE_PDF = ("vademecum-gazebo.pdf", "Vademecum del gazebo (rev. ottobre)", [
    "1. Si monta in due, mai da soli. Chiavi del furgoncino: Teo.",
    "2. Sul tavolo: volantini del quartiere, modulo contatti con consenso a parte, cassetta chiusa.",
    "3. Contatti solo sul modulo cartaceo con la firma del consenso. Mai foto ai moduli, mai whatsapp.",
    "4. Offerte: ricevuta dal blocchetto numerato, sopra i 50 euro nome e cognome.",
    "5. Giornalisti: gentili, ma il numero e' quello di Michele. Nessuna dichiarazione.",
    "6. Foto: niente bambini riconoscibili. Le foto vanno a Giada, non si postano da soli.",
    "7. A fine turno: moduli in busta chiusa a Teo, cassetta a Paolo, foto nella cartella condivisa.",
])
# the PDFs attached to a task ("attachment": key)
ATTACHMENTS = {
    "stage_report": ("preventivo-tipografia.pdf", "Preventivo stampa volantini (fittizio)", [
        "Volantino A5 fronte/retro, carta 115 g patinata opaca.",
        "5.000 copie: 210 euro + IVA. 10.000 copie: 320 euro + IVA.",
        "Consegna 3 giorni lavorativi dal pdf definitivo approvato.",
    ]),
}

# -- the projects of the list (no customers: the list works on projects of its own) ---------------------------
P_CASA = "Casa, sociale e giovani"
P_AMB = "Ambiente, aria e rifiuti"
P_SAN = "Sanità e ospedale"
P_LAV = "Lavoro, acciaieria e sviluppo"
P_PART = "Partecipazione, trasparenza e opposizione"
P_CAMP = "Campagna e organizzazione"
P_RASS = "Rassegna stampa e video"
P_ADEMP = "Adempimenti elettorali"

NORMATTIVA = "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:"

# -- the organisation ----------------------------------------------------------------------------------------
ANSA_2610 = ("https://www.ansa.it/umbria/notizie/2026/10/26/allopposizione-quattro-consiglieri-della-maggioranza-"
             "bandecchi-al-comune-di-terni_20b588a7-5ed9-4b69-b965-c64c46c2be2a.html")
UMBRIA24_2710 = ("https://www.umbria24.it/terni/crisi-politica-terni-centrodestra-invoca-dimissioni-dei-consiglieri-"
                 "m5s-chiede-sfiducia-a-bandecchi/")
SETTEGIORNI_2810 = "https://www.umbriasettegiorni.it/terni-centrosinistra-pronto-a-sfiduciare-bandecchi/"
QDU_2910 = ("https://www.quotidianodellumbria.it/terni/terni-il-centrosinistra-prepara-la-sfiducia-bandecchi-non-"
            "avranno-mai-17-voti/")
UMBRIAON_3110 = ("https://www.umbriaon.it/terni-fdi-attacca-pd-e-opposizioni-tante-parole-ma-mancano-le-firme-per-"
                 "cacciare-bandecchi/")
WIKI_2023 = "https://it.wikipedia.org/wiki/Elezioni_amministrative_in_Italia_del_2023"
GIORNALE_AP = ("https://www.ilgiornale.it/news/interni/alli-e-bandecchi-alternativa-popolare-e-dimensione-andranno-"
               "2593494.html")
BROCARDI_52 = "https://www.brocardi.it/testo-unico-enti-locali/parte-i/titolo-iii/capo-i/art52.html"
CONVOCAZIONE = "https://www.comune.terni.it/system/files/documenti/70023%20convocazione%205.5.pdf"
SKY_2023 = "https://tg24.sky.it/cronaca/2023/08/31/rissa-consiglio-comunale-terni-stefano-bandecchi-indagato"
LENTE_2023 = "https://lentepubblica.it/personale-e-previdenza/terni-sindaco-insulta-segretario/"
SKY_2024 = "https://tg24.sky.it/cronaca/2024/02/08/stefano-bandecchi-dimissioni-sindaco-terni"
ESPRESSO_2025 = ("https://lespresso.it/c/politica/2025/9/29/contestazione-bandecchi-terni-gaza-bambini-morti-cosa-e-"
                 "successo/57223")
PAGELLA_2024 = "https://pagellapolitica.it/articoli/centrosinistra-vinto-elezioni-umbria-proietti"
CONSIGLIO_ERP = "https://consiglio.regione.umbria.it/node/81922/printable/pdf"
RENEWABLE = ("https://www.renewablematter.eu/umbria-circolare-53-articoli-per-uscire-dalle-discariche-ma-strada-in-"
             "salita")
QSANITA = "https://www.quotidianosanita.it/?p=153129"
MIMIT_AST = ("https://www.mimit.gov.it/it/notizie-stampa/ast-terni-urso-mimit-ha-mantenuto-impegni-assunti-ora-"
             "monitorare-attuazione-accordo-programma")
ANSA_STADIO = ("https://www.ansa.it/umbria/notizie/2026/09/10/bandecchi-annuncia-che-il-progetto-stadio-clinica-a-"
               "terni-si-fara_75a5927f-4c2f-403e-95f8-973d6a00b9c1.html")
CALCIOFIN = "https://www.calcioefinanza.it/?p=223447"
NAZIONE_TERNANA = "https://www.lanazione.it/umbria/cronaca/nuova-ternana-tifosi-spaccati-e-32458a49"
NAZIONE_PM10 = "https://www.lanazione.it/umbria/cronaca/qualita-dellaria-nelle-nostre-citta-4808fe3b"

ORGANISATION = {
    "documents": [
        {"key": "vademecum_gazebo", "name": "Vademecum del gazebo (rev. ottobre)",
         "summary": "Vademecum interno, revisione di ottobre, con le regole del turno al gazebo della lista: si "
                    "sta in due, i contatti si raccolgono solo sul modulo con la casella del consenso separata, le "
                    "offerte si prendono con ricevuta numerata. Ai giornalisti si dà il numero del portavoce e le "
                    "foto passano solo dall'ufficio stampa. È il testo usato nella formazione dei volontari e "
                    "richiamato dalla procedura del turno al gazebo.",
         "pdf": PROCEDURE_PDF, "keep_text": True,
         "keywords": "vademecum gazebo, turno gazebo, banchetto, modulo contatti, consenso, offerte con ricevuta, "
                     "portavoce, formazione volontari"},
        {"key": "carta_valori", "name": "Carta dei valori T27",
         "summary": "Carta dei valori approvata dall'assemblea costitutiva del 20/9: Terni 2027 è una lista "
                    "civica, non un partito, sta nel centrosinistra e lavora al tavolo di coalizione per un "
                    "programma e un candidato sindaco comuni. Si impegna ad ascoltare i quartieri e a scrivere il "
                    "programma con comitati, associazioni e lavoratori, facendo un'opposizione dura ma documentata "
                    "alla giunta. Esclude insulti, frasi inventate, foto rubate e contatti presi senza consenso: "
                    "ogni affermazione sul sindaco e sulla giunta ha fonte e data.",
         "url": "https://drive.terni2027.example/statuto/carta-dei-valori", "keep_text": True,
         "text": "## Terni 2027 - carta dei valori (approvata assemblea 20/9)\n\n"
                 "Siamo una lista civica, non un partito. Stiamo nel centrosinistra e lavoriamo al tavolo con la "
                 "coalizione per un programma comune e un candidato sindaco comune.\n\n"
                 "Cosa facciamo: ascolto nei quartieri, programma scritto con chi vive i problemi (comitati, "
                 "associazioni, lavoratori), opposizione dura ma documentata alla giunta.\n\n"
                 "Cosa non facciamo: insulti, frasi inventate, foto rubate, liste di contatti prese chissà dove. "
                 "Ogni cosa che diciamo sul sindaco e sulla giunta ha una fonte e una data.\n",
         "keywords": "carta dei valori, Terni 2027, T27, lista civica, centrosinistra, assemblea costitutiva, "
                     "opposizione documentata, principi"},
    ],
    "rules": [
        {"name": "Mai virgolettati inventati", "severity": "never", "activities": ["communication"],
         "section": "operations", "keywords": "citazioni, virgolette, virgolettati, frasi inventate, fonte, link, "
                      "dichiarazioni attribuite, fake quote",
         "body": "Nessuna frase tra virgolette attribuita a qualcuno se non c'è il link a dove l'ha detta. Vale "
                 "per sindaco, giunta, alleati, chiunque. Neanche «più o meno ha detto così»."},
        {"name": "Sul sindaco sempre fonte e data", "severity": "must", "activities": ["communication", "analysis"],
         "section": "operations",
         "body": "Ogni cosa che scriviamo o diciamo sul sindaco (e sulla giunta) porta testata o atto, data e "
                 "link. Senza fonte non esce: né post, né volantino, né intervento al gazebo.",
         "keywords": "il sindaco, Bandecchi, giunta, fonte e data, link, verifica delle fonti, fact checking"},
        {"name": "Niente contatti presi dai social", "severity": "never", "activities": ["campaign", "communication"],
         "section": "compliance",
         "body": "Non si copiano numeri, mail o nomi da gruppi facebook, commenti, liste whatsapp o elenchi "
                 "telefonici per mandare materiale della lista. Si usano solo i contatti dati a noi con il "
                 "consenso (e le liste elettorali, nei limiti del Garante).",
         "keywords": "contatti dai social, gruppi Facebook, elenchi telefonici, liste WhatsApp, consenso, "
                      "privacy, Garante privacy, spam"},
        {"name": "Consenso separato per i contatti del gazebo", "severity": "must", "activities": ["campaign"],
         "section": "compliance",
         "body": "Chi lascia il numero o la mail al gazebo firma il consenso sul modulo, in una casella sua, "
                 "distinta dalla firma per la lista. Senza quella casella il contatto non entra nel foglio.",
         "keywords": "consenso separato, casella del consenso, modulo contatti, gazebo, privacy, GDPR, foglio "
                      "contatti"},
        {"name": "Coi giornalisti parla il portavoce", "severity": "must", "activities": ["communication"],
         "section": "operations",
         "body": "Interviste, dichiarazioni, risposte a cronisti anche «solo per capire»: solo Michele, o chi "
                 "lui indica caso per caso. Gli altri danno il suo numero.",
         "keywords": "portavoce, giornalisti, cronisti, interviste, dichiarazioni alla stampa, rapporti con la "
                      "stampa"},
        {"name": "Non si copiano gli articoli", "severity": "never", "activities": ["communication", "press"],
         "section": "compliance",
         "body": "Nella rassegna e nei gruppi si mette la scheda: testata, data, titolo, link e due righe nostre. "
                 "Mai il testo intero dell'articolo, mai pdf delle pagine del giornale.",
         "keywords": "articoli copiati, diritto d'autore, copyright, rassegna stampa, scheda di rassegna, pdf dei "
                      "giornali"},
        {"name": "Video solo come scheda", "severity": "never", "activities": ["press"], "section": "compliance",
         "body": "Non si scaricano video di altri e non si tirano fuori trascrizioni automatiche. Si archivia il "
                 "link con canale, titolo, data e i minuti che ci interessano, scritti da chi lo ha visto.",
         "keywords": "scheda video, download video, trascrizioni automatiche, YouTube, minuti, canale, diritto "
                      "d'autore"},
        {"name": "Posizioni degli alleati solo da fonti pubbliche", "severity": "must",
         "activities": ["communication", "analysis"], "section": "operations",
         "body": "Nei nostri testi la posizione di un partito alleato è solo quella che ha detto in pubblico "
                 "(con fonte). Quello che si dice al tavolo resta nei nostri verbali interni e non si attribuisce "
                 "a nessuno fuori.",
         "keywords": "alleati, coalizione, tavolo, verbali interni, posizioni dei partiti, fonti pubbliche, "
                      "riservatezza"},
        {"name": "Privati negli articoli non si schedano", "severity": "never", "activities": ["press"],
         "section": "compliance",
         "body": "Le persone private che compaiono in un articolo (testimoni, residenti, parenti) non entrano "
                 "nelle schede per nome. Si schedano persone pubbliche, enti, luoghi, atti.",
         "keywords": "persone private, privacy, testimoni, residenti, nomi nelle schede, persone pubbliche, "
                      "rassegna stampa"},
    ],
    "notes": [
        {"kind": "fact", "section": "profile", "name": "Chi siamo",
         "body": "Lista civica Terni 2027: rete di comitati e associazioni da giugno 2026, lista dall'assemblea del "
                 "20/9 "
                 "(saletta di Borgo Bovio). "
                 "Sta nel centrosinistra, per le comunali che arrivano se il consiglio va sciolto (primavera 2027). "
                 "Circa 60 iscritti, 25 attivi. Gruppi: casa/sociale/giovani, ambiente, sanità, lavoro, "
                 "partecipazione, campagna. Più rassegna e adempimenti.",
         "keywords": "Terni 2027, lista civica, T27, centrosinistra, comitati e associazioni, gruppi tematici, "
                      "assemblea del 20/9, comunali 2027"},
        {"kind": "fact", "section": "profile", "name": "Chi fa cosa",
         "body": "Fra (Francesca) coordina. Michele portavoce. Giada ufficio stampa e social. Luisa casa e "
                 "sociale. Tommy ambiente. Annamaria sanità (ex caposala). Sergio lavoro (ex RSU). Teo gazebo e "
                 "volontari. Paolo commercialista, fa il mandatario quando si parte.",
         "keywords": "organigramma, ruoli, coordinatrice, portavoce, ufficio stampa, mandatario, referenti dei "
                      "gruppi, responsabile gazebo"},
        {"kind": "fact", "section": "operations", "name": "Social e canali",
         "keywords": "instagram, facebook, Facebook, Instagram, terni2027, canale WhatsApp, gruppo T27 volontari, "
                      "password social, canali social",
         "body": "pagina fb e ig «terni2027», canale whatsapp pubblico, gruppo T27 volontari (interno). password "
                 "le ha Giada, backup Fra."},
        {"kind": "fact", "section": "sector", "name": "Comunali 2023: come è andata",
         "body": "1° turno 14-15/5/2023, ballottaggio 28-29/5. Bandecchi eletto 54,62% contro Masselli (cdx) "
                 "45,38%. Al 1° turno Kenny (csx) 21,94%, Fiorelli (M5S) 10,82%. Consiglio: 32 seggi, 20 alla "
                 "coalizione del sindaco, 7 cdx, 4 csx (3 PD), 1 M5S. Fonte: " + WIKI_2023 + " (letta 1/11/2026)",
         "keywords": "comunali 2023, ballottaggio, Bandecchi, Masselli, Kenny, Fiorelli, risultati elettorali, "
                      "seggi del consiglio"},
        {"kind": "fact", "section": "sector", "name": "AP e Dimensione: strade separate",
         "body": "10/01/2026: Alternativa Popolare e Dimensione (il partito fondato da Bandecchi) annunciano "
                 "percorsi separati. Fonte Il Giornale: " + GIORNALE_AP,
         "keywords": "Alternativa Popolare, AP, Dimensione, Bandecchi, partito del sindaco, percorsi separati, Il "
                      "Giornale"},
        {"kind": "fact", "section": "sector", "name": "Consiglio del 26/10: i quattro passano all'opposizione",
         "keywords": "Per Terni, i quattro, cambio di casacca, consiglieri all'opposizione, crisi di maggioranza, "
                      "bilancio consolidato, sfiducia ai presidenti di commissione, ANSA",
         "body": "ANSA 26/10/2026: quattro consiglieri lasciano la maggioranza e fanno il gruppo «Per Terni» "
                 "all'opposizione. In aula la maggioranza presenta una sfiducia contro due di loro, presidenti di "
                 "commissione: non votata, rimessa a un parere del Ministero dell'Interno. Nella stessa seduta "
                 "passa il bilancio consolidato: 15 sì, 9 no, 6 astenuti. Fonte: " + ANSA_2610 + "\n"
                 "NB: i nomi dei quattro non li scriviamo, per noi sono «i quattro di Per Terni»."},
        {"kind": "fact", "section": "sector", "name": "27/10: notaio e firme",
         "body": "Umbria24 27/10/2026: FdI, FI, Lega e UdC raccolgono dal notaio le dimissioni contestuali "
                 "(TUEL art. 141: ne servono 17 su 32, insieme); firmano in sei. Stesso giorno il M5S avvia la "
                 "raccolta firme per la sfiducia (13 per presentarla, 17 voti per approvarla). " + UMBRIA24_2710,
         "keywords": "dimissioni contestuali, notaio, TUEL art. 141, 17 consiglieri, centrodestra, FdI, raccolta "
                      "firme sfiducia, M5S, Umbria24"},
        {"kind": "fact", "section": "sector", "name": "Sfiducia: dove siamo al 31/10",
         "body": "28/10 (Umbria Settegiorni): PD, M5S, AVS, PSI, Casa Riformista-IV e Rifondazione d'accordo per "
                 "promuovere o sostenere una mozione. Al 31/10 non risulta depositata. 31/10 nota di FdI "
                 "(UmbriaON, fonte di parte): «tante parole ma mancano le firme per cacciare Bandecchi».\n"
                 "Il testo lo scrivono i gruppi in consiglio, noi in aula non ci siamo: nessuna bozza nostra. "
                 "Fonti: " + SETTEGIORNI_2810 + " ; " + UMBRIAON_3110,
         "keywords": "mozione di sfiducia, sfiducia a Bandecchi, centrosinistra, PD, M5S, AVS, nota FdI, Umbria "
                      "Settegiorni, mandare a casa il sindaco"},
        {"kind": "fact", "section": "sector", "name": "Il sindaco sui 17 voti (29/10)",
         "body": "Quotidiano dell'Umbria 29/10/2026: il sindaco risponde «Per sfiduciarmi servono 17 voti e loro "
                 "non ci arriveranno mai», dice di avere 15 consiglieri e indica il bilancio di previsione come "
                 "prossima prova. " + QDU_2910,
         "keywords": "il sindaco, Bandecchi, 17 voti, 15 consiglieri, bilancio di previsione, Quotidiano "
                      "dell'Umbria, sfiducia"},
        {"kind": "fact", "section": "sector", "name": "Come funziona la sfiducia (TUEL 52)",
         "body": "mozione motivata firmata da 2/5 dei consiglieri assegnati (13), discussa tra 10 e 30 gg dal "
                 "deposito, appello nominale, passa con la maggioranza assoluta (17). Se passa: scioglimento e "
                 "commissario (art. 141). " + BROCARDI_52,
         "keywords": "TUEL art. 52, mozione di sfiducia, 2/5 dei consiglieri, 13 firme, maggioranza assoluta, "
                      "appello nominale, scioglimento, commissario"},
        {"kind": "fact", "section": "sector", "name": "Quando si vota se cade",
         "body": "L. 182/1991 art. 2: i consigli da rinnovare per cause diverse dalla scadenza votano nel turno "
                 "ordinario (15 aprile-15 giugno) se le condizioni si verificano entro il 24 febbraio. Scioglimento "
                 "entro fine febbraio 2027 = voto in primavera 2027. Deduzione nostra dalla legge, non una "
                 "previsione dei giornali.",
         "keywords": "L. 182/1991, turno ordinario, 24 febbraio, elezioni anticipate, scioglimento del consiglio, "
                      "voto in primavera 2027, data del voto"},
        {"kind": "fact", "section": "sector", "name": "Chi sta all'opposizione in consiglio",
         "body": "Dalla convocazione del 5/5/2025: gruppi di opposizione FdI, Forza Italia, Misto, PD, M5S. "
                 "Presidente del consiglio comunale Sara Francescangeli. " + CONVOCAZIONE + "\n"
                 "Da ottobre 2026 c'è anche il gruppo Per Terni (vedi consiglio del 26/10). Composizione attuale "
                 "dei gruppi: non verificata.",
         "keywords": "gruppi consiliari, opposizione in consiglio, FdI, Forza Italia, PD, M5S, gruppo Misto, Per "
                      "Terni, presidente del consiglio comunale"},
        {"kind": "fact", "section": "sector", "name": "Candidato sindaco csx: ancora nessuno",
         "body": "al 1/11/2026 nessun candidato sindaco del centrosinistra annunciato. al tavolo: da definire.",
         "keywords": "candidato sindaco, centrosinistra, csx, candidatura, tavolo di coalizione, nomi da definire"},
        {"kind": "fact", "section": "sector", "name": "Regionali 2024",
         "body": "17-18/11/2024: Stefania Proietti 51,1%, Donatella Tesei 46,2%, affluenza 52,3%. Coalizione PD, "
                 "M5S, AVS, +Europa, Azione, IV. " + PAGELLA_2024,
         "keywords": "regionali 2024, elezioni regionali Umbria, Proietti, Tesei, affluenza, campo largo, Pagella "
                      "Politica"},
        {"kind": "fact", "section": "sector", "name": "Regione: legge case popolari cambiata in commissione",
         "body": "28/01/2026 la III commissione approva le modifiche alla LR 23/2003 sull'ERP: via la residenza "
                 "minima in Umbria, punteggi per disabilità, donne vittime di violenza tra le emergenze, "
                 "autorecupero, protocolli con Comuni, ATER e Terzo settore. " + CONSIGLIO_ERP,
         "keywords": "ERP, LR 23/2003, case popolari, edilizia residenziale pubblica, III commissione, residenza "
                      "minima, ATER, autorecupero"},
        {"kind": "fact", "section": "sector", "name": "Regione: rifiuti e ddl Umbria Circolare",
         "body": "21/04/2026 ddl «Umbria Circolare» (53 articoli): ambito unico regionale, tariffa puntuale, "
                 "discarica dal 30% al 20% entro il 2030. La giunta regionale: «nessun inceneritore»; il "
                 "termovalorizzatore del piano 2023 fermato, AURI sospende la procedura. " + RENEWABLE,
         "keywords": "Umbria Circolare, ddl rifiuti, inceneritore, termovalorizzatore, AURI, tariffa puntuale, "
                      "discarica, ambito unico regionale"},
        {"kind": "fact", "section": "sector", "name": "Nuovo Santa Maria: tre siti nel Docfap",
         "body": "Docfap presentato a fine luglio 2026 con tre alternative: Sabbione, Campitello, Colle Obito. "
                 "Prima della scelta è previsto un dibattito pubblico. Nessun sito deciso. " + QSANITA,
         "keywords": "nuovo ospedale, Santa Maria, Docfap, Sabbione, Campitello, Colle Obito, dibattito pubblico, "
                      "sito ospedale"},
        {"kind": "fact", "section": "sector", "name": "Acciaieria: accordo di programma firmato",
         "keywords": "AST, Arvedi, acciaieria, accordo di programma, 557 milioni, MIMIT, comitato esecutivo, costi "
                      "dell'energia",
         "body": "Accordo di programma AST firmato a giugno 2025: 557 milioni di investimenti entro il 2028. "
                 "28/09/2026 primo comitato esecutivo al MIMIT (tema: costi dell'energia). Quindi la firma c'è "
                 "già, ora è fase di attuazione e monitoraggio. " + MIMIT_AST},
        {"kind": "fact", "section": "sector", "name": "Stadio-clinica",
         "body": "ANSA 10/09/2026: la Regione comunica che il Comune rinuncia al Consiglio di Stato contro la "
                 "sentenza del TAR favorevole alla Regione; il sindaco dice che il progetto «si farà». "
                 + ANSA_STADIO,
         "keywords": "stadio-clinica, stadio, clinica, TAR, Consiglio di Stato, Regione Umbria, Bandecchi, ANSA"},
        {"kind": "fact", "section": "sector", "name": "Ternana",
         "body": "liquidazione giudiziale (udienza 17/04/2026). Nasce la «Nuova Ternana 1925» in serie D, "
                 "promossa dal sindaco (La Nazione 29/07/2026). " + CALCIOFIN + " ; " + NAZIONE_TERNANA,
         "keywords": "Ternana, Nuova Ternana 1925, liquidazione giudiziale, fallimento, serie D, tifosi, Bandecchi"},
        {"kind": "fact", "section": "sector", "name": "Smog: i numeri ARPA che abbiamo",
         "body": "Area di Terni: 30-40 superamenti l'anno del limite giornaliero delle polveri sottili (PM10), la "
                 "più inquinata dell'Umbria; Maratta 41 nel 2023. Dati ARPA riportati da La Nazione il 04/01/2025: "
                 + NAZIONE_PM10 + "\nDati 2024 e 2025 per stazione: non li abbiamo ancora, Tommy li chiede ad "
                 "ARPA. Fino ad allora in pubblico si cita il 2023 con la fonte.",
         "keywords": "smog, PM10, polveri sottili, ARPA, superamenti, Maratta, qualità dell'aria, La Nazione"},
        {"kind": "fact", "section": "operations", "name": "Sindaco e salute: le leve del Comune",
         "body": "quando ci dicono «la sanità è roba della Regione»:\n1) il sindaco è autorità sanitaria locale "
                 "(TUEL art. 50: ordinanze urgenti di igiene e sanità)\n2) sta nella conferenza dei sindaci che dà "
                 "pareri sulla programmazione e sul direttore generale (d.lgs 502/92)\n3) dove si fa il nuovo "
                 "ospedale passa anche dall'urbanistica del Comune\n4) sociale e sanitario si integrano nel "
                 "distretto: assistenza domiciliare, anziani, disabili sono anche soldi del Comune.\n"
                 "Annamaria lo ricontrolla prima di metterlo in un comunicato.",
         "keywords": "autorità sanitaria locale, TUEL art. 50, ordinanze contingibili e urgenti, conferenza dei "
                      "sindaci, d.lgs 502/92, integrazione sociosanitaria, distretto, sanità e Comune"},
        {"kind": "procedure", "section": "operations", "name": "Turno al gazebo",
         "body": "1 ritiro materiale da Teo (furgoncino) 2 montaggio in due 3 modulo contatti + consenso, cassetta, "
                 "volantini del quartiere 4 foto solo a Giada 5 smontaggio, moduli in busta a Teo, cassetta a "
                 "Paolo. vedi vademecum pdf",
         "keywords": "turno gazebo, banchetto, montaggio gazebo, modulo contatti, cassetta offerte, volantini, "
                      "vademecum"},
        {"kind": "procedure", "section": "operations", "name": "Comunicato stampa: giro",
         "body": "bozza Giada -> ok Michele -> ok Fra se tocca la coalizione -> invio dalla mail stampa alla "
                 "lista testate (foglio). Mai mandarlo dal telefono personale.",
         "keywords": "comunicato stampa, approvazione comunicato, portavoce, mail stampa, lista testate, invio ai "
                      "giornali"},
    ],
    "home_tasks": [
        {"name": "Assemblea costitutiva 20/9", "who": "lead", "stage": "Fatto",
         "description": "carta dei valori, nome, gruppi tematici",
         "notes": [("lead", 42, "fatta. 41 presenti. nome Terni 2027 votato a larga maggioranza (l'altro era "
                                "«Terni in comune»). carta approvata"),
                   ("lead", 40, "verbale in drive /statuto"),
                   ("lead", 0,
                    "Sintomo: la rete di comitati e associazioni vuole diventare una lista con nome, regole e "
                    "gruppi di lavoro.\nContesto: assemblea costitutiva del 20/9 nella saletta di Borgo Bovio: "
                    "carta dei valori, nome della lista, gruppi tematici.\nIntervento e stato: 41 presenti; nome "
                    "Terni 2027 votato a larga maggioranza (alternativa «Terni in comune»), carta dei valori "
                    "approvata; verbale in drive /statuto. Fatto.\nParole chiave: assemblea costitutiva, "
                    "fondazione della lista, Terni 2027, carta dei valori, statuto, nome della lista",
                    ["assemblea costitutiva", "fondazione della lista", "Terni 2027", "carta dei valori", "statuto",
                     "nome della lista", "Terni in comune"])],
         "keywords": ["assemblea costitutiva", "fondazione della lista", "Terni 2027", "carta dei valori",
                      "statuto", "nome della lista", "Terni in comune"]},
        {"name": "Conto corrente della lista", "who": "mandatario", "stage": "In corso",
         "description": "conto dell'associazione per ora. quello del mandatario si apre solo dopo l'indizione",
         "notes": [("mandatario", 30, "aperto c/c associazione T27 (alla filiale di via Cavour, "
                                      "costava meno)"),
                   ("mandatario", 5, "ricordo a tutti: per la campagna vera serve un conto dedicato del "
                                     "mandatario, non questo"),
                   ("mandatario", 0,
                    "Sintomo: servono un conto per le quote e le offerte prima della campagna vera.\nContesto: "
                    "conto dell'associazione T27 in via Cavour; per la campagna elettorale serve invece il conto "
                    "dedicato del mandatario, apribile solo dopo l'indizione.\nIntervento e stato: conto "
                    "dell'associazione aperto; ricordato a tutti che non vale come conto della campagna. In "
                    "corso.\nParole chiave: conto corrente, conto associazione, T27, conto del mandatario, banca, "
                    "indizione",
                    ["conto corrente", "conto associazione", "T27", "conto del mandatario", "banca", "indizione"])],
         "keywords": ["conto corrente", "conto associazione", "T27", "conto del mandatario", "banca", "indizione"]},
        {"name": "Logo e contrassegno", "who": "stampa", "stage": "In corso",
         "description": "logo per social adesso, contrassegno per la scheda dopo. due versioni",
         "notes": [("stampa", 35, "3 proposte del grafico, vince la torre con le onde"),
                   ("lead", 12, "attenzione: il contrassegno per la presentazione deve essere in tre misure e "
                                "non confondibile con altri. lo sistemiamo con gli adempimenti"),
                   ("stampa", 0,
                    "Sintomo: la lista ha bisogno di un logo per i social subito e del simbolo per la scheda "
                    "elettorale poi.\nContesto: contrassegno di lista da depositare in tre misure e non "
                    "confondibile con altri, secondo le istruzioni del Ministero dell'Interno.\nIntervento e "
                    "stato: tre proposte del grafico, scelta la torre con le onde; il contrassegno si sistema con "
                    "gli adempimenti. In corso.\nParole chiave: logo, contrassegno, simbolo elettorale, simbolo "
                    "della lista, torre con le onde, scheda elettorale",
                    ["logo", "contrassegno", "simbolo elettorale", "simbolo della lista", "torre con le onde",
                     "scheda elettorale"])],
         "keywords": ["logo", "contrassegno", "simbolo elettorale", "simbolo della lista", "torre con le onde",
                      "scheda elettorale"]},
        {"name": "Quote iscritti 2026", "who": "mandatario", "stage": "Da fare",
         "description": "10 euro, ricevute",
         "keywords": ["quote iscritti", "tesseramento", "iscrizione", "ricevute", "associazione T27"],
         "notes": [("mandatario", 0,
                    "Sintomo: vanno raccolte le quote annuali di chi si iscrive alla lista.\nContesto: quota "
                    "iscritti 2026 di 10 euro, con ricevuta, sul conto dell'associazione.\nIntervento e stato: da "
                    "fare; le quote si versano sul conto dell'associazione T27, non su quello del mandatario, che "
                    "si apre solo dopo l'indizione delle elezioni. Ogni quota con ricevuta.\nParole chiave: quote "
                    "iscritti, tesseramento, iscrizione, 10 euro, ricevute, associazione T27",
                    ["quote iscritti", "tesseramento", "iscrizione", "ricevute", "associazione T27"])]},
        {"name": "Assicurazione per i gazebo", "who": "banchetti", "stage": "Da fare",
         "description": "chiedere preventivo RC per eventi in piazza",
         "keywords": ["assicurazione", "responsabilità civile", "polizza RC", "eventi in piazza", "banchetti"],
         "notes": [("banchetti", 0,
                    "Sintomo: montare gazebo in piazza senza copertura espone i volontari a rischi in caso di "
                    "incidenti.\nContesto: polizza di responsabilità civile (RC) per eventi e banchetti in "
                    "piazza.\nIntervento e stato: da fare la richiesta di preventivo per la copertura dei turni di "
                    "novembre in piazza Tacito, Borgo Bovio e negli altri quartieri.\nParole chiave: "
                    "assicurazione, responsabilità civile, polizza RC, gazebo, eventi in piazza, banchetti",
                    ["assicurazione", "responsabilità civile", "polizza RC", "eventi in piazza", "banchetti"])]},
    ],
}

# -- the thematic projects (1/2) --------------------------------------------------------------------------------
PROJECT_CASA = {
    "name": P_CASA, "tags": ["casa", "sociale", "giovani"],
    "description": "<p>Gruppo casa, politiche sociali, giovani e servizi educativi. Referente Luisa. Capitolo del "
                   "programma, rapporti con comitati inquilini, coop sociali, associazioni di genitori.</p>",
    "milestones": [("Incontro coop 0-6", -33, 33), ("Bozza capitolo casa", 10, None),
                   ("Assemblea casa a Borgo Rivo", 20, None)],
    "tasks": [
        {"name": "Mail al comitato di Borgo Rivo (riscaldamento e infiltrazioni)", "who": "sociale", "stage": "Fatto",
         "description": "ci hanno scritto il 3/10. palazzine Ater dietro la chiesa",
         "notes": [("sociale", 28, "letta la lettera del comitato: termosifoni freddi a turno da tre inverni "
                                   "(centralizzato vecchio), acqua che entra dal tetto agli ultimi piani, muffa. "
                                   "chiedono cosa fa la lista"),
                   ("sociale", 24, "risposto per mail (testo in drive /casa/risposte): 1) chiediamo noi all'Ater "
                                   "il piano interventi con i tempi, se non rispondono accesso agli atti 2) la "
                                   "segnalazione la portano in commissione i consiglieri di opposizione che ci "
                                   "conoscono 3) nel programma un fondo comunale per i lavori urgenti sulle parti "
                                   "comuni, d'accordo con Ater 4) sopralluogo con loro sab 18"),
                   ("lead", 22, "ok, ma niente promesse di soldi che non sappiamo se ci sono: scritto "
                                "«proporremo», non «faremo»"),
                   ("sociale", 13, "sopralluogo fatto, 14 famiglie. foto delle macchie sui soffitti (senza "
                                   "persone) a Giada"),
                   ("sociale", 0,
                    "Sintomo: il comitato degli inquilini di Borgo Rivo scrive il 3/10: termosifoni freddi a turno "
                    "da tre inverni, acqua dal tetto agli ultimi piani, muffa; chiede cosa fa la lista.\nContesto: "
                    "palazzine ATER (edilizia residenziale pubblica) dietro la chiesa, riscaldamento centralizzato "
                    "vecchio, parti comuni.\nIntervento e stato: risposta per mail: richiesta ad ATER del piano "
                    "interventi con i tempi, accesso agli atti se tace; segnalazione in commissione tramite "
                    "consiglieri di opposizione; nel programma «proporremo» un fondo comunale per lavori urgenti; "
                    "sopralluogo fatto con 14 famiglie, foto senza persone. Fatto.\nParole chiave: case popolari, "
                    "ATER, Borgo Rivo, muffa, infiltrazioni, riscaldamento centralizzato, termosifoni, comitato "
                    "inquilini",
                    ["case popolari", "ATER", "edilizia residenziale pubblica", "Borgo Rivo", "muffa",
                     "infiltrazioni dal tetto", "riscaldamento centralizzato", "termosifoni freddi",
                     "comitato inquilini", "sopralluogo"])],
         "keywords": ["case popolari", "ATER", "edilizia residenziale pubblica", "Borgo Rivo", "muffa",
                      "infiltrazioni dal tetto", "riscaldamento centralizzato", "termosifoni freddi",
                      "comitato inquilini", "sopralluogo"]},
        {"name": "Leggere il dossier del Coordinamento casa", "who": "sociale", "stage": "Fatto",
         "description": "ce l'hanno girato a ottobre, pdf in drive",
         "notes": [("sociale", 19, "letto. i numeri delle case vuote sono loro, contati a mano. messo il "
                                   "riassunto nella scheda del documento"),
                   ("lead", 18, "in pubblico solo con «secondo il Coordinamento casa». Ater non ha mai dato un "
                                "numero"),
                   ("sociale", 0,
                    "Sintomo: il Coordinamento casa ha girato a ottobre un dossier in pdf sugli appartamenti "
                    "popolari vuoti e chiede che la lista lo usi.\nContesto: numeri contati a mano dal "
                    "Coordinamento con sopralluoghi e segnalazioni; ATER non ha mai fornito un dato ufficiale "
                    "sugli alloggi sfitti dell'edilizia residenziale pubblica.\nIntervento e stato: dossier letto, "
                    "riassunto nella scheda del documento. Regola d'uso: in pubblico le cifre si citano solo come "
                    "«secondo il Coordinamento casa», mai come dati ATER. Fatto.\nParole chiave: Coordinamento "
                    "casa, alloggi sfitti, case popolari vuote, ATER, dossier, riassegnazione, numeri non ufficiali",
                    ["Coordinamento casa", "alloggi sfitti", "case popolari vuote", "appartamenti chiusi", "ATER",
                     "dossier", "riassegnazione alloggi", "numeri non ufficiali"])],
         "keywords": ["Coordinamento casa", "alloggi sfitti", "case popolari vuote", "appartamenti chiusi", "ATER",
                      "dossier", "riassegnazione alloggi", "numeri non ufficiali"]},
        {"name": "Scheda programma: affitti e morosità", "who": "sociale", "stage": "In corso",
         "milestone": "Bozza capitolo casa", "deadline": 10,
         "description": "proposta per chi non ce la fa a pagare l'affitto",
         "notes": [("sociale", 20, "bozza 1: rimettere soldi del Comune nel contributo canoni oltre la quota "
                                   "regionale; sportello affitti unico in Comune; il fondo morosità incolpevole "
                                   "usato davvero (oggi poche domande perché nessuno lo conosce); canone concordato "
                                   "con garanzia comunale per i proprietari"),
                   ("sociale", 16, "aggiunto: tavolo in prefettura per graduare le esecuzioni, nessuno esce di casa "
                                   "senza un posto dove andare. sentita l'avvocata del comitato"),
                   ("lead", 9, "approvata dal gruppo, va nella bozza comune come proposta nostra"),
                   ("sociale", 0,
                    "Sintomo: famiglie che non riescono a pagare l'affitto e rischiano lo sfratto; il gruppo casa "
                    "vuole una proposta per loro.\nContesto: contributo canoni oltre la quota regionale, fondo "
                    "morosità incolpevole poco conosciuto, canone concordato con garanzia comunale, esecuzioni "
                    "degli sfratti graduate con un tavolo in prefettura; sentita l'avvocata del "
                    "comitato.\nIntervento e stato: bozza con sportello affitti unico in Comune, fondi comunali "
                    "sul contributo affitto, uso effettivo del fondo morosità, garanzia ai proprietari; nessuno "
                    "esce di casa senza alternativa. Approvata dal gruppo, entra nella bozza comune come proposta "
                    "della lista. In corso.\nParole chiave: sfratti, morosità incolpevole, contributo affitto, "
                    "canone concordato, emergenza abitativa, sportello affitti, prefettura",
                    ["sfratti", "morosità incolpevole", "contributo affitto", "fondo canoni", "canone concordato",
                     "emergenza abitativa", "sportello affitti", "tavolo in prefettura"])],
         "keywords": ["sfratti", "morosità incolpevole", "contributo affitto", "fondo canoni", "canone concordato",
                      "emergenza abitativa", "sportello affitti", "tavolo in prefettura"]},
        {"name": "Incontro coop sociali sui servizi 0-6", "who": "sociale", "stage": "Fatto",
         "milestone": "Incontro coop 0-6",
         "notes": [("sociale", 33, "gio in sede con 4 coop e l'associazione genitori di Città Giardino. c'eravamo "
                                   "io, Ilaria e Fra. problemi: le tariffe degli asili comunali pesano su chi sta "
                                   "appena sopra le soglie ISEE, famiglie con 2 figli che rinunciano; pochi posti "
                                   "a Cesi e San Valentino, lista d'attesa; educatrici delle coop precarie"),
                   ("lead", 31, "verbale in drive. proposta: fasce ISEE più fini e secondo figlio gratis, da far "
                                "quadrare coi costi (Paolo)"),
                   ("sociale", 0,
                    "Sintomo: cooperative sociali e associazione genitori di Città Giardino segnalano rette degli "
                    "asili troppo alte per chi sta appena sopra le soglie, famiglie con due figli che rinunciano, "
                    "liste d'attesa.\nContesto: servizi educativi 0-6, asili nido comunali, tariffe per fasce "
                    "ISEE, pochi posti a Cesi e San Valentino, educatrici delle cooperative precarie.\nIntervento "
                    "e stato: incontro in sede con 4 cooperative, verbale in drive. Proposta: fasce ISEE più fini "
                    "e secondo figlio gratis, da far quadrare con i costi. Fatto.\nParole chiave: asili nido, "
                    "servizi 0-6, rette, ISEE, cooperative sociali, secondo figlio gratis, liste d'attesa, Città "
                    "Giardino",
                    ["asili nido", "servizi 0-6", "rette asilo", "fasce ISEE", "cooperative sociali",
                     "secondo figlio gratis", "lista d'attesa", "Città Giardino", "educatrici precarie"])],
         "keywords": ["asili nido", "servizi 0-6", "rette asilo", "fasce ISEE", "cooperative sociali",
                      "secondo figlio gratis", "lista d'attesa", "Città Giardino", "educatrici precarie"]},
        {"name": "Centri giovani e sale studio di quartiere", "who": "sociale", "stage": "In corso",
         "milestone": "Bozza capitolo casa",
         "description": "bozza del sottogruppo giovani (Ilaria, Gigi)",
         "notes": [("sociale", 26, "idea: riaprire i locali comunali chiusi a Borgo Rivo e San Valentino come "
                                   "sale studio aperte fino a mezzanotte + centri giovani gestiti con le "
                                   "associazioni. prestito libri in rete con la biblioteca comunale, wifi"),
                   ("sociale", 12, "Cesi e Collestatte: i ragazzi non hanno niente e non c'è il bus la sera. "
                                   "aggiunto"),
                   ("lead", 5, "va bene ma servono i costi, chiedo a Paolo una stima"),
                   ("sociale", 0,
                    "Sintomo: i ragazzi dei quartieri non hanno spazi per studiare e ritrovarsi; a Cesi e "
                    "Collestatte non c'è nulla e manca il bus serale.\nContesto: locali comunali chiusi a Borgo "
                    "Rivo e San Valentino, rete con la biblioteca comunale, gestione con le associazioni, "
                    "politiche giovanili.\nIntervento e stato: bozza del sottogruppo giovani: sale studio aperte "
                    "fino a mezzanotte con wifi e prestito libri, centri giovani di quartiere; aggiunte le "
                    "frazioni. Manca la stima dei costi, chiesta al tesoriere. In corso.\nParole chiave: sale "
                    "studio, aule studio serali, centri giovani, aggregazione giovanile, biblioteca, Cesi, "
                    "Collestatte, locali comunali chiusi",
                    ["sale studio", "aule studio serali", "centri giovani", "aggregazione giovanile",
                     "biblioteca comunale", "Cesi", "Collestatte", "locali comunali chiusi"])],
         "keywords": ["sale studio", "aule studio serali", "centri giovani", "aggregazione giovanile",
                      "biblioteca comunale", "Cesi", "Collestatte", "locali comunali chiusi"]},
        {"name": "Nuova legge ERP della Regione: cosa cambia per noi", "who": "sociale", "stage": "Fatto",
         "notes": [("sociale", 60, "vedi fatto sulla commissione del 28/1: residenza minima tolta, punteggi "
                                   "disabilità, emergenze. la nostra scheda deve stare dentro quella cornice"),
                   ("sociale", 0,
                    "Sintomo: il gruppo casa vuole sapere se la riforma regionale delle case popolari cambia la "
                    "scheda programma.\nContesto: il 28/01/2026 la III commissione del Consiglio regionale "
                    "dell'Umbria approva le modifiche alla LR 23/2003 sull'edilizia residenziale pubblica: tolta "
                    "la residenza minima, punteggi per disabilità, donne vittime di violenza tra le emergenze, "
                    "autorecupero, protocolli con Comuni, ATER e Terzo settore.\nIntervento e stato: verificato "
                    "sul fatto verificato della commissione; la scheda casa della lista deve stare dentro quella "
                    "cornice. Fatto.\nParole chiave: ERP, LR 23/2003, legge regionale case popolari, III "
                    "commissione, residenza minima, graduatoria, ATER",
                    ["ERP", "LR 23/2003", "legge regionale case popolari", "edilizia residenziale pubblica",
                     "III commissione regionale", "residenza minima", "punteggi graduatoria", "autorecupero"])],
         "keywords": ["ERP", "LR 23/2003", "legge regionale case popolari", "edilizia residenziale pubblica",
                      "III commissione regionale", "residenza minima", "punteggi graduatoria", "autorecupero"]},
        {"name": "Sportello casa della parrocchia", "who": "sociale", "stage": "In corso",
         "description": "ci aiutano a capire i casi veri (senza nomi)",
         "notes": [("sociale", 15, "il volontario dello sportello dice che metà delle richieste sono per bollette "
                                   "arretrate, non per l'affitto"),
                   ("sociale", 0,
                    "Sintomo: la lista vuole capire i casi reali di disagio abitativo, senza nomi, attraverso chi "
                    "li incontra ogni giorno.\nContesto: sportello casa della parrocchia gestito da volontari; "
                    "secondo il volontario metà delle richieste riguarda bollette arretrate (povertà energetica) e "
                    "non l'affitto.\nIntervento e stato: contatto avviato, informazioni raccolte in forma anonima "
                    "per orientare la scheda casa e sociale. In corso.\nParole chiave: sportello casa, parrocchia, "
                    "bollette arretrate, povertà energetica, morosità utenze, disagio abitativo",
                    ["sportello casa", "parrocchia", "bollette arretrate", "povertà energetica", "morosità utenze",
                     "disagio abitativo"])],
         "keywords": ["sportello casa", "parrocchia", "bollette arretrate", "povertà energetica", "morosità utenze",
                      "disagio abitativo"]},
        {"name": "Storie per il volantino casa", "who": "stampa", "stage": "In attesa",
         "description": "solo con consenso scritto, niente nomi né foto riconoscibili",
         "notes": [("stampa", 14, "2 storie raccolte, una ritirata. aspettiamo"),
                   ("lead", 13, "se non ne abbiamo 3 usiamo dati, non storie"),
                   ("stampa", 0,
                    "Sintomo: per il volantino sulla casa servono storie vere di inquilini e famiglie in "
                    "difficoltà.\nContesto: raccolta solo con consenso scritto, niente nomi né foto riconoscibili "
                    "(tutela dei dati personali); due storie raccolte, una ritirata dall'interessato.\nIntervento "
                    "e stato: in attesa di altre testimonianze; se non si arriva a tre, il volantino usa dati con "
                    "fonte invece delle storie.\nParole chiave: testimonianze, storie inquilini, volantino casa, "
                    "consenso scritto, privacy, anonimato",
                    ["testimonianze", "storie inquilini", "volantino casa", "consenso scritto", "privacy",
                     "anonimato"])],
         "keywords": ["testimonianze", "storie inquilini", "volantino casa", "consenso scritto", "privacy",
                      "anonimato"]},
        {"name": "Questionario giovani online", "who": "sociale", "stage": "Da fare",
         "description": "google form? meglio di no per i dati. vedere alternativa",
         "keywords": ["questionario giovani", "sondaggio online", "Google Form", "modulo online", "privacy", "GDPR",
                      "ascolto giovani"],
         "notes": [("sociale", 0,
                    "Sintomo: il gruppo giovani vuole un questionario online per sentire cosa chiedono i "
                    "ragazzi.\nContesto: dubbio sullo strumento: un Google Form è sconsigliato per la protezione "
                    "dei dati personali dei rispondenti; serve un'alternativa conforme alla privacy.\nIntervento e "
                    "stato: da fare, scelta dello strumento ancora aperta.\nParole chiave: questionario giovani, "
                    "sondaggio online, Google Form, modulo online, privacy, GDPR, ascolto dei ragazzi",
                    ["questionario giovani", "sondaggio online", "Google Form", "modulo online", "privacy", "GDPR",
                     "ascolto giovani"])]},
        {"name": "Assemblea pubblica casa a Borgo Rivo", "who": "sociale", "stage": "Da fare",
         "milestone": "Assemblea casa a Borgo Rivo", "deadline": 20,
         "description": "sab 21/11 pomeriggio, sala del centro sociale anziani",
         "notes": [("banchetti", 3, "sala confermata, servono 40 sedie in più"),
                   ("sociale", 0,
                    "Sintomo: dopo le lettere e il sopralluogo, gli inquilini di Borgo Rivo e il quartiere "
                    "chiedono un momento pubblico sulla casa.\nContesto: assemblea pubblica sabato 21/11 "
                    "pomeriggio nella sala del centro sociale anziani; temi case popolari ATER, affitti, emergenza "
                    "abitativa.\nIntervento e stato: sala confermata, servono 40 sedie in più. Da fare.\nParole "
                    "chiave: assemblea pubblica casa, Borgo Rivo, centro sociale anziani, 21 novembre, case "
                    "popolari, inquilini ATER",
                    ["assemblea pubblica casa", "Borgo Rivo", "centro sociale anziani", "21 novembre",
                     "case popolari", "inquilini ATER"])],
         "keywords": ["assemblea pubblica casa", "Borgo Rivo", "centro sociale anziani", "21 novembre",
                      "case popolari", "inquilini ATER"]},
        {"name": "Barriere architettoniche nelle palazzine", "who": "sociale", "stage": "Da fare",
         "description": "ascensori rotti, segnalazioni da raccogliere",
         "keywords": ["barriere architettoniche", "ascensori rotti", "accessibilità", "disabilità",
                      "palazzine ATER", "case popolari"],
         "notes": [("sociale", 0,
                    "Sintomo: inquilini con ascensori rotti nelle palazzine, chi ha difficoltà motorie resta "
                    "bloccato in casa.\nContesto: barriere architettoniche negli edifici di edilizia residenziale "
                    "pubblica ATER; accessibilità e disabilità, collegato ai punteggi per disabilità della nuova "
                    "legge ERP regionale.\nIntervento e stato: da fare la raccolta delle segnalazioni palazzina "
                    "per palazzina.\nParole chiave: barriere architettoniche, ascensori rotti, accessibilità, "
                    "disabilità, palazzine ATER, case popolari, segnalazioni",
                    ["barriere architettoniche", "ascensori rotti", "accessibilità", "disabilità", "palazzine ATER",
                     "case popolari"])]},
    ],
    "updates": [
        ("Casa: ottobre", "on_track", 45, 9, "risposto al comitato di Borgo Rivo e fatto il sopralluogo. scheda "
                                             "affitti approvata dal gruppo. giovani: manca la stima dei costi. "
                                             "prossimo: assemblea del 21/11."),
    ],
}

PROJECT_AMB = {
    "name": P_AMB, "tags": ["ambiente", "rifiuti", "aria"],
    "description": "<p>Gruppo ambiente: rifiuti, aria, verde, energia, mobilità. Referente Tommy. Rapporti con il "
                   "Coordinamento ambientalisti e i comitati di Maratta e Prisciano.</p>",
    "milestones": [("Nota rifiuti", -20, 19), ("Scheda energia", 15, None), ("Bozza capitolo ambiente", 25, None)],
    "tasks": [
        {"name": "Nota rifiuti per il tavolo (termovalorizzatore)", "who": "ambiente", "stage": "Fatto",
         "milestone": "Nota rifiuti",
         "notes": [("ambiente", 20, "la nostra linea, votata in gruppo il 12/10: no a impianti che bruciano "
                                    "rifiuti nella conca, già piena di camini; sì porta a porta spinto e tariffa "
                                    "puntuale. sulla legge regionale (Umbria Circolare): d'accordo sull'impianto "
                                    "generale, chiediamo che gli impianti di trattamento non finiscano tutti qui"),
                   ("ambiente", 9, "al tavolo: la delegata dice che la bozza comune riprende la linea della "
                                   "Regione (nessun bruciatore). sugli impianti di trattamento: da definire al "
                                   "tavolo. noi insistiamo sulla frase sulla conca"),
                   ("lead", 8, "in pubblico resta la nostra nota del 12/10, niente di più"),
                   ("ambiente", 0,
                    "Sintomo: il tavolo di coalizione chiede la posizione della lista su rifiuti e "
                    "termovalorizzatore.\nContesto: linea votata in gruppo il 12/10: no a impianti che bruciano "
                    "rifiuti nella conca già piena di camini, sì porta a porta spinto e tariffa puntuale; sul ddl "
                    "regionale Umbria Circolare d'accordo sull'impianto generale, ma gli impianti di trattamento "
                    "non tutti a Terni.\nIntervento e stato: al tavolo la bozza comune riprende la linea della "
                    "Regione (nessun inceneritore); impianti di trattamento da definire. In pubblico solo la nota "
                    "del 12/10. Fatto.\nParole chiave: termovalorizzatore, inceneritore, inceneritori, Umbria "
                    "Circolare, porta a porta, tariffa puntuale, conca ternana, impianti di trattamento",
                    ["termovalorizzatore", "inceneritore", "Umbria Circolare", "raccolta porta a porta",
                     "tariffa puntuale", "conca ternana", "impianti di trattamento rifiuti", "AURI"])],
         "keywords": ["termovalorizzatore", "inceneritore", "Umbria Circolare", "raccolta porta a porta",
                      "tariffa puntuale", "conca ternana", "impianti di trattamento rifiuti", "AURI"]},
        {"name": "Smog: dati ARPA per stazione", "who": "ambiente", "stage": "In attesa",
         "description": "ci servono i superamenti 2024-2025 per stazione, non solo il dato vecchio",
         "notes": [("ambiente", 16, "mandata pec ad ARPA"),
                   ("ambiente", 2, "niente ancora. intanto usiamo i dati 2023 col link"),
                   ("ambiente", 0,
                    "Sintomo: per parlare di smog servono i superamenti recenti delle polveri sottili per ogni "
                    "centralina, non solo il dato vecchio.\nContesto: dati ARPA Umbria 2024-2025 per stazione non "
                    "disponibili; finora noto il 2023 (Maratta 41 superamenti PM10, fonte La Nazione).\nIntervento "
                    "e stato: richiesta inviata ad ARPA via PEC, nessuna risposta. Intanto in pubblico si usano i "
                    "dati 2023 con il link. In attesa.\nParole chiave: smog, inquinamento aria, PM10, polveri "
                    "sottili, ARPA, centraline, superamenti, Maratta",
                    ["smog", "inquinamento dell'aria", "PM10", "polveri sottili", "ARPA Umbria", "centraline",
                     "superamenti", "Maratta", "PEC"])],
         "keywords": ["smog", "inquinamento dell'aria", "PM10", "polveri sottili", "ARPA Umbria", "centraline",
                      "superamenti", "Maratta", "PEC"]},
        {"name": "CER sui tetti delle palazzine Ater", "who": "ambiente", "stage": "In corso",
         "milestone": "Scheda energia", "deadline": 15,
         "notes": [("ambiente", 30, "serata col Coordinamento ambientalisti della conca, 6 associazioni. "
                                    "accordo a voce: noi mettiamo nel programma una CER con il Comune capofila, "
                                    "prima i tetti delle case popolari e delle scuole; loro fanno gli incontri "
                                    "nei condomini; un loro tecnico fa gratis lo studio di fattibilità su 2 "
                                    "palazzine di Borgo Rivo"),
                   ("ambiente", 22, "mandato il testo della scheda, ok con 2 correzioni: lo sconto in bolletta "
                                    "va agli inquilini, non all'Ater"),
                   ("lead", 20, "protocollo d'intesa semplice da firmare dopo il 15/11"),
                   ("ambiente", 0,
                    "Sintomo: il Coordinamento ambientalisti della conca (6 associazioni) propone fotovoltaico "
                    "condiviso sulle case popolari per abbassare le bollette.\nContesto: comunità energetica "
                    "rinnovabile (CER) con il Comune capofila, prima i tetti delle palazzine ATER e delle scuole; "
                    "studio di fattibilità gratuito di un loro tecnico su 2 palazzine di Borgo Rivo.\nIntervento e "
                    "stato: accordo a voce; scheda inviata, ok con 2 correzioni: lo sconto in bolletta va agli "
                    "inquilini, non all'ATER. Protocollo d'intesa da firmare dopo il 15/11. In corso.\nParole "
                    "chiave: CER, comunità energetica rinnovabile, energia condivisa, fotovoltaico, pannelli "
                    "solari, case popolari, ATER, protocollo d'intesa",
                    ["CER", "comunità energetica rinnovabile", "energia condivisa", "fotovoltaico sui tetti",
                     "pannelli solari", "case popolari", "ATER", "Coordinamento ambientalisti",
                     "protocollo d'intesa"])],
         "keywords": ["CER", "comunità energetica rinnovabile", "energia condivisa", "fotovoltaico sui tetti",
                      "pannelli solari", "case popolari", "ATER", "Coordinamento ambientalisti",
                      "protocollo d'intesa"]},
        {"name": "Alberi tagliati: accesso agli atti e mappa segnalazioni", "who": "ambiente", "stage": "In corso",
         "notes": [("ambiente", 25, "per rispondere sugli alberi servono carte, non impressioni. 1) albo "
                                    "pretorio: determine di abbattimento e affidamenti delle potature 2026 "
                                    "(scaricate 11, cartella /ambiente/verde) 2) accesso agli atti per il "
                                    "censimento e le perizie di stabilità 3) mappa delle segnalazioni dei "
                                    "cittadini col modulo online"),
                   ("ambiente", 18, "della giunta non abbiamo nessuna dichiarazione archiviata con fonte su "
                                    "questo. chi vuole citare sindaco o assessore prima trova il link"),
                   ("ambiente", 6, "accesso agli atti protocollato, 30 gg"),
                   ("ambiente", 0,
                    "Sintomo: cittadini protestano per gli alberi abbattuti e le potature; la lista vuole "
                    "rispondere con documenti, non impressioni.\nContesto: albo pretorio del Comune: determine di "
                    "abbattimento e affidamenti delle potature 2026 (11 scaricate); accesso agli atti per "
                    "censimento del verde e perizie di stabilità; nessuna dichiarazione della giunta archiviata "
                    "con fonte.\nIntervento e stato: accesso agli atti protocollato (30 giorni); mappa delle "
                    "segnalazioni con modulo online. Chi cita sindaco o assessore deve prima trovare il link. In "
                    "corso.\nParole chiave: alberi abbattuti, taglio alberi, potature, verde pubblico, albo "
                    "pretorio, determine, accesso agli atti, perizie di stabilità",
                    ["alberi abbattuti", "taglio alberi", "potature", "verde pubblico", "albo pretorio",
                     "determine dirigenziali", "accesso agli atti", "perizie di stabilità", "censimento alberi"])],
         "keywords": ["alberi abbattuti", "taglio alberi", "potature", "verde pubblico", "albo pretorio",
                      "determine dirigenziali", "accesso agli atti", "perizie di stabilità", "censimento alberi"]},
        {"name": "Siti contaminati: capitolo per la bozza comune", "who": "ambiente", "stage": "In corso",
         "milestone": "Bozza capitolo ambiente",
         "notes": [("ambiente", 15, "nella bozza comune solo due righe generiche sull'ambiente industriale. il "
                                    "delegato di area ambientalista vuole un capitolo vero su vecchie discariche e "
                                    "terreni inquinati: elenco ufficiale, cronoprogramma, chi paga"),
                   ("ambiente", 9, "al tavolo nessun impegno preciso preso. da definire al tavolo, la delegata "
                                   "vuole prima l'elenco ufficiale dei siti. compito nostro: la scheda"),
                   ("ambiente", 2, "cerco l'anagrafe regionale dei siti. nessun nome di area nei testi finché "
                                   "non ce l'ho"),
                   ("ambiente", 0,
                    "Sintomo: il delegato di area ambientalista al tavolo trova nella bozza comune solo due righe "
                    "generiche sull'ambiente industriale e chiede un capitolo vero.\nContesto: vecchie discariche "
                    "e terreni inquinati, elenco ufficiale dei siti, cronoprogramma delle bonifiche, chi paga; "
                    "serve l'anagrafe regionale dei siti contaminati.\nIntervento e stato: al tavolo nessun "
                    "impegno preciso, da definire dopo l'elenco ufficiale; la lista scrive la scheda. Nessun nome "
                    "di area nei testi finché non c'è l'anagrafe. In corso.\nParole chiave: siti contaminati, "
                    "bonifiche, terreni inquinati, discariche, anagrafe regionale siti, inquinamento industriale",
                    ["siti contaminati", "bonifiche", "terreni inquinati", "vecchie discariche",
                     "anagrafe regionale dei siti", "inquinamento industriale", "cronoprogramma bonifiche"])],
         "keywords": ["siti contaminati", "bonifiche", "terreni inquinati", "vecchie discariche",
                      "anagrafe regionale dei siti", "inquinamento industriale", "cronoprogramma bonifiche"]},
        {"name": "Mobilità: bus serali e bici", "who": "ambiente", "stage": "Da fare",
         "description": "collegare con la scheda giovani (Cesi, Collestatte)",
         "keywords": ["bus serali", "trasporto pubblico locale", "autobus", "piste ciclabili",
                      "mobilità sostenibile", "Cesi", "Collestatte", "frazioni"],
         "notes": [("ambiente", 0,
                    "Sintomo: nelle frazioni la sera non passa il bus e i ragazzi restano isolati; chi va in bici "
                    "chiede percorsi.\nContesto: trasporto pubblico locale serale, ciclabili, collegamento con la "
                    "scheda giovani per Cesi e Collestatte.\nIntervento e stato: da fare, da scrivere insieme al "
                    "sottogruppo giovani.\nParole chiave: bus serali, trasporto pubblico, autobus notturni, piste "
                    "ciclabili, mobilità sostenibile, Cesi, Collestatte, frazioni",
                    ["bus serali", "trasporto pubblico locale", "autobus", "piste ciclabili",
                     "mobilità sostenibile", "Cesi", "Collestatte", "frazioni"])]},
        {"name": "Segnalazioni differenziata nei quartieri", "who": "banchetti", "stage": "In corso",
         "notes": [("banchetti", 11, "al gazebo di Borgo Bovio 6 lamentele sui cassonetti pieni. foto senza "
                                     "persone"),
                   ("banchetti", 0,
                    "Sintomo: al gazebo di Borgo Bovio arrivano 6 lamentele sui cassonetti sempre pieni e la "
                    "raccolta che non passa.\nContesto: raccolta differenziata e servizio di igiene urbana nei "
                    "quartieri; documentazione fotografica senza persone riconoscibili.\nIntervento e stato: "
                    "segnalazioni e foto raccolte per la scheda rifiuti. In corso.\nParole chiave: raccolta "
                    "differenziata, cassonetti pieni, rifiuti nei quartieri, igiene urbana, Borgo Bovio, "
                    "segnalazioni gazebo",
                    ["raccolta differenziata", "cassonetti pieni", "rifiuti nei quartieri", "igiene urbana",
                     "Borgo Bovio", "segnalazioni gazebo"])],
         "keywords": ["raccolta differenziata", "cassonetti pieni", "rifiuti nei quartieri", "igiene urbana",
                      "Borgo Bovio", "segnalazioni gazebo"]},
        {"name": "Incontro comitati di Maratta e Prisciano", "who": "ambiente", "stage": "Fatto",
         "notes": [("ambiente", 35, "chiedono centraline in più e dati pubblici in tempo reale. ok, va nella "
                                    "scheda aria"),
                   ("ambiente", 0,
                    "Sintomo: i comitati di Maratta e Prisciano, nella zona più colpita dallo smog, chiedono più "
                    "controlli sull'aria.\nContesto: centraline di monitoraggio della qualità dell'aria ARPA, dati "
                    "pubblici in tempo reale, polveri sottili PM10 vicino all'area industriale.\nIntervento e "
                    "stato: incontro fatto; le richieste (centraline in più, dati aperti in tempo reale) entrano "
                    "nella scheda aria del programma. Fatto.\nParole chiave: Maratta, Prisciano, comitati di "
                    "quartiere, centraline, qualità dell'aria, dati in tempo reale, ARPA, smog",
                    ["Maratta", "Prisciano", "comitati di quartiere", "centraline", "qualità dell'aria",
                     "dati in tempo reale", "ARPA", "smog"])],
         "keywords": ["Maratta", "Prisciano", "comitati di quartiere", "centraline", "qualità dell'aria",
                      "dati in tempo reale", "ARPA", "smog"]},
        {"name": "Volantino aria pulita", "who": "stampa", "stage": "Da fare",
         "description": "dati ARPA con fonte, niente allarmismi",
         "keywords": ["volantino aria", "aria pulita", "smog", "PM10", "polveri sottili", "ARPA",
                      "inquinamento atmosferico"],
         "notes": [("stampa", 0,
                    "Sintomo: ai gazebo serve un volantino sull'aria che informi senza spaventare.\nContesto: "
                    "volantino del gruppo ambiente per i gazebo nei quartieri più esposti, come Maratta e "
                    "Prisciano; solo dati ARPA con fonte (superamenti PM10, Maratta 41 nel 2023 da La Nazione), "
                    "niente allarmismi; collegato alla scheda aria e alla richiesta di dati per "
                    "stazione.\nIntervento e stato: da fare.\nParole chiave: volantino aria, aria pulita, smog, "
                    "PM10, polveri sottili, ARPA, inquinamento",
                    ["volantino aria", "aria pulita", "smog", "PM10", "polveri sottili", "ARPA",
                     "inquinamento atmosferico"])]},
    ],
    "updates": [
        ("Ambiente: a metà", "on_track", 40, 8, "nota rifiuti fatta, al tavolo impianti da definire. CER: accordo "
                                                "a voce con gli ambientalisti, protocollo dopo il 15/11. siti "
                                                "contaminati: manca l'elenco ufficiale."),
    ],
}

PROJECT_SAN = {
    "name": P_SAN, "tags": ["sanità", "ospedale"],
    "description": "<p>Gruppo sanità: nuovo ospedale, pronto soccorso, territorio, tempi d'attesa. Referente "
                   "Annamaria.</p>",
    "milestones": [("Lettera operatori", -17, 17), ("Assemblea sanità", 27, None)],
    "tasks": [
        {"name": "Ospedale nella bozza comune", "who": "sanita", "stage": "In corso",
         "notes": [("sanita", 25, "attenzione: sul sito non è deciso niente. il Docfap di luglio ha tre ipotesi "
                                  "(Sabbione, Campitello, Colle Obito) e prima ci sarà il dibattito pubblico. chi "
                                  "dice Colle Obito come cosa fatta sbaglia"),
                   ("sanita", 9, "tavolo: nessun documento firmato dai partiti, c'è la bozza di lavoro. ci "
                                 "scriviamo: tempi certi, finanziamento intero prima della gara, il vecchio non si "
                                 "svuota prima che il nuovo funzioni, dibattito pubblico vero. sito: da definire "
                                 "al tavolo dopo il dibattito"),
                   ("lead", 8, "ok. niente «il PD dice» o «i 5S dicono»: in pubblico solo la nostra posizione"),
                   ("sanita", 0,
                    "Sintomo: al gazebo e al tavolo c'è chi dà per deciso il sito del nuovo ospedale a Colle "
                    "Obito.\nContesto: nuovo ospedale Santa Maria: il Docfap di fine luglio 2026 ha tre "
                    "alternative (Sabbione, Campitello, Colle Obito) e prima è previsto il dibattito pubblico; al "
                    "tavolo di coalizione solo una bozza di lavoro, nessun documento firmato.\nIntervento e stato: "
                    "nella bozza: tempi certi, finanziamento intero prima della gara, il vecchio ospedale non si "
                    "svuota prima che il nuovo funzioni, dibattito pubblico vero; sito da definire dopo il "
                    "dibattito. In pubblico solo la posizione della lista. In corso.\nParole chiave: nuovo "
                    "ospedale, Santa Maria, Docfap, Colle Obito, Sabbione, Campitello, dibattito pubblico",
                    ["nuovo ospedale", "Santa Maria", "Docfap", "Colle Obito", "Sabbione", "Campitello",
                     "dibattito pubblico", "sito ospedale"])],
         "keywords": ["nuovo ospedale", "Santa Maria", "Docfap", "Colle Obito", "Sabbione", "Campitello",
                      "dibattito pubblico", "sito ospedale"]},
        {"name": "Lettera degli operatori del PS: risposta", "who": "sanita", "stage": "Fatto",
         "milestone": "Lettera operatori",
         "notes": [("sanita", 21, "arrivata la lettera di un gruppo di infermieri e OSS del PS con la RSU: "
                                  "barelle in corridoio, turni scoperti, aggressioni. chiedono cosa farebbe il "
                                  "Comune"),
                   ("sanita", 17, "risposto (testo in drive): 1) il Comune chiede in conferenza dei sindaci un "
                                  "piano assunzioni e un punto di primo intervento in città h12 per i codici "
                                  "minori 2) parcheggio gratis e bus notturno per chi fa i turni 3) incontro "
                                  "pubblico con loro a dicembre. nessuna promessa sui contratti: non dipendono "
                                  "dal Comune"),
                   ("portavoce", 16, "la mando ai giornali? no, resta privata finché non ce lo chiedono loro"),
                   ("sanita", 0,
                    "Sintomo: infermieri e OSS del pronto soccorso, con la RSU, scrivono: barelle in corridoio, "
                    "turni scoperti, aggressioni; chiedono cosa farebbe il Comune.\nContesto: pronto soccorso "
                    "dell'ospedale di Terni, conferenza dei sindaci, USL; i contratti non dipendono dal "
                    "Comune.\nIntervento e stato: risposta privata: piano assunzioni e punto di primo intervento "
                    "in città h12 per i codici minori chiesti in conferenza dei sindaci; parcheggio gratis e bus "
                    "notturno per i turnisti; incontro pubblico a dicembre. Nessuna promessa sui contratti; la "
                    "lettera non va ai giornali. Fatto.\nParole chiave: pronto soccorso, PS, infermieri, OSS, RSU, "
                    "barelle in corridoio, aggressioni, conferenza dei sindaci",
                    ["pronto soccorso", "PS", "infermieri", "OSS", "RSU", "barelle in corridoio",
                     "aggressioni al personale", "conferenza dei sindaci", "primo intervento h12"])],
         "keywords": ["pronto soccorso", "PS", "infermieri", "OSS", "RSU", "barelle in corridoio",
                      "aggressioni al personale", "conferenza dei sindaci", "primo intervento h12"]},
        {"name": "Verbale gruppo sanità 14/10", "who": "sanita", "stage": "Fatto",
         "notes": [("sanita", 18, "verbale: la delibera regionale sui distretti nessuno l'ha letta intera, il "
                                  "link che girava era una bozza. NON commentiamo atti che non abbiamo. CdC: "
                                  "chiedere alla USL quali presidi sono aperti davvero e con che orari, poi giro "
                                  "di verifica nostro"),
                   ("sanita", 4, "richiesta scritta mandata alla USL, aspettiamo"),
                   ("sanita", 0,
                    "Sintomo: nel gruppo sanità circolava un link alla delibera regionale sui distretti, poi "
                    "rivelatosi una bozza.\nContesto: delibera regionale sui distretti sanitari non letta per "
                    "intero; Case di Comunità (CdC) della USL: non è chiaro quali presidi siano aperti e con che "
                    "orari.\nIntervento e stato: deciso di non commentare atti non letti nel testo ufficiale; "
                    "richiesta scritta alla USL su presidi e orari delle Case di Comunità, poi giro di verifica "
                    "della lista. In attesa di risposta; verbale fatto.\nParole chiave: Case di Comunità, CdC, "
                    "distretti sanitari, delibera regionale, USL, sanità territoriale, presidi",
                    ["Case di Comunità", "CdC", "distretti sanitari", "delibera regionale", "USL",
                     "sanità territoriale", "presidi sanitari"])],
         "keywords": ["Case di Comunità", "CdC", "distretti sanitari", "delibera regionale", "USL",
                      "sanità territoriale", "presidi sanitari"]},
        {"name": "Scheda programma: tempi per esami e visite", "who": "sanita", "stage": "In corso",
         "notes": [("sanita", 27, "bozza: 1) CUP con tutte le agende, pubbliche e convenzionate, visibili 2) se il "
                                  "tempo massimo della ricetta (U, B, D) salta, l'esame si fa in intramoenia o "
                                  "nel convenzionato a carico della USL e non di chi aspetta: c'è già, nessuno lo "
                                  "sa 3) sportello comunale che aiuta a chiederlo"),
                   ("sanita", 11, "aggiunto: TAC e risonanze la sera e il sabato"),
                   ("sanita", 0,
                    "Sintomo: cittadini che aspettano mesi per esami e visite specialistiche e non sanno di avere "
                    "alternative.\nContesto: liste d'attesa, CUP con agende pubbliche e convenzionate, tempi "
                    "massimi delle priorità della ricetta (U, B, D); se saltano, la prestazione va garantita in "
                    "intramoenia o nel privato convenzionato a carico della USL.\nIntervento e stato: bozza: CUP "
                    "con tutte le agende visibili, diritto già esistente reso noto, sportello comunale che aiuta a "
                    "chiederlo; aggiunte TAC e risonanze la sera e il sabato. In corso.\nParole chiave: liste "
                    "d'attesa, tempi di attesa, CUP, intramoenia, ricetta priorità, esami diagnostici, TAC, "
                    "risonanza",
                    ["liste d'attesa", "tempi di attesa", "CUP", "intramoenia", "priorità ricetta",
                     "visite specialistiche", "TAC", "risonanza magnetica"])],
         "keywords": ["liste d'attesa", "tempi di attesa", "CUP", "intramoenia", "priorità ricetta",
                      "visite specialistiche", "TAC", "risonanza magnetica"]},
        {"name": "Incontro medici di famiglia", "who": "sanita", "stage": "Da fare",
         "description": "2 medici di San Valentino disponibili",
         "keywords": ["medici di famiglia", "medicina generale", "medici di base", "San Valentino",
                      "sanità territoriale"],
         "notes": [("sanita", 0,
                    "Sintomo: il gruppo sanità vuole sentire chi vede ogni giorno i pazienti sul "
                    "territorio.\nContesto: medicina generale e sanità territoriale; due medici di famiglia di San "
                    "Valentino si sono resi disponibili.\nIntervento e stato: incontro da organizzare per "
                    "raccogliere indicazioni utili alla scheda sanità (liste d'attesa, Case di Comunità, rapporto "
                    "con la USL). Da fare.\nParole chiave: medici di famiglia, medicina generale, medici di base, "
                    "San Valentino, sanità territoriale",
                    ["medici di famiglia", "medicina generale", "medici di base", "San Valentino",
                     "sanità territoriale"])]},
        {"name": "Assemblea pubblica sanità", "who": "sanita", "stage": "Da fare",
         "milestone": "Assemblea sanità", "deadline": 27,
         "description": "sab 28/11, con gli operatori del PS se vengono",
         "keywords": ["assemblea pubblica sanità", "28 novembre", "pronto soccorso", "operatori sanitari",
                      "ospedale Santa Maria"],
         "notes": [("sanita", 0,
                    "Sintomo: la lista vuole un incontro aperto sulla sanità cittadina, anche con chi lavora in "
                    "ospedale.\nContesto: assemblea pubblica sabato 28/11, con gli operatori del pronto soccorso "
                    "se vengono; temi PS, liste d'attesa, nuovo ospedale; annunciata alla stampa a fine "
                    "ottobre.\nIntervento e stato: da fare; serve confermare la partecipazione degli operatori del "
                    "PS.\nParole chiave: assemblea pubblica sanità, 28 novembre, pronto soccorso, operatori "
                    "sanitari, ospedale",
                    ["assemblea pubblica sanità", "28 novembre", "pronto soccorso", "operatori sanitari",
                     "ospedale Santa Maria"])]},
        {"name": "Numeri del PS", "who": "sanita", "stage": "In attesa",
         "description": "accessi e attese: dati affidabili non ne abbiamo",
         "notes": [("sanita", 10, "quelli che girano su facebook non hanno fonte. non usarli"),
                   ("sanita", 0,
                    "Sintomo: per parlare del pronto soccorso servono numeri su accessi e attese, ma quelli che "
                    "girano su Facebook non hanno fonte.\nContesto: dati ufficiali degli accessi al pronto "
                    "soccorso e dei tempi di attesa non disponibili alla lista.\nIntervento e stato: deciso di non "
                    "usare cifre senza fonte. In attesa di dati affidabili.\nParole chiave: pronto soccorso, PS, "
                    "accessi, tempi di attesa, dati senza fonte, statistiche",
                    ["pronto soccorso", "PS", "accessi", "tempi di attesa", "dati senza fonte",
                     "statistiche sanitarie"])],
         "keywords": ["pronto soccorso", "PS", "accessi", "tempi di attesa", "dati senza fonte",
                      "statistiche sanitarie"]},
        {"name": "Volantino sanità per i gazebo", "who": "stampa", "stage": "Da fare",
         "keywords": ["volantino sanità", "gazebo", "materiale informativo", "liste d'attesa", "ospedale"],
         "notes": [("stampa", 0,
                    "Sintomo: ai gazebo serve materiale sulla sanità da dare ai cittadini.\nContesto: volantino "
                    "del gruppo sanità basato sulle schede programma (liste d'attesa, pronto soccorso, nuovo "
                    "ospedale) e solo su dati con fonte.\nIntervento e stato: da fare, nessun testo ancora; da "
                    "scrivere quando le schede sanità sono chiuse, senza numeri del PS non verificati.\nParole "
                    "chiave: volantino sanità, gazebo, materiale informativo, sanità, liste d'attesa, ospedale",
                    ["volantino sanità", "gazebo", "materiale informativo", "liste d'attesa", "ospedale"])]},
    ],
    "updates": [
        ("Sanità", "on_track", 35, 9, "risposta agli operatori del PS mandata. ospedale: in bozza i nostri punti, "
                                      "sito da definire. CdC: aspettiamo la USL."),
    ],
}

PROJECT_LAV = {
    "name": P_LAV, "tags": ["lavoro", "acciaieria", "sviluppo"],
    "description": "<p>Gruppo lavoro: acciaieria, chimica di Polymer, piccole imprese, commercio, appalti del "
                   "Comune. Referente Sergio.</p>",
    "milestones": [("Impegno mense e pulizie", -20, 20), ("Bozza capitolo lavoro", 20, None)],
    "tasks": [
        {"name": "Acciaieria: cosa chiediamo sull'attuazione", "who": "lavoro", "stage": "In corso",
         "milestone": "Bozza capitolo lavoro",
         "notes": [("lavoro", 30, "ricordo: l'accordo è firmato (giugno 2025), al gazebo c'è ancora chi dice "
                                  "«quando lo firmano». siamo ai controlli: comitato esecutivo al MIMIT il 28/9 "
                                  "sui costi dell'energia"),
                   ("lavoro", 14, "le nostre richieste per la scheda: il Comune ai tavoli di monitoraggio, "
                                  "occupati diretti e indiretti contati ogni 6 mesi, investimenti ambientali "
                                  "(polveri, scorie) con cronoprogramma pubblico, la cassa integrazione non usata "
                                  "per ristrutturare"),
                   ("lead", 12, "ok. «chiediamo», non «pretendiamo»"),
                   ("lavoro", 0,
                    "Sintomo: al gazebo c'è ancora chi chiede «quando lo firmano» l'accordo per "
                    "l'acciaieria.\nContesto: accordo di programma AST (Acciai Speciali Terni, gruppo Arvedi) "
                    "firmato a giugno 2025; il 28/09/2026 primo comitato esecutivo al MIMIT sui costi "
                    "dell'energia: fase di attuazione e monitoraggio.\nIntervento e stato: richieste per la "
                    "scheda: Comune ai tavoli di monitoraggio, occupati diretti e indiretti contati ogni 6 mesi, "
                    "investimenti ambientali su polveri e scorie con cronoprogramma pubblico, cassa integrazione "
                    "non usata per ristrutturare. Tono: «chiediamo». In corso.\nParole chiave: acciaieria, AST, "
                    "Arvedi, accordo di programma, MIMIT, comitato esecutivo, cassa integrazione, occupazione",
                    ["acciaieria", "AST", "Acciai Speciali Terni", "Arvedi", "accordo di programma", "MIMIT",
                     "comitato esecutivo", "cassa integrazione", "monitoraggio occupazione"])],
         "keywords": ["acciaieria", "AST", "Acciai Speciali Terni", "Arvedi", "accordo di programma", "MIMIT",
                      "comitato esecutivo", "cassa integrazione", "monitoraggio occupazione"]},
        {"name": "Riunione ditte della subfornitura (Polymer)", "who": "lavoro", "stage": "Fatto",
         "notes": [("lavoro", 19, "mer sera a Polymer: 9 titolari di ditte che lavorano per acciaieria e chimica "
                                  "+ un'associazione di artigiani. problemi: pagamenti a 120 gg, energia, "
                                  "apprendisti che non si trovano. deciso: 1) nel programma un fondo di garanzia "
                                  "comunale per il credito alle piccole ditte 2) sportello comunale bandi 3) ci "
                                  "rivediamo a gennaio con la bozza"),
                   ("lavoro", 17, "verbale in drive /lavoro"),
                   ("lavoro", 0,
                    "Sintomo: titolari di piccole ditte dell'indotto lamentano pagamenti a 120 giorni, energia "
                    "cara e apprendisti introvabili.\nContesto: riunione serale a Polymer con 9 imprese che "
                    "lavorano per acciaieria e chimica e un'associazione di artigiani; subfornitura e indotto "
                    "industriale.\nIntervento e stato: deciso di inserire nel programma un fondo di garanzia "
                    "comunale per il credito alle piccole imprese e uno sportello comunale bandi; nuovo incontro a "
                    "gennaio con la bozza. Verbale in drive. Fatto.\nParole chiave: subfornitura, indotto, "
                    "Polymer, piccole imprese, artigiani, fondo di garanzia, credito, sportello bandi",
                    ["subfornitura", "indotto", "Polymer", "piccole imprese", "artigiani", "fondo di garanzia",
                     "accesso al credito", "sportello bandi", "ritardi nei pagamenti"])],
         "keywords": ["subfornitura", "indotto", "Polymer", "piccole imprese", "artigiani", "fondo di garanzia",
                      "accesso al credito", "sportello bandi", "ritardi nei pagamenti"]},
        {"name": "Negozi del centro: idee per il programma", "who": "lavoro", "stage": "In corso",
         "notes": [("lavoro", 24, "giro in centro con alcuni negozianti: vetrine vuote, affitti alti, parcheggi. "
                                  "idee: 1) canone agevolato per chi apre in un fondo vuoto da più di un anno, "
                                  "con sconto IMU ai proprietari 2) stop a nuove grandi superfici fuori città "
                                  "finché il centro si svuota 3) eventi tutto l'anno non solo a Natale 4) "
                                  "consegne a domicilio in comune tra i negozi"),
                   ("lead", 10, "il punto 2 è delicato: da definire al tavolo"),
                   ("lavoro", 0,
                    "Sintomo: i negozianti del centro mostrano vetrine vuote, affitti alti e mancanza di "
                    "parcheggi.\nContesto: commercio di prossimità e centro storico; strumenti: canone agevolato e "
                    "sconto IMU per i fondi sfitti, limiti alle grandi superfici di vendita fuori "
                    "città.\nIntervento e stato: idee: canone agevolato per chi apre in un fondo vuoto da oltre un "
                    "anno, eventi tutto l'anno, consegne a domicilio comuni; lo stop alle grandi superfici è da "
                    "definire al tavolo. In corso.\nParole chiave: negozi del centro, commercio, vetrine vuote, "
                    "fondi sfitti, IMU, grande distribuzione, centri commerciali, centro storico",
                    ["negozi del centro", "commercio di vicinato", "vetrine vuote", "fondi sfitti", "sconto IMU",
                     "grandi superfici di vendita", "centri commerciali", "centro storico"])],
         "keywords": ["negozi del centro", "commercio di vicinato", "vetrine vuote", "fondi sfitti", "sconto IMU",
                      "grandi superfici di vendita", "centri commerciali", "centro storico"]},
        {"name": "H2 nell'area industriale: documento del gruppo", "who": "lavoro", "stage": "In corso",
         "milestone": "Bozza capitolo lavoro",
         "notes": [("lavoro", 28, "il gruppo vuole una pagina sull'H2. priorità: i soldi della transizione per "
                                  "decarbonizzare acciaieria e trasporto pesante; filiera con l'università; aree "
                                  "dismesse per gli impianti"),
                   ("lavoro", 21, "NB quali fondi ci sono davvero non l'abbiamo verificato: niente cifre finché "
                                  "non abbiamo i bandi in mano. da chiedere a un tecnico"),
                   ("lavoro", 7, "bozza v2 in drive, solo indirizzi senza cifre"),
                   ("lavoro", 0,
                    "Sintomo: il gruppo lavoro vuole una pagina sull'idrogeno per l'area industriale.\nContesto: "
                    "idrogeno (H2) per decarbonizzare acciaieria e trasporto pesante, filiera con l'università, "
                    "aree dismesse per gli impianti; fondi della transizione non verificati.\nIntervento e stato: "
                    "bozza v2 in drive con soli indirizzi, nessuna cifra finché non ci sono i bandi; da sentire un "
                    "tecnico. In corso.\nParole chiave: idrogeno, H2, hydrogen valley, decarbonizzazione, "
                    "transizione energetica, area industriale, aree dismesse, università",
                    ["idrogeno", "H2", "hydrogen valley", "decarbonizzazione", "transizione energetica",
                     "area industriale", "aree dismesse", "polo universitario"])],
         "keywords": ["idrogeno", "H2", "hydrogen valley", "decarbonizzazione", "transizione energetica",
                      "area industriale", "aree dismesse", "polo universitario"]},
        {"name": "Lettera lavoratrici mense e pulizie", "who": "lavoro", "stage": "Fatto",
         "milestone": "Impegno mense e pulizie",
         "notes": [("lavoro", 26, "incontro con lavoratrici delle mense scolastiche e delle pulizie degli uffici "
                                  "comunali: part time che non hanno scelto, paura del cambio di ditta"),
                   ("lavoro", 20, "impegno scritto della lista, firmato da Fra: in ogni gara del Comune "
                                  "riassorbimento di tutto il personale al cambio d'appalto con le stesse ore e lo "
                                  "stesso contratto nazionale, niente ribassi sul costo del lavoro, controlli del "
                                  "Comune su paghe e turni. consegnata a mano il 12/10"),
                   ("lead", 19, "copia in drive /lavoro/impegni"),
                   ("lavoro", 0,
                    "Sintomo: lavoratrici delle mense scolastiche e delle pulizie degli uffici comunali denunciano "
                    "part time non scelto e paura del cambio di ditta.\nContesto: appalti di servizi del Comune, "
                    "cambio d'appalto, clausola sociale, contratto collettivo nazionale, ribassi sul costo del "
                    "lavoro.\nIntervento e stato: impegno scritto della lista firmato dalla coordinatrice e "
                    "consegnato a mano il 12/10: riassorbimento di tutto il personale con stesse ore e stesso "
                    "contratto, niente ribassi sul lavoro, controlli comunali su paghe e turni. Copia in drive. "
                    "Fatto.\nParole chiave: mense scolastiche, pulizie, appalti comunali, clausola sociale, cambio "
                    "d'appalto, part time involontario, lavoratrici",
                    ["mense scolastiche", "pulizie uffici comunali", "appalti comunali", "clausola sociale",
                     "cambio d'appalto", "part time involontario", "lavoratrici", "contratto nazionale"])],
         "keywords": ["mense scolastiche", "pulizie uffici comunali", "appalti comunali", "clausola sociale",
                      "cambio d'appalto", "part time involontario", "lavoratrici", "contratto nazionale"]},
        {"name": "Disoccupazione giovanile: dati", "who": "lavoro", "stage": "Da fare",
         "description": "dati verificati non ne abbiamo, cercare ISTAT",
         "keywords": ["disoccupazione giovanile", "lavoro giovani", "NEET", "ISTAT", "tasso di disoccupazione"],
         "notes": [("lavoro", 0,
                    "Sintomo: per la scheda lavoro e giovani manca un numero affidabile sulla disoccupazione dei "
                    "ragazzi a Terni.\nContesto: nessun dato verificato disponibile; fonte da cercare: "
                    "ISTAT.\nIntervento e stato: serve per le schede lavoro e giovani; da fare la ricerca dei dati "
                    "ufficiali; fino ad allora nessuna cifra nei testi.\nParole chiave: disoccupazione giovanile, "
                    "lavoro giovani, NEET, ISTAT, tasso di disoccupazione, dati ufficiali",
                    ["disoccupazione giovanile", "lavoro giovani", "NEET", "ISTAT", "tasso di disoccupazione"])]},
        {"name": "Incontro con il polo universitario", "who": "lavoro", "stage": "Da fare",
         "keywords": ["polo universitario", "università", "ricerca", "filiera idrogeno", "giovani laureati"],
         "notes": [("lavoro", 0,
                    "Sintomo: il gruppo lavoro vuole coinvolgere l'università nel programma sullo "
                    "sviluppo.\nContesto: polo universitario di Terni, collegato al documento sull'idrogeno "
                    "(filiera con l'università) e alle politiche per i giovani.\nIntervento e stato: incontro da "
                    "organizzare, nessun contatto registrato né data fissata; utile per la filiera dell'idrogeno e "
                    "per le sale studio. Da fare.\nParole chiave: polo universitario, università, ricerca, "
                    "filiera, idrogeno, giovani laureati",
                    ["polo universitario", "università", "ricerca", "filiera idrogeno", "giovani laureati"])]},
        {"name": "Ternana e stadio: cosa diciamo", "who": "portavoce", "stage": "In corso",
         "notes": [("portavoce", 15, "solo i fatti con fonte (liquidazione, Nuova Ternana, stadio-clinica). "
                                     "tifosi divisi, non ci mettiamo a fare il tifo"),
                   ("portavoce", 0,
                    "Sintomo: ai gazebo si chiede alla lista cosa pensa della Ternana e dello stadio; i tifosi "
                    "sono divisi.\nContesto: Ternana in liquidazione giudiziale (udienza 17/04/2026), nascita "
                    "della Nuova Ternana 1925 in serie D promossa dal sindaco, progetto stadio-clinica dopo la "
                    "rinuncia del Comune al Consiglio di Stato.\nIntervento e stato: deciso di citare solo i fatti "
                    "con fonte, senza prendere posizione da tifosi. In corso.\nParole chiave: Ternana, Nuova "
                    "Ternana 1925, stadio-clinica, stadio, liquidazione giudiziale, tifosi, serie D",
                    ["Ternana", "Nuova Ternana 1925", "stadio-clinica", "stadio", "liquidazione giudiziale",
                     "tifosi", "serie D", "Bandecchi"])],
         "keywords": ["Ternana", "Nuova Ternana 1925", "stadio-clinica", "stadio", "liquidazione giudiziale",
                      "tifosi", "serie D", "Bandecchi"]},
        {"name": "Turismo: Marmore e Valnerina", "who": "lavoro", "stage": "Da fare",
         "keywords": ["turismo", "Cascata delle Marmore", "Marmore", "Valnerina", "sviluppo turistico"],
         "notes": [("lavoro", 0,
                    "Sintomo: il gruppo lavoro vuole un capitolo sul turismo come leva di sviluppo.\nContesto: "
                    "Cascata delle Marmore e Valnerina, attrattori turistici del territorio ternano.\nIntervento e "
                    "stato: da fare, nessuna bozza né proposta registrata; il capitolo va collegato alle schede su "
                    "mobilità e commercio del centro. Da scrivere nel gruppo lavoro, acciaieria e "
                    "sviluppo.\nParole chiave: turismo, Cascata delle Marmore, Marmore, Valnerina, sviluppo "
                    "turistico, attrattori",
                    ["turismo", "Cascata delle Marmore", "Marmore", "Valnerina", "sviluppo turistico"])]},
    ],
    "updates": [
        ("Lavoro", "on_track", 40, 10, "impegno scritto per mense e pulizie consegnato. ditte di Polymer: ci "
                                       "rivediamo a gennaio. H2 senza cifre finché non verifichiamo i fondi."),
    ],
}

# -- the thematic projects (2/2) and the work of the list ------------------------------------------------------
PROJECT_PART = {
    "name": P_PART, "tags": ["partecipazione", "trasparenza", "opposizione"],
    "description": "<p>Opposizione alla giunta fuori dall'aula (noi in consiglio non ci siamo), trasparenza, "
                   "partecipazione dei quartieri. Referenti Michele e Fra.</p>",
    "milestones": [("Schedario episodi", -3, 3), ("Bozza capitolo partecipazione", 18, None)],
    "tasks": [
        {"name": "Raccolta episodi del sindaco con fonte", "who": "portavoce", "stage": "Fatto",
         "milestone": "Schedario episodi",
         "description": "quello che si può citare, con link e data. serve a noi e ai consiglieri se ce lo chiedono",
         "notes": [("portavoce", 5, "messo in fila, solo roba con link e data, niente sentito dire:\n"
                                    "- lug 2023: insulti in consiglio alla segretaria generale che aveva sollevato "
                                    "dubbi di incompatibilità, il sindacato dei segretari comunali condanna "
                                    "(Lentepubblica)\n"
                                    "- 31/8/2023: dopo lo scontro in aula con il consigliere FdI Cecconi la Procura "
                                    "lo iscrive tra gli indagati (minacce, oltraggio, interruzione di pubblico "
                                    "servizio); lui: «Lo rifarei» (Sky TG24)\n"
                                    "- 8/2/2024: annuncia in un video le dimissioni «per motivi politici», poi "
                                    "resta (Sky TG24)\n"
                                    "- 29/9/2025: su Gaza «20mila bambini non sono mai morti», contestazione "
                                    "davanti al Comune, i consiglieri di csx escono dall'aula (L'Espresso)\n"
                                    "- 29/10/2026: «servono 17 voti e loro non ci arriveranno mai» (Quotidiano "
                                    "dell'Umbria)\n"
                                    "le schede con i link sono nella rassegna"),
                   ("stampa", 4, "i 7 video: schede fatte, nessuno guardato per i minuti. niente frasi prese dai "
                                 "video finché qualcuno non li guarda"),
                   ("lead", 3, "su giornalisti e Regione non abbiamo altro di verificato oltre a questo. non "
                               "aggiungete cose a memoria"),
                   ("portavoce", 0,
                    "Sintomo: la lista e i consiglieri di opposizione chiedono un elenco citabile dei "
                    "comportamenti del sindaco, solo con link e data.\nContesto: episodi con fonte: luglio 2023 "
                    "insulti in consiglio alla segretaria generale (Lentepubblica); 31/8/2023 indagine dopo lo "
                    "scontro in aula con un consigliere FdI (Sky TG24); 8/2/2024 dimissioni annunciate e ritirate "
                    "(Sky TG24); 29/9/2025 frase su Gaza e contestazione (L'Espresso); 29/10/2026 i 17 voti "
                    "(Quotidiano dell'Umbria).\nIntervento e stato: elenco fatto, schede in rassegna; i 7 video "
                    "non ancora visti, nessuna frase dai video. Fatto.\nParole chiave: sindaco, Bandecchi, "
                    "episodi, segretaria generale, indagato, dimissioni, Gaza, rassegna",
                    ["il sindaco", "Bandecchi", "episodi con fonte", "segretaria generale", "sindaco indagato",
                     "dimissioni annunciate", "Gaza", "Alternativa Popolare", "Dimensione"])],
         "keywords": ["il sindaco", "Bandecchi", "episodi con fonte", "segretaria generale", "sindaco indagato",
                      "dimissioni annunciate", "Gaza", "Alternativa Popolare", "Dimensione"]},
        {"name": "Sfiducia: cosa facciamo noi", "who": "lead", "stage": "In corso",
         "notes": [("lead", 4, "noi non firmiamo niente, non siamo in aula. sosteniamo in pubblico la richiesta "
                               "di mandarlo a casa, sempre coi fatti (vedi fatti 26-31/10)"),
                   ("portavoce", 3, "post di sabato: solo fatti con fonte, nessun nome dei quattro"),
                   ("lead", 0,
                    "Sintomo: volontari e simpatizzanti chiedono se la lista firma la mozione per mandare a casa "
                    "il sindaco.\nContesto: mozione di sfiducia (TUEL art. 52: 13 firme, 17 voti) promossa dai "
                    "gruppi consiliari; la lista non ha consiglieri in aula; fatti del 26-31/10 con fonte, nascita "
                    "del gruppo Per Terni.\nIntervento e stato: la lista non firma nulla, sostiene in pubblico la "
                    "richiesta con i fatti; il post di sabato solo con fatti e fonti, senza nomi dei quattro "
                    "consiglieri. In corso.\nParole chiave: sfiducia, mozione di sfiducia, TUEL 52, scioglimento "
                    "del consiglio, Bandecchi, sindaco, Per Terni",
                    ["sfiducia", "mozione di sfiducia", "TUEL art. 52", "scioglimento del consiglio",
                     "mandare a casa il sindaco", "Bandecchi", "Per Terni", "crisi di maggioranza"])],
         "keywords": ["sfiducia", "mozione di sfiducia", "TUEL art. 52", "scioglimento del consiglio",
                      "mandare a casa il sindaco", "Bandecchi", "Per Terni", "crisi di maggioranza"]},
        {"name": "Scheda partecipazione: quartieri e dirette", "who": "lead", "stage": "In corso",
         "milestone": "Bozza capitolo partecipazione",
         "notes": [("lead", 22, "proposta: ogni anno una quota degli investimenti decisa dai quartieri, con "
                                "assemblee e voto anche online (1-2%); commissioni consiliari in diretta video e "
                                "registrate sul sito, scritto nel regolamento e non a discrezione del presidente; "
                                "ordini del giorno pubblicati 5 gg prima"),
                   ("sociale", 15, "aggiungere le consulte dei giovani"),
                   ("lead", 6, "v2 in drive /programma/partecipazione"),
                   ("lead", 0,
                    "Sintomo: i cittadini non sanno cosa si decide in Comune e non hanno voce sugli investimenti "
                    "di quartiere.\nContesto: bilancio partecipativo (1-2% degli investimenti), commissioni "
                    "consiliari in diretta video e registrate, regolamento del consiglio comunale, ordini del "
                    "giorno pubblicati 5 giorni prima, consulte dei giovani.\nIntervento e stato: proposta "
                    "scritta, v2 in drive con l'aggiunta delle consulte giovanili. In corso.\nParole chiave: "
                    "bilancio partecipativo, partecipazione, quartieri, dirette streaming, commissioni consiliari, "
                    "trasparenza, consulta giovani",
                    ["bilancio partecipativo", "partecipazione", "assemblee di quartiere", "dirette streaming",
                     "commissioni consiliari", "regolamento del consiglio", "consulta dei giovani", "trasparenza"])],
         "keywords": ["bilancio partecipativo", "partecipazione", "assemblee di quartiere", "dirette streaming",
                      "commissioni consiliari", "regolamento del consiglio", "consulta dei giovani", "trasparenza"]},
        {"name": "Serata dell'Osservatorio civico sulle società comunali", "who": "lavoro", "stage": "Fatto",
         "notes": [("lavoro", 23, "per la lista c'eravamo io e Paolo. l'Osservatorio civico (gruppo di "
                                  "cittadini) ha messo in fila: incarichi nei CdA dati senza avviso pubblico "
                                  "(secondo loro), compensi non pubblicati in amministrazione trasparente, "
                                  "bilanci di due società approvati in ritardo. tutto da verificare sugli atti, "
                                  "in pubblico non ripetiamo niente prima"),
                   ("mandatario", 21, "scaricato dal sito del Comune l'elenco delle società e gli ultimi bilanci, "
                                      "li confronto io"),
                   ("lavoro", 0,
                    "Sintomo: l'Osservatorio civico, gruppo di cittadini, denuncia poca trasparenza nelle società "
                    "partecipate dal Comune.\nContesto: secondo loro incarichi nei CdA senza avviso pubblico, "
                    "compensi non pubblicati in amministrazione trasparente, bilanci di due società approvati in "
                    "ritardo; tutto da verificare sugli atti.\nIntervento e stato: presenti due della lista; "
                    "scaricati dal sito del Comune l'elenco delle società e gli ultimi bilanci per il confronto. "
                    "In pubblico nulla prima della verifica. Fatto.\nParole chiave: società partecipate, società "
                    "comunali, Osservatorio civico, CdA, nomine, amministrazione trasparente, compensi, bilanci",
                    ["società partecipate", "società comunali", "Osservatorio civico", "nomine nei CdA",
                     "amministrazione trasparente", "compensi", "bilanci in ritardo"])],
         "keywords": ["società partecipate", "società comunali", "Osservatorio civico", "nomine nei CdA",
                      "amministrazione trasparente", "compensi", "bilanci in ritardo"]},
        {"name": "Accesso civico: atti da chiedere", "who": "lead", "stage": "Da fare",
         "description": "elenco: verde, società, appalti mense",
         "keywords": ["accesso civico", "FOIA", "accesso agli atti", "verde pubblico", "società partecipate",
                      "appalti mense", "trasparenza amministrativa"],
         "notes": [("lead", 0,
                    "Sintomo: per controllare la giunta servono documenti che non sono pubblici sul sito del "
                    "Comune.\nContesto: accesso civico generalizzato (FOIA) e accesso agli atti su tre filoni: "
                    "verde pubblico e abbattimenti, società partecipate, appalti delle mense.\nIntervento e stato: "
                    "elenco degli atti da chiedere definito; richieste da preparare. Da fare.\nParole chiave: "
                    "accesso civico, FOIA, accesso agli atti, verde pubblico, società partecipate, appalti mense, "
                    "trasparenza",
                    ["accesso civico", "FOIA", "accesso agli atti", "verde pubblico", "società partecipate",
                     "appalti mense", "trasparenza amministrativa"])]},
        {"name": "Chi segue le sedute del consiglio", "who": "portavoce", "stage": "In corso",
         "notes": [("portavoce", 7, "turni per seguire le sedute: io, Sergio, Luisa. appunti in drive il giorno "
                                    "dopo"),
                   ("portavoce", 0,
                    "Sintomo: la lista non ha consiglieri in aula e rischia di non sapere cosa succede in "
                    "consiglio comunale.\nContesto: sedute del consiglio comunale di Terni seguite dal pubblico o "
                    "in diretta, con appunti condivisi.\nIntervento e stato: turni fra tre volontari per seguire "
                    "le sedute; appunti in drive il giorno dopo. In corso.\nParole chiave: sedute del consiglio "
                    "comunale, consiglio comunale, turni, appunti, monitoraggio, opposizione, diretta",
                    ["sedute del consiglio comunale", "consiglio comunale", "turni sedute", "appunti",
                     "monitoraggio dell'aula", "diretta consiglio"])],
         "keywords": ["sedute del consiglio comunale", "consiglio comunale", "turni sedute", "appunti",
                      "monitoraggio dell'aula", "diretta consiglio"]},
        {"name": "Bilancio di previsione: cosa guardare", "who": "mandatario", "stage": "Da fare",
         "description": "il sindaco dice che la prossima prova è il bilancio di previsione (QdU 29/10)",
         "keywords": ["bilancio di previsione", "bilancio comunale", "voto in consiglio",
                      "tenuta della maggioranza", "Bandecchi", "il sindaco", "crisi in Comune"],
         "notes": [("mandatario", 0,
                    "Sintomo: il sindaco dice che la prossima prova della maggioranza sarà il bilancio di "
                    "previsione; la lista vuole sapere cosa guardare.\nContesto: Quotidiano dell'Umbria del "
                    "29/10/2026: il sindaco dichiara di avere 15 consiglieri e indica il bilancio di previsione "
                    "come prossimo passaggio; voto in consiglio comunale, crisi di maggioranza in "
                    "corso.\nIntervento e stato: da fare l'analisi delle voci e dei numeri dell'aula.\nParole "
                    "chiave: bilancio di previsione, bilancio comunale, voto in consiglio, maggioranza, Bandecchi, "
                    "sindaco, crisi in Comune",
                    ["bilancio di previsione", "bilancio comunale", "voto in consiglio", "tenuta della maggioranza",
                     "Bandecchi", "il sindaco", "crisi in Comune"])]},
        {"name": "Volantino: perché il consiglio va sciolto", "who": "stampa", "stage": "In attesa",
         "notes": [("stampa", 3, "bozza con 5 fatti e 5 link. aspetto Michele"),
                   ("portavoce", 2, "togli l'aggettivo «indecente», lasciamo parlare i fatti"),
                   ("stampa", 0,
                    "Sintomo: i volontari chiedono un volantino che spieghi perché il consiglio comunale deve "
                    "andare a casa.\nContesto: bozza con 5 fatti e 5 link (crisi di maggioranza, sfiducia, "
                    "dimissioni contestuali, scioglimento ex TUEL art. 141); regola della lista: ogni cosa sul "
                    "sindaco con fonte e data.\nIntervento e stato: in attesa del via del portavoce; tolto "
                    "l'aggettivo «indecente», si lasciano parlare i fatti.\nParole chiave: volantino scioglimento, "
                    "scioglimento del consiglio, sfiducia, mandare a casa, Bandecchi, fatti con fonte, crisi di "
                    "maggioranza",
                    ["volantino scioglimento", "scioglimento del consiglio comunale", "sfiducia",
                     "mandare a casa il sindaco", "Bandecchi", "fatti con fonte", "crisi di maggioranza"])],
         "keywords": ["volantino scioglimento", "scioglimento del consiglio comunale", "sfiducia",
                      "mandare a casa il sindaco", "Bandecchi", "fatti con fonte", "crisi di maggioranza"]},
        {"name": "Dati aperti del Comune", "who": "lead", "stage": "Da fare",
         "keywords": ["dati aperti", "open data", "trasparenza", "amministrazione trasparente",
                      "portale dati comunale"],
         "notes": [("lead", 0,
                    "Sintomo: la lista vuole dati pubblici del Comune riutilizzabili per controllare e "
                    "proporre.\nContesto: open data, amministrazione trasparente, portale dei dati del Comune di "
                    "Terni; collegato alla scheda partecipazione.\nIntervento e stato: da fare, nessuna attività "
                    "registrata; collegato alle richieste di accesso civico su verde, società partecipate e "
                    "appalti delle mense.\nParole chiave: dati aperti, open data, trasparenza, amministrazione "
                    "trasparente, portale dati, riuso",
                    ["dati aperti", "open data", "trasparenza", "amministrazione trasparente",
                     "portale dati comunale"])]},
    ],
    "updates": [
        ("Partecipazione e opposizione", "on_track", 45, 3, "schedario degli episodi fatto, solo con fonte. "
                                                           "sfiducia: noi non siamo in aula, sosteniamo in "
                                                           "pubblico. scheda quartieri e dirette alla v2."),
    ],
}

PROJECT_CAMP = {
    "name": P_CAMP, "tags": ["campagna", "volontari", "coalizione"],
    "description": "<p>Campagna e organizzazione: gazebo, volontari, social, materiali, tavolo di coalizione. "
                   "Referenti Fra (tavolo), Teo (gazebo), Giada (materiali).</p>",
    "milestones": [("Volantino quartieri in stampa", -5, 5), ("Presentazione pubblica della lista", 13, None),
                   ("Contributi alla bozza comune", 19, None)],
    "tasks": [
        {"name": "Calendario gazebo novembre", "who": "banchetti", "stage": "In corso",
         "notes": [("banchetti", 4, "prossime 2 settimane: sab 7 Borgo Bovio (mercato), dom 8 mattina piazza "
                                    "Tacito, mer 11 pomeriggio Città Giardino, sab 14 Cesi, dom 15 San Valentino, "
                                    "mer 18 Polymer all'uscita dei turni. foglio turni aggiornato"),
                   ("banchetti", 3, "dom mattina in piazza Tacito coordino io, con Ilaria e Gigi. suolo pubblico "
                                    "chiesto"),
                   ("lead", 2, "a piazza Tacito passa anche Michele dalle 11"),
                   ("banchetti", 0,
                    "Sintomo: i volontari chiedono dove e quando sono i gazebo delle prossime "
                    "settimane.\nContesto: sab 7 Borgo Bovio (mercato), dom 8 piazza Tacito, mer 11 Città "
                    "Giardino, sab 14 Cesi, dom 15 San Valentino, mer 18 Polymer all'uscita dei turni; occupazione "
                    "di suolo pubblico chiesta.\nIntervento e stato: foglio turni aggiornato, coordinamento di "
                    "piazza Tacito definito, passaggio del portavoce dalle 11. In corso.\nParole chiave: "
                    "calendario gazebo, banchetti, turni volontari, suolo pubblico, piazza Tacito, Borgo Bovio, "
                    "Polymer, novembre",
                    ["calendario gazebo", "banchetti", "turni volontari", "occupazione suolo pubblico",
                     "piazza Tacito", "Borgo Bovio", "Polymer", "Città Giardino"])],
         "keywords": ["calendario gazebo", "banchetti", "turni volontari", "occupazione suolo pubblico",
                      "piazza Tacito", "Borgo Bovio", "Polymer", "Città Giardino"]},
        {"name": "Tavolo di coalizione: riunione del 30/10", "who": "lead", "stage": "Fatto",
         "milestone": "Contributi alla bozza comune",
         "description": "verbale interno, non si gira",
         "notes": [("lead", 2, "presenti i delegati di sei forze del csx + noi + altre 2 civiche. bozza di "
                               "documento comune: indice in 8 capitoli approvato, contributi di ognuno entro il "
                               "20/11; casa e partecipazione li scriviamo noi. nomi: nessuno, né per sindaco né "
                               "per le liste. la delegata del tavolo propone di aspettare come va la sfiducia "
                               "prima di parlare di candidature. prossima riunione 13/11"),
                   ("portavoce", 1, "fuori si dice solo «lavoriamo al programma comune». niente su chi ha detto "
                                    "cosa"),
                   ("lead", 0,
                    "Sintomo: la lista partecipa al tavolo del centrosinistra per il programma comune e deve "
                    "sapere cosa riportare.\nContesto: presenti i delegati di sei forze del centrosinistra, la "
                    "lista e altre 2 civiche; bozza di documento comune con indice in 8 capitoli, contributi entro "
                    "il 20/11; casa e partecipazione scritti dalla lista; nessun nome per candidato sindaco o "
                    "liste, si aspetta l'esito della sfiducia.\nIntervento e stato: verbale interno, non circola. "
                    "Fuori si dice solo «lavoriamo al programma comune». Prossima riunione 13/11. Fatto.\nParole "
                    "chiave: tavolo di coalizione, centrosinistra, programma comune, bozza comune, candidature, "
                    "verbale riservato, civiche",
                    ["tavolo di coalizione", "centrosinistra", "csx", "programma comune", "bozza comune",
                     "candidato sindaco", "verbale riservato", "liste civiche"])],
         "keywords": ["tavolo di coalizione", "centrosinistra", "csx", "programma comune", "bozza comune",
                      "candidato sindaco", "verbale riservato", "liste civiche"]},
        {"name": "Volantino quartieri: versione finale", "who": "stampa", "stage": "Fatto",
         "milestone": "Volantino quartieri in stampa", "attachment": "stage_report",
         "notes": [("stampa", 6, "pdf definitivo approvato da Fra: drive /grafica/volantini/DEF/"
                                 "volantino_quartieri_v3_def.pdf, sorgenti del grafico in /grafica/sorgenti. NON "
                                 "usare quelli della cartella bozze"),
                   ("stampa", 5, "mandato a Conca Grafica, 5000 copie, metà per Borgo Bovio. preventivo allegato"),
                   ("banchetti", 2, "le copie per Borgo Bovio le ritiro gio, si girano al gazebo di sab"),
                   ("stampa", 0,
                    "Sintomo: serve il volantino dei quartieri stampato in tempo per i gazebo.\nContesto: pdf "
                    "definitivo approvato in /grafica/volantini/DEF/ (volantino_quartieri_v3_def.pdf), sorgenti in "
                    "/grafica/sorgenti; vietato usare la cartella bozze dopo un errore di stampa "
                    "precedente.\nIntervento e stato: inviato alla tipografia Conca Grafica, 5000 copie, metà per "
                    "Borgo Bovio, preventivo allegato; copie ritirate per il gazebo di sabato. Fatto.\nParole "
                    "chiave: volantino quartieri, stampa, tipografia, Conca Grafica, file definitivo, cartella "
                    "DEF, Borgo Bovio",
                    ["volantino quartieri", "stampa volantini", "tipografia", "Conca Grafica", "file definitivo",
                     "cartella DEF", "Borgo Bovio"])],
         "keywords": ["volantino quartieri", "stampa volantini", "tipografia", "Conca Grafica", "file definitivo",
                      "cartella DEF", "Borgo Bovio"]},
        {"name": "Piano social novembre", "who": "stampa", "stage": "In corso",
         "notes": [("stampa", 8, "3 post a settimana: un tema del programma, un gazebo, un fatto con fonte"),
                   ("stampa", 0,
                    "Sintomo: le pagine social della lista hanno bisogno di un ritmo regolare di "
                    "pubblicazione.\nContesto: pagine Facebook e Instagram «terni2027»; regola: ogni fatto sul "
                    "sindaco con fonte e data.\nIntervento e stato: piano di 3 post a settimana: un tema del "
                    "programma, un gazebo, un fatto con fonte. In corso.\nParole chiave: piano social, piano "
                    "editoriale, post, Facebook, Instagram, terni2027, comunicazione online",
                    ["piano social", "piano editoriale", "post", "Facebook", "Instagram", "terni2027",
                     "comunicazione online"])],
         "keywords": ["piano social", "piano editoriale", "post", "Facebook", "Instagram", "terni2027",
                      "comunicazione online"]},
        {"name": "Presentazione pubblica al CAOS", "who": "lead", "stage": "In corso",
         "milestone": "Presentazione pubblica della lista", "deadline": 13,
         "notes": [("lead", 10, "sala prenotata per sab 14/11 ore 17"),
                   ("portavoce", 6, "scaletta: 5 interventi da 5 minuti, uno per gruppo, poi domande"),
                   ("lead", 0,
                    "Sintomo: la lista vuole presentarsi alla città con un evento pubblico.\nContesto: sala del "
                    "CAOS (Centro Arti Opificio Siri) prenotata per sabato 14/11 alle 17; un intervento per ogni "
                    "gruppo tematico.\nIntervento e stato: scaletta definita: 5 interventi da 5 minuti, poi "
                    "domande dal pubblico; da annunciare sui social e ai gazebo. In corso.\nParole chiave: "
                    "presentazione pubblica, CAOS, evento, 14 novembre, scaletta, lancio della lista",
                    ["presentazione pubblica", "CAOS", "evento di lancio", "14 novembre", "scaletta interventi"])],
         "keywords": ["presentazione pubblica", "CAOS", "evento di lancio", "14 novembre", "scaletta interventi"]},
        {"name": "Formazione volontari dei gazebo", "who": "banchetti", "stage": "Fatto",
         "notes": [("banchetti", 20, "fatta in sede, 14 presenti. vademecum spiegato, modulo consenso provato"),
                   ("banchetti", 0,
                    "Sintomo: i nuovi volontari non sanno come comportarsi al gazebo con contatti, offerte e "
                    "giornalisti.\nContesto: vademecum del gazebo, modulo contatti con consenso separato "
                    "(privacy), ricevute delle offerte, rimando al portavoce per la stampa.\nIntervento e stato: "
                    "formazione fatta in sede con 14 presenti; vademecum spiegato e modulo consenso provato. "
                    "Fatto.\nParole chiave: formazione volontari, vademecum gazebo, modulo consenso, privacy, "
                    "banchetti, istruzioni volontari",
                    ["formazione volontari", "vademecum gazebo", "modulo consenso", "privacy", "banchetti",
                     "istruzioni volontari"])],
         "keywords": ["formazione volontari", "vademecum gazebo", "modulo consenso", "privacy", "banchetti",
                      "istruzioni volontari"]},
        {"name": "Foglio contatti: pulizia", "who": "banchetti", "stage": "In corso",
         "notes": [("banchetti", 9, "tolti 23 contatti senza la casella del consenso"),
                   ("lead", 9, "bene, e quelli che qualcuno aveva preso dal gruppo facebook del quartiere "
                               "vanno via tutti"),
                   ("banchetti", 0,
                    "Sintomo: nel foglio dei contatti ci sono persone che non hanno dato il consenso e altre prese "
                    "da un gruppo Facebook di quartiere.\nContesto: trattamento dei dati per propaganda elettorale "
                    "(Garante privacy 2019): solo contatti con consenso esplicito e separato, mai copiati dai "
                    "social.\nIntervento e stato: tolti 23 contatti senza la casella del consenso; da togliere "
                    "tutti quelli presi dal gruppo Facebook. In corso.\nParole chiave: foglio contatti, consenso, "
                    "privacy, GDPR, Garante privacy, contatti dai social, mailing list",
                    ["foglio contatti", "consenso", "privacy", "GDPR", "Garante privacy",
                     "contatti presi dai social", "mailing list"])],
         "keywords": ["foglio contatti", "consenso", "privacy", "GDPR", "Garante privacy",
                      "contatti presi dai social", "mailing list"]},
        {"name": "Video di presentazione", "who": "stampa", "stage": "Da fare",
         "keywords": ["video di presentazione", "reel", "Instagram", "comunicazione video", "chi siamo"],
         "notes": [("stampa", 0,
                    "Sintomo: la lista vuole un video che spieghi chi è e cosa propone.\nContesto: canali social "
                    "della lista (reel Instagram «perché una lista civica» già pubblicato a ottobre).\nIntervento "
                    "e stato: da fare, nessuna attività registrata; il video va usato su sito, Instagram e "
                    "Facebook della lista, con regole su foto e consenso delle persone riprese.\nParole chiave: "
                    "video di presentazione, reel, Instagram, comunicazione video, chi siamo",
                    ["video di presentazione", "reel", "Instagram", "comunicazione video", "chi siamo"])]},
        {"name": "Disponibilità a candidarsi", "who": "lead", "stage": "In corso",
         "description": "raccolta interna, riservata. servono 21-32 nomi e l'equilibrio di genere",
         "notes": [("lead", 7, "11 disponibilità, 7 uomini 4 donne: serve più equilibrio"),
                   ("lead", 0,
                    "Sintomo: per la lista servono persone disposte a candidarsi al consiglio comunale.\nContesto: "
                    "raccolta interna e riservata; servono 21-32 candidati con il genere tra 1/3 e 2/3 (equilibrio "
                    "di genere, quote di lista).\nIntervento e stato: 11 disponibilità, 7 uomini e 4 donne: serve "
                    "più equilibrio. In corso.\nParole chiave: candidature, candidati consiglieri, disponibilità, "
                    "equilibrio di genere, quote rosa, composizione della lista",
                    ["candidature", "candidati consiglieri", "disponibilità a candidarsi", "equilibrio di genere",
                     "quote rosa", "composizione della lista"])],
         "keywords": ["candidature", "candidati consiglieri", "disponibilità a candidarsi", "equilibrio di genere",
                      "quote rosa", "composizione della lista"]},
        {"name": "Regole del gruppo whatsapp volontari", "who": "banchetti", "stage": "Fatto",
         "notes": [("banchetti", 25, "messaggio fissato: solo organizzazione, niente screenshot di articoli, "
                                     "niente insulti a nessuno"),
                   ("banchetti", 0,
                    "Sintomo: nel gruppo WhatsApp dei volontari girano screenshot di articoli e toni "
                    "accesi.\nContesto: gruppo interno T27 volontari; regole della lista: non si copiano articoli, "
                    "niente insulti.\nIntervento e stato: messaggio fissato: solo organizzazione, niente "
                    "screenshot di articoli, niente insulti a nessuno; articoli solo come scheda con link. "
                    "Fatto.\nParole chiave: gruppo WhatsApp, chat volontari, regole del gruppo, screenshot, "
                    "insulti, T27 volontari",
                    ["gruppo WhatsApp", "chat volontari", "regole del gruppo", "screenshot articoli", "insulti",
                     "T27 volontari"])],
         "keywords": ["gruppo WhatsApp", "chat volontari", "regole del gruppo", "screenshot articoli", "insulti",
                      "T27 volontari"]},
        {"name": "Magliette e gadget", "who": "banchetti", "stage": "Da fare",
         "keywords": ["magliette", "gadget", "merchandising", "materiale promozionale", "logo"],
         "notes": [("banchetti", 0,
                    "Sintomo: i volontari chiedono magliette e materiale riconoscibile per i gazebo.\nContesto: "
                    "materiale promozionale della lista con il logo per social e gazebo; spese da registrare "
                    "secondo le regole della campagna.\nIntervento e stato: da fare, nessuna attività registrata; "
                    "prima serve il logo definitivo, poi i preventivi e la registrazione della spesa sul conto "
                    "della lista.\nParole chiave: magliette, gadget, merchandising, materiale promozionale, logo, "
                    "gazebo",
                    ["magliette", "gadget", "merchandising", "materiale promozionale", "logo"])]},
        {"name": "Sito della lista", "who": "stampa", "stage": "In corso",
         "notes": [("stampa", 12, "pagina programma e pagina gazebo online"),
                   ("stampa", 0,
                    "Sintomo: chi vuole conoscere la lista o venire a un gazebo deve trovare le informazioni "
                    "online.\nContesto: sito web della lista Terni 2027 con pagine dedicate.\nIntervento e stato: "
                    "pubblicate la pagina programma e la pagina gazebo; il sito resta da completare con le altre "
                    "sezioni. In corso.\nParole chiave: sito web, sito della lista, pagina programma, pagina "
                    "gazebo, Terni 2027, online",
                    ["sito web", "sito della lista", "pagina programma", "pagina gazebo", "Terni 2027"])],
         "keywords": ["sito web", "sito della lista", "pagina programma", "pagina gazebo", "Terni 2027"]},
    ],
    "updates": [
        ("Campagna: novembre", "on_track", 35, 2, "volantino in stampa, calendario gazebo fino al 18/11. tavolo "
                                                  "del 30/10: indice della bozza comune, nessun nome. "
                                                  "presentazione al CAOS il 14/11."),
    ],
}

PROJECT_RASS = {
    "name": P_RASS, "tags": ["rassegna", "stampa", "video"], "stages": RASSEGNA_STAGES,
    "description": "<p>Rassegna stampa e video: schede con testata, data, titolo, link e due righe nostre. "
                   "Niente articoli copiati, niente video scaricati. Ufficio stampa: Giada.</p>",
    "milestones": [("Schede settimana della crisi", -1, 1)],
    "tasks": [
        {"name": "Rassegna quotidiana: turni", "who": "stampa", "stage": "In lavorazione",
         "notes": [("stampa", 10, "lun-mer Giada, gio-ven Ilaria, weekend chi c'è. feed UmbriaON + giro dei siti"),
                   ("stampa", 0,
                    "Sintomo: la rassegna stampa quotidiana deve essere coperta tutti i giorni.\nContesto: turni "
                    "lunedì-mercoledì e giovedì-venerdì fra due volontarie, weekend a chi c'è; fonti: feed "
                    "UmbriaON e giro dei siti delle testate locali; schede secondo la regola della "
                    "rassegna.\nIntervento e stato: turni assegnati, rassegna in lavorazione.\nParole chiave: "
                    "rassegna stampa, turni rassegna, feed RSS, UmbriaON, testate locali, schede articoli",
                    ["rassegna stampa", "turni rassegna", "feed RSS", "UmbriaON", "testate locali",
                     "schede articoli"])],
         "keywords": ["rassegna stampa", "turni rassegna", "feed RSS", "UmbriaON", "testate locali",
                      "schede articoli"]},
        {"name": "Settimana 26-31/10: schede crisi in Comune", "who": "stampa", "stage": "Schedato",
         "milestone": "Schede settimana della crisi",
         "notes": [("stampa", 5, "fatte le schede di ANSA, Umbria24, Settegiorni, QdU, UmbriaON. tutte con link"),
                   ("stampa", 1, "aggiunta la nota FdI del 31/10, segnata come fonte di parte"),
                   ("stampa", 0,
                    "Sintomo: servono in archivio tutti gli articoli sulla crisi della maggioranza in Comune della "
                    "settimana 26-31 ottobre.\nContesto: schede di ANSA, Umbria24, Umbria Settegiorni, Quotidiano "
                    "dell'Umbria e UmbriaON: passaggio di quattro consiglieri all'opposizione (Per Terni), "
                    "dimissioni dal notaio, mozione di sfiducia, risposta del sindaco sui 17 voti.\nIntervento e "
                    "stato: tutte schedate con link; aggiunta la nota FdI del 31/10 segnata come fonte di parte. "
                    "Schedato.\nParole chiave: crisi in Comune, crisi di maggioranza, sfiducia, Per Terni, "
                    "dimissioni dal notaio, Bandecchi, rassegna stampa",
                    ["crisi in Comune", "crisi di maggioranza", "sfiducia", "Per Terni", "dimissioni dal notaio",
                     "Bandecchi", "rassegna stampa", "fonte di parte"])],
         "keywords": ["crisi in Comune", "crisi di maggioranza", "sfiducia", "Per Terni", "dimissioni dal notaio",
                      "Bandecchi", "rassegna stampa", "fonte di parte"]},
        {"name": "Video: chi li guarda", "who": "stampa", "stage": "Da schedare",
         "description": "7 link dai canali locali. segmenti da compilare",
         "notes": [("stampa", 4, "nessuno li ha ancora visti per intero. nelle schede solo link, canale, titolo"),
                   ("portavoce", 3, "li guardo io nel weekend, i minuti li scrivo nella scheda"),
                   ("stampa", 0,
                    "Sintomo: ci sono 7 video dei canali locali sul sindaco ma nessuno li ha visti per "
                    "intero.\nContesto: schede video con solo link, canale e titolo (Umbria24, Radio Tele Galileo, "
                    "TuttOggi, Terninrete); regola: niente download né trascrizioni automatiche, minuti scritti da "
                    "chi guarda.\nIntervento e stato: un volontario li guarda nel weekend e annota i minuti dei "
                    "passaggi nella scheda; segmenti ancora da compilare. Da schedare.\nParole chiave: video, "
                    "schede video, segmenti, minuti, YouTube, canali locali, Bandecchi",
                    ["schede video", "segmenti da compilare", "minutaggio", "YouTube", "canali locali", "Umbria24",
                     "Radio Tele Galileo", "Bandecchi"])],
         "keywords": ["schede video", "segmenti da compilare", "minutaggio", "YouTube", "canali locali", "Umbria24",
                      "Radio Tele Galileo", "Bandecchi"]},
        {"name": "Feed UmbriaON e Umbria7", "who": "stampa", "stage": "In lavorazione",
         "notes": [("stampa", 1, "UmbriaON ok. Umbria7 feed in errore 500, il sito però va. per ora a mano"),
                   ("stampa", 0,
                    "Sintomo: la rassegna automatica non riceve gli articoli di Umbria7.\nContesto: feed RSS di "
                    "UmbriaON funzionante; quello di Umbria7 risponde con errore 500, anche se il sito è "
                    "raggiungibile.\nIntervento e stato: per ora Umbria7 si controlla a mano durante il turno di "
                    "rassegna, finché il feed non torna a funzionare. In lavorazione.\nParole chiave: feed RSS, "
                    "UmbriaON, Umbria7, errore 500, rassegna automatica, aggregatore",
                    ["feed RSS", "UmbriaON", "Umbria7", "errore 500", "rassegna automatica", "aggregatore notizie"])],
         "keywords": ["feed RSS", "UmbriaON", "Umbria7", "errore 500", "rassegna automatica", "aggregatore notizie"]},
        {"name": "Scheda TuttOggi: titolo offensivo", "who": "stampa", "stage": "Schedato",
         "notes": [("stampa", 4, "il titolo del video riporta un insulto del sindaco in consiglio. nella scheda "
                                 "non lo ripeto, scrivo solo che c'è"),
                   ("stampa", 0,
                    "Sintomo: il titolo di un video di TuttOggi riporta un insulto pronunciato dal sindaco in "
                    "consiglio.\nContesto: scheda video del canale YouTube TuttOggi; regole della lista: niente "
                    "insulti, schede con persone pubbliche, atti e fonti.\nIntervento e stato: nella scheda "
                    "l'insulto non viene ripetuto, si annota solo che il titolo lo contiene. Schedato.\nParole "
                    "chiave: TuttOggi, titolo offensivo, insulto, video, consiglio comunale, Bandecchi, scheda "
                    "video",
                    ["TuttOggi", "titolo offensivo", "insulto in consiglio", "scheda video", "consiglio comunale",
                     "Bandecchi"])],
         "keywords": ["TuttOggi", "titolo offensivo", "insulto in consiglio", "scheda video", "consiglio comunale",
                      "Bandecchi"]},
        {"name": "Episodi 2023-2025: schede", "who": "stampa", "stage": "Schedato",
         "notes": [("stampa", 6, "Sky 2023 e 2024, Lentepubblica, Espresso: schede fatte per Michele"),
                   ("stampa", 0,
                    "Sintomo: il portavoce chiede le schede degli episodi passati del sindaco da poter "
                    "citare.\nContesto: schede di Sky TG24 (2023, scontro in aula e indagine; 2024, dimissioni "
                    "annunciate), Lentepubblica (2023, insulti alla segretaria generale) e L'Espresso (2025, "
                    "Gaza), con link e data.\nIntervento e stato: schede fatte e consegnate al portavoce. "
                    "Schedato.\nParole chiave: episodi del sindaco, Sky TG24, Lentepubblica, L'Espresso, "
                    "Bandecchi, segretaria generale, Gaza",
                    ["episodi del sindaco", "Sky TG24", "Lentepubblica", "L'Espresso", "Bandecchi",
                     "segretaria generale", "Gaza", "dimissioni annunciate"])],
         "keywords": ["episodi del sindaco", "Sky TG24", "Lentepubblica", "L'Espresso", "Bandecchi",
                      "segretaria generale", "Gaza", "dimissioni annunciate"]},
        {"name": "Uscite nostre sui giornali", "who": "stampa", "stage": "In lavorazione",
         "notes": [("stampa", 9, "TerniCittà e Conca Notizie hanno ripreso il comunicato dei gazebo"),
                   ("stampa", 0,
                    "Sintomo: la lista vuole tenere traccia di quando i giornali parlano di lei.\nContesto: "
                    "rassegna delle uscite della lista; TerniCittà e Conca Notizie hanno ripreso il comunicato sui "
                    "gazebo.\nIntervento e stato: raccolta delle uscite in lavorazione, ogni uscita schedata come "
                    "gli altri articoli (testata, data, titolo, link).\nParole chiave: uscite stampa, comunicato "
                    "stampa, TerniCittà, Conca Notizie, copertura mediatica, gazebo",
                    ["uscite stampa", "comunicato stampa", "TerniCittà", "Conca Notizie", "copertura mediatica"])],
         "keywords": ["uscite stampa", "comunicato stampa", "TerniCittà", "Conca Notizie", "copertura mediatica"]},
        {"name": "Licenza per la rassegna?", "who": "lead", "stage": "Schedato",
         "notes": [("lead", 30, "chiesto in giro: per copiare articoli servirebbe una licenza (Promopress) e "
                                "comunque non conviene. facciamo schede nostre, regola scritta"),
                   ("lead", 0,
                    "Sintomo: ci si chiede se si possono copiare gli articoli nella rassegna interna.\nContesto: "
                    "la riproduzione degli articoli richiederebbe una licenza (Promopress, diritto d'autore), "
                    "comunque non conveniente.\nIntervento e stato: deciso: schede proprie (testata, data, titolo, "
                    "link, due righe), mai testo copiato; regola scritta fra le regole della lista. "
                    "Schedato.\nParole chiave: licenza rassegna, Promopress, diritto d'autore, copyright, articoli "
                    "copiati, schede di rassegna",
                    ["licenza rassegna stampa", "Promopress", "diritto d'autore", "copyright", "articoli copiati",
                     "schede di rassegna"])],
         "keywords": ["licenza rassegna stampa", "Promopress", "diritto d'autore", "copyright", "articoli copiati",
                      "schede di rassegna"]},
        {"name": "Lista testate e redazioni", "who": "stampa", "stage": "Schedato",
         "keywords": ["lista testate", "redazioni", "contatti stampa", "giornalisti", "mailing stampa"],
         "notes": [("stampa", 0,
                    "Sintomo: per mandare i comunicati serve l'elenco aggiornato delle testate e delle "
                    "redazioni.\nContesto: foglio delle testate usato dalla procedura del comunicato stampa (invio "
                    "dalla mail stampa).\nIntervento e stato: elenco schedato, nessun dettaglio nel task; i "
                    "comunicati partono solo dalla mail stampa, mai dal telefono personale, dopo l'ok del "
                    "portavoce.\nParole chiave: lista testate, redazioni, contatti stampa, giornalisti, mailing "
                    "stampa, comunicati",
                    ["lista testate", "redazioni", "contatti stampa", "giornalisti", "mailing stampa"])]},
    ],
    "updates": [
        ("Rassegna", "on_track", 60, 1, "schede della settimana della crisi fatte (26-31/10). video: 7 schede "
                                        "senza minuti, li guarda Michele. Umbria7 a mano."),
    ],
}

PROJECT_ADEMP = {
    "name": P_ADEMP, "tags": ["adempimenti", "firme", "spese"],
    "description": "<p>Adempimenti per presentare la lista e per la campagna: firme e autenticazioni, candidati, "
                   "deposito, mandatario, spese e rendiconto, par condicio, privacy. Referenti Paolo e Fra.</p>",
    "milestones": [("Schema adempimenti", -10, 10), ("Moduli pronti", 60, None), ("Deposito della lista", 150, None)],
    "tasks": [
        {"name": "Raccolta sottoscrizioni: moduli e autenticatori", "who": "lead", "stage": "In attesa",
         "milestone": "Moduli pronti",
         "notes": [("banchetti", 9, "i fogli vidimati per le firme li abbiamo? sabato al gazebo partiamo?"),
                   ("lead", 8, "fermi tutti: 1) per le comunali non serve nessuna vidimazione (istruzioni del "
                               "Viminale 2026): servono moduli con il contrassegno e i dati dei candidati 2) "
                               "candidati e contrassegno non ci sono ancora, quindi niente raccolta: firme prese "
                               "troppo presto sono nulle (mai prima del 180° giorno prima della scadenza di "
                               "consegna) 3) sabato al gazebo solo contatti col consenso e volantini"),
                   ("mandatario", 7, "chi autentica quando si parte: l'avv. Silvia R. (ha già fatto la "
                                     "comunicazione all'ordine), un consigliere comunale di opposizione che si è "
                                     "detto disponibile (da confermare), i funzionari incaricati dal sindaco in "
                                     "Comune (orari da chiedere); il notaio costa. i turni li fa Teo quando c'è la "
                                     "data"),
                   ("banchetti", 7, "ok, tolto «firme» dal turno di sabato"),
                   ("lead", 0,
                    "Sintomo: i volontari chiedono se hanno i fogli vidimati e se possono partire con le firme "
                    "sabato al gazebo.\nContesto: istruzioni del Viminale 2026: per le comunali nessuna "
                    "vidimazione, servono moduli con contrassegno e dati dei candidati; firme nulle se raccolte "
                    "prima del 180° giorno dal termine di consegna; autenticatori ex L. 53/1990 art. 14 (avvocata, "
                    "consigliere comunale, funzionari incaricati dal sindaco; notaio costoso).\nIntervento e "
                    "stato: raccolta fermata, sabato solo contatti con consenso e volantini; turni degli "
                    "autenticatori quando c'è la data. In attesa.\nParole chiave: firme, sottoscrizioni, "
                    "autenticazione, autenticatori, vidimazione, moduli, presentazione lista",
                    ["firme", "raccolta firme", "sottoscrizioni", "autenticazione delle firme", "autenticatori",
                     "vidimazione", "moduli", "L. 53/1990"])],
         "keywords": ["firme", "raccolta firme", "sottoscrizioni", "autenticazione delle firme", "autenticatori",
                      "vidimazione", "moduli", "L. 53/1990"]},
        {"name": "Schema adempimenti dalle istruzioni del Viminale", "who": "mandatario", "stage": "Fatto",
         "milestone": "Schema adempimenti",
         "notes": [("mandatario", 12, "letto il libretto 2026 del Ministero, fatto lo schema (vedi procedure del "
                                      "progetto)"),
                   ("lead", 10, "grazie. lo rileggiamo quando c'è il decreto di indizione"),
                   ("mandatario", 0,
                    "Sintomo: il gruppo adempimenti vuole uno schema chiaro di cosa serve per presentare la lista "
                    "alle comunali.\nContesto: Pubblicazione n. 1/2026 del Ministero dell'Interno (DAIT) sulla "
                    "presentazione e ammissione delle candidature: sottoscrizioni, contrassegno, candidati, "
                    "accettazioni, collegamento al candidato sindaco, deposito.\nIntervento e stato: libretto "
                    "letto, schema scritto nelle procedure del progetto; da rileggere quando esce il decreto di "
                    "indizione. Fatto.\nParole chiave: Viminale, Ministero dell'Interno, istruzioni candidature, "
                    "adempimenti elettorali, presentazione lista, decreto di indizione, DAIT",
                    ["Viminale", "Ministero dell'Interno", "DAIT", "istruzioni candidature",
                     "adempimenti elettorali", "presentazione della lista", "decreto di indizione"])],
         "keywords": ["Viminale", "Ministero dell'Interno", "DAIT", "istruzioni candidature",
                      "adempimenti elettorali", "presentazione della lista", "decreto di indizione"]},
        {"name": "Accettazione candidature: moduli", "who": "lead", "stage": "Da fare",
         "description": "accettazione autenticata, collegamento col candidato sindaco",
         "keywords": ["accettazione candidatura", "moduli di accettazione", "autenticazione",
                      "collegamento al candidato sindaco", "deposito lista"],
         "notes": [("lead", 0,
                    "Sintomo: per depositare la lista servono i moduli di accettazione firmati dai "
                    "candidati.\nContesto: dichiarazione di accettazione della candidatura autenticata e "
                    "collegamento della lista al candidato sindaco, come da istruzioni del Ministero "
                    "dell'Interno.\nIntervento e stato: da fare la preparazione dei moduli, insieme agli "
                    "autenticatori, quando ci sono candidati e contrassegno; va consegnata con la lista in "
                    "segreteria comunale.\nParole chiave: accettazione candidatura, moduli, autenticazione, "
                    "collegamento al candidato sindaco, deposito lista, candidati",
                    ["accettazione candidatura", "moduli di accettazione", "autenticazione",
                     "collegamento al candidato sindaco", "deposito lista"])]},
        {"name": "Certificati elettorali dei firmatari", "who": "mandatario", "stage": "Da fare",
         "description": "collettivi, il Comune li dà entro 24 ore. anche via PEC o ANPR",
         "keywords": ["certificati elettorali", "iscrizione liste elettorali", "firmatari", "sottoscrittori",
                      "ANPR", "PEC", "ufficio elettorale"],
         "notes": [("mandatario", 0,
                    "Sintomo: per ogni firma raccolta serve la prova che il firmatario è elettore del "
                    "Comune.\nContesto: certificati di iscrizione nelle liste elettorali, anche collettivi, "
                    "rilasciati dal Comune entro 24 ore, anche via PEC o ANPR.\nIntervento e stato: da fare, "
                    "quando parte la raccolta delle sottoscrizioni; vanno depositati con le firme "
                    "autenticate.\nParole chiave: certificati elettorali, iscrizione liste elettorali, firmatari, "
                    "sottoscrittori, ANPR, PEC, ufficio elettorale",
                    ["certificati elettorali", "iscrizione liste elettorali", "firmatari", "sottoscrittori", "ANPR",
                     "PEC", "ufficio elettorale"])]},
        {"name": "Mandatario: nomina e conto dedicato", "who": "mandatario", "stage": "Da fare",
         "notes": [("mandatario", 5, "io sono designato, ma la nomina vale dall'indizione: comunicazione al "
                                     "Collegio regionale di garanzia elettorale, conto dedicato, da lì in poi i "
                                     "soldi passano solo da me"),
                   ("mandatario", 0,
                    "Sintomo: chi gestisce i soldi della campagna vuole sapere da quando e come diventa "
                    "ufficiale.\nContesto: mandatario elettorale (L. 515/1993, richiamata dalla L. 96/2012): la "
                    "nomina vale dall'indizione, comunicazione al Collegio regionale di garanzia elettorale, conto "
                    "corrente dedicato.\nIntervento e stato: il commercialista della lista è designato; "
                    "dall'indizione tutti i movimenti passano solo da lui. Da fare.\nParole chiave: mandatario "
                    "elettorale, conto dedicato, Collegio regionale di garanzia elettorale, indizione, spese "
                    "elettorali, tesoriere",
                    ["mandatario elettorale", "conto dedicato", "Collegio regionale di garanzia elettorale",
                     "indizione", "spese elettorali", "tesoriere"])],
         "keywords": ["mandatario elettorale", "conto dedicato", "Collegio regionale di garanzia elettorale",
                      "indizione", "spese elettorali", "tesoriere"]},
        {"name": "Offerte al gazebo: come le teniamo", "who": "mandatario", "stage": "In corso",
         "notes": [("mandatario", 11, "cassetta chiusa, blocchetto ricevute numerato, a fine turno la conto io "
                                      "con chi era di turno. vedi procedura"),
                   ("banchetti", 10, "sab a Borgo Bovio 37 euro, ricevute 1-9"),
                   ("mandatario", 0,
                    "Sintomo: ai gazebo la gente lascia offerte in contanti e serve un modo sicuro per "
                    "registrarle.\nContesto: procedura offerte e contributi: cassetta chiusa, blocchetto ricevute "
                    "numerato, conta in due a fine turno, foglio cassa, versamento sul conto; dall'indizione tutto "
                    "sul conto del mandatario.\nIntervento e stato: procedura in uso; sabato a Borgo Bovio "
                    "raccolti 37 euro, ricevute 1-9. In corso.\nParole chiave: offerte, donazioni, contributi, "
                    "ricevute, cassetta, foglio cassa, gazebo, contanti",
                    ["offerte", "donazioni", "contributi", "ricevute numerate", "cassetta", "foglio cassa",
                     "contanti"])],
         "keywords": ["offerte", "donazioni", "contributi", "ricevute numerate", "cassetta", "foglio cassa",
                      "contanti"]},
        {"name": "Preventivo di spesa della lista", "who": "mandatario", "stage": "Da fare",
         "description": "sopra 50.000 abitanti va reso pubblico (L. 81/1993 art. 30)",
         "keywords": ["preventivo di spesa", "spese elettorali", "L. 81/1993", "art. 30", "budget campagna"],
         "notes": [("mandatario", 0,
                    "Sintomo: la lista deve dichiarare in anticipo quanto pensa di spendere in "
                    "campagna.\nContesto: nei Comuni sopra 50.000 abitanti il preventivo di spesa va depositato "
                    "con la lista e reso pubblico (L. 81/1993 art. 30).\nIntervento e stato: da fare insieme al "
                    "mandatario, con i conti dei tetti di spesa della L. 96/2012; va consegnato con la "
                    "lista.\nParole chiave: preventivo di spesa, spese elettorali, L. 81/1993, art. 30, "
                    "trasparenza, deposito lista",
                    ["preventivo di spesa", "spese elettorali", "L. 81/1993", "art. 30", "budget campagna"])]},
        {"name": "Tetti di spesa: conti", "who": "mandatario", "stage": "Da fare",
         "description": "numero degli elettori dal Comune, poi formula L. 96/2012",
         "keywords": ["tetti di spesa", "limiti di spesa", "L. 96/2012", "art. 13", "spese elettorali",
                      "numero elettori"],
         "notes": [("mandatario", 0,
                    "Sintomo: bisogna sapere quanto possono spendere al massimo la lista e i candidati.\nContesto: "
                    "limiti di spesa della L. 96/2012 art. 13 (candidato sindaco, consiglieri, lista) calcolati "
                    "sul numero degli elettori del Comune.\nIntervento e stato: da fare: chiedere il numero degli "
                    "elettori al Comune, poi applicare la formula.\nParole chiave: tetti di spesa, limiti di "
                    "spesa, L. 96/2012, art. 13, spese elettorali, numero elettori",
                    ["tetti di spesa", "limiti di spesa", "L. 96/2012", "art. 13", "spese elettorali",
                     "numero elettori"])]},
        {"name": "Par condicio: cosa cambia dall'indizione", "who": "portavoce", "stage": "Da fare",
         "keywords": ["par condicio", "L. 28/2000", "AGCOM", "122/24/CONS", "comunicazione istituzionale",
                      "sondaggi", "indizione"],
         "notes": [("portavoce", 0,
                    "Sintomo: la lista vuole sapere cosa non si può più fare in comunicazione una volta indette le "
                    "elezioni.\nContesto: L. 28/2000 (par condicio): stop alla comunicazione istituzionale, "
                    "sondaggi vietati negli ultimi 15 giorni; AGCOM delibera 122/24/CONS per le comunali; silenzio "
                    "elettorale L. 212/1956.\nIntervento e stato: da fare.\nParole chiave: par condicio, L. "
                    "28/2000, AGCOM, 122/24/CONS, comunicazione istituzionale, sondaggi, indizione",
                    ["par condicio", "L. 28/2000", "AGCOM", "122/24/CONS", "comunicazione istituzionale",
                     "sondaggi", "indizione"])]},
        {"name": "Informativa privacy del gazebo", "who": "lead", "stage": "Fatto",
         "notes": [("lead", 21, "informativa sul retro del modulo contatti, consenso a parte. fatta sul modello "
                                "del Garante 2019"),
                   ("lead", 0,
                    "Sintomo: chi lascia i propri dati al gazebo deve sapere come verranno usati.\nContesto: "
                    "informativa sul trattamento dei dati per propaganda elettorale sul modello del provvedimento "
                    "del Garante privacy del 2019; consenso separato dalla firma.\nIntervento e stato: informativa "
                    "stampata sul retro del modulo contatti, consenso in una casella a parte. Fatto.\nParole "
                    "chiave: informativa privacy, GDPR, Garante privacy, consenso, modulo contatti, propaganda "
                    "elettorale",
                    ["informativa privacy", "GDPR", "Garante privacy", "consenso separato", "modulo contatti",
                     "propaganda elettorale"])],
         "keywords": ["informativa privacy", "GDPR", "Garante privacy", "consenso separato", "modulo contatti",
                      "propaganda elettorale"]},
        {"name": "Deposito: chi va in segreteria", "who": "lead", "stage": "Da fare",
         "milestone": "Deposito della lista",
         "keywords": ["deposito lista", "presentazione della lista", "segreteria comunale", "consegna candidature",
                      "termini di deposito"],
         "notes": [("lead", 0,
                    "Sintomo: bisogna decidere chi porta fisicamente la lista in Comune per il "
                    "deposito.\nContesto: consegna alla segreteria comunale dalle 8 del 30° giorno alle 12 del 29° "
                    "giorno prima del voto, con firme, certificati, candidati, accettazioni, programma, "
                    "contrassegno e preventivo.\nIntervento e stato: da fare; bisogna scegliere le persone "
                    "incaricate e controllare l'elenco dei documenti prima della scadenza.\nParole chiave: "
                    "deposito lista, presentazione lista, segreteria comunale, consegna, termini, presentatori",
                    ["deposito lista", "presentazione della lista", "segreteria comunale", "consegna candidature",
                     "termini di deposito"])]},
    ],
    "updates": [
        ("Adempimenti", "on_track", 15, 7, "schema fatto dal libretto del Ministero. niente raccolta firme finché "
                                           "non ci sono candidati e contrassegno (e niente vidimazione: non "
                                           "serve). autenticatori: elenco provvisorio."),
    ],
}

ORGANISATION["projects"] = [PROJECT_CASA, PROJECT_AMB, PROJECT_SAN, PROJECT_LAV, PROJECT_PART, PROJECT_CAMP,
                            PROJECT_RASS, PROJECT_ADEMP]

ORGANISATION["project_rules"] = [
    {"name": "Soldi della campagna solo dal mandatario", "where": "project:" + P_ADEMP, "severity": "must",
     "activities": ["election"], "section": "compliance",
     "body": "Dal giorno dopo l'indizione ogni euro raccolto o speso per la campagna passa dal mandatario e dal "
             "suo conto dedicato. Nessuno paga di tasca e chiede il rimborso dopo.",
     "keywords": "mandatario, conto dedicato, spese di campagna, rimborsi, indizione, finanziamento elettorale"},
    {"name": "Silenzio elettorale", "where": "project:" + P_CAMP, "severity": "never",
     "activities": ["communication"], "section": "compliance",
     "body": "Il giorno prima del voto e durante il voto: niente comizi, niente gazebo, niente volantini, niente "
             "post nuovi della lista.",
     "keywords": "silenzio elettorale, giorno prima del voto, comizi, gazebo, volantinaggio, post social, L. "
                  "212/1956"},
]

ORGANISATION["project_notes"] = [
    {"kind": "procedure", "where": "project:" + P_ADEMP, "who": "mandatario", "section": "compliance",
     "name": "Firme per presentare la lista: numeri e tempi",
     "body": "Terni sta tra 100.001 e 250.000 abitanti: 350-700 firme di elettori del Comune (L. 81/1993 art. 3). "
             "Nulle se raccolte prima del 180° giorno prima del termine di presentazione. Un elettore firma una "
             "sola lista. Il candidato non firma la sua lista. Sul modulo: contrassegno, candidati con i dati.",
     "keywords": "firme, sottoscrizioni, 350-700 firme, L. 81/1993 art. 3, 180° giorno, presentazione della "
                  "lista, contrassegno, fascia di abitanti"},
    {"kind": "fact", "where": "project:" + P_ADEMP, "who": "lead", "section": "compliance",
     "name": "Moduli: la vidimazione non serve",
     "body": "il libretto 2026 del Ministero per le comunali NON chiede la vidimazione dei fogli. chi dice «fogli "
             "vidimati» pensa ad altre elezioni. serve: contrassegno, dati dei candidati, autentica delle firme.",
     "keywords": "vidimazione, fogli vidimati, moduli firme, istruzioni Viminale 2026, autentica delle firme, "
                  "contrassegno, sottoscrizioni"},
    {"kind": "procedure", "where": "project:" + P_ADEMP, "who": "mandatario", "section": "compliance",
     "name": "Chi può autenticare le firme",
     "body": "notai, giudici di pace, cancellieri, consiglieri comunali (anche se candidati), segretario comunale, "
             "funzionari incaricati dal sindaco, avvocati che hanno comunicato la disponibilità all'ordine (DL "
             "7/2024). Ognuno solo nel suo territorio (L. 53/1990 art. 14). Certificati elettorali collettivi "
             "entro 24 ore, anche via PEC o ANPR.",
     "keywords": "autenticazione delle firme, autenticatori, L. 53/1990 art. 14, notai, avvocati, DL 7/2024, "
                  "consiglieri comunali, funzionari incaricati, certificati elettorali"},
    {"kind": "procedure", "where": "project:" + P_ADEMP, "who": "mandatario", "section": "compliance",
     "name": "Consegna della lista in Comune",
     "body": "segreteria comunale, dalle 8 del 30° giorno alle 12 del 29° giorno prima del voto. Dentro: firme "
             "autenticate + certificati, 21-32 candidati, genere tra 1/3 e 2/3, accettazioni autenticate, "
             "collegamento al candidato sindaco, programma, contrassegno, preventivo di spesa (sopra 50.000 "
             "abitanti, L. 81/1993 art. 30).",
     "keywords": "deposito lista, presentazione candidature, segreteria comunale, 30° giorno, equilibrio di "
                  "genere, accettazioni, preventivo di spesa, collegamento al candidato sindaco"},
    {"kind": "fact", "where": "project:" + P_ADEMP, "who": "lead", "section": "compliance",
     "name": "Mandatario: Paolo",
     "body": "mandatario designato Paolo Antonelli (commercialista). formalmente dall'indizione: un solo conto, "
             "un candidato per mandatario, nome al Collegio regionale di garanzia elettorale. il candidato che "
             "spende meno di 2.500 euro solo di tasca sua non deve nominarlo.",
     "keywords": "mandatario elettorale, commercialista, conto dedicato, Collegio regionale di garanzia "
                  "elettorale, indizione, 2.500 euro, spese elettorali"},
    {"kind": "procedure", "where": "project:" + P_ADEMP, "who": "mandatario", "section": "compliance",
     "name": "Offerte e contributi: come si registrano",
     "body": "gazebo: cassetta chiusa + blocchetto ricevute numerato. ricevuta sempre, sopra 50 euro nome e "
             "cognome sulla ricevuta. a fine turno conta in due, foglio cassa (data, gazebo, numeri ricevute, "
             "totale), versamento sul conto entro la settimana. contanti mai usati per pagare. contributi sopra "
             "3.000 euro l'anno: nominativi e dichiarati. dall'indizione tutto sul conto del mandatario (Paolo).",
     "keywords": "offerte, donazioni, contributi, ricevute, foglio cassa, contanti, 3.000 euro, conto del "
                  "mandatario"},
    {"kind": "fact", "where": "project:" + P_ADEMP, "who": "mandatario", "section": "compliance",
     "name": "Tetti di spesa (L. 96/2012)",
     "body": "art. 13: candidato sindaco 125.000 + 1 euro per elettore; consigliere 12.500 + 0,05 per elettore; "
             "lista 1 euro per elettore. dichiarazioni dei candidati entro 3 mesi.",
     "keywords": "tetti di spesa, limiti di spesa, L. 96/2012 art. 13, candidato sindaco, consigliere, euro per "
                  "elettore, spese elettorali"},
    {"kind": "procedure", "where": "project:" + P_ADEMP, "who": "mandatario", "section": "compliance",
     "name": "Dopo il voto: rendiconto",
     "body": "rendiconto della lista entro 45 gg dall'insediamento del consiglio, controllo della Corte dei conti "
             "regionale. candidati: dichiarazione spese entro 3 mesi. contributi sopra 3.000 euro per nome.",
     "keywords": "rendiconto, rendicontazione spese, 45 giorni, Corte dei conti, dichiarazione spese candidati, "
                  "contributi sopra 3.000 euro"},
    {"kind": "fact", "where": "project:" + P_ADEMP, "who": "portavoce", "section": "compliance",
     "name": "Par condicio e silenzio",
     "body": "dall'indizione niente comunicazione istituzionale (L. 28/2000), sondaggi vietati negli ultimi 15 "
             "gg. silenzio elettorale: L. 212/1956 art. 9. AGCOM per le comunali applica la 122/24/CONS (avviso "
             "2026).",
     "keywords": "par condicio, L. 28/2000, comunicazione istituzionale, sondaggi, silenzio elettorale, L. "
                  "212/1956, AGCOM, 122/24/CONS"},
    {"kind": "fact", "where": "project:" + P_ADEMP, "who": "lead", "section": "compliance",
     "name": "Contatti per la propaganda: cosa si può usare",
     "body": "Garante 2019: liste elettorali usabili senza consenso; elenchi telefonici e contatti dei social no. "
             "i contatti presi al gazebo per le firme si riusano solo con un consenso esplicito e separato.",
     "keywords": "propaganda elettorale, Garante privacy 2019, liste elettorali, consenso, elenchi telefonici, "
                  "contatti dai social, privacy, GDPR"},
    {"kind": "procedure", "where": "project:" + P_RASS, "who": "stampa", "section": "operations",
     "name": "Scheda di rassegna",
     "body": "testata, data, titolo, link, due righe nostre (chi, cosa, dove). niente testo copiato. video: link, "
             "canale, titolo, minuti solo se qualcuno l'ha visto.",
     "keywords": "scheda di rassegna, rassegna stampa, testata, link, scheda video, minuti, niente testo copiato"},
]

# -- the documents of the projects: press and video cards, the normative texts, internal papers ---------------
RASS = "project:" + P_RASS
ADEMP = "project:" + P_ADEMP


def _card(key, outlet, day, title, link, line="", where=RASS, keywords=None, summary=None):
    """A press card: outlet, date, headline, link and at most one line of the volunteer's own words as its text;
    the curated summary and keywords of the press office."""
    text = "%s, %s\n%s\n%s\n" % (outlet, day, title, link) + (line + "\n" if line else "")
    card = {"key": key, "where": where, "name": "%s %s - %s" % (outlet, day, title), "summary": summary or title,
            "url": link, "keep_text": True, "text": text}
    if keywords:
        card["keywords"] = keywords
    return card


def _video(key, channel, title, link, line="", name_title=None, keywords=None, summary=None):
    """A video card: link, channel, title; segments left to fill, no transcript; the curated summary and keywords."""
    text = ("YouTube, canale %s\ntitolo: %s\n%s\ndata: non confermata\nsegmenti: da compilare, video non visto\n"
            % (channel, title, link)) + (line + "\n" if line else "")
    return {"key": key, "where": RASS, "name": "Video %s - %s" % (channel, name_title or title),
            "summary": summary or "video %s: %s" % (channel, title), "url": link, "keep_text": True, "text": text,
            "keywords": keywords}


UMBRIAON_CARDS = [
    _card("um_fdi_firme", "UmbriaON", "31/10/2026",
          "Terni, FdI attacca Pd e opposizioni: «Tante parole ma mancano le firme per cacciare Bandecchi»",
          UMBRIAON_3110, "nota di FdI, fonte di parte",
          summary="Scheda UmbriaON pubblicata il 31/10/2026, fonte di parte: una nota di Fratelli d'Italia attacca "
                  "il PD e le opposizioni di centrosinistra sostenendo che, nonostante gli annunci, mancano le "
                  "firme per la mozione di sfiducia contro il sindaco Bandecchi. Evento: nota diffusa il "
                  "31/10/2026. Contesto verificato: al 31/10 la mozione non risultava depositata; per presentarla "
                  "servono 13 firme e 17 voti per approvarla (TUEL art. 52). Temi: sfiducia, crisi di maggioranza, "
                  "opposizione alla giunta. Rilevanza: alta per la settimana della crisi. Collegate: Umbria "
                  "Settegiorni 28/10, Umbria24 27/10, Quotidiano dell'Umbria 29/10.",
          keywords="FdI, Fratelli d'Italia, PD, mozione di sfiducia, firme per la sfiducia, Bandecchi, il sindaco, "
                   "fonte di parte, UmbriaON"),
    _card("um_villalago", "UmbriaON", "30/10/2026",
          "Terni, Villalago: 50 mila euro per la gronda. Ok a manutenzione straordinaria",
          "https://www.umbriaon.it/terni-villalago-50-mila-euro-per-la-gronda-ok-allintervento-francucci/",
          summary="Scheda UmbriaON pubblicata il 30/10/2026: secondo il titolo il Comune di Terni dà il via libera "
                  "a una manutenzione straordinaria a Villalago, con 50 mila euro per la gronda. La scheda "
                  "contiene solo titolo e link: data dell'atto, ufficio competente e dettagli dell'intervento non "
                  "sono riportati e restano da verificare sull'articolo o sull'albo pretorio. Temi: nessuno della "
                  "lista controllata in modo diretto; vicino a partecipazione e trasparenza (spesa e lavori "
                  "pubblici del Comune). Rilevanza: bassa, cronaca amministrativa. Collegate: nessuna.",
          keywords="Villalago, gronda, manutenzione straordinaria, 50 mila euro, lavori pubblici, Comune di Terni, "
                   "UmbriaON"),
    _card("um_galilei_annulla", "UmbriaON", "29/10/2026",
          "Terni, scarichi del ‘Galilei’ e largo don Minzoni: Comune annulla la propria ordinanza",
          "https://www.umbriaon.it/terni-scarichi-del-galilei-e-largo-don-minzoni-comune-annulla-subito-la-"
          "propria-ordinanza/", "segue la scheda del 27/10",
          summary="Scheda UmbriaON pubblicata il 29/10/2026: secondo il titolo il Comune di Terni annulla la "
                  "propria ordinanza sugli scarichi del ‘Galilei’ e su largo don Minzoni. È il seguito della "
                  "scheda del 27/10, che riferiva di uno scontro tra Comune e Provincia e dell'emissione "
                  "dell'ordinanza. La scheda ha solo titolo e link: motivi dell'annullamento e date degli atti "
                  "restano da verificare. Temi: ambiente e aria (scarichi), opposizione alla giunta. Rilevanza: "
                  "media, esempio di atto emesso e ritirato in due giorni. Collegate: UmbriaON 27/10/2026 sugli "
                  "scarichi del Galilei.",
          keywords="Galilei, scarichi, largo don Minzoni, ordinanza annullata, Comune e Provincia, ordinanza "
                   "sindacale, UmbriaON"),
    _card("um_teatro_verdi", "UmbriaON", "29/10/2026",
          "Terni: teatro Verdi pronto a giugno 2027 ma senza arredi. Servono altri 4 milioni",
          "https://www.umbriaon.it/terni-teatro-verdi-pronto-a-giugno-2027-ma-senza-arredi-servono-altri-4-"
          "milioni-di-euro-foto-e-video/", "per il capitolo cultura",
          summary="Scheda UmbriaON pubblicata il 29/10/2026: secondo il titolo il teatro Verdi di Terni sarà "
                  "pronto a giugno 2027 ma senza arredi, e servono altri 4 milioni di euro. La scheda contiene "
                  "solo titolo e link ed è annotata per il capitolo cultura del programma; dettagli su lavori, "
                  "finanziamenti e responsabili non sono riportati. Temi: fuori dalla lista controllata (cultura); "
                  "vicino a partecipazione e trasparenza per l'uso delle risorse pubbliche. Rilevanza: media per "
                  "il capitolo cultura. Collegate: nessuna.",
          keywords="teatro Verdi, cultura, lavori teatro, 4 milioni, arredi, giugno 2027, UmbriaON"),
    _card("um_17_voti", "UmbriaON", "29/10/2026",
          "Bandecchi ‘sfida’ le minoranze: «Per sfiduciarmi servono 17 voti e non ci arriveranno mai»",
          "https://www.umbriaon.it/bandecchi-sfida-le-minoranze-per-sfiduciarmi-servono-17-voti-e-loro-non-ci-"
          "arriveranno-mai/",
          summary="Scheda UmbriaON pubblicata il 29/10/2026: il sindaco Bandecchi sfida le minoranze in consiglio "
                  "comunale sostenendo che per sfiduciarlo servono 17 voti e che non li raggiungeranno. Evento: "
                  "dichiarazione del 29/10/2026, riportata anche dal Quotidiano dell'Umbria, dove il sindaco dice "
                  "di avere 15 consiglieri e indica il bilancio di previsione come prossima prova. Contesto: TUEL "
                  "art. 52, sfiducia con maggioranza assoluta di 17 su 32. Temi: sfiducia, crisi di maggioranza, "
                  "opposizione alla giunta. Rilevanza: alta. Collegate: Quotidiano dell'Umbria 29/10, Umbria "
                  "Settegiorni 28/10, UmbriaON 31/10.",
          keywords="Bandecchi, il sindaco, 17 voti, sfiducia, minoranze, crisi di maggioranza, bilancio di "
                   "previsione, UmbriaON"),
    _card("um_bernardini", "UmbriaON", "29/10/2026",
          "Terni, Bernardini (Pd): «Tutti facciano la propria parte per mandare a casa Bandecchi»",
          "https://www.umbriaon.it/terni-bernardini-pd-tutti-facciano-la-propria-parte-per-mandare-a-casa-"
          "bandecchi/",
          summary="Scheda UmbriaON pubblicata il 29/10/2026: secondo il titolo Bernardini del Partito Democratico "
                  "chiede che tutti facciano la propria parte per mandare a casa il sindaco Bandecchi. La scheda "
                  "contiene solo titolo e link; il contenuto della dichiarazione oltre il titolo non è riportato. "
                  "Contesto verificato: il 28/10 PD, M5S, AVS, PSI, Casa Riformista-IV e Rifondazione si dicono "
                  "d'accordo per promuovere o sostenere una mozione di sfiducia. Temi: sfiducia, crisi di "
                  "maggioranza, opposizione alla giunta. Rilevanza: media. Collegate: Umbria Settegiorni 28/10, "
                  "UmbriaON 27/10 (PD), UmbriaON 28/10.",
          keywords="Bernardini, PD, Partito Democratico, mandare a casa Bandecchi, sfiducia, centrosinistra, crisi "
                   "in Comune, UmbriaON"),
    _card("um_mozione", "UmbriaON", "28/10/2026",
          "Terni, crisi in Comune. Il centrosinistra: «Presentiamo la mozione di sfiducia»",
          "https://www.umbriaon.it/terni-crisi-in-comune-il-centrosinistra-presentiamo-la-mozione-di-sfiducia/",
          summary="Scheda UmbriaON pubblicata il 28/10/2026: nella crisi in Comune il centrosinistra annuncia la "
                  "presentazione di una mozione di sfiducia contro il sindaco Bandecchi. Evento: annuncio del "
                  "28/10/2026, lo stesso giorno in cui Umbria Settegiorni riporta l'accordo di PD, M5S, AVS, PSI, "
                  "Casa Riformista-IV e Rifondazione. Contesto verificato: al 31/10 la mozione non risultava "
                  "depositata; servono 13 firme e 17 voti (TUEL art. 52). Temi: sfiducia, crisi di maggioranza, "
                  "opposizione alla giunta. Rilevanza: alta. Collegate: Umbria Settegiorni 28/10, Umbria24 27/10, "
                  "UmbriaON 31/10.",
          keywords="mozione di sfiducia, centrosinistra, csx, crisi in Comune, Bandecchi, TUEL art. 52, "
                   "opposizioni, UmbriaON"),
    _card("um_eq", "UmbriaON", "28/10/2026",
          "Terni, governo del territorio: revoca di tre elevate qualificazioni. Via a iter per nuovi incarichi",
          "https://www.umbriaon.it/terni-governo-del-territorio-revoca-di-tre-elevate-qualificazioni-via-a-iter-"
          "per-nuovi-incarichi/",
          summary="Scheda UmbriaON pubblicata il 28/10/2026: secondo il titolo nella direzione governo del "
                  "territorio del Comune di Terni vengono revocate tre elevate qualificazioni (incarichi di "
                  "responsabilità dei funzionari) e parte l'iter per nuovi incarichi. La scheda contiene solo "
                  "titolo e link: atti, date e motivazioni restano da verificare sull'albo pretorio. Temi: "
                  "partecipazione e trasparenza (organizzazione degli uffici e incarichi), opposizione alla "
                  "giunta. Rilevanza: bassa-media, possibile spunto per l'accesso agli atti. Collegate: nessuna.",
          keywords="governo del territorio, elevate qualificazioni, posizioni organizzative, revoca incarichi, "
                   "urbanistica, organizzazione uffici, UmbriaON"),
    _card("um_galilei_ordinanza", "UmbriaON", "27/10/2026",
          "Terni, scarichi del ‘Galilei’ e largo don Minzoni: scontro Comune-Provincia, c’è l’ordinanza",
          "https://www.umbriaon.it/terni-bisticcio-tra-comune-e-provincia-per-gli-scarichi-del-galilei-ordinanza-"
          "di-bandecchi/",
          summary="Scheda UmbriaON pubblicata il 27/10/2026: secondo il titolo sugli scarichi del ‘Galilei’ e su "
                  "largo don Minzoni c'è uno scontro tra Comune di Terni e Provincia, ed è stata emessa "
                  "un'ordinanza. La scheda contiene solo titolo e link; contenuto e firmatario dell'ordinanza "
                  "restano da verificare sull'atto. Due giorni dopo, secondo la scheda del 29/10, il Comune "
                  "annulla la propria ordinanza. Temi: ambiente e aria (scarichi), opposizione alla giunta. "
                  "Rilevanza: media. Collegate: UmbriaON 29/10/2026, ordinanza annullata.",
          keywords="Galilei, scarichi, largo don Minzoni, Comune e Provincia, ordinanza, scontro istituzionale, "
                   "UmbriaON"),
    _card("um_pd_destino", "UmbriaON", "27/10/2026",
          "Terni, crisi in Comune. PD: «Destino Bandecchi è segnato. Al lavoro con gli alleati»",
          "https://www.umbriaon.it/terni-crisi-in-comune-pd-destino-bandecchi-e-segnato-al-lavoro-con-gli-alleati/",
          summary="Scheda UmbriaON pubblicata il 27/10/2026: nella crisi in Comune il PD sostiene che il destino "
                  "del sindaco Bandecchi è segnato e dice di lavorare con gli alleati. Evento: presa di posizione "
                  "del 27/10/2026, il giorno dopo il passaggio di quattro consiglieri all'opposizione nel gruppo "
                  "Per Terni e lo stesso giorno delle dimissioni raccolte dal notaio dal centrodestra e dell'avvio "
                  "delle firme M5S per la sfiducia. Temi: crisi di maggioranza, sfiducia, opposizione alla giunta. "
                  "Rilevanza: media. Collegate: ANSA 26/10, Umbria24 27/10, Umbria Settegiorni 28/10.",
          keywords="PD, Partito Democratico, crisi in Comune, Bandecchi, alleati, centrosinistra, Per Terni, "
                   "UmbriaON"),
]

# the articles of the verified layer: their headlines were not copied, the card carries our own words drawn
# only from the verified fact
def _article(key, outlet, day, words, link, keywords=None, summary=None):
    text = "%s, %s\n(titolo non copiato) %s\n%s\n" % (outlet, day, words, link)
    card = {"key": key, "where": RASS, "name": "%s %s - %s" % (outlet, day, words), "summary": summary or words,
            "url": link, "keep_text": True, "text": text}
    if keywords:
        card["keywords"] = keywords
    return card


ARTICLE_CARDS = [
    _article("ansa_quattro", "ANSA Umbria", "26/10/2026",
             "quattro consiglieri lasciano la maggioranza, nasce Per Terni; consolidato 15 sì 9 no 6 astenuti",
             ANSA_2610, keywords="Per Terni, i quattro consiglieri, crisi di maggioranza, bilancio consolidato, "
                      "presidenti di commissione, Ministero dell'Interno, Bandecchi, ANSA",
             summary="Scheda ANSA Umbria del 26/10/2026, evento nella seduta del consiglio comunale dello stesso "
                     "giorno. Quattro consiglieri lasciano la maggioranza del sindaco Bandecchi e formano il "
                     "gruppo Per Terni all'opposizione. La maggioranza presenta una sfiducia contro due di loro, "
                     "presidenti di commissione: non votata, rimessa a un parere del Ministero dell'Interno. Nella "
                     "stessa seduta passa il bilancio consolidato con 15 sì, 9 no e 6 astenuti. Temi: crisi di "
                     "maggioranza, opposizione alla giunta, sfiducia. Rilevanza: alta, apre la crisi. Collegate: "
                     "Umbria24 27/10, Umbria Settegiorni 28/10, Quotidiano dell'Umbria 29/10."),
    _article("umbriaventiquattro_notaio", "Umbria24", "27/10/2026",
             "cdx dal notaio per le dimissioni (firmano in sei), M5S avvia le firme per la sfiducia", UMBRIA24_2710,
             summary="Scheda Umbria24 del 27/10/2026, eventi dello stesso giorno. FdI, Forza Italia, Lega e UdC "
                     "raccolgono dal notaio le dimissioni contestuali dei consiglieri per sciogliere il consiglio "
                     "(TUEL art. 141: ne servono 17 su 32, insieme): firmano in sei. Il M5S avvia la raccolta "
                     "firme per la mozione di sfiducia al sindaco Bandecchi (13 firme per presentarla, 17 voti per "
                     "approvarla). Temi: crisi di maggioranza, sfiducia, opposizione alla giunta. Rilevanza: alta. "
                     "Collegate: ANSA 26/10, Umbria Settegiorni 28/10, UmbriaON 31/10 (nota FdI).",
             keywords="dimissioni contestuali, notaio, TUEL art. 141, centrodestra, FdI, Forza Italia, Lega, M5S, "
                      "firme per la sfiducia, Umbria24"),
    _article("settegiorni_sfiducia", "Umbria Settegiorni", "28/10/2026",
             "csx d'accordo sulla mozione di sfiducia (PD, M5S, AVS, PSI, CR-IV, Rifondazione)", SETTEGIORNI_2810,
             summary="Scheda Umbria Settegiorni del 28/10/2026, evento dello stesso giorno: PD, M5S, AVS, PSI, "
                     "Casa Riformista-Italia Viva e Rifondazione si dicono d'accordo per promuovere o sostenere "
                     "una mozione di sfiducia contro il sindaco Bandecchi. Contesto verificato: il testo lo "
                     "scrivono i gruppi in consiglio; al 31/10 la mozione non risultava depositata; servono 13 "
                     "firme e 17 voti (TUEL art. 52). La lista non ha consiglieri in aula e non firma. Temi: "
                     "sfiducia, crisi di maggioranza, opposizione alla giunta. Rilevanza: alta. Collegate: "
                     "UmbriaON 28/10, Umbria24 27/10, UmbriaON 31/10.",
             keywords="mozione di sfiducia, centrosinistra, PD, M5S, AVS, PSI, Casa Riformista-IV, Rifondazione, "
                      "Bandecchi, Umbria Settegiorni"),
    _article("qdu_17", "Quotidiano dell'Umbria", "29/10/2026",
             "il sindaco: «Per sfiduciarmi servono 17 voti e loro non ci arriveranno mai»", QDU_2910,
             summary="Scheda Quotidiano dell'Umbria del 29/10/2026, dichiarazione dello stesso giorno. Il sindaco "
                     "Bandecchi risponde al centrosinistra che prepara la sfiducia: «Per sfiduciarmi servono 17 "
                     "voti e loro non ci arriveranno mai». Dice di avere 15 consiglieri e indica il bilancio di "
                     "previsione come prossima prova. Contesto: TUEL art. 52, maggioranza assoluta di 17 su 32. "
                     "Temi: sfiducia, crisi di maggioranza, opposizione alla giunta. Rilevanza: alta, citabile con "
                     "fonte. Collegate: UmbriaON 29/10 (stessa dichiarazione), Umbria Settegiorni 28/10, UmbriaON "
                     "31/10.",
             keywords="il sindaco, Bandecchi, 17 voti, 15 consiglieri, sfiducia, bilancio di previsione, "
                      "Quotidiano dell'Umbria, QdU"),
    _article("giornale_ap", "Il Giornale", "10/01/2026", "AP e Dimensione, percorsi separati", GIORNALE_AP,
          summary="Scheda Il Giornale del 10/01/2026, annuncio dello stesso giorno: Alternativa Popolare e "
                  "Dimensione, il partito fondato dal sindaco Bandecchi, annunciano percorsi separati. È il fatto "
                  "verificato da usare quando si parla dei partiti di riferimento del sindaco, eletto nel 2023 al "
                  "ballottaggio. Temi: opposizione alla giunta, crisi di maggioranza. Rilevanza: media, contesto "
                  "sul partito del sindaco. Collegate: scheda comunali 2023, ANSA 26/10/2026.",
          keywords="Alternativa Popolare, AP, Dimensione, Bandecchi, partito del sindaco, percorsi separati, Il "
                   "Giornale"),
    _article("sky_2023", "Sky TG24", "31/08/2023",
             "scontro in aula col consigliere FdI Cecconi, sindaco indagato; lui: «Lo rifarei»", SKY_2023,
             summary="Scheda Sky TG24 del 31/08/2023. Dopo uno scontro in aula in consiglio comunale con il "
                     "consigliere di Fratelli d'Italia Cecconi, la Procura iscrive il sindaco Bandecchi tra gli "
                     "indagati per minacce, oltraggio e interruzione di pubblico servizio; lui commenta «Lo "
                     "rifarei». La data esatta dello scontro in aula non è nella scheda. Temi: opposizione alla "
                     "giunta. Rilevanza: alta, episodio citabile con fonte e data. Collegate: video Radio Tele "
                     "Galileo sulla rissa in consiglio (da confermare), Lentepubblica 07/2023, Sky TG24 08/02/2024.",
             keywords="Bandecchi, il sindaco, Cecconi, FdI, sindaco indagato, rissa in consiglio, Procura, Sky TG24"),
    _article("lente_2023", "Lentepubblica", "07/2023",
             "insulti in consiglio alla segretaria generale, il sindacato dei segretari condanna", LENTE_2023,
             summary="Scheda Lentepubblica, luglio 2023. In consiglio comunale il sindaco Bandecchi insulta la "
                     "segretaria generale del Comune, che aveva sollevato dubbi di incompatibilità; il sindacato "
                     "dei segretari comunali condanna l'episodio. La data esatta della seduta non è nella scheda. "
                     "Temi: opposizione alla giunta, partecipazione e trasparenza. Rilevanza: alta, episodio "
                     "citabile con fonte. Collegate: Sky TG24 31/08/2023, Sky TG24 08/02/2024, L'Espresso "
                     "29/09/2025.",
             keywords="Bandecchi, il sindaco, segretaria generale, segretario comunale, incompatibilità, insulti "
                      "in consiglio, sindacato dei segretari, Lentepubblica"),
    _article("sky_2024", "Sky TG24", "08/02/2024",
             "annuncia in un video le dimissioni «per motivi politici», poi resta", SKY_2024,
             summary="Scheda Sky TG24 dell'08/02/2024: il sindaco Bandecchi annuncia in un video le proprie "
                     "dimissioni «per motivi politici», ma poi resta in carica. L'evento coincide con la data di "
                     "pubblicazione secondo la scheda. Temi: opposizione alla giunta, crisi di maggioranza. "
                     "Rilevanza: alta come precedente, utile a confronto con la crisi di ottobre 2026. Collegate: "
                     "Sky TG24 31/08/2023, Lentepubblica 07/2023, ANSA 26/10/2026.",
             keywords="Bandecchi, il sindaco, dimissioni annunciate, dimissioni ritirate, video, motivi politici, "
                      "Sky TG24"),
    _article("espresso_2025", "L'Espresso", "29/09/2025",
             "su Gaza «20mila bambini non sono mai morti», contestazione davanti al Comune", ESPRESSO_2025,
             summary="Scheda L'Espresso del 29/09/2025. Il sindaco Bandecchi afferma su Gaza che «20mila bambini "
                     "non sono mai morti»; ne segue una contestazione davanti al Comune di Terni e i consiglieri "
                     "di centrosinistra escono dall'aula. L'evento è riportato alla data di pubblicazione. Temi: "
                     "opposizione alla giunta. Rilevanza: alta, episodio citabile solo con fonte e data. "
                     "Collegate: Lentepubblica 07/2023, Sky TG24 31/08/2023, Sky TG24 08/02/2024.",
             keywords="Bandecchi, il sindaco, Gaza, bambini, contestazione, consiglieri escono dall'aula, "
                      "centrosinistra, L'Espresso"),
    _article("pagella_2024", "Pagella Politica", "18/11/2024", "regionali: Proietti 51,1%, Tesei 46,2%",
             PAGELLA_2024,
             summary="Scheda Pagella Politica del 18/11/2024 sulle elezioni regionali in Umbria del 17-18/11/2024: "
                     "Stefania Proietti, candidata del centrosinistra, vince con il 51,1% contro la presidente "
                     "uscente Donatella Tesei al 46,2%; affluenza 52,3%. La coalizione vincente comprende PD, M5S, "
                     "AVS, +Europa, Azione e Italia Viva. Temi: campagna e organizzazione. Rilevanza: media, "
                     "contesto sul quadro regionale e sulla coalizione. Collegate: scheda comunali 2023, Umbria "
                     "Settegiorni 28/10/2026.",
             keywords="regionali 2024, elezioni regionali Umbria, Proietti, Tesei, centrosinistra, affluenza, "
                      "campo largo, Pagella Politica"),
    _article("consiglio_erp", "Consiglio regionale Umbria", "28/01/2026",
             "III commissione approva le modifiche alla LR 23/2003 sulle case popolari", CONSIGLIO_ERP,
             summary="Atto del Consiglio regionale dell'Umbria del 28/01/2026: la III commissione approva le "
                     "modifiche alla LR 23/2003 sull'edilizia residenziale pubblica. Si toglie la residenza minima "
                     "in Umbria, si introducono punteggi per la disabilità, le donne vittime di violenza entrano "
                     "tra le emergenze abitative, si prevedono autorecupero e protocolli con Comuni, ATER e Terzo "
                     "settore. Temi: casa e ERP, politiche sociali. Rilevanza: alta, cornice per la scheda casa "
                     "della lista. Collegate: dossier Coordinamento casa, TerniCittà 19/10/2026 su Borgo Rivo.",
             keywords="ERP, LR 23/2003, case popolari, edilizia residenziale pubblica, III commissione, residenza "
                      "minima, ATER, emergenza abitativa, Consiglio regionale Umbria"),
    _article("renewable_circolare", "Materia Rinnovabile", "29/04/2026",
             "ddl Umbria Circolare, 53 articoli, discarica dal 30 al 20% entro il 2030", RENEWABLE,
             summary="Scheda Materia Rinnovabile del 29/04/2026 sul disegno di legge regionale «Umbria Circolare» "
                     "del 21/04/2026: 53 articoli, ambito unico regionale per i rifiuti, tariffa puntuale, "
                     "conferimento in discarica dal 30% al 20% entro il 2030. Dai fatti verificati: la giunta "
                     "regionale dichiara nessun inceneritore, il termovalorizzatore del piano 2023 è fermato e "
                     "AURI sospende la procedura. Temi: rifiuti, ambiente e aria. Rilevanza: alta per la nota "
                     "rifiuti della lista. Collegate: Conca Notizie 05/10/2026 sulla CER.",
             keywords="Umbria Circolare, ddl rifiuti, tariffa puntuale, discarica, inceneritore, "
                      "termovalorizzatore, AURI, ambito unico regionale, Materia Rinnovabile"),
    _article("qs_ospedale", "Quotidiano Sanità", "03/09/2026",
             "nuovo Santa Maria, Docfap con tre alternative: Sabbione, Campitello, Colle Obito", QSANITA,
             summary="Scheda Quotidiano Sanità del 03/09/2026: il Docfap (documento di fattibilità delle "
                     "alternative progettuali) per il nuovo ospedale Santa Maria di Terni, presentato a fine "
                     "luglio 2026, indica tre alternative di sito: Sabbione, Campitello e Colle Obito. Prima della "
                     "scelta è previsto un dibattito pubblico: nessun sito è deciso. Temi: sanità e ospedale, "
                     "partecipazione e trasparenza. Rilevanza: alta, smentisce chi dà Colle Obito per scelto. "
                     "Collegate: TerniCittà 28/10/2026 sull'assemblea sanità.",
             keywords="nuovo ospedale, Santa Maria, Docfap, Sabbione, Campitello, Colle Obito, dibattito pubblico, "
                      "Quotidiano Sanità"),
    _article("mimit_ast", "MIMIT", "09/2026", "primo comitato esecutivo dell'accordo di programma AST", MIMIT_AST,
          summary="Comunicato del Ministero delle Imprese e del Made in Italy (MIMIT), settembre 2026: si riunisce "
                  "il 28/09/2026 il primo comitato esecutivo dell'accordo di programma per AST, l'acciaieria di "
                  "Terni, dedicato ai costi dell'energia. L'accordo è stato firmato a giugno 2025 e prevede 557 "
                  "milioni di investimenti entro il 2028: la fase ora è attuazione e monitoraggio. Temi: lavoro e "
                  "acciaieria, energia. Rilevanza: alta, corregge chi crede che l'accordo non sia firmato. "
                  "Collegate: nessuna.",
          keywords="MIMIT, acciaieria, AST, Arvedi, accordo di programma, comitato esecutivo, costi dell'energia, "
                   "557 milioni"),
    _article("ansa_stadio", "ANSA Umbria", "10/09/2026",
             "stadio-clinica: il Comune rinuncia al Consiglio di Stato, il sindaco: «si farà»", ANSA_STADIO,
             summary="Scheda ANSA Umbria del 10/09/2026: la Regione Umbria comunica che il Comune di Terni "
                     "rinuncia al ricorso al Consiglio di Stato contro la sentenza del TAR favorevole alla Regione "
                     "sul progetto stadio-clinica; il sindaco Bandecchi dice che il progetto «si farà». Temi: "
                     "sanità e ospedale, opposizione alla giunta. Rilevanza: media, da citare solo nei fatti. "
                     "Collegate: Calcio e Finanza 2026 sulla Ternana, La Nazione 29/07/2026.",
             keywords="stadio-clinica, stadio, clinica, TAR, Consiglio di Stato, Regione Umbria, Bandecchi, ANSA"),
    _article("calciofin_ternana", "Calcio e Finanza", "2026", "Ternana in liquidazione giudiziale", CALCIOFIN,
          summary="Scheda Calcio e Finanza, 2026: la Ternana Calcio è in liquidazione giudiziale, con udienza il "
                  "17/04/2026. Dopo la liquidazione nasce la Nuova Ternana 1925 in serie D, promossa dal sindaco "
                  "(La Nazione, 29/07/2026). Temi: lavoro e acciaieria (sviluppo e sport in città), opposizione "
                  "alla giunta. Rilevanza: media; la lista ne parla solo con fatti e fonti, senza prendere parte "
                  "fra i tifosi. Collegate: La Nazione Umbria 29/07/2026, ANSA 10/09/2026 sullo stadio-clinica.",
          keywords="Ternana, liquidazione giudiziale, fallimento Ternana, Nuova Ternana 1925, calcio, Calcio e "
                   "Finanza"),
    _article("nazione_ternana", "La Nazione Umbria", "29/07/2026",
             "Nuova Ternana 1925 in serie D promossa dal sindaco, tifosi divisi", NAZIONE_TERNANA,
             summary="Scheda La Nazione Umbria del 29/07/2026: dopo la liquidazione giudiziale della Ternana nasce "
                     "la Nuova Ternana 1925, iscritta in serie D e promossa dal sindaco Bandecchi; i tifosi sono "
                     "divisi. Temi: opposizione alla giunta, partecipazione e trasparenza. Rilevanza: media, "
                     "argomento sentito ai gazebo su cui la lista cita solo i fatti. Collegate: Calcio e Finanza "
                     "2026, ANSA 10/09/2026 sullo stadio-clinica.",
             keywords="Nuova Ternana 1925, Ternana, serie D, tifosi divisi, Bandecchi, il sindaco, La Nazione"),
    _article("nazione_pm10", "La Nazione Umbria", "04/01/2025",
             "aria: Terni la più inquinata dell'Umbria, Maratta 41 superamenti nel 2023", NAZIONE_PM10,
             summary="Scheda La Nazione Umbria del 04/01/2025 con dati ARPA Umbria: l'area di Terni registra 30-40 "
                     "superamenti l'anno del limite giornaliero delle polveri sottili PM10 ed è la più inquinata "
                     "della regione; la centralina di Maratta ne conta 41 nel 2023. I dati 2024 e 2025 per "
                     "stazione non sono ancora disponibili alla lista, che cita il 2023 con questa fonte. Temi: "
                     "ambiente e aria. Rilevanza: alta, fonte principale per volantino e scheda aria. Collegate: "
                     "Materia Rinnovabile 29/04/2026.",
             keywords="smog, PM10, polveri sottili, ARPA, superamenti, Maratta, qualità dell'aria, La Nazione"),
]

VIDEO_CARDS = [
    _video("yt_qualcuno", "Umbria24",
           "Crisi Comune Terni, Bandecchi: «Qualcuno sta con me anche senza starci. Cittadini dalla mia parte»",
           "https://www.youtube.com/watch?v=LG9ulka5gfM",
           summary="Scheda video del canale YouTube Umbria24, data non confermata. Dal titolo: il sindaco "
                   "Bandecchi parla della crisi in Comune, dicendo che qualcuno sta con lui anche senza starci e "
                   "che i cittadini sono dalla sua parte. Contesto verificato: crisi aperta il 26/10/2026 con il "
                   "passaggio di quattro consiglieri all'opposizione (Per Terni) e la mozione di sfiducia "
                   "annunciata dal centrosinistra. Video non visto: segmenti e minuti ancora da compilare, nessuna "
                   "frase utilizzabile oltre il titolo. Temi: crisi di maggioranza, sfiducia. Collegate: ANSA "
                   "26/10, Quotidiano dell'Umbria 29/10.",
           keywords="video, Umbria24, Bandecchi, il sindaco, crisi in Comune, maggioranza, segmenti da compilare, "
                    "YouTube"),
    _video("yt_portafoglio", "Radio Tele Galileo",
           "Terni, Bandecchi “Se non abbiamo la maggioranza, mandateci a casa non guardate il portafoglio”",
           "https://www.youtube.com/watch?v=8deYBz4AVnc",
           summary="Scheda video del canale YouTube Radio Tele Galileo, data non confermata. Dal titolo: il "
                   "sindaco Bandecchi dice che, se non ci fosse più la maggioranza, l'amministrazione va mandata a "
                   "casa, con l'invito a non guardare al portafoglio. Contesto verificato: crisi di maggioranza da "
                   "ottobre 2026, dimissioni contestuali (TUEL art. 141) e sfiducia (TUEL art. 52). Video non "
                   "visto: segmenti da compilare, nessuna frase utilizzabile oltre il titolo. Temi: crisi di "
                   "maggioranza, sfiducia. Collegate: Umbria24 27/10, video Terninrete sul notaio.",
           keywords="video, Radio Tele Galileo, Bandecchi, il sindaco, maggioranza, mandateci a casa, "
                    "scioglimento, YouTube"),
    _video("yt_tuttoggi", "TuttOggi", "titolo con un insulto del sindaco in consiglio («Bandecchi show in "
           "consiglio …»)", "https://www.youtube.com/watch?v=fSyb47e4Zn8",
           "nella scheda l'insulto non si ripete", name_title="«Bandecchi show in consiglio…» (titolo con un insulto)",
                               summary="Scheda video del canale YouTube TuttOggi, data non confermata. Il titolo "
                                       "riporta un insulto pronunciato dal sindaco in consiglio comunale: per "
                                       "regola della lista l'insulto non viene ripetuto nella scheda. Non è noto a "
                                       "quale seduta si riferisca. Video non visto: segmenti e minuti da "
                                       "compilare. Temi: opposizione alla giunta. Rilevanza: da valutare dopo la "
                                       "visione; non citabile finché qualcuno non lo guarda. Collegate: "
                                       "Lentepubblica 07/2023, Sky TG24 31/08/2023.",
                               keywords="video, TuttOggi, titolo offensivo, insulto in consiglio, Bandecchi, "
                                        "consiglio comunale, segmenti da compilare"),
    _video("yt_rissa", "Radio Tele Galileo",
           "Terni: Follia in consiglio comunale minacce e rissa tra Bandecchi e un consigliere di opposizione",
           "https://www.youtube.com/watch?v=ggWhRMVBXTc",
           "forse è l'episodio con Cecconi del 2023 (scheda Sky TG24): da confermare guardandolo",
           summary="Scheda video del canale YouTube Radio Tele Galileo, data non confermata. Dal titolo: minacce e "
                   "rissa in consiglio comunale tra il sindaco Bandecchi e un consigliere di opposizione. Potrebbe "
                   "essere l'episodio con il consigliere FdI Cecconi del 2023, per cui il sindaco fu indagato (Sky "
                   "TG24, 31/08/2023): da confermare guardando il video. Video non visto: segmenti da compilare. "
                   "Temi: opposizione alla giunta. Collegate: Sky TG24 31/08/2023.",
           keywords="video, Radio Tele Galileo, rissa in consiglio, minacce, Bandecchi, Cecconi, consigliere di "
                    "opposizione, YouTube"),
    _video("yt_aspetto", "Umbria24",
           "Terni, Bandecchi senza maggioranza: «Aspetto, non ho avuto voglia di consultazioni»",
           "https://www.youtube.com/watch?v=tJoRUxK43YA",
           summary="Scheda video del canale YouTube Umbria24, data non confermata. Dal titolo: il sindaco "
                   "Bandecchi, senza maggioranza, dice di aspettare e di non aver fatto consultazioni. Contesto "
                   "verificato: dal 26/10/2026 quattro consiglieri sono passati all'opposizione nel gruppo Per "
                   "Terni; il 29/10 il sindaco dichiara di avere 15 consiglieri. Video non visto: segmenti e "
                   "minuti da compilare. Temi: crisi di maggioranza. Collegate: ANSA 26/10, Quotidiano dell'Umbria "
                   "29/10.",
           keywords="video, Umbria24, Bandecchi, senza maggioranza, consultazioni, crisi di maggioranza, YouTube"),
    _video("yt_cani", "Umbria24", "Terni, Bandecchi va avanti: «Dimissioni? No, esultano solo i cani»",
           "https://www.youtube.com/watch?v=4LbpigioEQs",
           summary="Scheda video del canale YouTube Umbria24, data non confermata. Dal titolo: il sindaco "
                   "Bandecchi esclude le dimissioni e dice di andare avanti. Contesto verificato: crisi di "
                   "maggioranza da ottobre 2026, richieste di dimissioni contestuali dal centrodestra e di "
                   "sfiducia dal centrosinistra; il precedente dell'08/02/2024, dimissioni annunciate e poi "
                   "ritirate. Video non visto: segmenti e minuti da compilare. Temi: crisi di maggioranza, "
                   "sfiducia. Collegate: Sky TG24 08/02/2024, Umbria24 27/10/2026.",
           keywords="video, Umbria24, Bandecchi, dimissioni, va avanti, crisi di maggioranza, YouTube"),
    _video("yt_notaio", "Terninrete",
           "Terni, Bandecchi sfida ancora i consiglieri: andate dal notaio e sfiduciatemi così andiamo a casa",
           "https://www.youtube.com/shorts/BFlgotGTFfA", "è uno short",
           summary="Short del canale YouTube Terninrete, data non confermata. Dal titolo: il sindaco Bandecchi "
                   "sfida i consiglieri ad andare dal notaio e a sfiduciarlo. Contesto verificato: il 27/10/2026 "
                   "FdI, Forza Italia, Lega e UdC raccolgono dal notaio le dimissioni contestuali (firmano in sei, "
                   "ne servono 17); il M5S avvia le firme per la sfiducia. Video non visto: segmenti da compilare. "
                   "Temi: sfiducia, crisi di maggioranza. Collegate: Umbria24 27/10, Quotidiano dell'Umbria 29/10.",
           keywords="video, short, Terninrete, Bandecchi, notaio, dimissioni contestuali, sfiducia, YouTube"),
]

# invented outlets and invented events of the list: every outlet is marked as fictional
FICTIONAL_CARDS = [
    _card("tc_nasce", "TerniCittà (testata fittizia)", "22/09/2026",
          "Nasce Terni 2027, lista civica: «Il programma lo scriviamo nei quartieri»",
          "https://ternicitta.example/2026/09/22/nasce-terni-2027", "c'è la foto dell'assemblea",
          summary="Scheda TerniCittà del 22/09/2026 sulla nascita della lista civica Terni 2027, dopo l'assemblea "
                  "costitutiva del 20/9 nella saletta di Borgo Bovio. Il titolo riporta lo slogan della lista: il "
                  "programma si scrive nei quartieri. L'articolo ha la foto dell'assemblea. Temi: campagna e "
                  "organizzazione, partecipazione e trasparenza. Rilevanza: media, prima uscita stampa della "
                  "lista. Collegate: Conca Notizie 12/10/2026, reel Instagram 02/10/2026.",
          keywords="Terni 2027, nascita della lista, lista civica, assemblea costitutiva, quartieri, uscita "
                   "stampa, TerniCittà"),
    _card("cn_gazebo_bovio", "Conca Notizie (testata fittizia)", "12/10/2026",
          "Terni 2027 al mercato di Borgo Bovio: «Case, bus e verde le richieste più frequenti»",
          "https://concanotizie.example/terni-2027-gazebo-borgo-bovio",
          summary="Scheda Conca Notizie del 12/10/2026 sul gazebo di Terni 2027 al mercato di Borgo Bovio: secondo "
                  "il titolo le richieste più frequenti dei cittadini riguardano case, bus e verde. È una ripresa "
                  "del comunicato della lista sui gazebo. Temi: campagna e organizzazione, casa e ERP, mobilità, "
                  "ambiente e aria. Data dell'evento: gazebo precedente alla pubblicazione, giorno non indicato. "
                  "Rilevanza: media, uscita della lista. Collegate: TerniCittà 22/09/2026, TerniCittà 19/10/2026.",
          keywords="Borgo Bovio, gazebo, mercato, case, bus, verde pubblico, Terni 2027, Conca Notizie"),
    _card("tc_borgo_rivo", "TerniCittà (testata fittizia)", "19/10/2026",
          "Borgo Rivo, gli inquilini delle case Ater mostrano muffa e infiltrazioni alla lista civica",
          "https://ternicitta.example/2026/10/19/borgo-rivo-inquilini-ater", "foto dei soffitti, nessuna persona",
          summary="Scheda TerniCittà del 19/10/2026: a Borgo Rivo gli inquilini delle case popolari ATER mostrano "
                  "alla lista civica Terni 2027 muffa e infiltrazioni negli appartamenti. Corrisponde al "
                  "sopralluogo con il comitato degli inquilini; le foto dell'articolo mostrano soffitti, nessuna "
                  "persona. Temi: casa e ERP, politiche sociali. Rilevanza: alta per la campagna casa. Collegate: "
                  "Consiglio regionale 28/01/2026 sulla LR 23/2003, dossier Coordinamento casa.",
          keywords="Borgo Rivo, case popolari, ATER, muffa, infiltrazioni, inquilini, sopralluogo, TerniCittà"),
    _card("rnl_intervista", "Radio Nera Libera (emittente fittizia)", "15/10/2026",
          "Intervista al portavoce di Terni 2027 su casa e affitti",
          "https://radioneralibera.example/podcast/terni-2027-casa", "audio nostro: si può trascrivere, da fare",
          summary="Scheda Radio Nera Libera del 15/10/2026: intervista al portavoce di Terni 2027 sulla casa e "
                  "sugli affitti. L'audio è della lista e si può trascrivere: trascrizione ancora da fare. Temi: "
                  "casa e ERP, politiche sociali, campagna e organizzazione. Data dell'evento coincidente con la "
                  "pubblicazione secondo la scheda; nessun virgolettato schedato. Rilevanza: media, materiale "
                  "proprio riutilizzabile. Collegate: TerniCittà 19/10/2026, Conca Notizie 12/10/2026.",
          keywords="intervista radio, portavoce, casa, affitti, podcast, Terni 2027, Radio Nera Libera"),
    _card("ts_mense", "Terni Sera (testata fittizia)", "13/10/2026",
          "Mense e pulizie del Comune, la lista civica firma un impegno con le lavoratrici",
          "https://ternisera.example/mense-pulizie-impegno-lista",
          summary="Scheda Terni Sera del 13/10/2026: la lista civica Terni 2027 firma un impegno con le "
                  "lavoratrici delle mense scolastiche e delle pulizie degli uffici comunali, consegnato il 12/10. "
                  "L'impegno riguarda gli appalti del Comune e il cambio d'appalto. Temi: lavoro e acciaieria, "
                  "politiche sociali. Dal lavoro interno della lista, non dall'articolo: l'impegno prevede "
                  "riassorbimento del personale con stesse ore e stesso contratto nazionale e niente ribassi sul "
                  "costo del lavoro. Rilevanza: media, uscita della lista. Collegate: nessuna.",
          keywords="mense scolastiche, pulizie, appalti comunali, clausola sociale, lavoratrici, impegno firmato, "
                   "Terni Sera"),
    _card("cn_cer", "Conca Notizie (testata fittizia)", "05/10/2026",
          "Energia condivisa sui tetti delle case popolari: ambientalisti e Terni 2027 al lavoro",
          "https://concanotizie.example/cer-case-popolari-terni-2027",
          summary="Scheda Conca Notizie del 05/10/2026: ambientalisti e Terni 2027 lavorano a un progetto di "
                  "energia condivisa sui tetti delle case popolari, cioè una comunità energetica rinnovabile "
                  "(CER). Dal lavoro interno della lista, non dall'articolo: la scheda CER prevede il Comune "
                  "capofila e prima i tetti delle palazzine ATER e delle scuole, con il Coordinamento "
                  "ambientalisti della conca. Temi: energia, casa e ERP, ambiente e aria. Rilevanza: media, uscita "
                  "della lista sulla proposta CER. Collegate: Materia Rinnovabile 29/04/2026, TerniCittà "
                  "19/10/2026.",
          keywords="CER, comunità energetica rinnovabile, energia condivisa, fotovoltaico, case popolari, "
                   "ambientalisti, Conca Notizie"),
    _card("tc_sanita", "TerniCittà (testata fittizia)", "28/10/2026",
          "Sanità, Terni 2027 annuncia un'assemblea pubblica a fine novembre",
          "https://ternicitta.example/2026/10/28/terni-2027-assemblea-sanita",
          summary="Scheda TerniCittà del 28/10/2026: Terni 2027 annuncia un'assemblea pubblica sulla sanità a fine "
                  "novembre. Dal lavoro interno della lista, non dall'articolo: l'assemblea è fissata a sabato "
                  "28/11, con l'invito agli operatori del pronto soccorso. Contesto verificato: il Docfap del "
                  "nuovo ospedale Santa Maria ha tre siti e nessuno è deciso. Temi: sanità e ospedale, campagna e "
                  "organizzazione. Rilevanza: media, uscita della lista. Collegate: Quotidiano Sanità 03/09/2026 "
                  "sul nuovo Santa Maria.",
          keywords="assemblea pubblica sanità, sanità, ospedale, fine novembre, Terni 2027, TerniCittà"),
    _card("cn_osservatorio", "Conca Notizie (testata fittizia)", "10/10/2026",
          "Società del Comune, l'Osservatorio civico chiede trasparenza: in sala anche le liste civiche",
          "https://concanotizie.example/osservatorio-civico-societa-comunali",
          summary="Scheda Conca Notizie del 10/10/2026: l'Osservatorio civico chiede trasparenza sulle società "
                  "partecipate dal Comune di Terni; in sala anche le liste civiche. Le contestazioni "
                  "dell'Osservatorio restano da verificare sugli atti prima di ogni uso pubblico. Data "
                  "dell'evento: serata precedente alla pubblicazione, giorno non indicato nella scheda. Temi: "
                  "partecipazione e trasparenza, opposizione alla giunta. Rilevanza: media. Collegate: UmbriaON "
                  "28/10/2026 sulle elevate qualificazioni.",
          keywords="Osservatorio civico, società partecipate, società comunali, trasparenza, liste civiche, Conca "
                   "Notizie"),
    _card("ts_tavolo", "Terni Sera (testata fittizia)", "31/10/2026",
          "Centrosinistra, le civiche al tavolo del programma: «Prima i contenuti, poi i nomi»",
          "https://ternisera.example/civiche-tavolo-programma", "virgolettato nostro, di Michele",
          summary="Scheda Terni Sera del 31/10/2026: le liste civiche partecipano al tavolo del programma del "
                  "centrosinistra; il virgolettato del titolo è del portavoce di Terni 2027. Contesto verificato: "
                  "al 1/11/2026 nessun candidato sindaco del centrosinistra annunciato. Data dell'evento non "
                  "indicata; segue la riunione del tavolo di coalizione del 30/10. Temi: campagna e "
                  "organizzazione, crisi di maggioranza. Rilevanza: media, uscita della lista. Collegate: Umbria "
                  "Settegiorni 28/10/2026.",
          keywords="tavolo del programma, centrosinistra, liste civiche, programma comune, candidato sindaco, "
                   "portavoce, Terni Sera"),
    _card("ig_reel", "Instagram terni2027 (nostro)", "02/10/2026", "Reel: perché una lista civica",
          "https://instagram.example/terni2027/reel/perche-una-lista-civica", "video nostro, testo nel drive",
          summary="Reel Instagram della lista, pubblicato il 02/10/2026 sul profilo terni2027: spiega perché nasce "
                  "una lista civica. Video della lista, con testo nel drive. Data dell'evento coincidente con la "
                  "pubblicazione. Nessuna persona pubblica o atto coinvolto; serve a presentare la lista civica e "
                  "il suo metodo di lavoro nei quartieri. Temi: campagna e organizzazione. Rilevanza: bassa-media, "
                  "materiale proprio. Collegate: TerniCittà 22/09/2026.",
          keywords="reel, Instagram, terni2027, lista civica, video nostro, social"),
]

NORMATIVE_DOCS = [
    {"key": "dait_2026", "where": ADEMP,
     "name": "Ministero dell'Interno - istruzioni candidature comunali 2026 (pubblicazione n. 1)",
     "summary": "Pubblicazione n. 1/2026 del Ministero dell'Interno, Dipartimento per gli affari interni e "
                "territoriali (DAIT), con le istruzioni per presentare e ammettere le candidature alle elezioni "
                "comunali. Tratta sottoscrizioni (numero per fascia di abitanti, tempi, autenticatori, certificati "
                "elettorali), contrassegno, liste e candidati, accettazioni, collegamento al candidato sindaco, "
                "programma, termini e luogo di deposito, esame della commissione e giurisprudenza. Per le comunali "
                "non prevede la vidimazione dei moduli.",
     "url": "https://dait.interno.gov.it/elezioni/pubblicazioni",
     "text_file": "dait-istruzioni-candidature-comunali-2026",
     "keywords": "Viminale, Ministero dell'Interno, DAIT, istruzioni candidature, presentazione liste, "
                 "sottoscrizioni, contrassegno, deposito candidature"},
    {"key": "l81_1993", "where": ADEMP, "name": "L. 81/1993 - elezione diretta del sindaco",
     "summary": "Legge 25 marzo 1993, n. 81, testo vigente: elezione diretta del sindaco e del consiglio comunale. "
                "Contiene il numero di firme per presentare le liste per fascia di abitanti (art. 3: per Terni "
                "350-700), il sistema elettorale, il collegamento delle liste al candidato sindaco e l'obbligo di "
                "preventivo e rendiconto delle spese (art. 30, Comuni sopra 50.000 abitanti).",
     "url": NORMATTIVA + "1993-03-25;81", "text_file": "legge-81-1993-elezione-sindaco",
     "keywords": "L. 81/1993, elezione diretta del sindaco, art. 3, firme per le liste, collegamento liste, art. "
                 "30, preventivo di spesa, sistema elettorale comunale"},
    {"key": "l53_1990", "where": ADEMP, "name": "L. 53/1990 - autenticazione delle firme (art. 14)",
     "summary": "Legge 21 marzo 1990, n. 53, testo vigente: misure urgenti per il procedimento elettorale. L'art. "
                "14 elenca chi può autenticare le sottoscrizioni (notai, giudici di pace, cancellieri, consiglieri "
                "comunali, segretario comunale, funzionari incaricati dal sindaco, avvocati iscritti che hanno "
                "comunicato la disponibilità) e limita ciascuno al proprio territorio; regola anche i certificati "
                "di iscrizione nelle liste elettorali.",
     "url": NORMATTIVA + "1990-03-21;53", "text_file": "legge-53-1990-autenticazione-firme",
     "keywords": "L. 53/1990, art. 14, autenticazione delle firme, autenticatori, sottoscrizioni, certificati "
                 "elettorali, notai, avvocati"},
    {"key": "l515_1993", "where": ADEMP, "name": "L. 515/1993 - campagne elettorali, mandatario e rendiconto",
     "summary": "Legge 10 dicembre 1993, n. 515, testo vigente: disciplina delle campagne elettorali nata per "
                "Camera e Senato. Regola mandatario elettorale, conto dedicato, dichiarazioni e rendiconti delle "
                "spese, Collegio regionale di garanzia elettorale e sanzioni; si applica ai Comuni sopra 15.000 "
                "abitanti per richiamo della L. 96/2012.",
     "url": NORMATTIVA + "1993-12-10;515", "text_file": "legge-515-1993-campagne-elettorali",
     "keywords": "L. 515/1993, mandatario elettorale, conto dedicato, rendiconto spese, Collegio regionale di "
                 "garanzia elettorale, campagne elettorali, sanzioni"},
    {"key": "l96_2012", "where": ADEMP, "name": "L. 96/2012 - limiti di spesa nelle comunali (art. 13)",
     "summary": "Legge 6 luglio 2012, n. 96, testo vigente; l'art. 13 fissa i tetti di spesa nelle elezioni "
                "comunali sopra 15.000 abitanti: candidato sindaco 125.000 euro più 1 euro per elettore, "
                "consigliere 12.500 più 0,05 per elettore, lista 1 euro per elettore. Regola anche mandatario, "
                "dichiarazioni e controlli sulle spese.",
     "url": NORMATTIVA + "2012-07-06;96", "text_file": "legge-96-2012-limiti-spesa-comunali",
     "keywords": "L. 96/2012, art. 13, tetti di spesa, limiti di spesa, spese elettorali, candidato sindaco, "
                 "mandatario, comunali"},
    {"key": "l28_2000", "where": ADEMP, "name": "L. 28/2000 - par condicio",
     "summary": "Legge 22 febbraio 2000, n. 28, testo vigente (par condicio): parità di accesso ai mezzi di "
                "informazione nelle campagne elettorali e referendarie. Disciplina la comunicazione politica in "
                "radio e TV, i messaggi autogestiti, il divieto di comunicazione istituzionale delle "
                "amministrazioni dall'indizione e il divieto di sondaggi negli ultimi 15 giorni.",
     "url": NORMATTIVA + "2000-02-22;28", "text_file": "legge-28-2000-par-condicio",
     "keywords": "L. 28/2000, par condicio, comunicazione politica, messaggi autogestiti, comunicazione "
                 "istituzionale, sondaggi, radio e TV"},
    {"key": "l212_1956", "where": ADEMP, "name": "L. 212/1956 - propaganda elettorale e silenzio",
     "summary": "Legge 4 aprile 1956, n. 212, testo vigente: disciplina della propaganda elettorale. Regola "
                "affissioni e spazi per i manifesti, i divieti di propaganda e, all'art. 9, il silenzio "
                "elettorale: niente comizi e propaganda il giorno prima e il giorno del voto.",
     "url": NORMATTIVA + "1956-04-04;212", "text_file": "legge-212-1956-propaganda-silenzio",
     "keywords": "L. 212/1956, propaganda elettorale, affissioni, manifesti, silenzio elettorale, art. 9, comizi"},
    {"key": "agcom_122_24", "where": ADEMP, "name": "AGCOM delibera 122/24/CONS - par condicio comunali",
     "summary": "Delibera AGCOM n. 122/24/CONS del 30 aprile 2024: disposizioni attuative della par condicio per "
                "le elezioni comunali dell'8-9 giugno 2024. Regola comunicazione politica e messaggi autogestiti "
                "in radio e TV, programmi di informazione, emittenti locali e sondaggi; un avviso AGCOM del 2026 "
                "la applica anche alle comunali del 2026.",
     "url": "https://www.agcom.it/provvedimenti/delibera-122-24-cons", "text_file": "agcom-delibera-122-24-cons",
     "keywords": "AGCOM, 122/24/CONS, par condicio, comunali, emittenti locali, messaggi autogestiti, sondaggi"},
    {"key": "agcom_avviso_2026", "where": ADEMP, "name": "AGCOM avviso 8/4/2026 - comunali: vale la 122/24/CONS",
     "summary": "Avviso AGCOM dell'8 aprile 2026: per le elezioni comunali del primo semestre 2026 si applica la "
                "delibera 122/24/CONS sulla par condicio. Conferma il riferimento attuativo da usare per la "
                "comunicazione politica nelle comunali.",
     "url": "https://www.agcom.it/comunicazione/avvisi/avviso-elezioni-comunali-primo-semestre-2026",
     "text_file": "agcom-avviso-comunali-2026",
     "keywords": "AGCOM, avviso 2026, 122/24/CONS, par condicio, comunali 2026, comunicazione politica"},
    {"key": "garante_2019", "where": ADEMP, "name": "Garante privacy 18/4/2019 - dati e propaganda elettorale",
     "summary": "Provvedimento n. 96 del 18 aprile 2019 del Garante per la protezione dei dati personali sul "
                "trattamento dei dati per propaganda elettorale. Indica le fonti usabili senza consenso (liste "
                "elettorali) e quelle vietate (elenchi telefonici, contatti dai social), le regole su consenso e "
                "informativa e l'uso dei dati raccolti per le firme, riutilizzabili solo con consenso esplicito e "
                "separato.",
     "url": "https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9105201",
     "text_file": "garante-2019-propaganda-elettorale",
     "keywords": "Garante privacy, provvedimento 96/2019, propaganda elettorale, dati personali, consenso, "
                 "informativa, liste elettorali, GDPR"},
]

INTERNAL_DOCS = [
    {"key": "dossier_case_vuote", "where": "project:" + P_CASA,
     "name": "Dossier appartamenti Ater vuoti - Coordinamento casa (bozza)",
     "summary": "Riassunto interno del dossier del Coordinamento casa (ottobre 2026) sugli appartamenti ATER "
                "chiusi a Terni: secondo il Coordinamento circa 280 alloggi chiusi, un centinaio da ristrutturare, "
                "e oltre un anno in media tra un'uscita e la nuova assegnazione, concentrati a Borgo Rivo, San "
                "Valentino e Città Giardino. Sono stime del Coordinamento da sopralluoghi e segnalazioni, non dati "
                "ATER, che non ha risposto. In pubblico si citano solo come «secondo il Coordinamento casa».",
     "url": "https://drive.terni2027.example/casa/dossier-coordinamento-casa-ott", "keep_text": True,
     "text": "## dossier Coordinamento casa, ott 2026 (riassunto Luisa)\n\n"
             "- loro contano circa 280 appartamenti Ater chiusi in città, un centinaio da ristrutturare prima "
             "di darli\n- tra quando uno esce e quando entra il nuovo assegnatario passa più di un anno in media "
             "(loro stima)\n- concentrati a Borgo Rivo, San Valentino, Città Giardino\n\n"
             "ATTENZIONE: numeri del Coordinamento, contati con sopralluoghi e segnalazioni, NON dati Ater. "
             "Ater non ha risposto alla richiesta. In pubblico solo «secondo il Coordinamento casa».\n",
     "keywords": "Coordinamento casa, alloggi sfitti, case popolari vuote, ATER, riassegnazione, Borgo Rivo, San "
                 "Valentino, Città Giardino, stime non ufficiali"},
]

ORGANISATION["project_documents"] = UMBRIAON_CARDS + ARTICLE_CARDS + VIDEO_CARDS + FICTIONAL_CARDS + \
    NORMATIVE_DOCS + INTERNAL_DOCS

CUSTOMERS = []

# -- the lessons: findings without names, places, amounts or numbers ---------------------------------------------
LESSONS = [
    {"key": "fonte_prima", "who": "lead", "state": "active", "tags": ["comunicazione", "rassegna"],
     "activities": ["communication"], "title": "Una frase senza link non si pubblica",
     "applies_to": "campagne elettorali locali", "verified": "ottobre 2026", "keywords": "fonte, citazione, "
                  "virgolettato, link, smentita, frase dell'avversario, post rimosso, fact checking",
     "finding": "Una frase dell'avversario girata nei gruppi, ripetuta a memoria in un post, si è rivelata "
                "diversa dall'originale: il post è stato tolto e la smentita ha avuto più visibilità del post.",
     "solution": "Prima di citare qualcuno si apre il link e si copia la frase esatta con testata e data; "
                 "senza link la frase non esce."},
    {"key": "schede_non_articoli", "who": "stampa", "state": "active", "tags": ["rassegna"],
     "activities": ["press"], "title": "La rassegna fatta di schede si ritrova, quella di pdf no",
     "applies_to": "rassegna stampa di un'organizzazione piccola", "verified": "ottobre 2026", "keywords": "rassegna "
                  "stampa, schede, pdf dei giornali, archivio articoli, licenza, diritto d'autore, ricercabilità",
     "finding": "Una cartella di pagine di giornale salvate in pdf era inutilizzabile: nessuno ritrovava un "
                "articolo e copiarli non era consentito senza licenza.",
     "solution": "Una scheda per articolo: testata, data, titolo, link e due righe proprie con chi, cosa e dove."},
    {"key": "video_minuti", "who": "stampa", "state": "draft", "tags": ["rassegna", "video"],
     "activities": ["press"], "title": "video schedati senza minuti",
     "applies_to": "", "verified": None, "keywords": "schede video, minuti, minutaggio, segmenti, frase precisa, "
                  "YouTube, timestamp",
     "finding": "le schede dei video con solo il titolo non servono quando serve la frase precisa",
     "solution": "chi guarda il video scrive i minuti dei passaggi utili nella scheda, subito"},
    {"key": "firme_presto", "who": "lead", "state": "active", "tags": ["adempimenti", "firme"],
     "activities": ["election"], "title": "Firme raccolte troppo presto non valgono",
     "applies_to": "presentazione di liste alle comunali", "verified": "ottobre 2026",
     "keywords": "sottoscrizioni, firme nulle, raccolta firme, finestra legale, 180° giorno, moduli completi, "
                  "autenticatori",
     "finding": "I volontari volevano partire con la raccolta delle firme al gazebo prima di avere candidati, "
                "contrassegno e data: quelle firme sarebbero state nulle e da rifare.",
     "solution": "Raccogliere le firme solo con i moduli completi e dentro la finestra prevista dalla legge; "
                 "prima si raccolgono contatti con il consenso e disponibilità degli autenticatori."},
    {"key": "consenso_gazebo", "who": "lead", "state": "active", "tags": ["volontari", "privacy"],
     "activities": ["campaign"], "title": "Il consenso ai contatti va in una casella a parte",
     "applies_to": "gazebo e raccolte di contatti", "verified": "ottobre 2026", "keywords": "consenso, casella "
                  "separata, foglio contatti, privacy, GDPR, contatti dai social, cancellazione contatti",
     "finding": "Nel foglio dei contatti c'erano persone senza consenso e altre prese da un gruppo social del "
                "quartiere: tutte da cancellare, con il lavoro di settimane perso.",
     "solution": "Modulo con la casella del consenso separata dalla firma; nel foglio entra solo chi l'ha "
                 "barrata; mai contatti copiati dai social."},
    {"key": "tavolo_verbali", "who": "lead", "state": "active", "tags": ["coalizione"],
     "activities": ["communication"], "title": "Quello che si dice al tavolo resta nei verbali interni",
     "applies_to": "coalizioni di partiti e liste civiche", "verified": "ottobre 2026", "keywords": "tavolo di "
                  "coalizione, verbali interni, alleati, riservatezza, attriti, smentite, posizioni pubbliche",
     "finding": "Attribuire in pubblico a un alleato una posizione sentita in riunione crea attriti e smentite, "
                "anche quando il resoconto è fedele.",
     "solution": "Verbali interni senza diffusione; fuori si dice solo ciò che la coalizione ha deciso di dire "
                 "e ciò che ogni forza ha dichiarato in pubblico."},
    {"key": "un_portavoce", "who": "portavoce", "state": "active", "tags": ["comunicazione"],
     "activities": ["communication"], "title": "Un solo portavoce con i giornalisti",
     "applies_to": "", "verified": "ottobre 2026", "keywords": "portavoce, giornalisti, cronista, dichiarazioni, "
                  "battuta nel titolo, gazebo, rapporti con la stampa",
     "finding": "Un volontario ha risposto a un cronista al gazebo e la sua battuta è finita nel titolo, al "
                "posto della proposta che volevamo far passare.",
     "solution": "Ai giornalisti si dà il numero del portavoce; chi è al gazebo non rilascia dichiarazioni."},
    {"key": "volantino_def", "who": "stampa", "state": "draft", "tags": ["materiali"],
     "activities": [], "title": "mandata in stampa la bozza sbagliata",
     "applies_to": "", "verified": None, "keywords": "stampa, tipografia, bozza sbagliata, file definitivo, "
                  "cartella definitivi, refuso, versioni dei file",
     "finding": "allo stampatore è andato un file dalla cartella bozze, con un refuso nel titolo",
     "solution": "una sola cartella per i definitivi, con dentro solo file approvati, e il nome del file con def"},
    {"key": "numeri_altrui", "who": "lead", "state": "active", "tags": ["programma"],
     "activities": ["analysis"], "title": "I numeri dei comitati si citano come loro",
     "applies_to": "programmi scritti con comitati e associazioni", "verified": "ottobre 2026", "keywords": "numeri "
                  "dei comitati, stime non ufficiali, dato ufficiale, attribuzione della fonte, contestazione, "
                  "cifre non verificate",
     "finding": "Le stime di un comitato, presentate come dati ufficiali, sono state contestate dall'ente "
                "competente e la discussione si è spostata dalla proposta ai numeri.",
     "solution": "Citare sempre chi ha fatto il conteggio e chiedere il dato ufficiale all'ente; nel programma "
                 "le proposte, non le cifre non verificate."},
    {"key": "atti_prima", "who": "lead", "state": "active", "tags": ["programma", "opposizione"],
     "activities": ["analysis"], "title": "Non commentare atti che non abbiamo letto",
     "applies_to": "", "verified": "ottobre 2026", "keywords": "delibere, bozza di delibera, testo ufficiale, albo "
                  "pretorio, atti, commento pubblico, chat",
     "finding": "Una bozza di delibera girata in chat era diversa dal testo approvato: un commento pubblico "
                "su quella bozza sarebbe stato sbagliato.",
     "solution": "Si commenta solo il testo ufficiale preso dall'albo o dal sito dell'ente, con il link."},
]

EVAL = []


# -- the external sources (texo_sources): the press review of the list as the press office writes it ----------
# The channels the list follows (on the project of the press review), the themes of its programme as labels, one
# card per clipping written by an agent that did not see the questions, with the rule of inventing nothing: the
# abstract in its own words, the public persons, bodies, places and acts, the event date only when it is certain
# (28 cards have none), quotes only where the headline had them. The key of a card is the key of the document the
# clipping was filed as: both stay, so a question can be asked of either. A card that names persons is approved
# by the lead at the load.
SOURCES = {
    "where": RASS,
    "themes": ["Casa e sociale", "Ambiente", "Sanità", "Lavoro e sviluppo", "Partecipazione e trasparenza",
                "Campagna", "Crisi in Comune"],
    "channels": [
        {"name": "UmbriaON", "kind": "press", "website": "https://www.umbriaon.it", "territory": "Umbria",
          "note": "feed letto ogni giorno dalla rassegna"},
        {"name": "ANSA Umbria", "kind": "press", "website": "https://www.ansa.it", "territory": "Umbria"},
        {"name": "Umbria24", "kind": "press", "website": "https://www.umbria24.it", "territory": "Umbria",
          "note": "ha anche un canale YouTube (video schedati)"},
        {"name": "Umbria Settegiorni", "kind": "press", "website": "https://www.umbriasettegiorni.it",
          "territory": "Umbria"},
        {"name": "Quotidiano dell'Umbria", "kind": "press", "website": "https://www.quotidianodellumbria.it",
          "territory": "Umbria"},
        {"name": "Il Giornale", "kind": "press", "website": "https://www.ilgiornale.it", "territory": "Italia"},
        {"name": "Sky TG24", "kind": "broadcaster", "website": "https://tg24.sky.it", "territory": "Italia"},
        {"name": "Lentepubblica", "kind": "press", "website": "https://lentepubblica.it", "territory": "Italia"},
        {"name": "L'Espresso", "kind": "press", "website": "https://lespresso.it", "territory": "Italia"},
        {"name": "Pagella Politica", "kind": "press", "website": "https://pagellapolitica.it",
          "territory": "Italia"},
        {"name": "Consiglio regionale Umbria", "kind": "public_body",
          "website": "https://consiglio.regione.umbria.it", "territory": "Umbria"},
        {"name": "Materia Rinnovabile", "kind": "press", "website": "https://www.renewablematter.eu",
          "territory": "Italia"},
        {"name": "Quotidiano Sanità", "kind": "press", "website": "https://www.quotidianosanita.it",
          "territory": "Italia"},
        {"name": "MIMIT", "kind": "public_body", "website": "https://www.mimit.gov.it", "territory": "Italia"},
        {"name": "Calcio e Finanza", "kind": "press", "website": "https://www.calcioefinanza.it",
          "territory": "Italia"},
        {"name": "La Nazione Umbria", "kind": "press", "website": "https://www.lanazione.it",
          "territory": "Umbria"},
        {"name": "Radio Tele Galileo", "kind": "video", "website": None, "territory": "Umbria",
          "note": "canale YouTube locale"},
        {"name": "TuttOggi", "kind": "video", "website": None, "territory": "Umbria",
          "note": "canale YouTube locale"},
        {"name": "Terninrete", "kind": "video", "website": None, "territory": "Terni",
          "note": "canale YouTube locale"},
        {"name": "TerniCittà", "kind": "press", "website": "https://ternicitta.example", "territory": "Terni",
          "note": "testata fittizia"},
        {"name": "Conca Notizie", "kind": "press", "website": "https://concanotizie.example",
          "territory": "Terni", "note": "testata fittizia"},
        {"name": "Radio Nera Libera", "kind": "broadcaster", "website": "https://radioneralibera.example",
          "territory": "Terni", "note": "emittente fittizia"},
        {"name": "Terni Sera", "kind": "press", "website": "https://ternisera.example", "territory": "Terni",
          "note": "testata fittizia"},
        {"name": "Instagram terni2027", "kind": "other", "website": "https://instagram.example/terni2027",
          "territory": "Terni", "note": "canale nostro"},
    ],
    "cards": [
        {"key": "um_fdi_firme", "channel": "UmbriaON", "kind": "article", "published_on": "2026-10-31",
          "event_date": "2026-10-31", "stance": "none", "relevance": "3",
          "url": "https://www.umbriaon.it/terni-fdi-attacca-pd-e-opposizioni-tante-parole-ma-mancano-le-firme-per-"
                 "cacciare-bandecchi/",
          "title": "Terni, FdI attacca Pd e opposizioni: «Tante parole ma mancano le firme per cacciare Bandecchi»",
          "abstract": "Secondo UmbriaON del 31 ottobre 2026, Fratelli d'Italia attacca il PD e le altre "
                      "opposizioni in consiglio comunale a Terni: molte dichiarazioni sulla sfiducia al sindaco "
                      "Stefano Bandecchi, ma mancano le firme. È una nota di partito, fonte di parte. Al 31 "
                      "ottobre la mozione di sfiducia del centrosinistra non risulta depositata.",
          "quotes": "«Tante parole ma mancano le firme per cacciare Bandecchi» (nota di FdI)",
          "acts": "mozione di sfiducia al sindaco (TUEL art. 52), non depositata al 31/10/2026",
          "keywords": "Fratelli d'Italia, centrodestra, cdx, firme per la sfiducia, mandare a casa il sindaco, "
                      "fonte di parte, nota FdI",
          "persons": ["Stefano Bandecchi"], "bodies": ["FdI", "PD", "Comune di Terni"], "places": [],
          "themes": ["Crisi in Comune"], "related": ["um_mozione", "settegiorni_sfiducia", "umbriaventiquattro_notaio"]},
        {"key": "um_villalago", "channel": "UmbriaON", "kind": "article", "published_on": "2026-10-30",
          "event_date": None, "stance": "none", "relevance": "1",
          "url": "https://www.umbriaon.it/terni-villalago-50-mila-euro-per-la-gronda-ok-allintervento-francucci/",
          "title": "Terni, Villalago: 50 mila euro per la gronda. Ok a manutenzione straordinaria",
          "abstract": "Secondo UmbriaON del 30 ottobre 2026, a Villalago (Terni) sono previsti 50 mila euro per la "
                      "gronda: via libera a un intervento di manutenzione straordinaria. La scheda riporta solo "
                      "titolo e link; chi ha deciso e i tempi dei lavori non risultano dalla scheda.",
          "quotes": None, "acts": None,
          "keywords": "gronda, grondaie, lavori pubblici, manutenzione straordinaria, 50.000 euro, parco di "
                      "Villalago",
          "persons": [], "bodies": [], "places": ["Villalago"], "themes": [], "related": []},
        {"key": "um_galilei_annulla", "channel": "UmbriaON", "kind": "article", "published_on": "2026-10-29",
          "event_date": None, "stance": "none", "relevance": "2",
          "url": "https://www.umbriaon.it/terni-scarichi-del-galilei-e-largo-don-minzoni-comune-annulla-subito-la-"
                 "propria-ordinanza/",
          "title": "Terni, scarichi del ‘Galilei’ e largo don Minzoni: Comune annulla la propria ordinanza",
          "abstract": "Secondo UmbriaON del 29 ottobre 2026, il Comune di Terni annulla la propria ordinanza sugli "
                      "scarichi del «Galilei» e su largo don Minzoni, emessa due giorni prima nel contrasto con la "
                      "Provincia di Terni. Il titolo dell'articolo indica un annullamento immediato. Segue la "
                      "scheda UmbriaON del 27 ottobre.",
          "quotes": None,
          "acts": "ordinanza del sindaco sugli scarichi del Galilei (27/10/2026), annullata dal Comune",
          "keywords": "scarichi, fognature, acque reflue, ordinanza annullata, autotutela, Comune contro "
                      "Provincia, don Minzoni",
          "persons": [], "bodies": ["Comune di Terni", "Provincia di Terni"],
          "places": ["Galilei", "largo don Minzoni"], "themes": ["Ambiente"], "related": ["um_galilei_ordinanza"]},
        {"key": "um_teatro_verdi", "channel": "UmbriaON", "kind": "article", "published_on": "2026-10-29",
          "event_date": None, "stance": "none", "relevance": "2",
          "url": "https://www.umbriaon.it/terni-teatro-verdi-pronto-a-giugno-2027-ma-senza-arredi-servono-altri-4-"
                 "milioni-di-euro-foto-e-video/",
          "title": "Terni: teatro Verdi pronto a giugno 2027 ma senza arredi. Servono altri 4 milioni",
          "abstract": "Secondo UmbriaON del 29 ottobre 2026, il teatro Verdi di Terni sarà pronto a giugno 2027 ma "
                      "senza arredi: per completarlo servono altri 4 milioni di euro. L'articolo è corredato di "
                      "foto e video. Utile per il capitolo cultura del programma.",
          "quotes": None, "acts": None,
          "keywords": "teatro comunale, Verdi, cantiere, ristrutturazione, arredi, 4 milioni, cultura, riapertura "
                      "2027",
          "persons": [], "bodies": [], "places": ["teatro Verdi"], "themes": [], "related": []},
        {"key": "um_17_voti", "channel": "UmbriaON", "kind": "article", "published_on": "2026-10-29",
          "event_date": "2026-10-29", "stance": "none", "relevance": "3",
          "url": "https://www.umbriaon.it/bandecchi-sfida-le-minoranze-per-sfiduciarmi-servono-17-voti-e-loro-non-"
                 "ci-arriveranno-mai/",
          "title": "Bandecchi ‘sfida’ le minoranze: «Per sfiduciarmi servono 17 voti e non ci arriveranno mai»",
          "abstract": "Secondo UmbriaON del 29 ottobre 2026, il sindaco di Terni Stefano Bandecchi sfida le "
                      "minoranze in consiglio comunale: per approvare la sfiducia servono 17 voti e, secondo lui, "
                      "non ci arriveranno. La stessa dichiarazione è riportata dal Quotidiano dell'Umbria lo "
                      "stesso giorno.",
          "quotes": "«Per sfiduciarmi servono 17 voti e non ci arriveranno mai» (Stefano Bandecchi)",
          "acts": "mozione di sfiducia (TUEL art. 52: maggioranza assoluta, 17 voti su 32)",
          "keywords": "17 voti, maggioranza assoluta, sfiducia, il sindaco sfida, minoranze, opposizione, non ci "
                      "arriveranno",
          "persons": ["Stefano Bandecchi"], "bodies": ["Comune di Terni"], "places": [],
          "themes": ["Crisi in Comune"], "related": ["qdu_17"]},
        {"key": "um_bernardini", "channel": "UmbriaON", "kind": "article", "published_on": "2026-10-29",
          "event_date": None, "stance": "none", "relevance": "2",
          "url": "https://www.umbriaon.it/terni-bernardini-pd-tutti-facciano-la-propria-parte-per-mandare-a-casa-b"
                 "andecchi/",
          "title": "Terni, Bernardini (Pd): «Tutti facciano la propria parte per mandare a casa Bandecchi»",
          "abstract": "Secondo UmbriaON del 29 ottobre 2026, Bernardini del PD chiede che tutti facciano la "
                      "propria parte per mandare a casa il sindaco Stefano Bandecchi, nella crisi della "
                      "maggioranza in Comune a Terni. È una dichiarazione di parte del PD.",
          "quotes": "«Tutti facciano la propria parte per mandare a casa Bandecchi» (Bernardini, PD)",
          "acts": None,
          "keywords": "Partito Democratico, Pd, centrosinistra, csx, sfiducia, mandare a casa il sindaco, appello "
                      "alle opposizioni",
          "persons": ["Bernardini", "Stefano Bandecchi"], "bodies": ["PD", "Comune di Terni"], "places": [],
          "themes": ["Crisi in Comune"], "related": ["um_mozione", "um_pd_destino"]},
        {"key": "um_mozione", "channel": "UmbriaON", "kind": "article", "published_on": "2026-10-28",
          "event_date": "2026-10-28", "stance": "none", "relevance": "3",
          "url": "https://www.umbriaon.it/terni-crisi-in-comune-il-centrosinistra-presentiamo-la-mozione-di-sfiduc"
                 "ia/",
          "title": "Terni, crisi in Comune. Il centrosinistra: «Presentiamo la mozione di sfiducia»",
          "abstract": "Secondo UmbriaON del 28 ottobre 2026, il centrosinistra annuncia che presenterà la mozione "
                      "di sfiducia contro il sindaco Stefano Bandecchi, nella crisi in Comune a Terni. Lo stesso "
                      "giorno Umbria Settegiorni riporta l'accordo di PD, M5S, AVS, PSI, Casa Riformista-IV e "
                      "Rifondazione. Al 31 ottobre la mozione non risulta depositata.",
          "quotes": "«Presentiamo la mozione di sfiducia» (centrosinistra)",
          "acts": "mozione di sfiducia al sindaco (TUEL art. 52)",
          "keywords": "centrosinistra, csx, opposizioni, sfiducia, mozione, crisi in Comune, mandare a casa il "
                      "sindaco",
          "persons": ["Stefano Bandecchi"], "bodies": ["PD", "M5S", "Comune di Terni"], "places": [],
          "themes": ["Crisi in Comune"],
          "related": ["settegiorni_sfiducia", "um_fdi_firme", "um_bernardini", "um_pd_destino"]},
        {"key": "um_eq", "channel": "UmbriaON", "kind": "article", "published_on": "2026-10-28",
          "event_date": None, "stance": "none", "relevance": "1",
          "url": "https://www.umbriaon.it/terni-governo-del-territorio-revoca-di-tre-elevate-qualificazioni-via-a-"
                 "iter-per-nuovi-incarichi/",
          "title": "Terni, governo del territorio: revoca di tre elevate qualificazioni. Via a iter per nuovi "
                   "incarichi",
          "abstract": "Secondo UmbriaON del 28 ottobre 2026, al Comune di Terni, nell'area del governo del "
                      "territorio, sono revocate tre elevate qualificazioni e parte l'iter per assegnare nuovi "
                      "incarichi. La scheda riporta solo titolo e link.",
          "quotes": None, "acts": None,
          "keywords": "EQ, elevate qualificazioni, posizioni organizzative, incarichi, urbanistica, governo del "
                      "territorio, revoca, uffici comunali",
          "persons": [], "bodies": ["Comune di Terni"], "places": [], "themes": [], "related": []},
        {"key": "um_galilei_ordinanza", "channel": "UmbriaON", "kind": "article", "published_on": "2026-10-27",
          "event_date": None, "stance": "none", "relevance": "2",
          "url": "https://www.umbriaon.it/terni-bisticcio-tra-comune-e-provincia-per-gli-scarichi-del-galilei-ordi"
                 "nanza-di-bandecchi/",
          "title": "Terni, scarichi del ‘Galilei’ e largo don Minzoni: scontro Comune-Provincia, c’è l’ordinanza",
          "abstract": "Secondo UmbriaON del 27 ottobre 2026, sugli scarichi del «Galilei» e su largo don Minzoni "
                      "c'è uno scontro tra Comune di Terni e Provincia di Terni, e il sindaco Stefano Bandecchi "
                      "firma un'ordinanza. Due giorni dopo il Comune la annulla (scheda del 29 ottobre).",
          "quotes": None, "acts": "ordinanza del sindaco sugli scarichi del Galilei",
          "keywords": "scarichi, fognature, acque reflue, ordinanza sindacale, bisticcio Comune-Provincia, don "
                      "Minzoni",
          "persons": ["Stefano Bandecchi"], "bodies": ["Comune di Terni", "Provincia di Terni"],
          "places": ["Galilei", "largo don Minzoni"], "themes": ["Ambiente"], "related": ["um_galilei_annulla"]},
        {"key": "um_pd_destino", "channel": "UmbriaON", "kind": "article", "published_on": "2026-10-27",
          "event_date": None, "stance": "none", "relevance": "2",
          "url": "https://www.umbriaon.it/terni-crisi-in-comune-pd-destino-bandecchi-e-segnato-al-lavoro-con-gli-a"
                 "lleati/",
          "title": "Terni, crisi in Comune. PD: «Destino Bandecchi è segnato. Al lavoro con gli alleati»",
          "abstract": "Secondo UmbriaON del 27 ottobre 2026, il PD di Terni dichiara che il destino del sindaco "
                      "Stefano Bandecchi è segnato e che lavora con gli alleati, nella crisi della maggioranza in "
                      "consiglio comunale. È una dichiarazione di partito.",
          "quotes": "«Destino Bandecchi è segnato. Al lavoro con gli alleati» (PD)", "acts": None,
          "keywords": "Partito Democratico, Pd, centrosinistra, csx, alleati, crisi in Comune, maggioranza, caduta "
                      "del sindaco",
          "persons": ["Stefano Bandecchi"], "bodies": ["PD", "Comune di Terni"], "places": [],
          "themes": ["Crisi in Comune"], "related": ["um_bernardini", "um_mozione", "ansa_quattro"]},
        {"key": "ansa_quattro", "channel": "ANSA Umbria", "kind": "article", "published_on": "2026-10-26",
          "event_date": "2026-10-26", "stance": "none", "relevance": "3",
          "url": "https://www.ansa.it/umbria/notizie/2026/10/26/allopposizione-quattro-consiglieri-della-maggioran"
                 "za-bandecchi-al-comune-di-terni_20b588a7-5ed9-4b69-b965-c64c46c2be2a.html",
          "title": "quattro consiglieri lasciano la maggioranza, nasce Per Terni; consolidato 15 sì 9 no 6 astenuti",
          "abstract": "Secondo ANSA del 26 ottobre 2026, nel consiglio comunale di Terni quattro consiglieri "
                      "lasciano la maggioranza del sindaco Stefano Bandecchi e formano il gruppo «Per Terni» "
                      "all'opposizione. La maggioranza presenta una sfiducia contro due di loro, presidenti di "
                      "commissione: non votata, rimessa a un parere del Ministero dell'Interno. Passa il bilancio "
                      "consolidato con 15 sì, 9 no e 6 astenuti.",
          "quotes": None,
          "acts": "bilancio consolidato (15 sì, 9 no, 6 astenuti); sfiducia ai presidenti di commissione rimessa "
                  "al parere del Ministero dell'Interno",
          "keywords": "i quattro, Per Terni, consiglieri passati all'opposizione, maggioranza, consolidato, "
                      "presidenti di commissione, Viminale",
          "persons": ["Stefano Bandecchi"], "bodies": ["Comune di Terni", "Per Terni", "Ministero dell'Interno"],
          "places": [], "themes": ["Crisi in Comune"], "related": ["um_pd_destino"]},
        {"key": "umbriaventiquattro_notaio", "channel": "Umbria24", "kind": "article", "published_on": "2026-10-27",
          "event_date": "2026-10-27", "stance": "none", "relevance": "3",
          "url": "https://www.umbria24.it/terni/crisi-politica-terni-centrodestra-invoca-dimissioni-dei-consiglier"
                 "i-m5s-chiede-sfiducia-a-bandecchi/",
          "title": "cdx dal notaio per le dimissioni (firmano in sei), M5S avvia le firme per la sfiducia",
          "abstract": "Secondo Umbria24 del 27 ottobre 2026, FdI, Forza Italia, Lega e UdC raccolgono dal notaio "
                      "le dimissioni contestuali dei consiglieri comunali di Terni: ne servono 17 su 32 insieme, "
                      "firmano in sei. Lo stesso giorno il M5S avvia la raccolta firme per la sfiducia al sindaco "
                      "Stefano Bandecchi: 13 per presentarla, 17 voti per approvarla.",
          "quotes": None, "acts": "dimissioni contestuali (TUEL art. 141); mozione di sfiducia (TUEL art. 52)",
          "keywords": "notaio, dimissioni contestuali, art. 141, scioglimento, centrodestra, cdx, Movimento 5 "
                      "Stelle, 5S, raccolta firme",
          "persons": ["Stefano Bandecchi"],
          "bodies": ["FdI", "Forza Italia", "Lega", "UdC", "M5S", "Comune di Terni"], "places": [],
          "themes": ["Crisi in Comune"], "related": ["settegiorni_sfiducia", "um_fdi_firme"]},
        {"key": "settegiorni_sfiducia", "channel": "Umbria Settegiorni", "kind": "article",
          "published_on": "2026-10-28", "event_date": "2026-10-28", "stance": "none", "relevance": "3",
          "url": "https://www.umbriasettegiorni.it/terni-centrosinistra-pronto-a-sfiduciare-bandecchi/",
          "title": "csx d'accordo sulla mozione di sfiducia (PD, M5S, AVS, PSI, CR-IV, Rifondazione)",
          "abstract": "Secondo Umbria Settegiorni del 28 ottobre 2026, il centrosinistra di Terni (PD, M5S, AVS, "
                      "PSI, Casa Riformista-IV e Rifondazione) è d'accordo per promuovere o sostenere una mozione "
                      "di sfiducia al sindaco Stefano Bandecchi. Al 31 ottobre la mozione non risulta depositata.",
          "quotes": None, "acts": "mozione di sfiducia al sindaco (TUEL art. 52)",
          "keywords": "centrosinistra, csx, opposizioni unite, mozione di sfiducia, Alleanza Verdi Sinistra, "
                      "Italia Viva, Rifondazione Comunista",
          "persons": ["Stefano Bandecchi"],
          "bodies": ["PD", "M5S", "AVS", "PSI", "Casa Riformista-IV", "Rifondazione", "Comune di Terni"],
          "places": [], "themes": ["Crisi in Comune"],
          "related": ["um_mozione", "um_fdi_firme", "umbriaventiquattro_notaio"]},
        {"key": "qdu_17", "channel": "Quotidiano dell'Umbria", "kind": "article", "published_on": "2026-10-29",
          "event_date": "2026-10-29", "stance": "none", "relevance": "3",
          "url": "https://www.quotidianodellumbria.it/terni/terni-il-centrosinistra-prepara-la-sfiducia-bandecchi-"
                 "non-avranno-mai-17-voti/",
          "title": "il sindaco: «Per sfiduciarmi servono 17 voti e loro non ci arriveranno mai»",
          "abstract": "Secondo il Quotidiano dell'Umbria del 29 ottobre 2026, il sindaco di Terni Stefano "
                      "Bandecchi risponde al centrosinistra che prepara la sfiducia: servono 17 voti e non li "
                      "avranno. Dice di avere 15 consiglieri e indica il bilancio di previsione come prossima "
                      "prova.",
          "quotes": "«Per sfiduciarmi servono 17 voti e loro non ci arriveranno mai» (Stefano Bandecchi)",
          "acts": "mozione di sfiducia (TUEL art. 52); bilancio di previsione",
          "keywords": "17 voti, maggioranza assoluta, 15 consiglieri, bilancio di previsione, prossima prova, "
                      "sfiducia, il sindaco risponde",
          "persons": ["Stefano Bandecchi"], "bodies": ["Comune di Terni"], "places": [],
          "themes": ["Crisi in Comune"], "related": ["um_17_voti"]},
        {"key": "giornale_ap", "channel": "Il Giornale", "kind": "article", "published_on": "2026-01-10",
          "event_date": "2026-01-10", "stance": "none", "relevance": "2",
          "url": "https://www.ilgiornale.it/news/interni/alli-e-bandecchi-alternativa-popolare-e-dimensione-andran"
                 "no-2593494.html",
          "title": "AP e Dimensione, percorsi separati",
          "abstract": "Secondo Il Giornale del 10 gennaio 2026, Alternativa Popolare e Dimensione, il partito "
                      "fondato da Stefano Bandecchi, sindaco di Terni dal 2023, annunciano percorsi separati. Il "
                      "link dell'articolo nomina Alli e Bandecchi; la scheda non riporta altro.",
          "quotes": None, "acts": None,
          "keywords": "AP, Alternativa Popolare, Dimensione, quelli di Dimensione, partito del sindaco, "
                      "separazione, divorzio politico",
          "persons": ["Alli", "Stefano Bandecchi"], "bodies": ["Alternativa Popolare", "Dimensione"],
          "places": [], "themes": ["Crisi in Comune"], "related": []},
        {"key": "sky_2023", "channel": "Sky TG24", "kind": "article", "published_on": "2023-08-31",
          "event_date": "2023-08-31", "stance": "none", "relevance": "2",
          "url": "https://tg24.sky.it/cronaca/2023/08/31/rissa-consiglio-comunale-terni-stefano-bandecchi-indagato",
          "title": "scontro in aula col consigliere FdI Cecconi, sindaco indagato; lui: «Lo rifarei»",
          "abstract": "Secondo Sky TG24 del 31 agosto 2023, dopo uno scontro in aula nel consiglio comunale di "
                      "Terni con il consigliere di FdI Cecconi, il sindaco Stefano Bandecchi è iscritto dalla "
                      "Procura tra gli indagati (minacce, oltraggio, interruzione di pubblico servizio). Lui dice "
                      "che lo rifarebbe.",
          "quotes": "«Lo rifarei» (Stefano Bandecchi)", "acts": None,
          "keywords": "rissa in consiglio, scontro in aula, indagato, Procura, minacce, oltraggio, episodi del "
                      "sindaco, 2023",
          "persons": ["Stefano Bandecchi", "Cecconi"], "bodies": ["FdI", "Procura", "Comune di Terni"],
          "places": [], "themes": ["Partecipazione e trasparenza"], "related": ["yt_rissa"]},
        {"key": "lente_2023", "channel": "Lentepubblica", "kind": "article", "published_on": None,
          "event_date": None, "stance": "none", "relevance": "2",
          "url": "https://lentepubblica.it/personale-e-previdenza/terni-sindaco-insulta-segretario/",
          "title": "insulti in consiglio alla segretaria generale, il sindacato dei segretari condanna",
          "abstract": "Secondo Lentepubblica, a luglio 2023 il sindaco di Terni Stefano Bandecchi insulta in "
                      "consiglio comunale la segretaria generale, che aveva sollevato dubbi di incompatibilità; il "
                      "sindacato dei segretari comunali condanna. Data di pubblicazione: luglio 2023, giorno non "
                      "indicato.",
          "quotes": None, "acts": None,
          "keywords": "segretaria generale, segretario comunale, insulti, incompatibilità, sindacato segretari, "
                      "episodi del sindaco, 2023",
          "persons": ["Stefano Bandecchi"], "bodies": ["sindacato dei segretari comunali", "Comune di Terni"],
          "places": [], "themes": ["Partecipazione e trasparenza"], "related": []},
        {"key": "sky_2024", "channel": "Sky TG24", "kind": "article", "published_on": "2024-02-08",
          "event_date": "2024-02-08", "stance": "none", "relevance": "2",
          "url": "https://tg24.sky.it/cronaca/2024/02/08/stefano-bandecchi-dimissioni-sindaco-terni",
          "title": "annuncia in un video le dimissioni «per motivi politici», poi resta",
          "abstract": "Secondo Sky TG24 dell'8 febbraio 2024, il sindaco di Terni Stefano Bandecchi annuncia in un "
                      "video le proprie dimissioni «per motivi politici», ma poi resta in carica. Bandecchi era "
                      "stato eletto sindaco nel 2023, al ballottaggio, con il 54,62%.",
          "quotes": "«per motivi politici» (Stefano Bandecchi)", "acts": None,
          "keywords": "dimissioni annunciate, dimissioni ritirate, video del sindaco, ci ripensa, episodi del "
                      "sindaco, 2024",
          "persons": ["Stefano Bandecchi"], "bodies": ["Comune di Terni"], "places": [],
          "themes": ["Partecipazione e trasparenza"], "related": []},
        {"key": "espresso_2025", "channel": "L'Espresso", "kind": "article", "published_on": "2025-09-29",
          "event_date": "2025-09-29", "stance": "none", "relevance": "2",
          "url": "https://lespresso.it/c/politica/2025/9/29/contestazione-bandecchi-terni-gaza-bambini-morti-cosa-"
                 "e-successo/57223",
          "title": "su Gaza «20mila bambini non sono mai morti», contestazione davanti al Comune",
          "abstract": "Secondo L'Espresso del 29 settembre 2025, il sindaco di Terni Stefano Bandecchi afferma su "
                      "Gaza che 20mila bambini non sono mai morti; segue una contestazione davanti al Comune e i "
                      "consiglieri di centrosinistra escono dall'aula.",
          "quotes": "«20mila bambini non sono mai morti» (Stefano Bandecchi)", "acts": None,
          "keywords": "Gaza, bambini, contestazione, presidio davanti al Comune, consiglieri escono dall'aula, "
                      "episodi del sindaco, 2025",
          "persons": ["Stefano Bandecchi"], "bodies": ["Comune di Terni"], "places": [],
          "themes": ["Partecipazione e trasparenza"], "related": []},
        {"key": "pagella_2024", "channel": "Pagella Politica", "kind": "article", "published_on": "2024-11-18",
          "event_date": "2024-11-18", "stance": "none", "relevance": "2",
          "url": "https://pagellapolitica.it/articoli/centrosinistra-vinto-elezioni-umbria-proietti",
          "title": "regionali: Proietti 51,1%, Tesei 46,2%",
          "abstract": "Secondo Pagella Politica del 18 novembre 2024, alle regionali umbre del 17-18 novembre 2024 "
                      "vince Stefania Proietti con il 51,1% su Donatella Tesei al 46,2%, con affluenza al 52,3%. "
                      "La coalizione di Proietti comprende PD, M5S, AVS, +Europa, Azione e IV.",
          "quotes": None, "acts": None,
          "keywords": "regionali 2024, elezioni regionali, la Regione, presidente della Regione, centrosinistra, "
                      "affluenza, risultati",
          "persons": ["Stefania Proietti", "Donatella Tesei"],
          "bodies": ["Regione Umbria", "PD", "M5S", "AVS", "+Europa", "Azione", "IV"], "places": [], "themes": [],
          "related": []},
        {"key": "consiglio_erp", "channel": "Consiglio regionale Umbria", "kind": "act",
          "published_on": "2026-01-28", "event_date": "2026-01-28", "stance": "none", "relevance": "2",
          "url": "https://consiglio.regione.umbria.it/node/81922/printable/pdf",
          "title": "III commissione approva le modifiche alla LR 23/2003 sulle case popolari",
          "abstract": "Secondo il Consiglio regionale dell'Umbria, il 28 gennaio 2026 la III commissione approva "
                      "le modifiche alla legge regionale 23/2003 sulle case popolari: tolta la residenza minima in "
                      "Umbria, punteggi per disabilità, donne vittime di violenza tra le emergenze, autorecupero, "
                      "protocolli con Comuni, ATER e Terzo settore.",
          "quotes": None,
          "acts": "LR 23/2003 (edilizia residenziale pubblica), modifiche approvate dalla III commissione il "
                  "28/01/2026",
          "keywords": "ERP, edilizia residenziale pubblica, case popolari, alloggi popolari, legge regionale, "
                      "residenza, graduatorie, Ater",
          "persons": [], "bodies": ["Consiglio regionale Umbria", "Regione Umbria", "ATER"], "places": [],
          "themes": ["Casa e sociale"], "related": []},
        {"key": "renewable_circolare", "channel": "Materia Rinnovabile", "kind": "article",
          "published_on": "2026-04-29", "event_date": "2026-04-21", "stance": "none", "relevance": "2",
          "url": "https://www.renewablematter.eu/umbria-circolare-53-articoli-per-uscire-dalle-discariche-ma-strad"
                 "a-in-salita",
          "title": "ddl Umbria Circolare, 53 articoli, discarica dal 30 al 20% entro il 2030",
          "abstract": "Secondo Materia Rinnovabile del 29 aprile 2026, la Regione Umbria presenta il 21 aprile il "
                      "ddl «Umbria Circolare», 53 articoli: ambito unico regionale dei rifiuti, tariffa puntuale, "
                      "discarica dal 30% al 20% entro il 2030. Il termovalorizzatore del piano 2023 è fermato e "
                      "AURI sospende la procedura.",
          "quotes": None, "acts": "ddl regionale «Umbria Circolare» (53 articoli); piano rifiuti 2023",
          "keywords": "rifiuti, economia circolare, inceneritore, termovalorizzatore, bruciatore, discarica, "
                      "tariffa puntuale, legge regionale",
          "persons": [], "bodies": ["Regione Umbria", "AURI"], "places": [], "themes": ["Ambiente"],
          "related": []},
        {"key": "qs_ospedale", "channel": "Quotidiano Sanità", "kind": "article", "published_on": "2026-09-03",
          "event_date": None, "stance": "none", "relevance": "2",
          "url": "https://www.quotidianosanita.it/?p=153129",
          "title": "nuovo Santa Maria, Docfap con tre alternative: Sabbione, Campitello, Colle Obito",
          "abstract": "Secondo Quotidiano Sanità del 3 settembre 2026, per il nuovo ospedale Santa Maria di Terni "
                      "il Docfap presentato a fine luglio 2026 indica tre siti alternativi: Sabbione, Campitello e "
                      "Colle Obito. Prima della scelta è previsto un dibattito pubblico; nessun sito è deciso.",
          "quotes": None,
          "acts": "Docfap (documento di fattibilità delle alternative progettuali) del nuovo ospedale",
          "keywords": "nuovo ospedale, Santa Maria, Docfap, dove si fa l'ospedale, siti, dibattito pubblico, sanità",
          "persons": [], "bodies": [],
          "places": ["ospedale Santa Maria", "Sabbione", "Campitello", "Colle Obito"], "themes": ["Sanità"],
          "related": []},
        {"key": "mimit_ast", "channel": "MIMIT", "kind": "statement", "published_on": None,
          "event_date": "2026-09-28", "stance": "none", "relevance": "2",
          "url": "https://www.mimit.gov.it/it/notizie-stampa/ast-terni-urso-mimit-ha-mantenuto-impegni-assunti-ora"
                 "-monitorare-attuazione-accordo-programma",
          "title": "primo comitato esecutivo dell'accordo di programma AST",
          "abstract": "Nota del MIMIT (settembre 2026, giorno non indicato): il 28 settembre 2026 si riunisce il "
                      "primo comitato esecutivo dell'accordo di programma per AST di Terni, sui costi "
                      "dell'energia. L'accordo, firmato a giugno 2025, prevede 557 milioni di investimenti entro "
                      "il 2028; ora è in fase di attuazione e monitoraggio. Il link cita Urso.",
          "quotes": None, "acts": "accordo di programma AST (giugno 2025, 557 milioni entro il 2028)",
          "keywords": "acciaieria, AST, Acciai Speciali Terni, Arvedi, accordo di programma, comitato esecutivo, "
                      "ministero, energia",
          "persons": ["Urso"], "bodies": ["MIMIT", "AST"], "places": [], "themes": ["Lavoro e sviluppo"],
          "related": []},
        {"key": "ansa_stadio", "channel": "ANSA Umbria", "kind": "article", "published_on": "2026-09-10",
          "event_date": None, "stance": "none", "relevance": "2",
          "url": "https://www.ansa.it/umbria/notizie/2026/09/10/bandecchi-annuncia-che-il-progetto-stadio-clinica-"
                 "a-terni-si-fara_75a5927f-4c2f-403e-95f8-973d6a00b9c1.html",
          "title": "stadio-clinica: il Comune rinuncia al Consiglio di Stato, il sindaco: «si farà»",
          "abstract": "Secondo ANSA del 10 settembre 2026, la Regione Umbria comunica che il Comune di Terni "
                      "rinuncia al ricorso al Consiglio di Stato contro la sentenza del TAR favorevole alla "
                      "Regione sul progetto stadio-clinica; il sindaco Stefano Bandecchi dice che il progetto si "
                      "farà.",
          "quotes": "«si farà» (Stefano Bandecchi)",
          "acts": "sentenza del TAR sullo stadio-clinica; rinuncia al ricorso al Consiglio di Stato",
          "keywords": "stadio, clinica, stadio-clinica, Ternana, TAR, Consiglio di Stato, ricorso",
          "persons": ["Stefano Bandecchi"],
          "bodies": ["Regione Umbria", "Comune di Terni", "TAR", "Consiglio di Stato"], "places": [],
          "themes": ["Lavoro e sviluppo"], "related": ["nazione_ternana", "calciofin_ternana"]},
        {"key": "calciofin_ternana", "channel": "Calcio e Finanza", "kind": "article", "published_on": None,
          "event_date": None, "stance": "none", "relevance": "1",
          "url": "https://www.calcioefinanza.it/?p=223447", "title": "Ternana in liquidazione giudiziale",
          "abstract": "Secondo Calcio e Finanza (2026, giorno non indicato), la Ternana è in liquidazione "
                      "giudiziale; l'udienza indicata nei nostri fatti è del 17 aprile 2026. Dopo la liquidazione "
                      "nasce la «Nuova Ternana 1925» in serie D (scheda La Nazione Umbria del 29 luglio 2026).",
          "quotes": None, "acts": "liquidazione giudiziale",
          "keywords": "Ternana, Ternana Calcio, fallimento, liquidazione, calcio, squadra", "persons": [],
          "bodies": ["Ternana"], "places": [], "themes": ["Lavoro e sviluppo"], "related": ["nazione_ternana"]},
        {"key": "nazione_ternana", "channel": "La Nazione Umbria", "kind": "article",
          "published_on": "2026-07-29", "event_date": None, "stance": "none", "relevance": "1",
          "url": "https://www.lanazione.it/umbria/cronaca/nuova-ternana-tifosi-spaccati-e-32458a49",
          "title": "Nuova Ternana 1925 in serie D promossa dal sindaco, tifosi divisi",
          "abstract": "Secondo La Nazione Umbria del 29 luglio 2026, nasce la «Nuova Ternana 1925» in serie D, "
                      "promossa dal sindaco di Terni Stefano Bandecchi, dopo la liquidazione giudiziale della "
                      "Ternana; i tifosi sono divisi.",
          "quotes": None, "acts": None,
          "keywords": "Ternana, Nuova Ternana, serie D, tifosi, calcio, rifondazione della squadra",
          "persons": ["Stefano Bandecchi"], "bodies": ["Ternana", "Nuova Ternana 1925"], "places": [],
          "themes": ["Lavoro e sviluppo"], "related": ["calciofin_ternana", "ansa_stadio"]},
        {"key": "nazione_pm10", "channel": "La Nazione Umbria", "kind": "article", "published_on": "2025-01-04",
          "event_date": None, "stance": "none", "relevance": "2",
          "url": "https://www.lanazione.it/umbria/cronaca/qualita-dellaria-nelle-nostre-citta-4808fe3b",
          "title": "aria: Terni la più inquinata dell'Umbria, Maratta 41 superamenti nel 2023",
          "abstract": "Secondo La Nazione Umbria del 4 gennaio 2025, che riporta dati ARPA, l'area di Terni è la "
                      "più inquinata dell'Umbria per polveri sottili: 30-40 superamenti l'anno del limite "
                      "giornaliero del PM10, con Maratta a 41 superamenti nel 2023.",
          "quotes": None, "acts": None,
          "keywords": "smog, PM10, polveri sottili, qualità dell'aria, inquinamento, superamenti, centralina, ARPA "
                      "Umbria",
          "persons": [], "bodies": ["ARPA"], "places": ["Maratta"], "themes": ["Ambiente"], "related": []},
        {"key": "yt_qualcuno", "channel": "Umbria24", "kind": "video", "published_on": None, "event_date": None,
          "stance": "none", "relevance": "2", "url": "https://www.youtube.com/watch?v=LG9ulka5gfM",
          "title": "Crisi Comune Terni, Bandecchi: «Qualcuno sta con me anche senza starci. Cittadini dalla mia "
                   "parte»",
          "abstract": "Video del canale YouTube di Umbria24. Dal titolo, riguarda la crisi in Comune a Terni: il "
                      "sindaco Stefano Bandecchi dice che qualcuno sta con lui anche senza starci e che i "
                      "cittadini sono dalla sua parte. Video non visto: la scheda riporta solo canale, titolo e "
                      "link, data non confermata; nessun contenuto oltre il titolo.",
          "quotes": "«Qualcuno sta con me anche senza starci. Cittadini dalla mia parte» (Stefano Bandecchi)",
          "acts": None,
          "keywords": "crisi in Comune, maggioranza, consenso dei cittadini, video del sindaco, YouTube",
          "persons": ["Stefano Bandecchi"], "bodies": ["Comune di Terni"], "places": [],
          "themes": ["Crisi in Comune"], "related": []},
        {"key": "yt_portafoglio", "channel": "Radio Tele Galileo", "kind": "video", "published_on": None,
          "event_date": None, "stance": "none", "relevance": "2",
          "url": "https://www.youtube.com/watch?v=8deYBz4AVnc",
          "title": "Terni, Bandecchi “Se non abbiamo la maggioranza, mandateci a casa non guardate il portafoglio”",
          "abstract": "Video del canale YouTube di Radio Tele Galileo. Dal titolo, il sindaco di Terni Stefano "
                      "Bandecchi dice che, se non hanno la maggioranza, chiede di mandarli a casa senza guardare "
                      "al portafoglio. Video non visto: la scheda riporta solo canale, titolo e link, data non "
                      "confermata; nessun contenuto oltre il titolo.",
          "quotes": "«Se non abbiamo la maggioranza, mandateci a casa non guardate il portafoglio» (Stefano "
                    "Bandecchi)",
          "acts": None,
          "keywords": "maggioranza, mandare a casa, scioglimento, indennità, portafoglio, video del sindaco, RTG",
          "persons": ["Stefano Bandecchi"], "bodies": ["Comune di Terni"], "places": [],
          "themes": ["Crisi in Comune"], "related": []},
        {"key": "yt_tuttoggi", "channel": "TuttOggi", "kind": "video", "published_on": None, "event_date": None,
          "stance": "none", "relevance": "1", "url": "https://www.youtube.com/watch?v=fSyb47e4Zn8",
          "title": "titolo con un insulto del sindaco in consiglio («Bandecchi show in consiglio …»)",
          "abstract": "Video del canale YouTube di TuttOggi su un intervento del sindaco di Terni Stefano "
                      "Bandecchi in consiglio comunale. Il titolo contiene un insulto del sindaco, che nella "
                      "scheda non si ripete. Video non visto: la scheda riporta solo canale, titolo e link, data "
                      "non confermata; nessun contenuto oltre il titolo.",
          "quotes": None, "acts": None,
          "keywords": "Bandecchi show, consiglio comunale, insulto, titolo offensivo, episodi del sindaco, video",
          "persons": ["Stefano Bandecchi"], "bodies": ["Comune di Terni"], "places": [],
          "themes": ["Partecipazione e trasparenza"], "related": []},
        {"key": "yt_rissa", "channel": "Radio Tele Galileo", "kind": "video", "published_on": None,
          "event_date": None, "stance": "none", "relevance": "2",
          "url": "https://www.youtube.com/watch?v=ggWhRMVBXTc",
          "title": "Terni: Follia in consiglio comunale minacce e rissa tra Bandecchi e un consigliere di "
                   "opposizione",
          "abstract": "Video del canale YouTube di Radio Tele Galileo. Dal titolo, riguarda minacce e una rissa in "
                      "consiglio comunale a Terni tra il sindaco Stefano Bandecchi e un consigliere di "
                      "opposizione. Potrebbe essere l'episodio con Cecconi del 2023 (scheda Sky TG24): da "
                      "confermare guardandolo. Video non visto: la scheda riporta solo canale, titolo e link, data "
                      "non confermata; nessun contenuto oltre il titolo.",
          "quotes": None, "acts": None,
          "keywords": "rissa in consiglio, minacce, scontro in aula, consigliere di opposizione, follia, episodi "
                      "del sindaco, RTG",
          "persons": ["Stefano Bandecchi"], "bodies": ["Comune di Terni"], "places": [],
          "themes": ["Partecipazione e trasparenza"], "related": ["sky_2023"]},
        {"key": "yt_aspetto", "channel": "Umbria24", "kind": "video", "published_on": None, "event_date": None,
          "stance": "none", "relevance": "2", "url": "https://www.youtube.com/watch?v=tJoRUxK43YA",
          "title": "Terni, Bandecchi senza maggioranza: «Aspetto, non ho avuto voglia di consultazioni»",
          "abstract": "Video del canale YouTube di Umbria24. Dal titolo, il sindaco di Terni Stefano Bandecchi, "
                      "senza maggioranza, dice che aspetta e che non ha avuto voglia di consultazioni. Video non "
                      "visto: la scheda riporta solo canale, titolo e link, data non confermata; nessun contenuto "
                      "oltre il titolo.",
          "quotes": "«Aspetto, non ho avuto voglia di consultazioni» (Stefano Bandecchi)", "acts": None,
          "keywords": "senza maggioranza, consultazioni, crisi in Comune, attesa, video del sindaco",
          "persons": ["Stefano Bandecchi"], "bodies": ["Comune di Terni"], "places": [],
          "themes": ["Crisi in Comune"], "related": []},
        {"key": "yt_cani", "channel": "Umbria24", "kind": "video", "published_on": None, "event_date": None,
          "stance": "none", "relevance": "2", "url": "https://www.youtube.com/watch?v=4LbpigioEQs",
          "title": "Terni, Bandecchi va avanti: «Dimissioni? No, esultano solo i cani»",
          "abstract": "Video del canale YouTube di Umbria24. Dal titolo, il sindaco di Terni Stefano Bandecchi va "
                      "avanti ed esclude le dimissioni. Video non visto: la scheda riporta solo canale, titolo e "
                      "link, data non confermata; nessun contenuto oltre il titolo.",
          "quotes": None, "acts": None,
          "keywords": "dimissioni, va avanti, niente dimissioni, crisi in Comune, video del sindaco",
          "persons": ["Stefano Bandecchi"], "bodies": ["Comune di Terni"], "places": [],
          "themes": ["Crisi in Comune"], "related": []},
        {"key": "yt_notaio", "channel": "Terninrete", "kind": "video", "published_on": None, "event_date": None,
          "stance": "none", "relevance": "2", "url": "https://www.youtube.com/shorts/BFlgotGTFfA",
          "title": "Terni, Bandecchi sfida ancora i consiglieri: andate dal notaio e sfiduciatemi così andiamo a "
                   "casa",
          "abstract": "Short del canale YouTube di Terninrete. Dal titolo, il sindaco di Terni Stefano Bandecchi "
                      "sfida di nuovo i consiglieri ad andare dal notaio e a sfiduciarlo, così vanno tutti a casa. "
                      "Video non visto: la scheda riporta solo canale, titolo e link, data non confermata; nessun "
                      "contenuto oltre il titolo.",
          "quotes": None, "acts": None,
          "keywords": "notaio, dimissioni contestuali, sfiducia, sfida ai consiglieri, andare a casa, short, "
                      "YouTube",
          "persons": ["Stefano Bandecchi"], "bodies": ["Comune di Terni"], "places": [],
          "themes": ["Crisi in Comune"], "related": []},
        {"key": "tc_nasce", "channel": "TerniCittà", "kind": "article", "published_on": "2026-09-22",
          "event_date": "2026-09-20", "stance": "positive", "relevance": "2",
          "url": "https://ternicitta.example/2026/09/22/nasce-terni-2027",
          "title": "Nasce Terni 2027, lista civica: «Il programma lo scriviamo nei quartieri»",
          "abstract": "Secondo TerniCittà (testata fittizia) del 22 settembre 2026, nasce Terni 2027, lista civica "
                      "che vuole scrivere il programma nei quartieri. La lista è nata dall'assemblea del 20 "
                      "settembre nella saletta di Borgo Bovio; l'articolo ha la foto dell'assemblea.",
          "quotes": "«Il programma lo scriviamo nei quartieri» (Terni 2027)", "acts": None,
          "keywords": "nascita della lista, T27, lista civica, assemblea costitutiva, quartieri, programma "
                      "partecipato",
          "persons": [], "bodies": ["Terni 2027"], "places": ["Borgo Bovio"], "themes": ["Campagna"],
          "related": []},
        {"key": "cn_gazebo_bovio", "channel": "Conca Notizie", "kind": "article", "published_on": "2026-10-12",
          "event_date": None, "stance": "positive", "relevance": "2",
          "url": "https://concanotizie.example/terni-2027-gazebo-borgo-bovio",
          "title": "Terni 2027 al mercato di Borgo Bovio: «Case, bus e verde le richieste più frequenti»",
          "abstract": "Secondo Conca Notizie (testata fittizia) del 12 ottobre 2026, Terni 2027 è al mercato di "
                      "Borgo Bovio con il gazebo; casa, bus e verde sono le richieste più frequenti dei cittadini.",
          "quotes": "«Case, bus e verde le richieste più frequenti» (Terni 2027)", "acts": None,
          "keywords": "gazebo, banchetto, mercato, T27, ascolto, richieste dei cittadini, casa, trasporti, verde "
                      "pubblico",
          "persons": [], "bodies": ["Terni 2027"], "places": ["Borgo Bovio"], "themes": ["Campagna"],
          "related": []},
        {"key": "tc_borgo_rivo", "channel": "TerniCittà", "kind": "article", "published_on": "2026-10-19",
          "event_date": None, "stance": "positive", "relevance": "2",
          "url": "https://ternicitta.example/2026/10/19/borgo-rivo-inquilini-ater",
          "title": "Borgo Rivo, gli inquilini delle case Ater mostrano muffa e infiltrazioni alla lista civica",
          "abstract": "Secondo TerniCittà (testata fittizia) del 19 ottobre 2026, a Borgo Rivo gli inquilini delle "
                      "case ATER mostrano alla lista civica Terni 2027 muffa e infiltrazioni negli appartamenti. "
                      "Le foto dell'articolo mostrano i soffitti, nessuna persona.",
          "quotes": None, "acts": None,
          "keywords": "case popolari, Ater, inquilini, muffa, infiltrazioni, palazzine, sopralluogo, comitato "
                      "inquilini",
          "persons": [], "bodies": ["ATER", "Terni 2027"], "places": ["Borgo Rivo"], "themes": ["Casa e sociale"],
          "related": []},
        {"key": "rnl_intervista", "channel": "Radio Nera Libera", "kind": "other", "published_on": "2026-10-15",
          "event_date": None, "stance": "positive", "relevance": "2",
          "url": "https://radioneralibera.example/podcast/terni-2027-casa",
          "title": "Intervista al portavoce di Terni 2027 su casa e affitti",
          "abstract": "Secondo Radio Nera Libera (emittente fittizia) del 15 ottobre 2026, intervista audio al "
                      "portavoce di Terni 2027, Michele Santarelli, su casa e affitti. L'audio è della lista e si "
                      "può trascrivere: trascrizione ancora da fare.",
          "quotes": None, "acts": None,
          "keywords": "intervista, podcast, radio, portavoce, Michele, affitti, emergenza casa",
          "persons": ["Michele Santarelli"], "bodies": ["Terni 2027"], "places": [], "themes": ["Casa e sociale"],
          "related": []},
        {"key": "ts_mense", "channel": "Terni Sera", "kind": "article", "published_on": "2026-10-13",
          "event_date": "2026-10-12", "stance": "positive", "relevance": "2",
          "url": "https://ternisera.example/mense-pulizie-impegno-lista",
          "title": "Mense e pulizie del Comune, la lista civica firma un impegno con le lavoratrici",
          "abstract": "Secondo Terni Sera (testata fittizia) del 13 ottobre 2026, la lista civica Terni 2027 firma "
                      "un impegno con le lavoratrici delle mense e delle pulizie del Comune di Terni. L'impegno "
                      "scritto della lista è stato consegnato a mano il 12 ottobre: riassorbimento del personale "
                      "al cambio d'appalto con stesse ore e stesso contratto.",
          "quotes": None, "acts": None,
          "keywords": "mense scolastiche, pulizie, appalti, cambio d'appalto, clausola sociale, lavoratrici, "
                      "impegno firmato",
          "persons": [], "bodies": ["Terni 2027", "Comune di Terni"], "places": [],
          "themes": ["Lavoro e sviluppo"], "related": []},
        {"key": "cn_cer", "channel": "Conca Notizie", "kind": "article", "published_on": "2026-10-05",
          "event_date": None, "stance": "positive", "relevance": "2",
          "url": "https://concanotizie.example/cer-case-popolari-terni-2027",
          "title": "Energia condivisa sui tetti delle case popolari: ambientalisti e Terni 2027 al lavoro",
          "abstract": "Secondo Conca Notizie (testata fittizia) del 5 ottobre 2026, ambientalisti e Terni 2027 "
                      "lavorano a una comunità di energia condivisa sui tetti delle case popolari. La lista ne ha "
                      "concordato i punti con il Coordinamento ambientalisti della conca.",
          "quotes": None, "acts": None,
          "keywords": "CER, comunità energetica rinnovabile, energia condivisa, fotovoltaico, pannelli solari, "
                      "tetti, case popolari, Ater",
          "persons": [], "bodies": ["Terni 2027", "Coordinamento ambientalisti della conca"], "places": [],
          "themes": ["Ambiente"], "related": []},
        {"key": "tc_sanita", "channel": "TerniCittà", "kind": "article", "published_on": "2026-10-28",
          "event_date": None, "stance": "positive", "relevance": "2",
          "url": "https://ternicitta.example/2026/10/28/terni-2027-assemblea-sanita",
          "title": "Sanità, Terni 2027 annuncia un'assemblea pubblica a fine novembre",
          "abstract": "Secondo TerniCittà (testata fittizia) del 28 ottobre 2026, Terni 2027 annuncia un'assemblea "
                      "pubblica sulla sanità a fine novembre 2026. Secondo i nostri appunti interni l'assemblea è "
                      "fissata per sabato 28 novembre, con gli operatori del pronto soccorso se vengono.",
          "quotes": None, "acts": None,
          "keywords": "assemblea sanità, incontro pubblico, ospedale, pronto soccorso, sanità pubblica, novembre",
          "persons": [], "bodies": ["Terni 2027"], "places": [], "themes": ["Sanità"], "related": []},
        {"key": "cn_osservatorio", "channel": "Conca Notizie", "kind": "article", "published_on": "2026-10-10",
          "event_date": None, "stance": "neutral", "relevance": "2",
          "url": "https://concanotizie.example/osservatorio-civico-societa-comunali",
          "title": "Società del Comune, l'Osservatorio civico chiede trasparenza: in sala anche le liste civiche",
          "abstract": "Secondo Conca Notizie (testata fittizia) del 10 ottobre 2026, l'Osservatorio civico chiede "
                      "trasparenza sulle società del Comune di Terni; alla serata erano presenti anche le liste "
                      "civiche, tra cui Terni 2027. Quanto sostenuto dall'Osservatorio su incarichi e compensi è, "
                      "per la lista, da verificare sugli atti.",
          "quotes": None, "acts": None,
          "keywords": "società comunali, partecipate, trasparenza, CdA, compensi, Osservatorio civico, liste "
                      "civiche",
          "persons": [], "bodies": ["Osservatorio civico", "Comune di Terni", "Terni 2027"], "places": [],
          "themes": ["Partecipazione e trasparenza"], "related": []},
        {"key": "ts_tavolo", "channel": "Terni Sera", "kind": "article", "published_on": "2026-10-31",
          "event_date": None, "stance": "positive", "relevance": "3",
          "url": "https://ternisera.example/civiche-tavolo-programma",
          "title": "Centrosinistra, le civiche al tavolo del programma: «Prima i contenuti, poi i nomi»",
          "abstract": "Secondo Terni Sera (testata fittizia) del 31 ottobre 2026, le liste civiche del "
                      "centrosinistra partecipano al tavolo del programma con la linea prima i contenuti, poi i "
                      "nomi. Il virgolettato è del portavoce di Terni 2027, Michele Santarelli.",
          "quotes": "«Prima i contenuti, poi i nomi» (Michele Santarelli)", "acts": None,
          "keywords": "il tavolo, tavolo di coalizione, centrosinistra, csx, programma comune, liste civiche, "
                      "candidature, portavoce",
          "persons": ["Michele Santarelli"], "bodies": ["Terni 2027"], "places": [], "themes": ["Campagna"],
          "related": []},
        {"key": "ig_reel", "channel": "Instagram terni2027", "kind": "video", "published_on": "2026-10-02",
          "event_date": None, "stance": "positive", "relevance": "1",
          "url": "https://instagram.example/terni2027/reel/perche-una-lista-civica",
          "title": "Reel: perché una lista civica",
          "abstract": "Reel del profilo Instagram terni2027 del 2 ottobre 2026, canale della lista: spiega perché "
                      "una lista civica. È un video nostro, pubblicato sui social della lista; il testo è nel "
                      "drive della lista.",
          "quotes": None, "acts": None,
          "keywords": "reel, Instagram, social, video nostro, lista civica, perché una lista civica",
          "persons": [], "bodies": ["Terni 2027"], "places": [], "themes": ["Campagna"], "related": []},
    ],
}
