# Copyright 2026 Daniele Lucarelli
# License CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/).
"""The demo of the pack studio_progettazione: «Studio Tre Archi», an invented engineering and architecture firm.

Everything is invented: the studio, its people, its customers (a municipality, a social housing agency, a
condominium, a private client, a manufacturing company), their commissions, amounts, dates, tasks, chatter, hours,
rules, facts, procedures, internal documents and lessons. The profile of the studio (an associated studio of
engineers and architects in Terni: civil and industrial design, works direction and safety, BIM, energy retrofit,
restoration, Industria 5.0 support) follows only the kinds of services such a studio offers; no name, commission or
wording of a real one. Nothing concerns a real person, a served person or an address. The texts of demo/texts/*.md
(the public contracts code and its annexes, the fee decree, the CAM, the Conto Termico 3.0, the safety rules of
construction sites, an ANAC model tender, a TED notice, regional acts) are public acts, converted with Docling; what
the studio did with them is invented.

The chatter is written as engineers write in a hurry: terse notes full of acronyms and codes (SAL, CdP, CSE, PSC,
oGI, pGI, ACDat, QbII.05, E.20), first names, days of the week; customers write in their own plain words. On it
lies the curated layer of the memory: the searchable session note of every task, with its keywords (acronym,
expanded form, the word a non-technical person would use), the keywords of rules, facts, procedures, lessons and
documents, the summaries of the documents. Scenario S2 of the measure of the memory in four contexts: its question
sets are demo/questions.json. Loaded by <core>/setup/load-demo.sh through <core>/scripts/load_demo.py, only into the
databases of DATABASES.
"""

DATABASES = ("scenario-studio",)
TOKEN_NAME = "Tre Archi demo"
TOKEN_DAYS = 30

COMPANY = {"name": "Studio Tre Archi", "email": "studio@trearchi.example", "website": "https://trearchi.example"}

# role: (name, login, hub group). A partner engineer is the lead; the other partner is a hub lead too; the
# architect, the BIM coordinator, the junior and the office are members.
USERS = {
    "admin": ("Amministratore Tre Archi", None, "texo.group_texo_admin"),
    "lead": ("Andrea Montanucci", "andrea.montanucci@trearchi.example", "texo.group_texo_lead"),
    "partner": ("Lorenzo Paparelli", "lorenzo.paparelli@trearchi.example", "texo.group_texo_lead"),
    "arch": ("Chiara Bonifazi", "chiara.bonifazi@trearchi.example", "texo.group_texo_member"),
    "bim": ("Matteo Federici", "matteo.federici@trearchi.example", "texo.group_texo_member"),
    "junior": ("Elena Rinaldi", "elena.rinaldi@trearchi.example", "texo.group_texo_member"),
    "office": ("Rita Mattioli", "segreteria@trearchi.example", "texo.group_texo_member"),
}
WORK_GROUPS = ("project.group_project_user", "hr_timesheet.group_hr_timesheet_user")
TEAM = ("lead", "partner", "arch", "bim", "junior", "office")

# The stages: the last one of each list is folded (done).
DELIVERY_STAGES = ["Da fare", "In corso", "In attesa", "Fatto"]
TICKET_STAGES = ["Nuovo", "In lavorazione", "In attesa", "Risolto", "Chiuso"]
HOME_STAGES = ["Da fare", "In corso", "Fatto", "Annullato"]
GARE_STAGES = ["Scouting", "Valutazione", "In preparazione", "Inviata", "Chiusa"]
TICKET_TAG = "ticket"
ASSISTANCE = "Assistenza {name}"

# -- the sources: the generated PDFs of the studio's own cloud folder and of a task --------------------------------
SOURCES_FOLDER = "https://cloud.trearchi.example/procedure"
PROCEDURE_PDF = ("checklist-emissione-elaborati.pdf", "Checklist emissione elaborati (rev. 4)", [
    "1. Codifica file secondo linee guida BIM studio (commessa-fase-disciplina-tipo-numero-rev).",
    "2. Cartiglio: rev, data, redatto/controllato/approvato. Mai emettere senza il controllato.",
    "3. Modelli: export IFC 4 + verifica in viewer indipendente, BCF aperti chiusi o motivati.",
    "4. PDF firmati digitalmente (PAdES) dal progettista responsabile della disciplina.",
    "5. Elenco elaborati aggiornato e trasmissione con lettera o PEC, protocollo interno.",
    "6. Copia dell'emissione nella cartella PUBLISHED dell'ACDat, mai solo per mail.",
])
# the PDF attached to a task (ATTACHMENTS, by key)
STAGE_REPORT_PDF = ("verbale-prova-carico-solaio.pdf", "Verbale prova di carico solaio (fittizio)", [
    "Prova di carico su campata tipo del solaio piano primo, carico distribuito con cisterne.",
    "Freccia massima misurata 3,1 mm, residuo dopo scarico 0,2 mm: esito positivo.",
    "Presenti DL, impresa, collaudatore.",
])
ATTACHMENTS = {"stage_report": STAGE_REPORT_PDF}

# -- the organisation: its documents, rules, facts, procedures, home tasks and own projects ------------------------
P_GARE = "Gare SIA 2026"
P_BIMSTD = "Standard BIM dello studio"
P_CFP = "Formazione e crediti CFP 2026"
P_QUALITA = "Qualità e procedure interne"

NORMA = "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2023-03-31;36"

ORGANISATION = {
    "documents": [
        {"key": "checklist_emissione", "name": "Checklist emissione elaborati (rev. 4)",
         "summary": "Procedura interna dello studio (rev. 4) con i controlli da fare prima di emettere "
                    "elaborati e modelli. Copre codifica dei file, cartiglio, verifica dell'IFC in un viewer "
                    "indipendente, firma digitale PAdES, trasmissione e copia nello stato PUBLISHED dell'ACDat; "
                    "la revisione 4 nasce dalla non conformità sull'IFC rifiutato dall'ATER.",
         "pdf": PROCEDURE_PDF, "keep_text": True,
         "keywords": "checklist emissione elaborati, rev. 4, controllo tavole prima dell'invio, IFC verificato "
                     "/ viewer indipendente, firma PAdES / firma digitale, cartiglio e codifica, PUBLISHED / "
                     "ACDat, sistema qualità"},
        {"key": "linee_guida_bim", "name": "Linee guida BIM dello studio (rev. 2026)",
         "summary": "Linee guida BIM interne dello studio, revisione 2026. Definiscono i ruoli (BIM manager, "
                    "coordinator, specialist, CDE manager), gli stati dell'ACDat WIP/SHARED/PUBLISHED/ARCHIVED, "
                    "la codifica COMMESSA-FASE-DISCIPLINA-TIPO-NNN-REV, i formati di consegna (IFC 4, IFC 2x3 "
                    "solo se richiesto, BCF, PDF/A), i LOIN per fase (LOD B/C PFTE, D esecutivo, F as-built "
                    "impianti) e la clash detection settimanale con tolleranze 10 mm hard e 50 mm soft; danno "
                    "regole anche per l'oGI.",
         "url": "https://cloud.trearchi.example/standard/linee-guida-bim-2026", "keep_text": True,
         "text": "## Linee guida BIM - Studio Tre Archi (rev. 2026)\n\n"
                 "1. Ruoli. BIM manager: Andrea (partner). BIM coordinator: Matteo. BIM specialist: chi modella la "
                 "disciplina. CDE manager: Matteo, sostituto Elena. Ruoli e nomi vanno nel pGI di ogni commessa.\n\n"
                 "2. ACDat. Stati WIP -> SHARED -> PUBLISHED -> ARCHIVED. In SHARED solo modelli verificati dal "
                 "coordinator; in PUBLISHED solo IFC e PDF firmati. Nessuno lavora in locale fuori dall'ACDat.\n\n"
                 "3. Codifica. COMMESSA-FASE-DISCIPLINA-TIPO-NNN-REV, es. ATR-PFT-ARC-M3D-001-R02. Discipline: "
                 "ARC, STR, MEC, ELE, SIC.\n\n"
                 "4. Formati. Il modello nativo è uno strumento di lavoro: la consegna ufficiale è IFC 4 (IFC 2x3 "
                 "solo se il capitolato informativo lo chiede), più BCF per le issue e PDF/A per gli elaborati. "
                 "Ogni IFC si apre e si controlla in un viewer indipendente prima di emettere.\n\n"
                 "5. LOIN. PFTE: geometria LOD B/C, informazioni minime di ingombro e prestazione. Esecutivo: "
                 "LOD D, schede prodotto, codici WBS del computo. As-built: LOD F per gli impianti.\n\n"
                 "6. Clash detection. Ogni settimana su modello federato: hard clash tolleranza 10 mm, soft clash "
                 "(spazi di manutenzione) 50 mm. Le issue si aprono in BCF con responsabile e scadenza; si chiude "
                 "solo con verifica sul modello aggiornato.\n\n"
                 "7. Offerta di gestione informativa (oGI): modello base in cartella gare, si adatta al capitolato "
                 "informativo par. per par. e non si promette nulla che lo studio non ha (software, ruoli "
                 "certificati).\n",
         "keywords": "linee guida BIM, standard BIM studio, ruoli UNI 11337-7, ACDat / CDE / ambiente di "
                     "condivisione dati, codifica file, IFC 4 / BCF / PDF/A, LOIN / LOD, clash detection / "
                     "tolleranze, oGI / offerta di gestione informativa"},
        {"key": "glossario", "name": "Glossario dello studio",
         "summary": "Le sigle e i termini tecnici dello studio con la forma estesa e le parole dei committenti: "
                    "SAL e acconto, pGI e piano BIM, APE e certificato energetico, CSE e coordinatore della "
                    "sicurezza, una voce per riga.",
         "keywords": "glossario, sigle, acronimi, forma estesa, vocabolario controllato, parole del committente, "
                     "terminologia tecnica",
         "url": "https://cloud.trearchi.example/standard/glossario", "text_file": "glossario", "keep_text": True},
        {"key": "anac_bando_tipo_2", "name": "ANAC Bando tipo 2/2026 - disciplinare SIA sopra soglia",
         "summary": "Bando tipo n. 2/2026 dell'ANAC, approvato con delibera n. 153 del 15 aprile 2026: schema "
                    "di disciplinare per procedure aperte di servizi di architettura e ingegneria di importo "
                    "pari o superiore alle soglie europee (art. 14 D.Lgs. 36/2023), aggiudicate con OEPV sul "
                    "miglior rapporto qualità/prezzo. Regola requisiti, soccorso istruttorio, offerta tecnica "
                    "ed economica, equo compenso e BIM; è vincolante per le gare SIA sopra soglia e spesso "
                    "ricalcato anche sotto soglia.",
         "url": "https://www.anticorruzione.it/-/bando-tipo-n.-2-2026-servizi-architettura-ingegneria",
         "text_file": "anac-bando-tipo-2-2026-sia",
         "keywords": "bando tipo ANAC 2/2026, disciplinare di gara SIA, delibera 153/2026, sopra soglia UE, "
                     "OEPV / offerta economicamente più vantaggiosa / miglior rapporto qualità prezzo, soccorso "
                     "istruttorio, equo compenso, servizi di ingegneria e architettura"},
        {"key": "dm_17_06_2016", "name": "DM 17/06/2016 - corrispettivi SIA (articolato)",
         "summary": "Articolato del D.M. 17 giugno 2016 del Ministro della giustizia di concerto con il MIT "
                    "(decreto parametri), emanato in base all'art. 24 c. 8 del D.Lgs. 50/2016. Approva le "
                    "tabelle dei corrispettivi dei servizi di architettura e ingegneria commisurati al livello "
                    "qualitativo delle prestazioni: CP = V x G x Q x P, spese e oneri accessori, categorie "
                    "d'opera, gradi di complessità e prestazioni Q. È la base di ogni parcella e preventivo "
                    "dello studio.",
         "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:ministero.giustizia:decreto:2016-06-17",
         "text_file": "dm-17-06-2016-corrispettivi-sia",
         "keywords": "DM 17/06/2016 / decreto parametri, corrispettivi SIA / tariffe professionali, calcolo "
                     "parcella / onorario, CP = V x G x Q x P, spese e oneri accessori, base di gara, D.Lgs. "
                     "50/2016 art. 24"},
        {"key": "dm_tavole_categorie", "name": "DM 17/06/2016 - tavole (categorie, G, Q)",
         "summary": "Tavole allegate al D.M. 17/06/2016 (testo OCR dalla Gazzetta Ufficiale): classificazione "
                    "delle categorie d'opera E, S, IA, V, D, T, P, U con i gradi di complessità G e le "
                    "corrispondenze con le classi della vecchia L. 143/49, e aliquote Q delle prestazioni per "
                    "fase. Lo studio le usa per scegliere categoria e G (es. E.20 0,95, E.21 1,20, E.22 1,55).",
         "url": "https://www.gazzettaufficiale.it/eli/id/2016/07/27/16A05398/sg#tavole",
         "text_file": "dm-17-06-2016-tavole",
         "keywords": "tavole DM 17/06/2016, categorie d'opera / ID opere, grado di complessità G, aliquote Q / "
                     "prestazioni, E.20 / E.22 / S.03 / IA.02, corrispondenze L. 143/49, classificazione dei "
                     "servizi"},
        {"key": "all_i13", "name": "D.Lgs. 36/2023 All. I.13 - parametri per la progettazione",
         "summary": "Allegato I.13 del D.Lgs. 36/2023 (art. 41 c. 15): determina i corrispettivi della "
                    "progettazione attualizzando la tabella Z-2 del DM 17/06/2016 ai due livelli PFTE ed "
                    "esecutivo. Le aliquote del preliminare e del definitivo vanno al PFTE; QbII.05 va "
                    "all'esecutivo se non c'è appalto integrato, al PFTE se c'è; QbII.08 non si applica "
                    "nell'appalto integrato; QbIII.03-.05 e .07 si dividono a metà solo nell'appalto integrato.",
         "url": NORMA + "~all.I.13", "text_file": "dlgs-36-2023-allegato-i13-corrispettivi",
         "keywords": "All. I.13, parametri progettazione / corrispettivi, due livelli di progettazione, PFTE / "
                     "progetto di fattibilità tecnica ed economica, progetto esecutivo, QbII.05, appalto "
                     "integrato, DM 17/06/2016 tabella Z-2"},
        {"key": "all_i7", "name": "D.Lgs. 36/2023 All. I.7 - contenuti dei livelli di progettazione",
         "summary": "Allegato I.7 del D.Lgs. 36/2023 (artt. 41-44): contenuti minimi dei documenti di "
                    "progettazione. Definisce quadro esigenziale (competenza del committente), DOCFAP "
                    "(documento di fattibilità delle alternative progettuali), DIP (documento di indirizzo "
                    "della progettazione), PFTE e progetto esecutivo, con la possibilità di supportarli con "
                    "modelli informativi BIM e GIS.",
         "url": NORMA + "~all.I.7", "text_file": "dlgs-36-2023-allegato-i7-progettazione",
         "keywords": "All. I.7, livelli di progettazione, quadro esigenziale, DOCFAP / documento di fattibilità "
                     "delle alternative progettuali, DIP / documento di indirizzo della progettazione, PFTE, "
                     "progetto esecutivo, elaborati minimi"},
        {"key": "codice_articoli", "name": "D.Lgs. 36/2023 - articoli scelti (testo vigente)",
         "summary": "Estratto del D.Lgs. 36/2023 (codice dei contratti pubblici), testo vigente al 1° novembre "
                    "2026 con il correttivo D.Lgs. 209/2024. Articoli scelti su RUP (art. 15, responsabile "
                    "unico del progetto, nominato nel primo atto di avvio), livelli di progettazione (art. 41), "
                    "BIM (art. 43), affidamenti sotto soglia (art. 50), OEPV, direzione lavori e collaudo.",
         "url": NORMA, "text_file": "dlgs-36-2023-articoli-scelti",
         "keywords": "D.Lgs. 36/2023 / codice appalti, codice dei contratti pubblici, correttivo D.Lgs. "
                     "209/2024, RUP / responsabile unico del progetto, art. 50 affidamento diretto / sotto "
                     "soglia, art. 43 BIM, OEPV, direzione lavori e collaudo"},
        {"key": "dlgs_cantieri_sicurezza", "name": "D.Lgs. 81/2008 artt. 88-101 e All. XV",
         "summary": "Titolo IV Capo I del D.Lgs. 81/2008 (artt. 88-101) e Allegato XV, testo vigente: sicurezza "
                    "nei cantieri temporanei o mobili. Regola campo di applicazione ed esclusioni, obblighi del "
                    "committente, CSP e CSE, contenuti minimi di PSC e POS, notifica preliminare (art. 99) e "
                    "obblighi delle imprese.",
         "url": "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2008-04-09;81",
         "text_file": "dlgs-81-2008-cantieri-allegato-xv",
         "keywords": "D.Lgs. 81/2008 / testo unico sicurezza, cantieri temporanei o mobili, CSP / CSE / "
                     "coordinatore sicurezza, PSC / piano di sicurezza e coordinamento, POS / piano operativo "
                     "di sicurezza, notifica preliminare art. 99, Allegato XV, committente"},
        {"key": "cam_dm", "name": "DM MASE 24/11/2025 - nuovi CAM edilizia (decreto)",
         "summary": "Decreto del Ministero dell'ambiente e della sicurezza energetica (MASE) del 24 novembre "
                    "2025, pubblicato in GU n. 281 del 3/12/2025: adotta i nuovi criteri ambientali minimi per "
                    "progettazione e lavori edilizi, sostituendo il DM 256/2022 e il correttivo 2024. Si "
                    "applica da febbraio 2026; il testo estratto è in gran parte illeggibile (OCR).",
         "url": "https://www.gazzettaufficiale.it/eli/id/2025/12/03/25A06571/sg",
         "text_file": "cam-edilizia-dm-24-11-2025",
         "keywords": "DM MASE 24/11/2025, CAM edilizia / criteri ambientali minimi, GU 281/2025, DM 256/2022 "
                     "sostituito, appalti verdi / GPP, decreto CAM, progettazione sostenibile"},
        {"key": "cam_criteri", "name": "CAM edilizia 2025 - Allegato 1 (criteri)",
         "summary": "Allegato 1 dei CAM edilizia 2025 (Piano d'azione nazionale sul Green Public Procurement): "
                    "criteri ambientali minimi per servizi di progettazione e direzione lavori e per i lavori "
                    "edilizi. Contiene i criteri di progettazione (2.x, tra cui 2.4.7 isolanti e 2.6.6 "
                    "contenuto di riciclato), i criteri per i lavori (3.x), i criteri premianti, LCA e LCC e le "
                    "modalità di verifica.",
         "url": "https://www.mase.gov.it/portale/documents/cam-edilizia-2025-allegato-1",
         "text_file": "cam-edilizia-2025-criteri",
         "keywords": "CAM edilizia 2025 allegato 1, criteri ambientali minimi, criterio 2.4.7 isolanti, "
                     "criterio 2.6.6 contenuto di riciclato, LCA / LCC, criteri premianti, PANGPP / Green "
                     "Public Procurement, relazione CAM"},
        {"key": "ct3_dm", "name": "DM 7/8/2025 - Conto Termico 3.0",
         "summary": "Decreto del Ministro dell'ambiente e della sicurezza energetica del 7 agosto 2025 (GU n. "
                    "224 del 26/9/2025), il Conto Termico 3.0. Incentiva interventi di piccole dimensioni di "
                    "efficienza energetica e produzione di energia termica da fonti rinnovabili: soggetti "
                    "ammessi, interventi, accesso diretto o a prenotazione, diagnosi energetica e APE.",
         "url": "https://www.gazzettaufficiale.it/eli/id/2025/09/26/25A05310/sg",
         "text_file": "conto-termico-3-0-dm-07-08-2025",
         "keywords": "Conto Termico 3.0 / CT 3.0, DM 7/8/2025, incentivi efficienza energetica, rinnovabili "
                     "termiche, accesso a prenotazione, diagnosi energetica / APE, GSE, contributo statale"},
        {"key": "dd_618", "name": "Regione Umbria DD 618/2026 - elenchi regionali",
         "summary": "Determinazione dirigenziale n. 618 del 23/01/2026 della Regione Umbria: approva "
                    "l'aggiornamento dell'elenco regionale delle imprese per lavori pubblici sotto soglia con "
                    "le domande dall'1/11 al 31/12/2025 (art. 26 L.R. 3/2010). Le premesse ricostruiscono gli "
                    "elenchi della L.R. 3/2010 (artt. 21 e 26: professionisti per SIA, imprese per lavori), le "
                    "soglie portate alla soglia UE dalla L.R. 15/2023 e la gestione sul Portale Acquisti "
                    "Umbria. Non è l'elenco dei professionisti.",
         "url": "https://www.regione.umbria.it/opere-pubbliche/elenchi-regionali?atto=dd-618-2026",
         "text_file": "umbria-dd-618-2026-elenco-professionisti",
         "keywords": "DD 618/2026, Regione Umbria, elenco regionale imprese, elenco regionale professionisti, "
                     "L.R. 3/2010 artt. 21 e 26, L.R. 15/2023, Portale Acquisti Umbria, sotto soglia / "
                     "procedura negoziata"},
    ],
    "rules": [
        {"name": "Consegna ufficiale solo IFC", "severity": "never", "activities": [], "section": "operations",
         "keywords": "IFC, formato aperto, consegna ufficiale solo IFC, IFC 4 / formato aperto, modello nativo "
                     "vietato, rvt / pln / formato proprietario, PDF firmati, consegna a stazione appaltante, "
                     "ok del partner",
         "body": "Mai mandare il modello nativo (rvt/pln/ecc.) come consegna ufficiale a SA o committente. Si "
                 "emette IFC 4 (o la versione del CI) + PDF firmati. Il nativo solo se il contratto lo prevede, "
                 "a parte, con ok di un partner."},
        {"name": "SAL solo con libretto delle misure", "severity": "never", "activities": [],
         "section": "operations",
         "body": "Il DL non firma un SAL senza libretto delle misure aggiornato e controllato in contraddittorio. "
                 "Niente SAL a percentuale o sulla parola dell'impresa, nemmeno sui privati.",
         "keywords": "SAL / stato avanzamento lavori / acconto, libretto delle misure, misure in "
                     "contraddittorio, niente SAL a percentuale, DL / direttore dei lavori, contabilità lavori, "
                     "anche cantieri privati"},
        {"name": "Niente inizio lavori senza notifica e PSC", "severity": "never", "activities": [],
         "section": "compliance",
         "body": "Nei cantieri dove siamo CSE: nessuna impresa entra prima di notifica preliminare inviata (quando "
                 "dovuta), PSC consegnato, POS verificati. Vale anche per allestimento e recinzione.",
         "keywords": "inizio lavori, notifica preliminare, PSC / piano di sicurezza e coordinamento, POS "
                     "verificati / piano operativo di sicurezza, CSE / coordinatore sicurezza in esecuzione, "
                     "allestimento e recinzione, divieto accesso imprese"},
        {"name": "Con la stazione appaltante parla il partner di commessa", "severity": "must",
         "activities": ["communication"], "section": "operations",
         "body": "RUP, uffici tecnici, ATER: comunicazioni formali solo dal partner responsabile (o con lui in "
                 "copia), via PEC o piattaforma. Junior e collaboratori non mandano mail tecniche alla SA.",
         "keywords": "comunicazioni con la stazione appaltante, partner di commessa, RUP / uffici tecnici / "
                     "ATER, PEC / piattaforma, comunicazioni formali, junior e collaboratori, SA / stazione "
                     "appaltante"},
        {"name": "Crediti CFP registrati entro il mese", "severity": "must", "activities": [],
         "section": "compliance",
         "body": "Ogni corso/seminario: attestato in cartella CFP e riga nel foglio crediti entro fine mese. "
                 "Autocertificazione sul portale dell'ordine entro i termini.",
         "keywords": "CFP / crediti formativi, registrazione entro il mese, attestato in cartella CFP, foglio "
                     "crediti, autocertificazione portale ordine, corsi e seminari"},
        {"name": "Parcella sempre con DM 17/06/2016", "severity": "must", "activities": ["analysis"],
         "section": "offer",
         "body": "Ogni offerta a SA e ogni preventivo sopra 10k parte dal calcolo DM 17/06/2016 (foglio "
                 "parcella dello studio), verificato da un secondo. Categoria e G controllati sulle tavole.",
         "keywords": "DM 17/06/2016 / decreto parametri, parcella / calcolo corrispettivo, preventivo sopra 10 "
                     "mila, offerta a stazione appaltante, foglio parcella studio, verifica di un secondo, "
                     "categoria e grado di complessità G"},
    ],
    "notes": [
        {"kind": "fact", "section": "profile", "name": "Chi è lo studio",
         "body": "Studio associato di ingegneri e architetti a Terni, dal 2019. Due partner ing. (Andrea "
                 "strutture/DL, Lorenzo impianti/energia), Chiara arch. restauro e paesaggio, Matteo BIM "
                 "coordinator, Elena junior, Rita segreteria e amministrazione. Progettazione civile e "
                 "industriale, DL e sicurezza, BIM, riqualificazione energetica, restauri, supporto Industria "
                 "5.0. Iscritti all'elenco regionale professionisti Umbria.",
         "keywords": "Studio Tre Archi, studio associato ingegneri architetti, Terni, organigramma / ruoli, "
                     "strutture e DL / direzione lavori, impianti ed energia, restauro e paesaggio, BIM "
                     "coordinator, elenco regionale professionisti, Industria 5.0"},
        {"kind": "fact", "section": "compliance", "name": "Polizza RC professionale",
         "body": "RC prof. studio massimale 2,5 mln, rinnovo 30/4. Per le gare: copia polizza + quietanza "
                 "nella cartella documenti standard. Polizza progettista per verifica esecutivi: a parte, "
                 "per commessa.",
         "keywords": "polizza RC professionale, responsabilità civile professionale, assicurazione studio, "
                     "massimale 2,5 milioni, rinnovo 30/4, quietanza, polizza progettista verifica, documenti "
                     "standard gare"},
        {"kind": "fact", "section": "offer", "name": "Affidamenti diretti e soglie",
         "keywords": "sotto soglia, affidamento diretto, soglia 140 mila / sotto soglia, art. 50 D.Lgs. "
                     "36/2023, correttivo D.Lgs. 209/2024, equo compenso, ribasso solo sul 35%, ribasso massimo "
                     "20%, elenco regionale professionisti, procedura negoziata",
         "body": "D.Lgs. 36/2023 + correttivo 209/2024. SIA sotto 140k: affidamento diretto (art. 50), anche "
                 "senza più preventivi, scegliendo tra chi ha esperienza documentata; in Umbria le SA pescano "
                 "spesso dall'elenco regionale professionisti. Sopra 140k procedura. Equo compenso: sopra "
                 "140k il 65% del corrispettivo è fisso e il ribasso solo sul 35%, max 30 punti al prezzo; "
                 "negli affidamenti diretti ribasso max 20%."},
        {"kind": "fact", "section": "offer", "name": "Formula parcella",
         "body": "CP = V x G x Q x P + spese. P = 0,03 + 10/V^0,4. Spese fino al 25% sotto 1 mln di lavori, "
                 "scendono a 10% sopra 25 mln (interpolare). All. I.13: preliminare+definitivo -> PFTE, "
                 "QbII.05 va all'esecutivo se non è appalto integrato. Categoria su tavole DM (E.20 esistenti "
                 "G 0,95; E.21 G 1,20; E.22 vincolati G 1,55).",
         "keywords": "formula parcella / calcolo corrispettivo, CP = V x G x Q x P, DM 17/06/2016 / decreto "
                     "parametri, spese e oneri accessori, All. I.13, QbII.05, grado di complessità G, E.20 / "
                     "E.21 / E.22, onorario professionale"},
        {"kind": "fact", "section": "compliance", "name": "BIM obbligatorio",
         "body": "Dal 1/1/2025 metodi BIM obbligatori per nuove opere e interventi su esistente sopra 2 mln di "
                 "lavori (art. 43 e All. I.9). Formati aperti. CI della SA, oGI in offerta, pGI "
                 "dell'aggiudicatario. Ruoli UNI 11337-7: BIM manager, coordinator, specialist, CDE manager.",
         "keywords": "BIM obbligatorio, soglia 2 milioni, art. 43 / All. I.9, formati aperti / IFC, CI / "
                     "capitolato informativo, oGI / offerta di gestione informativa, pGI / piano di gestione "
                     "informativa, UNI 11337-7 ruoli BIM, CDE manager"},
        {"kind": "fact", "section": "compliance", "name": "CAM nuovi",
         "body": "DM MASE 24/11/2025 (GU 281 3/12/2025), si applicano da febbraio 2026, sostituiscono il DM "
                 "256/2022. Progetti pubblici avviati dopo: relazione CAM con verifica criterio per criterio. "
                 "Attenzione 2.4.7 isolanti e contenuto di riciclato: servono dichiarazioni/EPD del prodotto.",
         "keywords": "CAM / criteri ambientali minimi, DM MASE 24/11/2025, da febbraio 2026, DM 256/2022 "
                     "sostituito, relazione CAM, criterio 2.4.7 isolanti, contenuto di riciclato, EPD / "
                     "dichiarazione ambientale di prodotto, appalti verdi / GPP"},
        {"kind": "fact", "section": "sector", "name": "Detrazioni 2026-2027",
         "body": "2026: 50% abitazione principale, 36% altri immobili. 2027: 36% / 30%. Superbonus finito per i "
                 "nostri condomini. EPBD case green: non recepita, termine 29/5/2026 mancato, niente obblighi "
                 "nuovi per ora.",
         "keywords": "detrazioni fiscali / bonus casa, 50% abitazione principale, 36% seconde case, detrazioni "
                     "2027 36% / 30%, superbonus finito, EPBD / direttiva case green, recepimento mancato, "
                     "bonus ristrutturazione"},
        {"kind": "fact", "section": "sector", "name": "Conto Termico 3.0 - stato",
         "body": "DM 7/8/2025. PortalTermico aperto 2/2/2026, sospeso 3/3/2026 per budget 2026 esaurito, "
                 "riaperto 13/4/2026. Per PA ed ex IACP anche accesso a prenotazione, diagnosi ante allegata "
                 "per gli interventi che la richiedono.",
         "keywords": "Conto Termico 3.0, DM 7/8/2025, PortalTermico, GSE / Gestore servizi energetici, portale "
                     "sospeso / budget esaurito, accesso a prenotazione, PA ed ex IACP, diagnosi energetica "
                     "ante, incentivo efficienza energetica"},
        {"kind": "procedure", "section": "operations", "name": "Calcolo parcella",
         "body": "1 importi lavori per categoria (da QE o stima)\n2 categoria e G dalle tavole, se edificio "
                 "vecchio verificare vincolo (decreto o verifica interesse culturale) prima di usare E.22\n"
                 "3 Q per fase con I.13\n4 P per categoria\n5 spese %\n6 controllo di un secondo\n7 ribasso "
                 "solo dopo ok partner",
         "keywords": "procedura calcolo parcella, categoria e grado di complessità G, verifica vincolo / "
                     "interesse culturale, E.22 edifici vincolati, aliquote Q / All. I.13, spese percentuali, "
                     "controllo di un secondo, ribasso dopo ok partner, onorario / preventivo"},
        {"kind": "procedure", "section": "offer", "name": "Partecipazione gara SIA",
         "keywords": "gara, RTP, DGUE, partecipazione gara SIA, scouting gare / TED / albo pretorio, go / no "
                     "go, requisiti fatturato e servizi analoghi, RTP / raggruppamento temporaneo, giovane "
                     "professionista, DGUE / documento di gara unico europeo, PassOE, firma digitale file, "
                     "carico 48 ore prima",
         "body": "scouting (piattaforme + TED + albo pretorio) -> go/no go partner entro 3 gg -> requisiti "
                 "(fatturato, servizi analoghi per categoria, giovane professionista se RTP) -> RTP con atto "
                 "di impegno -> parcella -> relazione metodologica / oGI -> DGUE e dichiarazioni -> PassOE -> "
                 "firma digitale TUTTI i file -> carico 48h prima"},
        {"kind": "procedure", "section": "operations", "name": "Apertura cantiere come CSE",
         "body": "verifica idoneità tecnico-professionale imprese (fatta dal committente, noi controlliamo)\n"
                 "notifica preliminare art. 99 (ASL + Ispettorato) se più imprese o >= 200 uomini-giorno, PRIMA "
                 "dei lavori, copia in cantiere\nPSC consegnato, POS di ogni impresa verificati e accettati\n"
                 "riunione di coordinamento con verbale\nsolo dopo: verbale consegna lavori del DL",
         "keywords": "apertura cantiere CSE, CSE / coordinatore sicurezza in esecuzione, idoneità "
                     "tecnico-professionale imprese, notifica preliminare art. 99, ASL / Ispettorato del "
                     "lavoro, 200 uomini-giorno, PSC / piano di sicurezza e coordinamento, POS / piano "
                     "operativo di sicurezza, riunione di coordinamento, verbale consegna lavori"},
        {"kind": "fact", "section": "operations", "name": "Documenti standard per gare",
         "body": "Cartella GARE/standard: atto costitutivo studio, CV studio e singoli, iscrizioni albo, polizza RC, "
                 "DURC/Inarcassa regolarità, elenco servizi per categoria ID, fatturato ultimi 3 anni. Rita la "
                 "aggiorna ogni trimestre. Regolarità Inarcassa: scade, controllare prima di ogni gara.",
         "keywords": "documenti standard gare, cartella GARE/standard, atto costitutivo studio, curriculum / CV "
                     "studio, iscrizione albo, polizza RC, DURC / regolarità Inarcassa, elenco servizi per "
                     "categoria ID, fatturato ultimi 3 anni, aggiornamento trimestrale"},
    ],
    "home_tasks": [
        {"name": "Rinnovo polizza RC professionale", "who": "office", "stage": "Fatto",
         "description": "scad. 30/4",
         "notes": [("office", 190, "rinnovata, quietanza in GARE/standard"),
                   ("lead", 188, "ok, massimale invariato"),
                   ("office", 187, "Sintomo: la polizza professionale dello studio scadeva il 30/4 e senza di "
                    "essa non si partecipa alle gare né si firmano incarichi. Causa / contesto: polizza RC "
                    "professionale (responsabilità civile professionale) dello studio con massimale 2,5 "
                    "milioni; copia e quietanza vanno nella cartella documenti standard per le gare; la polizza "
                    "del progettista per la verifica degli esecutivi è separata, per commessa. Intervento e "
                    "stato: polizza rinnovata con massimale invariato, quietanza archiviata in GARE/standard. "
                    "Fatto.",
                    ["polizza RC professionale", "responsabilità civile professionale", "assicurazione studio",
                     "rinnovo 30/4", "quietanza", "massimale", "documenti standard gare"])]},
        {"name": "Fatturato 2025 per requisiti gare", "who": "office", "stage": "Fatto",
         "description": "tabella fatturato SIA ultimi 3 anni per categoria",
         "notes": [("office", 160, "fatto, foglio in GARE/standard. 2025: 612k di cui SIA 540k"),
                   ("office", 159, "Sintomo: per i requisiti di partecipazione alle gare serve il fatturato "
                    "dello studio degli ultimi tre anni, diviso per categoria. Causa / contesto: tabella del "
                    "fatturato SIA (servizi di ingegneria e architettura) per categoria, usata per i requisiti "
                    "economico-finanziari e conservata nella cartella documenti standard per le gare. "
                    "Intervento e stato: foglio pronto in GARE/standard; nel 2025 fatturato totale di 612 mila "
                    "euro, di cui 540 mila da servizi SIA. Fatto.",
                    ["fatturato SIA", "requisiti economico-finanziari", "fatturato ultimi 3 anni",
                     "requisiti gare", "servizi di ingegneria e architettura", "documenti standard gare"])]},
        {"name": "Nuovo server / backup ACDat", "who": "bim", "stage": "In corso",
         "description": "NAS saturo. valutare cloud",
         "notes": [("bim", 40, "NAS al 92%. preventivo cloud 2 TB chiesto"),
                   ("partner", 33, "ok cloud ma con copia locale notturna"),
                   ("bim", 32, "Sintomo: lo spazio di archiviazione dello studio è quasi pieno e servono backup "
                    "affidabili dei progetti e dei modelli. Causa / contesto: il NAS (server di rete locale) "
                    "che ospita l'ACDat (ambiente di condivisione dati) è al 92%; valutata la migrazione "
                    "dell'archivio su cloud. Intervento e stato: chiesto un preventivo per uno spazio cloud da "
                    "2 TB; deciso di passare al cloud mantenendo una copia locale notturna come backup. In "
                    "corso.",
                    ["NAS saturo", "server", "backup", "cloud 2 TB", "copia locale notturna",
                     "ACDat / ambiente di condivisione dati", "archiviazione"])]},
        {"name": "Licenze software 2027", "who": "bim", "stage": "Da fare", "deadline": 45,
         "description": "rinnovi a dicembre. 3 BIM authoring, 1 MEP, viewer gratuiti ok",
         "notes": [("bim", 1, "Sintomo: a dicembre scadono le licenze dei programmi di progettazione dello "
                    "studio e vanno rinnovate per il 2027. Causa / contesto: rinnovo di 3 licenze di software "
                    "BIM authoring (modellazione) e 1 licenza MEP per gli impianti; per la consultazione e il "
                    "controllo dei modelli IFC bastano i viewer gratuiti. Intervento e stato: rinnovi da "
                    "programmare a dicembre. Da fare.",
                    ["licenze software", "rinnovo licenze 2027", "BIM authoring", "software MEP / impianti",
                     "viewer gratuiti", "abbonamenti"])]},
        {"name": "Regolarità Inarcassa soci", "who": "office", "stage": "In corso",
         "description": "certificati regolarità contributiva per gare",
         "notes": [("office", 12, "Lorenzo ha la regolarità scaduta, chiesta rinnovo"),
                   ("office", 11, "Sintomo: per partecipare alle gare servono i certificati di regolarità "
                    "contributiva dei soci e uno risulta scaduto. Causa / contesto: certificato di regolarità "
                    "contributiva Inarcassa (cassa di previdenza di ingegneri e architetti), l'equivalente del "
                    "DURC per i liberi professionisti, conservato nei documenti standard per le gare; scade e "
                    "va controllato prima di ogni gara. Intervento e stato: chiesto il rinnovo del certificato "
                    "scaduto. In corso.",
                    ["regolarità Inarcassa", "certificato regolarità contributiva",
                     "cassa previdenza ingegneri architetti", "DURC professionisti", "requisiti gare",
                     "documenti standard gare"])]},
        {"name": "Sito: pagina servizi Industria 5.0", "who": "arch", "stage": "Annullato",
         "description": "rimandato, la misura è cambiata",
         "notes": [("arch", 1, "Sintomo: lo studio voleva una pagina del proprio sito web per presentare i "
                    "servizi di supporto alle imprese per Industria 5.0 (perizie e certificazioni). Causa / "
                    "contesto: la misura di incentivo Transizione 5.0, il credito d'imposta per investimenti "
                    "con risparmio energetico, è cambiata e i contenuti della pagina sarebbero stati da rifare. "
                    "Intervento e stato: pagina rimandata, task annullato. Annullato.",
                    ["sito web", "pagina servizi", "Industria 5.0", "Transizione 5.0", "credito d'imposta",
                     "marketing studio"])]},
    ],
}

