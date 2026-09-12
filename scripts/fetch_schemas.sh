#!/usr/bin/env bash
# Re-fetch the DATEX II 3.3 XSDs vendored in assets/schemas/ from the official
# source (http://datex2.eu/schema/3/<module>). Run from the repo root:
#   bash scripts/fetch_schemas.sh
# The vendored copies are © CEN / DATEX II (see assets/schemas/README.md and
# THIRD-PARTY-NOTICES.md) — this script exists so nobody has to trust a stale
# copy; it does not change their licence.
set -euo pipefail
mkdir -p assets/schemas
for m in common commonExtension d2Payload energyInfrastructure facilities locationExtension locationReferencing; do
  echo "fetching $m ..."
  curl -fsSL --retry 2 "http://datex2.eu/schema/3/$m" -o "assets/schemas/${m}.xsd.download"
  head -c 100 "assets/schemas/${m}.xsd.download" | grep -q '<?xml' \
    || { echo "erro: $m não é XML; a origem devolveu outra coisa?" >&2; rm -f "assets/schemas/${m}.xsd.download"; exit 1; }
  mv "assets/schemas/${m}.xsd.download" "assets/schemas/${m}.xsd"
done
echo "schemas refreshed:"
ls -lh assets/schemas/*.xsd
