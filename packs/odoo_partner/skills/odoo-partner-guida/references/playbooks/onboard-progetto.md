---
type: "Playbook"
title: "Playbook — Onboarding di un progetto"
description: "Entry point unico per prendere in carico un progetto."
tags: ["onboard-progetto"]
---

# Playbook — Onboarding di un progetto

> Entry point unico per prendere in carico un progetto. L'onboarding ha tre
> pezzi: il **cliente e il progetto nell'Odoo di coordinamento** (la casa della
> memoria: description, milestone, update, task, ore, regole), il **repository del
> progetto** clonato in `progetti/<slug>/` (il codice dell'istanza) e,
> opzionale, l'**istanza locale Docker**. Nulla dell'ente (persone, soci,
> beneficiari, documenti) finisce nei file versionati dei repository Texo, né nel
> repository dell'istanza: i fatti del progetto vivono solo nell'Odoo di
> coordinamento, con i suoi permessi.

## Prerequisiti

- L'Odoo di coordinamento raggiungibile e il tuo token nelle credenziali del customer
  (`~/.config/texo/<organisation>.env`, `<core>/playbooks/coordinamento-locale.md`): `texo whoami`
  risponde con il tuo ruolo.
- Accesso (SSH e `gh auth`) al repository GitHub del progetto:
  `gh repo view <owner>/<repo>`. **404 / permesso negato** → non sei
  collaboratore: chiedi l'accesso a chi lo gestisce, non cercare copie altrove.

## Flusso

1. **Cliente e progetto in Odoo**: il cliente è un partner di primo livello,
   il progetto un `project.project` con quel cliente, con il responsabile (chi
   fa da lead per la revisione delle bozze) e il team (gli utenti che possono
   leggerlo, se la visibilità è «solo team»). Li crea la persona nell'interfaccia;
   l'agente verifica con `texo query project.project --domain '[["name","ilike","<nome>"]]' --fields name,partner_id,user_id`.
2. **Description del progetto (bedrock)**: se `texo project <id>` mostra la
   description vuota, proponi il testo dal repository (`.gitmodules`, manifest,
   workflow di deploy) e da ciò che la persona dice; la persona lo scrive nella
   description del progetto in Odoo, l'agente non la riscrive mai da solo:
   - versione ed edizione di Odoo (Community);
   - l'organizzazione: tipo di ente, settore, vincoli particolari (per esempio
     servizi a persone vulnerabili → nessun dato di produzione fuori dalla
     produzione), referenti per ruolo, mai dati personali;
   - gli ambienti: produzione, stage, locale con ruolo e URL;
   - i moduli installati: custom, OCA e vendor con repository e branch;
   - repository e deploy: repository, branch principale, come si arriva a stage
     e produzione, backup;
   - le decisioni già prese e stabili, con il loro perché.
   Ciò che un agente deve fare sempre o non fare mai (le regole vincolanti, gli
   host di stage abilitati per `browser-test`) diventa una **regola** del
   progetto, dopo il sì della persona
   (`texo note "<titolo>" "<regola>" --project <id> --yes`; un lead aggiunge
   `--state active`). La roadmap sono le milestone, che crea la persona; il punto
   di partenza si scrive come primo update
   (`texo update <id> "<titolo>" on_track "<testo>" --yes`).
3. **Documenti già scritti** (analisi, verbali, note di progetto tenuti altrove): entrano nella memoria
   come documenti del progetto con la skill `memoria-ingestione`; i fatti stabili che danno si propongono
   per la description, come al passo 2.
4. **Clona il repository** in `progetti/<slug>/` (lo `<slug>` è il nome breve
   del progetto, lo stesso dell'istanza locale in `odoo/odoo-clients/`):

   ```bash
   # dalla cartella di lavoro: progetti/ è una cartella di lavoro (texo mount la crea, fuori da git)
   git clone --recurse-submodules <url-repo-progetto> progetti/<slug>
   bash <core>/setup/install-git-hooks.sh progetti/<slug>
   ```

5. **Documenti**: spec, requisiti, verbali, analisi forniti dall'ente si
   allegano al task pertinente dell'Odoo di coordinamento (li carica la persona),
   senza dati personali nei testi che l'agente scrive; i file originali (PDF,
   Office) non si versionano.
6. **Task**: `texo my-work` e `texo task <id>`; i task li crea la persona in
   Odoo, le PR ne citano l'id.
7. **Istanza locale — opzionale**: se serve un'istanza Docker per test o debug, la si crea in
   `odoo/odoo-clients/<slug>-v<N>/` (cartella di lavoro, solo locale, fuori da git), con l'immagine
   ufficiale di Odoo della versione del progetto, il repository del progetto e `modules/V<N>/` montati.
8. **DB di test**: se hai l'istanza locale, crea un database demo con il set di moduli della description
   del progetto — **niente dump di produzione** di default; un dump reale entra solo come eccezione decisa
   dalla persona, neutralizzato e anonimizzato (`$(texo where --pack odoo_partner)/scripts/neutralize-db.sh`,
   `anonymize-db.sh`), e si cancella a fine lavoro.

## Relazione con gli altri playbook

- Istanza di coordinamento, token, client: `<core>/playbooks/coordinamento-locale.md`.
- Test di un modulo sull'istanza locale: `test-modulo-locale.md`.
- Migrazione di versione del progetto: `migrazione-progetto.md`.
