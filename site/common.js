// Shared by every page: translations, DOM helpers, data loading, live status.
// Rule for the whole front end: text that comes from data goes in through
// textContent (el() below). OSM and operator names are third-party input.
'use strict';
(function () {
  var A = window.NAPAPP;
  var STR = {
    pt: {
      navFind: 'Procurar', navNet: 'Rede', navExplore: 'Explorar', navOps: 'Operadores',
      appearance: 'Aparência', theme: 'Tema', vision: 'Visão', auto: 'Automático', light: 'Claro', dark: 'Escuro',
      vdefault: 'Padrão', cb: 'Daltonismo', hc: 'Alto contraste', language: 'Idioma',
      liveOk: 'Estado ao vivo de {t} ({n} de {m} tomadas).', liveStale: 'Estado ao vivo indisponível: a mostrar o da semana ({t}).',
      liveOff: 'Sem ligação ao estado ao vivo: a mostrar o retrato de {t}.', loading: 'A carregar…',
      loadFail: 'Não foi possível carregar os dados. Verifica a ligação e recarrega a página.',
      st_available: 'Livre', st_charging: 'A carregar', st_outOfOrder: 'Avariado', st_inoperative: 'Inoperacional',
      st_unknown: 'Sem informação', st_blocked: 'Bloqueado', st_planned: 'Planeado', st_removed: 'Removido',
      mcsHeavy: 'pesados', rg_mainland: 'Continente', rg_madeira: 'Madeira', rg_azores: 'Açores', rg_OUTSIDE: 'Fora de PT',
      pw0: 'AC lento (<22 kW)', pw1: 'AC/DC 22–50 kW', pw2: 'DC rápido 50–150 kW', pw3: 'DC ultra 150–350 kW', pw4: 'DC ultra (≥350 kW)',
      pay_App: 'App', 'pay_Multibanco/contactless': 'Multibanco/contactless', pay_Dinheiro: 'Dinheiro',
      'pay_Cartão RFID eMSP': 'Cartão do comercializador (RFID)', 'pay_Sem autenticação': 'Sem autenticação',
      pk_opc: 'Taxa do operador (OPC), sem energia', pk_adhoc: 'Sem contrato (ad hoc), com energia',
      pk_direct: 'Fora da MOBI.E, preço único com energia', pk_napfee: 'Preço segundo o NAP, sem tarifa na MOBI.E',
      pks_opc: 'Taxa do operador', pks_adhoc: 'Sem contrato', pks_direct: 'Fora da MOBI.E', pks_napfee: 'Só no NAP',
      installLater: 'Agora não'
    },
    en: {
      navFind: 'Find', navNet: 'Network', navExplore: 'Explore', navOps: 'Operators',
      appearance: 'Appearance', theme: 'Theme', vision: 'Vision', auto: 'Automatic', light: 'Light', dark: 'Dark',
      vdefault: 'Default', cb: 'Colour-blind', hc: 'High contrast', language: 'Language',
      liveOk: 'Live status as of {t} ({n} of {m} sockets).', liveStale: 'Live status unavailable: showing this week\'s ({t}).',
      liveOff: 'No connection to live status: showing the snapshot of {t}.', loading: 'Loading…',
      loadFail: 'Could not load the data. Check your connection and reload the page.',
      st_available: 'Free', st_charging: 'Charging', st_outOfOrder: 'Out of order', st_inoperative: 'Inoperative',
      st_unknown: 'No information', st_blocked: 'Blocked', st_planned: 'Planned', st_removed: 'Removed',
      mcsHeavy: 'heavy vehicles', rg_mainland: 'Mainland', rg_madeira: 'Madeira', rg_azores: 'Azores', rg_OUTSIDE: 'Outside PT',
      pw0: 'Slow AC (<22 kW)', pw1: 'AC/DC 22–50 kW', pw2: 'Fast DC 50–150 kW', pw3: 'Ultra DC 150–350 kW', pw4: 'Ultra DC (≥350 kW)',
      pay_App: 'App', 'pay_Multibanco/contactless': 'Bank card/contactless', pay_Dinheiro: 'Cash',
      'pay_Cartão RFID eMSP': 'Supplier card (RFID)', 'pay_Sem autenticação': 'No authentication',
      pk_opc: 'Operator (CPO) fee, energy not included', pk_adhoc: 'No contract (ad hoc), energy included',
      pk_direct: 'Outside MOBI.E, single price with energy', pk_napfee: 'Price according to the NAP, no tariff in MOBI.E',
      pks_opc: 'Operator fee', pks_adhoc: 'No contract', pks_direct: 'Outside MOBI.E', pks_napfee: 'NAP only',
      installLater: 'Not now'
    }
  };
  var PW = ['AC slow (<22kW)', 'AC/DC 22-50kW', 'DC fast 50-150kW', 'DC ultra 150-350kW', 'DC ultra (>=350kW)'];
  var STATUSES = ['available', 'charging', 'outOfOrder', 'inoperative', 'unknown', 'blocked', 'planned', 'removed'];
  var listeners = [];

  function lang() { return A.state.lang; }
  function t(key, vars) {
    var s = (STR[lang()] && STR[lang()][key]);
    if (s == null) s = STR.pt[key];
    if (s == null) return key;
    return vars ? s.replace(/\{(\w+)\}/g, function (_, k) { return vars[k] != null ? vars[k] : ''; }) : s;
  }
  function addStrings(pt, en) { Object.assign(STR.pt, pt); Object.assign(STR.en, en); }
  function pwLabel(c) { var i = PW.indexOf(c); return i < 0 ? (c || '—') : t('pw' + i); }
  // min: decimals always shown (money: 0,40 and not 0,4).
  function nf(n, d, min) {
    if (n == null || n === '' || isNaN(n)) return '—';
    return Number(n).toLocaleString(lang() === 'pt' ? 'pt-PT' : 'en-GB', { maximumFractionDigits: d == null ? 0 : d, minimumFractionDigits: min || 0 });
  }
  // Every euro amount on the statistics pages: always two decimals (0,40, never 0,4 or 0,112).
  function eur(n) { return nf(n, 2, 2); }
  // The kinds of price a socket can have (the same rule as scripts/price_kinds.py):
  //   opc     operator fee on MOBI.E (REGULAR plan): energy NOT included, the driver's CEME bills it
  //   adhoc   no-contract price on MOBI.E (AD_HOC_PAYMENT plan): energy included
  //   direct  outside MOBI.E (regime sem_ceme): one price per kWh, energy included
  //   napfee  MOBI.E socket missing from MOBI.E's tariff file: what the NAP publishes. Nobody says
  //           whether that is the operator fee or the no-contract price, so it is never either.
  // Never average or compare across kinds. Returns {kind: {kwh, min, flat, tiers}} for the kinds present.
  var PRICE_KINDS = ['opc', 'adhoc', 'direct', 'napfee'];
  function num(v) { if (Array.isArray(v)) v = v[0]; if (v && typeof v === 'object') v = v.eur; return typeof v === 'number' && isFinite(v) ? v : null; }
  function planOf(x) {
    var tiers = (x.time || []).slice().sort(function (a, b) { return (a.from || 0) - (b.from || 0); });
    return { kwh: num(x.energy), min: num(tiers), flat: num(x.flat), tiers: tiers };
  }
  function prices(p) {
    var out = {}, f = p.fees || {};
    if (p.regime === 'sem_ceme') { if (num(p.nap) != null) out.direct = { kwh: num(p.nap), min: null, flat: null, tiers: [] }; return out; }
    if (f.REGULAR) out.opc = planOf(f.REGULAR);
    if (f.AD_HOC_PAYMENT) out.adhoc = planOf(f.AD_HOC_PAYMENT);
    if (p.regime === 'mobie_sem_tarifa' && p.nap_fees) out.napfee = { kwh: num(p.nap_fees.kwh), min: num(p.nap_fees.min), flat: num(p.nap_fees.flat), tiers: [] };
    return out;
  }
  // What one session costs at one price (an entry of prices(p)), without VAT: the flat part, the
  // €/kWh part and every €/min tier over the minutes kwh takes at a constant kw. The per-minute part
  // is why a slower car pays more for the same energy. Only within one kind of price: the operator
  // fee leaves out the energy the CEME bills. null when the price has no component at all.
  function sessionCost(v, kwh, kw) {
    if (!v || !(kw > 0)) return null;
    var tiers = v.tiers && v.tiers.length ? v.tiers : v.min != null ? [{ eur: v.min, from: 0, to: null }] : [];
    if (v.kwh == null && v.flat == null && !tiers.length) return null;
    var mins = 60 * kwh / kw, c = (v.flat || 0) + (v.kwh || 0) * kwh;
    tiers.forEach(function (x) {
      if (typeof x === 'number') x = { eur: x, from: 0, to: null };
      var a = x.from || 0, b = x.to == null ? mins : Math.min(x.to, mins);
      if (b > a) c += (x.eur || 0) * (b - a);
    });
    return c;
  }
  // "0,55 €/kWh + 0,10 €/min + 0,40 €": every component of one price, zeros left out.
  function priceText(v, dec) {
    var f = function (x) { return dec == null ? eur(x) : nf(x, dec); }, parts = [];
    if (v.kwh) parts.push(f(v.kwh) + ' €/kWh');
    if (v.min) parts.push(f(v.min) + ' €/min');
    if (v.flat) parts.push(f(v.flat) + ' €');
    return parts.length ? parts.join(' + ') : (v.kwh === 0 || v.min === 0 || v.flat === 0 ? f(0) + ' €' : '—');
  }
  function when(ms) {
    return new Date(ms).toLocaleString(lang() === 'pt' ? 'pt-PT' : 'en-GB', { day: '2-digit', month: '2-digit', hour: '2-digit', minute: '2-digit' });
  }

  // el('p', {class:'x'}, 'text', child…): strings always become text nodes.
  function el(tag, attrs) {
    var n = document.createElement(tag), i, k;
    if (attrs) for (k in attrs) {
      if (attrs[k] == null || attrs[k] === false) continue;
      if (k === 'class') n.className = attrs[k];
      else if (k.slice(0, 2) === 'on') n.addEventListener(k.slice(2), attrs[k]);
      else n.setAttribute(k, attrs[k] === true ? '' : attrs[k]);
    }
    for (i = 2; i < arguments.length; i++) add(n, arguments[i]);
    return n;
  }
  function add(n, c) {
    if (c == null || c === false) return;
    if (Array.isArray(c)) { c.forEach(function (x) { add(n, x); }); return; }
    n.appendChild(c.nodeType ? c : document.createTextNode(String(c)));
  }
  function clear(n) { while (n.firstChild) n.removeChild(n.firstChild); return n; }
  // "text with `code`" -> text and <code> nodes (report fragments).
  function md(s) {
    return String(s || '').split('`').map(function (part, i) {
      part = part.replace(/\*\*/g, '');
      return i % 2 ? el('code', null, part) : part;
    });
  }
  function status(s, withText) {
    var known = STATUSES.indexOf(s) >= 0 ? s : 'unknown';
    var d = el('span', { class: 'dot', 'data-s': known, 'aria-hidden': 'true' });
    return withText === false ? d : el('span', { class: 'st' }, d, t('st_' + known));
  }

  function applyI18n(root) {
    (root || document).querySelectorAll('[data-i18n]').forEach(function (n) { n.textContent = t(n.getAttribute('data-i18n')); });
    (root || document).querySelectorAll('[data-i18n-ph]').forEach(function (n) { n.setAttribute('placeholder', t(n.getAttribute('data-i18n-ph'))); });
    (root || document).querySelectorAll('[data-i18n-label]').forEach(function (n) { n.setAttribute('aria-label', t(n.getAttribute('data-i18n-label'))); });
    (root || document).querySelectorAll('[data-i18n-title]').forEach(function (n) { n.setAttribute('title', t(n.getAttribute('data-i18n-title'))); });
  }
  function onLang(fn) { listeners.push(fn); }
  function refresh() { applyI18n(); syncTools(); listeners.forEach(function (fn) { fn(); }); }

  function syncTools() {
    document.querySelectorAll('[data-set]').forEach(function (b) {
      var kv = b.getAttribute('data-set').split(':');
      b.setAttribute('aria-pressed', String(A.state[kv[0]] === kv[1]));
    });
  }
  function initChrome() {
    var btn = document.getElementById('appBtn'), panel = document.getElementById('appPanel');
    if (btn && panel) {
      var close = function () { panel.hidden = true; btn.setAttribute('aria-expanded', 'false'); };
      btn.addEventListener('click', function () {
        panel.hidden = !panel.hidden; btn.setAttribute('aria-expanded', String(!panel.hidden));
      });
      document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !panel.hidden) { close(); btn.focus(); } });
      document.addEventListener('click', function (e) { if (!panel.hidden && !panel.contains(e.target) && e.target !== btn && !btn.contains(e.target)) close(); });
    }
    document.querySelectorAll('[data-set]').forEach(function (b) {
      b.addEventListener('click', function () {
        var kv = b.getAttribute('data-set').split(':');
        A.set(kv[0], kv[1]);
        refresh();
      });
    });
    refresh();
  }

  var cache = {};
  function load(name) {
    if (!cache[name]) {
      cache[name] = fetch('data/' + name + '.json', { credentials: 'omit' }).then(function (r) {
        if (!r.ok) throw new Error(name + ': HTTP ' + r.status);
        return r.json();
      });
    }
    return cache[name];
  }

  // Live status from the AmpereArchive: no cookies, no referrer. A point is
  // matched by point_id plus a site id equal to, or ending in "-" + the site's
  // external id; anything ambiguous keeps the weekly status.
  var LIVE_MAX_AGE_MIN = 180;
  function liveUrl() {
    var m = document.querySelector('meta[name="nap-live-origin"]');
    return m ? m.getAttribute('content') + '/v1/PT/status.json.gz' : null;
  }
  function applyLive(obj, points, now) {
    if (!obj || typeof obj !== 'object' || !obj.points || typeof obj.points !== 'object') return null;
    var pub = Date.parse(obj.publishedAt);
    if (!isFinite(pub)) return null;
    if (((now || Date.now()) - pub) > LIVE_MAX_AGE_MIN * 60000) return { stale: true, t: pub };
    var idx = new Map();
    Object.keys(obj.points).forEach(function (k) {
      var i = k.indexOf('/'); if (i < 1) return;
      var pt = k.slice(i + 1); if (!idx.has(pt)) idx.set(pt, []); idx.get(pt).push(k.slice(0, i));
    });
    var n = 0;
    points.forEach(function (p) {
      var c = (idx.get(p.point_id) || []).filter(function (s) { return s === p.site_external_id || s.endsWith('-' + p.site_external_id); });
      if (c.length !== 1) return;
      var v = obj.points[c[0] + '/' + p.point_id], st = v && v.s;
      p.nap_site = c[0];   // the NAP site id (EZC-AMD-00051): Procurar's usage history is keyed by it
      if (typeof st === 'string' && STATUSES.indexOf(st) >= 0) { p.status = st; n++; }
    });
    return n ? { stale: false, t: pub, n: n, m: points.length } : null;
  }
  // A JSON file, 15 s at most, no cookies, no referrer. A .json.gz may arrive
  // still gzipped (served as a file, not with Content-Encoding).
  function fetchJson(url, cache) {
    if (typeof fetch !== 'function') return Promise.reject(new Error('no fetch'));
    var ctl = typeof AbortController === 'function' ? new AbortController() : null;
    var timer = ctl && setTimeout(function () { ctl.abort(); }, 15000);
    return fetch(url, { signal: ctl ? ctl.signal : undefined, credentials: 'omit', referrerPolicy: 'no-referrer', cache: cache || 'default' })
      .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.arrayBuffer(); })
      .then(function (buf) {
        var u = new Uint8Array(buf);
        if (u[0] === 0x1f && u[1] === 0x8b) {
          if (typeof DecompressionStream !== 'function') throw new Error('no DecompressionStream');
          return new Response(new Blob([buf]).stream().pipeThrough(new DecompressionStream('gzip'))).json();
        }
        return JSON.parse(new TextDecoder().decode(u));
      })
      .finally(function () { if (timer) clearTimeout(timer); });
  }
  function fetchLive(points) {
    var url = liveUrl();
    if (window.NAP_NO_LIVE || !url) return Promise.resolve(null);
    return fetchJson(url, 'no-cache')
      .then(function (obj) { return applyLive(obj, points); })
      .catch(function () { return null; });
  }
  function liveNote(node, res, snapshot) {
    var snap = Date.parse(snapshot);
    var st = isFinite(snap) ? when(snap) : String(snapshot || '');
    node.textContent = !res ? t('liveOff', { t: st }) : res.stale ? t('liveStale', { t: st })
      : t('liveOk', { t: when(res.t), n: nf(res.n), m: nf(res.m) });
  }

  // The id people see on a socket: its EVSE code (PT*TSL*E000T2X), the one on
  // the sticker. point_id stays the key (live status, history shards), but some
  // operators publish UUIDs or bare numbers there. Older points.json has no evse.
  function sockId(p) { return p.evse || p.point_id; }

  window.NAP = { t: t, sockId: sockId, addStrings: addStrings, lang: lang, nf: nf, eur: eur, prices: prices, priceText: priceText, sessionCost: sessionCost, PRICE_KINDS: PRICE_KINDS, when: when, el: el, add: add, clear: clear, md: md,
    status: status, pwLabel: pwLabel, PW: PW, STATUSES: STATUSES, onLang: onLang, initChrome: initChrome,
    applyI18n: applyI18n, load: load, fetchLive: fetchLive, applyLive: applyLive, liveNote: liveNote, fetchJson: fetchJson };
})();
