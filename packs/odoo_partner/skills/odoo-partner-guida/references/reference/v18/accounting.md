---
type: "Reference"
title: "Accounting — Delta Odoo 18"
description: "Accounting — Delta Odoo 18: i cambi di Odoo 18 rispetto alla versione prima, da leggere con le lesson del tag accounting e con il codice della versione."
tags: ["accounting", "v18"]
---

# Accounting — Delta Odoo 18

> Per i progetti su Odoo 18, insieme alle lesson del hub con il tag `accounting` (`texo search "<parole>" --scope lessons`) e al codice della versione nel mirror del filo `odoo-18` (`.texo/THREADS.md`). Breaking change 17→18 ed errori specifici della versione.

## Changed in 18.0

| What Changed | Before (17.0) | Now (18.0) | Impact |
|-------------|---------------|------------|--------|
| `analytic_distribution` | JSON field on `account.move.line` | Extended with analytic plan validation | **Enhancement** -- plans are now enforced |
| `account.payment` fields | `payment_method_id` used directly | `payment_method_line_id` replaces it as primary field | **Breaking** -- code using `payment_method_id` for creation may fail |
| Tax computation | `compute_all()` returns dict | Same API, but repartition lines now include `tax_tag_invert` | **Silent change** -- custom tax processing must handle new keys |
| Bank reconciliation | Widget-based reconciliation | Refactored reconciliation model with `account.bank.statement.line` as primary | **Enhancement** -- statement lines are now the core entity |
| `account.move` `state` | `draft` / `posted` / `cancel` | Same values, but `cancel` flow uses `button_draft()` then re-post | **Workflow change** -- cancellation is now a two-step process |

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
- Rimpiazza l'intera famiglia OCA `l10n_it_fatturapa_*` (out/in/purchase/sale/rc/sp/wt/stamp…).
- **Connettori esterni di trasmissione**: **dismettibili** a favore del proxy SdI nativo.

### Mappatura funzione → nativo V18
| Funzione | OCA (≤17) | Nativo V18 | Note |
|---|---|---|---|
| DDT | `l10n_it_delivery_note` | `l10n_it_stock_ddt` (source) | migrare i dati DDT |
| Ritenute d'acconto | `l10n_it_withholding_tax` | `l10n_it_edi_withholding` (source) | |
| Dichiarazione d'intento | `l10n_it_declaration_of_intent` | `l10n_it_edi_doi` (source) | |
| RiBa | `l10n_it_ricevute_bancarie` | `l10n_it_riba` (enterprise) | |
| Intrastat | `l10n_it_intrastat` | `account_intrastat` (enterprise) | verificare invio telematico |
| Cespiti | `l10n_it_asset_management` | `account_asset` (enterprise) | migrare registri cespiti |
| Libro giornale | `l10n_it_central_journal_reportlab` | `l10n_it_reports` (enterprise) | i patch custom diventano spesso obsoleti |
| Bilancio civilistico SP/CE | `l10n_it_financial_statements_report` | `l10n_it_reports` (enterprise) | **parziale**: verificare dettaglio/nota integrativa |
| Liquidazione periodica IVA (LIPE) | `l10n_it_vat_statement_communication` | `l10n_it_xml_export` (`comunicazioneIvp`, enterprise) | |
| Scissione pagamenti | `l10n_it_split_payment` | `l10n_it_edi` (EsigibilitaIVA=S) | gestita via tax/EDI |
| Reverse charge | `l10n_it_reverse_charge` | `l10n_it_edi` (TD16-19 / VJ) | **parziale**: verificare autofattura/integrazione |
| **Registri IVA** (stampa sezionali) | `l10n_it_vat_registries` | — **nessun nativo** | **GAP → KEEP-OCA** 18.0 |
| CF / IPA / REA / natura aliquote / tipi doc | `l10n_it_*` vari | `l10n_it` + `l10n_it.document.type` | nativo/parziale |

### Gap noti (restano OCA 18.0)
- **Registri IVA** (stampa formale dei registri sezionali vendite/acquisti/corrispettivi): nessun
  modulo nativo equivalente → mantenere `l10n_it_vat_registries`.
- Reportistica finanziaria/scadenziario di dettaglio (`account_financial_report`, `account_due_list`):
  valutare copertura di `account_reports` caso per caso.
