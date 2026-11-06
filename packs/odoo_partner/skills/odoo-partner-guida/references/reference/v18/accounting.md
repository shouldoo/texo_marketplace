---
type: "Reference"
title: "Contabilità — Delta Odoo 18"
description: "Contabilità — Delta Odoo 18: i cambi di Odoo 18 rispetto alla versione prima, da leggere con le lezioni del tag accounting e con il codice della versione."
tags: ["accounting", "v18"]
---

# Contabilità — Delta Odoo 18

> Per i progetti su Odoo 18, insieme alle lezioni del hub con il tag `accounting` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-18` (`.texo/THREADS.md`). Breaking change 17→18 ed errori specifici della versione.

## Cambiato in 18.0

| Cosa cambia | Prima (17.0) | Ora (18.0) | Impatto |
|-------------|---------------|------------|--------|
| `analytic_distribution` | Campo JSON su `account.move.line` | Esteso con la validazione dei piani analitici | **Miglioria** -- i piani ora sono imposti |
| Campi di `account.payment` | `payment_method_id` usato direttamente | `payment_method_line_id` lo sostituisce come campo principale | **Incompatibile** -- il codice che usa `payment_method_id` in creazione può fallire |
| Calcolo delle imposte | `compute_all()` restituisce un dict | Stessa API, ma le righe di ripartizione ora includono `tax_tag_invert` | **Cambio silenzioso** -- l'elaborazione custom delle imposte deve gestire le nuove chiavi |
| Riconciliazione bancaria | Riconciliazione basata su widget | Modello di riconciliazione rifatto, con `account.bank.statement.line` come entità principale | **Miglioria** -- le righe di estratto conto ora sono l'entità centrale |
| `state` di `account.move` | `draft` / `posted` / `cancel` | Stessi valori, ma il flusso di `cancel` usa `button_draft()` e poi una nuova registrazione | **Cambio di flusso** -- l'annullamento ora avviene in due passi |

## Localizzazione italiana: shift OCA → nativo Enterprise

> Le modifiche principali della localizzazione italiana sono entrate **in 18.0**: lo shift
> OCA `l10n-italy` → nativo descritto qui vale per **qualsiasi migrazione verso 18**
> (sia 16→18 sia 17→18). In V18 Enterprise gran parte delle funzioni storicamente coperte
> da OCA `l10n-italy` ha un **equivalente nativo**. Regola: **massimizzare il nativo, tenere
> OCA solo sui gap documentati**. Verifica sempre con native-check contro
> il codice di Odoo 18 (filo `odoo-18`) prima di decidere.
>
> Nei progetti Community le righe marcate *enterprise* non sono disponibili
> (Enterprise, fuori ambito): per quelle funzioni resta il modulo OCA
> `l10n-italy` alla versione di arrivo, se portato. La tabella serve a capire il
> confine, non a proporre Enterprise.

### E-invoicing (FatturaPA / SdI)
- Nativo: **`l10n_it_edi`** (trasmissione/ricezione via **proxy SdI Odoo**, `account_edi_proxy_client`),
  + `l10n_it_edi_sale`, `l10n_it_edi_doi` (dichiarazione d'intento), `l10n_it_edi_ndd` (note di debito),
  `l10n_it_edi_withholding` (ritenuta in e-fattura).
- Sostituisce l'intera famiglia OCA `l10n_it_fatturapa_*` (out/in/purchase/sale/rc/sp/wt/stamp…).
- **Connettori esterni di trasmissione**: **dismettibili** a favore del proxy SdI nativo.

### Mappatura funzione → nativo V18
| Funzione | OCA (≤17) | Nativo V18 | Note |
|---|---|---|---|
| DDT | `l10n_it_delivery_note` | `l10n_it_stock_ddt` (nei sorgenti Community) | migrare i dati DDT |
| Ritenute d'acconto | `l10n_it_withholding_tax` | `l10n_it_edi_withholding` (nei sorgenti Community) | |
| Dichiarazione d'intento | `l10n_it_declaration_of_intent` | `l10n_it_edi_doi` (nei sorgenti Community) | |
| RiBa | `l10n_it_ricevute_bancarie` | `l10n_it_riba` (enterprise) | |
| Intrastat | `l10n_it_intrastat` | `account_intrastat` (enterprise) | verificare invio telematico |
| Cespiti | `l10n_it_asset_management` | `account_asset` (enterprise) | migrare registri cespiti |
| Libro giornale | `l10n_it_central_journal_reportlab` | `l10n_it_reports` (enterprise) | le patch custom diventano spesso obsolete |
| Bilancio civilistico SP/CE | `l10n_it_financial_statements_report` | `l10n_it_reports` (enterprise) | **parziale**: verificare dettaglio/nota integrativa |
| Liquidazione periodica IVA (LIPE) | `l10n_it_vat_statement_communication` | `l10n_it_xml_export` (`comunicazioneIvp`, enterprise) | |
| Scissione pagamenti | `l10n_it_split_payment` | `l10n_it_edi` (EsigibilitaIVA=S) | gestita tramite imposte/EDI |
| Reverse charge | `l10n_it_reverse_charge` | `l10n_it_edi` (TD16-19 / VJ) | **parziale**: verificare autofattura/integrazione |
| **Registri IVA** (stampa sezionali) | `l10n_it_vat_registries` | — **nessun nativo** | **GAP → resta OCA** in 18.0 |
| CF / IPA / REA / natura aliquote / tipi doc | `l10n_it_*` vari | `l10n_it` + `l10n_it.document.type` | nativo/parziale |

### Gap noti (restano OCA 18.0)
- **Registri IVA** (stampa formale dei registri sezionali vendite/acquisti/corrispettivi): nessun
  modulo nativo equivalente → mantenere `l10n_it_vat_registries`.
- Reportistica finanziaria/scadenziario di dettaglio (`account_financial_report`, `account_due_list`):
  valutare copertura di `account_reports` caso per caso.
