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
`/149`). Note MOBI.E now acts as EADME for the NAP under DL 93/2025; a
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

## DATEX II XSDs

Vendored in `assets/schemas/` for enum validation. Sources:
`http://datex2.eu/schema/3/energyInfrastructure`, `/facilities`,
`/locationReferencing`, `/locationExtension`, `/commonExtension`, `/common`,
`/d2Payload`.

## Related / context

- OCPI integration doc (party-id rules, EVSE ID format): `20230620_MOBIE_OCPI_Phase2_Internal_v1_6.pdf`
  on mobie.pt documents.
- MOBI.Data portal (aggregated stats): `https://www.mobie.pt/mobilidade/mobi.data`
- ERSE tariffs: `https://www.erse.pt/eletricidade/mobilidade-eletrica/tarifas-e-precos/`