URL_TED = "https://ted.europa.eu/it/notice/-/detail/418556-2026"
URL_SAFFI = "https://www.regione.umbria.it/la-regione/bandi-di-gara?gara=progettazione-sede-terni-via-saffi"

ORGANISATION["projects"] = [
    {"name": P_GARE, "tags": ["gare", "SIA"], "stages": GARE_STAGES,
     "description": "<p>Partecipazione a gare SIA e affidamenti: scouting, go/no go, requisiti, RTP, offerta "
                    "tecnica ed economica. Obiettivo 2026: 6 gare, almeno 2 aggiudicate.</p>",
     "milestones": [("Primo semestre: 3 gare", -125, 130), ("Secondo semestre: 3 gare", 60, None)],
     "tasks": [
         {"name": "Ancona uffici giudiziari BIM (TED 418556)", "who": "lead", "stage": "Chiusa",
          "milestone": "Primo semestre: 3 gare",
          "description": "PFTE+CSP+DL+CSE+DO in BIM, 4,1 mln stimati. scad 20/7. RTP?",
          "notes": [("junior", 135, "trovata su TED. OEPV, criteri A-E, c'è anche architetto di chiara fama + "
                                    "esperienza post sisma 2016"),
                    ("lead", 133, "no go. requisiti servizi analoghi post sisma non li abbiamo, RTP con "
                                  "mandataria marchigiana ci metterebbe al 15%. non conviene"),
                    ("junior", 132, "archiviata, tenuto il disciplinare come modello oGI"),
                    ("lead", 131, "Sintomo: lo studio valuta se partecipare alla gara europea per la "
                     "riqualificazione degli uffici giudiziari di Ancona, servizi di progettazione, sicurezza e "
                     "direzione lavori in BIM, circa 4,1 milioni stimati, scadenza 20/7. Causa / contesto: "
                     "bando trovato su TED (Tenders Electronic Daily), procedura aperta con OEPV (offerta "
                     "economicamente più vantaggiosa) e criteri A-E; prestazioni PFTE (progetto di fattibilità "
                     "tecnica ed economica), CSP, DL, CSE, DO; richiesti architetto di chiara fama ed "
                     "esperienza post sisma 2016. Intervento e stato: decisione no go, mancano i servizi "
                     "analoghi post sisma e in RTP (raggruppamento temporaneo di professionisti) con mandataria "
                     "marchigiana la quota sarebbe al 15%. Chiusa; disciplinare conservato come modello per "
                     "l'oGI (offerta di gestione informativa).",
                     ["TED 418556", "gara europea", "uffici giudiziari Ancona", "no go",
                      "servizi analoghi post sisma", "architetto di chiara fama",
                      "OEPV / offerta economicamente più vantaggiosa", "RTP / raggruppamento temporaneo",
                      "oGI / offerta di gestione informativa"])]},
         {"name": "Gara palestra Narni - RTP con Studio Ferri", "who": "partner", "stage": "Chiusa",
          "milestone": "Primo semestre: 3 gare",
          "description": "procedura negoziata, esecutivo + CSP. noi mandanti impianti",
          "notes": [("partner", 170, "RTP 60/40, mandataria Ferri. giovane professionista: Elena"),
                    ("office", 151, "ESCLUSI. manca l'atto di impegno a costituire RTP firmato dalla mandante "
                                    "(noi!). soccorso istruttorio NON concesso perché lo consideravano parte "
                                    "dell'offerta. file caricato era la bozza non firmata"),
                    ("lead", 150, "brutto. d'ora in poi controllo incrociato firme su TUTTI i file prima del "
                                  "carico, checklist gare aggiornata"),
                    ("partner", 120, "ricorso sconsigliato dall'avvocato, lasciamo"),
                    ("partner", 119, "Sintomo: lo studio, mandante per gli impianti in un raggruppamento con "
                     "uno studio capofila, viene escluso dalla gara per la palestra di Narni (esecutivo e "
                     "coordinamento sicurezza in progettazione). Causa / contesto: procedura negoziata, RTP "
                     "(raggruppamento temporaneo di professionisti) 60/40 con giovane professionista; l'atto di "
                     "impegno a costituire l'RTP caricato era la bozza non firmata dalla mandante; il soccorso "
                     "istruttorio non è stato concesso perché il documento era considerato parte dell'offerta. "
                     "Intervento e stato: ricorso sconsigliato dal legale, si lascia; introdotto il controllo "
                     "incrociato delle firme digitali su tutti i file prima del caricamento e aggiornata la "
                     "checklist gare. Chiusa.",
                     ["esclusione gara", "atto di impegno RTP", "firma digitale mancante",
                      "soccorso istruttorio negato", "mandante / mandataria",
                      "RTP / raggruppamento temporaneo di professionisti", "palestra Narni",
                      "procedura negoziata", "checklist gare"])]},
         {"name": "Accordo quadro manutenzioni ASL - verifica requisiti", "who": "junior", "stage": "Chiusa",
          "description": "AQ 4 anni verifiche sismiche edifici sanitari",
          "notes": [("junior", 140, "requisito fatturato specifico 3x base gara, noi non ci arriviamo"),
                    ("lead", 139, "no go"),
                    ("junior", 138, "Sintomo: lo studio valuta l'accordo quadro dell'ASL per le verifiche "
                     "sismiche degli edifici sanitari, durata 4 anni. Causa / contesto: AQ (accordo quadro) di "
                     "manutenzione con requisito di fatturato specifico pari a 3 volte la base di gara; il "
                     "fatturato SIA (servizi di ingegneria e architettura) dello studio non raggiunge la "
                     "soglia. Intervento e stato: decisione no go, non si partecipa. Chiusa.",
                     ["AQ / accordo quadro", "ASL / azienda sanitaria", "verifiche sismiche edifici sanitari",
                      "vulnerabilità sismica ospedali", "requisito fatturato specifico",
                      "requisiti di partecipazione", "no go", "base di gara"])]},
         {"name": "Scuola Valfonda - affidamento diretto", "who": "lead", "stage": "Chiusa",
          "milestone": "Primo semestre: 3 gare",
          "description": "vedi commessa Comune di Valfonda. preventivo su richiesta RUP",
          "notes": [("lead", 128, "inviato preventivo con ribasso 8% sul DM. aggiudicato a maggio"),
                    ("lead", 127, "Sintomo: il RUP del Comune di Valfonda chiede allo studio un preventivo per "
                     "la progettazione della scuola media, senza gara. Causa / contesto: affidamento diretto "
                     "sotto soglia (SIA sotto 140 mila euro, art. 50 D.Lgs. 36/2023), collegato alla commessa "
                     "del Comune di Valfonda; il preventivo parte dal calcolo del DM 17/06/2016 (decreto "
                     "parametri) e negli affidamenti diretti il ribasso massimo è del 20%. Intervento e stato: "
                     "inviato preventivo con ribasso dell'8% sull'importo del DM; incarico aggiudicato a "
                     "maggio. Chiusa.",
                     ["affidamento diretto", "preventivo", "RUP / responsabile unico del progetto", "ribasso 8%",
                      "DM 17/06/2016 / decreto parametri", "scuola Valfonda", "sotto soglia", "aggiudicazione"])]},
         {"name": "Gara SIA Comune di Amelia - riqualificazione biblioteca", "who": "arch", "stage": "Inviata",
          "milestone": "Secondo semestre: 3 gare",
          "description": "OEPV, PFTE+esecutivo, E.22 (edificio vincolato), 182k base",
          "notes": [("arch", 44, "letto disciplinare: è già sul bando tipo 2/2026? no, sotto soglia, ma lo "
                                 "ricalcano. offerta tecnica max 30 facciate A4"),
                    ("lead", 40, "ribasso: equo compenso, ribasso solo sul 35%. offro 12% sulla quota "
                                 "ribassabile"),
                    ("arch", 21, "caricata giov, PassOE ok, firme controllate due volte"),
                    ("arch", 20, "Sintomo: lo studio partecipa alla gara del Comune di Amelia per la "
                     "riqualificazione della biblioteca, edificio vincolato, base 182 mila euro. Causa / "
                     "contesto: OEPV (offerta economicamente più vantaggiosa), PFTE ed esecutivo, categoria "
                     "E.22 (edifici tutelati); procedura sotto soglia che ricalca il bando tipo ANAC 2/2026; "
                     "offerta tecnica massimo 30 facciate A4; equo compenso: ribasso solo sul 35% del "
                     "corrispettivo. Intervento e stato: preparate relazione metodologica e servizi analoghi, "
                     "offerto 12% sulla quota ribassabile, PassOE ok, firme controllate due volte; offerta "
                     "caricata. Inviata.",
                     ["gara Amelia biblioteca", "OEPV / offerta economicamente più vantaggiosa",
                      "E.22 / edificio vincolato", "equo compenso", "quota ribassabile 35%",
                      "relazione metodologica / offerta tecnica", "PassOE", "bando tipo ANAC 2/2026"])],
          "worklog": [("arch", 30, 6.0, "relazione metodologica"), ("junior", 28, 4.0, "servizi analoghi")]},
         {"name": "Gara SIA Provincia - adeguamento sismico liceo", "who": "lead", "stage": "In preparazione",
          "milestone": "Secondo semestre: 3 gare", "deadline": 18,
          "description": "procedura aperta, sopra soglia UE -> bando tipo 2/2026 vincolante. BIM: si, >2 mln",
          "notes": [("lead", 14, "lavori 3,4 mln, BIM obbligatorio. CI della Provincia 22 pagine, oGI max 15 "
                                 "facciate"),
                    ("bim", 9, "oGI bozza su modello studio. da rivedere par. 4 (ACDat: loro chiedono il "
                               "loro, noi proponevamo il nostro) e par. 6 LOIN"),
                    ("lead", 3, "par. 4 ok usiamo ACDat della SA. RTP con geologo per relazione geologica"),
                    ("lead", 2, "Sintomo: lo studio prepara l'offerta per la gara della Provincia "
                     "sull'adeguamento sismico di un liceo. Causa / contesto: procedura aperta sopra soglia UE, "
                     "quindi bando tipo ANAC 2/2026 vincolante; lavori 3,4 milioni, BIM obbligatorio oltre 2 "
                     "milioni; CI (capitolato informativo) della Provincia di 22 pagine, oGI (offerta di "
                     "gestione informativa) massimo 15 facciate. Bozza oGI da rivedere al paragrafo 4 ACDat "
                     "(ambiente di condivisione dati, CDE) e al paragrafo 6 LOIN (livello di fabbisogno "
                     "informativo). Intervento e stato: si usa l'ACDat della stazione appaltante; RTP con "
                     "geologo per la relazione geologica. In preparazione.",
                     ["adeguamento sismico liceo", "gara Provincia sopra soglia", "bando tipo ANAC 2/2026",
                      "BIM obbligatorio", "oGI / offerta di gestione informativa", "CI / capitolato informativo",
                      "ACDat / CDE / ambiente di condivisione dati", "LOIN / livello di fabbisogno informativo",
                      "relazione geologica"])]},
         {"name": "Scouting dicembre (piattaforme Umbria)", "who": "junior", "stage": "Scouting",
          "description": "Portale Acquisti Umbria + MePA + albi. scadenze dic",
          "notes": [("junior", 4, "2 interessanti: verifica vulnerabilità scuole Orvieto (scad 12/12), DL "
                                  "rotatoria Spoleto (scad 5/12, solo strade, no)"),
                    ("junior", 3, "Sintomo: lo studio cerca nuove gare di progettazione con scadenza a dicembre "
                     "sulle piattaforme dell'Umbria. Causa / contesto: scouting periodico su Portale Acquisti "
                     "Umbria, MePA (mercato elettronico della pubblica amministrazione) e albi, primo passo "
                     "della procedura di partecipazione alle gare SIA prima del go/no go dei partner. "
                     "Intervento e stato: individuate due opportunità: verifica di vulnerabilità sismica delle "
                     "scuole di Orvieto (scadenza 12/12) e direzione lavori di una rotatoria a Spoleto "
                     "(scadenza 5/12), scartata perché riguarda solo strade. In scouting.",
                     ["scouting gare", "Portale Acquisti Umbria", "MePA / mercato elettronico",
                      "vulnerabilità sismica scuole Orvieto", "DL rotatoria Spoleto", "scadenze dicembre",
                      "albi fornitori"])]},
         {"name": "Iscrizione elenco regionale professionisti - aggiornamento", "who": "office", "stage": "Chiusa",
          "description": "aggiornare servizi e categorie sul portale",
          "notes": [("office", 210, "aggiornato con i servizi 2025. attenzione la DD 618 che gira è l'elenco "
                                    "imprese, il nostro è l'elenco professionisti (art. 21 LR 3/2010)"),
                    ("office", 209, "Sintomo: vanno aggiornati i servizi svolti e le categorie dello studio sul "
                     "portale dell'elenco regionale, da cui i Comuni scelgono a chi chiedere preventivi. Causa "
                     "/ contesto: elenco regionale dei professionisti (art. 21 L.R. 3/2010) usato dalle "
                     "stazioni appaltanti umbre per affidamenti diretti e procedure negoziate; la D.D. 618/2026 "
                     "che circola riguarda invece l'elenco delle imprese per i lavori pubblici, non quello dei "
                     "professionisti. Intervento e stato: iscrizione aggiornata con i servizi 2025. Chiusa.",
                     ["elenco regionale professionisti", "albo professionisti Umbria", "L.R. 3/2010 art. 21",
                      "DD 618/2026", "elenco imprese", "categorie e servizi SIA", "Portale Acquisti Umbria"])]},
         {"name": "Calcolo parcella tipo E.20/S.03 - foglio studio", "who": "junior", "stage": "Chiusa",
          "description": "rifare foglio parcella con I.13 (due livelli)",
          "notes": [("junior", 180, "foglio rifatto. testato su capitolato Regione sede Terni via Saffi "
                                    "(vecchio codice, buono per il calcolo): torna"),
                    ("partner", 178, "ok. aggiungere colonna QbII.05 spostabile"),
                    ("junior", 177, "Sintomo: serve un foglio di calcolo della parcella aggiornato per i lavori "
                     "E.20/S.03. Causa / contesto: calcolo corrispettivi con DM 17/06/2016 (decreto parametri) "
                     "e All. I.13 del D.Lgs. 36/2023 sui due livelli di progettazione; E.20 edilizia su "
                     "esistente, S.03 strutture. Intervento e stato: foglio rifatto e testato sul capitolato "
                     "della Regione per la sede di Terni via Saffi (vecchio codice, valido per il calcolo): i "
                     "risultati tornano. Da aggiungere una colonna per QbII.05 (elenco prezzi, computo, quadro "
                     "economico) spostabile. Chiusa.",
                     ["foglio parcella", "calcolo corrispettivo / onorario", "DM 17/06/2016 / decreto parametri",
                      "All. I.13", "E.20", "S.03", "QbII.05", "due livelli di progettazione"])]},
     ],
     "updates": [
         ("Bilancio primo semestre", "at_risk", 50, 125,
          "3 gare: 1 aggiudicata (Valfonda, diretto), 1 esclusa (Narni, atto impegno RTP non firmato), 1 no go "
          "(Ancona). checklist firme rifatta."),
         ("Ottobre", "on_track", 65, 6,
          "Amelia inviata, Provincia liceo in prep (oGI rev par. 4 e 6), scouting dicembre in corso."),
     ]},
    {"name": P_BIMSTD, "tags": ["BIM", "standard"],
     "description": "<p>Standard BIM dello studio: linee guida, template, ACDat, oGI/pGI tipo, clash detection.</p>",
     "milestones": [("Linee guida rev. 2026", -150, 148), ("Template pGI", 30, None)],
     "tasks": [
         {"name": "Linee guida BIM rev. 2026", "who": "bim", "stage": "Fatto", "milestone": "Linee guida rev. 2026",
          "description": "aggiornare a I.9 post correttivo + UNI 11337",
          "notes": [("bim", 160, "rev pronta. aggiunto par. formati: IFC 4 di default"),
                    ("lead", 148, "approvata"),
                    ("bim", 147, "Sintomo: le linee guida BIM interne dello studio vanno aggiornate alle nuove "
                     "regole sui formati e sui ruoli. Causa / contesto: allineamento all'All. I.9 del D.Lgs. "
                     "36/2023 dopo il correttivo e alla norma UNI 11337 sulla gestione informativa digitale; le "
                     "linee guida coprono ruoli, codifica, ACDat (ambiente di condivisione dati), LOIN, formati "
                     "e clash detection. Intervento e stato: revisione 2026 pronta, aggiunto il paragrafo sui "
                     "formati con IFC 4 (formato aperto, interoperabile) come formato di consegna di default; "
                     "revisione approvata. Fatto.",
                     ["linee guida BIM", "standard BIM studio", "All. I.9", "UNI 11337",
                      "IFC 4 / formato aperto", "gestione informativa digitale", "correttivo D.Lgs. 209/2024"])]},
         {"name": "Template pGI", "who": "bim", "stage": "In corso", "milestone": "Template pGI", "deadline": 30,
          "description": "dal pGI ATER fare un template riusabile",
          "notes": [("bim", 20, "struttura ok. manca matrice responsabilità e tabella LOIN per fase"),
                    ("bim", 19, "Sintomo: lo studio vuole un modello riutilizzabile di piano BIM da adattare a "
                     "ogni commessa pubblica, senza ripartire da zero. Causa / contesto: il pGI (piano di "
                     "gestione informativa) redatto per l'ATER sul suo capitolato informativo è preso come base "
                     "per un template; il pGI è il documento dell'aggiudicatario che risponde al CI della "
                     "stazione appaltante. Intervento e stato: struttura del template pronta; mancano ancora la "
                     "matrice delle responsabilità e la tabella LOIN (livello di fabbisogno informativo) per "
                     "fase. In corso.",
                     ["pGI / piano di gestione informativa", "piano BIM", "template", "matrice responsabilità",
                      "LOIN / livello di fabbisogno informativo", "BIM execution plan", "ATER"])]},
         {"name": "Test export IFC impianti", "who": "bim", "stage": "Fatto",
          "description": "IFC MEP perde i sistemi?",
          "notes": [("bim", 95, "export IFC4 RV: sistemi persi su canali flessibili. con mapping custom ok. "
                                "mapping salvato in template"),
                    ("bim", 94, "Sintomo: il modello degli impianti esportato in IFC sembra perdere i sistemi, "
                     "e la consegna in formato aperto rischia di essere incompleta. Causa / contesto: export "
                     "IFC4 Reference View del modello MEP (impianti meccanici ed elettrici) dal software di "
                     "authoring: i sistemi impiantistici si perdono sui canali flessibili. Intervento e stato: "
                     "test eseguito; con una mappatura personalizzata delle classi l'export conserva i sistemi; "
                     "il mapping è stato salvato nel template di progetto per le commesse successive. Fatto.",
                     ["export IFC", "IFC4 Reference View", "MEP / modello impianti", "sistemi persi",
                      "canali flessibili", "mapping personalizzato", "interoperabilità"])]},
         {"name": "Regole clash detection standard", "who": "bim", "stage": "Fatto",
          "description": "set regole STR/MEC/ELE",
          "notes": [("bim", 80, "hard 10mm, soft 50mm. regola extra: travi vs canali > 300mm"),
                    ("bim", 79, "Sintomo: serve un set standard di regole per il controllo delle interferenze "
                     "tra le discipline, per non perdere tempo tra centinaia di falsi conflitti. Causa / "
                     "contesto: clash detection (controllo interferenze) tra strutture, impianti meccanici ed "
                     "elettrici (STR/MEC/ELE) sul modello federato, eseguita ogni settimana secondo le linee "
                     "guida BIM. Intervento e stato: definite le regole: hard clash con tolleranza 10 mm, soft "
                     "clash (spazi di manutenzione) 50 mm, regola aggiuntiva travi contro canali oltre 300 mm. "
                     "Fatto.",
                     ["clash detection / controllo interferenze", "hard clash", "soft clash", "tolleranze",
                      "travi contro canali", "modello federato", "STR / MEC / ELE"])]},
         {"name": "Corso ACDat per Elena", "who": "bim", "stage": "Fatto",
          "description": "",
          "notes": [("junior", 70, "fatto. sostituta CDE manager"),
                    ("bim", 69, "Sintomo: una collaboratrice junior deve poter sostituire il responsabile "
                     "dell'ambiente di condivisione dati quando è assente. Causa / contesto: formazione "
                     "sull'ACDat (ambiente di condivisione dati, in inglese CDE) dello studio, con stati WIP, "
                     "SHARED, PUBLISHED e ARCHIVED, e sul ruolo di CDE manager previsto da UNI 11337-7 e dalle "
                     "linee guida BIM. Intervento e stato: corso completato; la junior è ora indicata come "
                     "sostituta del CDE manager. Fatto.",
                     ["ACDat / ambiente di condivisione dati", "CDE manager", "corso formazione", "sostituto",
                      "UNI 11337-7", "gestore ACDat"])]},
         {"name": "Valutare certificazione UNI 11337-7 Matteo", "who": "lead", "stage": "Da fare",
          "description": "BIM coordinator certificato: punti in oGI nelle gare grandi",
          "notes": [("lead", 1, "Sintomo: nelle gare di progettazione più grandi l'offerta BIM prende punti se "
                     "lo studio ha un BIM coordinator certificato. Causa / contesto: certificazione delle "
                     "figure professionali BIM secondo UNI 11337-7; i ruoli certificati danno punteggio "
                     "nell'oGI (offerta di gestione informativa), e le linee guida dello studio vietano di "
                     "promettere in oGI ruoli certificati che non si hanno. Intervento e stato: da valutare la "
                     "certificazione del BIM coordinator dello studio. Da fare.",
                     ["certificazione UNI 11337-7", "BIM coordinator certificato", "figure BIM", "punteggio oGI",
                      "offerta di gestione informativa", "qualifica professionale"])]},
     ],
     "updates": [
         ("Stato standard", "on_track", 70, 15, "linee guida ok, template pGI al 60%, certificazione da decidere."),
     ]},
    {"name": P_CFP, "tags": ["formazione", "CFP"],
     "description": "<p>Formazione continua: CFP di ingegneri e architetti, corsi interni, aggiornamento CSP/CSE.</p>",
     "milestones": [("Riepilogo crediti", 45, None)],
     "tasks": [
         {"name": "Aggiornamento 40h coordinatori sicurezza", "who": "lead", "stage": "In corso",
          "description": "quinquennio scade 2027 per Andrea, 2026 per Lorenzo!",
          "notes": [("partner", 50, "mi mancano 16h, scade a dicembre. iscritto al corso ordine nov"),
                    ("lead", 10, "Lorenzo: senza aggiornamento non puoi fare CSE su Meccanica Nera da gennaio"),
                    ("lead", 9, "Sintomo: i coordinatori della sicurezza dello studio rischiano di non poter "
                     "più fare il CSE per scadenza dell'aggiornamento. Causa / contesto: aggiornamento "
                     "obbligatorio di 40 ore ogni 5 anni per CSP/CSE (coordinatore sicurezza in progettazione / "
                     "in esecuzione); un quinquennio scade nel 2026, l'altro nel 2027. Mancano 16 ore con "
                     "scadenza a dicembre. Intervento e stato: iscrizione al corso dell'ordine di novembre; "
                     "senza aggiornamento niente CSE sul cantiere Meccanica Nera da gennaio. In corso.",
                     ["aggiornamento 40 ore", "quinquennio", "coordinatore sicurezza",
                      "CSE / coordinatore sicurezza in esecuzione",
                      "CSP / coordinatore sicurezza in progettazione", "D.Lgs. 81/2008",
                      "corso ordine ingegneri", "abilitazione"])]},
         {"name": "Seminario nuovi CAM", "who": "arch", "stage": "Fatto",
          "description": "3 CFP. ordine architetti",
          "notes": [("arch", 200, "fatto. attestato in cartella"),
                    ("arch", 199, "Sintomo: i progettisti devono aggiornarsi sui nuovi criteri ambientali "
                     "minimi, obbligatori nei progetti pubblici da febbraio 2026, e maturare crediti formativi. "
                     "Causa / contesto: seminario dell'ordine degli architetti sui nuovi CAM (criteri "
                     "ambientali minimi) edilizia del DM 24/11/2025, valido per 3 CFP (crediti formativi "
                     "professionali). Intervento e stato: seminario seguito; attestato archiviato nella "
                     "cartella CFP come prevede la regola di registrazione dei crediti entro il mese. Fatto.",
                     ["seminario CAM", "criteri ambientali minimi", "CFP / crediti formativi professionali",
                      "ordine architetti", "attestato", "formazione continua"])]},
         {"name": "Corso Conto Termico 3.0 GSE", "who": "partner", "stage": "Fatto",
          "description": "webinar GSE",
          "notes": [("partner", 230, "fatto. non dà CFP, solo attestato"),
                    ("partner", 229, "Sintomo: lo studio deve conoscere il nuovo incentivo statale per "
                     "efficienza energetica e rinnovabili termiche, usato per le case popolari. Causa / "
                     "contesto: webinar del GSE (Gestore dei servizi energetici) sul Conto Termico 3.0 (DM "
                     "7/8/2025), con accesso diretto o a prenotazione e diagnosi energetica. Intervento e "
                     "stato: corso seguito; non riconosce CFP (crediti formativi professionali), rilascia solo "
                     "un attestato di partecipazione. Fatto.",
                     ["Conto Termico 3.0", "GSE / Gestore servizi energetici", "webinar", "attestato senza CFP",
                      "incentivi efficienza energetica", "formazione"])]},
         {"name": "Riepilogo crediti 2026", "who": "office", "stage": "Da fare", "milestone": "Riepilogo crediti",
          "deadline": 45, "description": "foglio crediti per tutti",
          "notes": [("office", 1, "Sintomo: serve un quadro unico dei crediti formativi di tutto lo studio, per "
                     "non scoprire tardi chi non è in regola. Causa / contesto: foglio crediti con CFP (crediti "
                     "formativi professionali) di ingegneri (minimo 30, 5 di deontologia) e architetti (60 nel "
                     "triennio), più le scadenze dell'aggiornamento quinquennale di 40 ore dei coordinatori "
                     "della sicurezza. Intervento e stato: riepilogo 2026 da preparare per tutti i "
                     "professionisti dello studio. Da fare.",
                     ["riepilogo crediti", "foglio crediti", "CFP / crediti formativi professionali",
                      "formazione continua", "obbligo formativo", "scadenze aggiornamento"])]},
         {"name": "Crediti deontologia", "who": "junior", "stage": "In corso",
          "description": "obbligatori 5 cfp deontologici",
          "notes": [("junior", 25, "ne ho 2, corso online a novembre"),
                    ("junior", 24, "Sintomo: un ingegnere dello studio deve completare i crediti obbligatori di "
                     "etica professionale per poter continuare a esercitare in regola. Causa / contesto: "
                     "obbligo di 5 CFP (crediti formativi professionali) su etica e deontologia per gli "
                     "ingegneri, dentro il saldo minimo di 30 CFP; al momento ne risultano solo 2. Intervento e "
                     "stato: iscrizione a un corso online di deontologia previsto a novembre; attestato e riga "
                     "nel foglio crediti da registrare entro il mese. In corso.",
                     ["crediti deontologia", "CFP deontologici", "etica professionale",
                      "obbligo formativo ingegneri", "corso online", "formazione continua"])]},
     ],
     "updates": [
         ("Ottobre", "at_risk", 60, 10, "Lorenzo aggiornamento CSE scade a dicembre (16h mancanti)."),
     ]},
    {"name": P_QUALITA, "tags": ["qualità"],
     "description": "<p>Sistema qualità interno: procedure, checklist, audit, non conformità.</p>",
     "milestones": [("Riesame annuale", 55, None)],
     "tasks": [
         {"name": "NC 2026-03 esclusione gara per firma mancante", "who": "lead", "stage": "Fatto",
          "description": "non conformità dopo Narni",
          "notes": [("lead", 148, "azione correttiva: checklist gare punto 9 firme incrociate, due persone"),
                    ("lead", 147, "Sintomo: dopo l'esclusione dalla gara per una firma mancante serve evitare "
                     "che si ripeta. Causa / contesto: NC (non conformità) 2026-03 del sistema qualità, nata "
                     "dall'esclusione nella gara della palestra di Narni per l'atto di impegno RTP non firmato. "
                     "Intervento e stato: azione correttiva: punto 9 della checklist gare con controllo "
                     "incrociato delle firme da parte di due persone. Fatto.",
                     ["NC / non conformità", "azione correttiva", "esclusione gara", "firma digitale mancante",
                      "firme incrociate", "checklist gare", "sistema qualità"])]},
         {"name": "NC 2026-05 IFC rifiutato da ATER", "who": "bim", "stage": "Fatto",
          "description": "",
          "notes": [("bim", 100, "azione: export e verifica IFC in viewer indipendente prima dell'upload. in "
                                 "checklist emissione rev 4"),
                    ("bim", 99, "Sintomo: il gestore dell'ambiente di condivisione dati dell'ATER ha rifiutato "
                     "una consegna perché non era in IFC. Causa / contesto: NC (non conformità) 2026-05 del "
                     "sistema qualità: caricato il modello nativo del software di authoring invece dell'IFC "
                     "richiesto dal capitolato informativo. Intervento e stato: azione correttiva: export "
                     "dell'IFC e sua verifica in un viewer indipendente prima di ogni upload, inserita nella "
                     "checklist emissione elaborati rev. 4. Fatto.",
                     ["NC / non conformità", "IFC rifiutato", "consegna respinta ATER", "modello nativo",
                      "viewer indipendente", "checklist emissione", "azione correttiva"])]},
         {"name": "Checklist emissione elaborati rev 4", "who": "bim", "stage": "Fatto",
          "description": "", "notes": [("bim", 98, "pubblicata in cloud/procedure"),
                                       ("bim", 97, "Sintomo: serve una nuova lista di controllo prima di "
                                        "emettere tavole e modelli, per evitare consegne respinte. Causa / "
                                        "contesto: checklist emissione elaborati rev. 4, aggiornata dopo la non "
                                        "conformità sull'IFC rifiutato: codifica dei file, cartiglio, IFC "
                                        "verificato in viewer indipendente, firma digitale PAdES, trasmissione "
                                        "e copia in PUBLISHED sull'ACDat (ambiente di condivisione dati). "
                                        "Intervento e stato: checklist pubblicata nella cartella procedure del "
                                        "cloud dello studio. Fatto.",
                                        ["checklist emissione elaborati", "rev. 4", "controllo emissione tavole",
                                         "IFC verificato", "firma PAdES", "procedure interne", "sistema qualità"])]},
         {"name": "Riesame annuale", "who": "lead", "stage": "Da fare", "milestone": "Riesame annuale",
          "deadline": 55, "description": "NC, gare, reclami, formazione",
          "notes": [("lead", 1, "Sintomo: lo studio deve fare il bilancio annuale del proprio sistema qualità, "
                     "guardando cosa è andato storto e cosa migliorare. Causa / contesto: riesame annuale della "
                     "direzione che mette insieme le NC (non conformità) dell'anno, tra cui l'esclusione dalla "
                     "gara per firma mancante e l'IFC rifiutato, l'esito delle gare, i reclami e la formazione. "
                     "Intervento e stato: riesame ancora da fare. Da fare.",
                     ["riesame annuale", "riesame della direzione", "sistema qualità", "NC / non conformità",
                      "reclami", "formazione", "ISO 9001"])]},
     ],
     "updates": [
         ("Stato", "on_track", 75, 20, "2 NC chiuse con azioni, riesame a dicembre."),
     ]},
]

