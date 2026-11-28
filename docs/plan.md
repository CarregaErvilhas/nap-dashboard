# Plan

Open work only. Remove an item when it is done.

- **Hubs: places with several sites.** See [Hubs](#hubs) below.
- **PR check coverage.** Run `build_dashboard.py` on fixtures. It needs a versioned sample of the NAP CSVs, which raises the same third-party republication question as `data/tracker_errors.csv` (see `THIRD-PARTY-NOTICES.md`), so it waits for a decision.

## Hubs

No source publishes a place with several sites. Each operator publishes its own sites, and many split one place into one site per charger, so a search for one mall returns a card per charger and misses the sites whose name is only their code. A hub groups them. olh'o'posto and ohmigo read hubs from the model; olh'o'posto's side is in its `Docs/plan.md`.

### Definition

- **A hub is an OpenStreetMap area that holds two or more NAP sites.** The area is one of the kinds in `osm_places.py` `KINDS`, which gains `highway=services` (motorway services) and `amenity=fuel` (as an area, not a node).
- **A site belongs to the place whose outline holds its position.** This is the model's position, so OSM's, with the per-kind margin `osm_places.py` already uses.
- **A site inside two places goes to the higher one in `KINDS` order.** A car park inside a mall goes to the mall. If the sites of that place are spread wider than about 300 m (a campus, an airport), it goes to the next, smaller place instead.
- **A site with no place is in no hub.** Procurar shows the sites next to it as nearby, never as a hub. There is no grouping by distance alone: such a group would have no name and no stable id.
- **Sites under construction (`planned`) inside the place are listed with the hub,** but they don't count toward the two.
- **Id:** `HUB-` plus the OSM element, `HUB-w42645796` for Centro Comercial Colombo (`way/42645796`). Renaming the place keeps the id.
- **Name:** the place's OSM `name` (`name:en` in English, when present). A place with no name shows its kind and the NAP address ("Parque de estacionamento · Avenida Lusíada, Lisboa"), with a link to add the name on OSM. Only the model decides the name; olh'o'posto and ohmigo never edit it.
- **Manual exceptions** go in `assets/hubs_manual.json`, each entry with `source` and `checkedAt` (like ohmigo's `offers/manual.json`). Only two kinds: a name override, and a site to `exclude`. Everything else is fixed on OSM, and only by mapping what exists on the ground: no area is drawn just to group our sites.

### Splitting

- **Fix OSM first:** split the area, or map the smaller places. The next refresh redoes the hubs.
  - Example: at Grândola, OSM maps only the S-N side of the A2 as `highway=services` (`way/208645443`). That side's sites form a hub; the N-S side's don't, until someone maps that side's area. This is the right result, because nobody can cross the motorway.
- **A big place that is right is not split.** A mall with chargers on several floors is one hub, and the hub shows its `zones`. At the Colombo, OSM maps the CapWatt stations with `level=-3`.
- **A site that should not be in the hub:** fix its position on OSM, or add an `exclude` to the manual file.
- **Ids:** the area that remains keeps its id, and new areas get new ids. A hub that disappears is olh'o'posto's to handle (its `Docs/plan.md`).

### Model and pipeline

- **Model:** a top-level `hubs` list, beside `planned`. Each entry is `{id, name, kind, osm: {element}, lat, lon, sites, ops, npts, kw, zones}`, and each site gets `hub` (`sites.json` `hub`).
  - `zones`: the hub's sites grouped by OSM `level`, when the levels differ.
  - Additive, no `SCHEMA` bump. The key is left out when `osm_places.py` did not run, and `[]` means there are none, as with `planned`.
- **`scripts/hubs.py`** runs after `osm_places.py` and before `ohmigo_dataset.py`. It reads the same places cache, which must then keep the outlines and element ids, not only the names.
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
