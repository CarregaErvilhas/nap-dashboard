// "Estados das tomadas": what each NAP status means and the two cases we read
// differently (scripts/socket_states.py). The numbers come from stats.json
// `states` (scripts/archive_stats.states, the archive window of the weekly run).
'use strict';
(function () {
  var N = window.NAP, el = N.el, t = N.t;
  N.addStrings({
    esH1: 'Estados das tomadas',
    esLead: 'Cada operador declara ao NAP o estado de cada tomada. Aqui está o que cada estado quer dizer, e os dois casos em que o mostramos de outra forma, com os números que o justificam.',
    hList: 'Os estados', hShared: 'Tomadas partilhadas: não é avaria',
    hUnk: 'Sem informação: falha de comunicação ou posto parado', hWhere: 'Onde se aplica, e os limites',
    cNap: 'No NAP (DATEX II)', cShow: 'Aqui', cMeans: 'O que quer dizer',
    m_available: 'Pronta para começar uma sessão.',
    m_charging: 'Há uma sessão a decorrer.',
    m_shared: 'Nosso, não do NAP. O posto só carrega numa tomada de cada vez e a outra está a carregar: o operador declara esta fora de serviço (ou inoperacional, ou bloqueada), mas não está avariada. Conta como ocupada.',
    m_outOfOrder: 'Indisponível por avaria ou falha técnica. Conta como avariada, menos no caso acima.',
    m_inoperative: 'Temporariamente indisponível. Conta como avariada, menos no caso acima.',
    m_blocked: 'Não se pode começar a carregar (acesso bloqueado, restrição do local). Não conta como avariada.',
    m_reserved: 'Reservada para um utilizador. A rede portuguesa não a publica.',
    m_unknown: 'O operador não sabe o estado. Até 24 h seguidas: sem informação. A partir de 24 h: conta como avariada.',
    m_planned: 'Prevista, ainda não funciona. Fora das contas.',
    m_removed: 'Desativada e retirada. Fora das contas.',
    shNap: 'OUTOFORDER, INOPERATIVE ou BLOCKED',
    unkLong: 'Sem informação há 24 h ou mais: conta como Avariado',
    shText1: 'Muitos postos com CCS e CHAdeMO (e alguns AC) só carregam um carro de cada vez. Quando uma tomada começa a carregar, o operador põe a outra fora de serviço; quando acaba, volta a pô-la livre. Lido à letra, a tomada parada parecia avariada várias horas por dia.',
    shText2: 'Por isso aprendemos os pares a partir do histórico: uma tomada fica em par com outra do mesmo posto quando os seus períodos em baixo começam e acabam, com {tol} min de folga, ao mesmo tempo que uma carga da outra, pelo menos {k} vezes e em pelo menos {share} % desses períodos ({d} dias de histórico). Só nesses pares, e só enquanto a outra está a carregar, o estado passa a "Em uso pela outra tomada". Uma tomada de um par que fica em baixo sem a outra carregar continua avariada: uma regra para todos os postos esconderia avarias reais nos postos mais usados.',
    shStats: 'Agora: {p} tomadas em par, em {s} postos. {h} % do tempo de todas as tomadas estava declarado em baixo e era afinal a tomada partilhada.',
    shOps: 'Postos com tomadas partilhadas, por operador (prefixo do código NAP)', cOp: 'Operador', cSites: 'Postos',
    shEx: 'Exemplo: na Galp da Av. Marginal (OER-00076), a CHAdeMO aparecia avariada perto de um quarto do dia. Afinal ia para fora de serviço exatamente quando a CCS começava a carregar, e voltava a livre quando a CCS acabava.',
    unkText: 'O unknown tem duas caras. A maior parte são falhas de comunicação de minutos, no posto todo de uma vez, que voltam a livre: isso não é avaria. Mas um posto que fica dias sem dizer nada já não está a funcionar. Por isso, a partir de 24 h seguidas sem informação, a tomada conta como avariada.',
    unkStats: 'Na janela atual: {n} períodos em unknown, {u} % acabaram em menos de 1 h, {l} chegaram às 24 h. Em tempo: {ps} % do tempo de todas as tomadas foi unknown curto e {pl} % unknown de 24 h ou mais.',
    unkCaveat: 'Atenção: há tomadas que nunca publicam estado nenhum. Para essas, "avariado" pode ser só o operador a não enviar o estado. A tabela de fiabilidade por operador mostra essa parte numa coluna própria.',
    wh1: 'Procurar: o estado ao vivo, o histórico de cada posto e o mapa dia da semana × hora (que conta a tomada partilhada como ocupada).',
    wh2: 'Rede e Explorar: ocupação ao vivo e o painel Histórico (fiabilidade, tempo até reparar, ocupação).',
    wh3: 'Limites: ao vivo não sabemos há quanto tempo uma tomada está sem informação, por isso o unknown longo só entra no histórico. O retrato diário de "Ao longo dos anos" (Explorar) continua com o estado declarado. Os pares do histórico por posto são aprendidos nos {d} dias até cada dia; os outros usam os da janela atual.',
    src: 'Estados declarados pelos operadores ao NAP (IMT / MOBI.E), guardados pelo AmpereArchive: não são medições.',
    none: 'Ainda sem números: o histórico não está disponível nesta publicação.'
  }, {
    esH1: 'Socket statuses',
    esLead: 'Each operator declares the status of every socket to the NAP. Here is what each status means, and the two cases we show differently, with the numbers behind them.',
    hList: 'The statuses', hShared: 'Shared sockets: not a fault',
    hUnk: 'No information: a dropped link or a dead site', hWhere: 'Where it applies, and the limits',
    cNap: 'In the NAP (DATEX II)', cShow: 'Here', cMeans: 'What it means',
    m_available: 'Ready to start a session.',
    m_charging: 'A session is under way.',
    m_shared: 'Ours, not the NAP\'s. The site charges on one socket at a time and the other is charging: the operator declares this one out of order (or inoperative, or blocked), but it is not broken. Counts as busy.',
    m_outOfOrder: 'Unavailable because of a fault. Counts as out of order, except for the case above.',
    m_inoperative: 'Temporarily unavailable. Counts as out of order, except for the case above.',
    m_blocked: 'Charging cannot start (access blocked, a site restriction). Does not count as out of order.',
    m_reserved: 'Reserved for one user. The Portuguese network does not publish it.',
    m_unknown: 'The operator does not know. Up to 24 h in a row: no information. From 24 h: counts as out of order.',
    m_planned: 'Planned, not working yet. Left out of the figures.',
    m_removed: 'Decommissioned. Left out of the figures.',
    shNap: 'OUTOFORDER, INOPERATIVE or BLOCKED',
    unkLong: 'No information for 24 h or more: counts as Out of order',
    shText1: 'Many sites with CCS and CHAdeMO (and some AC ones) charge one car at a time. When one socket starts charging, the operator puts the other out of order; when it ends, it puts it back to free. Taken literally, the idle socket looked broken for hours every day.',
    shText2: 'So we learn the pairs from the history: a socket pairs with another one at the same site when its down periods start and end, within {tol} min, together with a charge of the other, at least {k} times and in at least {share}% of those periods ({d} days of history). Only for those pairs, and only while the other one is charging, the status becomes "In use by the other socket". A paired socket that goes down while the other is not charging stays out of order: one rule for every site would hide real faults at the busiest ones.',
    shStats: 'Now: {p} paired sockets at {s} sites. {h}% of all sockets\' time was declared down and was in fact the shared socket.',
    shOps: 'Sites with shared sockets, by operator (prefix of the NAP code)', cOp: 'Operator', cSites: 'Sites',
    shEx: 'Example: at Galp on Av. Marginal (OER-00076), the CHAdeMO looked out of order for about a quarter of the day. It went out of order exactly when the CCS started charging, and back to free when the CCS finished.',
    unkText: 'Unknown has two faces. Most are communication drops of a few minutes, for the whole site at once, that go back to free: that is not a fault. But a site that says nothing for days is no longer working. So from 24 h in a row without information, the socket counts as out of order.',
    unkStats: 'In the current window: {n} unknown periods, {u}% ended in under 1 h, {l} reached 24 h. In time: {ps}% of all sockets\' time was short unknown and {pl}% unknown for 24 h or more.',
    unkCaveat: 'Note: some sockets never publish any status. For those, "out of order" may just be the operator not sending it. The reliability table by operator shows that part in its own column.',
    wh1: 'Find: live status, each site\'s history and the weekday × hour map (which counts the shared socket as busy).',
    wh2: 'Network and Explore: live occupancy and the History panel (reliability, time to repair, occupancy).',
    wh3: 'Limits: live, we do not know how long a socket has had no information, so long unknown only enters the history. The daily snapshot of "Over the years" (Explore) keeps the declared status. Each site\'s history learns its pairs over the {d} days up to each day; the rest use the current window\'s.',
    src: 'Statuses declared by the operators to the NAP (IMT / MOBI.E), kept by the AmpereArchive: not measurements.',
    none: 'No figures yet: the history is not available in this release.'
  });
  var $ = function (id) { return document.getElementById(id); };
  var ROWS = [['AVAILABLE', 'available'], ['CHARGING', 'charging'], [null, 'shared'], ['OUTOFORDER', 'outOfOrder'],
    ['INOPERATIVE', 'inoperative'], ['BLOCKED', 'blocked'], ['RESERVED', null], ['UNKNOWN', 'unknown'],
    ['PLANNED', 'planned'], ['REMOVED', 'removed']];

  function list() {
    var body = ROWS.map(function (r) {
      var key = r[1] || 'reserved';
      return el('tr', null, el('td', null, r[0] ? el('code', null, r[0]) : el('code', null, t('shNap'))),
        el('td', null, r[1] ? N.status(r[1]) : '—'), el('td', null, t('m_' + key)));
    });
    body.push(el('tr', null, el('td', null, el('code', null, 'UNKNOWN'), ' ≥ 24 h'), el('td', null, N.status('outOfOrder')), el('td', null, t('unkLong'))));
    N.clear($('esList')).appendChild(el('div', { class: 'scroll', tabindex: '0' }, el('table', null,
      el('thead', null, el('tr', null, el('th', { scope: 'col' }, t('cNap')), el('th', { scope: 'col' }, t('cShow')), el('th', { scope: 'col' }, t('cMeans')))),
      el('tbody', null, body))));
  }

  function render(st) {
    list();
    var r = (st && st.rules) || { tol_s: 300, min_episodes: 3, min_share: 0.5, learn_days: 28, unknown_down_h: 24 };
    var sh = N.clear($('esShared'));
    sh.appendChild(el('p', null, t('shText1')));
    sh.appendChild(el('p', null, t('shEx')));
    sh.appendChild(el('p', null, t('shText2', { tol: N.nf(r.tol_s / 60), k: N.nf(r.min_episodes), share: N.nf(100 * r.min_share), d: N.nf(r.learn_days) })));
    var unk = N.clear($('esUnk'));
    unk.appendChild(el('p', null, t('unkText')));
    if (st && st.pairs != null) {
      var pct = st.pct || {};
      sh.appendChild(el('p', null, el('b', null, t('shStats', { p: N.nf(st.pairs), s: N.nf(st.sites), h: N.nf(pct.shared || 0, 1) }))));
      if (st.by_operator && st.by_operator.length) {
        sh.appendChild(el('div', { class: 'scroll', tabindex: '0' }, el('table', null, el('caption', null, t('shOps')),
          el('thead', null, el('tr', null, el('th', { scope: 'col' }, t('cOp')), el('th', { scope: 'col', class: 'n' }, t('cSites')))),
          el('tbody', null, st.by_operator.map(function (o) { return el('tr', null, el('td', null, o.op), el('td', { class: 'n' }, N.nf(o.sites))); })))));
      }
      var ue = st.unknown_episodes || {};
      unk.appendChild(el('p', null, el('b', null, t('unkStats', { n: N.nf(ue.n || 0), u: N.nf(ue.n ? 100 * ue.under_1h / ue.n : 0, 0),
        l: N.nf(ue.long || 0), ps: N.nf(pct.unknown || 0, 1), pl: N.nf(pct.unknownLong || 0, 1) }))));
    } else {
      sh.appendChild(el('p', { class: 'muted' }, t('none')));
    }
    unk.appendChild(el('p', null, t('unkCaveat')));
    var wh = N.clear($('esWhere'));
    [t('wh1'), t('wh2'), t('wh3', { d: N.nf(r.learn_days) })].forEach(function (s) { wh.appendChild(el('p', null, s)); });
    wh.appendChild(el('p', { class: 'small muted' }, t('src')));
  }

  var ST = null;
  N.onLang(function () { render(ST); });
  N.initChrome();
  N.load('stats').then(function (d) { ST = d && d.states; render(ST); }).catch(function () { render(null); });
})();
