#!/usr/bin/env bash
# Fetch fresh public data from official sources into the repo working dir.
# Run from the repo root:  bash scripts/fetch_data.sh
# Downloads up to ~230 MB (two NAP XMLs). Each URL below is the live origin, so
# re-running this keeps the analysis current without storing data in git.
# The static inventory is asked with If-None-Match: while the NAP answers 304,
# the copy already in data/ is used (see fetch_cached).
#
# Each download goes to <dest>.download first and is only renamed on success,
# so a failed/interrupted run never leaves a truncated file pretending to be
# the real one. Empty downloads fail loudly, and every file passes a content
# ("magic") check — a 200 carrying an HTML error page (ex. o mobie.pt a
# redireccionar um ficheiro para uma página HTML) tem tamanho >0 e passava no
# teste anterior.
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

# check_content <file> <expect>: xml | csv:TOKEN | json:KEY | html-table | archive-status
check_content() {
  local file="$1" expect="$2"
  case "$expect" in
    xml)        head -c 100 "$file" | grep -q '<?xml' ;;
    csv:*)      head -n 1 "$file" | grep -qF "${expect#csv:}" ;;
    json:*)     python3 -c 'import json,sys; sys.exit(0 if sys.argv[2] in json.load(open(sys.argv[1])) else 1)' "$file" "${expect#json:}" 2>/dev/null ;;
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

# fetch_cached <url> <dest> <expect>: like fetch, but keeps the response's ETag
# in <dest>.etag and sends it back next time. A 304 keeps <dest> as it is.
# Without both files, or if <dest> fails the content check, it is a plain full
# download. The ETag is only ever left beside the file it came with.
fetch_cached() {
  local url="$1" dest="$2" expect="$3"
  local etag_file="${dest}.etag" headers="${dest}.headers" code etag
  local cond=()
  if [ -s "$dest" ] && [ -s "$etag_file" ] && check_content "$dest" "$expect"; then
    cond=(-H "If-None-Match: $(cat "$etag_file")")
  fi
  rm -f "${dest}.download"
  # ${cond[@]+...}: an empty array trips `set -u` on the bash 3.2 of macOS.
  code=$(curl -fsSL --retry 2 ${cond[@]+"${cond[@]}"} -D "$headers" -w '%{http_code}' \
    "$url" -o "${dest}.download")
  if [ "$code" = 304 ] && [ "${#cond[@]}" -gt 0 ]; then
    echo "${dest}: 304, a origem não mudou; fica a cópia local"
    rm -f "${dest}.download" "$headers"
    return 0
  fi
  if [ "$code" != 200 ] || [ ! -s "${dest}.download" ] || ! check_content "${dest}.download" "$expect"; then
    echo "erro: ${dest}: HTTP $code, vazio ou não passa na verificação de conteúdo ($expect)" >&2
    rm -f "${dest}.download" "$headers"
    return 1
  fi
  # The last response's header: -L writes one block per redirect.
  etag=$(awk '/^HTTP\//{e=""} tolower($1)=="etag:"{sub(/^[^:]*:[ \t]*/, ""); sub(/\r$/, ""); e=$0} END{print e}' "$headers")
  rm -f "$etag_file" "$headers"
  mv "${dest}.download" "$dest"
  if [ -n "$etag" ]; then printf '%s\n' "$etag" > "$etag_file"; fi
}

# NAP MOBI.E — DATEX II 3.3 static inventory of sites/points (~190 MB, changes
# about once a day)
fetch_cached "https://pgm.mobie.pt/integration/nap/evChargingInfra" data/evChargingInfra_latest.xml xml

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

# MOBI.E OPC tariffs. Until 2026-11-09 a CSV on mobie.pt
# (documents/42032/106470/Tarifas); the new site dropped it and now redirects
# that URL to an HTML page. The MOBI.Data portal publishes the same data as two
# JSON files (its map's "Exportar CSV" joins them in the browser);
# mobie_tariffs.py rebuilds data/mobie_tarifas.csv in the old layout from them.
# Not in the new source: NIVELTENSAO (BTN/BTE/MT) and PARKING_TIME.
fetch "https://data.mobie.pt/data/tariffs.json" data/mobie_tariffs.json json:sets
fetch "https://data.mobie.pt/data/stations.json" data/mobie_stations.json json:stations
python3 scripts/mobie_tariffs.py

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
      data/mobie_tariffs.json data/mobie_stations.json data/mobie_tarifas.csv data/dgeg_opc.html data/dgeg_ceme.html 2>/dev/null || true
