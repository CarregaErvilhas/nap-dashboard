# AGENTS.md — NAP EADME data analysis

Analysis of the Portuguese EV charging network. It produces CSVs, a static multi-page site (`site/`) and reports, and publishes the network model that other projects read. This file is the map and the rules; the manual is in `docs/`. Don't over-engineer.

| Read | Before touching |
| --- | --- |
| [docs/pipeline.md](docs/pipeline.md) | fetching, pipeline scripts, guards, tracker, deliverables |
| [docs/network-model.md](docs/network-model.md) | `ohmigo_dataset.py`, `chargers.json`, OSM joins, models, photos |
| [docs/site.md](docs/site.md) | `assets/`, `site/`, the front end, live status, the map |
| [docs/archive.md](docs/archive.md) | AmpereArchive history, last 24 h, per-site usage |
| [docs/workflows.md](docs/workflows.md) | `.github/workflows/`, secrets, deploy, PR checks, Cloudflare |
| [docs/plan.md](docs/plan.md) | open work |

## Layout
- `scripts/` — the pipeline, the checks (`validate_site.py`, `pipeline_guard.py`, `model_parity.py`, `ci_paths.py`), the site helpers and the anomalies agent's deterministic side, plus `extract_enums.py` and `fetch_schemas.sh`. One-time migrations don't stay here once they've run: git keeps them.
- `ohmigo_dataset.py` is the network model; `opc_tariffs.py` is the one NAP↔MOBI.E tariff join; `osm_tags.py` holds the per-site OSM tags and the OSM-vs-NAP rule. Both the model and the site use them.
- `assets/` — the site's sources (`assets/site/`), outline and basemap JSON, icons, XSD schemas.
- `brand/` — submodule of `CarregaErvilhas/Brand`, pinned to a release tag: mascots, `install.js`, Nunito, the group page's text. The build needs it (`git submodule update --init`); never edit it here ([docs/site.md](docs/site.md)).
- `site/` — generated, committed, what `pages.yml` serves.
- `Agents/` — agent system prompts (see `Agents/AGENTS.md`); their reports go to `Agents-outputs/`.
- `references/` — docs for `SKILL.md` (data sources, gotchas).
- `tests/` — unittest.
- `data/` — everything fetched or derived. Gitignored (`data/*`, `data/.gitkeep` kept).
- The tracker verdicts live in a private cross-check repository, not here.

## Environment
- Always use a local venv, never the system Python (PEP 668 may block pip). `requirements.txt` pins the CI set; the core pipeline needs `pandas` and `lxml`:
  ```bash
  python3 -m venv venv
  venv/bin/pip install pandas lxml
  ```
- Call it as `venv/bin/python`; no absolute paths to this machine's venv.
- Run every script from the repo root: paths are `data/…` relative to it.
- Raw XMLs are big (`data/evChargingInfra_latest.xml`, ~190 MB). Never Read or `cat` them; parse with `scripts/nap_etl.py`.

## Pipeline order
The order `refresh.yml` runs ([details](docs/pipeline.md)):

1. `fetch_data.sh`, `nap_etl.py`
2. `network_news.py` (weekly report)
3. `check_quality.py`, `summary.py`, `mobie_join.py`, `dgeg_lists.py`, `dgeg_crossref.py`
4. `nap_static_checks.py`, `concelho_check.py`, `osm_umap.py`, `osm_planned.py`
5. `fetch_tracker.sh`, `tracker_sync.py`, `tracker_checks.py` (weekly report)
6. `archive_history.py`, `explore_history.py`, `explore_years.py` (optional)
7. `fetch_charger_models.sh`, `charger_photos.py`, `osm_places.py`
8. `ohmigo_dataset.py` (the network model), `hardware_checks.py`, `build_dashboard.py`
9. `pipeline_guard.py`, `model_parity.py`, `validate_site.py`

`make_pt_outline.py` runs by hand, only when `assets/pt_outline.json` is missing. If this list and `refresh.yml` disagree, the workflow wins.

## Build and check
```bash
venv/bin/python scripts/build_dashboard.py   # data + facts/errors + site/
venv/bin/python scripts/validate_site.py
python3 scripts/build_site.py                # pages only, from the committed site/data
python3 -m http.server --directory site      # local preview
```
- After editing `assets/site/*`, `build_dashboard.py` or `build_site.py`, always rebuild `site/` and re-validate.
- Preview over HTTP: `file://` does not work.

