"""Draw the link-preview image (assets/og.png, 1200x630) from the committed site data.

    python3 scripts/make_og_image.py [--chromium PATH]

X, WhatsApp, Facebook and LinkedIn show this image when someone shares a page
of the site (the og:image/twitter:image tags that build_site.py writes). It is
the mainland outline with a dot per charging site (site/data/outline.json +
sites.json) next to the site's name, in the site's colours and font. No counts
on it: the image is committed and would go out of date. Run it by hand when
the look changes; the build only copies it. Stdlib only, plus a Chromium binary
to rasterise (`chromium`, or --chromium / $CHROMIUM).
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
W, H = 1200, 630
# The map's box, on the right of the card. Mainland Portugal only: the islands
# would shrink it to nothing at this size.
MAP = (760, 40, 400, 550)  # x, y, w, h


def project(lon_lat, bounds, box):
    """Equirectangular, with longitude scaled by cos(latitude) so the shape isn't stretched."""
    (lo0, la0, lo1, la1), (x, y, w, h) = bounds, box
    k = 0.77  # cos(39.6°), the middle of the mainland
    sx, sy = (lo1 - lo0) * k, la1 - la0
    s = min(w / sx, h / sy)
    ox, oy = x + (w - sx * s) / 2, y + (h - sy * s) / 2
    return lambda lon, lat: (ox + (lon - lo0) * k * s, oy + (la1 - lat) * s)


def svg(outline, sites):
    rings = outline['outline']['mainland']
    lons = [p[0] for r in rings for p in r]
    lats = [p[1] for r in rings for p in r]
    pr = project(None, (min(lons), min(lats), max(lons), max(lats)), MAP)
    paths = ''.join('M' + 'L'.join(f'{x:.1f},{y:.1f}' for x, y in (pr(*p) for p in r)) + 'Z' for r in rings)
    dots = ''.join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6"/>'
                   for x, y in (pr(s['lon'], s['lat']) for s in sites
                                if s.get('region') == 'mainland' and s.get('lat') is not None
                                and s.get('status') not in ('planned', 'removed')))
    return (f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position:absolute;inset:0">'
            f'<path d="{paths}" fill="#f1e9df" stroke="#e3d6c8" stroke-width="1"/>'
            f'<g fill="#c2410c" fill-opacity=".55">{dots}</g></svg>')


def page(outline, sites):
    font = (ROOT / 'assets/site/fonts/nunito-latin.woff2').as_uri()
    bolt = '<path d="M13 2 5 13h6l-1 9 8-11h-6z"/>'
    return f"""<!doctype html><meta charset="utf-8"><style>
@font-face {{ font-family: Nunito; src: url("{font}") format("woff2"); font-weight: 200 1000; }}
html, body {{ margin: 0; width: {W}px; height: {H}px; overflow: hidden; background: #fbfaf5; }}
body {{ position: relative; font-family: Nunito, sans-serif; color: #14203a; }}
.txt {{ position: absolute; left: 80px; top: 0; bottom: 0; width: 640px; display: flex;
        flex-direction: column; justify-content: center; }}
.brand {{ display: flex; align-items: center; gap: 14px; font-weight: 800; font-size: 34px; }}
.brand span.tile {{ width: 56px; height: 56px; border-radius: 14px; background: #0f172a;
                    display: grid; place-items: center; }}
h1 {{ font-size: 70px; line-height: 1.05; font-weight: 900; margin: 34px 0 22px; letter-spacing: -1px; }}
p {{ font-size: 30px; line-height: 1.35; color: #56627a; margin: 0; }}
.url {{ margin-top: 34px; font-size: 26px; font-weight: 800; color: #c2410c; }}
</style><body>{svg(outline, sites)}
<div class="txt">
  <div class="brand"><span class="tile"><svg width="34" height="34" viewBox="0 0 24 24" fill="#38bdf8">{bolt}</svg></span>Postos PT</div>
  <h1>Postos de carregamento em Portugal</h1>
  <p>Onde estão, se estão livres agora e quanto custam. Dados oficiais do NAP.</p>
  <div class="url">nap.ocarroeletrico.com</div>
</div></body>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--chromium', default=os.environ.get('CHROMIUM') or shutil.which('chromium') or 'chromium')
    ap.add_argument('--out', default=str(ROOT / 'assets/og.png'))
    a = ap.parse_args()
    outline = json.loads((ROOT / 'site/data/outline.json').read_text(encoding='utf-8'))
    sites = json.loads((ROOT / 'site/data/sites.json').read_text(encoding='utf-8'))['sites']
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / 'og.html'
        src.write_text(page(outline, sites), encoding='utf-8')
        subprocess.run([a.chromium, '--headless', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
                        f'--window-size={W},{H}', f'--screenshot={a.out}', src.as_uri()],
                       check=True, capture_output=True)
    print('escrito', a.out, file=sys.stderr)


if __name__ == '__main__':
    main()
