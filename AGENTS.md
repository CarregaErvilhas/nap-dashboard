# AGENTS.md — NAP MOBI.E data analysis POC

## Project type
Single-machine POC analysis of the Portuguese EV charging network. No tests, no
package manifests, no CI. Code is meant to be run once and produce CSVs + a
self-contained dashboard. Don't over-engineer.

## Layout
- `scripts/` — pipeline (fetch_data.sh, nap_etl.py, mobie_join.py, dgeg_lists.py,
  dgeg_crossref.py, partyid_crossref.py, check_quality.py, summary.py,
  concelho_check.py, osm_umap.py, make_pt_outline.py, extract_enums.py,
  build_dashboard.py)
- `assets/` — `dashboard_template.html`, `pt_outline.json` (PT outline for the
  map), `schemas/*.xsd` (DATEX II 3.3)
- `references/` — docs for the SKILL.md (data sources, gotchas)
- `Agents/` — system prompts dos agentes automáticos (um `.md` por agente; ver
  `Agents/AGENTS.md`). Atual: `Agents/anomalias.md` (anomalias dos dados
  estáticos NAP → `Agents-outputs/anomalias-results.md`, agrupado por OPC).
- `Agents-outputs/` — relatórios gerados pelos agentes (ex.
  `Agents-outputs/anomalias-results.md`).
- Raw XMLs + intermediate CSVs live in the repo root and are gitignored
  (downloaded via `scripts/fetch_data.sh`). Run all scripts from the repo root;
  they resolve data files relative to the CWD.
- `umap_cache/` + `caop_cache/` — gitignored caches (umap maps/OSM dump,
  CAOP concelho polygons).

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
`scripts/osm_umap.py` → `scripts/make_pt_outline.py` →
`scripts/build_dashboard.py`.
`scripts/build_dashboard.py` reads the intermediate CSVs +
`osm_umap.csv`/`osm_caca.csv`/`assets/pt_outline.json` and writes
`dashboard.html`, `facts.md`, `errors.md`; it appends
`concelho_mismatches.md` (written by `concelho_check.py`) and
`osm_umap_findings.md` (written by `osm_umap.py`) to `errors.md` when present.
It also regenerates `dashboard.png` (README screenshot) via headless Chrome if
available; it only warns/skips otherwise.

`scripts/validate_dashboard.py` (rode no `refresh.yml` antes do commit e em
local depois de qualquer build) valida o `dashboard.html`: o JSON embutido
`const D = {…}` tem de fazer `json.loads`, cada `<script>` tem de passar
`node --check`, e a inicialização tem de correr sem exceção numa eval com DOM
stub. `scripts/pipeline_guard.py` travará o commit se um upstream mudar o
formato e o pipeline produzir dados absurdos sem rebentar (limiares mínimos
para sites/pontos/join/DGEG/registo) — falha o job e o dashboard online fica
no último bom.

`scripts/concelho_check.py` locates every site inside official CAOP concelho
polygons (downloaded on first run into `caop_cache/`, gitignored) and flags the
sites whose coordinates contradict the concelho implied by the site_id code.
Writes `concelho_check.csv` + `concelho_mismatches.md` (errors.md items 11a/11b).

`scripts/osm_umap.py` cross-references NAP sites against community OSM data: the
Overpass dump `Todos.json` from the author of the "Postos de Carregamento v2.1"
umap map (both `amenity=charging_station` and `man_made=charge_point` elements)
and the "Caça aos Postos" umap doubt layers. Fetches are cached in `umap_cache/`.
Matches by MOBI.E `ref` code (strips a `MOBI-` prefix, expands multi-code refs
"A;B;C", way polygons use the centroid). Writes `osm_umap.csv` (deduped per NAP
code, preferring the row with the most payment/auth tags), `osm_caca.csv` and
`osm_umap_findings.md` (errors.md item 12).