ORGANISATION["project_rules"] = [
    {"name": "Firme incrociate prima del carico", "where": "project:" + P_GARE, "severity": "must",
     "activities": [], "section": "offer",
     "body": "Prima di caricare un'offerta: due persone controllano firma digitale valida su ogni file, anche "
             "quelli dei mandanti RTP. Carico almeno 48h prima.",
     "keywords": "firme incrociate, firma digitale valida, controllo a due persone, carico offerta 48 ore "
                 "prima, mandanti RTP, esclusione gara, checklist gare"},
]

ORGANISATION["project_documents"] = [
    {"key": "ted_418556", "where": "task:" + P_GARE + "/Ancona uffici giudiziari BIM (TED 418556)",
     "name": "TED 418556-2026 - SIA in BIM, uffici giudiziari Ancona",
     "summary": "Bando europeo TED 418556-2026 (GUUE S 116 del 18/06/2026) del Provveditorato interregionale "
                "OO.PP. Toscana, Marche e Umbria, sede di Ancona. Procedura aperta con OEPV (artt. 71 e 108 "
                "D.Lgs. 36/2023) per servizi in modalità BIM di PFTE, CSP, architetto di chiara fama, DL, CSE, "
                "DO e ispettori di cantiere per gli uffici giudiziari di piazza Cavour 21 ad Ancona; valore "
                "stimato 4.128.351,48 euro, criteri A-E, scadenza 20/7/2026.",
     "url": URL_TED, "text_file": "ted-418556-2026-bim",
     "keywords": "TED 418556-2026, bando europeo / GUUE, Provveditorato OO.PP., uffici giudiziari Ancona, gara "
                 "in modalità BIM, OEPV, architetto di chiara fama, esperienza post sisma"},
    {"key": "capitolato_saffi", "where": "project:" + P_GARE,
     "name": "Regione Umbria - capitolato progettazione sede di Terni via Saffi",
     "summary": "Capitolato speciale descrittivo e prestazionale della Regione Umbria per progettazione "
                "definitiva, esecutiva e CSP dell'adeguamento sismico ed efficientamento energetico della sede "
                "regionale di Terni in via Saffi (POR FESR 2014-2020, Asse 8). Redatto col vecchio codice "
                "D.Lgs. 50/2016, base 329.886,16 euro calcolata con il DM 17/06/2016; descrive edificio "
                "(collaudato nel 1950), elaborati, tempi e penali. Lo studio lo ha usato per testare il foglio "
                "parcella.",
     "url": URL_SAFFI, "text_file": "umbria-capitolato-sede-terni",
     "keywords": "capitolato Regione Umbria, sede regionale Terni via Saffi, adeguamento sismico, "
                 "efficientamento energetico, POR FESR, D.Lgs. 50/2016 / vecchio codice, progettazione "
                 "definitiva ed esecutiva, base di gara DM 17/06/2016"},
    {"key": "all_i9", "where": "project:" + P_BIMSTD, "name": "D.Lgs. 36/2023 All. I.9 - gestione informativa digitale",
     "summary": "Allegato I.9 del D.Lgs. 36/2023 (art. 43): metodi e strumenti di gestione informativa digitale "
                "(BIM). Chiede alla stazione appaltante formazione, piano hardware/software e un atto di "
                "organizzazione, ACDat proprio e formati aperti non proprietari, il gestore dell'ACDat e dei "
                "processi digitali, capitolato informativo, oGI e pGI; fissa soglia e decorrenza dell'obbligo "
                "(dal 1/1/2025 sopra 2 milioni).",
     "url": NORMA + "~all.I.9", "text_file": "dlgs-36-2023-allegato-i9-bim",
     "keywords": "All. I.9, gestione informativa digitale / BIM, ACDat / CDE, formati aperti non proprietari / "
                 "IFC, capitolato informativo, oGI / pGI, atto di organizzazione, obbligo BIM sopra 2 milioni"},
]

