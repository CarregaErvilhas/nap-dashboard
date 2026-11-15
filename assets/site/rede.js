// "A rede em números": stat tiles and bar charts. Every chart is a real table
// (label, bar, value), so it reads the same with a screen reader or no CSS.
// The summary stays on top; the sections below it show one at a time (the
// subnav links act as tabs, "Tudo" shows the whole page as before).
'use strict';
(function () {
  var N = window.NAP, el = N.el, t = N.t;
  N.addStrings({
    netH1: 'A rede em números', netLead: 'Quantos postos há, de quem são, que potência têm e quanto estão ocupados.',
    sections: 'Secções', sSummary: 'Resumo', sNews: 'Novidades', sNetwork: 'Postos', sOps: 'Operadores', sOcc: 'Ocupação', sPrice: 'Preços',
    sHist: 'Histórico', sHubs: 'Hubs', sFacts: 'Factos', hNews: 'Novidades', hWeek: 'Na última semana', hNetwork: 'Que postos há', hOps: 'Quem opera a rede',
    hOcc: 'Ocupação neste momento', occNote: 'Tomadas a carregar sobre as que estão livres ou a carregar.', hPrice: 'Taxa do operador',
    priceNote: 'É o que o operador do posto (OPC) cobra pelo uso, sem IVA. A energia é cobrada à parte pelo teu comercializador (CEME).',
    hHist: 'Histórico (AmpereArchive)', hHubs: 'Maiores hubs por potência total', hFacts: 'Factos sobre a rede',
    cStatus: 'Tomadas por estado', cPw: 'Tomadas por classe de potência', cConn: 'Fichas por tipo', cRegion: 'Locais por região',
    cCity: 'Os 15 concelhos com mais locais', cOpSites: 'Os 15 operadores com mais locais', cOpPts: 'Os 15 operadores com mais tomadas',
    cOccPw: 'Ocupação por classe de potência (%)', cOccOp: 'Ocupação por operador, os 15 maiores (%)',
    cPriceOp: 'Taxa média por kWh, por operador (€/kWh)', cStatusPw: 'Estado por classe de potência', cPriceStats: 'Componentes da taxa do operador',
    colWhat: 'Componente', colN: 'tomadas', colMean: 'média', colMax: 'máximo', pEnergy: 'Por energia (€/kWh)', pTime: 'Por tempo (€/min)',
    pFlat: 'Fixa por carregamento (€)', pSem: 'Valor único fora da MOBI.E (*)', power: 'Classe de potência', value: 'Valor', sAll: 'Tudo'
  }, {
    netH1: 'The network in numbers', netLead: 'How many chargers there are, who runs them, how powerful and how busy they are.',
    sections: 'Sections', sSummary: 'Summary', sNews: 'News', sNetwork: 'Chargers', sOps: 'Operators', sOcc: 'Occupancy', sPrice: 'Prices',
    sHist: 'History', sHubs: 'Hubs', sFacts: 'Facts', hNews: 'News', hWeek: 'Over the last week', hNetwork: 'What chargers exist', hOps: 'Who runs the network',
    hOcc: 'Occupancy right now', occNote: 'Sockets charging over those free or charging.', hPrice: 'Operator fee',
    priceNote: 'What the charger operator (CPO) bills for use, without VAT. Energy is billed separately by your supplier (CEME).',
    hHist: 'History (AmpereArchive)', hHubs: 'Largest hubs by total power', hFacts: 'Facts about the network',
    cStatus: 'Sockets by status', cPw: 'Sockets by power class', cConn: 'Plugs by type', cRegion: 'Sites by region',
    cCity: 'The 15 municipalities with most sites', cOpSites: 'The 15 operators with most sites', cOpPts: 'The 15 operators with most sockets',
    cOccPw: 'Occupancy by power class (%)', cOccOp: 'Occupancy by operator, 15 largest (%)',
    cPriceOp: 'Mean fee per kWh, by operator (€/kWh)', cStatusPw: 'Status by power class', cPriceStats: 'Operator fee components',
    colWhat: 'Component', colN: 'sockets', colMean: 'mean', colMax: 'max', pEnergy: 'Per energy (€/kWh)', pTime: 'Per time (€/min)',
    pFlat: 'Flat per session (€)', pSem: 'Single value outside MOBI.E (*)', power: 'Power class', value: 'Value', sAll: 'All'
  });
  var D = null, liveRes = null;
  var $ = function (id) { return document.getElementById(id); };

  // rows: [[label, number|null, labelNode?]]
  function bars(id, title, rows, dec, suffix, min) {
    var max = Math.max.apply(null, rows.map(function (r) { return r[1] || 0; }).concat([0]));
    var tb = el('tbody', null, rows.map(function (r) {
      var fill = el('div', { class: 'fill' }); fill.style.width = (max ? 100 * (r[1] || 0) / max : 0) + '%';
      return el('tr', null, el('th', { scope: 'row' }, r[2] || r[0]), el('td', { class: 'b', 'aria-hidden': 'true' }, el('div', { class: 'track' }, fill)),
        el('td', null, r[1] == null ? '—' : N.nf(r[1], dec, min) + (suffix || '')));
    }));
    N.clear($(id)).appendChild(el('table', { class: 'bars' }, el('caption', null, t(title)),
      el('thead', { class: 'sr' }, el('tr', null, el('th', { scope: 'col' }, ''), el('td', null), el('th', { scope: 'col' }, t('value')))), tb));
  }
  var desc = function (o) { return Object.keys(o || {}).map(function (k) { return [k, o[k]]; }).sort(function (a, b) { return b[1] - a[1]; }); };

  // Sockets by status as one stacked bar. The bar is decoration: the list under
  // it carries every number, with the same shape + text marks as the rest of the site.
  function statusBar() {
    var rows = desc(D.status), total = rows.reduce(function (a, r) { return a + r[1]; }, 0);
    var bar = el('div', { class: 'stack', 'aria-hidden': 'true' }, rows.map(function (r) {
      var seg = el('i', { 'data-s': N.STATUSES.indexOf(r[0]) >= 0 ? r[0] : 'unknown' }); seg.style.flexGrow = r[1]; return seg; }));
    N.clear($('cStatus')).appendChild(el('h3', null, t('cStatus')));
    N.add($('cStatus'), [bar, el('ul', { class: 'legend' }, rows.map(function (r) {
      return el('li', null, N.status(r[0]), ' ', el('b', null, N.nf(r[1])), ' ',
        el('span', { class: 'muted' }, total ? N.nf(100 * r[1] / total, 1) + ' %' : '')); }))]);
  }

  function render() {
    if (!D) return;
    var ul = N.clear($('kpis'));
    (N.lang() === 'pt' ? D.kpis_pt : D.kpis).forEach(function (k) {
      ul.appendChild(el('li', null, el('span', { class: 't' }, k.t), el('span', { class: 'v' }, typeof k.v === 'number' ? N.nf(k.v) : k.v), el('span', { class: 's' }, k.s)));
    });
    statusBar();
    bars('cPw', 'cPw', N.PW.map(function (c) { return [N.pwLabel(c), D.pw[c] || 0]; }));
    // MCS (veículos pesados) sempre em destaque, mesmo a 0: diz que o NAP ainda não publica nenhuma.
    var conn = desc(D.conn).filter(function (r) { return r[0] !== 'MCS'; });
    conn.push(['MCS', (D.conn || {}).MCS || 0, [el('span', { class: 'tag mcs' }, 'MCS'), ' ', t('mcsHeavy')]]);
    bars('cConn', 'cConn', conn);
    bars('cRegion', 'cRegion', desc(D.region).map(function (r) { return [t('rg_' + r[0]), r[1]]; }));
    bars('cCity', 'cCity', desc(D.city));
    bars('cOpSites', 'cOpSites', desc(D.op_sites));
    bars('cOpPts', 'cOpPts', desc(D.op_pts));
    bars('cOccPw', 'cOccPw', D.occ_pw.map(function (x) { return [N.pwLabel(x.c), x.occ]; }), 1, ' %');
    bars('cOccOp', 'cOccOp', D.occ_op.slice().sort(function (a, b) { return (b.occ || 0) - (a.occ || 0); }).map(function (x) { return [x.op, x.occ]; }), 1, ' %');
    bars('cPriceOp', 'cPriceOp', desc(D.price_op), 2, '', 2);
    var sts = N.STATUSES.filter(function (s) { return D.status[s]; });
    N.clear($('cStatusPw')).appendChild(el('table', null, el('caption', null, t('cStatusPw')),
      el('thead', null, el('tr', null, el('th', { scope: 'col' }, t('power')), sts.map(function (s) { return el('th', { scope: 'col' }, t('st_' + s)); }))),
      el('tbody', null, N.PW.filter(function (c) { return D.status_pw[c]; }).map(function (c) {
        return el('tr', null, el('th', { scope: 'row', class: 'l' }, N.pwLabel(c)), sts.map(function (s) { return el('td', null, N.nf(D.status_pw[c][s] || 0)); })); }))));
    var ps = D.price_stats || {};
    N.clear($('cPriceStats')).appendChild(el('table', null, el('caption', null, t('cPriceStats')),
      el('thead', null, el('tr', null, ['colWhat', 'colN', 'colMean', 'colMax'].map(function (k) { return el('th', { scope: 'col' }, t(k)); }))),
      el('tbody', null, [['pEnergy', ps.energy], ['pTime', ps.time], ['pFlat', ps.flat], ['pSem', ps.sem_ceme]].filter(function (r) { return r[1]; }).map(function (r) {
        return el('tr', null, el('th', { scope: 'row', class: 'l' }, t(r[0])), el('td', null, N.nf(r[1].n)), el('td', null, N.eur(r[1].mean)), el('td', null, N.eur(r[1].max))); }))));
    N.liveNote($('live'), liveRes, D.snapshot);
  }

  // The same aggregations build_dashboard.py does, over the live statuses.
  function recompute(P) {
    var isAct = function (s) { return s === 'charging' || s === 'available'; };
    var occ = function (a) { var act = a.filter(function (p) { return isAct(p.status); });
      return act.length ? Math.round(1000 * act.filter(function (p) { return p.status === 'charging'; }).length / act.length) / 10 : null; };
    D.status = {}; P.forEach(function (p) { D.status[p.status] = (D.status[p.status] || 0) + 1; });
    var sw = {}; Object.keys(D.status_pw || {}).forEach(function (c) { sw[c] = {}; });
    P.forEach(function (p) { if (p.pw_class && sw[p.pw_class]) sw[p.pw_class][p.status] = (sw[p.pw_class][p.status] || 0) + 1; });
    D.status_pw = sw;
    D.occ_pw = D.occ_pw.map(function (x) { var a = P.filter(function (p) { return p.pw_class === x.c; });
      return { c: x.c, occ: occ(a), charging: a.filter(function (p) { return p.status === 'charging'; }).length, active: a.filter(function (p) { return isAct(p.status); }).length }; });
    D.occ_op = D.occ_op.map(function (x) { return { op: x.op, pts: x.pts, occ: occ(P.filter(function (p) { return p.operator_name === x.op; })) }; });
    var o = occ(P);
    if (o != null) {
      D.kpis.forEach(function (k) { if (/^Occupancy/.test(k.t)) { k.t = 'Occupancy (live)'; k.v = o.toFixed(1) + '%'; } });
      D.kpis_pt.forEach(function (k) { if (/^Ocupação/.test(k.t)) { k.t = 'Ocupação (ao vivo)'; k.v = o.toFixed(1).replace('.', ',') + '%'; } });
    }
  }

  // ---- one section at a time ----
  var main = $('main'), nav = document.querySelector('.subnav');
  function show(id, scroll) {
    var links = [].slice.call(nav.querySelectorAll('a')).filter(function (a) { return !a.hidden; });
    var ids = links.map(function (a) { return a.getAttribute('href').slice(1); });
    if (ids.indexOf(id) < 0) id = ids[0];
    main.classList.toggle('all', id === 'tudo');
    document.querySelectorAll('section.block').forEach(function (s) { s.classList.toggle('on', s.id === id); });
    links.forEach(function (a, i) { if (ids[i] === id) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current'); });
    if (!scroll) return;
    // Further down the page than the tab bar: bring the new section's start under it.
    var top = $('tabsTop').getBoundingClientRect().top + window.scrollY - document.querySelector('.top').offsetHeight;
    if (window.scrollY > top) window.scrollTo(0, top);
  }
  main.classList.add('tabbed');
  show(location.hash.slice(1), false);
  window.addEventListener('hashchange', function () { show(location.hash.slice(1), true); });

  // The pipeline's panels arrive as flat HTML. Histórico: each numbered study
  // becomes a <details>, so the section opens as a list of five titles.
  document.querySelectorAll('#historico [data-lang]').forEach(function (box) {
    var cur = null;
    [].slice.call(box.childNodes).forEach(function (n) {
      if (n.nodeType === 1 && n.tagName === 'H3') {
        cur = el('details', { class: 'fold' });
        box.insertBefore(cur, n);
        cur.appendChild(el('summary', null, n));
      } else if (cur) cur.appendChild(n);
    });
  });
  // The weekly growth table comes oldest first; show the latest week on top.
  document.querySelectorAll('#historico table.hist').forEach(function (tb) {
    var th = tb.querySelector('th'), body = tb.tBodies[0];
    if (!th || !body || !/^(semana|week)$/i.test(th.textContent.trim())) return;
    [].slice.call(body.rows).reverse().forEach(function (r) { body.appendChild(r); });
  });
  // Hubs: the first 10 of the table, the rest behind a button.
  var HUBS = { pt: ['Mostrar os {n} hubs', 'Mostrar só os 10 primeiros'], en: ['Show all {n} hubs', 'Show only the first 10'] };
  document.querySelectorAll('#hubs [data-lang]').forEach(function (box) {
    var table = box.querySelector('table'), n = table ? table.querySelectorAll('tr').length - 1 : 0;
    if (n <= 10) return;
    var txt = HUBS[box.getAttribute('data-lang')] || HUBS.pt;
    var btn = el('button', { class: 'btn sm', type: 'button', 'aria-expanded': 'false', onclick: function () {
      var cut = table.classList.toggle('cut');
      btn.textContent = cut ? txt[0].replace('{n}', n) : txt[1];
      btn.setAttribute('aria-expanded', String(!cut));
    } }, txt[0].replace('{n}', n));
    table.classList.add('cut');
    box.appendChild(btn);
  });


  // ---- Novidades: the last 24 h (data/changes.json, scripts/network_24h.py) ----
  N.addStrings({
    dWin: 'Das {a} às {b}. Conta o saldo de cada tomada: a que avariou e voltou a funcionar no mesmo período não aparece.',
    dLate: 'Esta lista tem {h} h de atraso: a próxima atualização ainda não chegou.',
    dGap: 'O arquivo esteve {m} min sem ler o NAP neste período: pode faltar alguma mudança.',
    dQuiet: 'Nenhum local nem tomada entrou ou saiu da rede neste período.',
    t_down: 'tomadas avariaram', t_up: 'tomadas voltaram a funcionar', t_sitesAdd: 'locais novos', t_sitesRem: 'locais saíram',
    t_ptsAdd: 'tomadas novas', t_ptsRem: 'tomadas retiradas', t_op: 'locais mudaram de operador', t_kw: 'tomadas mudaram de potência', t_fee: 'locais mudaram de taxa',
    g_down: 'Tomadas que avariaram', g_up: 'Tomadas que voltaram a funcionar', g_sitesAdd: 'Locais novos', g_sitesRem: 'Locais que saíram da rede',
    g_ptsAdd: 'Tomadas novas em locais que já existiam', g_ptsRem: 'Tomadas retiradas de locais que continuam',
    g_op: 'Mudança de operador', g_kw: 'Mudança de potência', g_fee: 'Taxa do operador',
    nSock: '{n} tomada', nSocks: '{n} tomadas', upTo: 'até {kw} kW', at: '{t}', before: 'antes', now: 'agora', noFee: 'sem taxa',
    f_pricePerDeliveryUnit: '{v} €/kWh', f_pricePerChargingTime: '{v} €/min', f_flatRate: '{v} € por carregamento', f_other: '{v} €',
    more: 'Mostrar os {n} locais', t_down1: 'tomada avariou', t_up1: 'tomada voltou a funcionar', t_sitesAdd1: 'local novo', t_sitesRem1: 'local saiu',
    t_ptsAdd1: 'tomada nova', t_ptsRem1: 'tomada retirada', t_op1: 'local mudou de operador', t_kw1: 'tomada mudou de potência', t_fee1: 'local mudou de taxa', less: 'Mostrar só os primeiros', findIt: 'Ver {s} em Procurar'
  }, {
    dWin: 'From {a} to {b}. Counts each socket\'s net change: one that broke and came back within the period is left out.',
    dLate: 'This list is {h} h behind: the next update has not arrived yet.',
    dGap: 'The archive went {m} min without reading the NAP in this period: some changes may be missing.',
    dQuiet: 'No site or socket joined or left the network in this period.',
    t_down: 'sockets went out of order', t_up: 'sockets back in service', t_sitesAdd: 'new sites', t_sitesRem: 'sites left',
    t_ptsAdd: 'new sockets', t_ptsRem: 'sockets removed', t_op: 'sites changed operator', t_kw: 'sockets changed power', t_fee: 'sites changed fee',
    g_down: 'Sockets that went out of order', g_up: 'Sockets back in service', g_sitesAdd: 'New sites', g_sitesRem: 'Sites that left the network',
    g_ptsAdd: 'New sockets at existing sites', g_ptsRem: 'Sockets removed from sites that remain',
    g_op: 'Operator change', g_kw: 'Power change', g_fee: 'Operator fee',
    nSock: '{n} socket', nSocks: '{n} sockets', upTo: 'up to {kw} kW', at: '{t}', before: 'before', now: 'now', noFee: 'no fee',
    f_pricePerDeliveryUnit: '{v} €/kWh', f_pricePerChargingTime: '{v} €/min', f_flatRate: '{v} € per session', f_other: '{v} €',
    more: 'Show all {n} sites', t_down1: 'socket went out of order', t_up1: 'socket back in service', t_sitesAdd1: 'new site', t_sitesRem1: 'site left',
    t_ptsAdd1: 'new socket', t_ptsRem1: 'socket removed', t_op1: 'site changed operator', t_kw1: 'socket changed power', t_fee1: 'site changed fee', less: 'Show only the first', findIt: 'See {s} in Find'
  });
  var C = null, DAY_CUT = 8, DAY_LATE_H = 6;
  // [key in changes.json, label key, status shape for the mark, sign]
  var GROUPS = [['down', 'down', 'outOfOrder', ''], ['up', 'up', 'available', ''],
    ['sites_added', 'sitesAdd', 'charging', '+'], ['sites_removed', 'sitesRem', 'removed', '−'],
    ['points_added', 'ptsAdd', 'charging', '+'], ['points_removed', 'ptsRem', 'removed', '−'],
    ['op_changes', 'op', 'unknown', ''], ['power_changes', 'kw', 'unknown', ''], ['fees', 'fee', 'unknown', '']];
  var socks = function (n) { return t(n === 1 ? 'nSock' : 'nSocks', { n: N.nf(n) }); };
  var kw = function (v) { return N.nf(v, 1) + ' kW'; };
  function fees(list) {
    if (!list || !list.length) return t('noFee');
    return list.map(function (f) { return t('f_' + f.policy, { v: N.eur(f.eur) }); }).join(' + ');
  }
  function count(k) {
    var L = C[k] || [];
    if (k === 'down' || k === 'up' || /^points_|^sites_/.test(k)) return L.reduce(function (a, x) { return a + (x.n || 0); }, 0);
    return L.length;
  }
  function detail(k, x) {
    if (k === 'down' || k === 'up') return [socks(x.n), ', ', t('at', { t: N.when(Date.parse(x.t)) })];
    if (/^sites_|^points_/.test(k)) return [socks(x.n), x.kw ? ', ' + t('upTo', { kw: N.nf(x.kw, 1) }) : ''];
    if (k === 'op_changes') return [x.from, ' → ', el('b', null, x.to)];
    if (k === 'power_changes') return [x.point, ': ', kw(x.from), ' → ', el('b', null, kw(x.to))];
    if (k === 'fees') return [socks(x.n), ': ', t('before'), ' ', fees(x.from), '; ', t('now'), ' ', el('b', null, fees(x.to))];
    return null;
  }
  function row(k, x) {
    var where = [x.city, x.op].filter(Boolean).join(', ');
    return el('li', null,
      el('a', { href: 'index.html?q=' + encodeURIComponent(x.site), title: t('findIt', { s: x.site }) }, x.name && x.name !== x.site ? x.name : x.site),
      where ? el('span', { class: 'where' }, where) : null,
      el('span', { class: 'what' }, detail(k, x)));
  }
  function renderDay() {
    var box = $('day');
    if (!box || !C || !C.to) return;
    var a = Date.parse(C.from), b = Date.parse(C.to);
    if (!isFinite(a) || !isFinite(b)) return;
    N.clear(box).hidden = false;
    box.appendChild(el('h3', null, t('dTitle')));
    box.appendChild(el('p', { class: 'muted' }, t('dWin', { a: N.when(a), b: N.when(b) })));
    var late = (Date.now() - b) / 3600000;
    if (late > DAY_LATE_H) box.appendChild(el('p', { class: 'note' }, t('dLate', { h: N.nf(late) })));
    if (C.gap_min > 30) box.appendChild(el('p', { class: 'note' }, t('dGap', { m: N.nf(C.gap_min) })));
    var shown = GROUPS.filter(function (g) { return (C[g[0]] || []).length; });
    box.appendChild(el('ul', { class: 'tally' }, shown.map(function (g) {
      return el('li', null, el('a', { href: '#d-' + g[1], onclick: function (e) {
        e.preventDefault(); var s = $('d-' + g[1]); if (s) { s.scrollIntoView(); s.querySelector('h4').focus(); } } },
        el('span', { class: 'dot', 'data-s': g[2], 'aria-hidden': 'true' }), el('b', null, g[3] + N.nf(count(g[0]))), ' ', t('t_' + g[1] + (count(g[0]) === 1 ? '1' : ''))));
    })));
    if (!['sites_added', 'sites_removed', 'points_added', 'points_removed'].some(function (k) { return (C[k] || []).length; }))
      box.appendChild(el('p', { class: 'muted' }, t('dQuiet')));
    var grid = el('div', { class: 'dgrid' });
    shown.forEach(function (g) {
      var L = C[g[0]], ul = el('ul', { class: 'rows' }, L.map(function (x) { return row(g[0], x); }));
      var sec = el('div', { class: 'dgroup', id: 'd-' + g[1] }, el('h4', { tabindex: '-1' },
        el('span', { class: 'dot', 'data-s': g[2], 'aria-hidden': 'true' }), t('g_' + g[1]), ' ', el('span', { class: 'muted' }, N.nf(count(g[0])))), ul);
      if (L.length > DAY_CUT) {
        ul.classList.add('cut');
        var btn = el('button', { class: 'btn sm', type: 'button', 'aria-expanded': 'false', onclick: function () {
          var cut = ul.classList.toggle('cut');
          btn.textContent = cut ? t('more', { n: N.nf(L.length) }) : t('less');
          btn.setAttribute('aria-expanded', String(!cut));
        } }, t('more', { n: N.nf(L.length) }));
        sec.appendChild(btn);
      }
      grid.appendChild(sec);
    });
    box.appendChild(grid);
  }
  N.addStrings({ dTitle: 'Nas últimas 24 horas' }, { dTitle: 'In the last 24 hours' });

  N.initChrome();
  N.onLang(render);
  N.onLang(renderDay);
  N.load('changes').then(function (c) { C = c; renderDay(); }).catch(function () {});
  N.load('stats').then(function (d) {
    D = d; render();
    // Live status needs the per-socket list (280 KB gzipped): fetched after the page is readable.
    return N.load('points').then(function (r) { return N.fetchLive(r.points).then(function (res) { liveRes = res; if (res && !res.stale) recompute(r.points); render(); }); });
  }).catch(function () { $('live').textContent = t('loadFail'); });
})();
