# Data sources (verified 2026-08-16)

All sources are public and free to access ("livre acesso"). Fetch everything with
`scripts/fetch_data.sh`. Prefer these origins over any local copy so the analysis
stays current.

## NAP MOBI.E — DATEX II 3.3

- **Static inventory** (sites/points/connectors), ~190 MB:
  `https://pgm.mobie.pt/integration/nap/evChargingInfra`
- **Dynamic status + prices** (per point, includes `publicationTime`), ~40 MB:
  `https://pgm.mobie.pt/integration/nap/evActualStatus`

Both are DATEX II 3.3 XML with namespaces:
`energyInfrastructure`, `facilities`, `locationReferencing`, `locationExtension`,
`commonExtension`, `common`. The schemas (v3) are vendored in `assets/schemas/`
and were downloaded from `http://datex2.eu/schema/3/<module>` (serves the XSD).

License: the NAP endpoints are published under free-access licences (see the
IMT-IP NAP pages `nap-portugal.imt-ip.pt/nap/multimodalsupplydetail/148` and
`/149`). IMT site terms: free use with source attribution, no lucrative or
illicit use — compatible with this repo's non-commercial licence, but the
dashboard footer must keep the attribution. Note MOBI.E now acts as EADME for
the NAP under DL 93/2025; a
transitional regime runs until 31 Dec 2027.

## MOBI.E OPC tariff

- CSV, semicolon-separated, decimal comma. One row per (site, plug, tariff type).
  Friendly URL that always resolves to the current version:
  `https://www.mobie.pt/documents/42032/106470/Tarifas`

  Columns: `ID;UID_TOMADA;TIPO_POSTO;MUNICIPIO;MORADA;OPERADOR;MOBICHARGER;
  NIVELTENSAO;TIPO_TARIFARIO;TIPO_TARIFA;TARIFA;TIPO_TOMADA;FORMATO_TOMADA;
  POTENCIA_TOMADA`. `TARIFA` is a text like `€ 0.261 /charge`, `€ 0.1 /kWh`,
  `€ 0.02 /min` — parse with a regex; `TIPO_TARIFA` is one of
  `FLAT | ENERGY | TIME | PARKING_TIME`.

  Licence: `© MOBI.E, all rights reserved` — no explicit reuse licence found
  on mobie.pt. Treat as factual reference; redistribution basis is unclear
  (see `THIRD-PARTY-NOTICES.md`). If MOBI.E objects, remove/redact on request.

## MOBI.E PartyID

- PDF (from ~2022 — **outdated**, use only as reference; 38 active tariff codes
  are missing from it, 22 codes in it are unused):
  `https://www.mobie.pt/documents/42032/223588/PartyID_MOBIE.pdf/3f0f61d7-a579-ca1c-4804-a39d4f2df8bc?t=1646652329843`
  Columns: `Código OCPI_Party_ID Nome Entidade CEME(eMSP) OPC(CPO)`.
  The `Código` column is the 4-letter MOBI.E code (`ACOR`, `BLUE`, …); the
  `OPC_Party_ID` column is the 3-char OCPI party id (`ACR`, `BLU`, …).

## DGEG — registered operators

- **OPC list** (HTML table `Nº | Entidade | Validade | Morada | NIF | Site`):
  `https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/operacao-de-pontos-de-carregamento/opc-para-a-mobilidade-eletrica/opc-com-reconhecimento-previo-dgeg/`
- **CEME list** (HTML table `Nº | Empresa | Sede | Site | NIPC | Obs.`):
  `https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/operacao-de-pontos-de-carregamento/comercializadores-de-eletricidade-para-a-mobilidade-eletrica/ceme-registados/`

  Note: the two tables have **different column names** (OPC: Entidade/Validade/
  Morada/NIF/Site; CEME: Empresa/Sede/Site/NIPC/Obs.). `scripts/dgeg_lists.py`
  parses the first table on each page; the CEME columns land in the same CSV
  positions, so re-check headers if DGEG changes the pages.

  Licence: DGEG site terms — free use with source mention, no commercial use
  against the public interest; IP belongs to DGEG. Keep the footer attribution.

## AFIR — power classes (reporting)

- **Regulation (EU) 2023/1804** (AFIR), stable link:
  `https://eur-lex.europa.eu/eli/reg/2023/1804/oj`
  (PT version: `https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32023R1804`).
- Neither NAP/DATEX II nor MOBI.E define power classes — they report
  continuous power (`max_power_w`, `voltage`/`max_current`). The only legal
  definitions are art. 2(37) "normal power" (≤22 kW) and art. 2(31)
  "high power" (>22 kW).
- The dashboard's `pw_class()` buckets follow **AFIR Annex III §2**
  (Member-State reporting categories), which is the established split the
  network actually needs above 150 kW:

  | Category | Subcategory | Power |
  |---|---|---|
  | Cat. 1 (AC) | slow mono-phase | P < 7,4 kW (normal) |
  | Cat. 1 (AC) | medium tri-phase | 7,4 ≤ P ≤ 22 kW (normal) |
  | Cat. 1 (AC) | fast tri-phase | P > 22 kW (high) |
  | Cat. 2 (DC) | slow | P < 50 kW |
  | Cat. 2 (DC) | fast | 50 ≤ P < 150 kW |
  | Cat. 2 (DC) | ultra-fast Level 1 | 150 ≤ P < 350 kW |
  | Cat. 2 (DC) | ultra-fast Level 2 | P ≥ 350 kW |

  The old top bucket `DC ultra (>150kW)` lumped both ultra-fast levels;
  it is now split into `DC ultra 150-350kW` (L1) and `DC ultra (>=350kW)`
  (L2, covers 350/400/600 kW HPC and future MCS).