ORGANISATION["project_notes"] = [
    {"kind": "fact", "where": "project:" + P_BIMSTD, "who": "bim", "section": "operations",
     "name": "ACDat studio",
     "body": "ACDat su cloud con stati WIP/SHARED/PUBLISHED/ARCHIVED. Se il CI chiede l'ACDat della SA si lavora "
             "lì e il nostro resta solo interno.",
     "keywords": "ACDat / ambiente di condivisione dati, CDE / common data environment, stati WIP / SHARED / "
                 "PUBLISHED / ARCHIVED, cloud dello studio, ACDat della stazione appaltante, archivio progetti "
                 "BIM"},
    {"kind": "fact", "where": "project:" + P_CFP, "who": "office", "section": "compliance",
     "name": "Crediti formativi: regole",
     "body": "ingegneri: saldo minimo 30 CFP per esercitare, 5 di etica/deontologia. architetti: 60 nel "
             "triennio, una parte su deontologia e compensi. coordinatori sicurezza: aggiornamento 40h ogni 5 "
             "anni sennò non si può fare CSP/CSE",
     "keywords": "crediti formativi / CFP, formazione continua obbligatoria, 30 CFP ingegneri, 5 CFP "
                 "deontologia / etica, 60 CFP triennio architetti, aggiornamento 40 ore coordinatori, "
                 "quinquennio, CSP / CSE abilitazione"},
]

# -- the customers --------------------------------------------------------------------------------------------
P_SCUOLA = "Scuola media Valfonda - esecutivo e CSP"
P_MUNICIPIO = "Municipio Valfonda - vulnerabilità sismica"

PARCELLA_TEXT = (
    "## Calcolo corrispettivo - Scuola media Valfonda, progetto esecutivo + CSP (rev. 2)\n\n"
    "Rif. DM 17/06/2016 e D.Lgs. 36/2023 All. I.13. Due livelli: il PFTE è del Comune (già approvato), a noi "
    "esecutivo e CSP. Nessun appalto integrato: QbII.05 (elenco prezzi, computo, QE) attribuita all'esecutivo.\n\n"
    "CP = V x G x Q x P, con P = 0,03 + 10 / V^0,4\n\n"
    "| ID | Opere | V (euro) | G | Q (somma) | P | CP (euro) |\n"
    "|---|---|---|---|---|---|---|\n"
    "| E.20 | edile, riqualificazione su esistente | 780.000,00 | 0,95 | 0,380 | 0,07397 | 20.828,63 |\n"
    "| S.03 | strutture c.a., miglioramento sismico | 520.000,00 | 0,95 | 0,385 | 0,08171 | 15.540,97 |\n"
    "| IA.02 | riscaldamento, VMC | 230.000,00 | 0,85 | 0,400 | 0,10167 | 7.950,23 |\n"
    "| IA.03 | impianti elettrici, FV | 90.000,00 | 1,15 | 0,400 | 0,13430 | 5.560,21 |\n\n"
    "Lavori totali 1.620.000,00. Compenso 49.880,04; spese e oneri accessori 24% = 11.971,21. Totale "
    "61.851,25 euro (oltre oneri previdenziali e IVA). Ribasso offerto 8% (max 20% in affidamento diretto): "
    "56.903,15 euro.\n\n"
    "Q comprende QbII.05, QbIII.01-.05 e QbIII.07 (PSC). Rev. 1 era su E.22 (G 1,55): totale 78.163,36. "
    "Corretta in E.20: edificio del 1962, nessun decreto di vincolo, meno di 70 anni, non serve la verifica "
    "dell'interesse culturale.\n")

VERBALE_TEXT = (
    "## Verbale di sopralluogo - Scuola media Valfonda\n\n"
    "Presenti: RUP del Comune, ing. Montanucci, ing. Rinaldi, il dirigente scolastico.\n\n"
    "1. Ispezionati piano terra, primo e copertura. Fessure a 45 gradi sui tamponamenti del vano scala lato "
    "nord; distacchi di copriferro su due travi del corridoio piano primo, armature ossidate.\n"
    "2. Copertura: guaina a fine vita, infiltrazioni in due aule (aule 12 e 14). Sottotetto non accessibile "
    "in sicurezza: serve linea vita provvisoria per i rilievi.\n"
    "3. Centrale termica: caldaia a gasolio del 1998 con serbatoio interrato, da dismettere. Nessuna VMC.\n"
    "4. Infissi in alluminio senza taglio termico, vetro singolo.\n"
    "5. Indagini concordate: 6 carote cls, 4 pacometriche, 2 saggi sui solai, prova di carico su un solaio "
    "tipo dopo l'intervento.\n"
    "6. Il dirigente chiede di non chiudere l'edificio per più di un anno scolastico: lavori in due fasi "
    "(estate + un semestre con le classi nei moduli). Da valutare nel cronoprogramma e nel PSC.\n")

