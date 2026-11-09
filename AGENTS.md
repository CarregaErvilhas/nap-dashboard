# AGENTS.md — NAP EADME data analysis

## Project type
Single-machine analysis of the Portuguese EV charging network. Pinned runtime
deps in `requirements.txt` (Dependabot, monthly); CI in `.github/workflows/`
(weekly `refresh.yml` pipeline + `pages.yml` deploy + `agents.yml`). Code
produces CSVs + a self-contained dashboard (`dashboard.html`, `facts.md`,
`errors.md`), validated by `scripts/validate_dashboard.py` +
`scripts/pipeline_guard.py`. Don't over-engineer.

## Layout
- `scripts/` — the pipeline (in the order of "Pipeline order" below, plus
  `extract_enums.py`, `fetch_schemas.sh` and the manual `tracker_fixed.py`);
  the checks (`validate_dashboard.py`, `pipeline_guard.py`, `ci_paths.py`);
  the dashboard helpers (`dashboard_payload.py`, `dashboard_i18n.py`); the
  anomalias agent's deterministic side (`anomalias_summary.py`,
  `anomalias_evidence.py`, `anomalias_check.py`, `format_anomalias.py`,
  `check_agents.py`); and `ohmigo_dataset.py`. One-time migrations don't stay
  here once they've run: git keeps them.
- `assets/` — `dashboard_template.html`, `pt_outline.json` (PT outline for the
  map), `schemas/*.xsd` (DATEX II 3.3 © CEN; ver `assets/schemas/README.md`)
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
- The repo root holds only code, docs and deliverables: `dashboard.html`,
  `dashboard.png`, `facts.md`, `errors.md`, `novidades.md`,
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
URLs), then `scripts/mobie_tariffs.py` rebuilds `data/mobie_tarifas.csv` in the
old MOBI.E layout from the two JSON files. Since 2026-11-09 mobie.pt no longer
serves the tariff CSV; see `references/data-sources.md` for what the new source
lacks (grid level, parking time, per-socket power, ~500 sites).

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
- Fonte: `--url` descarrega os ficheiros horários para `data/archive_cache/`
  (não há listagem: gera os nomes e aceita 404; usa `v1/<CC>/manifest.json` se
  um dia existir). `--root DIR | s3://bucket` lê uma cópia local ou o R2.
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
  (precisa de `vars.AMPERE_ARCHIVE_URL`; sem ela, ou se falhar, o dashboard
  sai sem o painel). `data/archive_cache/` fica em `actions/cache` entre
  corridas; o sync apaga os dias fora da janela (menos `static_versions`).
  Um 403 conta como erro, nunca como "hora sem ficheiro".

## Pipeline order
`scripts/nap_etl.py` → (`scripts/check_quality.py`, `scripts/summary.py`) →
`scripts/mobie_join.py` → `scripts/dgeg_lists.py` → `scripts/dgeg_crossref.py` →
`scripts/nap_static_checks.py` → `scripts/concelho_check.py` →
`scripts/osm_umap.py` → (`scripts/osm_places.py`, ohmigo dataset only) → `scripts/tracker_sync.py` + `scripts/tracker_checks.py` →
`scripts/make_pt_outline.py` →
`scripts/network_news.py` (diff semanal vs `network-census.json` do HEAD →
`novidades.md` + novo `network-census.json`; primeira corrida = baseline) →
`scripts/build_dashboard.py`.
`scripts/build_dashboard.py` reads the intermediate CSVs +
`data/osm_umap.csv`/`data/osm_caca.csv`/`assets/pt_outline.json` and writes
`dashboard.html`, `facts.md`, `errors.md`; it appends
`data/nap_static_findings.md` (written by `scripts/nap_static_checks.py`),
`data/concelho_mismatches.md` (written by `concelho_check.py`),
`data/osm_umap_findings.md` (written by `scripts/osm_umap.py`) and
`data/tracker_findings.md` (written by `scripts/tracker_checks.py`) to `errors.md`
when present.
It also regenerates `dashboard.png` (README screenshot) via headless Chrome if
available; it only warns/skips otherwise.