## DATEX II XSDs

Vendored in `assets/schemas/` for enum validation (see
`assets/schemas/README.md`; re-fetch with `scripts/fetch_schemas.sh`).
Sources:
`http://datex2.eu/schema/3/energyInfrastructure`, `/facilities`,
`/locationReferencing`, `/locationExtension`, `/commonExtension`, `/common`,
`/d2Payload`.

Licence: **© CEN / DATEX II organisation — NOT covered by this repo's
PolyForm licence** (see `THIRD-PARTY-NOTICES.md`). Free to use for
implementation/validation; vendored only as enum source.

## OSM / umap (community) — cross-check

Used by `scripts/osm_umap.py` to enrich NAP sites with community-sourced operator,
payment/authentication and location-doubt data. These are **not official sources**
— they are community-maintained maps/dumps; use as a lead for field verification,
never as ground truth. Fetches are cached in `umap_cache/` (gitignored).

Licence: underlying OSM data is **ODbL 1.0** — public use requires `©`
OpenStreetMap contributors + ODbL link **in the dashboard itself** (footer +
map attribution, done) and the OSM-derived CSVs/fields stay under ODbL
(share-alike; see `THIRD-PARTY-NOTICES.md` for how to obtain them). The two
umap layers below additionally carry their curators' own rights (no explicit
licence found) — always credit + link them.

- **Raw Overpass dump `Todos.json`** (primary source) — every OSM
  `amenity=charging_station` and `man_made=charge_point` element in Portugal,
  ~21.7k elements. From the author of the "Postos de Carregamento v2.1" map:
  `https://raw.githubusercontent.com/avataranedotas/umap_postos/main/Todos.json`
  (a `main`/`refs/heads/main` variant also works).
  Note: charging sites are tagged two ways — `amenity=charging_station` (node **or**
  way) and `man_made=charge_point` (node only). **Zero elements carry both tags**,
  so match by *either*. The `charge_point` nodes carry explicit `payment:*` /
  `authentication:*` tags that `charging_station` elements usually lack.

- **umap "Postos de Carregamento v2.1"** (map id `690884`, curadoria: Alexandre
  Moleiro) — the community OSM
  map the dump above was generated from. Its `Areas.geojson` export (remote
  `https://raw.githubusercontent.com/avataranedotas/umap_postos/main/Areas.geojson`)
  has ~1 854 polygons but only ~3.7k NAP-site matches; the raw dump (7.9k) is
  preferred, so the Areas.geojson is now superseded.
  URL: `https://umap.openstreetmap.fr/pt-pt/map/postos-de-carregamento-v21_690884`

- **umap "Caça aos Postos de Carregamento"** (map id `1386222`, curadoria:
  Alexandre Moleiro) — community doubt
  map. The relevant layer is "Possíveis novos postos" (~104 points: possible new
  posts, "nada no local" flags, under-construction, to-verify); the "Dúvidas"
  layer is empty in all published versions.
  URL: `https://umap.openstreetmap.fr/en/map/caca-aos-postos-de-carregamento_1386222`

- **umap API endpoints** (used to fetch the map settings + layer features):
  - Map settings (GeoJSON): `https://umap.openstreetmap.fr/en/map/{map_id}/geojson/`
  - Layer features: `https://umap.openstreetmap.fr/en/datalayer/{map_id}/{pk}/`
  - Full map download: `https://umap.openstreetmap.fr/map/{map_id}/download/`

## CAOP — concelho boundaries (geographic reference)

Used by `scripts/concelho_check.py` (point-in-polygon → concelho) and
`scripts/make_pt_outline.py` (PT outline + district/island labels). Downloaded on
first run into `caop_cache/` (gitignored) from the `jotanmiguel/caop_GeoJSON`
fork (kept current; the upstream `nmota/caop_GeoJSON` mirror is older) of
official CAOP data (WGS84 `geograficas` variants):
`https://raw.githubusercontent.com/jotanmiguel/caop_GeoJSON/master/`

- `geograficas/ContinenteConcelhos.geojson` — mainland concelhos
  (props `Concelho`, `Distrito`, `Area_Ha`)
- `geograficas/A%C3%A7ores/A%C3%A7oresConcelhos.geojson` — Açores
  (props `MUNICIPIO`, `ILHA`, `AREA_HA`)
- `geograficas/Madeira/MadeiraConcelhos.geojson` — Madeira
  (props `Municipio`, `Ilha`, `Area_Ha`)

Licence: official CAOP data is DGT open data under **CC-BY 4.0** — free use
incl. commercial, **must credit Direção-Geral do Território** (footer + map
attribution, done). The `jotanmiguel/caop_GeoJSON` fork itself has no explicit
licence; the data is DGT's. `assets/pt_outline.json` and any CAOP-derived
geometry are **excluded from this repo's PolyForm non-commercial restriction**
(see `THIRD-PARTY-NOTICES.md`).

## Related / context

- OCPI integration doc (party-id rules, EVSE ID format): `20230620_MOBIE_OCPI_Phase2_Internal_v1_6.pdf`
  on mobie.pt documents.
- MOBI.Data portal (aggregated stats): `https://www.mobie.pt/mobilidade/mobi.data`
- ERSE tariffs: `https://www.erse.pt/eletricidade/mobilidade-eletrica/tarifas-e-precos/`