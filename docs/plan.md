# Plan

Open work only. Remove an item when it is done.

- **Hubs: places with several sites.** See [Hubs](#hubs) below.
- **PR check coverage.** Run `build_dashboard.py` on fixtures. It needs a versioned sample of the NAP CSVs, which raises the same third-party republication question as `data/tracker_errors.csv` (see `THIRD-PARTY-NOTICES.md`), so it waits for a decision.

## Hubs

A hub groups the sites of one place across operators. What a hub is, its id and name, how it splits, and what the readers of the model may rely on are in [Architecture `Docs/hubs.md`](https://github.com/CarregaErvilhas/Architecture/blob/main/Docs/hubs.md), the group's one copy. This repo is the only one that decides the hubs; this section is its part of the work. olh'o'posto's part is in its `Docs/plan.md`.

### Model and pipeline

- **Places:** `osm_places.py` `KINDS` gains `highway=services` and `amenity=fuel` (an area, not a node). Its cache must keep each place's outline and OSM element, not only the name.
- **Manual exceptions:** `assets/hubs_manual.json`, each entry with `source` and `checkedAt`, like ohmigo's `offers/manual.json`. It holds only name overrides and sites to `exclude`.
- **Model:** a top-level `hubs` list, beside `planned`. Each entry is `{id, name, kind, osm: {element}, lat, lon, sites, ops, npts, kw, zones}`, and each site gets `hub` (`sites.json` `hub`).
  - `zones`: the hub's sites grouped by OSM `level`, when the levels differ.
  - Additive, no `SCHEMA` bump. The key is left out when `osm_places.py` did not run, and `[]` means there are none, as with `planned`.
- **`scripts/hubs.py`** applies the definition in Architecture `Docs/hubs.md` to the places cache and the model's positions. It runs after `osm_places.py` and before `ohmigo_dataset.py`.
- **`pipeline_guard.py`** warns when two hubs within 1 km share a name (both sides of one services area).

### Site

- **Procurar:**
  - A "Juntar por hub" filter, on by default, shows one stacked card per hub: a status bar per operator, and its sites behind "Ver os N postos".
  - Search finds a hub by its OSM name. Today, searching for the Colombo misses its two Galp sites, which are named only by their code.
- **Map:** one marker per hub until a close zoom. The number is the hub's sockets and the ring is their status; zooming in opens the hub into its sites.
- **Hub detail:**
  - a table of operators: sites, free sockets, power, the operator fee without VAT, and an hour of charging at that fee;
  - the hourly occupancy of all the hub's sockets, adding up the AmpereArchive per-site files;
  - the sites by operator, the zones, and the hubs and sites nearby.
- **Share page `/hub-<id>.html`,** like `/posto-<id>.html` (`share_pages.py`). Its image shows the week's figures, never the live status, which social networks would cache stale.
- **Rede:** the "Hubs" panel today ranks single sites by total power. Rename it "Maiores postos" and keep "Hubs" for these.
- **Strings:** every new fixed PT string gets its `dashboard_i18n.py` MAP entry.
- **Privacy:** everything above is built from the model and served as static files, so there is no new request. A change to that needs the privacy page.
