// /posto-<id>.html (scripts/share_pages.py) only holds a site's link-preview
// tags: send people on to the site's detail on the home page, keeping any other
// parameter (?lang=en). Crawlers don't run it.
(function () {
  var m = /^\/posto-([A-Za-z0-9][A-Za-z0-9._-]{0,63})\.html$/.exec(location.pathname);
  var p = new URLSearchParams(location.search);
  if (m) p.set('posto', m[1]);
  var q = p.toString();
  location.replace('/' + (q ? '?' + q : '') + location.hash);
})();
