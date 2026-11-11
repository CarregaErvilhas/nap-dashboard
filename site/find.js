// "Procurar posto": search, filters, list of sites with one mark per socket,
// and a canvas map of the same result set. The list is the accessible view;
// the map never holds information the list lacks.
'use strict';
(function () {
  var N = window.NAP, el = N.el, t = N.t;
  N.addStrings({
    findH1: 'Onde carregar, e se está livre agora',
    findLead: 'Todos os postos públicos de Portugal, com o estado que o operador declara, a potência, as tomadas e como se paga.',
    qLabel: 'Localidade, operador, nome ou código do posto', qPh: 'Ex.: Coimbra, Ionity, LSB-00123', near: 'Perto de mim',
    quick: 'Filtros rápidos', fFree: 'Livre agora', fFast: 'Rápido (50 kW ou mais)', fUltra: 'Ultra (150 kW ou mais)',
    fCard: 'Paga com cartão bancário', more: 'Mais filtros', conn: 'Tomada', op: 'Operador', region: 'Região', dcv: 'Tensão DC', any: 'Qualquer', opSearch: 'Procurar operador…', opNone: 'Nenhum operador encontrado.', selN: '{n} selecionados',
    dcv800: 'Para carros 800 V (mais de 500 V)', dcv400: 'Para carros 400 V (até 500 V)', dcvUnk: 'Tensão não declarada',
    dcvHelp: 'Tensão máxima declarada nos conectores DC do posto. Acima de 500 V é onde um carro de 800 V carrega à potência máxima; um carro de 400 V carrega em qualquer um.',
    reset: 'Limpar filtros', view: 'Vista', vList: 'Lista', vMap: 'Mapa', showMore: 'Mostrar mais', mapH: 'Mapa dos postos',
    zIn: 'Aproximar', zOut: 'Afastar', inView: ' na vista do mapa', allRes: 'Mostrar todos os resultados',
    mapDesc: 'O mapa mostra os mesmos postos da lista. Toca num ponto para o abrir na lista; a lista tem toda a informação.',
    count1: '{n} local', countN: '{n} locais', countNear: ', do mais perto para o mais longe', none: 'Nenhum posto com estes filtros. Tira um filtro ou procura outra localidade.',
    upTo: 'até', sockets: 'tomadas', freeOf: '{a} de {n} livres', km: 'a {d} km',
    geoAsk: 'A pedir a tua localização…', geoFail: 'Não foi possível obter a localização. Procura pela localidade.',
    geoNote: 'A localização fica só no teu dispositivo: não é enviada para lado nenhum.',
    dSockets: 'Tomadas', cId: 'Tomada', cPlug: 'Ficha', cKw: 'kW', cState: 'Estado', cKwh: '€/kWh', cMin: '€/min', cFlat: '€/carga',
    feeNote: 'Taxa do operador (OPC), sem IVA. A energia é faturada à parte pelo teu comercializador (CEME).',
    dOp: 'Operador', dCode: 'Código', dPay: 'Pagamento',
    dPayNone: 'sem informação da comunidade', dOsm: 'No OpenStreetMap', dHw: 'Carregador', dHws: 'Carregadores',
    dShared: 'Potência partilhada', sharedTxt: 'até {kw} kW no total por carregador: com outro carro ligado, cada um recebe menos (OpenStreetMap)',
    dOld: 'Código antigo', dWc: 'Cadeira de rodas', wc_yes: 'acessível', wc_limited: 'acesso limitado', wc_no: 'não acessível', dFixme: 'Por confirmar no OpenStreetMap', fixmeTell: '(confirmaste? diz no grupo do Telegram)',
    fWc: 'Acessível em cadeira de rodas', fWcTitle: 'Só os postos que o operador ou a comunidade confirmaram. A maioria não tem esta informação, o que não quer dizer que não seja acessível.', dAccess: 'Acesso', dFee: 'Estacionamento pago',
    dLoc: 'Localização', locWarn: 'O NAP e o OpenStreetMap discordam na localização (a {d} km). Mostramos a do OpenStreetMap.',
    dDoubt: 'Dúvida da comunidade', directions: 'Como chegar', seeOsm: 'Ver no OpenStreetMap', cost: 'Quanto custa carregar aqui (ohmigo)',
    loadingSockets: 'A carregar as tomadas…',
    life: 'Estado do posto', lifeOp: 'Em funcionamento', lifeConstruction: 'Em construção', lifePlanned: 'Planeado',
    lifeHelp: 'Por omissão só aparecem postos em funcionamento. Os postos em construção ou planeados vêm do OpenStreetMap: ainda não estão no NAP, por isso não têm estado, tomadas nem preços.',
    lcNote: 'Este posto ainda não está no NAP: o OpenStreetMap indica-o como {s}. Não há estado das tomadas nem preços, e a localização e a potência são as que a comunidade mapeou.',
    lcName: 'Posto {s}'
  }, {
    findH1: 'Where to charge, and whether it is free now',
    findLead: 'Every public charger in Portugal, with the status the operator declares, power, plugs and how to pay.',
    qLabel: 'Town, operator, name or charger code', qPh: 'E.g. Coimbra, Ionity, LSB-00123', near: 'Near me',
    quick: 'Quick filters', fFree: 'Free now', fFast: 'Fast (50 kW or more)', fUltra: 'Ultra (150 kW or more)',
    fCard: 'Takes bank cards', more: 'More filters', conn: 'Plug', op: 'Operator', region: 'Region', dcv: 'DC voltage', any: 'Any', opSearch: 'Search operators…', opNone: 'No operator found.', selN: '{n} selected',
    dcv800: 'For 800 V cars (over 500 V)', dcv400: 'For 400 V cars (up to 500 V)', dcvUnk: 'Voltage not declared',
    dcvHelp: 'Maximum voltage declared on the site’s DC connectors. Over 500 V is where an 800 V car charges at full power; a 400 V car charges on either.',
    reset: 'Clear filters', view: 'View', vList: 'List', vMap: 'Map', showMore: 'Show more', mapH: 'Charger map',
    zIn: 'Zoom in', zOut: 'Zoom out', inView: ' in the map view', allRes: 'Show all results',
    mapDesc: 'The map shows the same chargers as the list. Tap a dot to open it in the list; the list has all the information.',
    count1: '{n} site', countN: '{n} sites', countNear: ', nearest first', none: 'No chargers match these filters. Remove one or search another town.',
    upTo: 'up to', sockets: 'sockets', freeOf: '{a} of {n} free', km: '{d} km away',
    geoAsk: 'Asking for your location…', geoFail: 'Could not get your location. Search by town instead.',
    geoNote: 'Your location stays on your device: it is not sent anywhere.',
    dSockets: 'Sockets', cId: 'Socket', cPlug: 'Plug', cKw: 'kW', cState: 'Status', cKwh: '€/kWh', cMin: '€/min', cFlat: '€/session',
    feeNote: 'Operator (CPO) fee, without VAT. Energy is billed separately by your supplier (CEME).',
    dOp: 'Operator', dCode: 'Code', dPay: 'Payment',
    dPayNone: 'no community information', dOsm: 'On OpenStreetMap', dHw: 'Charger', dHws: 'Chargers',
    dShared: 'Shared power', sharedTxt: 'up to {kw} kW in total per charger: with another car plugged in, each gets less (OpenStreetMap)',
    dOld: 'Old code', dWc: 'Wheelchair', wc_yes: 'accessible', wc_limited: 'limited access', wc_no: 'not accessible', dFixme: 'To be confirmed on OpenStreetMap', fixmeTell: '(checked it? tell the Telegram group)',
    fWc: 'Wheelchair accessible', fWcTitle: 'Only the chargers the operator or the community confirmed. Most have no information, which does not mean they are not accessible.', dAccess: 'Access', dFee: 'Paid parking',
    dLoc: 'Location', locWarn: 'The NAP and OpenStreetMap disagree on the location ({d} km apart). We show the OpenStreetMap one.',
    dDoubt: 'Community doubt', directions: 'Directions', seeOsm: 'View on OpenStreetMap', cost: 'What charging here costs (ohmigo)',
    loadingSockets: 'Loading sockets…',
    life: 'Charger status', lifeOp: 'In service', lifeConstruction: 'Under construction', lifePlanned: 'Planned',
    lifeHelp: 'By default only chargers in service are listed. Chargers under construction or planned come from OpenStreetMap: they are not in the NAP yet, so they have no status, sockets or prices.',
    lcNote: 'This charger is not in the NAP yet: OpenStreetMap lists it as {s}. There is no socket status or pricing, and the location and power are what the community mapped.',
    lcName: '{s} charger'
  });

  var PAGE = 30;
  var S = [], P = null, bySite = new Map(), outline = null, snapshot = '';
  var F = fresh();
  function fresh() { return { q: '', free: false, fast: false, ultra: false, card: false, wc: false, conn: [], op: [], region: [], dcv: [], life: ['op'] }; }
  var here = null, shown = PAGE, result = [], listed = [], openExt = null, liveRes = null, dirty = false, opGroup = {};
  var $ = function (id) { return document.getElementById(id); };
  var norm = function (s) { return String(s == null ? '' : s).normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase(); };

  // The NAP spells one operator many ways ("Atlante Infra Portugal, S.A" / "... S.A." / "Atlante").
  // Group by name without accents, punctuation and legal suffixes; show the commonest spelling.
  var OP_ALIAS = { atlante: 'atlante infra portugal', 'galp gest': 'galpgeste' };
  function opKey(n) {
    var k = norm(n).replace(/[^a-z0-9]+/g, ' ').replace(/\b(lda|s a|sa|ltd|unipessoal|sociedade)\b/g, ' ').replace(/\s+/g, ' ').trim();
    return (OP_ALIAS[k] || k).replace(/ /g, '');  // "HighGreenPower" = "High Green Power"
  }
  // Words people type for an operator that the NAP name does not contain.
  var OP_WORDS = [['tesla', 'suc supercharger supercharging destination'],
                  ['continente', 'plug charge plugandcharge pnc cnt modelo'],
                  ['galp', 'galpgeste galp power'], ['edp', 'edp comercial'], ['ionity', 'ionity gmbh']];
  function words(q) { return norm(q).replace(/&/g, ' ').split(/[^a-z0-9]+/).filter(function (w) { return w && w !== 'and' && w !== 'e'; }); }
  function lev1(a, b) {  // true when a and b differ by at most one edit
    if (a === b) return true;
    if (Math.abs(a.length - b.length) > 1) return false;
    var i = 0; while (i < a.length && i < b.length && a[i] === b[i]) i++;
    return a.slice(i + 1) === b.slice(i + 1) || a.slice(i) === b.slice(i + 1) || a.slice(i + 1) === b.slice(i);
  }
  function opText(k, label) {
    var x = '';
    OP_WORDS.forEach(function (e) { if (k.indexOf(e[0]) >= 0) x += ' ' + e[1]; });
    return norm(label) + ' ' + x;
  }
  // Every query word must match a word of the text as substring, or (4+ letters) within one typo.
  function opMatch(q, text) {
    var ws = words(q), tw = text.split(/[^a-z0-9]+/).filter(Boolean);
    return ws.every(function (w) {
      return text.indexOf(w) >= 0 || (w.length >= 4 && tw.some(function (x) { return lev1(w, x) || (x.length > w.length && lev1(w, x.slice(0, w.length))); }));
    });
  }
  function dist(a, b) {
    var R = 6371, r = Math.PI / 180, dLat = (b.lat - a.lat) * r, dLon = (b.lon - a.lon) * r;
    var x = Math.sin(dLat / 2) * Math.sin(dLat / 2) + Math.cos(a.lat * r) * Math.cos(b.lat * r) * Math.sin(dLon / 2) * Math.sin(dLon / 2);
    return 2 * R * Math.asin(Math.sqrt(x));
  }
  function pts(s) { return bySite.get(s.ext) || []; }
  function freeCount(s) {
    if (!P) return s.status === 'available' ? 1 : 0;
    return pts(s).filter(function (p) { return p.status === 'available'; }).length;
  }

  function filter() {
    var words = norm(F.q).split(/\s+/).filter(Boolean);
    var wcHelp = document.getElementById('wcHelp');
    if (wcHelp) wcHelp.hidden = !F.wc;
    result = S.filter(function (s) {
      if (F.fast && !(s.kw >= 50)) return false;
      if (F.ultra && !(s.kw >= 150)) return false;
      if (F.card && s.pay.indexOf('Multibanco/contactless') < 0) return false;
      if (F.wc && s.wc !== 'yes' && s.wc !== 'limited') return false;
      if (F.conn.length && !F.conn.some(function (c) { return s.conns.indexOf(c) >= 0; })) return false;
      if (F.op.length && F.op.indexOf(s._g) < 0) return false;
      if (F.region.length && F.region.indexOf(s.region) < 0) return false;
      if (F.dcv.length && !F.dcv.some(function (c) { return (s.dcv || []).indexOf(c) >= 0; })) return false;
      if (F.free && !freeCount(s)) return false;
      if (F.life.length && F.life.indexOf(s.lc || 'op') < 0) return false;
      for (var i = 0; i < words.length; i++) if (s._k.indexOf(words[i]) < 0) return false;
      return true;
    });
    if (here) {
      result.forEach(function (s) { s._d = dist(here, s); });
      result.sort(function (a, b) { return a._d - b._d; });
    } else {
      // A search for a town lists that town first, not sites that merely mention it.
      var w0 = words[0], hit = function (s) { return w0 && norm(s.city).indexOf(w0) === 0 ? 0 : 1; };
      result.sort(function (a, b) {
        return hit(a) - hit(b) || (a.city === b.city ? (b.kw - a.kw) : String(a.city).localeCompare(String(b.city), 'pt'));
      });
    }
    shown = PAGE;
    render();
  }
  // The list follows the map: once the user pans or zooms, only sites inside the view are listed.
  function inView(s) { return s.lon >= view[0] && s.lon <= view[2] && s.lat >= view[1] && s.lat <= view[3]; }
  function byMap() { return dirty && !here; }

  function socketRow(s) {
    var list = pts(s);
    if (s.lc) return el('span', { class: 'st' }, N.status('planned', false), t('life' + (s.lc === 'planned' ? 'Planned' : 'Construction')) + (s.npts ? ' · ' + s.npts + ' ' + t('sockets') : ''));
    if (!P) return el('span', { class: 'st' }, N.status(s.status, false), s.npts + ' ' + t('sockets'));
    var free = freeCount(s);
    var row = el('span', { class: 'sockets', 'aria-hidden': 'true' }, list.slice(0, 24).map(function (p) { return N.status(p.status, false); }));
    return [row, el('b', null, t('freeOf', { a: free, n: list.length }))];
  }
  function card(s) {
    var open = openExt === s.ext, id = 'd-' + s.ext.replace(/[^\w-]/g, '_');
    var name = s.lc && (!s.name || s.name === s.ext) ? t('lcName', { s: t('life' + (s.lc === 'planned' ? 'Planned' : 'Construction')).toLowerCase() }) : (s.name && s.name !== s.ext ? s.name : s.ext);
    var btn = el('button', { type: 'button', 'aria-expanded': String(open), 'aria-controls': id, onclick: function () { toggle(s.ext); } },
      el('span', { class: 'nm' }, name),
      el('span', { class: 'kw' }, s.kw ? N.nf(s.kw) + ' kW' : '—', el('small', null, t('upTo'))),
      el('span', { class: 'where' }, [s.city, s.op].filter(Boolean).join(', '), here && s._d != null ? ' (' + t('km', { d: N.nf(s._d, s._d < 10 ? 1 : 0) }) + ')' : ''),
      el('span', { class: 'line' }, socketRow(s), s.conns.map(function (c) { return el('span', { class: 'tag' }, c); }),
        s.doubt ? el('span', { class: 'tag warn' }, t('dDoubt')) : null,
        s.loc_km ? el('span', { class: 'tag warn' }, t('dLoc')) : null));
    var li = el('li', { class: 'site' + (open ? ' sel' : ''), 'data-ext': s.ext }, btn);
    if (open) li.appendChild(detail(s, id));
    return li;
  }
  function money(v) { return v == null || v === '' ? '—' : N.nf(v, 3); }
  function detail(s, id) {
    var d = el('div', { class: 'detail', id: id });
    var dl = el('dl', null,
      el('dt', null, t('dOp')), el('dd', null, s.op || '—'),
      el('dt', null, t('dCode')), el('dd', null, el('code', null, s.ext)),
      el('dt', null, t('dPay')), el('dd', null, s.lc ? '—' : s.pay.length ? s.pay.map(function (p) { return t('pay_' + p); }).join(', ') : t('dPayNone')));
    if (s.osm_op || s.osm_access || s.osm_fee) {
      N.add(dl, [el('dt', null, t('dOsm')), el('dd', null, [s.osm_op, s.osm_access ? t('dAccess') + ': ' + s.osm_access : null,
        s.osm_fee ? t('dFee') + ': ' + s.osm_fee : null].filter(Boolean).join('; '))]);
    }
    if (s.hw) N.add(dl, [el('dt', null, t(s.hw.length > 1 ? 'dHws' : 'dHw')), el('dd', null, s.hw.join(', ') + ' (OpenStreetMap)')]);
    if (s.shared) N.add(dl, [el('dt', null, t('dShared')), el('dd', null, t('sharedTxt', { kw: N.nf(s.shared) }))]);
    if (s.wc) N.add(dl, [el('dt', null, t('dWc')), el('dd', null, t('wc_' + s.wc))]);
    if (s.old) N.add(dl, [el('dt', null, t('dOld')), el('dd', null, s.old.join(', ') + (s.oldop ? ' (' + s.oldop + ')' : ''))]);
    // Feedback on these goes to the OSM mappers' Telegram group (they asked for it there).
    if (s.fixme) N.add(dl, [el('dt', null, t('dFixme')), el('dd', null, s.fixme.join('; ') + ' ',
      el('a', { href: 'https://t.me/chatpostoscarregamento', rel: 'noopener noreferrer', target: '_blank' }, t('fixmeTell')))]);
    if (s.doubt) N.add(dl, [el('dt', null, t('dDoubt')), el('dd', null, s.doubt)]);
    if (s.loc_km) N.add(dl, [el('dt', null, t('dLoc')), el('dd', null, t('locWarn', { d: N.nf(s.loc_km, s.loc_km < 10 ? 1 : 0) }))]);
    d.appendChild(dl);
    if (s.lc) d.appendChild(el('p', { class: 'muted small' }, t('lcNote', { s: t('life' + (s.lc === 'planned' ? 'Planned' : 'Construction')).toLowerCase() })));
    else if (!P) d.appendChild(el('p', { class: 'muted small' }, t('loadingSockets')));
    else {
      var mobie = false;
      var rows = pts(s).map(function (p) {
        var only = p.regime === 'sem_ceme' && p.nap != null;
        if (p.regime !== 'sem_ceme') mobie = true;
        return el('tr', null, el('td', null, el('code', null, p.point_id)), el('td', { class: 'l' }, String(p.connectors || '—').split('|').join(', ')),
          el('td', null, p.kw ? N.nf(p.kw) : '—'), el('td', { class: 'l' }, N.status(p.status)),
          el('td', null, only ? N.nf(p.nap, 3) : money(p.ENERGY)), el('td', null, money(p.TIME)), el('td', null, money(p.FLAT)));
      });
      d.appendChild(el('div', { class: 'scroll', tabindex: '0', role: 'group', 'aria-label': t('dSockets') },
        el('table', null, el('caption', null, t('dSockets')),
          el('thead', null, el('tr', null, ['cId', 'cPlug', 'cKw', 'cState', 'cKwh', 'cMin', 'cFlat'].map(function (k, i) {
            return el('th', { scope: 'col', class: i === 1 || i === 3 ? 'l' : null }, t(k)); }))),
          el('tbody', null, rows))));
      // The OPC-fee / CEME split only exists on MOBI.E; elsewhere the operator bills directly.
      if (mobie) d.appendChild(el('p', { class: 'small muted' }, t('feeNote')));
    }
    var ll = s.lat + ',' + s.lon;
    d.appendChild(el('div', { class: 'actions' },
      el('a', { class: 'btn primary', href: 'https://www.google.com/maps/dir/?api=1&destination=' + encodeURIComponent(ll), rel: 'noopener noreferrer', target: '_blank' }, t('directions')),
      el('a', { class: 'btn', href: 'https://www.openstreetmap.org/?mlat=' + s.lat + '&mlon=' + s.lon + '#map=18/' + s.lat + '/' + s.lon, rel: 'noopener noreferrer', target: '_blank' }, t('seeOsm')),
      s.lc ? null : el('a', { class: 'btn', href: 'https://ohmigo.ocarroeletrico.com/', rel: 'noopener', target: '_blank' }, t('cost'))));
    return d;
  }
  function toggle(ext, scroll) {
    openExt = openExt === ext ? null : ext;
    if (openExt) {
      var i = listed.findIndex(function (s) { return s.ext === ext; });
      if (i >= shown) shown = i + 1;
    }
    render();
    var li = openExt && document.querySelector('.site[data-ext="' + (window.CSS && CSS.escape ? CSS.escape(openExt) : openExt) + '"]');
    if (li) { var b = li.querySelector('button'); b.focus({ preventScroll: !scroll }); if (scroll) li.scrollIntoView({ block: 'start' }); }
  }
  function render() {
    listed = byMap() ? result.filter(inView) : result;
    var n = listed.length;
    $('count').textContent = n ? t(n === 1 ? 'count1' : 'countN', { n: N.nf(n) }) + (byMap() ? t('inView') : '') + (here ? t('countNear') : '') : t('none');
    $('allRes').hidden = !byMap();
    var ul = N.clear($('sites'));
    listed.slice(0, shown).forEach(function (s) { ul.appendChild(card(s)); });
    $('moreBtn').hidden = shown >= n;
    drawMap();
  }
  var vt;
  function viewMoved() { dirty = true; clearTimeout(vt); vt = setTimeout(function () { shown = PAGE; openExt = openExt && result.some(function (s) { return s.ext === openExt && inView(s); }) ? openExt : null; render(); }, 150); }

  // ---- map ----
  var VIEWS = { mainland: [-9.75, 36.85, -6.0, 42.25], madeira: [-17.4, 32.35, -16.15, 33.2], azores: [-31.5, 36.8, -24.8, 39.85] };
  var view = VIEWS.mainland.slice();
  function colors() {
    var cs = getComputedStyle(document.documentElement), o = {};
    N.STATUSES.forEach(function (s) { o[s] = cs.getPropertyValue('--s-' + s).trim(); });
    o.land = cs.getPropertyValue('--card').trim(); o.line = cs.getPropertyValue('--muted').trim(); o.sel = cs.getPropertyValue('--ink').trim(); o.fg = cs.getPropertyValue('--fg').trim();
    return o;
  }
  function proj(cv) {
    var k = Math.cos(((view[1] + view[3]) / 2) * Math.PI / 180);
    var w = (view[2] - view[0]) * k, h = view[3] - view[1], sc = Math.min(cv.width / w, cv.height / h);
    var ox = (cv.width - w * sc) / 2, oy = (cv.height - h * sc) / 2;
    return { x: function (lon) { return ox + (lon - view[0]) * k * sc; }, y: function (lat) { return oy + (view[3] - lat) * sc; }, sc: sc, k: k };
  }
  function mark(g, x, y, r, st, c) {
    g.fillStyle = c[st] || c.unknown; g.strokeStyle = c[st] || c.unknown; g.beginPath();
    if (st === 'charging') g.rect(x - r, y - r, 2 * r, 2 * r);
    else if (st === 'outOfOrder' || st === 'inoperative') { g.moveTo(x, y - r * 1.2); g.lineTo(x + r * 1.2, y + r); g.lineTo(x - r * 1.2, y + r); g.closePath(); }
    else g.arc(x, y, r, 0, 6.3);
    if (st === 'unknown' || st === 'planned') { g.lineWidth = 2; g.stroke(); } else g.fill();
  }
  // Reference layer: OSM roads and place names from site/data/basemap.json (same origin, loaded
  // only when the map is first drawn). Roads thicken in as you zoom; names are placed greedily so
  // they never overlap, most important first (cities, then towns, villages, suburbs).
  var basemap = null, baseLoading = false;
  var ROAD_AT = [6.5, 3.2, 1.3], ROAD_W = [2.6, 2.1, 1.5];   // [class]: visible below this many degrees of latitude
  var PLACE_AT = [6.5, 2.4, 0.7, 0.22], PLACE_PX = [24, 21, 18, 17];
  function loadBasemap() {
    baseLoading = true;
    N.load('basemap').then(function (b) {
      var roads = b.roads.map(function (r) {
        var f = r[1], x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
        for (var i = 0; i < f.length; i += 2) { x0 = Math.min(x0, f[i]); x1 = Math.max(x1, f[i]); y0 = Math.min(y0, f[i + 1]); y1 = Math.max(y1, f[i + 1]); }
        return { c: r[0], f: f, b: [x0, y0, x1, y1] };
      });
      basemap = { roads: roads, places: b.places }; drawMap();
    }).catch(function () { baseLoading = false; basemap = { roads: [], places: [] }; });
  }
  function drawBase(g, c, p, cv) {
    var span = view[3] - view[1], i;
    g.save(); g.lineCap = 'round'; g.lineJoin = 'round'; g.strokeStyle = c.line; g.globalAlpha = 0.85;
    for (var cl = 2; cl >= 0; cl--) {
      if (span > ROAD_AT[cl]) continue;
      g.lineWidth = ROAD_W[cl]; g.beginPath();
      basemap.roads.forEach(function (r) {
        if (r.c !== cl || r.b[2] < view[0] || r.b[0] > view[2] || r.b[3] < view[1] || r.b[1] > view[3]) return;
        for (var j = 0; j < r.f.length; j += 2) { if (j) g.lineTo(p.x(r.f[j]), p.y(r.f[j + 1])); else g.moveTo(p.x(r.f[0]), p.y(r.f[1])); }
      });
      g.stroke();
    }
    g.restore();
    var fam = getComputedStyle(document.body).fontFamily, placed = [], n = 0;
    g.save(); g.textBaseline = 'middle'; g.lineJoin = 'round'; g.strokeStyle = c.land; g.lineWidth = 5;
    for (i = 0; i < basemap.places.length && n < 140; i++) {
      var q = basemap.places[i], k = q[3];
      if (span > PLACE_AT[k] || q[1] < view[0] || q[1] > view[2] || q[2] < view[1] || q[2] > view[3]) continue;
      var x = p.x(q[1]), y = p.y(q[2]);
      g.font = (k < 2 ? '700 ' : '600 ') + PLACE_PX[k] + 'px ' + fam;
      var w = g.measureText(q[0]).width + 10, h = PLACE_PX[k] + 2, bx = x - 4, by = y - h / 2;
      if (placed.some(function (o) { return bx < o[0] + o[2] && bx + w > o[0] && by < o[1] + o[3] && by + h > o[1]; })) continue;
      placed.push([bx, by, w, h]); n++;
      g.fillStyle = c.fg; g.globalAlpha = 0.75; g.beginPath(); g.arc(x, y, k < 2 ? 3.5 : 2.5, 0, 6.3); g.fill();
      g.globalAlpha = 0.9; g.strokeText(q[0], x + 7, y); g.fillText(q[0], x + 7, y);
    }
    g.restore();
    g.save(); g.font = '600 14px ' + fam; g.textAlign = 'right'; g.textBaseline = 'bottom'; g.fillStyle = c.line; g.strokeStyle = c.land; g.lineWidth = 4; g.lineJoin = 'round';
    g.strokeText('© OpenStreetMap', cv.width - 8, cv.height - 6); g.fillText('© OpenStreetMap', cv.width - 8, cv.height - 6);
    g.restore();
  }
  function drawMap() {
    var cv = $('map');
    if (!cv || $('mapbox').hidden && !window.matchMedia('(min-width: 980px)').matches) return;
    var g = cv.getContext('2d'), c = colors(), p = proj(cv);
    g.clearRect(0, 0, cv.width, cv.height);
    if (outline) {
      g.fillStyle = c.land; g.strokeStyle = c.line; g.lineWidth = 1.5;
      Object.keys(outline).forEach(function (rg) { (outline[rg] || []).forEach(function (ring) {
        g.beginPath(); ring.forEach(function (q, i) { if (i) g.lineTo(p.x(q[0]), p.y(q[1])); else g.moveTo(p.x(q[0]), p.y(q[1])); });
        g.closePath(); g.fill(); g.globalAlpha = 0.4; g.stroke(); g.globalAlpha = 1; }); });
    }
    if (!basemap && !baseLoading) loadBasemap();
    if (basemap) drawBase(g, c, p, cv);
    var r = Math.max(3.5, Math.min(9, p.sc / 260));
    var sel = null;
    result.forEach(function (s) {
      if (s.lon < view[0] || s.lon > view[2] || s.lat < view[1] || s.lat > view[3]) return;
      if (s.ext === openExt) { sel = s; return; }
      mark(g, p.x(s.lon), p.y(s.lat), r, s.status, c);
    });
    if (sel) { g.lineWidth = 4; g.strokeStyle = c.sel; g.beginPath(); g.arc(p.x(sel.lon), p.y(sel.lat), r + 7, 0, 6.3); g.stroke(); mark(g, p.x(sel.lon), p.y(sel.lat), r + 2, sel.status, c); }
    if (here) { g.fillStyle = c.sel; g.beginPath(); g.arc(p.x(here.lon), p.y(here.lat), 7, 0, 6.3); g.fill(); g.lineWidth = 3; g.strokeStyle = c.land; g.stroke(); }
  }
  function zoom(f, cx, cy) {
    var w = view[2] - view[0], h = view[3] - view[1];
    cx = cx == null ? view[0] + w / 2 : cx; cy = cy == null ? view[1] + h / 2 : cy;
    var nw = Math.min(12, Math.max(0.02, w * f)), nh = nw * h / w, rx = (cx - view[0]) / w, ry = (cy - view[1]) / h;
    view = [cx - nw * rx, cy - nh * ry, cx + nw * (1 - rx), cy + nh * (1 - ry)];
    drawMap(); viewMoved();
  }
  function initMap() {
    var cv = $('map'), drag = null, moved = false;
    var at = function (e) { var b = cv.getBoundingClientRect(); return { x: (e.clientX - b.left) * cv.width / b.width, y: (e.clientY - b.top) * cv.height / b.height }; };
    cv.addEventListener('pointerdown', function (e) { drag = at(e); moved = false; cv.setPointerCapture(e.pointerId); });
    cv.addEventListener('pointermove', function (e) {
      if (!drag) return;
      var q = at(e), p = proj(cv), dx = (q.x - drag.x) / (p.sc * p.k), dy = (q.y - drag.y) / p.sc;
      if (Math.abs(q.x - drag.x) + Math.abs(q.y - drag.y) > 6) moved = true;
      view = [view[0] - dx, view[1] + dy, view[2] - dx, view[3] + dy]; drag = q; drawMap();
    });
    cv.addEventListener('pointerup', function (e) {
      var q = at(e), p = proj(cv); drag = null;
      if (moved) { viewMoved(); return; }
      var best = null, bd = 26 * 26;
      result.filter(inView).forEach(function (s) { var dx = p.x(s.lon) - q.x, dy = p.y(s.lat) - q.y, d = dx * dx + dy * dy; if (d < bd) { bd = d; best = s; } });
      if (best) { openExt = null; setView('list'); toggle(best.ext, true); }
    });
    cv.addEventListener('wheel', function (e) {
      e.preventDefault(); var q = at(e), p = proj(cv);
      var lon = view[0] + (q.x - (cv.width - (view[2] - view[0]) * p.k * p.sc) / 2) / (p.k * p.sc), lat = view[3] - (q.y - (cv.height - (view[3] - view[1]) * p.sc) / 2) / p.sc;
      zoom(e.deltaY > 0 ? 1.25 : 0.8, lon, lat);
    }, { passive: false });
    $('zIn').addEventListener('click', function () { zoom(0.6); });
    $('zOut').addEventListener('click', function () { zoom(1.6); });
    document.querySelectorAll('[data-region]').forEach(function (b) { b.addEventListener('click', function () { view = VIEWS[b.getAttribute('data-region')].slice(); drawMap(); viewMoved(); }); });
    new MutationObserver(drawMap).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme', 'data-vision'] });
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', drawMap);
  }
  function setView(v) {
    var map = v === 'map';
    $('mapbox').hidden = !map; $('results').hidden = map;
    $('vMap').setAttribute('aria-pressed', String(map)); $('vList').setAttribute('aria-pressed', String(!map));
    if (map) drawMap();
  }
  function legend() {
    var ul = N.clear($('legend'));
    ['available', 'charging', 'outOfOrder', 'inoperative', 'unknown', 'planned'].forEach(function (s) { ul.appendChild(el('li', null, N.status(s))); });
  }

  // Multi-select: a <details> holding one checkbox per value; F[key] is the list of checked values.
  function multi(id, key, vals, search) {
    var box = $(id), body = box.querySelector('.msbody'), n = box.querySelector('.msn');
    if (search) {
      var si = box.querySelector('.mssearch'), none = box.querySelector('.msnone');
      if (!si) {
        si = el('input', { type: 'search', class: 'mssearch', autocomplete: 'off' });
        none = el('p', { class: 'small muted msnone', hidden: '' });
        body.parentNode.insertBefore(si, body); body.parentNode.appendChild(none);
        si.addEventListener('input', function () {
          var hits = 0;
          Array.prototype.forEach.call(body.children, function (l) {
            var ok = !si.value.trim() || opMatch(si.value, l.getAttribute('data-k')); l.hidden = !ok; if (ok) hits++;
          });
          none.hidden = hits > 0;
        });
      }
      si.setAttribute('placeholder', t('opSearch')); si.setAttribute('aria-label', t('opSearch'));
      none.textContent = t('opNone'); si.value = ''; none.hidden = true;
    }
    var keep = F[key].filter(function (v) { return vals.some(function (x) { return x[0] === v; }); });
    F[key] = keep;
    N.clear(body);
    vals.forEach(function (x) {
      var cb = el('input', { type: 'checkbox', value: x[0] });
      cb.checked = keep.indexOf(x[0]) >= 0;
      cb.addEventListener('change', function () {
        F[key] = Array.prototype.map.call(body.querySelectorAll('input:checked'), function (i) { return i.value; });
        n.textContent = F[key].length ? '(' + t('selN', { n: F[key].length }) + ')' : '';
        filter();
      });
      body.appendChild(el('label', { class: 'chk', 'data-k': search ? opText(x[0], x[1]) : '' }, cb, ' ', x[1]));
    });
    n.textContent = keep.length ? '(' + t('selN', { n: keep.length }) + ')' : '';
  }
  function options() {
    var uniq = function (a) { return Array.from(new Set(a)).filter(Boolean).sort(function (x, y) { return String(x).localeCompare(String(y), 'pt'); }); };
    var pair = function (v) { return [v, v]; };
    multi('fConn', 'conn', uniq([].concat.apply([], S.map(function (s) { return s.conns; }))).map(pair));
    // One entry per operator group; the label is the commonest spelling in the data.
    var cnt = {};
    S.forEach(function (s) { if (!s.op) return; var k = opKey(s.op); s._g = k; (cnt[k] = cnt[k] || {})[s.op] = ((cnt[k] || {})[s.op] || 0) + 1; });
    opGroup = {};
    Object.keys(cnt).forEach(function (k) {
      var names = Object.keys(cnt[k]).sort(function (a, b) { return cnt[k][b] - cnt[k][a] || a.length - b.length; });
      opGroup[k] = names[0].replace(/\s+/g, ' ').trim();
    });
    multi('fOp', 'op', Object.keys(opGroup).sort(function (a, b) { return opGroup[a].localeCompare(opGroup[b], 'pt'); }).map(function (k) { return [k, opGroup[k]]; }), true);
    multi('fRegion', 'region', uniq(S.map(function (s) { return s.region; })).map(function (v) { return [v, t('rg_' + v)]; }));
    multi('fDcv', 'dcv', [['800', t('dcv800')], ['400', t('dcv400')], ['unk', t('dcvUnk')]]);
    multi('fLife', 'life', [['op', t('lifeOp')], ['construction', t('lifeConstruction')], ['planned', t('lifePlanned')]]);
  }

  function init() {
    N.initChrome();
    legend();
    initMap();
    var q0 = new URLSearchParams(location.search).get('q');
    if (q0) { F.q = q0; $('q').value = q0; }
    $('search').addEventListener('submit', function (e) { e.preventDefault(); });
    var timer;
    $('q').addEventListener('input', function () { clearTimeout(timer); timer = setTimeout(function () { F.q = $('q').value; filter(); }, 180); });
    document.querySelectorAll('[data-f]').forEach(function (b) {
      b.addEventListener('click', function () { var k = b.getAttribute('data-f'); F[k] = !F[k]; b.setAttribute('aria-pressed', String(F[k])); filter(); });
    });
    $('allRes').addEventListener('click', function () { dirty = false; shown = PAGE; render(); });
    $('reset').addEventListener('click', function () {
      F = fresh(); here = null; dirty = false; view = VIEWS.mainland.slice();
      $('q').value = ''; options();
      document.querySelectorAll('[data-f]').forEach(function (b) { b.setAttribute('aria-pressed', 'false'); });
      $('near').setAttribute('aria-pressed', 'false'); filter();
    });
    $('near').addEventListener('click', function () {
      if (here) { here = null; $('near').setAttribute('aria-pressed', 'false'); filter(); return; }
      if (!navigator.geolocation) { $('live').textContent = t('geoFail'); return; }
      $('live').textContent = t('geoAsk');
      navigator.geolocation.getCurrentPosition(function (pos) {
        here = { lat: pos.coords.latitude, lon: pos.coords.longitude };
        $('near').setAttribute('aria-pressed', 'true'); $('live').textContent = t('geoNote');
        var w = 0.35; view = [here.lon - w, here.lat - w, here.lon + w, here.lat + w]; filter();
      }, function () { $('live').textContent = t('geoFail'); }, { enableHighAccuracy: false, timeout: 10000, maximumAge: 300000 });
    });
    $('moreBtn').addEventListener('click', function () { shown += PAGE; render(); });
    $('vList').addEventListener('click', function () { setView('list'); });
    $('vMap').addEventListener('click', function () { setView('map'); });
    N.onLang(function () { if (S.length) { options(); legend(); render(); if (P) N.liveNote($('live'), liveRes, snapshot); } });

    N.load('sites').then(function (d) {
      S = d.sites;
      S.forEach(function (s) { s._k = norm([s.name, s.ext, s.city, s.op, s.osm_op].concat(s.hw || [], s.old || []).join(' ')); s._g = s.op ? opKey(s.op) : ''; });
      options(); filter();
      N.load('outline').then(function (o) { outline = o.outline; drawMap(); });
      return Promise.all([N.load('points'), N.load('stats')]);
    }).then(function (r) {
      P = r[0].points; snapshot = r[1].snapshot;
      index();
      render();
      return N.fetchLive(P);
    }).then(function (res) {
      liveRes = res;
      if (res && !res.stale) { index(); S.forEach(siteStatus); filter(); }
      N.liveNote($('live'), res, snapshot);
    }).catch(function () { $('count').textContent = t('loadFail'); $('live').hidden = true; });
  }
  function index() { bySite = new Map(); P.forEach(function (p) { var a = bySite.get(p.site_external_id); if (a) a.push(p); else bySite.set(p.site_external_id, [p]); }); }
  // Same rule as the pipeline: a site shows its most common socket status.
  function siteStatus(s) {
    var m = {}, best = null; pts(s).forEach(function (p) { m[p.status] = (m[p.status] || 0) + 1; });
    for (var k in m) if (best === null || m[k] > m[best]) best = k;
    if (best) s.status = best;
  }
  init();
})();