COMUNE = {
    "ref": "TA-VALFONDA", "name": "Comune di Valfonda", "city": "Valfonda",
    "projects": [
        {"name": P_SCUOLA, "tags": ["opere pubbliche", "sismica", "energia", "scuola"],
         "description": "<p>Scuola media comunale (1962, c.a.), miglioramento sismico e riqualificazione energetica. "
                        "Lavori 1,62 mln (sotto 2 mln: BIM non obbligatorio). Incarico: progetto esecutivo + CSP, "
                        "affidamento diretto da elenco regionale, 56.903,15 + oneri e IVA. RUP del Comune. CAM "
                        "nuovi applicabili.</p>",
         "milestones": [("Affidamento", -160, 158), ("Consegna esecutivo", 25, None),
                        ("Verifica e validazione", 60, None)],
         "tasks": [
             {"name": "Preventivo e affidamento diretto", "who": "lead", "stage": "Fatto", "milestone": "Affidamento",
              "description": "richiesta preventivo del RUP via PEC, da elenco regionale professionisti",
              "notes": [("lead", 175, "richiesta arrivata. scad preventivo 10 gg"),
                        ("lead", 166, "preventivo inviato: DM rev 2, ribasso 8%"),
                        ("office", 158, "determina di affidamento arrivata. CIG nel fascicolo"),
                        ("lead", 157, "Sintomo: il RUP del Comune di Valfonda chiede via PEC un preventivo per "
                         "esecutivo e coordinamento sicurezza della scuola media, con 10 giorni per rispondere. "
                         "Causa / contesto: affidamento diretto sotto soglia (art. 50 D.Lgs. 36/2023), studio "
                         "scelto dall'elenco regionale dei professionisti; preventivo sul DM 17/06/2016 "
                         "(decreto parametri), foglio parcella rev. 2. Intervento e stato: preventivo inviato "
                         "con ribasso dell'8%; arrivata la determina di affidamento, CIG (codice identificativo "
                         "gara) archiviato nel fascicolo. Fatto.",
                         ["affidamento diretto", "richiesta preventivo PEC", "determina di affidamento",
                          "CIG / codice identificativo gara", "RUP / responsabile unico del progetto",
                          "elenco regionale professionisti", "ribasso 8%", "scuola media Valfonda"])]},
             {"name": "Calcolo parcella", "who": "junior", "stage": "Fatto",
              "description": "E.20 vs E.22? S.03, IA.02, IA.03",
              "notes": [("junior", 172, "rev1 fatta con E.22, l'edificio sembra storico (facciata anni '60 "
                                        "con mattoni a vista)"),
                        ("partner", 171, "E.22 è per vincolati. c'è il decreto? è del 62, meno di 70 anni, "
                                         "pubblico ma non soggetto. rifare in E.20"),
                        ("junior", 170, "rev2: da 78.163 a 61.851. QbII.05 spostata sull'esecutivo come da "
                                        "I.13 (no appalto integrato)"),
                        ("junior", 169, "Sintomo: il corrispettivo della scuola di Valfonda risultava troppo "
                         "alto perché l'edificio sembrava storico. Causa / contesto: calcolo con DM 17/06/2016 "
                         "e All. I.13; categorie E.20 (edilizia su esistente, G 0,95) o E.22 (edifici "
                         "vincolati, G 1,55), più S.03 strutture, IA.02 riscaldamento/VMC, IA.03 impianti "
                         "elettrici. L'edificio è del 1962, pubblico ma con meno di 70 anni e senza decreto di "
                         "vincolo. Intervento e stato: rev. 1 in E.22 corretta in rev. 2 in E.20, da 78.163 a "
                         "61.851 euro; QbII.05 attribuita all'esecutivo perché non c'è appalto integrato. "
                         "Fatto.",
                         ["calcolo parcella / corrispettivo", "E.20 / edilizia esistente",
                          "E.22 / edificio vincolato", "grado di complessità G", "vincolo culturale", "QbII.05",
                          "All. I.13", "appalto integrato"])],
              "worklog": [("junior", 172, 3.0, "parcella rev1"), ("junior", 170, 2.0, "parcella rev2 E.20")]},
             {"name": "Disciplinare d'incarico", "who": "office", "stage": "Fatto",
              "description": "firma digitale, polizza, tracciabilità flussi",
              "notes": [("office", 155, "firmato. conto dedicato comunicato"),
                        ("office", 154, "Sintomo: prima di iniziare va firmato il contratto con il Comune per "
                         "l'incarico di esecutivo e coordinamento sicurezza della scuola. Causa / contesto: "
                         "disciplinare d'incarico (contratto professionale con la pubblica amministrazione) con "
                         "firma digitale, polizza professionale e obblighi di tracciabilità dei flussi "
                         "finanziari, che richiedono di comunicare il conto corrente dedicato. Intervento e "
                         "stato: disciplinare firmato e conto dedicato comunicato al Comune. Fatto.",
                         ["disciplinare d'incarico", "contratto professionale", "firma digitale",
                          "tracciabilità flussi finanziari", "conto corrente dedicato", "polizza progettista",
                          "Comune di Valfonda"])]},
             {"name": "Sopralluogo e piano indagini", "who": "junior", "stage": "Fatto",
              "description": "verbale + piano indagini",
              "notes": [("junior", 150, "verbale caricato. 6 carote, 4 pacometriche, saggi solai"),
                        ("lead", 120, "esiti lab: fck medio 18 MPa, staffe rade. FC2 con indagini estese"),
                        ("junior", 119, "Sintomo: verificare lo stato della scuola e decidere quali prove fare "
                         "sulle strutture. Causa / contesto: verbale di sopralluogo e piano indagini: carotaggi "
                         "del calcestruzzo, indagini pacometriche sulle armature, saggi sui solai; esiti di "
                         "laboratorio con fck (resistenza caratteristica del calcestruzzo) medio 18 MPa e "
                         "staffe rade; livello di conoscenza FC2 con indagini estese. Intervento e stato: "
                         "verbale caricato, eseguite 6 carote, 4 pacometriche e saggi sui solai. Fatto.",
                         ["sopralluogo", "piano indagini", "carotaggi / carote calcestruzzo",
                          "indagini pacometriche", "saggi solai", "fck / resistenza calcestruzzo",
                          "fattore di confidenza FC2", "livello di conoscenza"])]},
             {"name": "Modello strutturale e verifica sismica", "who": "lead", "stage": "In corso",
              "milestone": "Consegna esecutivo",
              "description": "zeta E stato di fatto, miglioramento >= 0,6 (scuola, classe III)",
              "notes": [("lead", 90, "zetaE ante 0,42. con FRP nodi + 2 setti nuovi vano scala arriviamo a 0,63"),
                        ("lead", 20, "setti: fondazioni su micropali, sentito geologo. ok"),
                        ("lead", 19, "Sintomo: la scuola deve diventare più sicura in caso di terremoto, fino "
                         "al livello richiesto per un edificio scolastico. Causa / contesto: modello "
                         "strutturale e verifica sismica; zeta E (indice di sicurezza sismica) dello stato di "
                         "fatto 0,42, miglioramento sismico richiesto almeno 0,6 per scuola in classe d'uso "
                         "III. Intervento e stato: con rinforzi in FRP (fibre composite) ai nodi e 2 setti "
                         "nuovi in c.a. nel vano scala si arriva a 0,63; setti fondati su micropali, sentito il "
                         "geologo. In corso.",
                         ["verifica sismica", "miglioramento sismico", "zeta E / indice di sicurezza sismica",
                          "FRP / fibre di rinforzo", "setti in cemento armato", "micropali", "classe d'uso III",
                          "vulnerabilità sismica scuola"])]},
             {"name": "Progetto energetico ex L.10 e APE", "who": "partner", "stage": "In corso",
              "milestone": "Consegna esecutivo",
              "description": "cappotto, infissi, PdC al posto del gasolio, VMC aule, FV 20 kWp",
              "notes": [("partner", 60, "APE ante G, post stimato B. serbatoio gasolio interrato da bonificare: "
                                        "voce nel QE"),
                        ("partner", 15, "VMC aule con recupero, canali a vista nel corridoio"),
                        ("partner", 14, "Sintomo: il Comune vuole una scuola che consumi meno, senza più la "
                         "caldaia a gasolio. Causa / contesto: progetto energetico ex Legge 10 e APE (attestato "
                         "di prestazione energetica, certificato energetico): cappotto, infissi, PdC (pompa di "
                         "calore) al posto del gasolio, VMC (ventilazione meccanica controllata) nelle aule, FV "
                         "(fotovoltaico) 20 kWp. Intervento e stato: classe energetica ante G, post stimata B; "
                         "serbatoio gasolio interrato da bonificare inserito nel QE (quadro economico); VMC con "
                         "recupero e canali a vista nel corridoio. In corso.",
                         ["Legge 10 / relazione energetica",
                          "APE / attestato di prestazione energetica / classe energetica",
                          "PdC / pompa di calore", "VMC / ventilazione meccanica controllata",
                          "FV / fotovoltaico", "cappotto termico", "serbatoio gasolio interrato",
                          "efficientamento energetico scuola"])]},
             {"name": "Relazione CAM", "who": "arch", "stage": "In corso", "milestone": "Consegna esecutivo",
              "description": "nuovi CAM DM 24/11/2025 (da feb 2026), criterio per criterio",
              "notes": [("arch", 45, "PROBLEMA 2.4.7: EPS grafitato a capitolato senza dichiarazione contenuto di "
                                     "riciclato/EPD del produttore. non verificabile"),
                        ("arch", 38, "cambiato isolante: fibra di legno 14 cm con EPD (lambda peggiore, rifatti "
                                     "conti L.10 con Lorenzo). +18k sul computo"),
                        ("lead", 37, "ok, avvisato RUP via PEC del cambio e del motivo"),
                        ("arch", 36, "Sintomo: l'isolante previsto in capitolato non permette di dimostrare il "
                         "rispetto dei criteri ambientali. Causa / contesto: relazione CAM (criteri ambientali "
                         "minimi) secondo il DM 24/11/2025, in vigore da febbraio 2026; criterio 2.4.7 "
                         "isolanti: l'EPS grafitato non aveva dichiarazione del contenuto di riciclato né EPD "
                         "(dichiarazione ambientale di prodotto). Intervento e stato: sostituito con fibra di "
                         "legno 14 cm con EPD, rifatti i calcoli Legge 10 (lambda peggiore), computo aumentato "
                         "di 18 mila euro; RUP avvisato via PEC del cambio e del motivo. In corso.",
                         ["relazione CAM", "CAM / criteri ambientali minimi", "criterio 2.4.7 isolanti",
                          "EPD / dichiarazione ambientale di prodotto", "contenuto di riciclato",
                          "EPS grafitato", "fibra di legno", "DM 24/11/2025"])]},
             {"name": "Computo metrico e QE", "who": "junior", "stage": "In corso",
              "milestone": "Consegna esecutivo",
              "description": "prezzario Regione Umbria 2026, NP con analisi",
              "notes": [("junior", 10, "computo a 1,64 mln con fibra di legno, sforiamo di 20k. vedere con RUP"),
                        ("junior", 9, "Sintomo: il costo dei lavori della scuola supera il budget del Comune. "
                         "Causa / contesto: computo metrico estimativo e QE (quadro economico) sul prezzario "
                         "Regione Umbria 2026, con NP (nuovi prezzi) giustificati da analisi; l'isolante in "
                         "fibra di legno per i CAM ha aumentato i costi. Intervento e stato: computo a 1,64 "
                         "milioni, sforamento di circa 20 mila euro; da discutere con il RUP. In corso.",
                         ["computo metrico estimativo", "QE / quadro economico", "prezzario Regione Umbria 2026",
                          "NP / nuovi prezzi", "analisi prezzi", "sforamento budget / costo lavori",
                          "scuola Valfonda"])]},
             {"name": "PSC e fascicolo", "who": "lead", "stage": "In corso", "milestone": "Consegna esecutivo",
              "description": "due fasi, classi nei moduli prefabbricati, interferenze con scuola aperta",
              "notes": [("lead", 25, "PSC rev.1: fase 2 con scuola aperta, ingressi separati, recinzione "
                                     "h 2m, orari mezzi fuori ingresso/uscita alunni"),
                        ("lead", 8, "costi sicurezza 61k, troppi? RUP chiede di rivedere"),
                        ("lead", 7, "Sintomo: la scuola deve restare in parte aperta durante il cantiere e il "
                         "RUP trova alti i costi della sicurezza. Causa / contesto: PSC (piano di sicurezza e "
                         "coordinamento) e fascicolo dell'opera; lavori in due fasi, classi nei moduli "
                         "prefabbricati, interferenze con la scuola aperta. Intervento e stato: PSC rev. 1 con "
                         "ingressi separati, recinzione alta 2 m e mezzi fuori dagli orari di ingresso e uscita "
                         "degli alunni; costi della sicurezza 61 mila euro, il RUP chiede di rivederli. In "
                         "corso.",
                         ["PSC / piano di sicurezza e coordinamento", "fascicolo dell'opera",
                          "costi della sicurezza", "interferenze scuola aperta",
                          "moduli prefabbricati / container", "lavori in due fasi", "recinzione di cantiere"])]},
             {"name": "Incontro con dirigente scolastico", "who": "lead", "stage": "Fatto",
              "description": "",
              "notes": [("lead", 70, "la preside ha scritto: «i ragazzi a settembre dove li mettiamo? non posso "
                                     "avere un altro anno nei container, i genitori sono già arrabbiati». "
                                     "proposto: fase 1 estate (strutture vano scala), fase 2 un semestre"),
                        ("lead", 69, "Sintomo: la dirigente scolastica chiede dove andranno i ragazzi a "
                         "settembre: non vuole un altro anno nei container, i genitori sono già arrabbiati. "
                         "Causa / contesto: organizzazione delle fasi di cantiere e del cronoprogramma della "
                         "scuola media di Valfonda, con le classi nei moduli prefabbricati durante i lavori. "
                         "Intervento e stato: proposta fase 1 in estate (strutture del vano scala) e fase 2 di "
                         "un semestre. Fatto.",
                         ["dirigente scolastico / preside", "container / moduli prefabbricati",
                          "fasi di cantiere", "cronoprogramma", "lavori in estate",
                          "scuola aperta durante i lavori", "genitori"])]},
             {"name": "Verifica preventiva esecutivo", "who": "lead", "stage": "Da fare",
              "milestone": "Verifica e validazione", "deadline": 60,
              "description": "verificatore esterno del Comune, rispondere ai rilievi",
              "notes": [("lead", 1, "Sintomo: il progetto esecutivo della scuola deve superare il controllo del "
                         "verificatore incaricato dal Comune prima di andare in gara. Causa / contesto: "
                         "verifica preventiva della progettazione affidata dal Comune di Valfonda a un "
                         "verificatore esterno; lo studio dovrà rispondere ai rilievi, cioè alle osservazioni e "
                         "richieste di correzione sugli elaborati. Intervento e stato: attività da fare quando "
                         "arriveranno i rilievi del verificatore. Da fare.",
                         ["verifica preventiva progetto", "verificatore esterno", "rilievi del verificatore",
                          "validazione progetto", "progetto esecutivo", "scuola Valfonda"])]},
             {"name": "Consegna esecutivo", "who": "lead", "stage": "Da fare", "milestone": "Consegna esecutivo",
              "deadline": 25, "description": "PEC con elenco elaborati firmati",
              "notes": [("lead", 1, "Sintomo: il progetto esecutivo della scuola va consegnato ufficialmente al "
                         "Comune. Causa / contesto: per regola del Comune di Valfonda gli elaborati si mandano "
                         "firmati digitalmente e via PEC al RUP (o sulla piattaforma se la chiede), con "
                         "l'elenco degli elaborati firmati; link di trasferimento e mail ordinarie valgono solo "
                         "come copia di cortesia. Intervento e stato: consegna da fare. Da fare.",
                         ["consegna esecutivo", "PEC", "elenco elaborati", "firma digitale",
                          "trasmissione elaborati", "RUP / responsabile unico del progetto", "scuola Valfonda"])]},
         ],
         "updates": [
             ("Settembre", "on_track", 45, 40, "indagini fatte, verifica sismica ok (0,63), CAM: cambiato isolante."),
             ("Ottobre", "at_risk", 65, 7,
              "computo sfora di 20k per cambio isolante CAM, costi sicurezza da rivedere. consegna fra 25 gg."),
         ]},
        {"name": P_MUNICIPIO, "tags": ["opere pubbliche", "sismica"],
         "description": "<p>Verifica di vulnerabilità sismica del municipio (muratura, '800). Incarico 18.400.</p>",
         "milestones": [("Relazione di vulnerabilità", 70, None)],
         "tasks": [
             {"name": "Rilievo geometrico e materico", "who": "arch", "stage": "Fatto",
              "description": "laser scanner + saggi",
              "notes": [("arch", 30, "nuvola fatta, saggi su 4 maschi murari"),
                        ("arch", 29, "Sintomo: per valutare la sicurezza sismica del municipio serve conoscerne "
                         "con precisione la geometria e i materiali. Causa / contesto: rilievo geometrico con "
                         "laser scanner (nuvola di punti) e rilievo materico con saggi sulle murature portanti, "
                         "per la verifica di vulnerabilità sismica dell'edificio vincolato in muratura; i saggi "
                         "sono autorizzati dalla Soprintendenza. Intervento e stato: nuvola di punti "
                         "completata, saggi eseguiti su 4 maschi murari. Fatto.",
                         ["rilievo geometrico", "rilievo materico", "laser scanner / nuvola di punti",
                          "saggi murature", "maschi murari", "vulnerabilità sismica municipio",
                          "edificio in muratura"])]},
             {"name": "Prove martinetti piatti", "who": "junior", "stage": "In attesa",
              "description": "lab esterno",
              "notes": [("junior", 12, "il lab ci dà data a fine novembre"),
                        ("junior", 11, "Sintomo: mancano le prove sulle murature del municipio per poter "
                         "completare la valutazione della sicurezza sismica. Causa / contesto: prove con "
                         "martinetti piatti sulle murature portanti, per caratterizzare meccanicamente la "
                         "muratura dell'edificio vincolato; le prove sono affidate a un laboratorio esterno. "
                         "Intervento e stato: il laboratorio ha dato disponibilità solo a fine novembre; il "
                         "modello e i meccanismi locali attendono i risultati. In attesa.",
                         ["martinetti piatti", "prove su muratura", "laboratorio esterno",
                          "caratterizzazione meccanica", "vulnerabilità sismica municipio",
                          "indagini diagnostiche"])]},
             {"name": "Modello e meccanismi locali", "who": "lead", "stage": "Da fare",
              "milestone": "Relazione di vulnerabilità", "description": "cinematismi + globale",
              "notes": [("lead", 1, "Sintomo: bisogna capire come potrebbe danneggiarsi o crollare il municipio "
                         "in caso di terremoto, sia per singole parti sia nel suo complesso. Causa / contesto: "
                         "modello strutturale dell'edificio vincolato in muratura con analisi dei meccanismi "
                         "locali di collasso (cinematismi) e analisi globale, per la verifica di vulnerabilità "
                         "sismica commissionata dal Comune di Valfonda. Intervento e stato: attività da fare. "
                         "Da fare.",
                         ["meccanismi locali", "cinematismi", "analisi globale", "modello strutturale muratura",
                          "vulnerabilità sismica municipio", "ribaltamento pareti", "verifica sismica"])]},
             {"name": "Edificio vincolato: autorizzazione indagini", "who": "arch", "stage": "Fatto",
              "description": "Soprintendenza per i saggi",
              "notes": [("arch", 50, "autorizzazione saggi arrivata, niente carote sulla facciata"),
                        ("arch", 49, "Sintomo: per fare i saggi sul municipio, edificio tutelato, serve il "
                         "permesso della tutela dei beni culturali. Causa / contesto: edificio vincolato: le "
                         "indagini invasive per la verifica di vulnerabilità sismica (saggi, carotaggi) "
                         "richiedono l'autorizzazione della Soprintendenza. Intervento e stato: autorizzazione "
                         "ai saggi arrivata, con la prescrizione di non fare carotaggi sulla facciata; i saggi "
                         "del rilievo materico sono stati eseguiti sui maschi murari. Fatto.",
                         ["edificio vincolato / bene culturale", "Soprintendenza", "autorizzazione indagini",
                          "saggi", "divieto carote in facciata", "vulnerabilità sismica municipio"])]},
         ],
         "updates": [("Avvio", "on_track", 25, 12, "rilievo fatto, prove in attesa del lab.")]},
    ],
    "rules": [
        {"name": "Elaborati al Comune solo firmati e via PEC", "where": "customer", "who": "lead", "state": "active",
         "severity": "must", "activities": ["communication"], "section": "operations",
         "body": "Al Comune gli elaborati si mandano firmati digitalmente e via PEC al RUP (o sulla piattaforma se "
                 "la chiede). Link di trasferimento e mail ordinarie solo come copia di cortesia.",
         "keywords": "Comune di Valfonda, elaborati firmati digitalmente, PEC al RUP, piattaforma, link di "
                     "trasferimento, copia di cortesia, trasmissione elaborati"},
    ],
    "documents": [
        {"key": "parcella_scuola", "where": "task:" + P_SCUOLA + "/Calcolo parcella",
         "name": "Foglio parcella scuola Valfonda rev. 2",
         "summary": "Foglio di calcolo dello studio (rev. 2) del corrispettivo per esecutivo e CSP della scuola "
                    "media di Valfonda, con DM 17/06/2016 e All. I.13. Categorie E.20, S.03, IA.02, IA.03 su "
                    "1.620.000 euro di lavori; compenso 49.880,04 più spese 24%, totale 61.851,25 euro, con "
                    "ribasso 8% 56.903,15 euro; QbII.05 all'esecutivo (niente appalto integrato). La rev. 1 in "
                    "E.22 (78.163,36) è stata corretta: edificio del 1962 senza vincolo.",
         "url": "https://cloud.trearchi.example/commesse/valfonda-scuola/parcella-rev2", "keep_text": True,
         "text": PARCELLA_TEXT,
         "keywords": "foglio parcella, scuola Valfonda, calcolo corrispettivo / onorario, E.20 / S.03 / IA.02 / "
                     "IA.03, spese 24%, ribasso 8%, QbII.05, E.22 corretta"},
        {"key": "verbale_sopralluogo", "where": "task:" + P_SCUOLA + "/Sopralluogo e piano indagini",
         "name": "Verbale di sopralluogo scuola Valfonda",
         "summary": "Verbale di sopralluogo alla scuola media di Valfonda con RUP e dirigente scolastico. "
                    "Rileva fessure a 45 gradi nel vano scala, copriferri distaccati, copertura con "
                    "infiltrazioni, caldaia a gasolio del 1998 con serbatoio interrato, assenza di VMC, infissi "
                    "senza taglio termico; concorda 6 carote, 4 pacometriche, 2 saggi sui solai e una prova di "
                    "carico; lavori in due fasi per non chiudere la scuola più di un anno scolastico.",
         "url": "https://cloud.trearchi.example/commesse/valfonda-scuola/verbale-sopralluogo", "keep_text": True,
         "text": VERBALE_TEXT,
         "keywords": "verbale di sopralluogo, scuola media Valfonda, quadro fessurativo / crepe, infiltrazioni "
                     "copertura, caldaia a gasolio / serbatoio interrato, carote / pacometriche / saggi, lavori "
                     "in due fasi, linea vita"},
    ],
    "notes": [
        {"kind": "fact", "where": "customer", "who": "lead", "section": "profile", "name": "Comune: chi decide",
         "body": "RUP = resp. area tecnica (geom.), decide su tutto il tecnico. Determina e pagamenti: ragioneria, "
                 "lenta (60 gg). Sindaco interessato solo ai tempi della scuola.",
         "keywords": "Comune di Valfonda, RUP / responsabile unico del progetto, responsabile area tecnica, "
                     "determina, ragioneria pagamenti 60 giorni, sindaco, tempi scuola, chi decide / "
                     "interlocutori"},
        {"kind": "fact", "where": "project:" + P_SCUOLA, "who": "lead", "section": "operations",
         "name": "Scuola: decisioni progetto",
         "body": "miglioramento zetaE 0,42->0,63 (FRP nodi, 2 setti c.a. vano scala su micropali). fibra di legno "
                 "al posto EPS per CAM 2.4.7. PdC + VMC aule, FV 20 kWp. lavori in 2 fasi.",
         "keywords": "scuola media Valfonda, decisioni progetto, miglioramento sismico zeta E 0,42-0,63, FRP / "
                     "fibre di rinforzo, setti c.a. su micropali, fibra di legno al posto EPS, CAM 2.4.7, PdC / "
                     "pompa di calore e VMC, FV 20 kWp, lavori in 2 fasi"},
    ],
}

P_TIGLI = "Via dei Tigli - 24 alloggi ERP, riqualificazione energetica"

ATER = {
    "ref": "TA-ACUS", "name": "Agenzia Casa Umbria Sud (ATER fittizia)", "city": "Terni",
    "projects": [
        {"name": P_TIGLI, "tags": ["BIM", "energia", "Conto Termico", "ERP"],
         "description": "<p>Due palazzine ERP anni '70, 24 alloggi abitati. Cappotto, infissi, centrale a pompa "
                        "di calore, VMC, FV. Lavori 2,35 mln: BIM obbligatorio (CI ATER, pGI nostro). Incentivo "
                        "Conto Termico 3.0 a prenotazione (ex IACP). Incarico PFTE + esecutivo + CSP.</p>",
         "milestones": [("Prenotazione CT 3.0", -200, 199), ("PFTE approvato", -95, 90),
                        ("Esecutivo", 40, None)],
         "tasks": [
             {"name": "pGI su capitolato informativo ATER", "who": "bim", "stage": "Fatto",
              "description": "CI ATER: IFC 4, ACDat ATER, LOIN per fase, BCF",
              "notes": [("bim", 240, "pGI rev0 inviato, ruoli: BIM manager Andrea, coordinator Matteo"),
                        ("bim", 225, "rev1 dopo commenti: aggiunta matrice LOIN e codifica ATER"),
                        ("bim", 224, "Sintomo: l'ATER chiede come lo studio gestirà il processo BIM della "
                         "riqualificazione delle case popolari di via dei Tigli. Causa / contesto: pGI (piano "
                         "di gestione informativa, piano BIM) redatto sul CI (capitolato informativo) ATER: IFC "
                         "4, ACDat ATER, LOIN (livello di fabbisogno informativo) per fase, BCF per le issue; "
                         "ruoli BIM manager e BIM coordinator. Intervento e stato: rev. 0 inviata; rev. 1 dopo "
                         "i commenti con matrice LOIN e codifica ATER. Fatto.",
                         ["pGI / piano di gestione informativa / piano BIM", "CI / capitolato informativo",
                          "ATER / case popolari", "LOIN / livello di fabbisogno informativo", "BCF", "IFC 4",
                          "codifica ATER", "ERP / edilizia residenziale pubblica"])]},
             {"name": "Consegna PFTE su ACDat ATER", "who": "bim", "stage": "Fatto",
              "milestone": "PFTE approvato",
              "description": "IFC + PDF",
              "notes": [("bim", 112, "RIFIUTATA: caricato per errore il .rvt federato al posto dell'IFC. "
                                     "il gestore ACDat ATER: formato proprietario non ammesso (CI par. 3.2)"),
                        ("bim", 110, "ricaricato IFC4 verificato in viewer indipendente. accettato. NC aperta"),
                        ("lead", 109, "regola: consegna ufficiale solo IFC, mai il nativo"),
                        ("bim", 108, "Sintomo: il gestore dell'ambiente di condivisione dati ATER rifiuta la "
                         "consegna del progetto di fattibilità. Causa / contesto: caricato per errore il "
                         "modello federato nativo (.rvt, formato proprietario) invece dell'IFC; il CI "
                         "(capitolato informativo) par. 3.2 non ammette formati proprietari sull'ACDat. "
                         "Intervento e stato: ricaricato IFC4 verificato in un viewer indipendente, consegna "
                         "accettata; aperta una NC (non conformità); regola: consegna ufficiale solo IFC, mai "
                         "il nativo. Fatto.",
                         ["consegna PFTE / progetto di fattibilità", "consegna rifiutata",
                          "modello nativo / formato proprietario", "IFC4 / formato aperto", "ACDat ATER",
                          "viewer indipendente", "NC / non conformità", "capitolato informativo"])]},
             {"name": "Clash detection PFTE", "who": "bim", "stage": "Fatto",
              "description": "MEC vs STR, modello federato",
              "notes": [("bim", 125, "212 clash, 140 falsi (tolleranze). il grave: canale VMC DN250 che passa "
                                     "dentro la trave di bordo esistente piano 2 lato strada"),
                        ("partner", 123, "spostato il canale nel controsoffitto del disimpegno, niente forature "
                                         "di travi esistenti"),
                        ("bim", 118, "clash MEP/strutture risolti al 90%, restano soft clash centrale"),
                        ("bim", 117, "Sintomo: verificare che impianti e strutture del progetto di via dei "
                         "Tigli non si scontrino. Causa / contesto: clash detection (controllo interferenze) "
                         "MEC contro STR sul modello federato: 212 clash, 140 falsi positivi da tolleranze; il "
                         "grave è un canale VMC DN250 dentro la trave di bordo esistente al piano 2. Intervento "
                         "e stato: canale spostato nel controsoffitto del disimpegno, nessuna foratura di travi "
                         "esistenti; interferenze impianti/strutture risolte al 90%, restano soft clash in "
                         "centrale. Fatto.",
                         ["clash detection / controllo interferenze", "modello federato", "canale VMC",
                          "trave esistente", "falsi positivi", "controsoffitto", "soft clash", "MEP / strutture"])]},
             {"name": "Diagnosi energetica ante", "who": "partner", "stage": "Fatto",
              "description": "per prenotazione CT 3.0 serve la diagnosi ante",
              "notes": [("partner", 230, "APE ante G (tutte le unità), post stimato B. EPgl,nren da 210 a 62"),
                        ("partner", 215, "diagnosi firmata, allegata alla prenotazione"),
                        ("partner", 214, "Sintomo: per chiedere l'incentivo a prenotazione serve la fotografia "
                         "energetica degli alloggi prima dei lavori. Causa / contesto: diagnosi energetica ante "
                         "operam obbligatoria per la prenotazione del CT 3.0 (Conto Termico); APE (attestato di "
                         "prestazione energetica) ante in classe G per tutte le unità, post stimata B; "
                         "EPgl,nren (indice di prestazione energetica globale non rinnovabile) da 210 a 62. "
                         "Intervento e stato: diagnosi firmata e allegata alla prenotazione. Fatto.",
                         ["diagnosi energetica ante",
                          "APE / attestato di prestazione energetica / classe energetica", "EPgl,nren",
                          "CT 3.0 / Conto Termico", "prenotazione incentivo", "case popolari via dei Tigli",
                          "riqualificazione energetica"])]},
             {"name": "Domanda Conto Termico 3.0 a prenotazione", "who": "partner", "stage": "Fatto",
              "milestone": "Prenotazione CT 3.0",
              "description": "PortalTermico, soggetto ex IACP",
              "notes": [("partner", 245, "pronta per lunedì 2/3"),
                        ("partner", 243, "portale SOSPESO dal 3/3, budget 2026 esaurito. bloccati. avvisata ATER, "
                                 "niente avvio lavori prima"),
                        ("partner", 200, "riaperto 13/4, inviata il 15/4"),
                        ("partner", 160, "prenotazione confermata dal GSE. incentivo massimo a preventivo 690k"),
                        ("partner", 159, "Sintomo: l'ATER vuole l'incentivo statale per i lavori, ma il portale "
                         "chiude per fondi esauriti. Causa / contesto: domanda Conto Termico 3.0 a prenotazione "
                         "su PortalTermico del GSE (Gestore dei servizi energetici), soggetto ex IACP; portale "
                         "sospeso dal 3/3 per budget 2026 esaurito, riaperto il 13/4. Intervento e stato: "
                         "domanda inviata il 15/4, prenotazione confermata dal GSE con incentivo massimo a "
                         "preventivo di 690 mila euro; ATER avvisata di non avviare i lavori prima. Fatto.",
                         ["Conto Termico 3.0", "PortalTermico", "GSE / Gestore servizi energetici",
                          "prenotazione incentivo", "budget esaurito / portale sospeso", "ex IACP / ATER",
                          "incentivo a preventivo", "contributo statale"])]},
             {"name": "Relazione CAM esecutivo", "who": "arch", "stage": "In corso", "milestone": "Esecutivo",
              "description": "", "notes": [("arch", 18, "stessa storia isolanti della scuola: EPD richieste "
                                                        "in capitolato"),
                                           ("arch", 17, "Sintomo: nell'esecutivo delle case popolari si "
                                            "ripresenta il problema già visto sulla scuola: isolanti senza "
                                            "documentazione ambientale. Causa / contesto: relazione CAM "
                                            "(criteri ambientali minimi) del progetto esecutivo di via dei "
                                            "Tigli: gli isolanti devono avere EPD (dichiarazione ambientale di "
                                            "prodotto) e dichiarazione del contenuto di riciclato, altrimenti "
                                            "il criterio 2.4.7 non è verificabile. Intervento e stato: EPD e "
                                            "dichiarazioni richieste nel capitolato. In corso.",
                                            ["relazione CAM", "CAM / criteri ambientali minimi",
                                             "EPD / dichiarazione ambientale di prodotto", "isolanti",
                                             "criterio 2.4.7", "capitolato", "progetto esecutivo ATER"])]},
             {"name": "Esecutivo impianti centrale PdC", "who": "partner", "stage": "In corso",
              "milestone": "Esecutivo",
              "description": "PdC aria-acqua in cascata, accumulo, contabilizzazione",
              "notes": [("partner", 22, "3 PdC da 70 kW in cascata. vibrazioni: basamento antivibrante"),
                        ("partner", 21, "Sintomo: l'ATER vuole una nuova centrale termica per i 24 alloggi, "
                         "senza vibrazioni e rumore per gli inquilini. Causa / contesto: progetto esecutivo "
                         "degli impianti con PdC (pompe di calore) aria-acqua in cascata, accumulo e "
                         "contabilizzazione del calore per alloggio, nella riqualificazione energetica "
                         "incentivata dal Conto Termico 3.0. Intervento e stato: previste 3 PdC da 70 kW in "
                         "cascata su basamento antivibrante. In corso.",
                         ["PdC / pompa di calore aria-acqua", "centrale termica", "cascata", "accumulo",
                          "contabilizzazione calore", "basamento antivibrante", "vibrazioni / rumore"])]},
             {"name": "PSC con alloggi abitati", "who": "lead", "stage": "In corso", "milestone": "Esecutivo",
              "description": "inquilini dentro durante i lavori",
              "notes": [("lead", 30, "il tecnico ATER: «gli inquilini chiedono se devono uscire di casa e se "
                                     "resteranno senza riscaldamento a gennaio». risposto: no uscita, infissi "
                                     "un alloggio al giorno, centrale nuova in estate"),
                        ("lead", 29, "Sintomo: il tecnico ATER riferisce che gli inquilini chiedono se dovranno "
                         "uscire di casa e se resteranno senza riscaldamento a gennaio. Causa / contesto: PSC "
                         "(piano di sicurezza e coordinamento) con alloggi abitati durante i lavori; preavvisi "
                         "agli inquilini solo tramite ATER. Intervento e stato: risposto che non serve uscire, "
                         "infissi sostituiti un alloggio al giorno, centrale termica nuova realizzata in "
                         "estate. In corso.",
                         ["PSC / piano di sicurezza e coordinamento", "alloggi abitati", "inquilini",
                          "riscaldamento in inverno", "sostituzione infissi", "cantiere con residenti",
                          "ATER / case popolari"])]},
             {"name": "Verifica esecutivo ATER", "who": "lead", "stage": "Da fare", "deadline": 70,
              "description": "verifica interna ATER, risposte ai rilievi",
              "notes": [("lead", 1, "Sintomo: il progetto esecutivo delle case popolari di via dei Tigli deve "
                         "superare il controllo dell'ufficio tecnico dell'ATER prima dell'appalto. Causa / "
                         "contesto: verifica interna della progettazione da parte dell'ATER, stazione "
                         "appaltante; lo studio dovrà rispondere ai rilievi, con comunicazioni formali solo dal "
                         "partner di commessa via PEC o piattaforma. Intervento e stato: attività da fare "
                         "quando arriveranno i rilievi. Da fare.",
                         ["verifica esecutivo", "verifica progettazione", "rilievi", "validazione",
                          "ATER / stazione appaltante", "case popolari via dei Tigli"])]},
             {"name": "Fatture e acconti incarico", "who": "office", "stage": "In attesa",
              "description": "acconto 30% alla consegna PFTE",
              "notes": [("office", 60, "fattura acconto PFTE emessa, ATER paga a 60 gg"),
                        ("office", 59, "Sintomo: lo studio deve incassare il primo acconto dei propri onorari "
                         "per l'incarico delle case popolari. Causa / contesto: il contratto con l'ATER prevede "
                         "un acconto del 30% degli onorari alla consegna del PFTE (progetto di fattibilità "
                         "tecnica ed economica), consegna accettata in IFC sull'ACDat ATER; l'ATER paga a 60 "
                         "giorni. Intervento e stato: fattura di acconto PFTE emessa, si attende il pagamento. "
                         "In attesa.",
                         ["fattura acconto", "acconto 30%", "onorari", "pagamento a 60 giorni", "consegna PFTE",
                          "ATER", "incasso"])]},
         ],
         "updates": [
             ("PFTE approvato", "on_track", 50, 88, "PFTE approvato dopo IFC rifiutato e riconsegnato. CT 3.0 "
                                                     "prenotazione confermata."),
             ("Ottobre", "on_track", 70, 9, "esecutivo in corso, PSC con alloggi abitati, consegna fra 40 gg."),
         ]},
    ],
    "rules": [
        {"name": "Alloggi abitati: preavviso agli inquilini tramite ATER", "where": "customer", "who": "lead",
         "state": "active", "severity": "must", "activities": [], "section": "operations",
         "body": "Interruzioni di acqua, gas, riscaldamento o accessi agli alloggi: preavviso almeno 48h, sempre "
                 "tramite ATER, mai direttamente agli inquilini.",
         "keywords": "alloggi abitati, preavviso 48 ore, inquilini tramite ATER, interruzione acqua / gas / "
                     "riscaldamento, accesso agli alloggi, case popolari, mai contatto diretto"},
    ],
    "documents": [
        {"key": "ct3_regole", "where": "project:" + P_TIGLI, "name": "GSE - Regole applicative Conto Termico 3.0",
         "summary": "Regole applicative del GSE del 5/12/2025 per il DM 7/8/2025 (Conto Termico 3.0). "
                    "Descrivono interventi incentivabili, soggetti ammessi, spese ammissibili, condizioni, rate "
                    "di erogazione, accesso diretto e a prenotazione, diagnosi energetica e APE, documentazione "
                    "e casi specifici, tra cui gli edifici degli ex IACP.",
         "url": "https://www.gse.it/servizi-per-te/efficienza-energetica/conto-termico/regole-applicative-ct-3-0",
         "text_file": "conto-termico-3-0-regole-gse",
         "keywords": "regole applicative GSE, Conto Termico 3.0, spese ammissibili, accesso a prenotazione, ex "
                     "IACP / ATER / case popolari, diagnosi energetica / APE, rate incentivo, GSE / Gestore "
                     "servizi energetici"},
    ],
    "notes": [
        {"kind": "fact", "where": "customer", "who": "partner", "section": "profile", "name": "ATER: interlocutori",
         "body": "RUP ing. dell'ufficio tecnico ATER. gestore ACDat ATER separato, molto rigido sui formati. "
                 "inquilini: solo tramite ufficio utenza ATER.",
         "keywords": "ATER / Agenzia Casa Umbria Sud, interlocutori, RUP ufficio tecnico ATER, gestore ACDat "
                     "ATER, rigido sui formati, ufficio utenza, inquilini / case popolari, chi decide"},
        {"kind": "procedure", "where": "project:" + P_TIGLI, "who": "partner", "section": "operations",
         "name": "CT 3.0 prenotazione: passi",
         "keywords": "Conto Termico, GSE, procedura prenotazione Conto Termico, CT 3.0 / Conto Termico 3.0, GSE "
                     "/ Gestore servizi energetici, diagnosi ante firmata, scheda-domanda PortalTermico, "
                     "impegno a preventivo, acconto / rata intermedia / saldo, APE post, decadenza termini",
         "body": "diagnosi ante firmata\nscheda-domanda su PortalTermico con diagnosi allegata\nconferma GSE = "
                 "impegno a preventivo\nacconto all'avvio lavori, intermedia, saldo a fine lavori con APE post\n"
                 "rispettare i termini di avvio/fine sennò decadenza"},
        {"kind": "fact", "where": "project:" + P_TIGLI, "who": "bim", "section": "operations",
         "name": "CI ATER: formati",
         "body": "IFC 4 per i modelli, BCF 2.1 per le issue, PDF/A firmati. nativo non ammesso su ACDat ATER.",
         "keywords": "CI ATER / capitolato informativo, formati di consegna, IFC 4, BCF 2.1 / issue, PDF/A "
                     "firmati, formato nativo non ammesso, ACDat ATER"},
    ],
}

