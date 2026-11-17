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
    cPriceOp: 'Taxa média por kWh, por operador (€/kWh)', cStatusPw: 'Estado por classe de potência', cPriceStats: 'Componentes da taxa do operador', cPriceKinds: 'Preço por kWh, por tipo de preço', colKind: 'Tipo',
    kindsNote: 'Não compares entre linhas: a taxa do operador não inclui a energia, o preço sem contrato e o de fora da MOBI.E incluem, e no que só o NAP publica não se sabe.',
    colWhat: 'Componente', colN: 'tomadas', colMean: 'média', colMax: 'máximo', pEnergy: 'Por energia (€/kWh)', pTime: 'Por tempo (€/min)',
    pFlat: 'Fixa por carregamento (€)', pSem: 'Valor único fora da MOBI.E (*)', power: 'Classe de potência', value: 'Valor', sAll: 'Tudo',
    sessH: 'Quanto custa uma sessão de {k} kWh, por escalão',
    sessLead: 'Mediana das tomadas de cada escalão, contando as que cobram 0 €, sem IVA. Ao minuto, quanto mais devagar o carro carrega, mais paga pela mesma energia: por isso vai uma coluna por potência do carro.',
    sessAc: 'AC: carro a carregar a…', sessDc: 'DC: carro a carregar, em média, a…', sessCar: '{kw} kW', sessMin0: 'ao minuto desde o início', sessMinL: 'ao minuto só ao fim de um tempo',
    sessCap: 'A potência é a menor entre a do carro e a da tomada (a que o NAP declara). Escalões do NAP, separados em AC e DC pela ficha.',
    sessDcNote: 'No DC é uma potência média constante: a curva real do carro desce à medida que a bateria enche, por isso o tempo, e a parte ao minuto, são uma aproximação.',
    sessOut: '{n} tomadas ficam de fora: a ficha não bate com a classe de potência ou o NAP não a declara.',
    sessAc0: 'AC abaixo de 22 kW', sessAc1: 'AC 22 kW ou mais', sessDc1: 'DC 22–50 kW', sessDc2: 'DC 50–150 kW', sessDc3: 'DC 150–350 kW', sessDc4: 'DC 350 kW ou mais'
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
    cPriceOp: 'Mean fee per kWh, by operator (€/kWh)', cStatusPw: 'Status by power class', cPriceStats: 'Operator fee components', cPriceKinds: 'Price per kWh, by kind of price', colKind: 'Kind',
    kindsNote: 'Do not compare across rows: the operator fee does not include energy, the no-contract price and the one outside MOBI.E do, and for what only the NAP publishes nobody knows.',
    colWhat: 'Component', colN: 'sockets', colMean: 'mean', colMax: 'max', pEnergy: 'Per energy (€/kWh)', pTime: 'Per time (€/min)',
    pFlat: 'Flat per session (€)', pSem: 'Single value outside MOBI.E (*)', power: 'Power class', value: 'Value', sAll: 'All',
    sessH: 'What a {k} kWh session costs, by power class',
    sessLead: 'Median of the sockets in each class, counting those that charge €0, without VAT. Per minute, the slower the car charges, the more it pays for the same energy: hence one column per car power.',
    sessAc: 'AC: car charging at…', sessDc: 'DC: car charging, on average, at…', sessCar: '{kw} kW', sessMin0: 'per minute from the start', sessMinL: 'per minute only after a while',
    sessCap: 'The power is the lower of the car\'s and the socket\'s (as declared in the NAP). NAP power classes, split into AC and DC by plug.',
    sessDcNote: 'On DC this is a constant average power: the car\'s real curve drops as the battery fills, so the time, and the per-minute part, are an approximation.',
    sessOut: '{n} sockets are left out: the plug does not match the power class, or the NAP declares none.',
    sessAc0: 'AC below 22 kW', sessAc1: 'AC 22 kW or more', sessDc1: 'DC 22–50 kW', sessDc2: 'DC 50–150 kW', sessDc3: 'DC 150–350 kW', sessDc4: 'DC 350 kW or more'
  });
  var D = null, liveRes = null, PTS = null, sessKind = 'opc';
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
      el('tbody', null, [['pEnergy', ps.energy], ['pTime', ps.time], ['pFlat', ps.flat], ps.kinds ? null : ['pSem', ps.sem_ceme]].filter(function (r) { return r && r[1]; }).map(function (r) {
        return el('tr', null, el('th', { scope: 'row', class: 'l' }, t(r[0])), el('td', null, N.nf(r[1].n)), el('td', null, N.eur(r[1].mean)), el('td', null, N.eur(r[1].max))); }))));
    // One row per kind of price (scripts/price_kinds.py): each has its own mean, never a shared one.
    if (ps.kinds) {
      N.add($('cPriceStats'), [el('table', { class: 'kinds' }, el('caption', null, t('cPriceKinds')),
        el('thead', null, el('tr', null, ['colKind', 'colN', 'colMean', 'colMax'].map(function (k) { return el('th', { scope: 'col' }, t(k)); }))),
        el('tbody', null, N.PRICE_KINDS.filter(function (k) { return ps.kinds[k] && ps.kinds[k].kwh_n; }).map(function (k) {
          var v = ps.kinds[k];
          return el('tr', null, el('th', { scope: 'row', class: 'l' }, t('pk_' + k)), el('td', null, N.nf(v.kwh_n)), el('td', null, N.eur(v.mean)), el('td', null, N.eur(v.max))); }))),
        el('p', { class: 'muted small' }, t('kindsNote'))]);
    }
    sessionCard();
    fastCard();
    growthCard();
    cardPayCard();
    N.liveNote($('live'), liveRes, D.snapshot);
  }

  // What a reference session costs per power class (N.sessionCost), one kind of price at a time:
  // the operator fee and the no-contract price never share a table. Rows are the NAP's power classes
  // (as every Rede chart), split into AC and DC by plug; the socket's power is the NAP's too.
  var SESS_KWH = 20;
  var SESS = {
    AC: { cars: [3.7, 7.4, 11], rows: [['AC slow (<22kW)', 'sessAc0'], ['AC/DC 22-50kW', 'sessAc1']] },
    DC: { cars: [25, 50, 100], rows: [['AC/DC 22-50kW', 'sessDc1'], ['DC fast 50-150kW', 'sessDc2'], ['DC ultra 150-350kW', 'sessDc3'], ['DC ultra (>=350kW)', 'sessDc4']] }
  };
  function current(p) { return /CCS|CHAdeMO/i.test(p.connectors || '') ? 'DC' : p.connectors ? 'AC' : null; }
  function napKw(p) { return p.kw_src === 'osm' && p.nap_kw != null ? p.nap_kw : p.kw; }
  function median(xs) {
    if (!xs.length) return null;
    xs.sort(function (a, b) { return a - b; });
    var m = xs.length >> 1;
    return xs.length % 2 ? xs[m] : (xs[m - 1] + xs[m]) / 2;
  }
  // 'start' when a €/min tier above 0 runs from the first minute (a slower car pays more for the same
  // energy), 'later' when every such tier starts after a while (a fee for staying plugged in), else null.
  function perMinute(v) {
    var pos = (v.tiers && v.tiers.length ? v.tiers : [{ eur: v.min, from: 0 }]).map(function (x) {
      return typeof x === 'number' ? { eur: x, from: 0 } : x; }).filter(function (x) { return x && x.eur > 0; });
    return !pos.length ? null : pos.some(function (x) { return !x.from; }) ? 'start' : 'later';
  }
  function sessionCard() {
    var box = $('cSession');
    if (!box) return;
    N.clear(box);
    box.hidden = !PTS;   // the per-socket list comes after stats.json
    if (!PTS) return;
    var cells = {}, out = 0, counts = { opc: 0, adhoc: 0 };
    PTS.forEach(function (p) {
      var pk = N.prices(p), cur = current(p), kw = napKw(p), key = cur + '|' + p.pw_class;
      ['opc', 'adhoc'].forEach(function (k) { if (pk[k]) counts[k]++; });
      var v = pk[sessKind];
      if (!v || N.sessionCost(v, SESS_KWH, 1) == null) return;
      var row = cur && SESS[cur].rows.some(function (r) { return r[0] === p.pw_class; });
      if (!row || !(kw > 0)) { out++; return; }
      var c = cells[key] || (cells[key] = { n: 0, start: 0, later: 0, costs: SESS[cur].cars.map(function () { return []; }) });
      c.n++;
      var pm = perMinute(v);
      if (pm) c[pm]++;
      SESS[cur].cars.forEach(function (car, i) { c.costs[i].push(N.sessionCost(v, SESS_KWH, Math.min(car, kw))); });
    });
    box.appendChild(el('h3', null, t('sessH', { k: N.nf(SESS_KWH) })));
    box.appendChild(el('p', { class: 'muted small' }, t('sessLead')));
    box.appendChild(el('div', { class: 'seg', role: 'group', 'aria-label': t('colKind') }, ['opc', 'adhoc'].map(function (k) {
      return el('button', { class: 'btn sm', type: 'button', 'aria-pressed': String(sessKind === k), onclick: function () { sessKind = k; sessionCard(); } },
        t('pk_' + k), el('span', { class: 'muted' }, ' ' + N.nf(counts[k])));
    })));
    ['AC', 'DC'].forEach(function (cur) {
      var S = SESS[cur], rows = S.rows.filter(function (r) { return cells[cur + '|' + r[0]]; });
      if (!rows.length) return;
      box.appendChild(el('div', { class: 'scroll', tabindex: '0', role: 'group', 'aria-label': t(cur === 'AC' ? 'sessAc' : 'sessDc') }, el('table', { class: 'sess' },
        el('caption', null, t(cur === 'AC' ? 'sessAc' : 'sessDc')),
        el('thead', null, el('tr', null, el('th', { scope: 'col' }, t('power')), el('th', { scope: 'col' }, t('colN')), el('th', { scope: 'col' }, t('sessMin0')), el('th', { scope: 'col' }, t('sessMinL')),
          S.cars.map(function (car) { return el('th', { scope: 'col' }, t('sessCar', { kw: N.nf(car, 1) })); }))),
        el('tbody', null, rows.map(function (r) {
          var c = cells[cur + '|' + r[0]];
          return el('tr', null, el('th', { scope: 'row', class: 'l' }, t(r[1])), el('td', null, N.nf(c.n)), el('td', null, N.nf(100 * c.start / c.n) + ' %'), el('td', null, N.nf(100 * c.later / c.n) + ' %'),
            c.costs.map(function (xs) { var m = median(xs); return el('td', null, m == null ? '—' : N.eur(m) + ' €'); }));
        })))));
    });
    box.appendChild(el('p', { class: 'muted small' }, t('sessCap') + ' ' + t('sessDcNote')));
    if (out) box.appendChild(el('p', { class: 'muted small' }, t('sessOut', { n: N.nf(out) })));
  }

  // ---- Concelhos (CAOP) and bank cards at fast chargers: stats.json `territory`, `card_pay`
  // (scripts/territory_stats.py). Weekly numbers, never recounted with the live status.
  N.addStrings({
    sConc: 'Concelhos', hConc: 'Os concelhos',
    concNote: 'Concelho onde o posto fica, pelas coordenadas que o operador publica e os limites oficiais (CAOP, Direção-Geral do Território). Pode diferir do concelho escrito no NAP, que é o do gráfico dos 15 concelhos.',
    fastH: 'Concelhos sem posto de 50 kW ou mais',
    fastLead: 'Dos {n} concelhos, {s} têm pelo menos um local de carregamento no NAP e {f} têm pelo menos um posto de 50 kW ou mais. Nos {x} da lista só há carregamento mais lento.',
    fastNone: 'Concelhos sem nenhum local de carregamento no NAP', fastDef: 'Posto de 50 kW ou mais: uma tomada com essa potência, tal como o NAP a declara, esteja ou não a funcionar.',
    colRegion: 'Região', colConc: 'Concelho', colDist: 'Distrito ou ilha', colConcN: 'concelhos', colWithSite: 'com algum local', colWithFast: 'com 50 kW ou mais', colSitesSlow: 'locais, todos abaixo de 50 kW',
    growthH: 'Locais por concelho, há um ano e agora',
    growthLead: 'De {a} a {b}, sem as entradas em bloco da nota em baixo, a rede passou de {n0} para {n1} locais ({d}) e de {p0} para {p1} tomadas ({dp}).',
    growthCount: 'Em {what}, {g} concelhos ganharam, {s} ficaram iguais e {l} perderam.', gBy: 'Contar', gByP: 'tomadas', gByN: 'locais',
    growthMerge: 'Um operador pode juntar vários postos num só local: em Lisboa, a Maksu está a passar os seus para a Telpark, do mesmo grupo, com menos locais e mais tomadas. Por isso a contagem por tomadas vem primeiro.',
    growthBulk: 'Ficam de fora os {n} locais, ainda publicados hoje, que entraram no NAP de uma vez, no dia em que o operador os começou a publicar, e não no dia em que abriram: {list}.',
    growthBulkItem: '{op} ({n}, a {d})',
    growthHow: 'Conta os locais publicados no NAP em cada um dos dois dias, a partir do arquivo AmpereArchive. Um local que mudou de código conta como o mesmo.',
    growthUnplaced: '{n} locais com coordenadas fora de qualquer concelho (no mar, fora do país) ficam de fora.',
    gAbs: 'Maior subida', gPct: 'Maior subida em %', gDown: 'Desceram', gPctNote: 'Só concelhos com {m} ou mais {what} há um ano.',
    colYearAgo: 'há um ano', colNow: 'agora', colDiff: 'diferença', colPct: '%',
    cardH: 'Pagar com cartão bancário nos postos de 50 kW ou mais',
    cardLead: 'O regulamento europeu AFIR obriga os postos de 50 kW ou mais instalados desde 13 de abril de 2024 a aceitar cartão bancário, com leitor ou sem contacto, e os mais antigos na rede rodoviária transeuropeia (RTE-T) a partir de 1 de janeiro de 2027. O NAP não diz quando cada posto foi instalado nem se fica na RTE-T: estes números não dizem quem cumpre.',
    cardSrc: 'Fonte', cardYes: 'aceita', cardNo: 'não aceita', cardUnk: 'não diz', cardNap: 'NAP (o operador)', cardOsm: 'OpenStreetMap (a comunidade)',
    cardSites: '{n} locais com pelo menos um posto de 50 kW ou mais.',
    cardDisagree: 'As duas fontes discordam em {a} locais: em {b} o NAP diz que aceita e o OpenStreetMap que não, em {c} é ao contrário.',
    cardOpsH: 'Por operador, os {n} com mais locais de 50 kW ou mais', colOp: 'Operador', colFast: 'locais', colNapYes: 'NAP: aceita', colOsmYes: 'OSM: aceita', colOsmNo: 'OSM: não aceita',
    cardHow: 'No NAP conta o cartão de crédito ou de débito (creditCard, debitCard) nos meios de autenticação do local; nfc e pinpad sozinhos não dizem que o cartão é bancário. No OpenStreetMap, a etiqueta payment:cards.'
  }, {
    sConc: 'Municipalities', hConc: 'Municipalities',
    concNote: 'The municipality the charger is in, from the coordinates the operator publishes and the official boundaries (CAOP, Direção-Geral do Território). It can differ from the town written in the NAP, which is what the 15-municipality chart uses.',
    fastH: 'Municipalities without a 50 kW or faster charger',
    fastLead: 'Of the {n} municipalities, {s} have at least one charging site in the NAP and {f} have at least one charger of 50 kW or more. The {x} listed have only slower charging.',
    fastNone: 'Municipalities with no charging site in the NAP', fastDef: 'Charger of 50 kW or more: a socket with that power as the NAP declares it, working or not.',
    colRegion: 'Region', colConc: 'Municipality', colDist: 'District or island', colConcN: 'municipalities', colWithSite: 'with any site', colWithFast: 'with 50 kW or more', colSitesSlow: 'sites, all below 50 kW',
    growthH: 'Sites per municipality, a year ago and now',
    growthLead: 'From {a} to {b}, leaving out the bulk entries in the note below, the network went from {n0} to {n1} sites ({d}) and from {p0} to {p1} sockets ({dp}).',
    growthCount: 'In {what}, {g} municipalities gained, {s} stayed the same and {l} lost.', gBy: 'Count', gByP: 'sockets', gByN: 'sites',
    growthMerge: 'An operator can merge several chargers into one site: in Lisbon, Maksu is handing its chargers to Telpark, from the same group, with fewer sites and more sockets. That is why the socket count comes first.',
    growthBulk: 'Left out: the {n} sites, still published today, that entered the NAP all at once, on the day the operator started publishing them rather than the day they opened: {list}.',
    growthBulkItem: '{op} ({n}, on {d})',
    growthHow: 'Counts the sites published in the NAP on each of the two days, from the AmpereArchive. A site that changed code counts as the same site.',
    growthUnplaced: '{n} sites whose coordinates fall outside every municipality (at sea, abroad) are left out.',
    gAbs: 'Largest rise', gPct: 'Largest rise in %', gDown: 'Fell', gPctNote: 'Only municipalities with {m} or more {what} a year ago.',
    colYearAgo: 'a year ago', colNow: 'now', colDiff: 'change', colPct: '%',
    cardH: 'Paying by bank card at chargers of 50 kW or more',
    cardLead: 'The EU AFIR regulation requires chargers of 50 kW or more installed since 13 April 2024 to take bank cards, with a reader or contactless, and older ones on the trans-European road network (TEN-T) from 1 January 2027. The NAP does not say when each charger was installed or whether it is on the TEN-T: these numbers do not say who complies.',
    cardSrc: 'Source', cardYes: 'accepts', cardNo: 'does not', cardUnk: 'does not say', cardNap: 'NAP (the operator)', cardOsm: 'OpenStreetMap (the community)',
    cardSites: '{n} sites with at least one charger of 50 kW or more.',
    cardDisagree: 'The two sources disagree on {a} sites: on {b} the NAP says cards work and OpenStreetMap says they do not, on {c} the other way round.',
    cardOpsH: 'By operator, the {n} with most sites of 50 kW or more', colOp: 'Operator', colFast: 'sites', colNapYes: 'NAP: accepts', colOsmYes: 'OSM: accepts', colOsmNo: 'OSM: does not',
    cardHow: 'In the NAP, a credit or debit card (creditCard, debitCard) among the site\'s authentication methods; nfc and pinpad alone do not say the card is a bank card. In OpenStreetMap, the payment:cards tag.'
  });
  var growthView = 'abs', growthBy = 'p', GROWTH_TOP = 15, GROWTH_PCT_MIN = 10;
  var cols = function (keys) { return el('thead', null, el('tr', null, keys.map(function (k) { return el('th', { scope: 'col' }, t(k)); }))); };
  var pctOf = function (a, n) { return n ? N.nf(100 * a / n, 1) + ' %' : '—'; };
  var signed = function (v, d) { return (v > 0 ? '+' : v < 0 ? '−' : '') + N.nf(Math.abs(v), d); };
  var day = function (iso) { return new Date(iso).toLocaleDateString(N.lang() === 'pt' ? 'pt-PT' : 'en-GB', { day: '2-digit', month: '2-digit', year: 'numeric' }); };
  var wrap = function (label, table) { return el('div', { class: 'scroll', tabindex: '0', role: 'group', 'aria-label': label }, table); };

  function fastCard() {
    var box = $('cFast'), T = D.territory;
    box.hidden = !T;
    if (!T) return;
    N.clear(box).appendChild(el('h3', null, t('fastH')));
    box.appendChild(el('p', null, t('fastLead', { n: N.nf(T.n), s: N.nf(T.with_site), f: N.nf(T.with_fast), x: N.nf(T.no_fast.length) })));
    box.appendChild(wrap(t('colRegion'), el('table', { class: 'conc' }, cols(['colRegion', 'colConcN', 'colWithSite', 'colWithFast']),
      el('tbody', null, ['mainland', 'madeira', 'azores'].filter(function (r) { return T.by_region[r]; }).map(function (r) {
        var b = T.by_region[r];
        return el('tr', null, el('th', { scope: 'row', class: 'l' }, t('rg_' + r)), el('td', null, N.nf(b.n)), el('td', null, N.nf(b.with_site)), el('td', null, N.nf(b.with_fast)));
      })))));
    if (T.no_fast.length) {
      box.appendChild(wrap(t('fastH'), el('table', { class: 'conc' }, el('caption', null, t('fastH')), cols(['colConc', 'colDist', 'colSitesSlow']),
        el('tbody', null, T.no_fast.map(function (r) {
          return el('tr', null, el('th', { scope: 'row', class: 'l' }, r[0]), el('td', { class: 'l' }, r[1]), el('td', null, N.nf(r[3])));
        })))));
    }
    if (T.none.length) {
      box.appendChild(wrap(t('fastNone'), el('table', { class: 'conc' }, el('caption', null, t('fastNone')), cols(['colConc', 'colDist']),
        el('tbody', null, T.none.map(function (r) {
          return el('tr', null, el('th', { scope: 'row', class: 'l' }, r[0]), el('td', { class: 'l' }, r[1]));
        })))));
    }
    box.appendChild(el('p', { class: 'muted small' }, t('fastDef')));
  }

  function growthCard() {
    var box = $('cGrowth'), G = D.territory && D.territory.growth;
    box.hidden = !G;
    if (!G) return;
    var hasP = G.p0 != null, by = hasP ? growthBy : 'n', i0 = by === 'p' ? 6 : 3;
    var rows = G.rows.map(function (r) { return { c: r[0], d: r[1], n0: r[i0], n1: r[i0 + 1], diff: r[i0 + 1] - r[i0] }; });
    var up = rows.filter(function (r) { return r.diff > 0; }).length, down = rows.filter(function (r) { return r.diff < 0; }).length;
    var change = function (a, b) { return signed(b - a) + (a ? ', ' + signed(100 * (b - a) / a, 1) + ' %' : ''); };
    var what = t(by === 'p' ? 'gByP' : 'gByN');
    N.clear(box).appendChild(el('h3', null, t('growthH')));
    box.appendChild(el('p', null, t('growthLead', { a: day(G.t0), b: day(G.t1), n0: N.nf(G.n0), n1: N.nf(G.n1), d: change(G.n0, G.n1),
      p0: N.nf(G.p0), p1: N.nf(G.p1), dp: hasP ? change(G.p0, G.p1) : '—' })));
    if (hasP) box.appendChild(el('div', { class: 'seg', role: 'group', 'aria-label': t('gBy') }, [el('span', { class: 'muted small' }, t('gBy') + ':')].concat(['p', 'n'].map(function (v) {
      return el('button', { class: 'btn sm', type: 'button', 'aria-pressed': String(by === v), onclick: function () { growthBy = v; growthCard(); } }, t(v === 'p' ? 'gByP' : 'gByN'));
    }))));
    box.appendChild(el('p', null, t('growthCount', { what: what, g: N.nf(up), s: N.nf(rows.length - up - down), l: N.nf(down) })));
    var views = { abs: function (a, b) { return b.diff - a.diff || b.n1 - a.n1; },
      pct: function (a, b) { return b.diff / b.n0 - a.diff / a.n0 || b.diff - a.diff; },
      down: function (a, b) { return a.diff - b.diff || b.n0 - a.n0; } };
    var pick = rows.filter(function (r) {
      return growthView === 'down' ? r.diff < 0 : growthView === 'pct' ? r.n0 >= GROWTH_PCT_MIN && r.diff > 0 : r.diff > 0; })
      .sort(views[growthView]).slice(0, GROWTH_TOP);
    box.appendChild(el('div', { class: 'seg', role: 'group', 'aria-label': t('growthH') }, [['abs', 'gAbs'], ['pct', 'gPct'], ['down', 'gDown']].map(function (v) {
      return el('button', { class: 'btn sm', type: 'button', 'aria-pressed': String(growthView === v[0]), onclick: function () { growthView = v[0]; growthCard(); } }, t(v[1]));
    })));
    box.appendChild(wrap(t('growthH'), el('table', { class: 'conc' }, cols(['colConc', 'colDist', 'colYearAgo', 'colNow', 'colDiff', 'colPct']),
      el('tbody', null, pick.map(function (r) {
        return el('tr', null, el('th', { scope: 'row', class: 'l' }, r.c), el('td', { class: 'l' }, r.d), el('td', null, N.nf(r.n0)), el('td', null, N.nf(r.n1)),
          el('td', null, signed(r.diff)), el('td', null, r.n0 ? signed(100 * r.diff / r.n0, 0) + ' %' : '—'));
      })))));
    if (growthView === 'pct') box.appendChild(el('p', { class: 'muted small' }, t('gPctNote', { m: N.nf(GROWTH_PCT_MIN), what: what })));
    var notes = [t('growthHow')].concat(hasP ? [t('growthMerge')] : []);
    if (G.bulk) notes.push(t('growthBulk', { n: N.nf(G.bulk), list: G.bulk_entries.map(function (b) {
      return t('growthBulkItem', { op: b.op || '—', n: N.nf(b.n), d: day(b.day + 'T12:00:00Z') }); }).join('; ') }));
    if (G.unplaced) notes.push(t('growthUnplaced', { n: N.nf(G.unplaced) }));
    box.appendChild(el('p', { class: 'muted small' }, notes.join(' ')));
  }

  function cardPayCard() {
    var box = $('cCardPay'), C = D.card_pay;
    box.hidden = !C;
    if (!C) return;
    N.clear(box).appendChild(el('h3', null, t('cardH')));
    box.appendChild(el('p', { class: 'muted small' }, t('cardLead')));
    box.appendChild(el('p', null, t('cardSites', { n: N.nf(C.n) })));
    var cell = function (v) { return el('td', null, N.nf(v), ' ', el('span', { class: 'muted' }, pctOf(v, C.n))); };
    var src = [['cardNap', C.nap, C.n - C.nap, null]];
    if (C.osm) src.push(['cardOsm', C.osm_yes, C.osm_no, C.osm_none]);
    box.appendChild(wrap(t('cardH'), el('table', { class: 'conc' }, cols(['cardSrc', 'cardYes', 'cardNo', 'cardUnk']),
      el('tbody', null, src.map(function (r) {
        return el('tr', null, el('th', { scope: 'row', class: 'l' }, t(r[0])), cell(r[1]), cell(r[2]), r[3] == null ? el('td', null, '—') : cell(r[3]));
      })))));
    if (C.osm) box.appendChild(el('p', null, t('cardDisagree', { a: N.nf(C.nap_only + C.osm_only), b: N.nf(C.nap_only), c: N.nf(C.osm_only) })));
    var opCols = ['colOp', 'colFast', 'colNapYes'].concat(C.osm ? ['colOsmYes', 'colOsmNo'] : []);
    box.appendChild(wrap(t('cardOpsH', { n: N.nf(C.ops.length) }), el('table', { class: 'conc' }, el('caption', null, t('cardOpsH', { n: N.nf(C.ops.length) })), cols(opCols),
      el('tbody', null, C.ops.map(function (o) {
        var td = function (v) { return el('td', null, N.nf(v), ' ', el('span', { class: 'muted' }, pctOf(v, o[1]))); };
        return el('tr', null, el('th', { scope: 'row', class: 'l' }, o[0]), el('td', null, N.nf(o[1])), td(o[2]), C.osm ? td(o[3]) : null, C.osm ? td(o[4]) : null);
      })))));
    box.appendChild(el('p', { class: 'muted small' }, t('cardHow')));
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
    return N.load('points').then(function (r) { PTS = r.points; return N.fetchLive(r.points).then(function (res) { liveRes = res; if (res && !res.stale) recompute(r.points); render(); }); });
  }).catch(function () { $('live').textContent = t('loadFail'); });
})();
