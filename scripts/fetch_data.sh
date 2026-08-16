#!/usr/bin/env bash
# Fetch fresh public data from official sources into the repo working dir.
# Run from the repo root:  bash scripts/fetch_data.sh
# Downloads ~230 MB (two NAP XMLs). Each URL below is the live origin, so
# re-running this keeps the analysis current without storing data in git.
set -euo pipefail

# NAP MOBI.E — DATEX II 3.3 static inventory of sites/points (200 MB)
curl -fsSL --retry 2 \
  "https://pgm.mobie.pt/integration/nap/evChargingInfra" \
  -o evChargingInfra_latest.xml

# NAP MOBI.E — DATEX II 3.3 dynamic status + prices (40 MB)
curl -fsSL --retry 2 \
  "https://pgm.mobie.pt/integration/nap/evActualStatus" \
  -o evActualStatus_latest.xml

# MOBI.E OPC tariff file (CSV, semicolon-separated, decimal comma)
# Friendly Liferay URL that always resolves to the current version.
curl -fsSL --retry 2 \
  "https://www.mobie.pt/documents/42032/106470/Tarifas" \
  -o mobie_tarifas.csv

# MOBI.E PartyID (official operator/CEME codes). PDF from 2022 — outdated:
# use as reference only; many active tariff codes are missing from it.
curl -fsSL --retry 2 \
  "https://www.mobie.pt/documents/42032/223588/PartyID_MOBIE.pdf/3f0f61d7-a579-ca1c-4804-a39d4f2df8bc?t=1646652329843" \
  -o mobie_partyid.pdf

# DGEG — registered OPC list (HTML table)
curl -fsSL --retry 2 -A "Mozilla/5.0 (Macintosh)" \
  "https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/operacao-de-pontos-de-carregamento/opc-para-a-mobilidade-eletrica/opc-com-reconhecimento-previo-dgeg/" \
  -o dgeg_opc.html

# DGEG — registered CEME list (HTML table)
curl -fsSL --retry 2 -A "Mozilla/5.0 (Macintosh)" \
  "https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/operacao-de-pontos-de-carregamento/comercializadores-de-eletricidade-para-a-mobilidade-eletrica/ceme-registados/" \
  -o dgeg_ceme.html

echo "fetched:"
ls -lh evChargingInfra_latest.xml evActualStatus_latest.xml mobie_tarifas.csv \
      mobie_partyid.pdf dgeg_opc.html dgeg_ceme.html
