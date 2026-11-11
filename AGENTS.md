# AGENTS.md — NAP EADME data analysis

## Project type
Single-machine analysis of the Portuguese EV charging network. Pinned runtime
deps in `requirements.txt` (Dependabot, monthly); CI in `.github/workflows/`
(weekly `refresh.yml` pipeline + `pages.yml` deploy + `agents.yml`). Code
produces CSVs + a static multi-page site (`site/`, `facts.md`, `errors.md`),
validated by `scripts/validate_site.py` + `scripts/pipeline_guard.py`. Don't over-engineer.

## Layout
- `scripts/` — the pipeline (in the order of "Pipeline order" below, plus
  `extract_enums.py`, `fetch_schemas.sh` and the manual `tracker_fixed.py`);
  the checks (`validate_site.py`, `pipeline_guard.py`, `ci_paths.py`);
  the site helpers (`site_data.py`, `build_site.py`, `dashboard_payload.py`,
  `dashboard_i18n.py`); the
  anomalias agent's deterministic side (`anomalias_summary.py`,
  `anomalias_evidence.py`, `anomalias_check.py`, `format_anomalias.py`,
  `check_agents.py`); `ohmigo_dataset.py` (the network model, below) with
  `model_parity.py` (the site shows what the model says); `opc_tariffs.py`
  (the one NAP↔MOBI.E tariff join, shared by the model and `mobie_join.py`);
  and `osm_tags.py` (the per-site OSM tags from the Overpass dump and the
  OSM-vs-NAP rule per socket, shared by the model and the site). One-time
  migrations don't stay here once they've run: git keeps them.
- `assets/` — `site/` (the site's sources: `index.html`, `rede.html`,
  `operadores.html`, the `_head/_header/_footer.html` partials, `app.css`,
  `boot.js`, `common.js`, `find.js`, `rede.js`, `operadores.js`, `fonts/Nunito`),
  `privacidade.html`, `404.html`, `llms.txt`, `pt_outline.json` (PT outline for
  the map), `pt_basemap.json` (OSM places + main roads for the map; refresh by hand with `scripts/make_pt_basemap.py`, copied to `site/data/basemap.json`), `schemas/*.xsd` (DATEX II 3.3 © CEN; ver `assets/schemas/README.md`)
- `references/` — docs for the SKILL.md (data sources, gotchas)
- `Agents/` — system prompts dos agentes automáticos (um `.md` por agente; ver
  `Agents/AGENTS.md`). Atual: `Agents/anomalias.md` (anomalias dos dados
  estáticos NAP → `Agents-outputs/anomalias-results.md`, agrupado por OPC).
- `Agents-outputs/` — relatórios gerados pelos agentes (ex.
  `Agents-outputs/anomalias-results.md`).
- `data/` — everything fetched from a source or derived by the pipeline: raw XMLs,
  the MOBI.E tariff CSV, the DGEG HTML/CSV, all intermediate CSVs,
  the tracker's `data/pt_pcve_errors.xlsx`, and the `data/umap_cache/` (umap maps/OSM
  dump) + `data/caop_cache/` (CAOP concelho polygons) caches. All gitignored
  (`data/*`, with `data/.gitkeep` kept), tracker derivatives included (below).
  Still run every script from the repo root — paths are `data/…` relative to it.
- **Nothing derived from the tracker is versioned.** `data/tracker_errors.csv`,
  `data/opc_registry_authority.csv` and `data/tracker_meta.json` are
  re-extracted from the source xlsx on every run and stay out of git: they are
  a third party's data with no reuse licence, and this repo is public.
- The repo root holds only code, docs and deliverables: `site/`,
  `facts.md`, `errors.md`, `novidades.md`,
  `network-census.json`, `assets/`, `scripts/`, `Agents/`, `Agents-outputs/`.

## Environment
- Create and use a local venv — never rely on the system Python (it may be a
  recent version where pip is blocked by PEP 668). The core pipeline needs
  `pandas` and `lxml` (`requirements.txt` pins the full CI set):
  ```bash
  python3 -m venv venv
  venv/bin/pip install pandas lxml
  ```
- Reference the venv interpreter as `venv/bin/python` in commands; do not
  hardcode absolute paths to this machine's venv.
- Raw XMLs are big (`data/evChargingInfra_latest.xml` ~190 MB). Don't read them with
  the Read tool or cat them; parse with `scripts/nap_etl.py`.

## Fetch fresh data
```bash
bash scripts/fetch_data.sh
```
Downloads the live NAP XMLs, the MOBI.Data tariff/station JSON and the DGEG
HTML pages from the official origins (see `scripts/fetch_data.sh` for the exact
URLs), then `scripts/mobie_tariffs.py` builds `data/mobie_tarifas.csv` (the layout
`mobie_join.py` and `ohmigo_dataset.py` read) from the two JSON files. mobie.pt
does not serve a tariff CSV; see `references/data-sources.md` for what MOBI.Data
lacks (grid level, parking time, per-socket power, some sites).