ORGANISATION["documents"].append(
    {"key": "all_ii14", "name": "D.Lgs. 36/2023 All. II.14 - direzione lavori e collaudo",
     "summary": "Allegato II.14 del D.Lgs. 36/2023 (art. 114 c. 5): direzione dei lavori e dell'esecuzione e "
                "collaudo. Definisce compiti del DL e dell'ufficio di DL (attestazione sullo stato dei luoghi, "
                "consegna lavori, accettazione materiali, ordini di servizio comunicati al RUP, controllo del "
                "deposito sismico), contabilità con libretto delle misure, SAL e certificati di pagamento, "
                "varianti, sospensioni, ultimazione, CRE e collaudo.",
     "url": NORMA + "~all.II.14", "text_file": "dlgs-36-2023-allegato-ii14-direzione-lavori-collaudo",
     "keywords": "All. II.14, DL / direttore dei lavori, ordini di servizio / OdS, consegna lavori, libretto "
                 "delle misure / SAL / CdP, sospensioni e varianti, collaudo / CRE / certificato di regolare "
                 "esecuzione, contabilità lavori"})

P_QUERCE = "Condominio Le Querce - cappotto e pompa di calore"

DIAGNOSI_TEXT = (
    "## Diagnosi energetica - Condominio Le Querce (sintesi)\n\n"
    "Edificio del 1978, 18 unità su 6 piani, struttura in c.a. con tamponamenti a cassa vuota non isolati, "
    "copertura piana, centrale termica a metano del 2004 (caldaia 280 kW), contabilizzazione già presente.\n\n"
    "Stato di fatto: APE delle unità tra F e G, EPgl,nren medio 168 kWh/m2 anno. Dispersioni: pareti 41%, "
    "infissi 22%, copertura 14%, ponti termici balconi 11%.\n\n"
    "Scenari:\n"
    "A) cappotto 12 cm + copertura: -38% fabbisogno, costo stimato 610.000 euro.\n"
    "B) A + sistema ibrido (PdC 2x40 kW + caldaia esistente in integrazione): -61%, 760.000 euro.\n"
    "C) A + PdC solo elettrica e radiatori a bassa temperatura sostituiti: -66%, 905.000 euro.\n\n"
    "Consigliato B: i radiatori esistenti lavorano a 55 gradi con l'involucro isolato, la caldaia resta per i "
    "giorni più freddi. Salto atteso di almeno due classi per tutte le unità.\n\n"
    "Detrazioni 2026: 50% per chi ha l'abitazione principale, 36% per gli altri immobili (seconde case, "
    "uffici), sulla quota millesimale. Nel 2027 scendono al 36% e 30%.\n")

QUERCE = {
    "ref": "TA-QUERCE", "name": "Condominio Le Querce", "city": "Terni",
    "projects": [
        {"name": P_QUERCE, "tags": ["condominio", "energia", "detrazioni", "DL"],
         "description": "<p>18 unità, 1978. Cappotto 12 cm, copertura, sistema ibrido PdC + caldaia. Lavori "
                        "760k, detrazioni 2026 50/36%. Noi: diagnosi, progetto, CILA, DL, CSP/CSE, APE post. "
                        "Amministratore: rag. Pieroni.</p>",
         "milestones": [("Delibera assembleare", -150, 148), ("Inizio lavori", -60, 58),
                        ("Fine lavori", 75, None)],
         "tasks": [
             {"name": "Diagnosi energetica e APE ante", "who": "partner", "stage": "Fatto",
              "description": "3 scenari",
              "notes": [("partner", 190, "APE ante F/G, scenario B consigliato"),
                        ("partner", 189, "Sintomo: il condominio vuole sapere quanto consuma l'edificio e quali "
                         "lavori conviene fare. Causa / contesto: diagnosi energetica e APE (attestato di "
                         "prestazione energetica, certificato energetico) ante in classe F/G per l'edificio del "
                         "1978; tre scenari: A cappotto e copertura, B cappotto più sistema ibrido con pompa di "
                         "calore e caldaia esistente, C pompa di calore solo elettrica. Intervento e stato: "
                         "consigliato lo scenario B. Fatto.",
                         ["diagnosi energetica", "APE / attestato di prestazione energetica / classe energetica",
                          "scenari di intervento", "cappotto termico", "sistema ibrido / pompa di calore",
                          "condominio Le Querce", "riqualificazione energetica condominio"])]},
             {"name": "Assemblea di presentazione", "who": "lead", "stage": "Fatto",
              "milestone": "Delibera assembleare",
              "description": "presentare scenari e detrazioni",
              "notes": [("lead", 150, "assemblea lunga. molte domande sulle seconde case (36%). approvato B "
                                      "con 640 millesimi"),
                        ("lead", 148, "verbale arrivato dall'amministratore"),
                        ("lead", 147, "Sintomo: in un'assemblea lunga i condòmini chiedono soprattutto delle "
                         "seconde case e di quanto potranno detrarre. Causa / contesto: assemblea condominiale "
                         "di presentazione degli scenari della diagnosi energetica e delle detrazioni fiscali "
                         "2026: 50% per l'abitazione principale, 36% per seconde case e altri immobili; le "
                         "delibere passano con almeno 500 millesimi. Intervento e stato: approvato lo scenario "
                         "B con 640 millesimi; verbale ricevuto dall'amministratore. Fatto.",
                         ["assemblea condominiale", "delibera / millesimi", "detrazioni fiscali / bonus",
                          "seconde case 36%", "abitazione principale 50%", "scenario B", "verbale assemblea"])]},
             {"name": "Progetto e CILA", "who": "arch", "stage": "Fatto",
              "description": "", "notes": [("arch", 120, "CILA depositata, colore facciata scelto in assemblea "
                                                         "(ocra chiaro)"),
                                           ("arch", 119, "Sintomo: il condominio deve poter avviare i lavori "
                                            "del cappotto e decidere il colore della facciata. Causa / "
                                            "contesto: progetto dell'intervento e CILA (comunicazione di inizio "
                                            "lavori asseverata), il titolo edilizio per la manutenzione "
                                            "straordinaria, depositata in Comune; lo scenario scelto prevede "
                                            "cappotto e pompa di calore ibrida. Intervento e stato: CILA "
                                            "depositata; colore della facciata scelto in assemblea condominiale "
                                            "(ocra chiaro). Fatto.",
                                            ["CILA / comunicazione inizio lavori asseverata", "titolo edilizio",
                                             "progetto cappotto", "colore facciata",
                                             "manutenzione straordinaria", "condominio Le Querce"])]},
             {"name": "Mail amministratore su pagamenti", "who": "lead", "stage": "Fatto",
              "description": "",
              "notes": [("lead", 45, "Pieroni scrive: «i condomini mi chiedono quando arriva il prossimo acconto "
                                     "da pagare alla ditta e se chi ha la seconda casa paga di più. la sig.ra "
                                     "del 4° piano dice che il geometra di suo figlio le ha detto che recupera "
                                     "metà»"),
                        ("lead", 44, "risposto: prossimo SAL a fine novembre, rata da delibera. stessa quota "
                                     "millesimale per tutti, cambia la detrazione (50% abitaz. principale, 36% "
                                     "altri). non diamo consulenza fiscale ai singoli"),
                        ("lead", 43, "Sintomo: l'amministratore scrive che i condòmini chiedono quando arriva "
                         "il prossimo acconto da pagare alla ditta, se chi ha la seconda casa paga di più, e "
                         "una condomina ha sentito che recupera metà. Causa / contesto: pagamenti a SAL (stato "
                         "di avanzamento lavori) con rate da delibera; detrazioni 50% abitazione principale e "
                         "36% altri immobili sulla stessa quota millesimale. Intervento e stato: risposto "
                         "all'amministratore: prossimo SAL a fine novembre, stessa quota millesimale per tutti, "
                         "cambia solo la detrazione; nessuna consulenza fiscale ai singoli. Fatto.",
                         ["SAL / stato avanzamento lavori / acconto", "rate condominiali", "quota millesimale",
                          "detrazione 50% / 36%", "seconda casa", "bonus ristrutturazione",
                          "amministratore di condominio", "consulenza fiscale"])]},
             {"name": "Notifica preliminare e PSC", "who": "lead", "stage": "Fatto", "milestone": "Inizio lavori",
              "description": "2 imprese (edile + termoidraulica) -> notifica",
              "notes": [("lead", 65, "notifica inviata ASL+ITL 6 gg prima della consegna. PSC consegnato"),
                        ("lead", 64, "Sintomo: il cantiere del condominio con due ditte deve partire in regola. "
                         "Causa / contesto: con più imprese (edile e termoidraulica) serve la notifica "
                         "preliminare art. 99 D.Lgs. 81/2008 ad ASL e ITL (Ispettorato territoriale del lavoro) "
                         "e il PSC (piano di sicurezza e coordinamento). Intervento e stato: notifica inviata 6 "
                         "giorni prima della consegna dei lavori, PSC consegnato. Fatto.",
                         ["notifica preliminare art. 99", "ASL / ITL / Ispettorato del lavoro",
                          "PSC / piano di sicurezza e coordinamento", "più imprese in cantiere",
                          "D.Lgs. 81/2008", "apertura cantiere", "condominio Le Querce"])]},
             {"name": "SAL 1", "who": "lead", "stage": "Fatto",
              "description": "ponteggi, rimozioni",
              "notes": [("lead", 30, "SAL 1 ok 148k, CdP emesso. libretto misure firmato in contraddittorio"),
                        ("lead", 29, "Sintomo: l'amministratore deve pagare alla ditta il primo acconto dei "
                         "lavori del condominio, per ponteggi e rimozioni. Causa / contesto: SAL 1 (stato di "
                         "avanzamento lavori) basato sul libretto delle misure firmato in contraddittorio con "
                         "l'impresa; poi CdP (certificato di pagamento) all'amministratore, che chiede la rata "
                         "ai condòmini. Intervento e stato: SAL 1 approvato per 148 mila euro, CdP emesso, "
                         "libretto delle misure firmato. Fatto.",
                         ["SAL / stato avanzamento lavori / acconto", "CdP / certificato di pagamento",
                          "libretto delle misure", "contraddittorio", "ponteggi", "contabilità lavori",
                          "condominio Le Querce"])]},
             {"name": "SAL 2", "who": "lead", "stage": "In corso", "deadline": 28,
              "description": "cappotto facciate nord ed est",
              "notes": [("junior", 6, "misure facciata nord fatte, est da finire giov"),
                        ("lead", 5, "Sintomo: l'amministratore attende il secondo acconto dei lavori, relativo "
                         "al cappotto delle facciate nord ed est. Causa / contesto: SAL 2 (stato di avanzamento "
                         "lavori): il direttore lavori non firma senza libretto delle misure aggiornato e "
                         "controllato in contraddittorio con l'impresa; dopo il SAL si emette il CdP "
                         "(certificato di pagamento). Intervento e stato: misure della facciata nord fatte, "
                         "facciata est da completare giovedì. In corso.",
                         ["SAL / stato avanzamento lavori / acconto", "libretto delle misure",
                          "misure in contraddittorio", "cappotto facciate", "contabilità lavori",
                          "condominio Le Querce"])]},
             {"name": "Pompa di calore: posizione unità esterne", "who": "partner", "stage": "In attesa",
              "description": "in copertura, peso e rumore",
              "notes": [("partner", 20, "verifica solaio copertura per 2 unità da 690 kg: serve telaio di "
                                        "ripartizione su travi"),
                        ("partner", 12, "un condomino dell'ultimo piano teme il rumore, chiesto all'amm. di "
                                        "fargli vedere la scheda dB(A)"),
                        ("partner", 11, "Sintomo: un condomino dell'ultimo piano teme il rumore delle macchine "
                         "sul tetto e il solaio potrebbe non reggerne il peso. Causa / contesto: unità esterne "
                         "della PdC (pompa di calore) in copertura, 2 unità da 690 kg: verifica del solaio di "
                         "copertura, serve un telaio di ripartizione sulle travi; rumore in dB(A) dalla scheda "
                         "tecnica. Intervento e stato: chiesto all'amministratore di mostrare la scheda dB(A) "
                         "al condomino. In attesa.",
                         ["PdC / pompa di calore", "unità esterne in copertura", "verifica solaio",
                          "telaio di ripartizione", "rumore dB(A)", "peso macchine", "condominio Le Querce"])]},
             {"name": "APE post e asseverazioni", "who": "partner", "stage": "Da fare",
              "milestone": "Fine lavori", "deadline": 80, "description": "APE post per ogni unità",
              "notes": [("partner", 1, "Sintomo: a fine lavori ogni proprietario del condominio avrà bisogno "
                         "del nuovo certificato energetico, anche per le detrazioni. Causa / contesto: APE "
                         "(attestato di prestazione energetica, classe energetica) post intervento per ognuna "
                         "delle unità immobiliari e asseverazioni tecniche dei lavori; la diagnosi prevede un "
                         "salto di almeno due classi. Intervento e stato: attività da fare a fine lavori. Da "
                         "fare.",
                         ["APE post / attestato di prestazione energetica", "certificato energetico",
                          "classe energetica", "asseverazioni", "unità immobiliari", "fine lavori",
                          "condominio Le Querce"])]},
         ],
         "updates": [
             ("Lavori avviati", "on_track", 35, 55, "consegna lavori fatta, ponteggi montati, SAL 1 a fine mese."),
             ("Ottobre", "on_track", 50, 5, "SAL 1 ok, SAL 2 in misura. PdC in copertura: serve telaio."),
         ]},
    ],
    "rules": [
        {"name": "Con i condòmini parla l'amministratore", "where": "customer", "who": "lead", "state": "active",
         "severity": "must", "activities": ["communication"], "section": "operations",
         "body": "Domande dei singoli condòmini su spese, rate e detrazioni: si risponde all'amministratore, per "
                 "scritto. Niente consulenza fiscale ai singoli.",
         "keywords": "condòmini, amministratore di condominio, risposta scritta, spese e rate, detrazioni, "
                     "niente consulenza fiscale ai singoli, condominio Le Querce"},
    ],
    "documents": [
        {"key": "diagnosi_querce", "where": "project:" + P_QUERCE, "name": "Diagnosi energetica Condominio Le Querce",
         "summary": "Sintesi della diagnosi energetica del condominio Le Querce: edificio del 1978, 18 unità su "
                    "6 piani, APE tra F e G, EPgl,nren medio 168 kWh/m2 anno, dispersioni soprattutto dalle "
                    "pareti (41%). Tre scenari: A cappotto e copertura (610 mila euro, -38%), B con sistema "
                    "ibrido PdC 2x40 kW e caldaia (760 mila, -61%, consigliato), C PdC solo elettrica (905 "
                    "mila, -66%); detrazioni 2026 50%/36%, 2027 36%/30%.",
         "url": "https://cloud.trearchi.example/commesse/querce/diagnosi-energetica", "keep_text": True,
         "text": DIAGNOSI_TEXT,
         "keywords": "diagnosi energetica, condominio Le Querce, APE / classe energetica, EPgl,nren, "
                     "dispersioni termiche, scenari cappotto / ibrido / pompa di calore, sistema ibrido, "
                     "detrazioni 50% / 36%"},
    ],
    "notes": [
        {"kind": "fact", "where": "customer", "who": "lead", "section": "profile", "name": "Le Querce: chi decide",
         "body": "amministratore rag. Pieroni, consiglieri 3. delibere a maggioranza con 500+ millesimi. paga "
                 "le imprese con rate da delibera, i nostri onorari a SAL.",
         "keywords": "condominio Le Querce, amministratore di condominio, consiglieri, delibere 500 millesimi, "
                     "maggioranza assembleare, rate da delibera, onorari a SAL, chi decide"},
        {"kind": "fact", "where": "project:" + P_QUERCE, "who": "partner", "section": "operations",
         "name": "Le Querce: impianto",
         "body": "ibrido: 2 PdC 40 kW in copertura + caldaia esistente in integrazione sotto 2 gradi esterni. "
                 "radiatori esistenti a 55 gradi. telaio di ripartizione in copertura.",
         "keywords": "condominio Le Querce, impianto ibrido, PdC / pompa di calore 2 x 40 kW, caldaia in "
                     "integrazione, radiatori a 55 gradi, telaio di ripartizione copertura, centrale termica "
                     "condominiale"},
        {"kind": "procedure", "where": "customer", "who": "lead", "section": "operations",
         "name": "SAL condominio",
         "body": "misure in contraddittorio con l'impresa -> libretto -> SAL -> CdP all'amministratore -> "
                 "l'amm. chiede la rata ai condòmini -> bonifico parlante per detrazioni",
         "keywords": "procedura SAL condominio, SAL / stato avanzamento lavori / acconto, misure in "
                     "contraddittorio, libretto delle misure, CdP / certificato di pagamento, rata condòmini, "
                     "bonifico parlante, detrazioni fiscali"},
    ],
}

