# NAP EADME — EV charging network (Portugal)

Analysis of Portugal's EV charging network from official
public data sources. The goal:

- Extract and cross-reference data from several sources (NAP MOBI.E, OPC tariff,
  DGEG registries, OSM/umap)
- Build a **static site** (`site/`) to find chargers and explore the network
- Produce a list of **interesting facts** and a list of **reportable errors** for
  the data owners

## Data sources

| Source | Description | File |
|-------|-----------|----------|
| NAP MOBI.E (DATEX II 3.3) | Static inventory of sites/points | `data/evChargingInfra_latest.xml` |
| NAP MOBI.E (DATEX II 3.3) | Dynamic status (state, prices) | `data/evActualStatus_latest.xml` |
| MOBI.Data OPC tariff | Per-point tariffs (€/kWh, €/min, flat fee) | `data/mobie_tariffs.json` + `data/mobie_stations.json` → `data/mobie_tarifas.csv` |
| DGEG | Recognized OPC and CEME lists | `data/dgeg_opc.csv`, `data/dgeg_ceme.csv` |
| OSM/umap (community) | Overpass dump of the "Postos de Carregamento v2.1" map + "Caça aos Postos" umap | `data/umap_cache/`, `data/osm_umap.csv` |
| PCVE error tracker | Defects reported by the data owners, per operator/asset | `data/pt_pcve_errors.xlsx` (see note below) |

## Results

**Live demo:** <https://nap.ocarroeletrico.com/> (custom domain via CNAME;
auto-published by `.github/workflows/pages.yml` on every `push` that touches
`site/`; regenerated weekly by `.github/workflows/refresh.yml`,
Mondays 06:00 UTC).

- **`site/`** — three-page static site, no external libraries, with the data in
  `site/data/*.json` (local preview: `python3 -m http.server --directory site`;
  `file://` does not work because the pages fetch the JSON). **Bilingual PT/EN**: Portuguese for Portuguese-language
  browsers, English for everyone else (PT|EN button top-right persists the
  choice; `?lang=pt|en` forces a language); auto/light/dark theme and vision
  options (colour-blind, high contrast).
  - **Find** (`index.html`): for drivers. Search by town, operator or code, "Near me"
    (geolocation stays on the device), quick filters, a card per site with one
    status mark per socket, detail with sockets, operator fees, payment and
    "Directions" links (Google Maps, OpenStreetMap), and a canvas map.
  - **Network** (`rede.html`): community statistics (KPIs, news, bar charts as
    tables, history, hubs, facts).
  - **Operators** (`operadores.html`): for the OPCs. Weekly anomaly report per
    operator (from `Agents-outputs/anomalias-results.md`), OPC churn and reportable
    errors.
- **`facts.md`** — interesting facts about the network.
- **`errors.md`** — errors worth reporting to the data owners (includes community
  OSM/umap doubts and operator/payment divergences).

## Running

Requires Python 3.11+ with `pandas` and `lxml`. On machines where system pip is blocked (e.g. PEP 668), use a venv:

```bash
python3 -m venv venv
venv/bin/pip install pandas lxml
```

Pipeline (in dependency order):

```bash
bash scripts/fetch_data.sh            # download fresh data from official origins
venv/bin/python scripts/nap_etl.py    # NAP XML -> static/dynamic CSVs
venv/bin/python scripts/check_quality.py   # quality validation
venv/bin/python scripts/summary.py         # numeric summary
venv/bin/python scripts/mobie_join.py      # join NAP + MOBI.E tariff -> data/nap_opc_points.csv
venv/bin/python scripts/dgeg_lists.py      # DGEG OPC/CEME from the web pages
venv/bin/python scripts/dgeg_crossref.py   # resolve OPC codes -> DGEG entities
venv/bin/python scripts/nap_static_checks.py # placeholder voltages + fake three-phase -> errors.md item 8
venv/bin/python scripts/concelho_check.py    # validate coordinates vs CAOP concelho
venv/bin/python scripts/osm_umap.py          # cross-reference NAP with OSM/umap (community)
venv/bin/python scripts/make_pt_outline.py   # generate assets/pt_outline.json (map)
venv/bin/python scripts/tracker_sync.py  # PCVE tracker -> OPC registry + labelled errors
venv/bin/python scripts/tracker_checks.py # tracker + NAP -> errors.md item 13
venv/bin/python scripts/build_dashboard.py # generate site/, facts.md, errors.md
```

`build_dashboard.py` reads all intermediate CSVs, writes the data to
`site/data/*.json` and renders the pages from `assets/site/` into `site/` (via
`scripts/site_data.py` and `scripts/build_site.py`). To re-render the pages without
the CSVs, from the committed `site/data`: `python3 scripts/build_site.py`.
`scripts/validate_site.py` validates the result.

## Automated agents

System prompts live in `Agents/` (one `.md` file each) and the reports they
produce in `Agents-outputs/`. See `Agents/AGENTS.md` for details.

To run the anomaly agent (static NAP data → per-OPC report), paste this into a
new OpenCode session with cwd at the repo root:

```text
Follow strictly the system prompt in Agents/anomalias.md and execute it
on the current data. Write the report to
Agents-outputs/anomalias-results.md in the exact format defined in the prompt.
```

After adding or editing an agent, validate the eval:

```bash
python3 scripts/check_agents.py
```

## Main files

| File | Role |
|----------|------|
| `scripts/nap_etl.py` | NAP XML parser (static + dynamic) to CSV |
| `scripts/mobie_join.py` | NAP↔MOBI.E join by `site_external_id` + plug |
| `scripts/dgeg_crossref.py` | OPC code → entity resolution (fuzzy match) |
| `scripts/nap_static_checks.py` | Rules on the static NAP alone -> `errors.md` item 8 (placeholder voltages, fake three-phase) |
| `scripts/concelho_check.py` | Coordinate validation vs CAOP concelho boundaries |
| `scripts/osm_umap.py` | Community OSM/umap cross-check (operators, payment, doubts) |
| `scripts/fetch_tracker.sh` | Downloads the PCVE error tracker (no CI credentials; URL kept in a secret) |
| `scripts/tracker_sync.py` | Tracker xlsx -> authoritative OPC registry + labelled defect set |
| `scripts/tracker_checks.py` | Tracker + NAP cross-check -> `errors.md` item 13 (OPC identity, removed assets) |
| `scripts/make_pt_outline.py` | Portugal outline for the SVG map (from CAOP) |
| `scripts/check_quality.py` | Physical/schema sanity checks |
| `scripts/build_dashboard.py` | Computes the data and generates `site/` + facts/errors |
| `scripts/site_data.py`, `scripts/build_site.py` | Split the data into `site/data/*.json` and render the pages |
| `scripts/validate_site.py` | Validates `site/` (JSON, schema, JS, CSP, no `innerHTML`) |
| `assets/site/` | Site source: pages, partials, CSS, JS, Nunito font |
| `assets/pt_outline.json` | PT outline polygons + district/island labels for the map (143 KB) |
| `assets/schemas/*.xsd` | DATEX II 3.3 schemas © CEN (enum source; see `assets/schemas/README.md`, re-fetch `scripts/fetch_schemas.sh`) |
| `SKILL.md` | Reusable skill with all knowledge and the pipeline |

## Intermediate data (CSV)

Everything fetched or derived lives in `data/`, which is gitignored without
exceptions. The repo root holds only code, docs and deliverables.

`sites`, `points`, `status`, `pricing` (NAP output), `nap_opc_points` (NAP
+tariffs), `nap_opc_registry` (OPC code→entity), `mobie_tarifas`, `dgeg_*`.

From the PCVE error tracker: `opc_registry_authority` (PartyId/PartyCode/name, 99
CPOs), `tracker_errors` (3153 labelled defects) and `tracker_meta` (date+sha256).
These are always re-extracted from the source xls on each run and **never
versioned** — they are third-party data with no reuse licence. If the tracker
cannot be fetched, errors.md simply has no tracker item. See
`THIRD-PARTY-NOTICES.md`.

## Engineering notes / pitfalls

- The NAP↔MOBI.E join uses `site_external_id` (= MOBI.E id) + the last segment of
  `point_id` (the plug, int-normalized). **Do not** join on raw `point_external_id`:
  the `PT*op*[E]*reg*num*tom` format is inconsistent (glued `E` prefix, variable
  segment count).
- `brands_accepted` in NAP is the per-point global CEME list, **not** an operator
  discriminator.
- `facilityLocation` lives in the `locationReferencing` namespace, not in
  `locationExtension`.
- Static CSVs are read with `dtype=str` to avoid losing leading zeros.
- Site JSON: use `allow_nan=False` plus NaN/Inf cleaning, otherwise
  the browser's `JSON.parse` fails (bug already fixed).
- OSM/umap: the v2.1 map author's dump (`Todos.json`) covers ~96% of NAP sites
  (8 011/8 357) by MOBI.E code; `man_made=charge_point` nodes carry payment tags
  that `charging_station` elements lack — consider both. The "Caça aos Postos"
  umap lists community doubts, including "nothing on site" points ≤500 m from
  active NAP sites.

## License

Own code (`scripts/`, template, docs, analysis): `PolyForm-Noncommercial-1.0.0` — see `LICENSE`.

- Noncommercial use (individuals, hobby, research, education, public/charitable
  bodies): free to use, modify and share the code and dashboard/site, with
  credit to <https://nap.ocarroeletrico.com/>.
- Commercial use: requires a separate commercial license, agreed case by case.
  Contact: [info@ocarroeletrico.com](mailto:info@ocarroeletrico.com) ·
  [Messenger](https://m.me/OCarroEletricoDotCom).

**Third-party data and schemas are NOT covered by PolyForm** — see
`THIRD-PARTY-NOTICES.md`: NAP/MOBI.E (free use with attribution, no commercial
use; tariff © MOBI.E), DGEG lists (same), CAOP outline © DGT (CC-BY
4.0), OSM data © OpenStreetMap contributors (ODbL 1.0, share-alike) +
v2.1/Caça community maps, DATEX II schemas © CEN. `site/` is a
collective work: our code is PolyForm, published data keeps its original
licences (attribution in footer + map).