Optional: read the dynamic status (`evActualStatus`, ~40 MB) from the
[AmpereArchive](https://github.com/CarregaErvilhas/AmpereArchive) instead of the
NAP: `NAP_STATUS_SOURCE=archive AMPERE_ARCHIVE_URL=https://ohm-age.ocarroeletrico.com bash scripts/fetch_data.sh`
(country via `AMPERE_ARCHIVE_COUNTRY`, default `PT`). It downloads
`v1/PT/status.json.gz` to `data/archiveStatus_latest.json.gz`, and
`nap_etl.py` uses it when `data/evActualStatus_latest.xml` is absent
(`scripts/archive_status.py` converts it to the same CSVs). A missing, stale
(> `ARCHIVE_MAX_AGE_MIN`, 180) or truncated file falls back to the NAP. Default
stays `nap`; the static feed still comes from the NAP (the archive does
not keep `brandsAccepted`, NUTS or contacts).

## Histórico (AmpereArchive, opcional)
`scripts/archive_history.py` lê o Parquet do
[AmpereArchive](https://github.com/CarregaErvilhas/AmpereArchive) com DuckDB e
escreve `data/archive_stats.json`; o `build_dashboard.py` mostra-o no painel
"Histórico" (`scripts/archive_panel.py`, PT+EN) e esconde-o quando o ficheiro
não existe. Cálculos em `scripts/archive_stats.py`, testes em `tests/`:
```bash
venv/bin/pip install duckdb
venv/bin/python scripts/archive_history.py --url https://ohm-age.ocarroeletrico.com   # ou AMPERE_ARCHIVE_URL
venv/bin/python -m unittest discover -s tests
```
- Fonte: `--url` descarrega para `data/archive_cache/` os ficheiros que
  `v1/<CC>/manifest.json` lista (o endereço não lista; o coletor reescreve o
  manifest depois de cada hora, e ele inclui o backfill `part-backfill`/`part-ocpi`).
  Sem manifest, gera os nomes `part-<HH>` desde `ARCHIVE_EPOCH` e aceita 404,
  e aí o backfill não entra. `--root DIR | s3://bucket` lê uma cópia local ou o R2.
  Janela `--days 28`; `static_versions` vem sempre desde o 1.º dia.
- Modelo: o snapshot diário é o ponto de partida (instante = `publication_time`
  da 1.ª leitura de estado do dia depois do retrato estático); os eventos
  aplicam-se por cima e cada snapshot seguinte corrige o estado. A
  `coverage.anchor_mismatch` tem de ficar a 0 (1.º evento depois do snapshot
  com `prev_status` ≠ estado do snapshot). As lacunas de recolha (`polls`,
  leituras boas separadas por > 5 min) saem do tempo observado.
- Stats: (1) % do tempo `outOfOrder`/`inoperative` por OPC; (2) episódios
  `outOfOrder`/`inoperative` → `available` (mediana dos fechados; saídas para
  `charging`/outro, abertos e censurados contados à parte); (3) ocupação
  dia × hora local (Lisboa/Açores/Madeira pelas coordenadas), DC vs AC pelo
  `mode` dos conectores; (4) tomadas paradas e tomadas que oscilam com
  `unknown`; (5) locais/tomadas/kW por semana desde o retrato inicial.
- Cada stat diz quantos dias tem por trás e fica "preliminar" abaixo de
  `NEEDS_DAYS` (ocupação e reparação: 14 dias). Os estados são declarados
  pelos operadores, não medidos; dados NAP, uso não comercial.
- No `refresh.yml`: passo `continue-on-error` antes do `build_dashboard.py`
  (precisa de `vars.AMPERE_ARCHIVE_URL`; sem ela, ou se falhar, o site
  sai sem o painel). `data/archive_cache/` fica em `actions/cache` entre
  corridas; o sync apaga os dias fora da janela (menos `static_versions`).
  Um 403 conta como erro, nunca como "hora sem ficheiro".

## Pipeline order
`scripts/nap_etl.py` → (`scripts/check_quality.py`, `scripts/summary.py`) →
`scripts/mobie_join.py` → `scripts/dgeg_lists.py` → `scripts/dgeg_crossref.py` →
`scripts/nap_static_checks.py` → `scripts/concelho_check.py` →
`scripts/osm_umap.py` → `scripts/tracker_sync.py` + `scripts/tracker_checks.py` →
`scripts/make_pt_outline.py` →
`scripts/network_news.py` (diff semanal vs `network-census.json` do HEAD →
`novidades.md` + novo `network-census.json`; primeira corrida = baseline) →
(`scripts/osm_places.py`) → `scripts/ohmigo_dataset.py` (the network model,
`data/ohmigo_chargers.json`) → `scripts/build_dashboard.py` →
`scripts/model_parity.py`.
`scripts/build_dashboard.py` reads the network model for everything it shows
per socket and per site in "Procurar" (see "Network model"), and the
intermediate CSVs +
`data/osm_umap.csv`/`data/osm_caca.csv`/`assets/pt_outline.json`, computes the
`data` dict and writes `facts.md`, `errors.md` and the site: it calls
`build_site.render(clean(data), 'site', AMPERE_ARCHIVE_URL)`, which splits the
payload into `site/data/{stats,panels,sites,points,outline,opc}.json`
(`scripts/site_data.py`, lossless) and renders the pages from `assets/site/`.
It appends
`data/nap_static_findings.md` (written by `scripts/nap_static_checks.py`),
`data/concelho_mismatches.md` (written by `concelho_check.py`),
`data/osm_umap_findings.md` (written by `scripts/osm_umap.py`) and
`data/tracker_findings.md` (written by `scripts/tracker_checks.py`) to `errors.md`
when present.
`python3 scripts/build_site.py` re-renders the pages from the committed
`site/data` without the CSVs (use it to ship a front-end change between weekly
refreshes).

`scripts/validate_site.py` (rode no `refresh.yml` antes do commit, no
`pr-checks.yml` em cada PR, e em local depois de qualquer build) valida o
`site/`: os JSON de `site/data` fazem `json.loads` e cumprem o esquema,
cada `.js` passa `node --check`, nenhuma página tem `<script>` inline, a CSP é
a esperada, o front end não usa sinks do tipo `innerHTML` (ver "Site
specifics") e `applyLive` se comporta com dados sintéticos.
`scripts/pipeline_guard.py` travará o commit se um upstream mudar o formato e o
pipeline produzir dados absurdos sem rebentar (limiares mínimos para
sites/pontos/join/DGEG/registo) — falha o job e o site online fica no
último bom.

`scripts/nap_static_checks.py` runs the rules on the static NAP alone that
were mined from the tracker's classes: 750/600 V on a DC connector (legacy
placeholder; tracker: 171 rows of 750 → 500 V) and `mode3AC3p` with
single-phase voltage and < 11 kW (tracker: 199 rows of `mode3AC3p` →
`mode2AC1p`). They live outside `tracker_checks.py` so they still run when the
tracker fetch fails. Writes `data/nap_static_findings.csv` + `.md` (errors.md
item 8, subsections 8a/8b); `build_dashboard.py` imports `findings()` for the
item-8 counts.

`scripts/concelho_check.py` locates every site inside official CAOP concelho
polygons (downloaded on first run into `data/caop_cache/`, gitignored) and flags the
sites whose coordinates contradict the concelho implied by the site_id code.
Writes `data/concelho_check.csv` + `data/concelho_mismatches.md` (errors.md items 11a/11b).

`scripts/osm_planned.py` reads the same Overpass dump and writes `data/osm_planned.csv`:
sites OSM calls planned or under construction (`construction:`/`planned:`/`proposed:`
`amenity=charging_station`, a `amenity=charging_station` whose stalls are all
`construction:man_made=charge_point` — how Tesla hubs are mapped — or loose stalls
grouped within 40 m), minus those already in the NAP (ref match or ≤30 m).
`build_dashboard.py` appends them to `sites.json` with `lc` = `construction`|`planned`,
`status` `planned` and no points; "Procurar" has an "Estado do posto" filter whose default
is in-service only. They are not counted in any KPI.

`scripts/osm_umap.py` cross-references NAP sites against community OSM data: the
Overpass dump `Todos.json` from the author of the "Postos de Carregamento v2.1"
umap map (both `amenity=charging_station` and `man_made=charge_point` elements)
and the "Caça aos Postos" umap doubt layers. Fetches are cached in `data/umap_cache/`.
Matches by MOBI.E `ref` code (strips a `MOBI-` prefix, expands multi-code refs
"A;B;C", way polygons use the centroid). Writes `data/osm_umap.csv` (deduped per NAP
code, preferring the row with the most payment/auth tags), `data/osm_caca.csv` and
`data/osm_umap_findings.md` (errors.md item 12).

`scripts/make_pt_outline.py` builds `assets/pt_outline.json` (decimated PT
outline for the site map **plus per-district/island labels** — `{outline:
{region: [rings]}, districts: {region: {name: [lon, lat]}}}`) from the CAOP
concelho polygons in `data/caop_cache/`. Mainland labels use the CAOP `Distrito`
attribute (18), Madeira/Açores fall back to island name (`Ilha`/`ILHA`, 2+9).
Run it once when the outline asset is missing; the JSON is committed.

`scripts/tracker_sync.py` + `scripts/tracker_checks.py` cross-check the NAP
snapshot against the **PCVE error tracker** (`pt-pcve-errors.xlsx`), the data
owners' own error list per operator/asset. Refresh cycle:

```bash
bash scripts/fetch_tracker.sh                # TRACKER_URL, or gog, or skip
venv/bin/python scripts/tracker_sync.py     # xlsx -> data/tracker_*.csv (derivados, fora do git)
venv/bin/python scripts/tracker_checks.py   # CSVs + NAP -> findings
```

- `fetch_tracker.sh` has two strategies, neither of which may fail the pipeline:
  `TRACKER_URL` (anonymous download — **what CI uses**, since the file's owner
  shares it as "anyone with the link", so no credentials are needed), then `gog`
  (authenticated Drive download, for when link sharing is off — local only).
  Nothing is versioned: if both fail, `tracker_sync.py` skips and `tracker_checks.py`
  warns, so errors.md simply has **no** tracker item for that run. `nap-dashboard`
  is a **public** repo, so keep that URL in the `TRACKER_URL` repo secret, never
  as a literal in the workflow — otherwise the repo publishes a permanent pointer
  to the data owners' file. Set the secret to the shareable download URL of the xlsx.
- **Google blocks other endpoints from the runners.** The tracker is an
  **xlsx (Office file) hosted on Google Drive**, not a native Google Sheet, and
  `TRACKER_URL` is Drive's export download endpoint (`…export=download…`): that
  is what gets past the block on GitHub-hosted runners. The Sheets API and
  `/spreadsheets/…/export?format=xlsx` reject an Office file with `400
  failedPrecondition: must not be an Office file`. `fetch_tracker.sh` reports
  the HTTP status when a fetch fails (`HTTP 403`/`429` = blocked or
  rate-limited, `200` + non-ZIP = Drive interstitial). Do not work around a
  failure by committing a copy of the tracker.
- `data/tracker_meta.json` carries `synced_at` + the xlsx `sha256` on every run,
  so errors.md item 13 always states which version of the tracker it came from.
- `scripts/tracker_fixed.py` (run after `nap_etl.py` + `tracker_sync.py`) replaces
  the manual match: for each `TO FIX` row with a `correct_data` it finds the site
  (same `asset_variants` as `tracker_checks.py`) and compares the current NAP
  value with the wrong and the correct one. Verdicts: `FIXED_CANDIDATA`,
  `AINDA_ERRADO`, `MISTO` (wrong and correct coexist on the site — several
  connectors, review by hand), `ALTERADO_OUTRO`, `SITE_NAO_ENCONTRADO`,
  `NAO_VERIFICAVEL` (Register/Payment info/Cable/Tariff have no static NAP
  field). Covers Voltage, Amperage, Power, Charge mode, Plug type, Location
  (≤25 m of the correct coordinates). Writes `data/tracker_fixed.csv` + `.md`
  (gitignored). Backtested on the tracker's already-`FIXED` rows: Location,
  Amperage and Charge mode are recovered almost always; Voltage is weak (many
  `MISTO`), so only `FIXED_CANDIDATA` is trustworthy there. These are
  *candidates* for the owners to flip to `FIXED`, never an automatic status change.
- Products: `data/opc_registry_authority.csv` (the only *current* OPC identity table —
  `PartyId | PartyCode | name`, 99 CPO) and
  `data/tracker_errors.csv` (the project's only labelled/ground-truth set: 3153 real
  defects with the value the owner considers correct, plus `notes_class`).
- `tracker_checks.py` writes `data/tracker_findings.md`/`.csv` (errors.md item 13).
  Rules: OPC sem PartyId resolúvel, PartyCode em vez de PartyId (e.g. BBGE,
  CIRC, CONT), nomes fragmentados, assets declarados removidos ainda
  publicados; the counts are in the generated file. The NAP-only rules mined from the tracker (placeholder DC
  voltages, 58; `mode3AC3p` without three-phase power, 35 rows / 24 sites) are
  in `scripts/nap_static_checks.py`, errors.md item 8.
  The rules are mined from the tracker's own classes (171 rows of 750→500 V,
  199 of `mode3AC3p`→`mode2AC1p`), which is what makes them non-speculative.
- Known limits: OPC identity resolves by `operator_name`, so an operator that
  renames itself drops out until the tracker catches up; `min_fee = 0` covers
  46% of pricing rows, so zero is **not** a pricing anomaly.

## Network model (ohmigo dataset)
`scripts/ohmigo_dataset.py` builds `data/ohmigo_chargers.json`, **the network
model**: the one place that decides what is true about each charger. Two
readers: the ohmigo MCP server (EV charging cost answers for ChatGPT/Claude)
and this repo's site, whose `build_dashboard.py` takes each socket's power,
operator fees, regime and NAP-only issues from it (`site/data/points.json`
`kw`/`kw_src`/`nap_kw`/`fees`/`regime`/`nap`/`issues`, and each site's `kw` and
`dcv` in `sites.json`). Before, the site computed its own from the same CSVs and
the two drifted (fees cut to the first €/min tier, kW rounded to the unit, the
short-`UID_TOMADA` matches only ohmigo had, OSM's power only ohmigo applied).
`scripts/model_parity.py` runs after the build in `refresh.yml` and fails the
refresh if `site/data` disagrees with the model of the same run. The Rede
statistics stay on what the NAP declares (`max_power_w`, `pw_class`,
`data/nap_opc_points.csv`): they describe the NAP's publication.
The OPC tariffs come from `scripts/opc_tariffs.py`, the same join
`mobie_join.py` uses for `data/nap_opc_points.csv`, so the stats and the model
agree on which socket has which fee.
Contents: sites, points, power,
the connector's declared tensão (`v`, V) and max current (`a`, A), the grid
voltage level (`level`: BTN/BTE/MT, which picks the TAR; **always `null`**,
because neither MOBI.Data nor the NAP publishes it) and the **raw** MOBI.E OPC tariffs per socket (every €/min tier and
the `AD_HOC_PAYMENT` plan, which `data/nap_opc_points.csv` collapses to one value),
whether the cable is attached (`cable`, from `connectorFormat`), the NAP's site
`name`, opening `hours` (converted by `nap_etl.py` from DATEX II
`operatingHours` to OSM `opening_hours` syntax: `24/7`, `Mo-Su 09:00-21:00`),
`locationDescription` ("Parque Coberto - Piso -1") and the operator's `phone`,
plus a per-site `osm` block (name, brand, operator, opening hours, location,
access, parking fee, maxstay, level, covered, indoor, phone, email,
manufacturer, model, capacity, `payment` = the `payment:*`/`authentication:*`
methods tagged yes, and `cards` = true/false when OSM says whether a bank card
works at the charger) and a per-point `osm` with the kW/V/A of the matching OSM
`socket:*` (same plug type, nearest power), **only where it differs from the
NAP** — read off the charger's plate by the community, it is usually more
right than the NAP's declaration (DC placeholders 750/600 V, impossible
powers), so the model applies it: `kw`/`v`/`a`/`cable` are OSM's and the NAP's
value goes to `napKw`/`napV`/`napA`/`napCable`, present only when replaced
(`null` = the NAP declared none). An OSM number has to be plausible first
(`osm_tags.sane_osm`: at most 1000 kW / 1500 V / 1500 A, and within ×20 kW or
×10 V/A of a plausible NAP value), or it is dropped. ohmigo made this call itself
until the model did; it now reads the result. Per point, `issues` lists what
the NAP-only rules of `nap_static_checks.py` found on it (`tensao_placeholder`,
`trifasico_sem_3p`, errors.md item 8). Nothing from the PCVE tracker goes into
the model: it is a third party's data with no reuse licence, and the model is
public. Where OSM agrees with the NAP, the point
lists those fields in `osmSame` (`["a", "v"]`), so ohmigo can tell a value
confirmed on the charger from one only the operator declared (a DC socket's
current decides the power a 400 V car gets). All joined from the Overpass dump in
`data/umap_cache/todos.json` by `ref` = NAP `external_id` (any code form, so
Continente's `0001PL0002` joins too; ≤1 km from the NAP point). It's what lets
ohmigo find "o posto do Lidl de Coimbra": OSM's `brand`/`operator` are often
the owner, not the CPO (Lidl owns its chargers, Galp operates them: the NAP
says Galp, OSM says Lidl). Additive and optional, so no `SCHEMA` bump;
without the dump (osm_umap.py not run) sites just lack `osm`. ODbL: see
`THIRD-PARTY-NOTICES.md`.
The `osm` block also has `hardware`: every charger make + model mapped at the
site, most common first (`["ABB Terra HP CP4", "Alpitronic HYC_400"]`;
`manufacturer`/`model` are only the commonest). The site shows the same list
(`hw` in `sites.json`, "Carregadores: …" in the detail) and its search finds
a site by it. Both come from `scripts/osm_tags.py`, so the site and ohmigo
never disagree about a charger. An element > 1 km from the NAP point is a
wrong `ref` on OSM, not a second charger, and is left out.
Also from `osm_tags.py`, in both the `osm` block and `sites.json`:
- `sharedKw` (`shared`): the total a charger declares
  (`charging_station:output`/`charge_point:output`) when it is below its
  sockets charging together. DC plugs of one multi-standard charger
  (CCS + CHAdeMO) don't add up, only the largest DC type × its count plus the
  AC sockets, so a 50 kW triple charger with a 50 kW CCS is not "shared".
- `oldRefs` + `oldOperator` (`old`, `oldop`): OSM `old_ref`/`old_operator`,
  the sticker of a charger that changed operator. An old code that is another
  site's code now is dropped. Searchable on the site and in ohmigo.
- `wheelchair` (`wc`): OSM `wheelchair` yes/limited/no; the site and ohmigo
  also read the NAP's DATEX II `accessibility` (`nap_etl.py` writes it to
  `nap_static_sites.csv`; `wheelChairAccessible`/`disabilityAccessible`/
  `barrierFreeAccessible` = yes). The "Acessível em cadeira de rodas" filter
  keeps yes and limited; very few sites say anything, and the help text says
  that missing information is not "inaccessible".
- `fixme`: the community's open questions on OSM, shown on the site as
  "Por confirmar no OpenStreetMap"; ohmigo keeps up to 3, cut at 160
  characters, and tells the assistant to present them as things to check on
  site, never as facts.
- `evse` (dataset build only, never written): OSM `ref:EU:EVSE` per element,
  matched to the NAP `point_external_id` (`evse_key`), so a socket's OSM
  kW/V/A come from the element that is that socket; the plug + nearest power
  match over the whole site stays the fallback.
Also per site, `places`: the shopping centres, hospitals, universities, airports,
stadiums, supermarkets, car parks and hotels (named, from OSM) whose outline holds
the site or lies a few metres from it, `{name, type, osm, m}` (`m` = metres to
the edge, 0 = inside; up to 3, inside first). OSM doesn't say which place a
charger is at, so `scripts/osm_places.py` works it out (point in polygon, stdlib
only) from `data/umap_cache/places.json`, which it builds with `osmium`
(pyosmium) from Geofabrik's Portugal extract: `refresh.yml` downloads
`portugal-latest.osm.pbf` (~400 MB) and runs
`python scripts/osm_places.py <pbf>` (~10 s) with `continue-on-error` before
the dataset; without the cache sites just lack `places`. Overpass was tried
first and timed out even on half-degree tiles. The radius outside the outline
depends on the type (a hotel or car park only counts right beside it), and a
place whose name repeats one already kept is dropped (two OSM objects for the
same mall, "Centro Comercial Colombo - Estacionamento Piso -1").
It's what lets ohmigo find "os postos do Mar Shopping", which no charger is named.
No status and no CEME prices: ohmigo reads status live from the NAP feed and gets
energy prices from ceme-v2. `refresh.yml` builds it before the site (the site
reads it) and uploads it, only after the pipeline guard, the parity check and
`validate_site.py` pass, as the `ohmigo-dataset` Actions artifact (90-day retention; not
committed: ~10 MB a week; not a release, because the repo's releases are
immutable and an asset can't be replaced); `pages.yml` copies the newest one to
`https://nap.ocarroeletrico.com/ohmigo/chargers.json`, accepting only artifacts
from a `refresh.yml` or `ohmigo-daily.yml` run on `main` of this repo, triggered
by `schedule` or `workflow_dispatch`, not already failed (fork PRs can upload an
artifact with the same name). It exits non-zero (and the
refresh fails) below 5 000 sites or 10 000 tariffed points. `SCHEMA` in the
script bumps on incompatible format changes.

A daily refresh (`ohmigo-daily.yml`, cron `49 2,14 * * *`) re-runs only the ohmigo
pipeline (NAP ETL + OSM dump + places + dataset) and publishes a new
`ohmigo-dataset` artifact (30-day retention), then triggers a Pages deploy, so
the MCP sees fresher OSM/NAP data between weekly refreshes. It does not build
the site or commit to `main`.

## Housekeeping: save ad-hoc analysis scripts
When an interactive query ends up producing new analysis code (point-in-polygon,
cross-checks, one-off joins), save it as a script in `scripts/` (or append it to
the relevant pipeline script) instead of leaving it in the terminal or /tmp —
future re-runs should not regenerate all that code from scratch. If it's a
throwaway one-liner, at least note it in AGENTS.md so it can be rebuilt.

## Build command
```bash
venv/bin/python scripts/build_dashboard.py   # data + facts/errors + site/
venv/bin/python scripts/validate_site.py
python3 scripts/build_site.py                # pages only, from the committed site/data
python3 -m http.server --directory site      # local preview
```
After editing `assets/site/*` or `scripts/build_dashboard.py`/`build_site.py`,
**always rebuild `site/`** (the deliverable) and re-validate. `file://` does not
work: the pages fetch their JSON, so preview over HTTP. `refresh.yml` runs
`validate_site.py` before the commit.

## Data gotchas (verified)
- Join NAP↔MOBI.E by `site_external_id` + last segment of `point_id` (tomada,
  int-normalized). Do NOT join on `point_external_id`: format
  `PT*op*[E]*reg*num*tom` is unreliable (glued `E` prefix, variable segment count).
- `brands_accepted` (NAP) = global CEME list per point, NOT an operator discriminator.
- `facilityLocation` is in the `locationReferencing` namespace, not `locationExtension`.
- NUTS in NAP is level-1 only.
- Point ids are only unique **within a site**: some OPCs (Iberdrola | bp pulse,
  `HGP-*`, `ACC-*`) publish bare ids (`19`, `160`, `332`) that repeat on other
  sites. Key every point by
  `(site_id, point_id)`; the dynamic CSVs carry `site_id` (first `<reference>` of
  each `energyInfrastructureSiteStatus`). Keyed that way, static and dynamic match
  1:1 and no point has two statuses. A point that seems to appear 2–3× with
  conflicting states is this collision, not a feed error.
- 33% of connector rows (6 948/21 056) have declared power inconsistent with
  V×I (>25% off); 2 686 declare power above physical capacity (impossible, e.g.
  1200 V × 600 A = 720 kW declared as 200 kW).
- NAP `operator_id` is not a reliable OPC key: 21 ids carry more than one
  `operator_name` (3448 sites; ATLA alone has 7 spellings over 598 sites) and 3
  operators publish under the PartyCode instead of the PartyId (`BBGE`, `CIRC`,
  `CONT`). `CONT` is the Continente case — 450 sites under the acquirer's name
  ("Modelo Continente Hipermercados, S.A.") while the CPO is `CNT`
  "Continente Plug & Charge". Use the tracker's PartyId (see
  `scripts/tracker_checks.py`), and note that some operators publish sites
  without their own prefix (`CNT-0002PL0012` → `0002PL0012`), so asset matching
  needs both forms.
- NAP `min_fee = 0` is not an anomaly (46% of pricing rows); `min_fee` currently
  ranges 0–3,0 with no absurd values since the `97,561 €/min` class was fixed.
- Every NAP price (`min_fee`, `pricePerDeliveryUnit`, also outside MOBI.E) comes
  **without VAT** (confirmed with the NAP). So do MOBI.E's tariff file values,
  `AD_HOC_PAYMENT` included (its 0,51 €/kWh at IONITY × 1,23 = IONITY's own 0,63).
  VAT depends on the site's region (lower on Madeira and the Azores); ohmigo adds it.
- 808 MOBI.Data EVSE ids are bare numbers (FCT, ACC, HGP, VIA). The
  `UID_TOMADA` in `data/mobie_tarifas.csv` is synthetic (`<ID>-<socket>-1`)
  except for those, which keep the bare id so ohmigo's per-site fallback still
  sees them.
- MOBI.Data's per-socket `kw` is the station maximum repeated on every socket,
  so there is no NAP↔MOBI.E power comparison (errors.md item 2 says
  "sem dados").
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

## Site specifics
- Three pages, no external libs, pure CSS/JS: `index.html` "Procurar" (drivers:
  search by town/operator/code, "Perto de mim", quick filters, a card per site
  with one status mark per socket, detail with sockets, operator fees, payment
  and directions links to Google Maps/OpenStreetMap, canvas map),
  `rede.html` "Rede" (community statistics: KPIs, news, bar charts as real
  tables, history, hubs, facts) and `operadores.html` "Operadores" (OPCs: weekly
  anomaly report per operator parsed from `Agents-outputs/anomalias-results.md`
  by `build_site.parse_opc_report`, OPC churn, reportable errors).
- Sources in `assets/site/`; output in `site/` (committed, what `pages.yml`
  serves). Data in `site/data/{stats,panels,sites,points,outline,opc}.json`,
  fetched same-origin (`credentials: 'omit'`) and split by `scripts/site_data.py`
  so each page loads only what it uses; a key added to `data` that is not
  listed there lands in `stats.json`, never dropped.
- **Must** sanitize NaN/Inf floats to null before the dump (`clean()` in
  `build_dashboard.py`): bare `NaN` breaks `JSON.parse`.
- Data is no longer embedded in a `<script>`, so it needs no `<`/`>`/`&`
  escaping. The rule now: the front end inserts third-party text (OSM names,
  operator names, community notes, report fragments) **only as text nodes**,
  through the `el()`/`md()` helpers in `common.js`, never `innerHTML` or
  similar. `validate_site.py` enforces it. The pre-rendered panels
  (facts/errs/anom/hubs/churn/news/hist) are baked into the HTML at build time
  (`<!--PANEL:name-->`) from build-escaped HTML, both languages in `data-lang`
  blocks.
- CSP (`<meta>`, in `_head.html`; Pages can't set headers): `default-src 'none';
  script-src 'self'` (no inline scripts); `style-src 'self' 'unsafe-inline'`
  only because the history heat map uses inline background styles;
  `connect-src 'self'` plus the AmpereArchive origin; `font-src 'self'`;
  `img-src 'self' data:`. Nunito is served from `fonts/`, no font CDN.
- Bilingual PT/EN: `boot.js` picks the language before paint (`?lang=pt|en`,
  then `localStorage` `nap-lang`, then the browser; PT for `pt*`). Strings live
  in the `STR` tables of `common.js` plus `N.addStrings` per page
  (`data-i18n`/`data-i18n-ph`/`data-i18n-title` attrs); data enums are
  display-mapped at render time, so the data keeps stable PT/code values.
  `data` carries EN mirrors (`kpis_pt` is the PT one; `kpis` stays EN;
  `facts/errs/anom/hubs/churn_html_en`) generated via
  `scripts/dashboard_i18n.py` (phrase MAP + PT→EN number conversion). New fixed
  PT strings in FACTS/ERRS/ANOM/HUBS/CHURN_HTML/NEWS_HTML **must** get a MAP
  entry or they render in PT for EN users.
- If a page shows nothing below the KPIs, suspect a JS runtime error (an element
  id that doesn't exist, a variable out of scope); check the browser console and
  `validate_site.py`.
- Map: a canvas drawn from `sites.json` (per-site lon/lat) + `outline.json` (PT
  polygons). Regions are `mainland`/`madeira`/`acores`; site `region` values are
  `azores` (with a `z`), so the map re-maps `azores`→`acores`.
- Search and filters on `index.html` run on `sites.json`; point-level data
  (`points.json`) loads after, for the detail view and the live status. Both
  take power, fees and the DC voltage filter from the network model, so the
  detail shows every €/min tier ("0; 0,18 após 30 min"), OSM's power with the
  NAP's beside it ("22 (NAP: 11)") and the NAP-only issues per socket.
  `find.js` still renders the pre-model `points.json` (`ENERGY`/`TIME`/`FLAT`
  strings; `site_data.POINT_SHAPES` accepts both) until the first refresh
  rewrites it; drop that branch after. The
  payment filter uses `x.pay` (list of OSM payment methods: App/Cartão/Cartão de
  membro/Sem autenticação/Dinheiro) joined per-site onto every point row.
- "Perto de mim": the browser asks for the location only when the button is
  pressed; the coordinates are used on the device to sort and centre the map,
  never sent or stored.

- Aparência: tema (auto/claro/escuro) e visão (padrão/daltonismo/alto contraste)
  são `data-theme`/`data-vision` no `<html>`, definidos por `boot.js` antes de
  pintar (valida contra lista fechada o que lê de `nap-theme`/`nap-vision`;
  `nap-lang` idem). Cores só por variáveis CSS (`--s-<estado>` para os
  estados); um estado nunca é só cor: cor + forma + texto.
  O único pedido a outro domínio é o estado ao vivo
  (`connect-src` na CSP, abaixo). `assets/privacidade.html`, `404.html`, os
  ícones e `llms.txt` são copiados para `site/` pelo `build_site.py`; a página
  de privacidade descreve os pedidos do site, o `localStorage` e a localização
  (PT e EN), por isso qualquer pedido ou chave novos têm de entrar lá também.
- Estado ao vivo: ao abrir, `index.html` e `rede.html` leem `v1/PT/status.json.gz` do
  AmpereArchive (sem cookies nem referrer; se vier ainda em gzip, descomprime
  com `DecompressionStream`) e refaz o que depende do estado: gráficos de
  estado e ocupação, KPI de ocupação, cores do mapa, cartões e filtro de
  estado. Factos, erros e novidades continuam da semana. Casa cada ponto pelo
  `point_id` e por `site_id` == `site_external_id` ou a acabar em
  `-<site_external_id>` (o arquivo usa o `site_id` do NAP, `EZC-AMD-00051`;
  casa quase todos, sem ambíguos); ambíguo fica como estava. Só aceita
  estados da lista DATEX II e ignora ficheiros com mais de 180 min. Sem rede,
  bloqueado ou desatualizado, mostra o estado da semana e diz-o no cabeçalho.
  `validate_site.py` desliga o fetch (`NAP_NO_LIVE`) e testa
  `applyLive` com dados sintéticos. O host vem de `<meta name="nap-live-origin">`
  (`dashboard_payload.ARCHIVE_ORIGIN_DEFAULT`) e o build troca-o, nessa meta e
  no `connect-src` da CSP, pela origem de `AMPERE_ARCHIVE_URL` (variável do
  repo, passada ao passo de build); só aceita `https://host[:porta]`, senão
  avisa e fica o por omissão.

## Convenções de escrita (PT-PT técnico)
- **tensão**, nunca "voltagem". Unidades abreviam-se `V`/`A`/`kW` normalmente.
- `voltage`/`max_current` mantêm-se em inglês só quando referem identificadores
  de código ou colunas (CSV, DATEX II, snippets) — em prosa portuguesa é tensão.

## PR checks (`.github/workflows/pr-checks.yml`)

Gate de ~1 s em cada PR para `main`, sem rede e sem dependências (stdlib).
`scripts/ci_paths.py` corre quatro verificações:

- **A** — nenhum ficheiro de dados na raiz do repo;
- **B** — em código, workflows e docs, qualquer menção a um ficheiro de dados
  tem de aparecer com o prefixo `data/` (apanha um `pd.read_csv('nap_static_sites.csv')`
  que volte ao sítio antigo);
- **C** — cada `scripts/*.py`/`*.sh` citado num workflow existe no disco;
- **D** — os derivados do tracker estão **fora** do git, e o `.gitignore` não
  tem excepções para eles (testa o índice com `git ls-files`, **não**
  `git check-ignore`: este reporta ficheiros já versionados como "não
  ignorados", que é precisamente o caso proibido).

Mais `compileall` nos scripts Python e `bash -n` nos shell, para o check não ser
decorativo (um erro de sintaxe só apareceria no refresh da semana seguinte).

**E `scripts/validate_site.py`**, que valida o `site/` commitado (o artefacto
que o `pages.yml` publica sem validação nenhuma): JSON e esquema, sintaxe JS,
sem `<script>` inline, CSP e sem sinks do tipo `innerHTML`. Sem isto, um PR
podia injectar um script ou um `innerHTML` com dados de terceiros e o merge
publicava-o.

**O que este gate não cobre, de propósito:** o pipeline completo não corre no PR
— `fetch_data.sh` são ~230 MB e o `osm_umap.py` traz um dump Overpass; bater nos
servidores oficiais a cada PR não é aceitável. Em troca, o `refresh.yml` semanal
é o teste de integração a sério.

Fica em aberto, se quiseres mais cobertura: correr `build_dashboard.py` em cima
de fixtures. Exige versionar uma amostra dos CSVs do NAP, e isso levanta a mesma
questão de republicação de dados de terceiros que o `tracker_errors.csv` já
levanta (ver `THIRD-PARTY-NOTICES.md`) — por isso não foi feito sem decisão.

Ao mover/renomear um ficheiro de dados, actualizar a lista `DATA_FILES` em
`scripts/ci_paths.py`: é a fonte de verdade dos quatro checks.

## Deliverables
- `site/` — the static site (preview: `python3 -m http.server --directory site`)
- `facts.md` — interesting facts
- `novidades.md` — weekly network news (new/removed sites, OPC moves, power
  records; panel on "Rede", EN via `dashboard_i18n.MAP`) with
  `network-census.json` (committed state for next week's diff)
- `errors.md` — reportable data errors, numbered, for the data owners; the
  last item is the tracker cross-check, appended from `data/tracker_findings.md`
  when the tracker was fetched (don't hard-code the total, it changes)
- `Agents-outputs/anomalias-results.md` — output do agente `Agents/anomalias.md`
  (anomalias dos dados estáticos, agrupadas por OPC)
- `/ohmigo/chargers.json` on Pages — the ohmigo dataset (Actions artifact, see
  "ohmigo dataset"). `pages.yml` serves `site/` as the web root plus a
  `/dashboard.html` redirect to `/`, and also publishes `robots.txt`, `sitemap.xml`
  and `/.well-known/security.txt` (RFC 9116; `Expires` 180 days from each
  deploy).

## Workflows and secrets
- Pushes to `main` come only from the **"nap-dashboard push" GitHub App**, the
  only actor on the `review branch` ruleset's bypass list in "Always" mode.
  Repository admins are on it in "For pull requests only" mode, so nobody
  (another admin, or the owner by accident) pushes straight to `main`. The
  App has `Contents: write` on this repo and nothing else; its client id is
  the `PUSH_APP_CLIENT_ID` variable and its key the `PUSH_APP_PRIVATE_KEY`
  secret. `actions/create-github-app-token` mints a 1-hour token (revoked at
  the end of the job) in two places only: the `publish` job of `refresh.yml`
  (a fresh runner: no pip, no repo script on third-party data; it downloads
  the `refresh-publish` artifact, checks each file is a regular file under
  20 MB and in the closed allowlist, which includes the `site/` tree, then commits) and the `publish` job of `agents.yml`, same pattern
  for a closed list of files from `Agents-outputs/`. A push with the App's token triggers `pages.yml`, which
  one with the `GITHUB_TOKEN` wouldn't. The agent job (a model with a
  shell, reading third-party data) never shares a machine with it, and code
  an agent writes (`scripts/anomalias_check.py`) never reaches `main` on its
  own: it's in the run's `agent-outputs` artifact, for someone to review and
  open a PR.
- `GITHUB_TOKEN` is read-only everywhere except `issues: write` (failure
  issues) and what `pages.yml` needs to deploy.
- Actions are pinned by SHA (Dependabot bumps them).