`scripts/validate_dashboard.py` (rode no `refresh.yml` antes do commit, no
`pr-checks.yml` em cada PR, e em local depois de qualquer build) valida o
`dashboard.html`: o JSON embutido `const D = {…}` tem de fazer `json.loads`,
tem de estar escapado para o contexto `<script>` (sem `<`, `>` ou `&` crus — ver
"Dashboard specifics"), cada `<script>` tem de passar `node --check`, e a
inicialização tem de correr sem exceção numa eval com DOM stub.
`scripts/pipeline_guard.py` travará o commit se um upstream mudar o formato e o
pipeline produzir dados absurdos sem rebentar (limiares mínimos para
sites/pontos/join/DGEG/registo) — falha o job e o dashboard online fica no
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

`scripts/osm_umap.py` cross-references NAP sites against community OSM data: the
Overpass dump `Todos.json` from the author of the "Postos de Carregamento v2.1"
umap map (both `amenity=charging_station` and `man_made=charge_point` elements)
and the "Caça aos Postos" umap doubt layers. Fetches are cached in `data/umap_cache/`.
Matches by MOBI.E `ref` code (strips a `MOBI-` prefix, expands multi-code refs
"A;B;C", way polygons use the centroid). Writes `data/osm_umap.csv` (deduped per NAP
code, preferring the row with the most payment/auth tags), `data/osm_caca.csv` and
`data/osm_umap_findings.md` (errors.md item 12).

`scripts/make_pt_outline.py` builds `assets/pt_outline.json` (decimated PT
outline for the dashboard map **plus per-district/island labels** — `{outline:
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
  (gitignored). Backtest on the 1000 already-`FIXED` rows (2026-10-24): Location
  373/397, Amperage 75/85, Charge mode 29/30 are recovered; Voltage is weak
  (`MISTO` 131/184), so only `FIXED_CANDIDATA` is trustworthy there. These are
  *candidates* for the owners to flip to `FIXED`, never an automatic status change.
- Products: `data/opc_registry_authority.csv` (the only *current* OPC identity table —
  `PartyId | PartyCode | name`, 99 CPO) and
  `data/tracker_errors.csv` (the project's only labelled/ground-truth set: 3153 real
  defects with the value the owner considers correct, plus `notes_class`).
- `tracker_checks.py` writes `data/tracker_findings.md`/`.csv` (errors.md item 13).
  Rules and the snapshot they were validated on (2026-10-18): OPC sem PartyId
  resolúvel (3), PartyCode em vez de PartyId (3: BBGE, CIRC, CONT), nomes
  fragmentados (21 ids / 3448 sites), assets declarados removidos ainda
  publicados (5). The NAP-only rules mined from the tracker (placeholder DC
  voltages, 58; `mode3AC3p` without three-phase power, 35 rows / 24 sites) are
  in `scripts/nap_static_checks.py`, errors.md item 8.
  The rules are mined from the tracker's own classes (171 rows of 750→500 V,
  199 of `mode3AC3p`→`mode2AC1p`), which is what makes them non-speculative.
- Known limits: OPC identity resolves by `operator_name`, so an operator that
  renames itself drops out until the tracker catches up; `min_fee = 0` covers
  46% of pricing rows, so zero is **not** a pricing anomaly.

## ohmigo dataset
`scripts/ohmigo_dataset.py` builds `data/ohmigo_chargers.json` for the ohmigo
MCP server (EV charging cost answers for ChatGPT/Claude): sites, points, power,
the connector's declared tensão (`v`, V) and max current (`a`, A), the grid
voltage level (`level`: BTN/BTE/MT, which picks the TAR; **always `null` since
2026-11-09**, because neither MOBI.Data nor the NAP publishes it) and the **raw** MOBI.E OPC tariffs per socket (every €/min tier and
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
powers), and ohmigo prefers it. Where OSM agrees with the NAP, the point
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
energy prices from ceme-v2. `refresh.yml` runs it after the pipeline guard and
uploads it as the `ohmigo-dataset` Actions artifact (90-day retention; not
committed: ~10 MB a week; not a release, because the repo's releases are
immutable and an asset can't be replaced); `pages.yml` copies the newest one to
`https://nap.ocarroeletrico.com/ohmigo/chargers.json`. It exits non-zero (and the
refresh fails) below 5 000 sites or 10 000 tariffed points. `SCHEMA` in the
script bumps on incompatible format changes.

