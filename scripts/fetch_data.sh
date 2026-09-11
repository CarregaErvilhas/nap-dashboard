#!/usr/bin/env bash
# Fetch fresh public data from official sources into the repo working dir.
# Run from the repo root:  bash scripts/fetch_data.sh
# Downloads ~230 MB (two NAP XMLs). Each URL below is the live origin, so
# re-running this keeps the analysis current without storing data in git.
#
# Each download goes to <dest>.download first and is only renamed on success,
# so a failed/interrupted run never leaves a truncated file pretending to be
# the real one. Empty downloads fail loudly.
set -euo pipefail

fetch() {
  local url="$1" dest="$2"
  shift 2
  curl -fsSL --retry 2 "$@" "$url" -o "${dest}.download"
  if [ ! -s "${dest}.download" ]; then
    echo "erro: download vazio para ${dest} ($url)" >&2
    rm -f "${dest}.download"
    return 1
  fi
  mv "${dest}.download" "$dest"
}

# NAP MOBI.E — DATEX II 3.3 static inventory of sites/points (200 MB)
fetch "https://pgm.mobie.pt/integration/nap/evChargingInfra" evChargingInfra_latest.xml

# NAP MOBI.E — DATEX II 3.3 dynamic status + prices (40 MB)
fetch "https://pgm.mobie.pt/integration/nap/evActualStatus" evActualStatus_latest.xml

# MOBI.E OPC tariff file (CSV, semicolon-separated, decimal comma)
# Friendly Liferay URL that always resolves to the current version.
fetch "https://www.mobie.pt/documents/42032/106470/Tarifas" mobie_tarifas.csv

# MOBI.E PartyID (official operator/CEME codes). PDF from 2022 — outdated:
# use as reference only; many active tariff codes are missing from it.
fetch "https://www.mobie.pt/documents/42032/223588/PartyID_MOBIE.pdf/3f0f61d7-a579-ca1c-4804-a39d4f2df8bc?t=1646652329843" mobie_partyid.pdf

# DGEG — registered OPC list (HTML table)
fetch \
  "https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/operacao-de-pontos-de-carregamento/opc-para-a-mobilidade-eletrica/opc-com-reconhecimento-previo-dgeg/" \
  dgeg_opc.html -A "Mozilla/5.0 (Macintosh)"

# DGEG — registered CEME list (HTML table)
fetch \
  "https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/operacao-de-pontos-de-carregamento/comercializadores-de-eletricidade-para-a-mobilidade-eletrica/ceme-registados/" \
  dgeg_ceme.html -A "Mozilla/5.0 (Macintosh)"

echo "fetched:"
ls -lh evChargingInfra_latest.xml evActualStatus_latest.xml mobie_tarifas.csv \
      mobie_partyid.pdf dgeg_opc.html dgeg_ceme.html