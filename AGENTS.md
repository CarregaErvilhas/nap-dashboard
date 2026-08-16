# AGENTS.md — NAP MOBI.E data analysis POC

## Project type
Single-machine POC analysis of the Portuguese EV charging network. No tests, no
package manifests, no CI. Code is meant to be run once and produce CSVs + a
self-contained dashboard. Don't over-engineer.

## Layout
- `scripts/` — pipeline (fetch_data.sh, nap_etl.py, mobie_join.py, dgeg_lists.py,
  dgeg_crossref.py, partyid_crossref.py, check_quality.py, summary.py,
  concelho_check.py, build_dashboard.py)
- `assets/` — `dashboard_template.html` and `schemas/*.xsd` (DATEX II 3.3)
- `references/` — docs for the SKILL.md (data sources, gotchas)
- Raw XMLs + intermediate CSVs live in the repo root and are gitignored
  (downloaded via `scripts/fetch_data.sh`). Run all scripts from the repo root;
  they resolve data files relative to the CWD.

## Environment
- Create and use a local venv — never rely on the system Python (it may be a
  recent version where pip is blocked by PEP 668). It just needs `pandas`, `lxml`
  and `pdfplumber`:
  ```bash
  python3 -m venv venv
  venv/bin/pip install pandas lxml pdfplumber
  ```
- Reference the venv interpreter as `venv/bin/python` in commands; do not
  hardcode absolute paths to this machine's venv.
- Raw XMLs are big (`evChargingInfra_latest.xml` ~190 MB). Don't read them with
  the Read tool or cat them; parse with `scripts/nap_etl.py`.

## Fetch fresh data
```bash
bash scripts/fetch_data.sh
```
Downloads the live NAP XMLs, MOBI.E tariff CSV, PartyID PDF and DGEG HTML pages
from the official origins (see `scripts/fetch_data.sh` for the exact URLs).

## Pipeline order
`scripts/nap_etl.py` → (`scripts/check_quality.py`, `scripts/summary.py`) →
`scripts/mobie_join.py` → `scripts/dgeg_lists.py` → `scripts/dgeg_crossref.py` →
`scripts/partyid_crossref.py` → `scripts/concelho_check.py` →
`scripts/build_dashboard.py`.
`scripts/build_dashboard.py` reads the intermediate CSVs and
writes `dashboard.html`, `facts.md`, `errors.md`; it appends
`concelho_mismatches.md` (written by `concelho_check.py`) to `errors.md` when
present. It also regenerates `dashboard.png` (README screenshot) via headless
Chrome if available; it only warns/skips otherwise.

`scripts/concelho_check.py` locates every site inside official CAOP concelho
polygons (downloaded on first run into `caop_cache/`, gitignored) and flags the
sites whose coordinates contradict the concelho implied by the site_id code.
Writes `concelho_check.csv` + `concelho_mismatches.md` (errors.md items 11a/11b).

## Housekeeping: save ad-hoc analysis scripts
When an interactive query ends up producing new analysis code (point-in-polygon,
cross-checks, one-off joins), save it as a script in `scripts/` (or append it to
the relevant pipeline script) instead of leaving it in the terminal or /tmp —
future re-runs should not regenerate all that code from scratch. If it's a
throwaway one-liner, at least note it in AGENTS.md so it can be rebuilt.

## Build command
```bash
venv/bin/python scripts/build_dashboard.py
```
After editing `assets/dashboard_template.html` or `scripts/build_dashboard.py`,
**always rebuild `dashboard.html`** (the deliverable) and re-validate:
- embedded JSON must parse: extract `const D = (.*?);` and `json.loads` it
- inline JS must pass `node --check` (extract the `<script>` block first)

## Data gotchas (verified)
- Join NAP↔MOBI.E by `site_external_id` + last segment of `point_id` (tomada,
  int-normalized). Do NOT join on `point_external_id`: format
  `PT*op*[E]*reg*num*tom` is unreliable (glued `E` prefix, variable segment count).
- `brands_accepted` (NAP) = global CEME list per point, NOT an operator discriminator.
- `facilityLocation` is in the `locationReferencing` namespace, not `locationExtension`.
- NUTS in NAP is level-1 only.
- Dynamic & static point ids match 100%; but 46 points appear 2–3× in dynamic
  status with conflicting states (48 extra rows).
- 30% of connector rows (6 206/20 624) have declared power inconsistent with
  V×I (>25% off); 2 690 declare power above physical capacity (impossible, e.g.
  1200 V × 600 A = 720 kW declared as 200 kW).
- MOBI.E PartyID is a 2022 PDF: 38 active tariff codes missing, 22 unused codes.
- 733 MOBI.E `UID_TOMADA` values are bare numeric ids.
- Power agreement NAP↔MOBI.E is 99.8% (only 29/18 923 diverge >30%).

## Dashboard specifics
- Data injected into `assets/dashboard_template.html` at the `/*__DATA__*/` marker via
  `json.dumps(clean(data), ensure_ascii=False, allow_nan=False)`.
- **Must** sanitize NaN/Inf floats to null before dumping — bare `NaN` breaks
  browser `JSON.parse`. The `clean()` helper in `build_dashboard.py` does this.
- No external libs, pure CSS/JS, must open via `file://`.
- Two runtime bugs were fixed historically: (1) a reference to non-existent
  element id `status`, (2) `label()` using undefined `max` instead of the local
  `m` in `bars()`. If the dashboard shows nothing below the KPIs, suspect a JS
  runtime error — validate the script with a DOM-stub eval in node.
- Table features: text search across all columns, dropdown filters (estado,
  região, classe potência, operador), click-to-sort headers, pagination (200/page).

## Deliverables
- `dashboard.html` — the interactive dashboard (open with `open dashboard.html`)
- `facts.md` — interesting facts
- `errors.md` — reportable data errors (11 items, for the data owners)