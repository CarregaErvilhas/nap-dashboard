# Plan

Open work only. Remove an item when it is done.

- **Hubs and station areas: grouping sites.** See [Hubs and station areas](#hubs-and-station-areas) below.
- **PR check coverage.** Run `build_dashboard.py` on fixtures. It needs a versioned sample of the NAP CSVs, which raises the same third-party republication question as `data/tracker_errors.csv` (see `THIRD-PARTY-NOTICES.md`), so it waits for a decision.

## Hubs and station areas

Sites are grouped in two levels: the **station area** (the OpenStreetMap `amenity=charging_station` area around one operator's chargers, id `EST-w…`) and the **hub** (a place with several station areas or sites, id `HUB-w…`). What each level is, how its members and name are found, how a grouping is fixed, and what the readers of the model may rely on are in [Architecture `Docs/hubs.md`](https://github.com/CarregaErvilhas/Architecture/blob/main/Docs/hubs.md), the group's one copy. This repo is the only one that decides both levels, and this section is its part of the work. olh'o'posto's part is in its `Docs/plan.md`.

### Model and pipeline

- **Station areas:** `scripts/hubs.py` reads the `amenity=charging_station` ways and their nodes from the `Todos.json` that `osm_umap.py` already fetches (`data/umap_cache/todos.json`). It finds each area's members two ways, by its `ref` list and by the `man_made=charge_point` nodes inside its outline. The outline test reuses `osm_places.py`'s point-in-polygon, so there is no new dependency.
- **Disagreements:** a code in an area's `ref` with no node inside, or a node inside missing from the `ref`, goes to `data/station_area_findings.md`. That file is appended to `errors.md` like the other findings, as a new item for the OpenStreetMap community, and it needs an entry in `DATA_FILES` (`ci_paths.py`).
- **Places:** `osm_places.py` `KINDS` gains `highway=services` and `amenity=fuel` (an area, not a node). Its cache must keep each place's outline and OSM element, not only the name.
- **Hubs:** `scripts/hubs.py` tests each station area's centre, and each site in no station area, against the place outlines. A place with two or more of those units is a hub.
- **Manual exceptions:** `assets/hubs_manual.json`, each entry with `source` and `checkedAt`, like ohmigo's `offers/manual.json`. It holds only name overrides and sites to `exclude`.
- **Model:**
  - a top-level `stationAreas` list, each `{id, name, osm: {element}, ops, sites, stalls, level, hub}`. `stalls` are the chargers inside the area with no NAP code, such as Tesla bays or a Continente charger not yet in the NAP;
  - a top-level `hubs` list beside `planned`, each `{id, name, kind, osm: {element}, lat, lon, stationAreas, sites, ops, npts, kw}`;
  - on each site, `stationArea` and `hub` (`sites.json` `sa` and `hub`).

  Additive, so no `SCHEMA` bump. A key is left out when its input did not run, and `[]` means there are none, as with `planned`.
- **Order:** `scripts/hubs.py` runs after `osm_umap.py` and `osm_places.py`, and before `ohmigo_dataset.py`.
- **`pipeline_guard.py`** warns when two hubs within 1 km share a name.

### Site

- **Procurar:** a "Juntar por local" filter, on by default. Each result is the site's location: its hub, else its station area, else the site.
  - A hub card has a status bar per zone. A station area card has one status bar.
  - The sites are behind "Ver os N postos".
  - Search finds a location by its name. Today, searching for the Colombo misses its two Galp sites, which are named only by their code.
- **Map:** one marker per location until a close zoom. The number is the location's sockets and the ring is their status; zooming in opens it into its sites.
- **Location detail:** one view for both levels:
  - a table of operators: sites, free sockets, power, the operator fee without VAT, and an hour of charging at that fee;
  - the hourly occupancy of all the location's sockets, adding up the AmpereArchive per-site files;
  - the zones and sites, any stalls not in the NAP, and the locations and sites nearby.
- **Share page `/local-<id>.html`** for `HUB-…` and `EST-…`, like `/posto-<id>.html` (`share_pages.py`). Its image shows the week's figures, never the live status, which social networks would cache stale.
- **Rede:** the "Hubs" panel today ranks single sites by total power. Rename it "Maiores postos" and keep "Hubs" for these.
- **Strings:** every new fixed PT string gets its `dashboard_i18n.py` MAP entry.
- **Privacy:** everything above is built from the model and served as static files, so there is no new request. A change to that needs the privacy page.