P_CASALE = "Casale Moretti - restauro e ampliamento"

MORETTI = {
    "ref": "TA-MORETTI", "name": "Moretti Giovanni", "city": "Montecastrilli",
    "projects": [
        {"name": P_CASALE, "tags": ["restauro", "paesaggio", "privati", "sismica"],
         "description": "<p>Casa colonica in pietra in area con vincolo paesaggistico. Restauro, miglioramento "
                        "sismico, piccolo ampliamento. Diventerà abitazione principale del cliente.</p>",
         "milestones": [("Autorizzazione paesaggistica", 50, None), ("Permesso di costruire", 120, None)],
         "tasks": [
             {"name": "Rilievo e stato di fatto", "who": "arch", "stage": "Fatto",
              "description": "", "notes": [("arch", 140, "rilievo fatto, quadro fessurativo cantonale NE"),
                                           ("arch", 139, "Sintomo: il proprietario vuole restaurare e ampliare "
                                            "il suo casale e serve conoscere con precisione lo stato attuale "
                                            "dell'edificio. Causa / contesto: rilievo geometrico e stato di "
                                            "fatto del casale in muratura di pietra, edificio soggetto a "
                                            "vincolo paesaggistico; il quadro fessurativo (crepe e lesioni nei "
                                            "muri) è concentrato sul cantonale nord-est ed è il dato di "
                                            "partenza per il progetto di miglioramento sismico. Intervento e "
                                            "stato: rilievo completato. Fatto.",
                                            ["rilievo", "stato di fatto", "quadro fessurativo / crepe",
                                             "cantonale", "casale in pietra", "restauro", "Casale Moretti"])]},
             {"name": "Relazione paesaggistica e istanza", "who": "arch", "stage": "In attesa",
              "milestone": "Autorizzazione paesaggistica",
              "description": "autorizzazione ordinaria, parere Soprintendenza",
              "notes": [("arch", 80, "istanza depositata al Comune"),
                        ("arch", 35, "integrazioni Soprintendenza: coppi di recupero non nuovi anticati, "
                                     "infissi legno senza oscuranti esterni, ampliamento più basso di 60 cm"),
                        ("arch", 34, "Sintomo: per il casale in zona tutelata serve il permesso paesaggistico e "
                         "la Soprintendenza chiede modifiche. Causa / contesto: relazione paesaggistica e "
                         "istanza di autorizzazione paesaggistica ordinaria con parere della Soprintendenza; "
                         "integrazioni richieste: coppi di recupero e non nuovi anticati, infissi in legno "
                         "senza oscuranti esterni, ampliamento più basso di 60 cm. Intervento e stato: istanza "
                         "depositata al Comune; si attende dopo le integrazioni. In attesa.",
                         ["relazione paesaggistica", "autorizzazione paesaggistica ordinaria",
                          "vincolo paesaggistico", "Soprintendenza", "integrazioni", "coppi di recupero",
                          "infissi in legno", "Casale Moretti"])]},
             {"name": "Ampliamento rivisto", "who": "arch", "stage": "In corso",
              "description": "abbassare 60 cm, falda unica",
              "notes": [("arch", 25, "nuove tavole, il cliente non è contento ma accetta"),
                        ("arch", 24, "Sintomo: il proprietario del casale deve accettare un ampliamento più "
                         "basso di quello progettato, e non ne è contento. Causa / contesto: revisione del "
                         "progetto di ampliamento secondo le prescrizioni della Soprintendenza "
                         "nell'autorizzazione paesaggistica: abbassamento di 60 cm e copertura a falda unica. "
                         "Intervento e stato: nuove tavole di progetto preparate; il cliente non è soddisfatto "
                         "ma accetta la soluzione. In corso.",
                         ["ampliamento", "prescrizioni Soprintendenza", "abbassamento 60 cm", "falda unica",
                          "nuove tavole", "vincolo paesaggistico", "Casale Moretti"])]},
             {"name": "Miglioramento sismico muratura", "who": "lead", "stage": "In corso",
              "description": "cuci-scuci, catene, solai in legno irrigiditi",
              "notes": [("lead", 40, "niente cordoli in c.a. in sommità (Soprintendenza non li vuole), "
                                     "cordolo in muratura armata"),
                        ("lead", 39, "Sintomo: il proprietario vuole il casale più sicuro in caso di terremoto, "
                         "ma la tutela limita le tecniche ammesse. Causa / contesto: miglioramento sismico "
                         "della muratura con cuci-scuci, catene e solai in legno irrigiditi; la Soprintendenza "
                         "non vuole cordoli in c.a. (cemento armato) in sommità ai muri. Intervento e stato: "
                         "previsto un cordolo in muratura armata al posto del cordolo in c.a. In corso.",
                         ["miglioramento sismico", "muratura", "cuci-scuci", "catene",
                          "solai in legno irrigiditi", "cordolo in muratura armata", "cordolo in c.a.",
                          "Casale Moretti"])]},
             {"name": "Domanda del cliente sui bonus", "who": "lead", "stage": "Fatto",
              "description": "",
              "notes": [("lead", 60, "Moretti: «il geometra del paese dice che con il bonus lo Stato mi ridà "
                                     "metà di quello che spendo, è vero anche se ci vado a vivere dopo?»"),
                        ("lead", 59, "risposto: 50% se diventa abitazione principale (regole 2026), 36% "
                                     "altrimenti; dal 2027 36/30. chiedere al commercialista per i tempi del "
                                     "trasferimento residenza"),
                        ("lead", 58, "Sintomo: il proprietario chiede se è vero che con il bonus lo Stato gli "
                         "ridà metà della spesa, anche se ci andrà a vivere dopo. Causa / contesto: detrazioni "
                         "edilizie 2026: 50% se l'immobile diventa abitazione principale, 36% altrimenti; dal "
                         "2027 36% e 30%. Intervento e stato: risposto con le regole 2026-2027 e indicato di "
                         "chiedere al commercialista per i tempi del trasferimento di residenza. Fatto.",
                         ["bonus ristrutturazione", "detrazione 50% / 36%", "abitazione principale",
                          "trasferimento residenza", "detrazioni 2027", "commercialista", "Casale Moretti"])]},
             {"name": "Preventivi imprese", "who": "arch", "stage": "Da fare", "deadline": 100,
              "description": "3 imprese con esperienza su pietra",
              "notes": [("arch", 1, "Sintomo: il proprietario deve scegliere l'impresa a cui affidare il "
                         "restauro del casale. Causa / contesto: raccolta e confronto di preventivi da 3 "
                         "imprese con esperienza su murature in pietra, per lavori di restauro, ampliamento e "
                         "miglioramento sismico con cuci-scuci, catene e prescrizioni della Soprintendenza "
                         "(coppi di recupero, intonaci a calce). Intervento e stato: richiesta dei preventivi "
                         "da fare. Da fare.",
                         ["preventivi imprese", "scelta impresa", "confronto offerte", "muratura in pietra",
                          "restauro", "Casale Moretti"])]},
             {"name": "Contratto d'incarico", "who": "office", "stage": "Fatto",
              "description": "", "notes": [("office", 150, "firmato, acconto ricevuto"),
                                           ("office", 149, "Sintomo: l'incarico con il proprietario del casale "
                                            "va formalizzato prima di iniziare la progettazione del restauro. "
                                            "Causa / contesto: contratto d'incarico professionale (lettera "
                                            "d'incarico) con committente privato per restauro e ampliamento del "
                                            "casale, con acconto sugli onorari; il documento è conservato in "
                                            "memoria senza testo perché contiene dati anagrafici, compensi e "
                                            "modalità di pagamento. Intervento e stato: contratto firmato e "
                                            "acconto ricevuto. Fatto.",
                                            ["contratto d'incarico", "incarico professionale", "acconto onorari",
                                             "lettera d'incarico", "committente privato", "Casale Moretti"])]},
         ],
         "updates": [("Ottobre", "at_risk", 30, 14,
                      "integrazioni Soprintendenza: ampliamento abbassato, coppi di recupero. tempi slittano.")]},
    ],
    "rules": [],
    "documents": [
        {"key": "contratto_moretti", "where": "customer", "name": "Contratto d'incarico Moretti",
         "summary": "Contratto d'incarico professionale firmato con il proprietario del Casale Moretti per "
                    "restauro e ampliamento. Il testo non è conservato perché contiene dati anagrafici, "
                    "compensi e modalità di pagamento.",
         "url": "https://cloud.trearchi.example/commesse/moretti/contratto", "keep_text": False,
         "text": "Testo non salvato: contratto con dati anagrafici, compensi e modalità di pagamento.",
         "keywords": "contratto d'incarico, Casale Moretti, incarico professionale, lettera d'incarico, "
                     "committente privato, documento riservato / dati personali"},
    ],
    "notes": [
        {"kind": "fact", "where": "project:" + P_CASALE, "who": "arch", "section": "operations",
         "name": "Casale: prescrizioni Soprintendenza",
         "keywords": "vincolo paesaggistico, Casale Moretti, prescrizioni Soprintendenza, coppi di recupero, "
                     "infissi in legno senza persiane, ampliamento -60 cm falda unica, intonaci a calce, niente "
                     "cordoli in c.a.",
         "body": "coppi di recupero, infissi legno senza persiane esterne, ampliamento -60 cm falda unica, "
                 "intonaci a calce, niente cordoli c.a."},
    ],
}

P_CAPANNONE = "Nuovo capannone produzione - DL e CSE"
P_T50 = "Transizione 5.0 - perizie e certificazioni"

SAL_TEXT = (
    "## Stato di avanzamento lavori n. 3 - Nuovo capannone produzione\n\n"
    "Contratto a corpo e misura, importo contrattuale 1.380.000,00 euro. Ritenuta di garanzia 5% da contratto.\n\n"
    "| Voce | Importo a tutto il SAL 3 (euro) |\n|---|---|\n"
    "| Scavi e fondazioni | 182.300,00 |\n| Struttura prefabbricata (pilastri, travi, tegoli) | 318.600,00 |\n"
    "| Pannelli di tamponamento (parziale) | 74.500,00 |\n| Reti interrate | 37.000,00 |\n"
    "| Totale lavori a tutto il SAL 3 | 612.400,00 |\n\n"
    "A dedurre SAL precedenti: 418.900,00. Importo del SAL 3: 193.500,00. Ritenuta 5%: 9.675,00. Certificato "
    "di pagamento: 183.825,00 euro oltre IVA.\n\n"
    "Non contabilizzati: scavo in roccia zona vasca antincendio richiesto dall'impresa (47.600,00): lavorazione "
    "non prevista, serve nuovo prezzo e variante approvata dal committente. L'impresa firma con riserva.\n")

