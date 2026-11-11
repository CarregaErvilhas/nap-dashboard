// "A rede em números": stat tiles and bar charts. Every chart is a real table
// (label, bar, value), so it reads the same with a screen reader or no CSS.
'use strict';
(function () {
  var N = window.NAP, el = N.el, t = N.t;
  N.addStrings({
    netH1: 'A rede em números', netLead: 'Quantos postos há, de quem são, que potência têm e quanto estão ocupados.',
    sections: 'Secções', sSummary: 'Resumo', sNews: 'Novidades', sNetwork: 'Postos', sOps: 'Operadores', sOcc: 'Ocupação', sPrice: 'Preços',
    sHist: 'Histórico', sHubs: 'Hubs', sFacts: 'Factos', hNews: 'Novidades da semana', hNetwork: 'Que postos há', hOps: 'Quem opera a rede',
    hOcc: 'Ocupação neste momento', occNote: 'Tomadas a carregar sobre as que estão livres ou a carregar.', hPrice: 'Taxa do operador',
    priceNote: 'É o que o operador do posto (OPC) cobra pelo uso, sem IVA. A energia é cobrada à parte pelo teu comercializador (CEME).',
    hHist: 'Histórico (AmpereArchive)', hHubs: 'Maiores hubs por potência total', hFacts: 'Factos sobre a rede',
    cStatus: 'Tomadas por estado', cPw: 'Tomadas por classe de potência', cConn: 'Fichas por tipo', cRegion: 'Locais por região',
    cCity: 'Os 15 concelhos com mais locais', cOpSites: 'Os 15 operadores com mais locais', cOpPts: 'Os 15 operadores com mais tomadas',
    cOccPw: 'Ocupação por classe de potência (%)', cOccOp: 'Ocupação por operador, os 15 maiores (%)',
    cPriceOp: 'Taxa média por kWh, por operador (€/kWh)', cStatusPw: 'Estado por classe de potência', cPriceStats: 'Componentes da taxa do operador',
    colWhat: 'Componente', colN: 'tomadas', colMean: 'média', colMax: 'máximo', pEnergy: 'Por energia (€/kWh)', pTime: 'Por tempo (€/min)',
    pFlat: 'Fixa por carregamento (€)', pSem: 'Valor único fora da MOBI.E (*)', power: 'Classe de potência', value: 'Valor'
  }, {
    netH1: 'The network in numbers', netLead: 'How many chargers there are, who runs them, how powerful and how busy they are.',
    sections: 'Sections', sSummary: 'Summary', sNews: 'News', sNetwork: 'Chargers', sOps: 'Operators', sOcc: 'Occupancy', sPrice: 'Prices',
    sHist: 'History', sHubs: 'Hubs', sFacts: 'Facts', hNews: 'This week\'s news', hNetwork: 'What chargers exist', hOps: 'Who runs the network',
    hOcc: 'Occupancy right now', occNote: 'Sockets charging over those free or charging.', hPrice: 'Operator fee',
    priceNote: 'What the charger operator (CPO) bills for use, without VAT. Energy is billed separately by your supplier (CEME).',
    hHist: 'History (AmpereArchive)', hHubs: 'Largest hubs by total power', hFacts: 'Facts about the network',
    cStatus: 'Sockets by status', cPw: 'Sockets by power class', cConn: 'Plugs by type', cRegion: 'Sites by region',
    cCity: 'The 15 municipalities with most sites', cOpSites: 'The 15 operators with most sites', cOpPts: 'The 15 operators with most sockets',
    cOccPw: 'Occupancy by power class (%)', cOccOp: 'Occupancy by operator, 15 largest (%)',
    cPriceOp: 'Mean fee per kWh, by operator (€/kWh)', cStatusPw: 'Status by power class', cPriceStats: 'Operator fee components',
    colWhat: 'Component', colN: 'sockets', colMean: 'mean', colMax: 'max', pEnergy: 'Per energy (€/kWh)', pTime: 'Per time (€/min)',
    pFlat: 'Flat per session (€)', pSem: 'Single value outside MOBI.E (*)', power: 'Power class', value: 'Value'
  });
  var D = null, liveRes = null;
  var $ = function (id) { return document.getElementById(id); };

  // rows: [[label, number|null, labelNode?]]
  function bars(id, title, rows, dec, suffix) {
    var max = Math.max.apply(null, rows.map(function (r) { return r[1] || 0; }).concat([0]));
    var tb = el('tbody', null, rows.map(function (r) {
      var fill = el('div', { class: 'fill' }); fill.style.width = (max ? 100 * (r[1] || 0) / max : 0) + '%';
      return el('tr', null, el('th', { scope: 'row' }, r[2] || r[0]), el('td', { class: 'b', 'aria-hidden': 'true' }, el('div', { class: 'track' }, fill)),
        el('td', null, r[1] == null ? '—' : N.nf(r[1], dec) + (suffix || '')));
    }));
    N.clear($(id)).appendChild(el('table', { class: 'bars' }, el('caption', null, t(title)),
      el('thead', { class: 'sr' }, el('tr', null, el('th', { scope: 'col' }, ''), el('td', null), el('th', { scope: 'col' }, t('value')))), tb));
  }
  var desc = function (o) { return Object.keys(o || {}).map(function (k) { return [k, o[k]]; }).sort(function (a, b) { return b[1] - a[1]; }); };

  function render() {
    if (!D) return;
    var ul = N.clear($('kpis'));
    (N.lang() === 'pt' ? D.kpis_pt : D.kpis).forEach(function (k) {
      ul.appendChild(el('li', null, el('span', { class: 't' }, k.t), el('span', { class: 'v' }, typeof k.v === 'number' ? N.nf(k.v) : k.v), el('span', { class: 's' }, k.s)));
    });
    bars('cStatus', 'cStatus', desc(D.status).map(function (r) { return [r[0], r[1], N.status(r[0])]; }));
    bars('cPw', 'cPw', N.PW.map(function (c) { return [N.pwLabel(c), D.pw[c] || 0]; }));
    bars('cConn', 'cConn', desc(D.conn));
    bars('cRegion', 'cRegion', desc(D.region).map(function (r) { return [t('rg_' + r[0]), r[1]]; }));
    bars('cCity', 'cCity', desc(D.city));
    bars('cOpSites', 'cOpSites', desc(D.op_sites));
    bars('cOpPts', 'cOpPts', desc(D.op_pts));
    bars('cOccPw', 'cOccPw', D.occ_pw.map(function (x) { return [N.pwLabel(x.c), x.occ]; }), 1, ' %');
    bars('cOccOp', 'cOccOp', D.occ_op.slice().sort(function (a, b) { return (b.occ || 0) - (a.occ || 0); }).map(function (x) { return [x.op, x.occ]; }), 1, ' %');
    bars('cPriceOp', 'cPriceOp', desc(D.price_op), 3);
    var sts = N.STATUSES.filter(function (s) { return D.status[s]; });
    N.clear($('cStatusPw')).appendChild(el('table', null, el('caption', null, t('cStatusPw')),
      el('thead', null, el('tr', null, el('th', { scope: 'col' }, t('power')), sts.map(function (s) { return el('th', { scope: 'col' }, t('st_' + s)); }))),
      el('tbody', null, N.PW.filter(function (c) { return D.status_pw[c]; }).map(function (c) {
        return el('tr', null, el('th', { scope: 'row', class: 'l' }, N.pwLabel(c)), sts.map(function (s) { return el('td', null, N.nf(D.status_pw[c][s] || 0)); })); }))));
    var ps = D.price_stats || {};
    N.clear($('cPriceStats')).appendChild(el('table', null, el('caption', null, t('cPriceStats')),
      el('thead', null, el('tr', null, ['colWhat', 'colN', 'colMean', 'colMax'].map(function (k) { return el('th', { scope: 'col' }, t(k)); }))),
      el('tbody', null, [['pEnergy', ps.energy], ['pTime', ps.time], ['pFlat', ps.flat], ['pSem', ps.sem_ceme]].filter(function (r) { return r[1]; }).map(function (r) {
        return el('tr', null, el('th', { scope: 'row', class: 'l' }, t(r[0])), el('td', null, N.nf(r[1].n)), el('td', null, N.nf(r[1].mean, 3)), el('td', null, N.nf(r[1].max, 3))); }))));
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

  N.initChrome();
  N.onLang(render);
  N.load('stats').then(function (d) {
    D = d; render();
    // Live status needs the per-socket list (280 KB gzipped): fetched after the page is readable.
    return N.load('points').then(function (r) { return N.fetchLive(r.points).then(function (res) { liveRes = res; if (res && !res.stale) recompute(r.points); render(); }); });
  }).catch(function () { $('live').textContent = t('loadFail'); });
})();
