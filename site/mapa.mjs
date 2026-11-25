// "Mapa detalhado": the streets around the sites, on demand. Procurar's canvas
// map stays the light default; this module and MapLibre (~1.7 MB) load only
// when someone presses the button. The basemap is a Portugal extract of the
// Protomaps OSM build on our own R2 (maptiles.ocarroeletrico.com, refreshed
// monthly by basemap-tiles.yml): current.json names the dated .pmtiles file,
// so a new month never mixes with ranges of the old one in a cache.
// Glyphs and sprites live next to it. Nothing here talks to a third party.

const BASE = 'https://maptiles.ocarroeletrico.com';
const VENDOR = new URL('./vendor/', import.meta.url).href;
const ATTRIBUTION = '<a href="https://www.openstreetmap.org/copyright">© OpenStreetMap</a> · <a href="https://protomaps.com">Protomaps</a>';

let ready = null;
function loadScript(src) {
  return new Promise((ok, ko) => {
    const s = document.createElement('script');
    s.src = src; s.onload = ok; s.onerror = () => ko(new Error('script ' + src));
    document.head.appendChild(s);
  });
}
function loadCss(href) {
  if (document.querySelector('link[data-maplibre]')) return;
  const l = document.createElement('link');
  l.rel = 'stylesheet'; l.href = href; l.setAttribute('data-maplibre', '');
  document.head.appendChild(l);
}
// MapLibre, the PMTiles reader and the style generator, once per page.
function libs() {
  if (!ready) {
    loadCss(VENDOR + 'maplibre/maplibre-gl.css');
    ready = Promise.all([
      import(VENDOR + 'maplibre/maplibre-gl.mjs'),
      import(VENDOR + 'basemaps/basemaps.mjs'),
      loadScript(VENDOR + 'pmtiles/pmtiles.js'),
      fetch(BASE + '/current.json', { credentials: 'omit', cache: 'no-store' }).then((r) => {
        if (!r.ok) throw new Error('current.json ' + r.status);
        return r.json();
      }),
    ]).then(([ml, bm, , cur]) => {
      if (!/^[\w.-]+\.pmtiles$/.test(cur && cur.pmtiles || '')) throw new Error('current.json');
      const maplibregl = ml.default || ml;
      const protocol = new window.pmtiles.Protocol();
      maplibregl.addProtocol('pmtiles', protocol.tile);
      return { maplibregl, bm, url: 'pmtiles://' + BASE + '/' + cur.pmtiles };
    });
    ready.catch(() => { ready = null; });  // a failed load can be retried
  }
  return ready;
}

function style(bm, url, lang, dark) {
  const flavor = dark ? 'dark' : 'light';
  return {
    version: 8,
    glyphs: BASE + '/fonts/{fontstack}/{range}.pbf',
    sprite: BASE + '/sprites/v4/' + flavor,
    sources: { protomaps: { type: 'vector', url, attribution: ATTRIBUTION } },
    layers: bm.layers('protomaps', bm.namedFlavor(flavor), { lang }),
  };
}

function features(sites, statusOf) {
  return {
    type: 'FeatureCollection',
    features: sites.map((s) => ({
      type: 'Feature',
      geometry: { type: 'Point', coordinates: [s.lon, s.lat] },
      properties: { ext: s.ext, st: statusOf(s) },
    })),
  };
}

// opts: box (element), bounds [w, s, e, n] or center + zoom, lang, dark,
// sites, statusOf(site), statuses (icon ids), icon(status, px) -> ImageData,
// selected (ext), here ({lon, lat}), onPick(ext), onMove([w, s, e, n]).
export async function open(opts) {
  const { maplibregl, bm, url } = await libs();
  const map = new maplibregl.Map({
    container: opts.box,
    style: style(bm, url, opts.lang, opts.dark),
    bounds: opts.bounds, center: opts.center, zoom: opts.zoom,
    maxBounds: [[-33, 29], [-4.5, 43.5]],
    minZoom: 5, maxZoom: 19,
    attributionControl: { compact: true },
    dragRotate: false, pitchWithRotate: false, touchPitch: false,
  });
  map.touchZoomRotate.disableRotation();
  map.keyboard.enable();
  let sites = opts.sites, selected = opts.selected, here = opts.here;
  const px = Math.max(1, Math.round(window.devicePixelRatio || 1));

  // The sites go on top of whatever basemap style is loaded: on the first
  // load and again after a theme switch, which replaces the whole style.
  map.on('style.load', () => {
    opts.statuses.forEach((st) => { if (!map.hasImage('st-' + st)) map.addImage('st-' + st, opts.icon(st, 22 * px), { pixelRatio: px }); });
    map.addSource('sites', { type: 'geojson', data: features(sites, opts.statusOf) });
    map.addSource('sel', { type: 'geojson', data: point(selectedSite()) });
    map.addSource('here', { type: 'geojson', data: point(here) });
    map.addLayer({ id: 'sel', type: 'circle', source: 'sel',
      paint: { 'circle-radius': 16, 'circle-color': 'rgba(0,0,0,0)', 'circle-stroke-width': 4, 'circle-stroke-color': opts.ink } });
    map.addLayer({ id: 'sites', type: 'symbol', source: 'sites',
      layout: { 'icon-image': ['concat', 'st-', ['get', 'st']], 'icon-allow-overlap': true, 'icon-ignore-placement': true,
        'icon-size': ['interpolate', ['linear'], ['zoom'], 6, 0.5, 12, 0.8, 16, 1] } });
    map.addLayer({ id: 'here', type: 'circle', source: 'here',
      paint: { 'circle-radius': 7, 'circle-color': opts.ink, 'circle-stroke-width': 3, 'circle-stroke-color': '#fff' } });
  });
  map.on('click', 'sites', (e) => { const f = e.features && e.features[0]; if (f) opts.onPick(f.properties.ext); });
  map.on('mouseenter', 'sites', () => { map.getCanvas().style.cursor = 'pointer'; });
  map.on('mouseleave', 'sites', () => { map.getCanvas().style.cursor = ''; });
  map.on('moveend', () => {
    const b = map.getBounds();
    opts.onMove([b.getWest(), b.getSouth(), b.getEast(), b.getNorth()]);
  });

  function selectedSite() { return sites.find((s) => s.ext === selected) || null; }
  function point(p) {
    return { type: 'FeatureCollection', features: p ? [{ type: 'Feature', geometry: { type: 'Point', coordinates: [p.lon, p.lat] }, properties: {} }] : [] };
  }
  function set(id, data) { const src = map.getSource(id); if (src) src.setData(data); }

  return {
    update(next) {
      sites = next.sites; selected = next.selected; here = next.here;
      set('sites', features(sites, opts.statusOf)); set('sel', point(selectedSite())); set('here', point(here));
    },
    fit(bounds) { map.fitBounds(bounds, { duration: 0 }); },
    fly(center, zoom) { map.jumpTo({ center, zoom: Math.max(map.getZoom(), zoom) }); },
    zoomBy(d) { if (d > 0) map.zoomIn(); else map.zoomOut(); },
    bounds() { const b = map.getBounds(); return [b.getWest(), b.getSouth(), b.getEast(), b.getNorth()]; },
    theme(dark, lang) { map.setStyle(style(bm, url, lang, dark), { diff: false }); },
    resize() { map.resize(); },
    remove() { map.remove(); },
  };
}
