# Gotchas (all verified against the 2026-08-16 snapshot)

## Joining NAP ↔ MOBI.E

- **Join key**: `site_external_id` (= MOBI.E `ID`) + last segment of `point_id`
  (the tomada/plug, **int-normalized**: strip leading zeros). This matches
  18 923 / 20 521 points (92.2%).
- **Do NOT join on `point_external_id`.** Its format `PT*op*[E]*reg*num*tom` is
  unreliable: the region part sometimes has a glued `E` prefix (`ELSB` vs MOBI.E
  `LSB`), and the segment count varies (3–7). Parse `site_external_id` directly.
- MOBI.E `UID_TOMADA` comes in several formats (`PT-EDP-EABF-00009-1-1`,
  `PT-*…`, bare numerics). `mobie_join.py` takes the second-to-last `-`-segment
  then int-normalizes. 733 `UID_TOMADA` values are bare numeric ids (`97`, `98`).
- The tariff has multiple rows per (site, plug): keep the `REGULAR` tariff type
  when present, else any; pivot `FLAT/ENERGY/TIME/PARKING_TIME` to wide.
- MOBI.E OPC tariffs are the **station-usage fee, not the energy price**:
  `ENERGY` (€/kWh) is the usage component indexed on energy — the energy itself
  is billed by the driver's CEME. Only ad-hoc / off-MOBI.E OPCs charge the final
  all-in price. Never label `ENERGY` means as "energy price" in UI text.

## NAP static XML quirks

- `brands_accepted` is the **global CEME list per point**, NOT an operator
  discriminator. Don't use it to attribute operators.
- `facilityLocation` (address, postcode, city) lives in the
  **`locationReferencing`** namespace, not `locationExtension`.
- NUTS is **level-1 only** (`nuts1Code`); `nuts2Code`/`nuts3Code` never appear.
- One point can appear with several connectors — aggregate to point level with
  `max(max_power_w)` and a `|`-joined connector set.
- Coordinates: mainland `lon∈(-9.8,-5.5) lat∈(36.5,42.5)`, Açores
  `lon∈(-32,-24) lat∈(36.5,40)`, Madeira `lon∈(-17.5,-16) lat∈(32,33.5)`. All
  sites pass these bounds; city↔coords was not spot-checked (needs reverse
  geocoding).
- Read the XMLs with `lxml.etree.iterparse(…, huge_tree=True)` streaming — they
  don't fit in memory as DOM.

## Dynamic (evActualStatus) quirks

- Dynamic and static point ids match 100%. But **46 points appear 2–3×** in the
  dynamic feed with conflicting states (48 extra rows) — dedupe with
  `keep='first'` and note the conflict in errors.
- `pricePerChargingTime` can reach 3.00 €/min (4 points >1.0 €/min) — likely a
  €/min vs €/h unit error.

## Quality findings (reportable)

- 30% of connector rows (6 206/20 624) have declared `max_power_w` inconsistent
  with `voltage × current` (>25% off). Of these, 2 690 declare power **above**
  the electrical capability (impossible, e.g. 1200 V × 600 A = 720 kW declared as
  200 kW). Suspicious raw values: 1200 V, 3600 V, 600 A.
  For `mode3AC3p` the physical power is `√3 × V × I`; single-phase `V × I`.
- NAP↔MOBI.E power agreement is 99.8% — only 29/18 923 points diverge >30%.
- MOBI.E PartyID (2022): 38 active tariff codes missing from the PDF, 22 codes in
  the PDF unused. Post-2022 operators (ATL, ZUN, SLX, KLS, WEN, …) are absent.
- 227 points (1%) have no `usage_type`.
- 3 013 points (15%) marked `removed` in the dynamic feed are still listed in the
  static inventory.
- Operator names are fragmented (Galp Power/Galpgeste/Galp Gest; 6 Atlante
  variants; 3 Iberdrola; REPSOL case variants) — normalize before aggregating.

## Dashboard build

- `build_dashboard.py` injects data into `assets/dashboard_template.html` at the
  `/*__DATA__*/` marker via
  `json.dumps(clean(data), ensure_ascii=False, allow_nan=False)`.
- **Must** sanitize NaN/Inf floats → null before dumping; bare `NaN` breaks the
  browser's `JSON.parse` (historical bug, now fixed by the `clean()` helper).
- Validate after rebuilding: `json.loads` the extracted `const D = (.*?);` JSON,
  and `node --check` on the extracted `<script>` block.
- Dashboard must open via `file://` with no external libs (pure CSS/JS).
- Historical JS bugs to watch: reference to a non-existent element id `status`;
  `label()` using an undefined `max` instead of the local `m`. If charts are
  blank below the KPIs, suspect a runtime error and eval the script with a DOM
  stub in node.
## Operator identity (`operator_id` is not an OPC key)

- **Never group by NAP `operator_id` alone.** 21 ids carry more than one
  `operator_name` (3448 sites; `ATLA` alone has 7 spellings over 598 sites) and
  3 operators publish under the registry's `PartyCode` instead of its `PartyId`
  (`BBGE`, `CIRC`, `CONT`).
- **`CONT` is a genuine mis-attribution**: NAP publishes 450 sites as "Modelo
  Continente Hipermercados, S.A." — the acquirer — while the CPO is `CNT`
  "Continente Plug & Charge". This is also why asset matching needs both
  `CNT-0002PL0012` and `0002PL0012`: the prefix comes and goes.
- The authoritative `PartyId | PartyCode | name` table comes from the PCVE error
  tracker (`data/opc_registry_authority.csv`, via `scripts/tracker_sync.py`).
  `scripts/tracker_checks.py` resolves an operator by `operator_name`
  (exact, then containment for legal-form variants like "Acciona Recarga
  Portugal" vs "ACCIONA RECARGA PORTUGAL,UNIPESSOAL LDA") — so an operator that
  renames itself drops out until the tracker catches up. That is a limitation of
  the source, not a bug to paper over with fuzzy matching.
- The MOBI.E PartyID PDF (`scripts/partyid_crossref.py`) is **2022**; the tracker
  is the only current source.

## PCVE error tracker (`pt-pcve-errors.xlsx`)

- It is an **Office file, not a native Google Sheet**: the Sheets API and
  `/export?format=xlsx` both fail with
  `400 failedPrecondition: must not be an Office file`. Use
  `drive.google.com/uc?export=download?id=…`.
- `Error List`: header on **row 15**, data from **row 16**, columns **B..K**.
  Column B (`CPO`) is a `VLOOKUP` against the `CPO` tab, so an openpyxl rewrite
  keeps the formula but loses the cached value — Excel/Sheets recalculate.
- The `Error Stats` / `Error details` tabs are pivot tables with **no cached
  values**: they read as empty until refreshed in Excel/Sheets.
- The declared error-type vocabulary has 11 entries but only 10 are used —
  `AFIR compliant` has zero rows. A few `DOUBT` rows have no `Error type` at
  all (the text went into `Notes`), so any filter on that column silently drops
  them.
- Use it as a **labelled set**: it pairs each real defect with the value the
  owner considers correct. That is what makes an anomaly rule non-speculative —
  e.g. 171 rows of `750 V → 500 V` justify the placeholder-voltage check, and
  199 rows of `mode3AC3p → mode2AC1p` justify the three-phase check.
- What it refutes: **pricing is not a useful outlier source**. `min_fee` spans
  0–3,0 with no absurd values since the `97,561 €/min` class was fixed, so a
  global band yields zero findings, and a per-operator band (>10× the operator
  median) yields >1300 false positives. `min_fee = 0` covers 46% of pricing
  rows and is **not** an anomaly.
