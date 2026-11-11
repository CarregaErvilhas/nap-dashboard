// "Para operadores": the weekly agent's findings, one operator at a time.
// Report text is third-party-derived: rendered through N.md (text + <code>).
'use strict';
(function () {
  var N = window.NAP, el = N.el, t = N.t;
  N.addStrings({
    opsH1: 'O que os teus dados dizem no NAP',
    opsLead: 'Escolhe o operador para ver as anomalias encontradas esta semana nos dados que publica, com a regra de cada uma e o que afeta.',
    hPick: 'Anomalias por operador', pickLabel: 'Operador (código e nome)', pickAll: 'Todos: ver a tabela resumo',
    hChurn: 'Entradas, saídas e mudanças de operadores', hErrs: 'Erros reportáveis nos dados oficiais',
    errsNote: 'Problemas de toda a rede, para quem gere os dados (NAP, MOBI.E, DGEG). A lista completa por tomada está no errors.md.',
    errsLink: 'Ler o errors.md completo no GitHub',
    repNote: 'Relatório de {d}, feito por um agente automático sobre os dados estáticos do NAP. Impossível = viola a física ou a norma; suspeito = merece revisão. As anomalias são reportadas em português.',
    repNone: 'Sem relatório de anomalias nesta semana.', tSummary: 'Resumo por operador ({n} operadores)', cOp: 'Operador', cSites: 'locais', cPts: 'tomadas',
    cImp: 'impossíveis', cSus: 'suspeitos', cFind: 'anomalias', rule: 'Regra', affected: 'Afetados', none: 'Sem anomalias detalhadas para este operador.',
    evidence: 'Ver todas as evidências deste operador no GitHub', sumLine: '{s} locais, {p} tomadas: {i} entidades em categorias impossíveis e {u} em suspeitas.',
    sev_CRÍTICO: 'Crítico', sev_ALTO: 'Alto', sev_MÉDIO: 'Médio', sev_BAIXO: 'Baixo', back: 'Voltar à tabela resumo'
  }, {
    opsH1: 'What your data says on the NAP',
    opsLead: 'Pick the operator to see the anomalies found this week in the data it publishes, with the rule behind each one and what it affects.',
    hPick: 'Anomalies by operator', pickLabel: 'Operator (code and name)', pickAll: 'All: see the summary table',
    hChurn: 'Operators joining, leaving and changing', hErrs: 'Reportable errors in the official data',
    errsNote: 'Network-wide problems, for the data owners (NAP, MOBI.E, DGEG). The full per-socket list is in errors.md.',
    errsLink: 'Read the full errors.md on GitHub',
    repNote: 'Report of {d}, made by an automatic agent on the NAP static data. Impossible = breaks physics or the standard; suspect = worth a review. Findings are reported in Portuguese.',
    repNone: 'No anomaly report this week.', tSummary: 'Summary by operator ({n} operators)', cOp: 'Operator', cSites: 'sites', cPts: 'sockets',
    cImp: 'impossible', cSus: 'suspect', cFind: 'findings', rule: 'Rule', affected: 'Affected', none: 'No detailed findings for this operator.',
    evidence: 'See all evidence for this operator on GitHub', sumLine: '{s} sites, {p} sockets: {i} entities in impossible categories and {u} in suspect ones.',
    sev_CRÍTICO: 'Critical', sev_ALTO: 'High', sev_MÉDIO: 'Medium', sev_BAIXO: 'Low', back: 'Back to the summary table'
  });
  var R = null, sort = { k: 'imp', dir: -1 };
  var ORDER = ['CRÍTICO', 'ALTO', 'MÉDIO', 'BAIXO'];
  var $ = function (id) { return document.getElementById(id); };
  var sev = function (s) { return el('span', { class: 'sev', 'data-sev': s }, t('sev_' + s)); };

  function pick(id, focus) {
    $('opSel').value = id || '';
    try { history.replaceState(null, '', id ? '#opc-' + encodeURIComponent(id) : location.pathname + location.search); } catch (e) {}
    view();
    if (focus) $('opView').focus();
  }
  function table() {
    var cols = [['id', 'cOp'], ['sites', 'cSites'], ['points', 'cPts'], ['imp', 'cImp'], ['sus', 'cSus'], ['n', 'cFind']];
    var rows = R.opcs.map(function (o) { return Object.assign({ n: o.findings.length }, o); }).sort(function (a, b) {
      var x = a[sort.k], y = b[sort.k]; return (typeof x === 'string' ? x.localeCompare(y) : x - y) * sort.dir || b.sus - a.sus; });
    return el('div', { class: 'card' }, el('div', { class: 'scroll', tabindex: '0', role: 'group', 'aria-label': t('tSummary', { n: rows.length }) },
      el('table', null, el('caption', null, t('tSummary', { n: rows.length })),
        el('thead', null, el('tr', null, cols.map(function (c) {
          return el('th', { scope: 'col', 'aria-sort': sort.k === c[0] ? (sort.dir > 0 ? 'ascending' : 'descending') : null },
            el('button', { type: 'button', onclick: function () { sort = { k: c[0], dir: sort.k === c[0] ? -sort.dir : (c[0] === 'id' ? 1 : -1) }; view(); } }, t(c[1]))); }))),
        el('tbody', null, rows.map(function (o) {
          return el('tr', null, el('th', { scope: 'row', class: 'l' }, el('a', { href: '#opc-' + encodeURIComponent(o.id), onclick: function (e) { e.preventDefault(); pick(o.id, true); } }, o.id), ' ', o.name),
            el('td', null, N.nf(o.sites)), el('td', null, N.nf(o.points)), el('td', null, N.nf(o.imp)), el('td', null, N.nf(o.sus)), el('td', null, o.n)); })))));
  }
  function one(o) {
    var f = o.findings.slice().sort(function (a, b) { return ORDER.indexOf(a.sev) - ORDER.indexOf(b.sev); });
    return el('div', { class: 'card' },
      el('h3', null, o.id + ' ' + o.name),
      el('p', null, t('sumLine', { s: N.nf(o.sites), p: N.nf(o.points), i: N.nf(o.imp), u: N.nf(o.sus) })),
      f.length ? f.map(function (x) {
        return el('div', { class: 'finding', lang: 'pt' }, el('h4', null, sev(x.sev), el('span', null, N.md(x.title))),
          x.rule ? el('p', null, el('b', null, t('rule') + ': '), N.md(x.rule)) : null,
          x.affected ? el('p', null, el('b', null, t('affected') + ': '), N.md(x.affected)) : null);
      }) : el('p', { class: 'muted' }, t('none')),
      el('div', { class: 'actions' },
        el('a', { class: 'btn primary', href: R.url + '#opc-' + encodeURIComponent(o.id), rel: 'noopener', target: '_blank' }, t('evidence')),
        el('button', { class: 'btn', type: 'button', onclick: function () { pick('', true); } }, t('back'))));
  }
  function view() {
    if (!R) return;
    var note = $('repNote');
    if (!R.opcs.length) { note.textContent = t('repNone'); N.clear($('opView')); return; }
    note.textContent = t('repNote', { d: R.date || '?' });
    var sel = $('opSel'), cur = sel.value;
    if (sel.options.length < 2) R.opcs.slice().sort(function (a, b) { return a.id.localeCompare(b.id); }).forEach(function (o) {
      sel.appendChild(el('option', { value: o.id }, o.id + ' ' + o.name)); });
    sel.value = cur;
    var o = R.opcs.find(function (x) { return x.id === cur; });
    N.clear($('opView')).appendChild(o ? one(o) : table());
  }
  N.initChrome();
  N.onLang(view);
  $('opSel').addEventListener('change', function () { pick($('opSel').value); });
  N.load('opc').then(function (r) {
    R = r; view();
    var h = /^#opc-(.+)$/.exec(location.hash);
    if (h) pick(decodeURIComponent(h[1]));
  }).catch(function () { $('repNote').textContent = t('loadFail'); });
})();