A daily refresh (`ohmigo-daily.yml`, cron `49 2,14 * * *`) re-runs only the ohmigo
pipeline (NAP ETL + OSM dump + places + dataset) and publishes a new
`ohmigo-dataset` artifact (30-day retention), then triggers a Pages deploy, so
the MCP sees fresher OSM/NAP data between weekly refreshes. It does not build
the dashboard or commit to `main`.

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
- Point ids are only unique **within a site**: some OPCs (Iberdrola | bp pulse,
  `HGP-*`, `ACC-*`) publish bare ids (`19`, `160`, `332`) that repeat on other
  sites (66 ids / 134 points on 2026-10-24). Key every point by
  `(site_id, point_id)`; the dynamic CSVs carry `site_id` (first `<reference>` of
  each `energyInfrastructureSiteStatus`). Keyed that way, static and dynamic match
  1:1 and no point has two statuses. The old "44 points appear 2–3× with
  conflicting states" finding was this collision, not a feed error.
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
  so there is no NAP↔MOBI.E power comparison any more (errors.md item 2 says
  "sem dados"). With the old CSV the agreement was 99.8%.
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
  `dashboard_payload.dump_payload(clean(data))` (`scripts/dashboard_payload.py`).
- **Must** sanitize NaN/Inf floats to null before dumping — bare `NaN` breaks
  browser `JSON.parse`. The `clean()` helper in `build_dashboard.py` does this.
- **Must** dump through `dashboard_payload.dump_payload()`, never a raw
  `json.dumps()`: the payload vive dentro de um `<script>` e o tokenizer HTML
  fecha o elemento no primeiro `</script`, mesmo dentro de uma string JSON — um
  `</script>` num dado do OSM/umap (campos `doubt`, `osm_op`, `osm_fee`…) saía
  do elemento e o resto do ficheiro passava a ser HTML executado (XSS
  armazenado no dashboard publicado). O escaper converte `<`, `>` e `&` em
  `\u003c`/`\u003e`/`\u0026`; o `JSON.parse` reconstrói os caracteres originais,
  por isso o valor em runtime é idêntico. `validate_dashboard.py` chumba
  qualquer payload com `<`, `>` ou `&` crus.
- No external libs, pure CSS/JS, must open via `file://` (the live status fetch works there too: the archive sends `access-control-allow-origin: *`).
- Bilingual PT/EN (single file): `detectLang()` shows PT for `pt*` browsers,
  EN otherwise; PT|EN toggle persists to `localStorage`, `?lang=pt|en` overrides.
  Static chrome lives in the JS `STR` table (`data-i18n`/`data-i18n-ph`/
  `data-i18n-title` attrs); data enums (status/region/pay) are display-mapped at
  render time, so `D` keeps stable PT/code values for filtering. All dynamic
  rendering goes through `setLang()`-called functions (never one-shot), and the
  status×power panel re-renders into `#statusPwPanel` instead of repeated
  `insertAdjacentHTML`. `D` carries EN mirrors (`kpis_pt` is the PT one —
  `kpis` stays EN; `facts/errs/anom/hubs/churn_html_en`) generated via
  `scripts/dashboard_i18n.py` (phrase MAP + PT→EN number conversion); template
  falls back to PT when an `_en` key is missing. New fixed PT strings in
  FACTS/ERRS/ANOM/HUBS/CHURN_HTML/NEWS_HTML **must** get a MAP entry or they render in PT
  for EN users.
- The `validate_dashboard.py` DOM stub must keep `navigator`/`localStorage`/
  `documentElement` (installed via `defineProperty` — node ≥21 has read-only
  natives that swallow plain assignment) or lang detection renders the wrong
  branch under eval.
