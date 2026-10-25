#!/usr/bin/env bash
# Fetch the PCVE error tracker (pt-pcve-errors.xlsx) for the pipeline.
# Run from the repo root:  bash scripts/fetch_tracker.sh
#
# The tracker is the data owners' own error list: real defects per operator and
# asset, with the value each owner considers correct, the status
# (TO FIX / FIXED / DOUBT) and the dates requested/fixed. Two products come out
# of it (scripts/tracker_sync.py):
#
#   * the authoritative OPC table (`CPO` tab): PartyId -> PartyCode -> name.
#     Only *current* source of OPC identity — the MOBI.E PartyID PDF is 2022;
#   * the declared-dead assets ("Remove. Replaced with new asset"), i.e. a
#     positive list of assets that should no longer be published.
#
# Three fetch strategies, tried in order; none of them may fail the pipeline
# (the versioned snapshot in git is the fallback, and its age is reported):
#
#   1. TRACKER_URL set  -> anonymous download. This is what CI uses: the file is
#      shared by its owner as "anyone with the link", so no credentials are
#      needed. On GitHub, keep the URL in a repo *secret* (TRACKER_URL), not in
#      the workflow: nap-dashboard is a public repo and the pointer to the data
#      owners' file should not be published there.
#   2. `gog` available  -> authenticated Drive download, for when link sharing is
#      off. Needs local Drive credentials, so it never works in CI.
#   3. neither          -> warn and keep the versioned snapshot.
#
# TRACKER_URL may be either endpoint. The original copy was an Office file, NOT
# a native Google Sheet, so the Sheets API and /export?format=xlsx rejected it
# with `400 failedPrecondition: must not be an Office file` and
# `drive.google.com/uc?export=download` was needed. The current copy is a native
# Sheet (2026-10-24), where `…/export?format=xlsx` works.
#
# Escape hatches: SKIP_TRACKER=1 to skip entirely, TRACKER_FILE to change the
# destination name.
set -euo pipefail

mkdir -p data

DEST="${TRACKER_FILE:-data/pt_pcve_errors.xlsx}"
# No default file id on purpose: this repo is public, so the pointer to the data
# owners' file lives in the environment/secret, never in the source.
FILE_ID="${TRACKER_FILE_ID:-}"
TMP="${DEST}.download"

if [ "${SKIP_TRACKER:-0}" = "1" ]; then
  echo "tracker: SKIP_TRACKER=1, mantendo ${DEST} (se existir)"
  exit 0
fi

# An Office file is a ZIP container ("PK"). Anything else — an HTML login page,
# Drive's "can't scan for viruses" interstitial, a truncated transfer — is not
# the tracker and must never overwrite the last good copy. Silencioso: quem
# chama decide o que dizer, para uma tentativa não duplicar o aviso.
accept() {
  [ -s "$1" ] && head -c 2 "$1" | grep -q 'PK'
}

fetched=0
tried=""
LAST_CODE=""
LAST_BODY=""

# Uma tentativa de download anónimo. Guarda o código HTTP e o corpo da resposta
# para o aviso final ser diagnosticável: sem isto, um HTTP 400 do Google parecia
# o mesmo que "URL não configurada".
try_anonymous() {
  local code
  code=$(curl -sSL --retry 2 --max-time 120 -w '%{http_code}' \
              "$@" -o "$TMP" 2>/dev/null) || code="curl_error"
  LAST_CODE="$code"
  if [ "$code" = "200" ]; then
    if accept "$TMP"; then return 0; fi
    LAST_BODY="$(head -c 200 "$TMP" | tr -d '\0' | tr '\n' ' ')"
    LAST_BODY="200 mas não é ZIP: ${LAST_BODY}"
  else
    [ -s "$TMP" ] && LAST_BODY="$(head -c 200 "$TMP" | tr -d '\0' | tr '\n' ' ')"
  fi
  rm -f "$TMP"
  return 1
}

# 1. anonymous (CI path)
if [ -n "${TRACKER_URL:-}" ]; then
  tried="TRACKER_URL"
  echo "-> ${DEST} (anónimo, TRACKER_URL)"
  # O Drive respondeu HTTP 400 ao IP das runners do GitHub (não 403), por isso
  # a hipótese de bloqueio de IP não está confirmada. Tentamos primeiro o curl
  # simples; se falhar, com um User-Agent de browser e com confirm=t, que é o
  # que o Drive usa quando o download passa pelo interstitial de virus scan.
  UA_BROWSER='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
  if try_anonymous "$TRACKER_URL"; then
    mv "$TMP" "$DEST"; fetched=1
  elif try_anonymous -A "$UA_BROWSER" "${TRACKER_URL/&/&confirm=t&}"; then
    echo "   (o Download só passou com User-Agent de browser + confirm=t)" >&2
    mv "$TMP" "$DEST"; fetched=1
  else
    echo "       a origem respondeu HTTP ${LAST_CODE}" >&2
    [ -n "$LAST_BODY" ] && echo "       corpo: ${LAST_BODY}" >&2
    # Distingue "o Drive bloqueia este IP" de "a Google está inacessível a
    # partir das runners": a API responde sem auth com 401, o que já prova que
    # o endpoint chega. Se 401, uma service account resolve; se a chamada não
    # volta, é bloqueio de IP e não há atalho sem sair do GitHub-hosted.
    api_code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 20 \
               "https://www.googleapis.com/drive/v3/about" 2>/dev/null) \
               || api_code="sem_resposta"
    echo "       Google Drive API alcançável a partir daqui: HTTP ${api_code}" >&2
    case "$api_code" in
      401) echo "       -> o endpoint responde: uma service account resolveria" >&2 ;;
      sem_resposta|000) echo "       -> sem rota: o Google parece cortar os IPs das runners" >&2 ;;
      *) echo "       -> respondeu com ${api_code}; olhar para o proxy de rede" >&2 ;;
    esac
  fi
fi

# 2. authenticated (local path; also the fallback if 1 failed)
if [ "$fetched" -eq 0 ] && [ -n "$FILE_ID" ] && command -v gog >/dev/null 2>&1; then
  echo "-> ${DEST} (Drive autenticado, id ${FILE_ID})"
  if gog drive download "$FILE_ID" --out "$TMP" --overwrite 2>/dev/null \
     && accept "$TMP"; then
    mv "$TMP" "$DEST"; fetched=1
  fi
fi

if [ "$fetched" -eq 0 ]; then
  if [ -n "$tried" ]; then
    echo "aviso: o tracker não foi descarregado (tentado: ${tried})" >&2
    echo "       via curl simples e via User-Agent de browser; última resposta:" >&2
    echo "       HTTP ${LAST_CODE:-?} ${LAST_BODY}" >&2
  else
    echo "aviso: o tracker não foi descarregado (nem TRACKER_URL nem 'gog' com" >&2
    echo "       TRACKER_FILE_ID estão disponíveis)." >&2
  fi
  echo "       O pipeline continua sem o cross-check: o item 13 de errors.md" >&2
  echo "       simplesmente não é escrito nesta corrida. Preferimos uma secção" >&2
  echo "       em falta a um item congelado sem dizer nada." >&2
  rm -f "$TMP"
  exit 0
fi

ls -lh "$DEST"
