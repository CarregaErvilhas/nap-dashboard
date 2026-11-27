// "Uso ao longo do tempo" in Procurar's site detail: what each socket did over
// the last 24 h, 7 days, 30 days and since the archive has it, plus a weekday x
// hour map. Data: data/sites/<xx>.json.gz, 256 files of a few dozen sites each,
// built every hour from the AmpereArchive by scripts/site_history.py
// (site-history.yml) and published with the site; a detail fetches its file. Every
// bucket is [cells, charging, available, down, shared] with the last four summed in
// hundredths of a cell, so sockets add up; empty buckets are 0. A fifth
// number, when present, is the time "in use by the other socket": one of a pair
// of sockets that charge one at a time, which the operator declares down while
// its partner charges (scripts/socket_states.py, estados.html).
(function () {
  'use strict';
  var N = window.NAP, t = N.t, el = N.el;
  N.addStrings({
    uTitle: 'Uso ao longo do tempo', uPeriod: 'Período', uSocket: 'Tomada', uAll: 'Posto inteiro',
    u24: '24 h', u7: '7 dias', u30: '30 dias', uMax: 'Tudo',
    uCharging: 'A carregar', uAvailable: 'Livre', uDown: 'Avariado', uShared: 'Em uso pela outra tomada', uUnknown: 'Sem informação', uNa: 'sem dados',
    uStates: 'O que quer dizer cada estado', 
    uSum24: 'Nas últimas 24 h', uSum7: 'Nos últimos 7 dias', uSum30: 'Nos últimos 30 dias', uSumMax: 'Desde {m}',
    uLanes: '{p}, tomada a tomada:', uOne: '{p}, tomada {id}:', uGroup: '{n} × {plug} {kw} kW',
    uSampled: 'Meses com barras mais claras: o arquivo tem poucas leituras por hora, por isso são uma amostra, não o tempo todo.',
    uTip: '{w}: {v}', uTipNa: '{w}: sem dados', uTipSample: ' (amostra)',
    uHeat: 'Ocupação por dia da semana e hora (%)', uHeatOne: 'Ocupação por dia da semana e hora (%), tomada {id}',
    uHeatLo: 'menos ocupado', uHeatHi: 'mais ocupado (máximo: {m} %)',
    uHeatNote: 'Hora local, últimos {d} dias. Percentagem do tempo ocupado (a carregar ou em uso pela outra tomada), entre o tempo ocupado e livre; uma hora precisa de 2 dias com dados.',
    uHeatCell: '{w}, {h} h: {v} % ocupado', uHeatNa: '{w}, {h} h: sem dados',
    uSrc: 'Estados declarados pelos operadores ao NAP (IMT / MOBI.E), guardados pelo AmpereArchive: não são medições. Atualizado de hora a hora; dados até {t}.',
    uLoading: 'A carregar o histórico…', uFail: 'Sem histórico de uso para este posto.',
    uWd0: 'Segunda', uWd1: 'Terça', uWd2: 'Quarta', uWd3: 'Quinta', uWd4: 'Sexta', uWd5: 'Sábado', uWd6: 'Domingo'
  }, {
    uTitle: 'Use over time', uPeriod: 'Period', uSocket: 'Socket', uAll: 'Whole site',
    u24: '24 h', u7: '7 days', u30: '30 days', uMax: 'All',
    uCharging: 'Charging', uAvailable: 'Available', uDown: 'Out of order', uShared: 'In use by the other socket', uUnknown: 'No information', uNa: 'no data',
    uStates: 'What each status means', 
    uSum24: 'Over the last 24 h', uSum7: 'Over the last 7 days', uSum30: 'Over the last 30 days', uSumMax: 'Since {m}',
    uLanes: '{p}, socket by socket:', uOne: '{p}, socket {id}:', uGroup: '{n} × {plug} {kw} kW',
    uSampled: 'Months with lighter bars: the archive has few reads per hour, so they are a sample, not the whole time.',
    uTip: '{w}: {v}', uTipNa: '{w}: no data', uTipSample: ' (sample)',
    uHeat: 'Occupancy by weekday and hour (%)', uHeatOne: 'Occupancy by weekday and hour (%), socket {id}',
    uHeatLo: 'less busy', uHeatHi: 'busier (maximum: {m}%)',
    uHeatNote: 'Local time, last {d} days. Share of the time busy (charging or in use by the other socket), out of the time busy or available; an hour needs 2 days with data.',
    uHeatCell: '{w}, {h}:00: {v}% busy', uHeatNa: '{w}, {h}:00: no data',
    uSrc: 'Statuses declared by the operators to the NAP (IMT / MOBI.E), kept by the AmpereArchive: not measurements. Updated every hour; data up to {t}.',
    uLoading: 'Loading the history…', uFail: 'No usage history for this site.',
    uWd0: 'Monday', uWd1: 'Tuesday', uWd2: 'Wednesday', uWd3: 'Thursday', uWd4: 'Friday', uWd5: 'Saturday', uWd6: 'Sunday'
  });

  var SHARDS = 256, MAX_LANES = 8, SAMPLE_RES = 2;
  var KEYS = ['charging', 'shared', 'available', 'down', 'unknown'];
  var NAME = { charging: 'uCharging', shared: 'uShared', available: 'uAvailable', down: 'uDown', unknown: 'uUnknown' };
  var NS = 'http://www.w3.org/2000/svg';
  var shards = new Map(), views = new Map(), uid = 0;

  // Same hash as scripts/site_history.py shard_of: FNV-1a 32 over UTF-8.
  function shardOf(id) {
    var h = 0x811c9dc5, b = new TextEncoder().encode(id);
    for (var i = 0; i < b.length; i++) { h ^= b[i]; h = Math.imul(h, 0x01000193) >>> 0; }
    return (h % SHARDS).toString(16).padStart(2, '0');
  }
  function shard(k) {
    if (!shards.has(k)) {
      var p = N.fetchJson('data/sites/' + k + '.json.gz');
      p.catch(function () { shards.delete(k); });
      shards.set(k, p);
    }
    return shards.get(k);
  }
  function sv(tag, attrs) {
    var e = document.createElementNS(NS, tag);
    Object.keys(attrs || {}).forEach(function (k) { e.setAttribute(k, attrs[k]); });
    return e;
  }
  // Files from before the shared state have four numbers: the fifth reads as 0.
  function add(a, b) {
    if (!b) return a;
    if (!a) return [b[0], b[1], b[2], b[3], b[4] || 0];
    return a.map(function (v, i) { return v + (b[i] || 0); });
  }
  function sumOf(lists) {   // lists of buckets -> one list, bucket by bucket
    return lists.reduce(function (acc, l) { return acc ? acc.map(function (b, i) { return add(b, l[i] || 0); }) : l.map(function (b) { return add(0, b); }); }, null);
  }
  function parts(b) {   // bucket -> percentages per KEYS, or null
    if (!b || !b[0]) return null;
    var s = b[4] || 0, tot = 100 * b[0], u = Math.max(0, tot - b[1] - b[2] - b[3] - s);
    return [b[1], s, b[2], b[3], u].map(function (v) { return 100 * v / tot; });
  }
  function pct(v) { return N.nf(Math.round(v)) + ' %'; }
  function summary(list) {
    var tot = list.reduce(function (a, b) { return add(a, b || 0); }, 0), p = parts(tot);
    if (!p) return t('uNa');
    return KEYS.filter(function (k, i) { return k === 'charging' || k === 'available' || k === 'down' || p[i] >= 0.5; }).map(function (k) { return t(NAME[k]).toLowerCase() + ' ' + pct(p[KEYS.indexOf(k)]); }).join(' · ');
  }

  function fmt(tz, opts) {
    try { return new Intl.DateTimeFormat(N.lang() === 'en' ? 'en-GB' : 'pt-PT', Object.assign({ timeZone: tz }, opts)); }
    catch (e) { return new Intl.DateTimeFormat(N.lang() === 'en' ? 'en-GB' : 'pt-PT', opts); }
  }
  // Buckets of the chosen period, with labels and whether each is a sample.
  function period(doc, site, per, pick) {
    var tz = site.tz, n, lab = [], tip = [], axis = [], sampled = [];
    if (per === '24' || per === '7') {
      var h0 = Date.parse(doc.hours.from), hh = fmt(tz, { hour: 'numeric', hourCycle: 'h23' }), dd = fmt(tz, { day: 'numeric', month: 'numeric' }), full = fmt(tz, { weekday: 'short', day: 'numeric', month: 'numeric', hour: 'numeric', hourCycle: 'h23' });
      var from = per === '24' ? doc.hours.n - 24 : 0;
      for (var i = from; i < doc.hours.n; i++) {
        var d = new Date(h0 + i * 3600e3), hr = +hh.format(d);
        tip.push(full.format(d)); sampled.push(false);
        axis.push(per === '24' ? (i % 3 === 0 ? String(hr) : '') : (hr === 0 ? dd.format(d) : ''));
      }
      return { b: pick('h').slice(from), tip: tip, axis: axis, sampled: sampled };
    }
    if (per === '30') {
      var d0 = Date.parse(doc.days.from + 'T12:00:00Z'), df = fmt('UTC', { day: 'numeric', month: 'numeric' }), dl = fmt('UTC', { weekday: 'short', day: 'numeric', month: 'numeric' });
      for (var j = 0; j < doc.days.n; j++) {
        var dj = new Date(d0 + j * 864e5);
        tip.push(dl.format(dj)); axis.push(j % 5 === 0 ? df.format(dj) : ''); sampled.push(false);
      }
      return { b: pick('d'), tip: tip, axis: axis, sampled: sampled };
    }
    // Leading months before this site has any data are dropped, then labelled.
    var b = pick('m'), first = Math.max(0, b.findIndex(function (x) { return x; }));
    var list = doc.months.list.slice(first), res = doc.months.res.slice(first);
    var mf = fmt('UTC', { month: 'short' }), ml = fmt('UTC', { month: 'long', year: 'numeric' }), every = Math.ceil(list.length / 12);
    list.forEach(function (m, k) {
      var dm = new Date(m + '-15T12:00:00Z');
      tip.push(ml.format(dm)); sampled.push((res[k] || 0) < SAMPLE_RES);
      axis.push(k % every === 0 ? mf.format(dm).replace('.', '') + (m.slice(5) === '01' || k === 0 ? ' ' + m.slice(2, 4) : '') : '');
    });
    return { b: b.slice(first), tip: tip, axis: axis, sampled: sampled };
  }

  // One chart: stacked bars of KEYS per bucket, hatched where there is no data.
  function chart(pd, H, withAxis, label) {
    var W = 700, top = 6, left = 34, bot = withAxis ? 20 : 4, n = pd.b.length, bw = (W - left) / n, gap = n > 60 ? 0.4 : n > 30 ? 1 : 2;
    var svg = sv('svg', { class: 'uchart', viewBox: '0 0 ' + W + ' ' + (H + bot), role: 'img', 'aria-label': label });
    var id = 'uhatch' + (++uid), defs = sv('defs'), pat = sv('pattern', { id: id, width: 5, height: 5, patternUnits: 'userSpaceOnUse', patternTransform: 'rotate(45)' });
    pat.appendChild(sv('line', { x1: 0, y1: 0, x2: 0, y2: 5, class: 'uh' })); defs.appendChild(pat); svg.appendChild(defs);
    (H < 120 ? [0, 100] : [0, 50, 100]).forEach(function (p) {
      var y = top + (H - top) * (1 - p / 100);
      svg.appendChild(sv('line', { x1: left, x2: W, y1: y, y2: y, class: 'ugrid' }));
      var tx = sv('text', { x: left - 4, y: y + 4, 'text-anchor': 'end' }); tx.textContent = p + '%'; svg.appendChild(tx);
    });
    pd.b.forEach(function (b, i) {
      var x = left + i * bw + gap / 2, w = Math.max(0.4, bw - gap), p = parts(b), g = sv('g'), ti = sv('title');
      if (!p) {
        g.appendChild(sv('rect', { x: x, y: top, width: w, height: H - top, fill: 'url(#' + id + ')', class: 'una' }));
        ti.textContent = t('uTipNa', { w: pd.tip[i] });
      } else {
        var y = H;
        KEYS.forEach(function (k, j) {
          var h = (H - top) * p[j] / 100;
          y -= h;
          if (h > 0.05) g.appendChild(sv('rect', { x: x, y: y, width: w, height: h, class: 'u-' + k + (pd.sampled[i] ? ' us' : '') }));
        });
        ti.textContent = t('uTip', { w: pd.tip[i] }) + (pd.sampled[i] ? t('uTipSample') : '') + ': ' + KEYS.map(function (k, j) { return t(NAME[k]) + ' ' + pct(p[j]); }).join(', ');
      }
      g.appendChild(ti); svg.appendChild(g);
      if (withAxis && pd.axis[i]) {
        var tx = sv('text', { x: x + w / 2, y: H + 15, 'text-anchor': n > 30 ? 'start' : 'middle' }); tx.textContent = pd.axis[i]; svg.appendChild(tx);
      }
    });
    return svg;
  }

  function heat(box, doc, w) {
    var cells = [], mx = 0, wd, h;
    for (wd = 0; wd < 7; wd++) {
      cells.push([]);
      for (h = 0; h < 24; h++) {
        var b = w[wd * 24 + h], busy = b ? b[1] + (b[4] || 0) : 0, act = b ? busy + b[2] : 0;
        var v = b && b[0] >= 2 && act > 0 ? 100 * busy / act : null;
        cells[wd].push(v); if (v != null && v > mx) mx = v;
      }
    }
    var head = el('tr', null, el('td'));
    for (h = 0; h < 24; h++) head.appendChild(el('td', null, h % 3 ? '' : String(h)));
    var body = cells.map(function (row, wd) {
      return el('tr', null, el('th', { scope: 'row' }, t('uWd' + wd)), row.map(function (v, h) {
        if (v == null) return el('td', { class: 'na', title: t('uHeatNa', { w: t('uWd' + wd), h: h }) }, el('span', { class: 'sr' }, t('uNa')));
        var td = el('td', { title: t('uHeatCell', { w: t('uWd' + wd), h: h, v: N.nf(v, 0) }) }, el('span', { class: 'sr' }, N.nf(v, 0) + ' %'));
        td.style.setProperty('--k', Math.round(8 + 92 * v / (mx || 1)) + '%');   // CSSOM: the CSP forbids style attributes
        return td;
      }));
    });
    box.appendChild(el('div', { class: 'scroll', tabindex: '0' }, el('table', { class: 'uheat' }, el('thead', null, head), el('tbody', null, body))));
    var sw = function (k, cls) { var s = el('span', { class: 'sw' + (cls ? ' ' + cls : '') }); if (k) s.style.setProperty('--k', k); return s; };
    box.appendChild(el('div', { class: 'ukey small' }, el('span', null, sw('8%'), sw('54%'), sw('100%'), ' ' + t('uHeatLo') + ' → ' + t('uHeatHi', { m: N.nf(mx, 0) })),
      el('span', null, sw(null, 'na'), ' ' + t('uNa'))));
    box.appendChild(el('p', { class: 'small muted' }, t('uHeatNote', { d: doc.heat.days })));
  }

  // The plug and power of each socket, from points.json.
  function sockLabel(p) { return String(p.connectors || '—').split('|').join(', ') + (p.kw ? ' ' + N.nf(p.kw, p.kw % 1 ? 1 : 0) + ' kW' : ''); }

  function render(box, doc, site, pts, st) {
    N.clear(box);
    // Keys stay point_ids (they index site.p); what is shown is the EVSE code.
    var byId = {};
    pts.forEach(function (p) { byId[p.point_id] = p; });
    var name = function (id) { return byId[id] ? N.sockId(byId[id]) : id; };
    var ids = Object.keys(site.p).sort(function (a, b) { return name(a).localeCompare(name(b), undefined, { numeric: true }); });
    var seg = function (label, opts, cur, set) {
      return el('div', { class: 'seg', role: 'group', 'aria-label': label }, el('span', { class: 'lbl' }, label), opts.map(function (o) {
        return el('button', { class: 'btn sm', type: 'button', 'aria-pressed': String(cur === o[0]), onclick: function () { set(o[0]); render(box, doc, site, pts, st); } }, o[1]);
      }));
    };
    var ctl = el('div', { class: 'uctl' }, seg(t('uPeriod'), [['24', t('u24')], ['7', t('u7')], ['30', t('u30')], ['max', t('uMax')]], st.per, function (v) { st.per = v; }));
    if (ids.length > 1) {
      var opts = [['all', t('uAll')]].concat(ids.map(function (id) { return [id, name(id) + (byId[id] ? ' · ' + sockLabel(byId[id]) : '')]; }));
      if (ids.length <= 6) ctl.appendChild(seg(t('uSocket'), opts, st.sock, function (v) { st.sock = v; }));
      else {
        var sel = el('select', { 'aria-label': t('uSocket'), onchange: function () { st.sock = sel.value; render(box, doc, site, pts, st); } },
          opts.map(function (o) { var op = el('option', { value: o[0] }, o[1]); if (o[0] === st.sock) op.selected = true; return op; }));
        ctl.appendChild(el('label', { class: 'field' }, t('uSocket'), sel));
      }
    }
    box.appendChild(el('h4', null, t('uTitle')));
    box.appendChild(ctl);
    var mfirst = doc.months.list[(site.p[ids[0]].m || []).findIndex(function (x) { return x; })] || doc.months.from;
    var perTxt = st.per === 'max' ? t('uSumMax', { m: fmt('UTC', { month: 'long', year: 'numeric' }).format(new Date(mfirst + '-15T12:00:00Z')) }) : t('uSum' + st.per);
    var charts = el('div', { class: 'ucharts' }), anySample = false;
    var pick = function (list) { return function (k) { return sumOf(list.map(function (id) { return site.p[id][k]; })); }; };
    if (st.sock === 'all' && ids.length > 1) {
      // One lane per socket; on a large site, per kind of socket (same plug and power).
      var lanes = ids.map(function (id) { return { ids: [id], label: name(id) + (byId[id] ? ' · ' + sockLabel(byId[id]) : '') }; });
      if (ids.length > MAX_LANES) {
        var groups = {};
        ids.forEach(function (id) { var k = byId[id] ? sockLabel(byId[id]) : '—'; (groups[k] = groups[k] || []).push(id); });
        lanes = Object.keys(groups).sort().map(function (k) { return { ids: groups[k], label: groups[k].length > 1 ? groups[k].length + ' × ' + k : k }; });
      }
      box.appendChild(el('p', { class: 'small' }, t('uLanes', { p: perTxt })));
      lanes.forEach(function (ln, i) {
        var pd = period(doc, site, st.per, pick(ln.ids));
        anySample = anySample || pd.sampled.some(Boolean);
        charts.appendChild(el('div', { class: 'ulane' }, el('div', { class: 'small' }, el('b', null, ln.label), ' ', el('span', { class: 'muted' }, summary(pd.b))),
          chart(pd, 64, i === lanes.length - 1, ln.label + ': ' + summary(pd.b))));
      });
    } else {
      var one = st.sock === 'all' ? ids : [st.sock], pd1 = period(doc, site, st.per, pick(one));
      anySample = pd1.sampled.some(Boolean);
      box.appendChild(el('p', { class: 'small' }, t('uOne', { p: perTxt, id: one.length > 1 ? '' : name(one[0]) }), ' ', el('b', null, summary(pd1.b))));
      charts.appendChild(chart(pd1, 170, true, summary(pd1.b)));
    }
    box.appendChild(charts);
    box.appendChild(el('div', { class: 'ukey small' }, KEYS.map(function (k) { return el('span', null, el('i', { class: 'u-' + k }), t(NAME[k])); }).concat(
      el('span', null, el('i', { class: 'una' }), t('uNa')),
      el('a', { class: 'uinfo', href: 'estados.html' + (N.lang() === 'en' ? '?lang=en' : ''), title: t('uStates') }, el('span', { 'aria-hidden': 'true' }, 'ⓘ '), t('uStates')))));
    if (st.per === 'max' && anySample) box.appendChild(el('p', { class: 'small muted' }, t('uSampled')));
    var hid = st.sock === 'all' ? ids : [st.sock];
    box.appendChild(el('h4', null, st.sock === 'all' ? t('uHeat') : t('uHeatOne', { id: name(st.sock) })));
    heat(box, doc, pick(hid)('w'));
    box.appendChild(el('p', { class: 'small muted' }, t('uSrc', { t: fmt(site.tz, { day: 'numeric', month: 'numeric', hour: 'numeric', minute: '2-digit', hourCycle: 'h23' }).format(new Date(doc.until)) })));
  }

  // The section for one site, filled when its file arrives. A site the file
  // does not have gets a line saying so. `pts` are the site's points.json rows.
  function section(s, pts) {
    var id = s.oop || (pts.filter(function (p) { return p.nap_site; })[0] || {}).nap_site;
    if (!id || !pts.length) return null;
    var box = el('div', { class: 'uso' }, el('p', { class: 'small muted' }, t('uLoading')));
    // The choice survives the detail being redrawn (live status, language).
    var st = views.get(id) || { per: '24', sock: 'all' };
    views.set(id, st);
    shard(shardOf(id)).then(function (doc) {
      var site = doc && doc.sites && doc.sites[id];
      if (!site || !Object.keys(site.p || {}).length) { N.clear(box).appendChild(el('p', { class: 'small muted' }, t('uFail'))); return; }
      render(box, doc, site, pts, st);
    // No file (a deploy without the history, offline): the section just goes away.
    }).catch(function () { box.hidden = true; });
    return box;
  }

  window.NAP_USO = { section: section, shardOf: shardOf };
})();
