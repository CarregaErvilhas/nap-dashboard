# DATEX II 3.3 XSDs (vendored copies)

Source: `http://datex2.eu/schema/3/<module>` (DATEX II documentation portal,
`https://datex2.eu/` / `https://docs.datex2.eu/`).

Files: `common.xsd`, `commonExtension.xsd`, `d2Payload.xsd`,
`energyInfrastructure.xsd`, `facilities.xsd`, `locationExtension.xsd`,
`locationReferencing.xsd` (DATEX II 3.3, CEN 16157 series).

Licence: **© CEN / DATEX II organisation — NOT covered by this repo's
PolyForm-Noncommercial licence** (see `THIRD-PARTY-NOTICES.md`). They are
freely usable to implement/validate a DATEX II exchange; they are vendored
here only as the enum source for `scripts/check_quality.py`,
`scripts/extract_enums.py` and `scripts/anomalias_summary.py`.

To re-fetch instead of trusting the vendored copies:

```bash
bash scripts/fetch_schemas.sh
```
