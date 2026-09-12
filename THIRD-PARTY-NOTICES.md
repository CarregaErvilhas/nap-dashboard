# Third-party notices — nap-dashboard

Our code/template/docs are `PolyForm-Noncommercial-1.0.0` (see `LICENSE`).
Everything below keeps its **own licence/terms** and is **not** covered by
PolyForm. Where embedded in `dashboard.html`, the dashboard is a collective
work: our code is PolyForm-Noncommercial, the embedded third-party portions
stay under their own terms.

## Data sources and schemas

| Resource | Origin | Licence / terms | What we do |
|---|---|---|---|
| NAP MOBI.E static + dynamic feeds (DATEX II 3.3 XML) | `https://pgm.mobie.pt/integration/nap/evChargingInfra`, `/evActualStatus` via NAP `nap-portugal.imt-ip.pt` (fichas 148/149, org. MOBI.E) | IMT NAP terms: free use **with source attribution, no lucrative/illicit use**. AFIR/NAP free-access framework. | Attribution in dashboard footer + here. Not re-licensed. |
| MOBI.E OPC tariff CSV + PartyID PDF | `https://www.mobie.pt/documents/42032/106470/Tarifas`, `.../PartyID_MOBIE.pdf/...` | `© MOBI.E, all rights reserved` — **no explicit reuse licence**. Used as factual reference; redistribution basis unclear. | Attribution in footer. If MOBI.E objects, we remove/redact on request. Contact in `LICENSE`. |
| DGEG OPC / CEME lists | `https://www.dgeg.gov.pt/.../opc-com-reconhecimento-previo-dgeg/`, `.../ceme-registados/` | DGEG site terms: free use **with source mention, no commercial use** against public interest; IP belongs to DGEG. | Attribution in footer + here. |
| CAOP concelho boundaries (via `jotanmiguel/caop_GeoJSON` fork of official DGT data) | `https://raw.githubusercontent.com/jotanmiguel/caop_GeoJSON/master/geograficas/...` — official data: DGT | **CC-BY 4.0** (DGT open data): free use incl. commercial, **must credit Direção-Geral do Território**. The GitHub fork itself has no explicit licence; the underlying data is DGT's. | `assets/pt_outline.json` + concelho check derived from it. Credited as `© DGT (CAOP)` in footer, map and here. This file and any CAOP-derived geometry are **excluded from the PolyForm non-commercial restriction**. |
| OpenStreetMap data (via `avataranedotas/umap_postos` `Todos.json` Overpass dump) | `https://raw.githubusercontent.com/avataranedotas/umap_postos/main/Todos.json` | **ODbL 1.0**: **must credit `© OpenStreetMap contributors`** + make clear data is available under ODbL (link below); derivative databases shared under ODbL on public use. | Credited in footer + map. Per-site OSM fields in `dashboard.html` (`pay`, `osm_op`, `osm_access`, `osm_fee`, `ad_hoc`, `doubt`) are ODbL-covered. |
| Community umap layers | `Postos de Carregamento v2.1` (`https://umap.openstreetmap.fr/pt-pt/map/postos-de-carregamento-v21_690884`, map 690884) and `Caça aos Postos de Carregamento` (`https://umap.openstreetmap.fr/en/map/caca-aos-postos-de-carregamento_1386222`, map 1386222) | ODbL (underlying OSM) **plus the curators' own rights** (no explicit licence found). | Credited + linked in footer and here. Treat as reference leads, never ground truth. |
| DATEX II 3.3 XSDs (`assets/schemas/*.xsd`) | `http://datex2.eu/schema/3/<module>` (see `assets/schemas/README.md`) | **© CEN / DATEX II organisation**. Free to use for implementation; **not** re-licensed under PolyForm. | Vendored copies kept only for enum validation (`scripts/check_quality.py`, `scripts/extract_enums.py`). Re-fetch with `scripts/fetch_schemas.sh`. |
| Python runtime deps | `requirements.txt` (`pandas`, `lxml`, `pdfplumber`, transitive `numpy`) | BSD-3 / BSD / MIT (permissive). Not distributed, installed via pip. | Compatible. No action needed. |
| GitHub Actions (`checkout`, `setup-python`, `upload-artifact`, `deploy-pages`) | `actions/*` | MIT. Build-time only, not distributed. | Compatible. |

## Required attribution (copy-paste)

- `© OpenStreetMap contributors — data available under the <a href="https://opendatacommons.org/licenses/odbl/">Open Database License (ODbL)</a> (<a href="https://www.openstreetmap.org/copyright">openstreetmap.org/copyright</a>)`
- `Contorno CAOP © Direção-Geral do Território (DGT), <a href="https://www.dgterritorio.gov.pt/dados-abertos">dados abertos CC-BY 4.0</a>`
- `Dados NAP/MOBI.E (MOBI.E via NAP-IMT), listas DGEG — uso livre com menção de fonte, sem fins lucrativos`
- `Esquemas DATEX II © CEN / DATEX II (<a href="https://datex2.eu/">datex2.eu</a>)`
- `Mapas comunidade: <a href="https://umap.openstreetmap.fr/pt-pt/map/postos-de-carregamento-v21_690884">Postos de Carregamento v2.1</a> (dump <a href="https://github.com/avataranedotas/umap_postos">avataranedotas/umap_postos</a>) + <a href="https://umap.openstreetmap.fr/en/map/caca-aos-postos-de-carregamento_1386222">Caça aos Postos</a>`

## ODbL share-alike — how to get the OSM-derived database

`osm_umap.csv` / `osm_caca.csv` (`scripts/osm_umap.py` output, gitignored) and
the per-site OSM fields embedded in `dashboard.html` are derived from OSM data
and fall under ODbL. To comply:

1. Regenerate them yourself: `bash scripts/fetch_data.sh` (needs the static
   CSVs) then `python scripts/osm_umap.py` — method + origin URLs are in the
   script header and `references/data-sources.md`.
2. Or ask us for a copy of the exact CSVs behind the published dashboard
   (`info@ocarroeletrico.com`): we provide them under ODbL 1.0 on request to
   anyone who received/viewed the dashboard, per ODbL §4.
