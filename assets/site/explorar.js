// "Explorar a rede": cross-filters over every socket. Each list is both a chart
// and a filter; a list ignores its own filter, so you can always widen it.
// All text from data goes in through N.el (text nodes); charts are SVG built
// with createElementNS, never markup strings.
'use strict';
(function () {
  var N = window.NAP, el = N.el, t = N.t;
  N.addStrings({
    xH1: 'Explorar a rede', xLead: 'Escolhe um operador, um concelho ou uma potência: todos os números, o mapa e as tendências passam a falar só dessa parte da rede.',
    xMetric: 'Medir por', xActive: 'Filtros ativos', xReset: 'Limpar filtros', xSum: 'A tua seleção', xStatus: 'Estado das tomadas agora',
    xDims: 'Reparte e filtra', xDimsNote: 'Carrega numa linha para ficar só com ela. Podes juntar várias, na mesma lista ou em listas diferentes.',
    xMap: 'Onde ficam', xMapAria: 'Mapa dos locais da seleção', xSites: 'Maiores locais da seleção', xFee: 'Quanto cobra o operador',
    xFeeNote: 'Taxa do operador (OPC) por kWh, sem IVA, nas tomadas da seleção que a têm. A energia é cobrada à parte pelo teu comercializador (CEME).',
    xTrend: 'Ao longo do tempo', xTSize: 'Tomadas publicadas, dia a dia', xTDown: 'Fora de serviço, dia a dia (%)', xTOcc: 'Ocupação hora a hora (%)',
    xTHeat: 'Ocupação por dia da semana e hora (%)',
    xSrc: 'Estados declarados pelos operadores ao NAP (IMT / MOBI.E), guardados pelo AmpereArchive. Não são medições.',
    m_n: 'Tomadas', m_sites: 'Locais', m_kw: 'Potência', m_occ: 'Ocupação', m_down: 'Fora de serviço', m_fee: 'Taxa por kWh',
    d_op: 'Operador', d_city: 'Concelho', d_pw: 'Potência', d_conn: 'Ficha', d_region: 'Região', d_status: 'Estado', d_regime: 'Preço', d_pay: 'Pagamento',
    xFind: 'Procurar em {d}', xAll: 'Mostrar todos ({n})', xLess: 'Mostrar menos', xNone: 'Sem informação', xNoMatch: 'Nada com esse nome.',
    xr_mobie: 'MOBI.E, com taxa publicada', xr_mobie_sem_tarifa: 'MOBI.E, sem taxa publicada', xr_sem_ceme: 'Fora da MOBI.E (preço único)',
    xSelAll: 'A rede toda: {n} tomadas.', xSelSome: '{n} tomadas de {m} ({p} % da rede).', xSelZero: 'Nenhuma tomada com estes filtros. Tira um deles.',
    xRemove: 'Tirar o filtro {v}', k_n: 'Tomadas', k_sites: 'Locais', k_kw: 'Potência instalada', k_free: 'Livres agora', k_chg: 'A carregar agora', k_down: 'Fora de serviço',
    ks_share: '{p} % da rede', ks_persite: '{v} por local', ks_kw: 'média de {v} kW por tomada', ks_pct: '{p} % das tomadas', ks_occ: 'ocupação de {p} %',
    xFew: 'poucas tomadas', sName: 'Local', sCity: 'Concelho', sN: 'Tomadas', sKw: 'kW', sFree: 'Livres',
    xMapNote: '{n} locais no mapa.', xMapIsl: ' Mais {n} nas ilhas ou fora do mapa.', xOpenFind: 'Abrir {v} em Procurar',
    feeN: '{n} tomadas com taxa por kWh. Mediana: {m} €/kWh.', feeNone: 'Nenhuma tomada da seleção tem taxa por kWh publicada.', feeBin: '{a} a {b} €/kWh: {n} tomadas',
    feeAxis: '€/kWh', xTrendBase: 'Estas séries seguem os filtros de operador, potência e região. Até 8 de novembro há uma leitura por dia, de recolhas mais antigas e menos completas; a partir daí a recolha é contínua.', xTrendIgn: ' Os outros filtros ativos ({f}) não se aplicam aqui.',
    xTrendHour: ' A ocupação hora a hora não segue a região.', xNoHist: 'Sem histórico para esta seleção.',
    tipN: '{d}: {v} tomadas', tipPct: '{d}: {v} %', heatNote: 'Hora de Lisboa. {d} dias de recolha: com menos de 14, lê isto como uma primeira impressão. Cor mais forte é mais ocupado; o máximo é {m} %.',
    heatCell: '{w}, {h} h: {v} %', wd0: 'Segunda', wd1: 'Terça', wd2: 'Quarta', wd3: 'Quinta', wd4: 'Sexta', wd5: 'Sábado', wd6: 'Domingo', xHour: 'Hora', xDay: 'Dia',
    xTable: 'Ver como tabela', xVal: 'Valor'
  }, {
    xH1: 'Explore the network', xLead: 'Pick an operator, a municipality or a power class: every number, the map and the trends then describe only that part of the network.',
    xMetric: 'Measure by', xActive: 'Active filters', xReset: 'Clear filters', xSum: 'Your selection', xStatus: 'Socket status right now',
    xDims: 'Break down and filter', xDimsNote: 'Press a row to keep only that one. You can combine several, in the same list or across lists.',
    xMap: 'Where they are', xMapAria: 'Map of the sites in the selection', xSites: 'Largest sites in the selection', xFee: 'What the operator charges',
    xFeeNote: 'Operator (CPO) fee per kWh, without VAT, for the sockets in the selection that have one. Energy is billed separately by your supplier (CEME).',
    xTrend: 'Over time', xTSize: 'Published sockets, day by day', xTDown: 'Out of service, day by day (%)', xTOcc: 'Occupancy hour by hour (%)',
    xTHeat: 'Occupancy by weekday and hour (%)',
    xSrc: 'Statuses declared by operators to the NAP (IMT / MOBI.E), kept by the AmpereArchive. They are not measurements.',
    m_n: 'Sockets', m_sites: 'Sites', m_kw: 'Power', m_occ: 'Occupancy', m_down: 'Out of service', m_fee: 'Fee per kWh',
    d_op: 'Operator', d_city: 'Municipality', d_pw: 'Power', d_conn: 'Plug', d_region: 'Region', d_status: 'Status', d_regime: 'Price', d_pay: 'Payment',
    xFind: 'Search in {d}', xAll: 'Show all ({n})', xLess: 'Show fewer', xNone: 'No information', xNoMatch: 'Nothing with that name.',
    xr_mobie: 'MOBI.E, fee published', xr_mobie_sem_tarifa: 'MOBI.E, no fee published', xr_sem_ceme: 'Outside MOBI.E (single price)',
    xSelAll: 'The whole network: {n} sockets.', xSelSome: '{n} sockets of {m} ({p}% of the network).', xSelZero: 'No sockets match these filters. Remove one.',
    xRemove: 'Remove the filter {v}', k_n: 'Sockets', k_sites: 'Sites', k_kw: 'Installed power', k_free: 'Free now', k_chg: 'Charging now', k_down: 'Out of service',
    ks_share: '{p}% of the network', ks_persite: '{v} per site', ks_kw: 'mean of {v} kW per socket', ks_pct: '{p}% of sockets', ks_occ: 'occupancy of {p}%',
    xFew: 'few sockets', sName: 'Site', sCity: 'Municipality', sN: 'Sockets', sKw: 'kW', sFree: 'Free',
    xMapNote: '{n} sites on the map.', xMapIsl: ' {n} more on the islands or off the map.', xOpenFind: 'Open {v} in Find',
    feeN: '{n} sockets with a fee per kWh. Median: {m} €/kWh.', feeNone: 'No socket in the selection has a published fee per kWh.', feeBin: '{a} to {b} €/kWh: {n} sockets',
    feeAxis: '€/kWh', xTrendBase: 'These series follow the operator, power and region filters. Until 8 November there is one reading a day, from older and less complete collections; from then on collection is continuous.', xTrendIgn: ' The other active filters ({f}) do not apply here.',
    xTrendHour: ' Hour-by-hour occupancy does not follow the region.', xNoHist: 'No history for this selection.',
    tipN: '{d}: {v} sockets', tipPct: '{d}: {v}%', heatNote: 'Lisbon time. {d} days collected: with fewer than 14, read this as a first impression. A stronger colour is busier; the maximum is {m}%.',
    heatCell: '{w}, {h}h: {v}%', wd0: 'Monday', wd1: 'Tuesday', wd2: 'Wednesday', wd3: 'Thursday', wd4: 'Friday', wd5: 'Saturday', wd6: 'Sunday', xHour: 'Hour', xDay: 'Day',
    xTable: 'View as a table', xVal: 'Value'
  });

  var $ = function (id) { return document.getElementById(id); };
  var SVG = 'http://www.w3.org/2000/svg';
  function sv(tag, attrs) {
    var n = document.createElementNS(SVG, tag), k, i;
    if (attrs) for (k in attrs) if (attrs[k] != null) n.setAttribute(k, attrs[k]);
    for (i = 2; i < arguments.length; i++) N.add(n, arguments[i]);
    return n;
  }

  var DIMS = ['op', 'city', 'pw', 'conn', 'region', 'regime', 'pay', 'status'];
  var CARDS = ['op', 'city', 'pw', 'conn', 'region', 'regime', 'pay'];   // status has its own strip
  var LONG = { op: 1, city: 1 }, MULTI = { conn: 1, pay: 1 };
  var FIXED = { pw: N.PW, status: N.STATUSES, region: ['mainland', 'madeira', 'azores', 'OUTSIDE'], regime: ['mobie', 'mobie_sem_tarifa', 'sem_ceme'] };
  var METRICS = ['n', 'sites', 'kw', 'occ', 'down', 'fee'];
  var RATIO = { occ: 1, down: 1, fee: 1 }, MIN_N = 10, TOP = 10;
  var P = [], V = {}, F = {}, metric = 'n', A = null, liveRes = null, snapshot = '';
  var siteInfo = new Map(), outline = null, H = null, open = {}, query = {};
  DIMS.forEach(function (d) { F[d] = new Set(); V[d] = []; });

  // ---------------------------------------------------------------- data
  function prep(points) {
    P = points;
    P.forEach(function (p, i) {
      V.op[i] = [p.operator_name || '_'];
      V.city[i] = [p.city || '_'];
      V.pw[i] = [p.pw_class || '_'];
      V.conn[i] = p.connectors ? String(p.connectors).split('|') : ['_'];
      V.region[i] = [p.region || '_'];
      V.regime[i] = [p.regime || '_'];
      V.pay[i] = p.pay && p.pay.length ? p.pay : ['_'];
      var f = p.fees && p.fees.REGULAR, e = f && f.energy;
      p._fee = e && e.length && typeof e[0] === 'number' ? e[0] : null;
    });
  }
  function label(d, v) {
    if (v === '_') return t('xNone');
    if (d === 'pw') return N.pwLabel(v);
    if (d === 'region') return t('rg_' + v);
    if (d === 'status') return t('st_' + v);
    if (d === 'regime') return t('xr_' + v);
    if (d === 'pay') return t('pay_' + v);
    if (d === 'conn' && v === 'MCS') return 'MCS (' + t('mcsHeavy') + ')';
    return v;
  }
  function acc() { return { n: 0, kw: 0, chg: 0, act: 0, down: 0, feeS: 0, feeN: 0, sites: new Set() }; }
  function put(a, p) {
    a.n++; a.kw += p.kw || 0; a.sites.add(p.site_external_id);
    if (p.status === 'charging') { a.chg++; a.act++; } else if (p.status === 'available') a.act++;
    else if (p.status === 'outOfOrder' || p.status === 'inoperative') a.down++;
    if (p._fee != null) { a.feeS += p._fee; a.feeN++; }
  }
  function val(a, m) {
    if (!a) return null;
    if (m === 'n') return a.n;
    if (m === 'sites') return a.sites.size;
    if (m === 'kw') return a.kw / 1000;
    if (m === 'occ') return a.act ? 100 * a.chg / a.act : null;
    if (m === 'down') return a.n ? 100 * a.down / a.n : null;
    return a.feeN ? a.feeS / a.feeN : null;
  }
  function fmt(v, m) {
    if (v == null) return '—';
    if (m === 'kw') return N.nf(v, v < 100 ? 1 : 0) + ' MW';
    if (m === 'occ' || m === 'down') return N.nf(v, 1) + ' %';
    if (m === 'fee') return N.eur(v) + ' €';
    return N.nf(v);
  }
  function passes(d, vals) {
    var f = F[d]; if (!f.size) return true;
    for (var i = 0; i < vals.length; i++) if (f.has(vals[i])) return true;
    return false;
  }
  function compute() {
    var by = {}, total = acc(), sel = [];
    DIMS.forEach(function (d) { by[d] = new Map(); });
    for (var i = 0; i < P.length; i++) {
      var p = P[i], fails = 0, bad = null, k, d;
      for (k = 0; k < DIMS.length; k++) {
        d = DIMS[k];
        if (!passes(d, d === 'status' ? [p.status] : V[d][i])) { fails++; bad = d; if (fails > 1) break; }
      }
      if (fails > 1) continue;
      if (!fails) { put(total, p); sel.push(p); }
      for (k = 0; k < DIMS.length; k++) {
        d = DIMS[k];
        if (fails && bad !== d) continue;
        var vs = d === 'status' ? [p.status] : V[d][i];
        for (var j = 0; j < vs.length; j++) { var a = by[d].get(vs[j]); if (!a) by[d].set(vs[j], a = acc()); put(a, p); }
      }
    }
    A = { by: by, total: total, sel: sel };
  }

  // ---------------------------------------------------------------- state
  function toggle(d, v) { if (F[d].has(v)) F[d].delete(v); else F[d].add(v); update(); }
  function readHash() {
    var h = location.hash.replace(/^#/, ''); if (!h) return;
    h.split('&').forEach(function (kv) {
      var i = kv.indexOf('='); if (i < 1) return;
      var k = kv.slice(0, i), raw = kv.slice(i + 1);
      if (k === 'm') { if (METRICS.indexOf(raw) >= 0) metric = raw; return; }
      if (!F[k]) return;
      raw.split('~').forEach(function (x) { try { x = decodeURIComponent(x); } catch (e) { return; } if (x) F[k].add(x); });
    });
  }
  function writeHash() {
    var parts = metric === 'n' ? [] : ['m=' + metric];
    DIMS.forEach(function (d) { if (F[d].size) parts.push(d + '=' + Array.from(F[d]).map(encodeURIComponent).join('~')); });
    try { history.replaceState(null, '', parts.length ? '#' + parts.join('&') : location.pathname + location.search); } catch (e) {}
  }
  // A filter value that no longer exists (shared link from another week) is dropped.
  function pruneFilters() {
    DIMS.forEach(function (d) {
      var known = new Set(); P.forEach(function (p, i) { (d === 'status' ? [p.status] : V[d][i]).forEach(function (v) { known.add(v); }); });
      Array.from(F[d]).forEach(function (v) { if (!known.has(v)) F[d].delete(v); });
    });
  }

  // ---------------------------------------------------------------- tooltip
  function tip(e, lines) {
    var n = $('tip');
    if (!lines) { n.hidden = true; return; }
    N.clear(n); lines.forEach(function (l, i) { n.appendChild(el(i ? 'span' : 'b', null, l)); });
    n.hidden = false;
    var w = n.offsetWidth, x = Math.min(window.innerWidth - w - 8, Math.max(8, e.clientX + 14));
    n.style.left = x + 'px'; n.style.top = Math.max(8, e.clientY - n.offsetHeight - 12) + 'px';
  }

  // ---------------------------------------------------------------- header
  function renderBar() {
    var seg = N.clear($('metric'));
    METRICS.forEach(function (m) {
      seg.appendChild(el('button', { class: 'btn sm', type: 'button', 'aria-pressed': String(metric === m), onclick: function () { metric = m; update(); } }, t('m_' + m)));
    });
    var chips = N.clear($('chips')), any = false;
    DIMS.forEach(function (d) { F[d].forEach(function (v) {
      any = true; var name = t('d_' + d) + ': ' + label(d, v);
      chips.appendChild(el('li', null, el('button', { class: 'xchip', type: 'button', 'aria-label': t('xRemove', { v: name }), onclick: function () { toggle(d, v); } },
        name, el('span', { 'aria-hidden': 'true' }, ' ×'))));
    }); });
    $('reset').hidden = !any;
    var n = A.total.n;
    $('selText').textContent = !n ? t('xSelZero') : n === P.length ? t('xSelAll', { n: N.nf(n) })
      : t('xSelSome', { n: N.nf(n), m: N.nf(P.length), p: N.nf(100 * n / P.length, 1) });
  }
  function renderKpis() {
    var a = A.total, n = a.n, ul = N.clear($('kpis'));
    var pct = function (x) { return n ? N.nf(100 * x / n, 1) : '—'; };
    [[t('k_n'), N.nf(n), n === P.length ? '' : t('ks_share', { p: N.nf(100 * n / P.length, 1) })],
      [t('k_sites'), N.nf(a.sites.size), a.sites.size ? t('ks_persite', { v: N.nf(n / a.sites.size, 1) }) : ''],
      [t('k_kw'), fmt(a.kw / 1000, 'kw'), n ? t('ks_kw', { v: N.nf(a.kw / n) }) : ''],
      [t('k_free'), N.nf(a.act - a.chg), t('ks_pct', { p: pct(a.act - a.chg) })],
      [t('k_chg'), N.nf(a.chg), a.act ? t('ks_occ', { p: N.nf(100 * a.chg / a.act, 1) }) : ''],
      [t('k_down'), N.nf(a.down), t('ks_pct', { p: pct(a.down) })]
    ].forEach(function (k) { ul.appendChild(el('li', null, el('span', { class: 't' }, k[0]), el('span', { class: 'v' }, k[1]), el('span', { class: 's' }, k[2]))); });
  }
  function renderStatus() {
    var m = A.by.status, tot = 0, stack = N.clear($('stack')), lg = N.clear($('legend'));
    m.forEach(function (a) { tot += a.n; });
    N.STATUSES.forEach(function (s) {
      var a = m.get(s); if (!a) return;
      var on = F.status.has(s), dim = F.status.size && !on, share = 100 * a.n / tot;
      var segm = el('span', { class: 'xseg' + (dim ? ' dim' : ''), 'data-s': s, 'aria-hidden': 'true' });
      segm.style.width = share + '%';
      segm.addEventListener('click', function () { toggle('status', s); });
      segm.addEventListener('mousemove', function (e) { tip(e, [t('st_' + s), N.nf(a.n) + ' (' + N.nf(share, 1) + ' %)']); });
      segm.addEventListener('mouseleave', function () { tip(); });
      stack.appendChild(segm);
      lg.appendChild(el('li', null, el('button', { class: 'xleg' + (dim ? ' dim' : ''), type: 'button', 'aria-pressed': String(on), 'data-v': s, onclick: function () { toggle('status', s); } },
        N.status(s), el('b', null, N.nf(a.n)), el('span', { class: 'muted' }, N.nf(share, 1) + ' %'))));
    });
  }

  // ---------------------------------------------------------------- dimension cards
  function rowsFor(d) {
    var m = A.by[d], rows = [];
    m.forEach(function (a, v) { rows.push({ v: v, a: a, x: val(a, metric), few: RATIO[metric] && a.n < MIN_N }); });
    if (FIXED[d]) {
      var order = FIXED[d];
      rows.sort(function (r, s) { return (order.indexOf(r.v) < 0 ? 99 : order.indexOf(r.v)) - (order.indexOf(s.v) < 0 ? 99 : order.indexOf(s.v)); });
    } else {
      rows.sort(function (r, s) { return (r.few - s.few) || ((s.x == null ? -1 : s.x) - (r.x == null ? -1 : r.x)) || (s.a.n - r.a.n); });
    }
    return rows;
  }
  function buildCards() {
    var box = N.clear($('dims'));
    CARDS.forEach(function (d) {
      var card = el('div', { class: 'card xdim', id: 'dim_' + d }, el('h3', { id: 'hd_' + d }));
      if (LONG[d]) {
        var inp = el('input', { type: 'search', class: 'xfind', id: 'q_' + d, autocomplete: 'off' });
        inp.addEventListener('input', function () { query[d] = inp.value.trim().toLowerCase(); renderCard(d); });
        card.appendChild(inp);
      }
      card.appendChild(el('ul', { class: 'xrows', id: 'rows_' + d, 'aria-labelledby': 'hd_' + d }));
      if (LONG[d]) card.appendChild(el('button', { class: 'btn sm xmore', type: 'button', id: 'more_' + d, onclick: function () { open[d] = !open[d]; renderCard(d); } }));
      box.appendChild(card);
    });
  }
  function renderCard(d) {
    var ul = $('rows_' + d), rows = rowsFor(d), q = query[d] || '';
    var focusV = document.activeElement && ul.contains(document.activeElement) ? document.activeElement.getAttribute('data-v') : null;
    $('hd_' + d).textContent = t('d_' + d) + (RATIO[metric] || metric !== 'n' ? ', ' + t('m_' + metric).toLowerCase() : '');
    if (LONG[d]) { var inp = $('q_' + d), ph = t('xFind', { d: t('d_' + d).toLowerCase() }); inp.setAttribute('placeholder', ph); inp.setAttribute('aria-label', ph); }
    var max = 0; rows.forEach(function (r) { if (!r.few && r.x != null && r.x > max) max = r.x; });
    // Shares are of this list's own total: the list ignores its own filter, so the selection is not its base.
    var share = (metric === 'n' || metric === 'kw') && !MULTI[d], total = 0, shown = rows;
    if (share) rows.forEach(function (r) { total += r.x || 0; });
    if (q) shown = rows.filter(function (r) { return label(d, r.v).toLowerCase().indexOf(q) >= 0; });
    else if (LONG[d] && !open[d]) shown = rows.filter(function (r, i) { return i < TOP || F[d].has(r.v); });
    N.clear(ul);
    shown.forEach(function (r) {
      var on = F[d].has(r.v), dim = F[d].size && !on;
      var fill = el('span', { class: 'fill' }); fill.style.width = (max && r.x != null ? Math.min(100, 100 * r.x / max) : 0) + '%';
      var extra = r.few ? t('xFew') : (share && total ? N.nf(100 * r.x / total, 1) + ' %' : N.nf(r.a.n) + ' ' + t('m_n').toLowerCase());
      if (metric === 'n' && MULTI[d]) extra = '';
      ul.appendChild(el('li', null, el('button', { class: 'xrow' + (dim ? ' dim' : '') + (r.few ? ' few' : '') + (d === 'conn' && r.v === 'MCS' ? ' mcs' : ''), type: 'button', 'aria-pressed': String(on), 'data-v': r.v, onclick: function () { toggle(d, r.v); } },
        el('span', { class: 'lb' }, label(d, r.v)), el('span', { class: 'track', 'aria-hidden': 'true' }, fill),
        el('span', { class: 'vl' }, fmt(r.x, metric)), el('span', { class: 'ex muted' }, extra))));
    });
    if (!shown.length) ul.appendChild(el('li', { class: 'muted small' }, t('xNoMatch')));
    if (LONG[d]) { var b = $('more_' + d); b.hidden = !!q || rows.length <= TOP; b.textContent = open[d] ? t('xLess') : t('xAll', { n: N.nf(rows.length) }); }
    if (focusV != null) { var again = Array.prototype.filter.call(ul.querySelectorAll('button'), function (x) { return x.getAttribute('data-v') === focusV; })[0]; if (again) again.focus(); }
  }

  // ---------------------------------------------------------------- sites + map
  function siteRows() {
    var m = new Map();
    A.sel.forEach(function (p) {
      var s = m.get(p.site_external_id);
      if (!s) m.set(p.site_external_id, s = { ext: p.site_external_id, city: p.city, op: p.operator_name, n: 0, kw: 0, free: 0, chg: 0, down: 0 });
      s.n++; s.kw += p.kw || 0;
      if (p.status === 'available') s.free++; else if (p.status === 'charging') s.chg++;
      else if (p.status === 'outOfOrder' || p.status === 'inoperative') s.down++;
    });
    return Array.from(m.values());
  }
  function siteState(s) { return s.free ? 'available' : s.chg ? 'charging' : s.down ? 'outOfOrder' : 'unknown'; }
  function renderSites(rows) {
    var top = rows.slice().sort(function (a, b) { return b.kw - a.kw || b.n - a.n; }).slice(0, 25);
    N.clear($('sites')).appendChild(el('table', null,
      el('thead', null, el('tr', null, ['sName', 'sCity', 'sN', 'sKw', 'sFree'].map(function (k, i) { return el('th', { scope: 'col', class: i < 2 ? 'l' : null }, t(k)); }))),
      el('tbody', null, top.map(function (s) {
        var info = siteInfo.get(s.ext), name = info && info.name && info.name !== s.ext ? info.name : s.ext;
        return el('tr', null, el('th', { scope: 'row', class: 'l' }, el('a', { href: 'index.html?q=' + encodeURIComponent(s.ext), title: t('xOpenFind', { v: s.ext }) }, name),
          el('span', { class: 'muted small xop' }, s.op)), el('td', { class: 'l' }, s.city), el('td', null, N.nf(s.n)), el('td', null, N.nf(s.kw)), el('td', null, N.nf(s.free)));
      }))));
  }
  var MAINLAND = [-9.75, 36.85, -6.05, 42.25], mapPts = [], mapProj = null;
  function drawMap(rows) {
    var cv = $('map'), g = cv.getContext('2d'), cs = getComputedStyle(document.documentElement), c = {};
    ['available', 'charging', 'outOfOrder', 'unknown'].forEach(function (s) { c[s] = cs.getPropertyValue('--s-' + s).trim(); });
    var land = cs.getPropertyValue('--bg-alt').trim(), line = cs.getPropertyValue('--muted').trim();
    var pts = [], off = 0;
    rows.forEach(function (s) { var i = siteInfo.get(s.ext); if (i && isFinite(i.lat) && isFinite(i.lon)) pts.push({ s: s, lon: i.lon, lat: i.lat, name: i.name, region: i.region }); else off++; });
    var main = pts.filter(function (p) { return p.region === 'mainland'; }), use = main.length ? main : pts;
    off += pts.length - use.length;
    var v = MAINLAND.slice();
    if (use.length && (use.length < pts.length || !main.length || rows.length < siteInfo.size * 0.5)) {
      // Frame the bulk of the selection: a site with wrong coordinates must not shrink a city to a dot.
      var lons = use.map(function (p) { return p.lon; }).sort(function (a, b) { return a - b; });
      var lats = use.map(function (p) { return p.lat; }).sort(function (a, b) { return a - b; });
      var cut = use.length >= 30 ? Math.floor(use.length * 0.02) : 0;
      v = [lons[cut], lats[cut], lons[lons.length - 1 - cut], lats[lats.length - 1 - cut]];
      var padX = Math.max(0.06, (v[2] - v[0]) * 0.08), padY = Math.max(0.06, (v[3] - v[1]) * 0.08);
      v = [v[0] - padX, v[1] - padY, v[2] + padX, v[3] + padY];
    }
    var k = Math.cos(((v[1] + v[3]) / 2) * Math.PI / 180), w = (v[2] - v[0]) * k, h = v[3] - v[1], sc = Math.min(cv.width / w, cv.height / h);
    var ox = (cv.width - w * sc) / 2, oy = (cv.height - h * sc) / 2;
    var X = function (lon) { return ox + (lon - v[0]) * k * sc; }, Y = function (lat) { return oy + (v[3] - lat) * sc; };
    g.clearRect(0, 0, cv.width, cv.height);
    if (outline) {
      g.fillStyle = land; g.strokeStyle = line; g.lineWidth = 1;
      Object.keys(outline).forEach(function (rg) { outline[rg].forEach(function (ring) {
        g.beginPath(); ring.forEach(function (q, i) { if (i) g.lineTo(X(q[0]), Y(q[1])); else g.moveTo(X(q[0]), Y(q[1])); });
        g.closePath(); g.fill(); g.globalAlpha = 0.35; g.stroke(); g.globalAlpha = 1; }); });
    }
    var r = use.length > 3000 ? 2.2 : use.length > 600 ? 3 : use.length > 80 ? 4.5 : 6.5;
    var order = { unknown: 0, outOfOrder: 1, charging: 2, available: 3 };
    mapPts = use.map(function (p) { return { x: X(p.lon), y: Y(p.lat), p: p, st: siteState(p.s) }; }).sort(function (a, b) { return order[a.st] - order[b.st]; });
    mapPts.forEach(function (m) {
      g.fillStyle = c[m.st]; g.strokeStyle = c[m.st]; g.beginPath();
      if (m.st === 'charging') g.rect(m.x - r, m.y - r, 2 * r, 2 * r);
      else if (m.st === 'outOfOrder') { g.moveTo(m.x, m.y - r * 1.2); g.lineTo(m.x + r * 1.2, m.y + r); g.lineTo(m.x - r * 1.2, m.y + r); g.closePath(); }
      else g.arc(m.x, m.y, r, 0, 6.3);
      if (m.st === 'unknown') { g.lineWidth = 1.5; g.stroke(); } else { g.globalAlpha = use.length > 600 ? 0.8 : 1; g.fill(); g.globalAlpha = 1; }
    });
    mapProj = { r: r };
    $('mapNote').textContent = t('xMapNote', { n: N.nf(use.length) }) + (off ? t('xMapIsl', { n: N.nf(off) }) : '');
  }
  function mapHit(e) {
    var cv = $('map'), b = cv.getBoundingClientRect(), x = (e.clientX - b.left) * cv.width / b.width, y = (e.clientY - b.top) * cv.height / b.height;
    var best = null, bd = Math.pow(Math.max(10, (mapProj ? mapProj.r : 4) * 2.5), 2);
    for (var i = mapPts.length - 1; i >= 0; i--) { var dx = mapPts[i].x - x, dy = mapPts[i].y - y, dd = dx * dx + dy * dy; if (dd < bd) { bd = dd; best = mapPts[i]; } }
    return best;
  }
  function initMap() {
    var cv = $('map');
    cv.addEventListener('mousemove', function (e) {
      var m = mapHit(e); cv.style.cursor = m ? 'pointer' : '';
      tip(e, m && [m.p.name || m.p.s.ext, m.p.s.op, N.nf(m.p.s.n) + ' ' + t('m_n').toLowerCase() + ', ' + N.nf(m.p.s.kw) + ' kW', t('st_' + m.st)]);
    });
    cv.addEventListener('mouseleave', function () { tip(); });
    cv.addEventListener('click', function (e) { var m = mapHit(e); if (m) location.href = 'index.html?q=' + encodeURIComponent(m.p.s.ext); });
  }

  // ---------------------------------------------------------------- charts
  // Column chart of counts per bin.
  function renderFee() {
    var box = N.clear($('fee')), xs = [];
    A.sel.forEach(function (p) { if (p._fee != null) xs.push(p._fee); });
    if (!xs.length) { box.appendChild(el('p', { class: 'muted' }, t('feeNone'))); return; }
    xs.sort(function (a, b) { return a - b; });
    var STEP = 0.05, NB = 12, bins = [];
    for (var i = 0; i < NB; i++) bins.push(0);
    xs.forEach(function (x) { bins[Math.min(NB - 1, Math.floor(x / STEP + 1e-9))]++; });
    var W = 640, Hh = 200, L = 8, B = 28, T = 18, bw = (W - 2 * L) / NB, max = Math.max.apply(null, bins);
    var svg = sv('svg', { viewBox: '0 0 ' + W + ' ' + Hh, class: 'xchart', role: 'img', 'aria-label': t('xFee') });
    svg.appendChild(sv('line', { x1: L, x2: W - L, y1: Hh - B, y2: Hh - B, class: 'axis' }));
    bins.forEach(function (n, i) {
      var h = max ? (Hh - B - T) * n / max : 0, x = L + i * bw, a = N.eur(i * STEP), b = i === NB - 1 ? '+' : N.eur((i + 1) * STEP);
      var txt = i === NB - 1 ? a + '+ €/kWh: ' + N.nf(n) : t('feeBin', { a: a, b: b, n: N.nf(n) });
      if (n) svg.appendChild(sv('path', { class: 'col', d: 'M' + (x + 1) + ' ' + (Hh - B) + 'V' + (Hh - B - h + 4) + 'q0 -4 4 -4H' + (x + bw - 5) + 'q4 0 4 4V' + (Hh - B) + 'Z' }));
      if (n && h > 0) svg.appendChild(sv('text', { x: x + bw / 2, y: Hh - B - h - 5, class: 'vlab', 'text-anchor': 'middle' }, N.nf(n)));
      svg.appendChild(sv('text', { x: x, y: Hh - 8, class: 'tick', 'text-anchor': i ? 'middle' : 'start' }, a));
      var hit = sv('rect', { x: x, y: 0, width: bw, height: Hh - B, class: 'hit' });
      hit.addEventListener('mousemove', function (e) { tip(e, [txt]); }); hit.addEventListener('mouseleave', function () { tip(); });
      svg.appendChild(hit);
    });
    svg.appendChild(sv('text', { x: W - L, y: Hh - 8, class: 'tick', 'text-anchor': 'end' }, t('feeAxis')));
    box.appendChild(svg);
    box.appendChild(el('p', { class: 'muted small' }, t('feeN', { n: N.nf(xs.length), m: N.eur(xs[Math.floor(xs.length / 2)]) })));
  }
  function niceStep(span, n) {
    var raw = span / n, p = Math.pow(10, Math.floor(Math.log(raw) / Math.LN10)), f = raw / p;
    return (f <= 1 ? 1 : f <= 2 ? 2 : f <= 5 ? 5 : 10) * p;
  }
  // One series, one axis. ys may hold nulls (no data: the line breaks).
  function lineChart(box, o) {
    N.clear(box);
    var ys = o.ys, n = ys.length, vals = ys.filter(function (y) { return y != null; });
    if (vals.length < 2) { box.appendChild(el('p', { class: 'muted' }, t('xNoHist'))); return; }
    var W = o.w || 640, Hh = o.h || 220, L = 46, R = 14, T = 14, B = 26;
    var lo = Math.min.apply(null, vals), hi = Math.max.apply(null, vals);
    if (o.zero) lo = 0;
    if (hi === lo) { hi = lo + 1; }
    var step = niceStep(hi - lo, 4); lo = Math.floor(lo / step) * step; hi = Math.ceil(hi / step) * step;
    var X = function (i) { return L + (W - L - R) * (n > 1 ? i / (n - 1) : 0); }, Y = function (y) { return T + (Hh - T - B) * (1 - (y - lo) / (hi - lo)); };
    var svg = sv('svg', { viewBox: '0 0 ' + W + ' ' + Hh, class: 'xchart', role: 'img', 'aria-label': o.title });
    for (var g = lo; g <= hi + step / 2; g += step) {
      svg.appendChild(sv('line', { x1: L, x2: W - R, y1: Y(g), y2: Y(g), class: 'grid' }));
      svg.appendChild(sv('text', { x: L - 6, y: Y(g) + 4, class: 'tick', 'text-anchor': 'end' }, N.nf(g, o.dec)));
    }
    (o.ticks || []).forEach(function (tk) { svg.appendChild(sv('text', { x: X(tk[0]), y: Hh - 8, class: 'tick', 'text-anchor': 'middle' }, tk[1])); });
    var d = '', pen = false;
    ys.forEach(function (y, i) { if (y == null) { pen = false; return; } d += (pen ? 'L' : 'M') + X(i).toFixed(1) + ' ' + Y(y).toFixed(1); pen = true; });
    svg.appendChild(sv('path', { d: d, class: 'ln' }));
    var last = n - 1; while (last > 0 && ys[last] == null) last--;
    svg.appendChild(sv('circle', { cx: X(last), cy: Y(ys[last]), r: 4, class: 'pt' }));
    var cross = sv('line', { y1: T, y2: Hh - B, class: 'cross', visibility: 'hidden' }), dot = sv('circle', { r: 5, class: 'pt ring', visibility: 'hidden' });
    var hit = sv('rect', { x: L, y: 0, width: W - L - R, height: Hh, class: 'hit' });
    function move(e) {
      var b = svg.getBoundingClientRect(), x = (e.clientX - b.left) * W / b.width, i = Math.round((x - L) / (W - L - R) * (n - 1));
      i = Math.max(0, Math.min(n - 1, i));
      if (ys[i] == null) { cross.setAttribute('visibility', 'hidden'); dot.setAttribute('visibility', 'hidden'); tip(); return; }
      cross.setAttribute('x1', X(i)); cross.setAttribute('x2', X(i)); cross.setAttribute('visibility', 'visible');
      dot.setAttribute('cx', X(i)); dot.setAttribute('cy', Y(ys[i])); dot.setAttribute('visibility', 'visible');
      tip(e, [o.xs[i], N.nf(ys[i], o.tipDec == null ? o.dec : o.tipDec) + (o.unit || '')]);
    }
    hit.addEventListener('pointermove', move); hit.addEventListener('pointerdown', move);
    hit.addEventListener('pointerleave', function () { cross.setAttribute('visibility', 'hidden'); dot.setAttribute('visibility', 'hidden'); tip(); });
    svg.appendChild(cross); svg.appendChild(dot); svg.appendChild(hit);
    box.appendChild(svg);
    // The same numbers as a table, for screen readers and for copying.
    var every = Math.max(1, Math.ceil(n / 60)), rows = [];
    ys.forEach(function (y, i) { if (y != null && (i % every === 0 || i === last)) rows.push(el('tr', null, el('th', { scope: 'row', class: 'l' }, o.xs[i]), el('td', null, N.nf(y, o.tipDec == null ? o.dec : o.tipDec) + (o.unit || '')))); });
    box.appendChild(el('details', { class: 'xtable' }, el('summary', null, t('xTable')), el('div', { class: 'scroll' },
      el('table', null, el('thead', null, el('tr', null, el('th', { scope: 'col', class: 'l' }, o.xlabel), el('th', { scope: 'col' }, t('xVal')))), el('tbody', null, rows)))));
  }

  // ---------------------------------------------------------------- history
  var lisbon = null;
  function local(ms) {   // [weekday 0=Mon, hour, 'dd/mm'] in Lisbon time
    if (!lisbon) lisbon = new Intl.DateTimeFormat('en-GB', { timeZone: 'Europe/Lisbon', weekday: 'short', hour: '2-digit', day: '2-digit', month: '2-digit', hour12: false });
    var o = {}; lisbon.formatToParts(new Date(ms)).forEach(function (p) { o[p.type] = p.value; });
    return [['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'].indexOf(o.weekday), Number(o.hour) % 24, o.day + '/' + o.month];
  }
  function renderTrends() {
    if (!H || !H.daily || !H.daily.days.length) { $('tend').hidden = true; return; }
    $('tend').hidden = false;
    var opIx = new Set(), pwIx = new Set(), rgIx = new Set();
    H.ops.forEach(function (o, i) { if (F.op.has(o)) opIx.add(i); });
    H.pw.forEach(function (c, i) { if (F.pw.has(c)) pwIx.add(i); });
    H.regions.forEach(function (r, i) { if (F.region.has(r)) rgIx.add(i); });
    var okOp = function (i) { return !F.op.size || opIx.has(i); }, okPw = function (i) { return !F.pw.size || pwIx.has(i); }, okRg = function (i) { return !F.region.size || rgIx.has(i); };
    var ign = DIMS.filter(function (d) { return F[d].size && d !== 'op' && d !== 'pw' && d !== 'region'; }).map(function (d) { return t('d_' + d).toLowerCase(); });
    $('trendNote').textContent = t('xTrendBase') + (ign.length ? t('xTrendIgn', { f: ign.join(', ') }) : '') + (F.region.size ? t('xTrendHour') : '');

    var D = H.daily, nd = D.days.length, n = new Array(nd).fill(0), dn = new Array(nd).fill(0);
    D.combos.forEach(function (c, k) {
      if (!okOp(c[0]) || !okPw(c[1]) || !okRg(c[2])) return;
      for (var i = 0; i < nd; i++) { n[i] += D.n[k][i]; dn[i] += D.down[k][i]; }
    });
    var dlab = D.days.map(function (d) { return d.slice(8, 10) + '/' + d.slice(5, 7); }), dticks = [];
    for (var i = 0; i < nd; i += Math.max(1, Math.round(nd / 6))) dticks.push([i, dlab[i]]);
    lineChart($('tSize'), { title: t('xTSize'), xs: dlab, ys: n.map(function (x) { return x || null; }), dec: 0, ticks: dticks, xlabel: t('xDay') });
    lineChart($('tDown'), { title: t('xTDown'), xs: dlab, ys: n.map(function (x, i) { return x ? 100 * dn[i] / x : null; }), dec: 1, unit: ' %', zero: true, ticks: dticks, xlabel: t('xDay') });

    var Q = H.hourly, nh = Q.hours, chg = new Array(nh).fill(0), act = new Array(nh).fill(0), t0 = Date.parse(Q.start);
    Q.combos.forEach(function (c, k) {
      if (!okOp(c[0]) || !okPw(c[1])) return;
      for (var i = 0; i < nh; i++) { chg[i] += Q.chg[k][i]; act[i] += Q.act[k][i]; }
    });
    var hx = [], hticks = [], heat = [], cnt = [], w, days = new Set();
    for (w = 0; w < 7; w++) { heat.push(new Array(24).fill(0)); cnt.push(new Array(24).fill(0)); }
    var occ = [];
    for (i = 0; i < nh; i++) {
      var lc = local(t0 + i * 3600000), ok = Q.samples[i] > 0 && act[i] > 0;
      hx.push(t('wd' + lc[0]).slice(0, 3) + ' ' + lc[2] + ', ' + lc[1] + ' h');
      if (lc[1] === 0) hticks.push([i, lc[2]]);
      occ.push(ok ? 100 * chg[i] / act[i] : null);
      if (ok) { heat[lc[0]][lc[1]] += chg[i]; cnt[lc[0]][lc[1]] += act[i]; days.add(lc[2]); }
    }
    if (hticks.length > 8) hticks = hticks.filter(function (_, j) { return j % Math.ceil(hticks.length / 8) === 0; });
    lineChart($('tOcc'), { title: t('xTOcc'), xs: hx, ys: occ, dec: 0, tipDec: 1, unit: ' %', zero: true, ticks: hticks, w: $('tOcc').clientWidth > 700 ? 1120 : 640, h: 240, xlabel: t('xHour') });

    var hmax = 0; for (w = 0; w < 7; w++) for (i = 0; i < 24; i++) if (cnt[w][i]) hmax = Math.max(hmax, 100 * heat[w][i] / cnt[w][i]);
    var hours = []; for (i = 0; i < 24; i++) hours.push(i);
    N.clear($('tHeat')).appendChild(el('table', { class: 'xheat' },
      el('thead', null, el('tr', null, el('td', null), hours.map(function (h) { return el('th', { scope: 'col' }, h % 3 ? el('span', { class: 'sr' }, String(h)) : String(h)); }))),
      el('tbody', null, heat.map(function (row, wd) {
        return el('tr', null, el('th', { scope: 'row', class: 'l' }, t('wd' + wd)), row.map(function (s, h) {
          if (!cnt[wd][h]) return el('td', { class: 'na' }, el('span', { class: 'sr' }, '—'));
          var v = 100 * s / cnt[wd][h], td = el('td', null, el('span', { class: 'sr' }, N.nf(v, 1) + ' %'));
          td.style.setProperty('--k', (hmax ? Math.round(8 + 92 * v / hmax) : 0) + '%');
          var txt = t('heatCell', { w: t('wd' + wd), h: h, v: N.nf(v, 1) });
          td.addEventListener('mousemove', function (e) { tip(e, [txt]); }); td.addEventListener('mouseleave', function () { tip(); });
          return td;
        }));
      }))));
    $('heatNote').textContent = t('heatNote', { d: days.size, m: N.nf(hmax, 1) });
  }

  // ---------------------------------------------------------------- loop
  function update() {
    compute(); writeHash();
    renderBar(); renderKpis(); renderStatus();
    CARDS.forEach(renderCard);
    var rows = siteRows(); renderSites(rows); drawMap(rows);
    renderFee(); renderTrends();
    N.liveNote($('live'), liveRes, snapshot);
  }
  function live() {
    return N.fetchLive(P).then(function (res) { if (res) liveRes = res; update(); });
  }

  N.initChrome();
  $('reset').addEventListener('click', function () { DIMS.forEach(function (d) { F[d].clear(); }); update(); });
  initMap();
  Promise.all([N.load('points'), N.load('stats')]).then(function (r) {
    snapshot = r[1].snapshot; prep(r[0].points); readHash(); pruneFilters(); buildCards(); update();
    N.onLang(update);
    live();
    // The archive rewrites the status file every few minutes: follow it while the page is visible.
    setInterval(function () { if (!document.hidden) live(); }, 5 * 60000);
    N.load('sites').then(function (s) {
      s.sites.forEach(function (x) { if (!x.lc) siteInfo.set(x.ext, { name: x.name, lat: x.lat, lon: x.lon, region: x.region }); });
      return N.load('outline');
    }).then(function (o) { outline = o.outline; update(); }).catch(function () {});
    N.load('history').then(function (h) { H = h; renderTrends(); }).catch(function () {});
  }).catch(function () { $('live').textContent = t('loadFail'); });
})();