- If the dashboard shows nothing below the KPIs, suspect a JS runtime error (an
  element id that doesn't exist, a variable out of scope):
  `validate_dashboard.py`'s DOM-stub eval catches most of them.
- To ship a template change without the data (the CSVs aren't in a fresh
  checkout), regenerate `dashboard.html` as `build_dashboard.py` would: the
  new template with the committed payload in place of `/*__DATA__*/`. The
  weekly refresh rebuilds it from scratch anyway.
- The template has no external resources and a `data:` favicon, so it keeps
  working from `file://`.
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

- Aparência: tema (auto/claro/escuro) e visão (padrão/daltonismo/alto contraste)
  são `data-theme`/`data-vision` no `<html>`, definidos por `window.NAPAPP` num
  `<script>` do `<head>` (valida contra lista fechada o que lê de
  `nap-theme`/`nap-vision`; `nap-lang` idem). Cores só por variáveis CSS
  (`--s-<estado>` para os estados); em cb/hc o mapa usa uma forma por estado.
  A CSP vai em `<meta>` (o Pages não deixa definir cabeçalhos): o único
  pedido à rede permitido é `connect-src https://ohm-age.ocarroeletrico.com`
  (estado ao vivo, abaixo). `assets/privacidade.html`, `404.html` e os ícones
  são copiados para o site pelo `pages.yml`; a página de privacidade descreve
  esse pedido (PT e EN), por isso qualquer pedido novo tem de entrar lá também.
- Estado ao vivo: ao abrir, a página lê `v1/PT/status.json.gz` do
  AmpereArchive (sem cookies nem referrer; se vier ainda em gzip, descomprime
  com `DecompressionStream`) e refaz o que depende do estado: gráficos de
  estado e ocupação, KPI de ocupação, cores do mapa, tabela e filtro de
  estado. Factos, erros e novidades continuam da semana. Casa cada ponto pelo
  `point_id` e por `site_id` == `site_external_id` ou a acabar em
  `-<site_external_id>` (o arquivo usa o `site_id` do NAP, `EZC-AMD-00051`;
  2026-11-09: 19 534/19 537, 0 ambíguos); ambíguo fica como estava. Só aceita
  estados da lista DATEX II e ignora ficheiros com mais de 180 min. Sem rede,
  bloqueado ou desatualizado, mostra o estado da semana e diz-o no cabeçalho.
  `validate_dashboard.py` desliga o fetch (`NAP_NO_LIVE`) e testa
  `applyLive` com dados sintéticos. O host está no template
  (`dashboard_payload.ARCHIVE_ORIGIN_DEFAULT`) e o build troca-o, na CSP e
  no `LIVE_URL`, pela origem de `AMPERE_ARCHIVE_URL` (variável do repo, passada
  ao passo "Build dashboard"); só aceita `https://host[:porta]`, senão avisa e
  fica o do template.

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

**E `scripts/validate_dashboard.py`**, que valida o `dashboard.html` commitado
(o artefacto que o `pages.yml` publica sem validação nenhuma): JSON embutido,
escape do payload para o contexto `<script>`, sintaxe JS e inicialização. Sem
isto, um PR podia injectar `<script>`/`</script>` no ficheiro e o merge
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
- `dashboard.html` — the interactive dashboard (open with `open dashboard.html`)
- `facts.md` — interesting facts
- `novidades.md` — weekly network news (new/removed sites, OPC moves, power
  records; panel above "Visão geral", EN via `dashboard_i18n.MAP`) with
  `network-census.json` (committed state for next week's diff)
- `errors.md` — reportable data errors, numbered, for the data owners; the
  last item is the tracker cross-check, appended from `data/tracker_findings.md`
  when the tracker was fetched (don't hard-code the total, it changes)
- `Agents-outputs/anomalias-results.md` — output do agente `Agents/anomalias.md`
  (anomalias dos dados estáticos, agrupadas por OPC)
- `/ohmigo/chargers.json` on Pages — the ohmigo dataset (Actions artifact, see
  "ohmigo dataset"). `pages.yml` also publishes `robots.txt`, `sitemap.xml`
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
  the end of the job) in two places only: just before the last step of
  `refresh.yml` (the same runner as the pipeline, which runs our scripts and
  the pinned `requirements.txt`, no model) and in the `publish` job of
  `agents.yml`, a fresh runner that copies a closed list of files from
  `Agents-outputs/`. A push with the App's token triggers `pages.yml`, which
  one with the `GITHUB_TOKEN` wouldn't. The agent job (a model with a
  shell, reading third-party data) never shares a machine with it, and code
  an agent writes (`scripts/anomalias_check.py`) never reaches `main` on its
  own: it's in the run's `agent-outputs` artifact, for someone to review and
  open a PR.
- `GITHUB_TOKEN` is read-only everywhere except `issues: write` (failure
  issues) and what `pages.yml` needs to deploy.
- Actions are pinned by SHA (Dependabot bumps them).
