#!/usr/bin/env bash
# Fetch the catalogue of charger models for charger_models.py and hardware_checks.py.
# Run from the repo root:  bash scripts/fetch_charger_models.sh
#
# The catalogue is a public Google Doc ("Modelos de Carregadores usados em
# Portugal") that Alexandre Moleiro keeps, free to use: per model and version,
# the maximum DC voltage and current (`1000V 200A`), the total power and what
# each car gets at 400 V and 800 V. charger_models.py parses it (the network
# model's `models`); hardware_checks.py reads the rated voltage (errors.md
# item 14).
#
#   * Fetched fresh on every run (data/ is gitignored), so it never goes stale.
#   * A failed fetch never fails the pipeline: the model then has no `models`,
#     and hardware_checks.py runs on OSM's socket voltages alone and says so.
#
# CHARGER_MODELS_URL overrides the Doc's plain-text export below; a local copy
# works too: CHARGER_MODELS_FILE=path/to/export.txt.
CHARGER_MODELS_URL="${CHARGER_MODELS_URL:-https://docs.google.com/document/d/1SyhISXEaZiAPYuRLQ9dA2OtFrwysFm01Yei11qTLQLw/export?format=txt}"
set -euo pipefail

mkdir -p data
DEST=data/charger_models.txt
TMP="${DEST}.download"

# A real export has many `§.Marca.Modelo` lines. A login page, Google's
# interstitial or a truncated transfer does not, and must not replace anything.
accept() {
  [ -s "$1" ] && [ "$(grep -c '^§\.' "$1" || true)" -ge 20 ]
}

if [ -n "${CHARGER_MODELS_FILE:-}" ]; then
  cp "$CHARGER_MODELS_FILE" "$TMP"
elif [ -n "${CHARGER_MODELS_URL:-}" ]; then
  code=$(curl -sSL --retry 2 --max-time 60 -w '%{http_code}' \
              "$CHARGER_MODELS_URL" -o "$TMP" 2>/dev/null) || code="curl_error"
  if [ "$code" != "200" ]; then
    echo "aviso: catálogo de modelos não descarregado (HTTP ${code})." >&2
    rm -f "$TMP"
  fi
fi

if [ -f "$TMP" ]; then
  # Google exports with CRLF; the parser only wants lines.
  tr -d '\r' < "$TMP" > "${TMP}.lf" && mv "${TMP}.lf" "$TMP"
  if accept "$TMP"; then
    mv "$TMP" "$DEST"
    echo "catálogo de modelos: $(grep -c '^§\.' "$DEST") secções -> ${DEST}"
  else
    echo "aviso: o catálogo descarregado não tem secções §.Marca.Modelo; ignorado." >&2
    echo "       corpo: $(head -c 200 "$TMP" | tr -d '\0' | tr '\n' ' ')" >&2
    rm -f "$TMP"
  fi
fi
exit 0
