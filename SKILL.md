---
name: nap-mobie-portugal-ev
description: >-
  Analyse Portugal's public EV charging network from official open data: NAP MOBI.E
  (DATEX II 3.3 static + dynamic), MOBI.E OPC tariffs, MOBI.E PartyID and DGEG
  operator registries. Produces a self-contained local dashboard (dashboard.html),
  a facts list and a reportable-errors list. Use when the user asks to analyse,
  aggregate, join, map, visualise, audit data quality of, or build a dashboard for
  the Portuguese EV charging network / "rede de carregamento" / NAP MOBI.E / OPC
  tariffs / pontos de carregamento / DGEG. Triggers on words like "NAP", "MOBI.E",
  "mobilidade elétrica", "pontos de carregamento", "tarifário OPC", "EV charging
  Portugal", "carregadores", "rede de carregamento".
---

# NAP MOBI.E — Portuguese EV charging network analysis

Analyses Portugal's public EV charging infrastructure by joining official open
sources. Output: a **self-contained `dashboard.html`** (no external libs, opens
via `file://`), `facts.md`, and `errors.md` (items to report to data owners).

The skill always pulls **fresh data from the official origins** — never rely on a
stale local copy. `scripts/fetch_data.sh` downloads everything (~230 MB).

## What this skill does

1. **Fetch** fresh NAP XMLs, MOBI.E tariff CSV, PartyID PDF and DGEG pages.
2. **ETL** the two DATEX II XMLs (streaming) into clean CSVs.
3. **Join** NAP points ↔ MOBI.E OPC tariffs (the non-obvious part — see Gotchas).
4. **Resolve** OPC/CEME codes → entities via DGEG registries + PartyID.
5. **Validate** physical/schema sanity and cross-source consistency.
6. **Build** the dashboard + facts + reportable errors.

Verified numbers for the 2026-08-16 snapshot (re-run to refresh): 8 260 sites,
20 521 points, 90 operators, 92.2% NAP↔MOBI.E tariff match, 99.8% power
agreement, 30% of connectors with V×I/power inconsistency.

## Environment

- venv with `pandas`, `lxml`, `pdfplumber`:
  ```bash
  python3 -m venv venv
  venv/bin/pip install pandas lxml pdfplumber
  ```
- Always run scripts from the repo root — they resolve data files relative to
  the CWD (`venv/bin/python scripts/nap_etl.py`, not from inside `scripts/`).
- Never read the ~190 MB XMLs with the Read tool; parse with `scripts/nap_etl.py`.

## Pipeline

```bash
bash scripts/fetch_data.sh                    # fresh data from origins (see references/data-sources.md)
venv/bin/python scripts/nap_etl.py            # XML -> nap_static_sites.csv, nap_static_points.csv,
                                              #        nap_dynamic_status.csv, nap_dynamic_pricing.csv
venv/bin/python scripts/check_quality.py      # enums + V×I sanity + coords
venv/bin/python scripts/summary.py            # numeric overview
venv/bin/python scripts/mobie_join.py         # NAP ↔ MOBI.E tariffs -> nap_opc_points.csv
venv/bin/python scripts/dgeg_lists.py         # DGEG pages -> dgeg_opc.csv, dgeg_ceme.csv
venv/bin/python scripts/dgeg_crossref.py      # OPC codes -> entities -> nap_opc_registry.csv
venv/bin/python scripts/partyid_crossref.py   # enrich with PartyID
venv/bin/python scripts/build_dashboard.py    # -> dashboard.html, facts.md, errors.md
```

Outputs to give the user:
- `dashboard.html` — open with `open dashboard.html`
- `facts.md` — interesting facts
- `errors.md` — reportable data errors (11 items)

## Data sources

`references/data-sources.md` has the exact URLs and license notes. Summary:
- **NAP static**: `https://pgm.mobie.pt/integration/nap/evChargingInfra`
- **NAP dynamic**: `https://pgm.mobie.pt/integration/nap/evActualStatus`
- **OPC tariff**: `https://www.mobie.pt/documents/42032/106470/Tarifas` (CSV)
- **PartyID**: MOBI.E documents PDF (2022, outdated — see Gotchas)
- **DGEG**: OPC-com-reconhecimento-previo and CEME-registados pages

## Non-obvious stuff (read `references/gotchas.md` in full before analysing)

- **Join NAP↔MOBI.E by `site_external_id` + last segment of `point_id`**
  (the tomada, int-normalized). Do NOT join on `point_external_id` — its
  `PT*op*[E]*reg*num*tom` format is inconsistent (glued `E` prefix, variable
  segment count).
- `brands_accepted` (NAP) is the global CEME list per point, NOT an operator
  discriminator.
- `facilityLocation` is in the `locationReferencing` namespace, not
  `locationExtension`.
- NUTS is level-1 only.
- Dynamic point ids match static 100%, but 46 points appear 2–3× in the dynamic
  feed with conflicting states — dedupe `keep='first'`, flag as error.
- 30% of connector rows have declared power inconsistent with V×I (>25% off);
  for `mode3AC3p` the physical power is `√3×V×I`, else `V×I`.
- MOBI.E PartyID PDF is from 2022: 38 active tariff codes missing, 22 unused.
- **Dashboard JSON**: sanitize NaN/Inf → null and dump with `allow_nan=False`,
  otherwise the browser's `JSON.parse` fails (historical bug).

## Dashboard validation (always do this after a rebuild)

```bash
venv/bin/python -c "import re,json;h=open('dashboard.html').read();m=re.search(r'const D = (.*?);\n',h,re.S);D=json.loads(m.group(1));print('JSON OK', len(D['points']))"
venv/bin/python -c "import re;h=open('dashboard.html').read();m=re.search(r'<script>(.*?)</script>',h,re.S);open('/tmp/dash_check.js','w').write(m.group(1))"
node --check /tmp/dash_check.js
```

If the dashboard renders nothing below the KPIs, it's a JS runtime error — see
the historical bugs in `references/gotchas.md`.

## Layout

- `scripts/` — the pipeline
- `assets/` — `dashboard_template.html`, `schemas/*.xsd` (DATEX II 3.3)
- `references/` — `data-sources.md`, `gotchas.md`
- Raw XMLs + CSVs live in the repo root, gitignored, refreshed by `fetch_data.sh`

## When NOT to use

- Real-time streaming or OCPI API access (this uses the public DATEX II dumps).
- The MOBI.Data aggregated portal as a source (it's derived; we use the raw
  NAP feeds).
- Charging data of networks *not* connected to MOBI.E (off-network operators
  must be fetched from their own sources).