## Never
- **No tracker data in git.** `data/tracker_errors.csv`, `data/opc_registry_authority.csv` and `data/tracker_meta.json` are a third party's data with no reuse licence, and this repo is public.
- **Never republish** the cross-check's output or any per-row tracker data. Never commit a copy of the tracker, even to work around a failed fetch.
- **Nothing from the tracker goes into the network model**: the model is public.
- **No tracker URL or file id** in code or workflows: it stays in the `TRACKER_URL` secret.
- **No data files in git or at the repo root.** The root holds only code, docs and deliverables (`site/`, `facts.md`, `errors.md`, `novidades.md`, `network-census.json`, `assets/`, `scripts/`, `Agents/`, `Agents-outputs/`). Moving or renaming a data file means updating `DATA_FILES` in `scripts/ci_paths.py`.
- **The charger-model catalogue is never committed** (`data/charger_models.txt` is fetched on every run). Use only its numbers, never its photos or operator logos, and credit it with its link.
- **Third-party text only as text nodes** (`el()`/`md()` in `common.js`), never `innerHTML` or similar. `validate_site.py` enforces it.
- **No inline `<script>`, no `style` attributes.** The CSP is the `<meta>` in `assets/site/_head.html`; keep `default-src 'none'` and don't loosen it ([docs/site.md](docs/site.md)).
- **A new request or `localStorage` key** must also go into the privacy page (`assets/privacidade.html`, PT and EN).
- **NaN/Inf must become null** before the JSON dump (`clean()` in `build_dashboard.py`).
- **A new fixed PT string** in the pre-rendered panels needs a MAP entry in `dashboard_i18n.py`, or EN users see PT.
- **`SCHEMA` bumps** on any incompatible change to the network model.
- **Never average or compare different kinds of price** (`scripts/price_kinds.py`).
- **Pushes to `main`** come only from the push App in the workflows; agent-written code never reaches `main` on its own ([docs/workflows.md](docs/workflows.md)).

## Data gotchas (verified)
- Join NAP↔MOBI.E by `site_external_id` + last segment of `point_id` (tomada, int-normalized). Do NOT join on `point_external_id`: `PT*op*[E]*reg*num*tom` is unreliable (glued `E` prefix, variable segment count).
- Point ids are unique only within a site (some OPCs publish bare ids like `19`). Always key by `(site_id, point_id)`; the dynamic CSVs carry `site_id` (first `<reference>` of each `energyInfrastructureSiteStatus`). A point that seems to appear 2–3× with conflicting states is this collision, not a feed error.
- `brands_accepted` is the global CEME list per point, NOT an operator discriminator.
- `facilityLocation` is in the `locationReferencing` namespace, not `locationExtension`.
- NUTS in NAP is level-1 only.
- Declared connector power is often inconsistent with V×I, sometimes above what is physically possible.
- `operator_id` is not a reliable OPC key: one id carries several `operator_name`s, and some operators publish under the PartyCode (`BBGE`, `CIRC`, `CONT`). `CONT` is Continente, published under the acquirer's name while the CPO is `CNT`. Use the tracker's PartyId (`tracker_checks.py`). Some sites lack their operator prefix (`CNT-0002PL0012` → `0002PL0012`), so asset matching needs both forms.
- `min_fee = 0` is common and is not a pricing anomaly.
- Every NAP price, also outside MOBI.E, is **without VAT** (confirmed with the NAP), and so are MOBI.E's tariff file values, `AD_HOC_PAYMENT` included. VAT depends on the region (lower on Madeira and the Azores); ohmigo adds it.
- Some MOBI.Data EVSE ids are bare numbers (FCT, ACC, HGP, VIA). `UID_TOMADA` in `data/mobie_tarifas.csv` is synthetic (`<ID>-<socket>-1`) except for those, which keep the bare id for ohmigo's per-site fallback.
- MOBI.Data's per-socket `kw` is the station maximum on every socket, so there is no NAP↔MOBI.E power comparison (errors.md item 2 says "sem dados").
- OSM tags charging sites two ways: `amenity=charging_station` (node or way) and `man_made=charge_point` (node, usually per post). A site's `ref` can be under either and no element has both, so filter by either. `charge_point` nodes usually carry the `payment:*`/`authentication:*` tags.

## Workflows and secrets
- `refresh.yml` runs four times a day and has a weekly report; `pages.yml` deploys; `network-24h.yml` and `site-history.yml` are hourly; `agents.yml` follows the weekly report.
- A refresh publishes only after `pipeline_guard.py`, `model_parity.py` and `validate_site.py` pass.
- `GITHUB_TOKEN` is read-only except for failure issues and the deploy; actions are pinned by SHA.
- Full description, artifacts, secrets and PR checks: [docs/workflows.md](docs/workflows.md).

## Conventions
- Save new analysis code as a script in `scripts/` (or append it to the relevant one) instead of leaving it in the terminal or /tmp. At least note a throwaway one-liner here or in `docs/pipeline.md`.
- PT-PT técnico: **tensão**, nunca "voltagem". Unidades `V`/`A`/`kW`. `voltage`/`max_current` ficam em inglês só quando referem identificadores de código ou colunas (CSV, DATEX II, snippets).
