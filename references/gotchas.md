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