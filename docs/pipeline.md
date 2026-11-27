# Pipeline

How the data is fetched, checked and turned into deliverables. The environment, the order and the data gotchas are in [AGENTS.md](../AGENTS.md).

## Fetch fresh data

```bash
bash scripts/fetch_data.sh
```

```bash
bash scripts/fetch_data.sh
```
Downloads the live NAP XMLs, the MOBI.Data tariff/station JSON and the DGEG HTML pages from the official origins (see `scripts/fetch_data.sh` for the exact URLs), then `scripts/mobie_tariffs.py` builds `data/mobie_tarifas.csv` (the layout `mobie_join.py` and `ohmigo_dataset.py` read) from the two JSON files. mobie.pt does not serve a tariff CSV; see `references/data-sources.md` for what MOBI.Data lacks (grid level, parking time, per-socket power, some sites).

Optional: read the dynamic status (`evActualStatus`, ~40 MB) from the [AmpereArchive](https://github.com/CarregaErvilhas/AmpereArchive) instead of the NAP: `NAP_STATUS_SOURCE=archive AMPERE_ARCHIVE_URL=https://ohm-age.ocarroeletrico.com bash scripts/fetch_data.sh` (country via `AMPERE_ARCHIVE_COUNTRY`, default `PT`). It downloads `v1/PT/status.json.gz` to `data/archiveStatus_latest.json.gz`, and `nap_etl.py` uses it when `data/evActualStatus_latest.xml` is absent (`scripts/archive_status.py` converts it to the same CSVs). A missing, stale (> `ARCHIVE_MAX_AGE_MIN`, 180) or truncated file falls back to the NAP. Default stays `nap`; the static feed still comes from the NAP (the archive does not keep `brandsAccepted`, NUTS or contacts).

## Pipeline order

The order is in [AGENTS.md](../AGENTS.md#pipeline-order). `scripts/network_news.py` is the weekly diff against HEAD's `network-census.json` (→ `novidades.md` + a new `network-census.json`; the first run is the baseline). `scripts/ohmigo_dataset.py` writes the network model, `data/ohmigo_chargers.json`.

## What `build_dashboard.py` writes

`scripts/build_dashboard.py` reads the network model for everything it shows per socket and per site in "Procurar" (see [network-model.md](network-model.md)), and the intermediate CSVs + `data/osm_umap.csv`/`data/osm_caca.csv`/`assets/pt_outline.json`, computes the `data` dict and writes `facts.md`, `errors.md` and the site: it calls `build_site.render(clean(data), 'site', AMPERE_ARCHIVE_URL)`, which splits the payload into `site/data/{stats,panels,sites,points,outline,opc}.json` (`scripts/site_data.py`, lossless) and renders the pages from `assets/site/`. It appends `data/nap_static_findings.md` (written by `scripts/nap_static_checks.py`), `data/concelho_mismatches.md` (written by `concelho_check.py`), `data/osm_umap_findings.md` (written by `scripts/osm_umap.py`), `data/tracker_findings.md` (written by `scripts/tracker_checks.py`) and `data/hardware_findings.md` (written by `scripts/hardware_checks.py`) to `errors.md` when present.

`python3 scripts/build_site.py` re-renders the pages from the committed `site/data` without the CSVs (use it to ship a front-end change between weekly refreshes).

## Guards

`scripts/validate_site.py` (rode no `refresh.yml` antes do commit, no `pr-checks.yml` em cada PR, e em local depois de qualquer build) valida o `site/`: os JSON de `site/data` fazem `json.loads` e cumprem o esquema, cada `.js` passa `node --check`, nenhuma página tem `<script>` inline, a CSP é a esperada, o front end não usa sinks do tipo `innerHTML` (ver [site.md](site.md)) e `applyLive` se comporta com dados sintéticos.

`scripts/pipeline_guard.py` travará o commit se um upstream mudar o formato e o pipeline produzir dados absurdos sem rebentar (limiares mínimos para sites/pontos/join/DGEG/registo) — falha o job e o site online fica no último bom.

## NAP-only rules (`nap_static_checks.py`)

`scripts/nap_static_checks.py` runs the rules on the static NAP alone. Two were mined from the tracker's classes: 750/600 V on a DC connector (legacy placeholder; tracker class 750 → 500 V) and `mode3AC3p` with single-phase voltage and < 11 kW (tracker class `mode3AC3p` → `mode2AC1p`). Two need no adjudication: a DC connector with no voltage, and a voltage above 1500 V, where low voltage ends for DC. They live outside `tracker_checks.py` so they still run when the tracker fetch fails. Writes `data/nap_static_findings.csv` + `.md` (errors.md item 8, subsections 8a–8d, one fixed letter per rule); `build_dashboard.py` imports `findings()` for the item-8 counts.

## Declared voltage vs installed equipment (`hardware_checks.py`)

`scripts/hardware_checks.py` checks the DC voltage the NAP declares against the equipment installed (errors.md item 14), from the network model: the socket's voltage on OSM (`osm.v`, or the NAP's when `osmSame` confirms it) and, on CCS, the rated voltage of the charger OSM maps at the site (`osm.hardware`), looked up in the community's catalogue of models (a Google Doc, "Modelos de Carregadores usados em Portugal": `§.Marca.Modelo` sections with `1000V 200A`).

14a: the NAP and the equipment fall on different sides of 500 V, the threshold of Procurar's "Tensão DC" filter and of ohmigo (the error that changes what an 800 V car gets). 14b: same side, a different value from OSM's, aggregated per operator and pattern (many sockets, mostly one template value per operator). 14c: OSM and the catalogue disagree with each other, the list for someone with a photo of the plate.

The catalogue alone never makes a 14b: the maximum voltage varies between revisions of a model. A site's rating counts only when every charger mapped there is in the catalogue and the DC ones share one voltage.

The catalogue is public and free to use (credit to the catalogue's maintainer: `THIRD-PARTY-NOTICES.md`): `fetch_charger_models.sh` downloads its text export on every run into `data/charger_models.txt` (gitignored, check D of `ci_paths.py`: a copy in git would go stale), and without it item 14 runs on OSM alone and says so. The parser is `charger_models.parse`, shared with the network model's `models` ([network-model.md](network-model.md#charger-models)): it also reads the brands at the end of the document that have no `§.Marca.Modelo` line (Wallbox, Volt-E, Wowplug, XCharge...).

## Concelhos (`concelho_check.py`)

`scripts/concelho_check.py` locates every site inside official CAOP concelho polygons (downloaded on first run into `data/caop_cache/`, gitignored) and flags the sites whose coordinates contradict the concelho implied by the site_id code. Writes `data/concelho_check.csv` + `data/concelho_mismatches.md` (errors.md items 11a/11b), plus `data/concelhos.csv`: all 308 concelhos (278 mainland, 19 Azores, 11 Madeira; it warns on any other count), the denominator of Rede > Concelhos. `load_concelhos()` + `locator()` are reused by `build_dashboard.py` to place the archive's sites ([archive.md](archive.md)).

## Planned sites (`osm_planned.py`)

`scripts/osm_planned.py` reads the same Overpass dump and writes `data/osm_planned.csv`: sites OSM calls planned or under construction (`construction:`/`planned:`/`proposed:` `amenity=charging_station`, a `amenity=charging_station` whose stalls are all `construction:man_made=charge_point` — how Tesla hubs are mapped — or loose stalls grouped within 40 m), minus those whose code the NAP already has. A NAP site within 30 m does not drop one: it is noted in `nap`/`nap_m` (a new fast charger beside an old AC one is common), and Procurar leaves those out.

Each site's `codes` are the NAP codes the community wrote on it, in `ref` **and in the name** (`codes_of`): mappers often put the future code only in the name. `/` replaces the last digits (`ALM-00114/155` = ALM-00114 + ALM-00155, `GDM-00074/75/76` = three), `…` or `...` is an inclusive range (`MLD-00036…39` = four), a range of more than 20 keeps only its first code, and `MOBI-` is dropped.

The network model publishes them as `planned` ([network-model.md](network-model.md#planned)); `build_dashboard.py` reads them from there and appends them to `sites.json` with `lc` = `construction`|`planned`, `status` `planned`, `codes`, `oop` (the OSM id, only under construction: olh'o'posto opens a page for those, not for planned ones) and no points; "Procurar" has an "Estado do posto" filter whose default is in-service only. They are not counted in any KPI. Tests in `tests/test_osm_planned.py`.

## OSM cross-reference (`osm_umap.py`)

`scripts/osm_umap.py` cross-references NAP sites against community OSM data: the Overpass dump `Todos.json` from the author of the "Postos de Carregamento v2.1" umap map (both `amenity=charging_station` and `man_made=charge_point` elements) and the "Caça aos Postos" umap doubt layers. Fetches are cached in `data/umap_cache/`. Matches by MOBI.E `ref` code (strips a `MOBI-` prefix, expands multi-code refs "A;B;C", way polygons use the centroid). Writes `data/osm_umap.csv` (deduped per NAP code, preferring the row with the most payment/auth tags, tie-break: nearest), `data/osm_caca.csv` and `data/osm_umap_findings.md` (errors.md item 12).

## PT outline (`make_pt_outline.py`)

`scripts/make_pt_outline.py` builds `assets/pt_outline.json` (decimated PT outline for the site map **plus per-district/island labels** — `{outline: {region: [rings]}, districts: {region: {name: [lon, lat]}}}`) from the CAOP concelho polygons in `data/caop_cache/`. Mainland labels use the CAOP `Distrito` attribute (18), Madeira/Açores fall back to island name (`Ilha`/`ILHA`, 2+9). Run it once when the outline asset is missing; the JSON is committed.

## PCVE tracker cross-check

`scripts/tracker_sync.py` + `scripts/tracker_checks.py` cross-check the NAP snapshot against the **PCVE error tracker** (`pt-pcve-errors.xlsx`), the data owners' own error list per operator/asset. Refresh cycle:

```bash
bash scripts/fetch_tracker.sh                # TRACKER_URL, or gog, or skip
venv/bin/python scripts/tracker_sync.py     # xlsx -> data/tracker_*.csv (derivados, fora do git)
venv/bin/python scripts/tracker_checks.py   # CSVs + NAP -> findings
```

- `fetch_tracker.sh` has two strategies, neither of which may fail the pipeline: `TRACKER_URL` (anonymous download — **what CI uses**, since the file's owner shares it as "anyone with the link", so no credentials are needed), then `gog` (authenticated Drive download, for when link sharing is off — local only). Nothing is versioned: if both fail, `tracker_sync.py` skips and `tracker_checks.py` warns, so errors.md simply has **no** tracker item for that run. `nap-dashboard` is a **public** repo, so keep that URL in the `TRACKER_URL` repo secret, never as a literal in the workflow — otherwise the repo publishes a permanent pointer to the data owners' file. Set the secret to the shareable download URL of the xlsx.
- **Google blocks other endpoints from the runners.** The tracker is an **xlsx (Office file) hosted on Google Drive**, not a native Google Sheet, and `TRACKER_URL` is Drive's export download endpoint (`…export=download…`): that is what gets past the block on GitHub-hosted runners. The Sheets API and `/spreadsheets/…/export?format=xlsx` reject an Office file with `400 failedPrecondition: must not be an Office file`. `fetch_tracker.sh` reports the HTTP status when a fetch fails (`HTTP 403`/`429` = blocked or rate-limited, `200` + non-ZIP = Drive interstitial). Do not work around a failure by committing a copy of the tracker.
- `data/tracker_meta.json` carries `synced_at` + the xlsx `sha256` on every run, so errors.md item 13 always states which version of the tracker it came from.
- Deciding which `TO FIX` rows are now fixed in the NAP is **not done here**: it lives in a private cross-check repository (which uses this repo's `scripts/nap_etl.py` at a pinned commit). It covers Voltage, Amperage, Power, Charge mode, Plug type, Location (≤10 m FIXED / ≤30 m POSSIBLE), Payment info and Register, and its verdicts are only *candidates* for the owners to flip to `FIXED`. The old `tracker_fixed.py` was removed to avoid two copies of the same cross-check. **Never republish its output (or any per-row tracker data) in this public repo**: the tracker has no reuse licence.
- Products: `data/opc_registry_authority.csv` (the only *current* OPC identity table — `PartyId | PartyCode | name`) and `data/tracker_errors.csv` (the project's only labelled/ground-truth set: real defects with the value the owner considers correct, plus `notes_class`).
- `tracker_checks.py` writes `data/tracker_findings.md`/`.csv` (errors.md item 13). Rules: OPC sem PartyId resolúvel, PartyCode em vez de PartyId (e.g. BBGE, CIRC, CONT), nomes fragmentados, assets declarados removidos ainda publicados; the counts are in the generated file. The NAP-only rules mined from the tracker (placeholder DC voltages; `mode3AC3p` without three-phase power) are in `scripts/nap_static_checks.py`, errors.md item 8. The rules are mined from the tracker's own classes (750→500 V, `mode3AC3p`→`mode2AC1p`), which is what makes them non-speculative.
- Known limits: OPC identity resolves by `operator_name`, so an operator that renames itself drops out until the tracker catches up; `min_fee = 0` is common in the pricing rows, so zero is **not** a pricing anomaly.

## Build and preview

## Build command
```bash
venv/bin/python scripts/build_dashboard.py   # data + facts/errors + site/
venv/bin/python scripts/validate_site.py
python3 scripts/build_site.py                # pages only, from the committed site/data
python3 -m http.server --directory site      # local preview
```
After editing `assets/site/*` or `scripts/build_dashboard.py`/`build_site.py`, **always rebuild `site/`** (the deliverable) and re-validate. `file://` does not work: the pages fetch their JSON, so preview over HTTP. `refresh.yml` runs `validate_site.py` before the commit.

## Deliverables

- `site/` — the static site (preview: `python3 -m http.server --directory site`)
- `facts.md` — interesting facts
- `novidades.md` — weekly network news (new/removed sites, OPC moves, power records; panel on "Rede", EN via `dashboard_i18n.MAP`) with `network-census.json` (committed state for next week's diff)
- `errors.md` — reportable data errors, numbered, for the data owners; the last item is the tracker cross-check, appended from `data/tracker_findings.md` when the tracker was fetched (don't hard-code the total, it changes)
- `Agents-outputs/anomalias-results.md` — output do agente `Agents/anomalias.md` (anomalias dos dados estáticos, agrupadas por OPC)
- `/ohmigo/chargers.json` on Pages — the ohmigo dataset (Actions artifact, see [network-model.md](network-model.md)). `pages.yml` serves `site/` as the web root plus a `/dashboard.html` redirect to `/`, and also publishes `robots.txt`, `sitemap.xml` and `/.well-known/security.txt` (RFC 9116; `Expires` 180 days from each deploy).
