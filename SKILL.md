---
name: nap-mobie-portugal-ev
description: >-
  Analyse Portugal's public EV charging network from official open data: NAP MOBI.E
  (DATEX II 3.3 static + dynamic), MOBI.E OPC tariffs, DGEG operator registries
  and the PCVE error tracker. Produces a static multi-page site (site/),
  a facts list and a reportable-errors list. Use when the user asks to analyse,
  aggregate, join, map, visualise, audit data quality of, or build a dashboard for
  the Portuguese EV charging network / "rede de carregamento" / NAP MOBI.E / OPC
  tariffs / pontos de carregamento / DGEG. Triggers on words like "NAP", "MOBI.E",
  "mobilidade elétrica", "pontos de carregamento", "tarifário OPC", "EV charging
  Portugal", "carregadores", "rede de carregamento".
---

# NAP MOBI.E — Portuguese EV charging network analysis

Analyses Portugal's public EV charging infrastructure by joining official open
sources. Output: a **static site in `site/`** (three pages, no external libs, data in
`site/data/*.json`, preview with `python3 -m http.server --directory site`), `facts.md`, and `errors.md` (items to report to data owners).

The skill always pulls **fresh data from the official origins** — never rely on a
stale local copy. `scripts/fetch_data.sh` downloads everything (~230 MB).

## What this skill does

