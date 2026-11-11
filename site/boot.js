// Runs in <head>, before first paint: theme, vision mode and language, so the
// page never flashes the wrong one. Values are checked against a closed list
// because localStorage can hold anything (another script, an old version).
window.NAPAPP = (function () {
  var OPT = { theme: ['auto', 'light', 'dark'], vision: ['default', 'cb', 'hc'], lang: ['pt', 'en'] };
  function get(k) {
    var v = null;
    try { v = localStorage.getItem('nap-' + k); } catch (e) {}
    return OPT[k].indexOf(v) >= 0 ? v : null;
  }
  function detectLang() {
    var q = /[?&]lang=(pt|en)\b/.exec(location.search);
    if (q) return q[1];
    var s = get('lang');
    if (s) return s;
    return /^pt/i.test(navigator.language || '') ? 'pt' : 'en';
  }
  var state = { theme: get('theme') || 'auto', vision: get('vision') || 'default', lang: detectLang() };
  function apply() {
    var r = document.documentElement;
    if (state.theme === 'auto') r.removeAttribute('data-theme'); else r.setAttribute('data-theme', state.theme);
    if (state.vision === 'default') r.removeAttribute('data-vision'); else r.setAttribute('data-vision', state.vision);
    r.setAttribute('lang', state.lang);
  }
  function set(k, v) {
    if (!OPT[k] || OPT[k].indexOf(v) < 0) return;
    state[k] = v;
    try { localStorage.setItem('nap-' + k, v); } catch (e) {}
    apply();
  }
  apply();
  return { state: state, set: set, OPT: OPT };
})();