MECNERA = {
    "ref": "TA-MECNERA", "name": "Meccanica Nera srl", "city": "Terni",
    "projects": [
        {"name": P_CAPANNONE, "tags": ["industriale", "DL", "sicurezza", "cantiere"],
         "description": "<p>Capannone prefabbricato 2.400 m2 + soppalco uffici. Progetto nostro, DL Andrea, CSP "
                        "Andrea, CSE Lorenzo. Lavori 1,38 mln a corpo e misura, 3 imprese + subappalti. Il "
                        "titolare vuole il capannone pronto per la linea nuova a marzo.</p>",
         "milestones": [("Consegna lavori", -175, 171), ("Struttura completata", -20, None),
                        ("Ultimazione", 130, None), ("Collaudo statico", 180, None)],
         "tasks": [
             {"name": "Progetto strutturale e deposito sismico", "who": "lead", "stage": "Fatto",
              "description": "prefabbricato + fondazioni a plinti, deposito alla Regione",
              "notes": [("lead", 230, "deposito sismico fatto, autorizzazione ok"),
                        ("lead", 229, "Sintomo: il titolare dell'azienda deve poter costruire il nuovo "
                         "capannone di produzione in tempo per la nuova linea. Causa / contesto: progetto "
                         "strutturale di capannone prefabbricato con fondazioni a plinti e deposito sismico "
                         "(pratica di autorizzazione sismica) presso la Regione; il direttore lavori deve "
                         "accertare deposito e autorizzazione prima dell'inizio dei lavori. Intervento e stato: "
                         "deposito sismico presentato, autorizzazione ottenuta. Fatto.",
                         ["progetto strutturale", "deposito sismico", "autorizzazione sismica",
                          "capannone prefabbricato", "fondazioni a plinti", "Regione", "Meccanica Nera"])]},
             {"name": "Notifica preliminare", "who": "partner", "stage": "Fatto", "milestone": "Consegna lavori",
              "description": "3 imprese -> notifica art. 99 prima dei lavori",
              "notes": [("partner", 176, "l'impresa ha montato recinzione e baracche lun senza dircelo. "
                                         "notifica NON ancora inviata (la aspettavamo con il POS del sub)"),
                        ("partner", 175, "notifica inviata oggi a ASL e ITL, 4 gg dopo l'allestimento. fermato "
                                         "tutto fino all'invio, ordine al capocantiere"),
                        ("lead", 174, "spiegato al titolare perché abbiamo fermato 2 gg. regola ribadita"),
                        ("partner", 173, "Sintomo: l'impresa ha montato recinzione e baracche senza avvisare e "
                         "il cantiere è stato fermato due giorni. Causa / contesto: con 3 imprese serve la "
                         "notifica preliminare art. 99 D.Lgs. 81/2008 ad ASL e ITL prima dell'inizio dei "
                         "lavori; si aspettava il POS (piano operativo di sicurezza) del subappaltatore; "
                         "l'allestimento conta come inizio lavori. Intervento e stato: notifica inviata 4 "
                         "giorni dopo l'allestimento, lavori fermati fino all'invio con ordine al capocantiere; "
                         "spiegato al titolare. Fatto.",
                         ["notifica preliminare art. 99", "allestimento cantiere / inizio lavori",
                          "recinzione e baracche", "fermo cantiere", "ASL / ITL",
                          "POS / piano operativo di sicurezza", "CSE / coordinatore sicurezza in esecuzione",
                          "Meccanica Nera"])]},
             {"name": "PSC e POS", "who": "lead", "stage": "Fatto",
              "description": "PSC rev.2 dopo cambio prefabbricatore",
              "notes": [("lead", 185, "PSC rev.2 inviato al CSE: montaggio con autogru 2, area stoccaggio "
                                      "tegoli spostata"),
                        ("partner", 172, "POS edile e prefabbricatore ok. POS impianti elettrici manca"),
                        ("lead", 171, "Sintomo: aggiornare i piani di sicurezza del capannone dopo il cambio "
                         "del fornitore del prefabbricato. Causa / contesto: PSC (piano di sicurezza e "
                         "coordinamento) rev. 2 e verifica dei POS (piani operativi di sicurezza) delle "
                         "imprese. Intervento e stato: PSC rev. 2 inviato con montaggio da 2 autogru e area di "
                         "stoccaggio dei tegoli spostata; POS edile e prefabbricatore accettati, manca quello "
                         "degli impianti elettrici. Fatto.",
                         ["PSC / piano di sicurezza e coordinamento", "POS / piano operativo di sicurezza",
                          "prefabbricatore", "autogru", "stoccaggio tegoli", "verifica POS", "Meccanica Nera"])]},
             {"name": "Verbale consegna lavori", "who": "lead", "stage": "Fatto", "milestone": "Consegna lavori",
              "description": "",
              "notes": [("lead", 171, "verbale consegna parziale: area capannone sì, piazzale no (ancora "
                                      "deposito materiali del vecchio reparto)"),
                        ("lead", 170, "Sintomo: l'impresa può iniziare solo su una parte dell'area perché il "
                         "piazzale è ancora occupato dai materiali dell'azienda. Causa / contesto: verbale di "
                         "consegna lavori del DL (direttore dei lavori), redatto solo dopo notifica "
                         "preliminare, PSC e POS: area del capannone consegnata, piazzale no per il deposito "
                         "materiali del vecchio reparto. Intervento e stato: verbale di consegna parziale "
                         "redatto. Fatto.",
                         ["verbale consegna lavori", "consegna parziale", "DL / direttore dei lavori",
                          "piazzale occupato", "inizio lavori", "Meccanica Nera"])]},
             {"name": "Subappalto impianti: documenti", "who": "partner", "stage": "In corso",
              "description": "manca DURC sub, POS sub",
              "notes": [("partner", 40, "manca DURC sub elettrico, POS ok. non entra finché non arriva"),
                        ("partner", 33, "DURC arrivato, sub ammesso in cantiere"),
                        ("partner", 32, "Sintomo: il subappaltatore degli impianti elettrici voleva entrare in "
                         "cantiere senza documenti completi. Causa / contesto: ammissione del subappalto: "
                         "servono DURC (documento unico di regolarità contributiva) e POS (piano operativo di "
                         "sicurezza) del subappaltatore; nessuna impresa entra prima che i documenti siano "
                         "verificati. Intervento e stato: POS ok, DURC mancante e accesso negato finché non è "
                         "arrivato; ora DURC ricevuto e sub ammesso in cantiere. In corso.",
                         ["subappalto impianti", "DURC / regolarità contributiva",
                          "POS / piano operativo di sicurezza", "ammissione subappaltatore", "accesso cantiere",
                          "impianti elettrici", "Meccanica Nera"])]},
             {"name": "SAL 1 e 2", "who": "lead", "stage": "Fatto", "description": "",
              "notes": [("lead", 120, "SAL 1 ok, CdP emesso"), ("lead", 70, "SAL 2 ok, CdP emesso"),
                        ("lead", 69, "Sintomo: l'impresa del capannone deve ricevere i primi due acconti sui "
                         "lavori eseguiti. Causa / contesto: SAL 1 e SAL 2 (stati di avanzamento lavori) del "
                         "contratto a corpo e misura, con ritenuta di garanzia del 5%, e relativi CdP "
                         "(certificati di pagamento) emessi dal DL (direttore dei lavori) sulla base del "
                         "libretto delle misure. Intervento e stato: SAL 1 e SAL 2 approvati, CdP emessi. "
                         "Fatto.",
                         ["SAL / stato avanzamento lavori / acconto", "CdP / certificato di pagamento",
                          "contabilità lavori", "DL / direttore dei lavori", "capannone", "Meccanica Nera"])]},
             {"name": "SAL 3 contestato", "who": "lead", "stage": "In corso",
              "description": "impresa chiede 241k, DL contabilizza 193,5k",
              "notes": [("lead", 16, "impresa vuole nel SAL 3 lo scavo in roccia vasca antincendio (47,6k) a "
                                     "prezzo loro. non è in contratto: niente NP, niente variante approvata"),
                        ("lead", 14, "SAL 3 emesso a 193.500, CdP 183.825. l'impresa firma il registro con "
                                     "riserva"),
                        ("lead", 9, "riserva esplicata entro 15 gg come da contratto. proposto NP.07 con "
                                    "analisi prezzi al titolare"),
                        ("lead", 8, "Sintomo: l'impresa chiede 241 mila euro nel terzo acconto, il direttore "
                         "lavori ne riconosce 193,5. Causa / contesto: l'impresa vuole lo scavo in roccia della "
                         "vasca antincendio (47,6 mila) a prezzo proprio; non è in contratto, manca NP (nuovo "
                         "prezzo) e variante approvata. Intervento e stato: SAL 3 (stato avanzamento lavori) "
                         "emesso a 193.500, CdP (certificato di pagamento) 183.825 con ritenuta 5%; l'impresa "
                         "firma il registro di contabilità con riserva, esplicata entro 15 giorni; proposto al "
                         "titolare il NP.07 con analisi prezzi. In corso.",
                         ["SAL contestato / stato avanzamento lavori", "CdP / certificato di pagamento",
                          "riserva dell'impresa", "scavo in roccia", "NP / nuovo prezzo",
                          "registro di contabilità", "ritenuta di garanzia 5%", "vasca antincendio"])],
              "worklog": [("lead", 14, 5.0, "contabilità SAL 3 e libretto misure")]},
             {"name": "Variante scavo in roccia", "who": "lead", "stage": "In attesa",
              "description": "perizia di variante, NP.07",
              "notes": [("lead", 8, "perizia di variante + NP.07 a 31 euro/m3, inviata al titolare per ok scritto"),
                        ("lead", 7, "Sintomo: l'impresa vuole essere pagata per lo scavo in roccia non previsto "
                         "della vasca antincendio e ha firmato il SAL con riserva. Causa / contesto: perizia di "
                         "variante con NP.07 (nuovo prezzo) a 31 euro/m3, con analisi prezzi; per regola "
                         "nessuna lavorazione extra si contabilizza senza approvazione scritta del titolare e "
                         "perizia del DL. Intervento e stato: perizia e nuovo prezzo inviati al titolare per "
                         "l'ok scritto. In attesa.",
                         ["perizia di variante", "NP.07 / nuovo prezzo", "scavo in roccia",
                          "approvazione scritta committente", "lavori extra / lavorazione imprevista",
                          "analisi prezzi", "Meccanica Nera"])]},
             {"name": "Ordini di servizio", "who": "lead", "stage": "In corso",
              "description": "registro OdS",
              "notes": [("lead", 95, "OdS 4: niente getti con temperatura sotto 5 gradi o pioggia battente"),
                        ("lead", 50, "OdS 6: ripristino copriferro plinto P12 prima del montaggio"),
                        ("lead", 49, "Sintomo: il direttore lavori deve dare all'impresa disposizioni "
                         "vincolanti su getti e riparazioni del calcestruzzo. Causa / contesto: registro degli "
                         "OdS (ordini di servizio) del DL (direttore dei lavori), comunicati al RUP o al "
                         "committente e annotati nella contabilità. Intervento e stato: OdS 4: niente getti con "
                         "temperatura sotto 5 gradi o con pioggia battente; OdS 6: ripristino del copriferro "
                         "del plinto P12 prima del montaggio della struttura. In corso.",
                         ["OdS / ordini di servizio", "registro ordini di servizio", "getti calcestruzzo",
                          "basse temperature / pioggia", "copriferro", "plinto", "DL / direttore dei lavori"])]},
             {"name": "Mail del titolare sui tempi", "who": "lead", "stage": "Fatto",
              "description": "",
              "notes": [("lead", 26, "il titolare: «Ingegnere, la linea nuova arriva il 15 marzo, io il "
                                     "capannone lo devo avere chiuso e con la corrente. Se l'impresa ritarda chi "
                                     "paga?» risposto: penali da contratto 0,5 per mille al giorno, cronoprogramma "
                                     "aggiornato venerdì"),
                        ("lead", 25, "Sintomo: il titolare scrive che la linea nuova arriva il 15 marzo, il "
                         "capannone deve essere chiuso e con la corrente, e chiede chi paga se l'impresa "
                         "ritarda. Causa / contesto: contratto d'appalto con penali per ritardo dello 0,5 per "
                         "mille al giorno e cronoprogramma dei lavori. Intervento e stato: risposto citando le "
                         "penali da contratto e il cronoprogramma aggiornato venerdì. Fatto.",
                         ["penali ritardo", "0,5 per mille al giorno", "cronoprogramma", "tempi di consegna",
                          "termine ultimazione", "contratto d'appalto", "Meccanica Nera"])]},
             {"name": "Sospensione parziale pannelli", "who": "lead", "stage": "Fatto",
              "description": "",
              "notes": [("lead", 60, "verbale di sospensione parziale: pannelli in ritardo dal fornitore, 10 gg"),
                        ("lead", 50, "verbale di ripresa. termine di ultimazione spostato di 10 gg"),
                        ("lead", 49, "Sintomo: i pannelli di tamponamento del capannone arrivano in ritardo dal "
                         "fornitore e i lavori non possono proseguire. Causa / contesto: verbale di sospensione "
                         "parziale dei lavori di 10 giorni redatto dal DL (direttore dei lavori) e successivo "
                         "verbale di ripresa, con effetto sul termine contrattuale di ultimazione previsto a "
                         "marzo. Intervento e stato: lavori ripresi, termine di ultimazione spostato di 10 "
                         "giorni. Fatto.",
                         ["sospensione parziale lavori", "verbale di sospensione", "verbale di ripresa",
                          "proroga / termine ultimazione", "pannelli in ritardo", "fornitore", "Meccanica Nera"])]},
             {"name": "Collaudo statico", "who": "lead", "stage": "Da fare", "milestone": "Collaudo statico",
              "description": "collaudatore nominato dal committente. prova di carico soppalco",
              "attachment": "stage_report",
              "notes": [("lead", 5, "prova di carico soppalco fatta, verbale allegato. esito ok"),
                        ("lead", 4, "Sintomo: il capannone deve essere collaudato prima di poter essere usato. "
                         "Causa / contesto: collaudo statico affidato al collaudatore nominato dal committente, "
                         "con prova di carico sul soppalco; è uno dei passi di chiusura lavori dopo certificato "
                         "di ultimazione e conto finale, prima dell'agibilità (SCA). Intervento e stato: prova "
                         "di carico del soppalco eseguita, verbale allegato, esito positivo; task ancora "
                         "aperto. Da fare.",
                         ["collaudo statico", "collaudatore", "prova di carico", "soppalco", "verbale di prova",
                          "chiusura lavori", "Meccanica Nera"])]},
         ],
         "updates": [
             ("Struttura", "on_track", 45, 40, "struttura montata, SAL 2 ok, sub elettrico ammesso."),
             ("Ottobre", "at_risk", 55, 7,
              "SAL 3 con riserva dell'impresa (scavo in roccia), variante in attesa del titolare. pannelli finiti."),
         ]},
        {"name": P_T50, "tags": ["industria 5.0", "energia"],
         "description": "<p>Supporto alla pratica Transizione 5.0 sugli investimenti 2025: certificazione del "
                        "risparmio energetico ex ante ed ex post, FV in autoconsumo, perizia beni 4.0.</p>",
         "milestones": [("Certificazione ex post", 40, None)],
         "tasks": [
             {"name": "Certificazione ex ante risparmio", "who": "partner", "stage": "Fatto",
              "description": "", "notes": [("partner", 300, "risparmio struttura produttiva 6,8%, fascia sopra 5%"),
                                           ("partner", 299, "Sintomo: l'azienda vuole l'agevolazione fiscale "
                                            "per i nuovi investimenti che riducono i consumi. Causa / contesto: "
                                            "certificazione ex ante del risparmio energetico per Transizione "
                                            "5.0, che determina la fascia di credito d'imposta: riduzione dei "
                                            "consumi della struttura produttiva del 6,8%, nella fascia sopra il "
                                            "5%. Intervento e stato: certificazione ex ante completata; seguirà "
                                            "la certificazione ex post dopo 12 mesi di misure. Fatto.",
                                            ["Transizione 5.0", "certificazione ex ante",
                                             "risparmio energetico 6,8%", "fascia di risparmio",
                                             "credito d'imposta", "struttura produttiva", "Meccanica Nera"])]},
             {"name": "FV 300 kWp in autoconsumo", "who": "partner", "stage": "Fatto",
              "description": "moduli con requisiti di origine", "notes": [("partner", 260, "collaudato"),
                                                                          ("partner", 259, "Sintomo: l'azienda "
                                                                           "installa un impianto solare per "
                                                                           "coprire con energia propria i "
                                                                           "consumi elettrici della produzione "
                                                                           "e ridurre la bolletta. Causa / "
                                                                           "contesto: impianto FV "
                                                                           "(fotovoltaico) da 300 kWp in "
                                                                           "autoconsumo, parte del pacchetto di "
                                                                           "investimenti agevolati con "
                                                                           "Transizione 5.0 e il relativo "
                                                                           "credito d'imposta; per accedere "
                                                                           "all'agevolazione i moduli devono "
                                                                           "rispettare i requisiti di origine "
                                                                           "richiesti dalla misura. Intervento "
                                                                           "e stato: impianto realizzato e "
                                                                           "collaudato. Fatto.",
                                                                           ["FV / fotovoltaico", "300 kWp",
                                                                            "autoconsumo",
                                                                            "requisiti di origine moduli",
                                                                            "Transizione 5.0",
                                                                            "collaudo impianto",
                                                                            "Meccanica Nera"])]},
             {"name": "Perizia interconnessione beni 4.0", "who": "junior", "stage": "In corso",
              "description": "2 centri di lavoro + MES",
              "notes": [("junior", 15, "manca la prova dell'interconnessione col MES del secondo centro"),
                        ("junior", 14, "Sintomo: per l'agevolazione sui nuovi macchinari serve dimostrare che "
                         "sono collegati al sistema informatico di fabbrica. Causa / contesto: perizia di "
                         "interconnessione dei beni 4.0 per Transizione 5.0: 2 centri di lavoro e MES (sistema "
                         "di gestione della produzione); manca ancora la prova dell'interconnessione del "
                         "secondo centro di lavoro con il MES. Intervento e stato: perizia in attesa della "
                         "prova. In corso.",
                         ["perizia interconnessione", "beni 4.0 / Industria 4.0",
                          "MES / sistema gestione produzione", "centri di lavoro", "Transizione 5.0",
                          "credito d'imposta", "Meccanica Nera"])]},
             {"name": "Certificazione ex post", "who": "partner", "stage": "Da fare",
              "milestone": "Certificazione ex post", "deadline": 40, "description": "misure dei consumi 12 mesi",
              "notes": [("partner", 3, "il titolare: «a me interessa solo sapere quanto credito d'imposta "
                                       "prendo e quando»"),
                        ("partner", 2, "Sintomo: il titolare dice che gli interessa solo sapere quanto credito "
                         "d'imposta prende e quando. Causa / contesto: certificazione ex post di Transizione "
                         "5.0, basata sulle misure dei consumi energetici per 12 mesi dopo l'investimento, che "
                         "conferma il risparmio dichiarato nella certificazione ex ante (6,8%). Intervento e "
                         "stato: certificazione da fare al termine dei 12 mesi di misure. Da fare.",
                         ["certificazione ex post", "Transizione 5.0", "credito d'imposta",
                          "misure consumi 12 mesi", "risparmio energetico", "Meccanica Nera"])]},
         ],
         "updates": [("Ottobre", "on_track", 70, 15, "ex ante ok, FV collaudato, perizia 4.0 in corso.")]},
    ],
    "rules": [
        {"name": "Varianti solo con ok scritto del titolare", "where": "customer", "who": "lead", "state": "active",
         "severity": "never", "activities": [], "section": "operations",
         "body": "Nessuna lavorazione extra o nuovo prezzo si contabilizza senza approvazione scritta del "
                 "titolare (mail va bene) e perizia del DL.",
         "keywords": "varianti / perizia di variante, nuovo prezzo / NP, lavorazioni extra, ok scritto del "
                     "titolare, approvazione committente via mail, contabilizzazione, Meccanica Nera"},
    ],
    "documents": [
        {"key": "sal3_capannone", "where": "task:" + P_CAPANNONE + "/SAL 3 contestato",
         "name": "SAL 3 capannone - stato avanzamento e certificato di pagamento",
         "summary": "Stato di avanzamento lavori n. 3 del nuovo capannone di Meccanica Nera, contratto a corpo "
                    "e misura da 1.380.000 euro con ritenuta del 5%. Lavori a tutto il SAL 3 612.400 euro, meno "
                    "SAL precedenti 418.900: SAL 3 193.500 euro, ritenuta 9.675, certificato di pagamento "
                    "183.825 euro oltre IVA. Escluso lo scavo in roccia della vasca antincendio (47.600 euro) "
                    "senza nuovo prezzo e variante; l'impresa firma con riserva.",
         "url": "https://cloud.trearchi.example/commesse/meccanica-nera/sal-3", "keep_text": True,
         "text": SAL_TEXT,
         "keywords": "SAL 3 / stato avanzamento lavori, CdP / certificato di pagamento, ritenuta di garanzia "
                     "5%, contratto a corpo e misura, scavo in roccia escluso, riserva dell'impresa, nuovo "
                     "prezzo / variante, capannone Meccanica Nera"},
    ],
    "notes": [
        {"kind": "fact", "where": "customer", "who": "lead", "section": "profile", "name": "Meccanica Nera: chi decide",
         "body": "decide tutto il titolare, risponde solo al telefono la sera. RSPP interno per le interferenze "
                 "con il reparto vecchio in funzione.",
         "keywords": "Meccanica Nera, titolare / chi decide, contatto telefonico serale, RSPP / responsabile "
                     "servizio prevenzione e protezione, interferenze reparto in funzione, committente privato "
                     "industriale"},
        {"kind": "fact", "where": "project:" + P_CAPANNONE, "who": "lead", "section": "operations",
         "name": "Capannone: contratto impresa",
         "body": "a corpo e misura 1,38 mln, ritenuta 5%, penale 0,5 per mille/giorno, riserve da esplicare entro "
                 "15 gg dalla firma con riserva. ultimazione: marzo.",
         "keywords": "contratto d'appalto capannone, a corpo e misura 1,38 milioni, ritenuta di garanzia 5%, "
                     "penale 0,5 per mille al giorno, riserve entro 15 giorni, firma con riserva, ultimazione "
                     "marzo, Meccanica Nera"},
        {"kind": "procedure", "where": "project:" + P_CAPANNONE, "who": "lead", "section": "operations",
         "name": "Chiusura lavori",
         "keywords": "ultimazione, collaudo, chiusura lavori, certificato di ultimazione lavori, piccole "
                     "lavorazioni 60 giorni, conto finale / relazione DL, collaudo statico, fascicolo "
                     "dell'opera, agibilità / SCA / segnalazione certificata, fine cantiere",
         "body": "certificato di ultimazione (con eventuali piccole lavorazioni entro 60 gg)\nconto finale + "
                 "relazione DL\ncollaudo statico (collaudatore del committente)\nfascicolo dell'opera "
                 "aggiornato dal CSE\nagibilità (SCA)"},
    ],
}

CUSTOMERS = [COMUNE, ATER, QUERCE, MORETTI, MECNERA]

# -- the lessons: findings without customer, people, amounts or record numbers ------------------------------------
LESSONS = [
    {"key": "atto_impegno_rtp", "who": "lead", "state": "active", "tags": ["gare", "SIA"], "activities": ["analysis"],
     "title": "Atto di impegno RTP non firmato: esclusione senza soccorso",
     "applies_to": "gare SIA in raggruppamento", "verified": "maggio 2026",
     "finding": "Un raggruppamento è stato escluso perché l'atto di impegno a costituire l'RTP caricato era la "
                "bozza non firmata da un mandante; la commissione lo ha trattato come parte dell'offerta e non "
                "ha concesso il soccorso istruttorio.",
     "solution": "Controllo incrociato da due persone della firma digitale valida su ogni file, compresi quelli "
                 "dei mandanti, e carico almeno due giorni prima della scadenza.",
     "keywords": "atto di impegno RTP, firma digitale mancante, esclusione gara, soccorso istruttorio negato, "
                 "mandante / raggruppamento temporaneo, firme incrociate, carico 48 ore prima"},
    {"key": "categoria_e22", "who": "lead", "state": "active", "tags": ["parcella", "SIA"], "activities": ["analysis"],
     "title": "E.22 solo per edifici vincolati",
     "applies_to": "calcolo dei corrispettivi con il decreto parametri", "verified": "aprile 2026",
     "finding": "Un corrispettivo era stato calcolato con la categoria degli edifici tutelati perché l'edificio "
                "sembrava storico; non c'era vincolo e l'edificio pubblico aveva meno di settant'anni, quindi la "
                "categoria giusta era quella degli edifici esistenti, con grado di complessità molto più basso.",
     "solution": "Prima di usare la categoria dei vincolati cercare il decreto di vincolo o l'esito della verifica "
                 "dell'interesse culturale; altrimenti categoria degli esistenti.",
     "keywords": "E.22 / edifici vincolati, E.20 / edifici esistenti, grado di complessità G, decreto di "
                 "vincolo, verifica interesse culturale, 70 anni, edificio che sembra storico, parcella "
                 "sovrastimata"},
    {"key": "qbii05", "who": "partner", "state": "active", "tags": ["parcella"], "activities": ["analysis"],
     "title": "QbII.05 va all'esecutivo senza appalto integrato",
     "applies_to": "corrispettivi con l'allegato I.13", "verified": "aprile 2026",
     "finding": "Con due livelli di progettazione l'aliquota di elenco prezzi, computo e quadro economico del "
                "vecchio definitivo non resta al PFTE se non c'è appalto integrato.",
     "solution": "Attribuirla al progetto esecutivo e tenerla in una colonna separata del foglio parcella.",
     "keywords": "QbII.05, elenco prezzi / computo / quadro economico, progetto esecutivo, appalto integrato, "
                 "due livelli di progettazione / PFTE, All. I.13, foglio parcella"},
    {"key": "ifc_rifiutato", "who": "bim", "state": "active", "tags": ["BIM", "IFC"], "activities": [],
     "title": "Modello nativo rifiutato dall'ACDat della stazione appaltante",
     "applies_to": "consegne BIM a stazioni appaltanti", "verified": "luglio 2026",
     "finding": "Una consegna è stata respinta perché era stato caricato il modello federato nel formato del "
                "software di authoring invece dell'IFC richiesto dal capitolato informativo.",
     "solution": "Consegna ufficiale solo in IFC (versione del capitolato), aperto e controllato in un viewer "
                 "indipendente prima del caricamento; il nativo resta interno.",
     "keywords": "formato aperto, modello nativo rifiutato, IFC / formato aperto, consegna respinta, ACDat "
                 "stazione appaltante, capitolato informativo, viewer indipendente, modello federato, formato "
                 "proprietario"},
    {"key": "clash_trave_canale", "who": "bim", "state": "active", "tags": ["BIM", "clash detection"],
     "activities": [], "title": "Canali di ventilazione contro travi esistenti",
     "applies_to": "riqualificazioni con VMC su edifici in c.a.", "verified": "giugno 2026",
     "finding": "La clash detection sul modello federato ha trovato un canale di mandata che attraversava una "
                "trave di bordo esistente; centinaia di altri conflitti erano falsi positivi dovuti alle "
                "tolleranze.",
     "solution": "Regole separate per hard clash con tolleranza stretta e una regola dedicata travi contro canali "
                 "grandi; risolvere spostando i canali nei controsoffitti, mai forando travi esistenti.",
     "keywords": "clash detection / controllo interferenze, canali di ventilazione / VMC, travi esistenti, "
                 "falsi positivi / tolleranze, hard clash, controsoffitto, foratura travi, modello federato"},
    {"key": "ct3_sospensione", "who": "partner", "state": "active", "tags": ["Conto Termico", "energia"],
     "activities": [], "title": "Il portale del Conto Termico può chiudere per budget esaurito",
     "applies_to": "domande di incentivo al GSE", "verified": "aprile 2026",
     "finding": "Il portale è stato sospeso un mese dopo l'apertura per esaurimento del budget annuale e "
                "riaperto dopo sei settimane; una domanda pronta è rimasta ferma.",
     "solution": "Inviare appena il portale apre, con diagnosi e documenti pronti prima; non avviare i lavori "
                 "prima della conferma della prenotazione.",
     "keywords": "PortalTermico, Conto Termico, portale sospeso, budget esaurito, GSE, prenotazione, inviare "
                 "subito all'apertura, avvio lavori dopo conferma"},
    {"key": "cam_isolanti", "who": "arch", "state": "active", "tags": ["CAM", "energia"], "activities": [],
     "title": "CAM: isolante senza dichiarazione del riciclato non è verificabile",
     "applies_to": "progetti pubblici con i nuovi CAM edilizia", "verified": "settembre 2026",
     "finding": "Un isolante sintetico previsto a capitolato non aveva dichiarazione del contenuto di riciclato "
                "né EPD: il criterio sugli isolanti non era dimostrabile e il materiale è stato cambiato a "
                "progetto avanzato, con nuovi calcoli energetici e aumento del computo.",
     "solution": "Scegliere i prodotti isolanti già in PFTE tra quelli con EPD e dichiarazioni conformi, e "
                 "chiedere le schede in capitolato.",
     "keywords": "CAM / criteri ambientali minimi, isolante, dichiarazione contenuto di riciclato, EPD / "
                 "dichiarazione ambientale di prodotto, criterio non verificabile, cambio materiale, scelta "
                 "prodotti in PFTE, aumento computo"},
    {"key": "notifica_tardiva", "who": "partner", "state": "active", "tags": ["sicurezza", "cantiere"],
     "activities": [], "title": "L'allestimento del cantiere conta come inizio lavori",
     "applies_to": "cantieri con più imprese", "verified": "maggio 2026",
     "finding": "L'impresa ha montato recinzione e baraccamenti prima che la notifica preliminare fosse inviata; "
                "il coordinatore ha dovuto fermare il cantiere fino all'invio.",
     "solution": "Inviare la notifica appena le imprese sono note, non aspettare i POS dei subappaltatori, e "
                 "dire per scritto all'impresa che nessuno entra prima della consegna.",
     "keywords": "notifica preliminare, allestimento cantiere, inizio lavori, recinzione e baracche, fermo "
                 "cantiere, coordinatore sicurezza / CSE, POS subappaltatori"},
    {"key": "sal_riserva", "who": "lead", "state": "active", "tags": ["DL", "contabilità"], "activities": [],
     "title": "Lavorazioni non contrattuali fuori dal SAL",
     "applies_to": "direzione lavori", "verified": "ottobre 2026",
     "finding": "L'impresa ha chiesto di inserire nel SAL una lavorazione imprevista a prezzo proprio; senza "
                "nuovo prezzo e variante approvata il DL non può contabilizzarla e l'impresa firma con riserva.",
     "solution": "Escludere la voce, verbalizzare, preparare subito perizia e nuovo prezzo con analisi e farli "
                 "approvare per scritto dal committente.",
     "keywords": "lavorazioni non contrattuali, SAL / stato avanzamento lavori, nuovo prezzo / NP, perizia di "
                 "variante, riserva dell'impresa, lavori extra / imprevisti, approvazione scritta committente"},
    {"key": "pdc_copertura", "who": "partner", "state": "draft", "tags": ["condominio", "energia"],
     "activities": [], "title": "pdc in copertura: verificare solaio",
     "applies_to": "", "verified": None,
     "finding": "unità esterne pompa di calore in copertura piana troppo pesanti per il solaio esistente",
     "solution": "telaio di ripartizione sulle travi, verificare prima di scegliere la macchina",
     "keywords": "PdC / pompa di calore, unità esterne in copertura, verifica solaio, peso macchine, telaio di "
                 "ripartizione, copertura piana, travi"},
    {"key": "aggiornamento_cse", "who": "lead", "state": "active", "tags": ["formazione", "sicurezza"],
     "activities": [], "title": "Aggiornamento quinquennale dei coordinatori",
     "applies_to": "", "verified": None,
     "finding": "Senza le quaranta ore di aggiornamento nel quinquennio un coordinatore non può più svolgere il "
                "ruolo di CSP o CSE, anche su un cantiere già in corso.",
     "solution": "Scadenze del quinquennio nel foglio crediti dello studio, avviso sei mesi prima.",
     "keywords": "aggiornamento quinquennale, 40 ore, coordinatore sicurezza, CSP / CSE, decadenza "
                 "abilitazione, foglio crediti, scadenze formazione"},
]

# the question sets are demo/questions.json (titles resolved on the database by eval_memoria.py)
EVAL = []
