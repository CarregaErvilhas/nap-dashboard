// Shared by every page: translations, DOM helpers, data loading, live status.
// Rule for the whole front end: text that comes from data goes in through
// textContent (el() below). OSM and operator names are third-party input.
'use strict';
(function () {
  var A = window.NAPAPP;
  var STR = {
    pt: {
      navFind: 'Procurar', navNet: 'Rede', navOps: 'Operadores',
      appearance: 'Aparência', theme: 'Tema', vision: 'Visão', auto: 'Automático', light: 'Claro', dark: 'Escuro',
      vdefault: 'Padrão', cb: 'Daltonismo', hc: 'Alto contraste', language: 'Idioma',
      liveOk: 'Estado ao vivo de {t} ({n} de {m} tomadas).', liveStale: 'Estado ao vivo indisponível: a mostrar o da semana ({t}).',
      liveOff: 'Sem ligação ao estado ao vivo: a mostrar o retrato de {t}.', loading: 'A carregar…',
      loadFail: 'Não foi possível carregar os dados. Verifica a ligação e recarrega a página.',
      st_available: 'Livre', st_charging: 'A carregar', st_outOfOrder: 'Avariado', st_inoperative: 'Inoperacional',
      st_unknown: 'Sem informação', st_blocked: 'Bloqueado', st_planned: 'Planeado', st_removed: 'Removido',
      rg_mainland: 'Continente', rg_madeira: 'Madeira', rg_azores: 'Açores', rg_OUTSIDE: 'Fora de PT',
      pw0: 'AC lento (<22 kW)', pw1: 'AC/DC 22–50 kW', pw2: 'DC rápido 50–150 kW', pw3: 'DC ultra 150–350 kW', pw4: 'DC ultra (≥350 kW)',
      pay_App: 'App', 'pay_Multibanco/contactless': 'Multibanco/contactless', pay_Dinheiro: 'Dinheiro',
      'pay_Cartão RFID eMSP': 'Cartão do comercializador (RFID)', 'pay_Sem autenticação': 'Sem autenticação'
    },
    en: {
      navFind: 'Find', navNet: 'Network', navOps: 'Operators',
      appearance: 'Appearance', theme: 'Theme', vision: 'Vision', auto: 'Automatic', light: 'Light', dark: 'Dark',
      vdefault: 'Default', cb: 'Colour-blind', hc: 'High contrast', language: 'Language',
      liveOk: 'Live status as of {t} ({n} of {m} sockets).', liveStale: 'Live status unavailable: showing this week\'s ({t}).',
      liveOff: 'No connection to live status: showing the snapshot of {t}.', loading: 'Loading…',
      loadFail: 'Could not load the data. Check your connection and reload the page.',
      st_available: 'Free', st_charging: 'Charging', st_outOfOrder: 'Out of order', st_inoperative: 'Inoperative',
      st_unknown: 'No information', st_blocked: 'Blocked', st_planned: 'Planned', st_removed: 'Removed',
      rg_mainland: 'Mainland', rg_madeira: 'Madeira', rg_azores: 'Azores', rg_OUTSIDE: 'Outside PT',
      pw0: 'Slow AC (<22 kW)', pw1: 'AC/DC 22–50 kW', pw2: 'Fast DC 50–150 kW', pw3: 'Ultra DC 150–350 kW', pw4: 'Ultra DC (≥350 kW)',
      pay_App: 'App', 'pay_Multibanco/contactless': 'Bank card/contactless', pay_Dinheiro: 'Cash',
      'pay_Cartão RFID eMSP': 'Supplier card (RFID)', 'pay_Sem autenticação': 'No authentication'
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
      if (typeof st === 'string' && STATUSES.indexOf(st) >= 0) { p.status = st; n++; }
    });
    return n ? { stale: false, t: pub, n: n, m: points.length } : null;
  }
  function fetchLive(points) {
    var url = liveUrl();
    if (window.NAP_NO_LIVE || !url || typeof fetch !== 'function') return Promise.resolve(null);
    var ctl = typeof AbortController === 'function' ? new AbortController() : null;
    var timer = ctl && setTimeout(function () { ctl.abort(); }, 15000);
    return fetch(url, { signal: ctl ? ctl.signal : undefined, credentials: 'omit', referrerPolicy: 'no-referrer', cache: 'no-cache' })
      .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.arrayBuffer(); })
      .then(function (buf) {
        var u = new Uint8Array(buf);
        if (u[0] === 0x1f && u[1] === 0x8b) {
          if (typeof DecompressionStream !== 'function') throw new Error('no DecompressionStream');
          return new Response(new Blob([buf]).stream().pipeThrough(new DecompressionStream('gzip'))).json();
        }
        return JSON.parse(new TextDecoder().decode(u));
      })
      .then(function (obj) { return applyLive(obj, points); })
      .catch(function () { return null; })
      .then(function (r) { if (timer) clearTimeout(timer); return r; });
  }
  function liveNote(node, res, snapshot) {
    var snap = Date.parse(snapshot);
    var st = isFinite(snap) ? when(snap) : String(snapshot || '');
    node.textContent = !res ? t('liveOff', { t: st }) : res.stale ? t('liveStale', { t: st })
      : t('liveOk', { t: when(res.t), n: nf(res.n), m: nf(res.m) });
  }

  window.NAP = { t: t, addStrings: addStrings, lang: lang, nf: nf, when: when, el: el, add: add, clear: clear, md: md,
    status: status, pwLabel: pwLabel, PW: PW, STATUSES: STATUSES, onLang: onLang, initChrome: initChrome,
    applyI18n: applyI18n, load: load, fetchLive: fetchLive, applyLive: applyLive, liveNote: liveNote };
})();
