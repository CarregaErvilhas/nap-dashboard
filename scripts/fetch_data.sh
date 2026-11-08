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

mkdir -p data

# Fonte do estado dinâmico (evActualStatus, ~40 MB):
#   NAP_STATUS_SOURCE=nap      (omissão) directo do NAP, como sempre.
#   NAP_STATUS_SOURCE=archive  do AmpereArchive: lê $AMPERE_ARCHIVE_URL/v1/<CC>/status.json.gz
#                              (1–2 MB). Se o arquivo falhar, estiver velho
#                              (> ARCHIVE_MAX_AGE_MIN, 180 por omissão) ou truncado, cai para o NAP.
# O estático (~190 MB) continua a vir do NAP: o arquivo não guarda todos os
# campos que o dashboard usa (brandsAccepted, NUTS, contactos, ...).
NAP_STATUS_SOURCE="${NAP_STATUS_SOURCE:-nap}"
AMPERE_ARCHIVE_URL="${AMPERE_ARCHIVE_URL:-}"
AMPERE_ARCHIVE_COUNTRY="${AMPERE_ARCHIVE_COUNTRY:-PT}"
ARCHIVE_MAX_AGE_MIN="${ARCHIVE_MAX_AGE_MIN:-180}"

# check_content <file> <expect>: xml | pdf | csv:TOKEN | html-table
check_content() {
  local file="$1" expect="$2"
  case "$expect" in
    xml)        head -c 100 "$file" | grep -q '<?xml' ;;
    pdf)        head -c 5 "$file" | grep -q '%PDF' ;;
    csv:*)      head -n 1 "$file" | grep -qF "${expect#csv:}" ;;
    html-table) grep -qi '<table' "$file" ;;
    archive-status) python3 scripts/archive_status.py --check "$file" --max-age-min "$ARCHIVE_MAX_AGE_MIN" >&2 ;;
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
fetch "https://pgm.mobie.pt/integration/nap/evChargingInfra" data/evChargingInfra_latest.xml xml

# Estado dinâmico + preços OPC. O nap_etl.py usa data/evActualStatus_latest.xml
# se existir, senão data/archiveStatus_latest.json.gz; só um dos dois fica no disco.
fetch_dynamic_nap() {
  rm -f data/archiveStatus_latest.json.gz
  # NAP MOBI.E — DATEX II 3.3 dynamic status + prices (40 MB)
  fetch "https://pgm.mobie.pt/integration/nap/evActualStatus" data/evActualStatus_latest.xml xml
}

case "$NAP_STATUS_SOURCE" in
  nap) fetch_dynamic_nap ;;
  archive)
    if [ -z "$AMPERE_ARCHIVE_URL" ]; then
      echo "aviso: NAP_STATUS_SOURCE=archive sem AMPERE_ARCHIVE_URL; a usar o NAP" >&2
      fetch_dynamic_nap
    elif [[ ! "$AMPERE_ARCHIVE_COUNTRY" =~ ^[A-Z]{2}$ ]]; then
      echo "erro: AMPERE_ARCHIVE_COUNTRY inválido '$AMPERE_ARCHIVE_COUNTRY'" >&2
      exit 1
    elif fetch "${AMPERE_ARCHIVE_URL%/}/v1/${AMPERE_ARCHIVE_COUNTRY}/status.json.gz" \
         data/archiveStatus_latest.json.gz archive-status; then
      rm -f data/evActualStatus_latest.xml
    else
      echo "aviso: AmpereArchive indisponível ou desactualizado; a usar o NAP" >&2
      fetch_dynamic_nap
    fi ;;
  *) echo "erro: NAP_STATUS_SOURCE='$NAP_STATUS_SOURCE' (nap|archive)" >&2; exit 1 ;;
esac

# MOBI.E OPC tariff file (CSV, semicolon-separated, decimal comma)
# Friendly Liferay URL that always resolves to the current version.
fetch "https://www.mobie.pt/documents/42032/106470/Tarifas" data/mobie_tarifas.csv csv:UID_TOMADA

# MOBI.E PartyID (official operator/CEME codes). PDF from 2022 — outdated:
# use as reference only; many active tariff codes are missing from it.
fetch "https://www.mobie.pt/documents/42032/223588/PartyID_MOBIE.pdf/3f0f61d7-a579-ca1c-4804-a39d4f2df8bc?t=1646652329843" data/mobie_partyid.pdf pdf

# DGEG — registered OPC list (HTML table)
# 2026-10: DGEG restructured the site under DL 93/2025
# (operacao-e-comercializacao/); the old operacao-de-pontos-de-carregamento/
# deep URLs now 301 to the homepage (no <table>) and fail the content check.
fetch \
  "https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/operacao-e-comercializacao/lista-de-opc/" \
  data/dgeg_opc.html html-table -A "Mozilla/5.0 (Macintosh)"

# DGEG — registered CEME list (HTML table, transitional regime)
fetch \
  "https://www.dgeg.gov.pt/pt/areas-setoriais/energia/energia-eletrica/mobilidade-eletrica/operacao-e-comercializacao/regime-transitorio/ceme-registados/" \
  data/dgeg_ceme.html html-table -A "Mozilla/5.0 (Macintosh)"

echo "fetched:"
ls -lh data/evChargingInfra_latest.xml data/evActualStatus_latest.xml data/archiveStatus_latest.json.gz \
      data/mobie_tarifas.csv data/mobie_partyid.pdf data/dgeg_opc.html data/dgeg_ceme.html 2>/dev/null || true