1. **Fetch** fresh NAP XMLs, MOBI.E tariff CSV and DGEG pages.
2. **ETL** the two DATEX II XMLs (streaming) into clean CSVs.
3. **Join** NAP points ↔ MOBI.E OPC tariffs (the non-obvious part — see Gotchas).
4. **Resolve** OPC/CEME codes → entities via DGEG registries (OPC identity: the PCVE tracker's PartyId).
5. **Validate** physical/schema sanity and cross-source consistency.
6. **Build** the site + facts + reportable errors.

The current numbers (sites, points, operators, tariff match, power agreement,
V×I inconsistencies) are in `facts.md`, regenerated every week: read them
there instead of copying them here, where they'd go stale.

## Environment

- venv with `pandas`, `lxml`:
  ```bash
  python3 -m venv venv
  venv/bin/pip install pandas lxml
  ```
- Always run scripts from the repo root — data paths are `data/…` **relative to
  it** (`venv/bin/python scripts/nap_etl.py … data`, not from inside `scripts/`).
- Never read the ~190 MB XMLs with the Read tool; parse with `scripts/nap_etl.py`.

## Pipeline

```bash
bash scripts/fetch_data.sh                    # fresh data from origins (see references/data-sources.md)
bash scripts/fetch_tracker.sh                 # PCVE error tracker -> data/pt_pcve_errors.xlsx
venv/bin/python scripts/nap_etl.py            # XML -> data/nap_static_sites.csv, data/nap_static_points.csv,
                                              #        data/nap_dynamic_status.csv, data/nap_dynamic_pricing.csv
venv/bin/python scripts/check_quality.py      # enums + V×I sanity + coords
venv/bin/python scripts/summary.py            # numeric overview
venv/bin/python scripts/mobie_join.py         # NAP ↔ MOBI.E tariffs -> data/nap_opc_points.csv
venv/bin/python scripts/dgeg_lists.py         # DGEG pages -> data/dgeg_opc.csv, data/dgeg_ceme.csv
venv/bin/python scripts/dgeg_crossref.py      # OPC codes -> entities -> data/nap_opc_registry.csv
venv/bin/python scripts/nap_static_checks.py  # NAP-only rules -> data/nap_static_findings.md (errors.md item 8)
venv/bin/python scripts/tracker_sync.py       # PCVE tracker xlsx -> derived CSVs (never versioned)
venv/bin/python scripts/tracker_checks.py     # tracker + NAP -> data/tracker_findings.md (errors.md item 13)
venv/bin/python scripts/build_dashboard.py    # -> site/, facts.md, errors.md
```

`fetch_tracker.sh` / `tracker_sync.py` need the tracker to be fetched: nothing
derived from it is versioned, so without the xlsx there is no cross-check and
errors.md simply has no tracker item. That is deliberate — a frozen copy of
somebody else's error list would go stale silently. Never fails the run.

Outputs to give the user:
- `site/` — preview with `python3 -m http.server --directory site` (`file://` does not work: the pages fetch JSON)
- `facts.md` — interesting facts
- `errors.md` — reportable data errors, numbered; the last item is the PCVE
  tracker cross-check (only present when the tracker was fetched — do not
  hard-code a total, it goes stale)

## Data sources

`references/data-sources.md` has the exact URLs and license notes. Summary:
- **NAP static**: `https://pgm.mobie.pt/integration/nap/evChargingInfra`
- **NAP dynamic**: `https://pgm.mobie.pt/integration/nap/evActualStatus`
- **OPC tariff**: `https://data.mobie.pt/data/tariffs.json` + `https://data.mobie.pt/data/stations.json` (MOBI.Data JSON, converted to `data/mobie_tarifas.csv` by `scripts/mobie_tariffs.py`)
- **DGEG**: OPC-com-reconhecimento-previo and CEME-registados pages
- **PCVE error tracker**: `pt-pcve-errors.xlsx`, the data owners' own error list
  per operator/asset. Not public API — fetched by `scripts/fetch_tracker.sh`
  (anonymous link download; no URL is committed, it lives in the `TRACKER_URL`
  secret). Gives the authoritative OPC table and the only labelled defect set.

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
- Point ids are only unique within a site (bare `19`, `160`… repeat across
  sites): key points by `(site_id, point_id)`. Keyed that way, dynamic matches
  static 1:1 with no conflicting states.
- 30% of connector rows have declared power inconsistent with V×I (>25% off);
  for `mode3AC3p` the physical power is `√3×V×I`, else `V×I`.
- **Site JSON**: sanitize NaN/Inf → null and dump with `allow_nan=False`,
  otherwise the browser's `JSON.parse` fails.

## Site validation (always do this after a rebuild)

```bash
venv/bin/python scripts/validate_site.py
```

It checks that the JSON parses and matches the schema, `node --check` on every
script, no inline scripts, the CSP, no `innerHTML`-style sinks and the live-status
behaviour. If a page renders nothing below the KPIs, it's a JS runtime error — see
`references/gotchas.md`.

## PR checks

`.github/workflows/pr-checks.yml` runs on every PR to `main`: ~1 s, no network,
no dependencies. `scripts/ci_paths.py` asserts that (A) no data file sits in the
repo root, (B) every reference to a data file is `data/`-prefixed, (C) every
`scripts/*` cited in a workflow exists, (D) the tracker's derived files are NOT tracked. Plus `compileall` and `bash -n`.
It also runs `scripts/validate_site.py` on the committed `site/`
(the artifact `pages.yml` publishes unchecked): JSON and schema, JS syntax, no
inline scripts, CSP, no `innerHTML`-style sinks.

It deliberately does **not** run the full pipeline (`fetch_data.sh` is ~230 MB and
`osm_umap.py` pulls an Overpass dump — don't hammer the official sources on every
PR); the weekly `refresh.yml` is the real integration test. When you move or
rename a data file, update `DATA_FILES` in `scripts/ci_paths.py`.

## Layout

- `scripts/` — the pipeline
- `assets/` — `site/` (pages, partials, CSS, JS, fonts), `schemas/*.xsd` (DATEX II 3.3 © CEN; ver `assets/schemas/README.md`)
- `references/` — `data-sources.md`, `gotchas.md`
- `data/` — every fetched or derived file (raw XMLs, CSVs, the tracker xlsx,
  `umap_cache/`, `caop_cache/`), gitignored. Scripts still run from the repo
  root and read `data/…` relative to it.
- Repo root = code, docs and deliverables only (`site/`, `facts.md`,
  `errors.md`, `novidades.md`, `network-census.json`, `assets/`, `Agents-outputs/`)

## When NOT to use

- Real-time streaming or OCPI API access (this uses the public DATEX II dumps).
- The MOBI.Data aggregated portal as a source (it's derived; we use the raw
  NAP feeds).
- Charging data of networks *not* connected to MOBI.E (off-network operators
  must be fetched from their own sources).