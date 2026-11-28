// /posto/<id>/ (scripts/share_pages.py) only holds a site's link-preview tags:
// send people on to the site's detail on the home page. Crawlers don't run it.
(function () {
  var m = /^\/posto\/([A-Za-z0-9][A-Za-z0-9._-]{0,63})\/?$/.exec(location.pathname);
  location.replace('/' + (m ? '?posto=' + encodeURIComponent(m[1]) : '') + location.hash);
})();
