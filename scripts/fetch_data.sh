#!/usr/bin/env bash
# Fetch fresh public data from official sources into the repo working dir.
# Run from the repo root:  bash scripts/fetch_data.sh
# Downloads ~230 MB (two NAP XMLs). Each URL below is the live origin, so
# re-running this keeps the analysis current without storing data in git.
#
# Each download goes to <dest>.download first and is only renamed on success,
# so a failed/interrupted run never leaves a truncated file pretending to be
# the real one. Empty downloads fail loudly, and every file passes a content
# ("magic") check — a 200 carrying an HTML error page (ex. Liferay a devolver
# HTML em vez do CSV) tem tamanho >0 e passava no teste anterior.
set -euo pipefail

# check_content <file> <expect>: xml | pdf | csv:TOKEN | html-table
check_content() {
  local file="$1" expect="$2"
  case "$expect" in
    xml)        head -c 100 "$file" | grep -q '<?xml' ;;
    pdf)        head -c 5 "$file" | grep -q '%PDF' ;;
    csv:*)      head -n 1 "$file" | grep -qF "${expect#csv:}" ;;
    html-table) grep -qi '<table' "$file" ;;
    *) echo "erro interno: expect desconhecido '$expect'" >&2; return 1 ;;
  esac
}

fetch() {
  local url="$1" dest="$2" expect="$3"
  shift 3
  curl -fsSL --retry 2 "$@" "$url" -o "${dest}.download"
  if [ ! -s "${dest}.download" ]; then
    echo "erro: download vazio para ${dest} ($url)" >&2
    rm -f "${dest}.download"
    return 1
  fi
  if ! check_content "${dest}.download" "$expect"; then
    echo "erro: ${dest} não passa na verificação de conteúdo ($expect); a origem devolveu outra coisa?" >&2
    rm -f "${dest}.download"
    return 1
  fi
  mv "${dest}.download" "$dest"
}

# NAP MOBI.E — DATEX II 3.3 static inventory of sites/points (200 MB)
fetch "https://pgm.mobie.pt/integration/nap/evChargingInfra" evChargingInfra_latest.xml xml

# NAP MOBI.E — DATEX II 3.3 dynamic status + prices (40 MB)
fetch "https://pgm.mobie.pt/integration/nap/evActualStatus" evActualStatus_latest.xml xml

# MOBI.E OPC tariff file (CSV, semicolon-separated, decimal comma)
# Friendly Liferay URL that always resolves to the current version.
fetch "https://www.mobie.pt/documents/42032/106470/Tarifas" mobie_tarifas.csv csv:UID_TOMADA

# MOBI.E PartyID (official operator/CEME codes). PDF from 2022 — outdated:
# use as reference only; many active tariff codes are missing from it.
fetch "https://www.mobie.pt/documents/42032/223588/PartyID_MOBIE.pdf/3f0f61d7-a579-ca1c-4804-a39d4f2df8bc?t=1646652329843" mobie_partyid.pdf pdf

# DGEG — registered OPC list (HTML table)
fetch \
  "https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/operacao-de-pontos-de-carregamento/opc-para-a-mobilidade-eletrica/opc-com-reconhecimento-previo-dgeg/" \
  dgeg_opc.html html-table -A "Mozilla/5.0 (Macintosh)"

# DGEG — registered CEME list (HTML table)
fetch \
  "https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/operacao-de-pontos-de-carregamento/comercializadores-de-eletricidade-para-a-mobilidade-eletrica/ceme-registados/" \
  dgeg_ceme.html html-table -A "Mozilla/5.0 (Macintosh)"

echo "fetched:"
ls -lh evChargingInfra_latest.xml evActualStatus_latest.xml mobie_tarifas.csv \
      mobie_partyid.pdf dgeg_opc.html dgeg_ceme.html
