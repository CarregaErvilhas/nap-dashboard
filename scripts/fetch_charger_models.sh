#!/usr/bin/env bash
# Fetch the community's catalogue of charger models for hardware_checks.py.
# Run from the repo root:  bash scripts/fetch_charger_models.sh
#
# The catalogue is a Google Doc ("Modelos de Carregadores usados em Portugal")
# that a member of the community keeps: one section per model (`§.Marca.Modelo`)
# with its maximum DC voltage and current (`1000V 200A`). hardware_checks.py
# reads it to know the rated voltage of the charger OSM says is at each site.
#
# Same rules as the PCVE tracker (fetch_tracker.sh): it is someone else's work
# with no reuse licence and this repo is public, so
#   * the URL lives in the CHARGER_MODELS_URL secret, never in the source;
#   * nothing from it is versioned (data/ is gitignored);
#   * a failed fetch never fails the pipeline: hardware_checks.py then runs on
#     OSM's socket voltages alone and errors.md says the catalogue was missing.
#
# CHARGER_MODELS_URL is the Doc's plain-text export,
# https://docs.google.com/document/d/<id>/export?format=txt
# A local copy works too: CHARGER_MODELS_FILE=path/to/export.txt.
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
else
  echo "aviso: sem CHARGER_MODELS_URL nem CHARGER_MODELS_FILE: o item 14 de errors.md" >&2
  echo "       usa só a tensão das tomadas no OSM nesta corrida." >&2
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