`scripts/make_pt_outline.py` builds `assets/pt_outline.json` (decimated PT
outline for the dashboard map **plus per-district/island labels** — `{outline:
{region: [rings]}, districts: {region: {name: [lon, lat]}}}`) from the CAOP
concelho polygons in `caop_cache/`. Mainland labels use the CAOP `Distrito`
attribute (18), Madeira/Açores fall back to island name (`Ilha`/`ILHA`, 2+9).
Run it once when the outline asset is missing; the JSON is committed.

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
**always rebuild `dashboard.html`** (the deliverable) and re-validate. The
mandated checks live in `scripts/validate_dashboard.py` (JSON embutido +
`node --check` + eval de inicialização com DOM stub) e o `refresh.yml` corre-o
antes do commit; em local:
```bash
venv/bin/python scripts/build_dashboard.py
venv/bin/python scripts/validate_dashboard.py
```

## Data gotchas (verified)
- Join NAP↔MOBI.E by `site_external_id` + last segment of `point_id` (tomada,
  int-normalized). Do NOT join on `point_external_id`: format
  `PT*op*[E]*reg*num*tom` is unreliable (glued `E` prefix, variable segment count).
- `brands_accepted` (NAP) = global CEME list per point, NOT an operator discriminator.
- `facilityLocation` is in the `locationReferencing` namespace, not `locationExtension`.
- NUTS in NAP is level-1 only.
- Dynamic & static point ids match bar 3 missing rows; but 44 points appear 2–3× in dynamic
  status with conflicting states (47 extra rows).
- 33% of connector rows (6 948/21 056) have declared power inconsistent with
  V×I (>25% off); 2 686 declare power above physical capacity (impossible, e.g.
  1200 V × 600 A = 720 kW declared as 200 kW).
- MOBI.E PartyID is a 2022 PDF: 37 active tariff codes missing, 22 unused codes.
- 764 MOBI.E `UID_TOMADA` values are bare numeric ids.
- Power agreement NAP↔MOBI.E is 99.8% (only 27/16 601 diverge >30%).
- OSM: charging sites are tagged two ways — `amenity=charging_station` (node **or**
  way; the way form is the whole site) and `man_made=charge_point` (node only,
  usually one per post/pole). **A site's `ref` can appear under either tag, and
  zero elements carry both tags**, so filter by *either*. In the author's Overpass
  dump: 6 579 `charging_station` (4 720 nodes + 1 859 ways) vs 5 102
  `charge_point` (all nodes, ~4 135 with a MOBI.E-pattern `ref`). The
  `charge_point` nodes usually carry explicit `payment:*`/`authentication:*` tags
  that the `charging_station` elements lack — matching by `charging_station` alone
  hides ~90 ad-hoc payment divergences. `scripts/osm_umap.py` dedups per NAP code
  preferring the row with the most payment/auth tags (tie-break: nearest).

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
- Interactive map: a self-contained SVG (`#map`) rendered from `D.sites` (per-site
  lon/lat) + `D.outline` (PT polygons). Regions live in a `REGIONS` object with
  keys `mainland`/`madeira`/`acores`; site `region` values are `azores` (with a
  `z`), so the map re-maps `azores`→`acores`. Dots are colored by status
  (`STATUS_COLOR`), wheel zooms, drag pans, click shows a detail panel
  (`#mDetail`) with NAP + OSM cross-ref. Filters apply to both table and map;
  map rows are filtered in `renderMap()`, which reads the same multiSel filter
  sets (guarded with `typeof …!=='undefined'` because the map runs before the
  filters are declared).
- Table features: text search across all columns, multi-select dropdown filters
  (estado, região, classe potência, operador, tomada, pagamento), click-to-sort
  headers, pagination (200/page). The payment filter uses `x.pay` (list of OSM
  payment methods: App/Cartão/Cartão de membro/Sem autenticação/Dinheiro) joined
  per-site onto every point row.

## Convenções de escrita (PT-PT técnico)
- **tensão**, nunca "voltagem". Unidades abreviam-se `V`/`A`/`kW` normalmente.
- `voltage`/`max_current` mantêm-se em inglês só quando referem identificadores
  de código ou colunas (CSV, DATEX II, snippets) — em prosa portuguesa é tensão.

## Deliverables
- `dashboard.html` — the interactive dashboard (open with `open dashboard.html`)
- `facts.md` — interesting facts
- `errors.md` — reportable data errors (12 items, for the data owners)
- `Agents-outputs/anomalias-results.md` — output do agente `Agents/anomalias.md`
  (anomalias dos dados estáticos, agrupadas por OPC)