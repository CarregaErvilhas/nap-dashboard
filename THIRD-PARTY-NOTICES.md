# Third-party notices — nap-dashboard

Our code/site templates/docs are `PolyForm-Noncommercial-1.0.0` (see `LICENSE`). Everything below keeps its **own licence/terms** and is **not** covered by PolyForm. Where published in the site (`site/data/*.json`, fetched by `index.html`, `rede.html` and `operadores.html`, plus the panels pre-rendered into their HTML), the site is a collective work: our code is PolyForm-Noncommercial, the third-party portions stay under their own terms.

## Mascots of the group's sites

`assets/site/grupo/*.svg` (copied to `site/grupo/`, shown on `grupo.html`) are the mascots of the sites of the O Carro Elétrico group (O Carro Elétrico, ohmigo, Voltaria, Comparador CEME, Postos PT, olh'o'posto, AmpereArchive), plus `pano.svg`, the logo of the Panoramax project. Each belongs to its own site and is its brand: they are **not** covered by PolyForm or any other licence of this repo, and may not be reused apart from a link to that site.

## Data sources and schemas

| Resource | Origin | Licence / terms | What we do |
|---|---|---|---|
| NAP MOBI.E static + dynamic feeds (DATEX II 3.3 XML) | `https://pgm.mobie.pt/integration/nap/evChargingInfra`, `/evActualStatus` via NAP `nap-portugal.imt-ip.pt` (fichas 148/149, org. MOBI.E) | IMT NAP terms: free use **with source attribution, no lucrative/illicit use**. AFIR/NAP free-access framework. | Attribution in dashboard footer + here. Not re-licensed. |
| MOBI.Data OPC tariffs + station list (MOBI.E) | `https://data.mobie.pt/data/tariffs.json`, `https://data.mobie.pt/data/stations.json` (until 2026-11-09: the tariff CSV on mobie.pt) | The portal calls itself "dados abertos" (open data), but **no explicit licence was found**. Used as factual reference; redistribution basis unclear. | Attribution in footer. If MOBI.E objects, we remove/redact on request. Contact in `LICENSE`. |
| DGEG OPC / CEME lists | `https://www.dgeg.gov.pt/.../operacao-e-comercializacao/lista-de-opc/`, `.../regime-transitorio/ceme-registados/` | DGEG site terms: free use **with source mention, no commercial use** against public interest; IP belongs to DGEG. | Attribution in footer + here. |
| PCVE error tracker (`pt-pcve-errors.xlsx`) | Shared by its owner (PCVE/data-owners side) on Google Drive as an Office file; **no public API and no licence statement found**. Not redistributed here — fetched at run time. | **Unknown / no explicit licence.** The owner shares it as "anyone with the link", which authorises *reading*, but says nothing about republication. | **Read and derive only.** Source file, URL and file id are never committed (URL lives in the `TRACKER_URL` secret). See the derived-data note below. |
| CAOP concelho boundaries (via `jotanmiguel/caop_GeoJSON` fork of official DGT data) | `https://raw.githubusercontent.com/jotanmiguel/caop_GeoJSON/master/geograficas/...` — official data: DGT | **CC-BY 4.0** (DGT open data): free use incl. commercial, **must credit Direção-Geral do Território**. The GitHub fork itself has no explicit licence; the underlying data is DGT's. | `assets/pt_outline.json` + concelho check derived from it. Credited as `© DGT (CAOP)` in footer, map and here. This file and any CAOP-derived geometry are **excluded from the PolyForm non-commercial restriction**. |
| OpenStreetMap data (via `avataranedotas/umap_postos` `Todos.json` Overpass dump) | `https://raw.githubusercontent.com/avataranedotas/umap_postos/main/Todos.json` | **ODbL 1.0**: **must credit `© OpenStreetMap contributors`** + make clear data is available under ODbL (link below); derivative databases shared under ODbL on public use. | Credited in footer + map. Per-site OSM fields in `site/data/sites.json` (`pay`, `osm_op`, `osm_access`, `osm_fee`, `ad_hoc`, `doubt`; `pay` is also joined onto each row of `site/data/points.json`) are ODbL-covered. |
| OpenStreetMap places and main roads (basemap of the site's map) | Overpass API, built by `scripts/make_pt_basemap.py` into `assets/pt_basemap.json` → `site/data/basemap.json` | **ODbL 1.0**, credit `© OpenStreetMap contributors`. | Credited on the map canvas (`© OpenStreetMap`) and in the footer. Static file, no tile requests from the visitor's browser. |
| Community umap layers (curadoria: Alexandre Moleiro) | `Postos de Carregamento v2.1` (`https://umap.openstreetmap.fr/pt-pt/map/postos-de-carregamento-v21_690884`, map 690884) and `Caça aos Postos de Carregamento` (`https://umap.openstreetmap.fr/en/map/caca-aos-postos-de-carregamento_1386222`, map 1386222) | ODbL (underlying OSM) **plus the curator's own rights** (no explicit licence found). | Credited + linked in footer and here. Treat as reference leads, never ground truth. |
| Charger model list ("Modelos de Carregadores usados em Portugal", Alexandre Moleiro) | [Public Google Doc](https://docs.google.com/document/d/1SyhISXEaZiAPYuRLQ9dA2OtFrwysFm01Yei11qTLQLw), fetched at run time by `scripts/fetch_charger_models.sh` into `data/charger_models.txt` (gitignored, so it never goes stale) | **Public and free to use**, as its author shares it. Only the numbers are used (power, voltage, current, power per car); the document's photos and operator logos never are (they are not his). | Author and link next to every figure: Procurar's detail, ohmigo's answers (`modelsSource`), `errors.md` item 14. Per-site figures are `models` in the network model and `mdl` in `site/data/sites.json`. |
| Charger photos | Panoramax (federated, `api.panoramax.xyz`), Wikimedia Commons; referenced from OSM (`panoramax=`, `wikimedia_commons=`, `image=`) or chosen by hand per model (`assets/charger_model_photos.json`). Thumbnails fetched by `scripts/charger_photos.py`, published on Pages under `/photos/` | Each photo's own licence, almost always **CC BY-SA 4.0** (Panoramax) or a CC licence on Commons. | Author, licence and a link to the original next to each photo (site and ohmigo). Mapillary photos are linked, never copied. |
| "Mapa detalhado" basemap (OpenStreetMap + Natural Earth, Protomaps build) | Daily planet build `build.protomaps.com`, cut to Portugal by `.github/workflows/basemap-tiles.yml` (`scripts/basemap_region.py`) and served from our R2 at `maptiles.ocarroeletrico.com` | OSM: **ODbL 1.0**, credit `© OpenStreetMap contributors`; Natural Earth: public domain; Protomaps tile schema and style design: CC0 / BSD-3 (Protomaps LLC, Kelso Cartography). | `© OpenStreetMap · Protomaps` on the map itself. Loaded only when the visitor presses "Mapa detalhado". |
| Map glyphs and sprites (`protomaps/basemaps-assets`) | Noto Sans glyph ranges and the v4 light/dark sprites, copied to the same R2 bucket | Noto Sans: **SIL OFL 1.1** (licence text at `maptiles.ocarroeletrico.com/fonts/OFL.txt`); sprites: Protomaps style design **CC0**, some icons derived from Mapzen's **MIT** icons. | Served unchanged. |
| MapLibre GL JS 6.17.0, pmtiles 4.5.0, @protomaps/basemaps 5.7.2 (`assets/site/vendor/`) | npm, copied byte for byte (`validate_site.VENDOR` pins each sha256) | **BSD-3-Clause** (MapLibre contributors / Mapbox; Brandon Liu, Protomaps; The Protomaps Authors). | Each licence ships next to the code (`vendor/*/LICENSE.txt`). Not re-licensed under PolyForm. |
| DATEX II 3.3 XSDs (`assets/schemas/*.xsd`) | `http://datex2.eu/schema/3/<module>` (see `assets/schemas/README.md`) | **© CEN / DATEX II organisation**. Free to use for implementation; **not** re-licensed under PolyForm. | Vendored copies kept only for enum validation (`scripts/check_quality.py`, `scripts/extract_enums.py`). Re-fetch with `scripts/fetch_schemas.sh`. |
| Python runtime deps | `requirements.txt` (`pandas`, `lxml`, `openpyxl`, `duckdb`, `osmium`, transitive `numpy`) | BSD-3 / BSD / MIT (permissive). Not distributed, installed via pip. | Compatible. No action needed. |
| GitHub Actions (`checkout`, `setup-python`, `upload-artifact`, `deploy-pages`) | `actions/*` | MIT. Build-time only, not distributed. | Compatible. |

## Derived data from the PCVE error tracker — needs the owner's OK

The tracker is fetched at run time and **not** redistributed. Three files are derived from it on each run, none of them versioned, and one report is published:

| Derived (never versioned) | What it is |
|---|---|
| `data/opc_registry_authority.csv` | 99 rows: `PartyId`, `PartyCode`, official operator name |
| `data/tracker_errors.csv` | 3153 rows: the owners' error list (asset id, status, error type, current/correct value) |
| `data/tracker_meta.json` | sha256 + sync date (no content) |

`errors.md` item 13 is the only place derived findings are published, and it quotes `site_external_id`/`point_id` + operator — no contact details. Item 8 (NAP data only) also cites two aggregate tracker class counts (171 and 199 rows) as the reason its rules exist; no row of the tracker is reproduced there.

**None of them is versioned.** They are re-extracted from the source xlsx on every run (`fetch_tracker.sh` → `tracker_sync.py`) and stay gitignored; the weekly CI fetches the xls itself via the `TRACKER_URL` secret. A copy of a third party's internal defect list has no place in a public repository, and a versioned one would also go stale without saying anything.

Consequence to be aware of: if the fetch stops working, errors.md simply has no tracker item. That is the intended failure mode — an absent section is honest, a frozen snapshot is not. `tracker_meta.json` is rewritten on each run and records `synced_at` + the xlsx `sha256`, so item 13 always names the version it came from.

## Required attribution (copy-paste)

- `© OpenStreetMap contributors — data available under the <a href="https://opendatacommons.org/licenses/odbl/">Open Database License (ODbL)</a> (<a href="https://www.openstreetmap.org/copyright">openstreetmap.org/copyright</a>)`
- `Contorno CAOP © Direção-Geral do Território (DGT), <a href="https://www.dgterritorio.gov.pt/dados-abertos">dados abertos CC-BY 4.0</a>`
- `Dados NAP/MOBI.E (MOBI.E via NAP-IMT), listas DGEG — uso livre com menção de fonte, sem fins lucrativos`
- `Esquemas DATEX II © CEN / DATEX II (<a href="https://datex2.eu/">datex2.eu</a>)`
- `Mapas comunidade: <a href="https://umap.openstreetmap.fr/pt-pt/map/postos-de-carregamento-v21_690884">Postos de Carregamento v2.1</a> (dump <a href="https://github.com/avataranedotas/umap_postos">avataranedotas/umap_postos</a>) + <a href="https://umap.openstreetmap.fr/en/map/caca-aos-postos-de-carregamento_1386222">Caça aos Postos</a> (curadoria: Alexandre Moleiro)`

## ODbL share-alike — how to get the OSM-derived database

`data/osm_umap.csv` / `data/osm_caca.csv` (`scripts/osm_umap.py` output, gitignored), the per-site OSM fields published in `site/data/sites.json` and `site/data/points.json`, and the per-site `osm` blocks of the ohmigo dataset (`scripts/ohmigo_dataset.py`, published at `/ohmigo/chargers.json`; the ohmigo server credits OpenStreetMap whenever it shows them) are derived from OSM data and fall under ODbL. The `osm` blocks are themselves the OSM-derived database, published openly in that file. To comply:

1. Regenerate them yourself: `bash scripts/fetch_data.sh` (needs the static CSVs) then `python scripts/osm_umap.py` — method + origin URLs are in the script header and `references/data-sources.md`.
2. Or ask us for a copy of the exact CSVs behind the published dashboard (`info@ocarroeletrico.com`): we provide them under ODbL 1.0 on request to anyone who received/viewed the site, per ODbL §4.
