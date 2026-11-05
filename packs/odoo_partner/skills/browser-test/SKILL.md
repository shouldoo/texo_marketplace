---
name: browser-test
description: >-
  Drive the Odoo web client of a LOCAL instance or of a stage host explicitly enabled by an
  active rule of the project (the hub, `texo context`) with a headless Chromium
  (Playwright, open source) to verify what a change does in the real UI: log in,
  open records, click buttons, capture screenshots and collect JS/console/HTTP
  errors. Use after changing JavaScript, Owl templates, views or actions of a
  module (e.g. a new smart button or client action), or when the user asks to
  "provalo nel browser", "verifica l'interfaccia", "screenshot della vista",
  "controlla errori JS". Read-only by intent: it never touches hosts outside
  localhost unless it is an enabled stage host. Never for production hosts.
---

# Browser test — provare la UI di un'istanza locale o di stage

Strumento attivabile al bisogno: Playwright (Python) + Chromium in un virtualenv
dedicato, installato una volta per macchina con comandi standard:

```bash
python3 -m venv ~/.local/share/texo/browser
~/.local/share/texo/browser/bin/pip install --upgrade playwright
~/.local/share/texo/browser/bin/playwright install --with-deps chromium   # --with-deps richiede sudo su Linux
~/.local/share/texo/browser/bin/python -c "import playwright; print('ok')" # verifica
```

Se la verifica fallisce, proponi l'installazione all'utente prima di procedere.

## Safety gate

- Di default solo istanze **locali**: ogni scenario installa il filtro di rete
  qui sotto, che aborta le richieste verso host diversi da `localhost`,
  `127.0.0.1`, `::1` e da quelli elencati in `ODOO_BROWSER_ALLOW`.
- Gli host di **stage** sono ammessi solo se una regola **attiva** del progetto
  (`texo context --project <id>`, le `rules` del livello progetto,
  per esempio «Browser-test ammesso sullo stage `<host>`») li abilita: si abilitano con
  `ODOO_BROWSER_ALLOW=<host>`. Prima di abilitarlo controlla che l'host sia proprio in quella
  regola e che la description del progetto non lo indichi come ambiente di produzione; se l'host
  non è nella regola, la regola è una bozza o il ruolo non è chiaro, non lo abiliti: chiedi "è
  produzione o stage?" e proponi la regola (la scrivi dopo il sì della persona, con lo stato che
  il tuo ruolo consente: da member resta una bozza finché un lead non la attiva). **Mai** un host di produzione, nemmeno in sola
  lettura (a maggior ragione per le organizzazioni con vincoli dichiarati nel contesto, come
  chi serve persone vulnerabili).
- Su un host di stage le scritture dell'UI sono scritture sul DB di stage: ammesse per
  provare i flussi, ma solo su dati creati per il test (progetto/commessa ad hoc) e dichiarando
  all'utente cosa si è creato.
- Le credenziali non passano dalla chat: per i DB demo locali (`admin`/`admin`) va bene
  scriverle nello scenario; per DB con dati reali e per i branch di stage leggile dall'ambiente
  (`ODOO_TEST_URL`, `ODOO_TEST_DB`, `ODOO_TEST_LOGIN`, `ODOO_TEST_PASSWORD`, eventualmente da un
  file per progetto in `~/.config/texo/<slug>-test.env`, modo 600, che l'utente crea
  o autorizza). Mai stampare la password.
- Gli screenshot possono contenere dati dell'organizzazione: salvali in una cartella temporanea
  della sessione (`BROWSER_TEST_OUT`, fuori dal repo: la cartella di lavoro temporanea
  dell'assistente se ne ha una, altrimenti `mktemp -d`), **mai** in un repository Texo, nelle
  cartelle dei moduli o nel repository del progetto.

## Uso

```bash
BROWSER_TEST_OUT=<dir-temporanea> ~/.local/share/texo/browser/bin/python scenario.py
HEADED=1 ...                                          # finestra visibile (serve un display)
```

Scenario tipo (script Python autonomo):

```python
import os, sys, urllib.parse
from playwright.sync_api import sync_playwright

ALLOWED = {"localhost", "127.0.0.1", "::1"} | set(filter(None, os.environ.get("ODOO_BROWSER_ALLOW", "").split(",")))
OUT = os.environ.get("BROWSER_TEST_OUT", "/tmp/browser-test")
os.makedirs(OUT, exist_ok=True)
errors = []

def guard(route):
    host = urllib.parse.urlparse(route.request.url).hostname
    route.continue_() if host in ALLOWED or route.request.url.startswith("data:") else route.abort()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=not os.environ.get("HEADED"))
    page = browser.new_page()
    page.route("**/*", guard)
    page.on("pageerror", lambda e: errors.append(f"PAGEERROR {e}"))
    page.on("console", lambda m: m.type == "error" and errors.append(f"CONSOLE {m.text}"))
    page.on("response", lambda r: r.status >= 500 and errors.append(f"HTTP {r.status} {r.url}"))
    try:
        base = "http://localhost:<porta>"                       # porta dello stack: docker ps
        page.goto(f"{base}/web/login?db=<db>")
        page.fill("input[name=login]", "admin"); page.fill("input[name=password]", "admin")
        page.click("button[type=submit]"); page.wait_for_selector(".o_web_client")
        page.goto(f"{base}/odoo/action-sale.action_orders/28")
        page.wait_for_selector(".o_form_view")
        page.click("button[name=action_view_replenishments]")
        page.wait_for_selector(".o_stock_forecasted_page")
        print(page.locator("tbody tr").all_inner_texts())
        page.screenshot(path=f"{OUT}/replenishments.png", full_page=True)
    except Exception:
        page.screenshot(path=f"{OUT}/failure.png"); raise
    finally:
        print("\n".join(errors)); browser.close()
    sys.exit(1 if any(e.startswith("PAGEERROR") for e in errors) else 0)
```

A fine corsa lo scenario stampa gli errori JS/HTTP raccolti (`PAGEERROR`,
`CONSOLE`, `HTTP 5xx`) ed esce con codice 1 se c'è un `PAGEERROR` o lo scenario
fallisce (salva `failure.png`). Guarda gli screenshot aprendo il PNG con lo strumento di
lettura file dell'assistente, che mostra le immagini.

## Note operative

- `dbfilter` delle istanze di progetto: il DB deve rispettare il pattern dello stack
  (es. `<slug>-(dev|local|mirror)`), altrimenti il login risponde "Database not found".
- Le istanze in `dev_mode=reload,qweb,xml` ricompilano gli asset da sole: dopo
  una modifica JS/XML ricarica la pagina, senza restart.
- Lo scenario aspetta ciò che gli dici tu (`wait_for_selector`): scegli selettori
  stabili (`button[name=...]`, classi `o_*`), non testi tradotti.
