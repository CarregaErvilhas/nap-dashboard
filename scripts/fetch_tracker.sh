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
# `drive.google.com/uc?export=download` is the right endpoint here: the file is
# an Office file, NOT a native Google Sheet, so both the Sheets API and the
# /export?format=xlsx endpoint reject it with
# `400 failedPrecondition: must not be an Office file`.
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
# the tracker and must never overwrite the last good copy.
accept() {
  if [ ! -s "$1" ]; then
    echo "aviso: download do tracker vazio — descartado." >&2
    rm -f "$1"; return 1
  fi
  if ! head -c 2 "$1" | grep -q 'PK'; then
    echo "aviso: o download não é um xlsx (ZIP) — descartado." >&2
    head -c 200 "$1" | tr -d '\0' | sed 's/^/        /' >&2 || true
    rm -f "$1"; return 1
  fi
  return 0
}

fetched=0
tried=""

# 1. anonymous (CI path)
if [ -n "${TRACKER_URL:-}" ]; then
  echo "-> ${DEST} (anónimo, TRACKER_URL)"
  tried="TRACKER_URL"
  # Sem -f: queremos o corpo para o accept() poder dizer O QUE voltou. Guardamos
  # o código HTTP para o aviso final ser diagnosticável — a primeira versão
  # silenciava o curl com 2>/dev/null e um 403 do Google parecia "sem URL".
  code=$(curl -sSL --retry 2 --max-time 120 -w '%{http_code}' \
              "$TRACKER_URL" -o "$TMP" 2>/dev/null) || code="curl_error"
  if [ "$code" != "200" ]; then
    echo "       a origem respondeu HTTP ${code} (o Drive pode estar a bloquear" >&2
    echo "       o IP das runners ou a pedir interstitial)" >&2
    rm -f "$TMP"
  elif accept "$TMP"; then
    mv "$TMP" "$DEST"; fetched=1
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
    echo "aviso: o tracker não foi descarregado (tentado: ${tried})." >&2
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
