# Plan

Open work only. Remove an item when it is done.

- **PR check coverage.** Run `build_dashboard.py` on fixtures. It needs a versioned sample of the NAP CSVs, which raises the same third-party republication question as `data/tracker_errors.csv` (see `THIRD-PARTY-NOTICES.md`), so it waits for a decision.
- **Pre-model `points.json`.** `find.js` still renders it (`ENERGY`/`TIME`/`FLAT` strings; `site_data.POINT_SHAPES` accepts both). Drop that branch once the refresh has rewritten the file in the model shape.
