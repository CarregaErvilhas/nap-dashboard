#!/usr/bin/env bash
# Fetch the MOBI.E/PCVE error tracker (pt-pcve-errors.xlsx) from Drive.
# Run from the repo root:  bash scripts/fetch_tracker.sh
#
# The tracker is the data owners' own error list: a curated table of real
# defects reported per operator/asset, with the *correct* value, the status
# (TO FIX / FIXED / DOUBT) and the dates requested/fixed. Two things come out
# of it and feed the pipeline (scripts/tracker_sync.py):
#
#   * the authoritative OPC table (CPO tab): PartyId -> PartyCode -> name,
#     which is the only current source of OPC identity — the MOBI.E PartyID
#     PDF is from 2022;
#   * the declared-dead assets ("Remove. Replaced with new asset"), i.e. a
#     positive list of assets that should NOT be published any more.
#
# It is an Office file, not a native Google Sheet: the Sheets API rejects it
# with `400 failedPrecondition: must not be an Office file`, so this uses the
# Drive API (gog) and a plain download, never the Sheets API.
#
# This step needs Drive credentials, so it is LOCAL-ONLY by design: the weekly
# CI has no auth for this file and reuses the last committed
# opc_registry_authority.csv (see scripts/tracker_meta.json for its age). It
# never fails the pipeline — missing/stale tracker is reported, not fatal.
#
# Override the file id with TRACKER_FILE_ID, or skip with SKIP_TRACKER=1.
set -euo pipefail

DEST="${TRACKER_FILE:-pt_pcve_errors.xlsx}"
FILE_ID="${TRACKER_FILE_ID:-1zsEHrtPvcjDXJxuoyoPlqTMv3BPxW6ZW}"

if [ "${SKIP_TRACKER:-0}" = "1" ]; then
  echo "tracker: SKIP_TRACKER=1, mantendo ${DEST} (se existir)"
  exit 0
fi

if ! command -v gog >/dev/null 2>&1; then
  echo "aviso: 'gog' não está instalado — tracker não descarregado." >&2
  echo "       O pipeline continua com a última opc_registry_authority.csv versionada." >&2
  exit 0
fi

echo "-> ${DEST} (Drive ${FILE_ID})"
if ! gog drive download "$FILE_ID" --out "${DEST}.download" --overwrite; then
  echo "aviso: download do tracker falhou — o pipeline continua com o registo versionado." >&2
  rm -f "${DEST}.download"
  exit 0
fi

# Content check: an Office file is a ZIP container ("PK"). A failed download
# or an auth error page would otherwise pass a plain size test.
if ! head -c 2 "${DEST}.download" | grep -q 'PK'; then
  echo "aviso: ${DEST}.download não é um xlsx (ZIP) — o download foi descartado." >&2
  rm -f "${DEST}.download"
  exit 0
fi
if [ ! -s "${DEST}.download" ]; then
  echo "aviso: download do tracker vazio — descartado." >&2
  rm -f "${DEST}.download"
  exit 0
fi

mv "${DEST}.download" "$DEST"
ls -lh "$DEST"
