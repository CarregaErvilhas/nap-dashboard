"""Draw the link-preview image (assets/og.png, 1200x630) from the committed site data,
and the raster icons (assets/favicon.ico, assets/apple-touch-icon.png, assets/icon-*.png) from the mascot.

    python3 scripts/make_og_image.py [--chromium PATH]

The mascot is assets/favicon.svg: a map pin with a face and the group's
lightning bolt, like the other sites' (ohmigo's plug, Voltaria's book, the
reporter car of ocarroeletrico.com). The header shows it as is; browsers that
can't use an SVG favicon, and iPhones' home screens, get the PNG/ICO drawn here.

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
import struct
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
W, H = 1200, 630
# The map's box, on the right of the card. Mainland Portugal only: the islands
# would shrink it to nothing at this size.
MAP = (760, 40, 400, 550)  # x, y, w, h
MASCOT_H = 230


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
    # The mascot is a map pin: its tip marks Lisbon. In the SVG's viewBox (24 8 212 252) the tip
    # is at (130, 248), so at MASCOT_H px tall it sits 106/212 of the width in and 240/252 down.
    lx, ly = pr(-9.14, 38.72)
    mw = MASCOT_H * 212 / 252
    pin = (f'<img src="{(ROOT / "assets/favicon.svg").as_uri()}" alt="" style="position:absolute;'
           f'left:{lx - mw * 106 / 212:.0f}px;top:{ly - MASCOT_H * 240 / 252:.0f}px;height:{MASCOT_H}px;'
           f'z-index:1;filter:drop-shadow(0 10px 12px rgba(15,23,42,.18))">')
    return pin + (f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position:absolute;inset:0">'
            f'<path d="{paths}" fill="#f1e9df" stroke="#e3d6c8" stroke-width="1"/>'
            f'<g fill="#c2410c" fill-opacity=".55">{dots}</g></svg>')


def page(outline, sites):
    font = (ROOT / 'assets/site/fonts/nunito-latin.woff2').as_uri()
    return f"""<!doctype html><meta charset="utf-8"><style>
@font-face {{ font-family: Nunito; src: url("{font}") format("woff2"); font-weight: 200 1000; }}
html, body {{ margin: 0; width: {W}px; height: {H}px; overflow: hidden; background: #fbfaf5; }}
body {{ position: relative; font-family: Nunito, sans-serif; color: #14203a; }}
.txt {{ position: absolute; left: 80px; top: 0; bottom: 0; width: 640px; display: flex;
        flex-direction: column; justify-content: center; }}
.brand {{ display: flex; align-items: center; gap: 14px; font-weight: 800; font-size: 34px; }}
h1 {{ font-size: 70px; line-height: 1.05; font-weight: 900; margin: 34px 0 22px; letter-spacing: -1px; }}
p {{ font-size: 30px; line-height: 1.35; color: #56627a; margin: 0; }}
.url {{ margin-top: 34px; font-size: 26px; font-weight: 800; color: #c2410c; }}
</style><body>{svg(outline, sites)}
<div class="txt">
  <div class="brand">Postos PT</div>
  <h1>Postos de carregamento em Portugal</h1>
  <p>Onde estão, se estão livres agora e quanto custam. Dados oficiais do NAP.</p>
  <div class="url">nap.ocarroeletrico.com</div>
</div></body>"""


def shot(chromium, html, size, out, transparent):
    """Screenshot an HTML string at size x size."""
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / 'p.html'
        src.write_text(html, encoding='utf-8')
        args = [chromium, '--headless', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
                f'--window-size={size},{size}', f'--screenshot={out}', src.as_uri()]
        if transparent:
            args.insert(2, '--default-background-color=00000000')
        subprocess.run(args, check=True, capture_output=True)


def icon_html(size, share, background):
    """The mascot centred in a square, filling `share` of its height."""
    svg = (ROOT / 'assets/favicon.svg').as_uri()
    return (f'<!doctype html><body style="margin:0;width:{size}px;height:{size}px;display:grid;'
            f'place-items:center;background:{background}"><img src="{svg}" style="height:{size * share:.0f}px">')


def icons(chromium):
    """favicon.ico (16, 32 and 48 px, transparent), apple-touch-icon.png (180 px on the page's
    background, with room around: iOS rounds the corners) and the manifest's PNG icons."""
    shot(chromium, icon_html(180, .78, '#fbfaf5'), 180, ROOT / 'assets/apple-touch-icon.png', False)
    # The manifest's icons for "Instalar app" (Chrome wants 192 and 512 px PNGs). The maskable one
    # keeps the mascot inside the central 80 % circle that Android may crop the icon to.
    shot(chromium, icon_html(192, .78, '#fbfaf5'), 192, ROOT / 'assets/icon-192.png', False)
    shot(chromium, icon_html(512, .78, '#fbfaf5'), 512, ROOT / 'assets/icon-512.png', False)
    shot(chromium, icon_html(512, .6, '#fbfaf5'), 512, ROOT / 'assets/icon-maskable-512.png', False)
    pngs = []
    with tempfile.TemporaryDirectory() as tmp:
        for s in (16, 32, 48):
            p = Path(tmp) / f'{s}.png'
            shot(chromium, icon_html(s, 1, 'transparent'), s, p, True)
            pngs.append((s, p.read_bytes()))
    # ICO with PNG entries (every browser since IE Vista reads them): a 6-byte header,
    # a 16-byte entry per image, then the PNGs.
    head = struct.pack('<HHH', 0, 1, len(pngs))
    off, dirs = 6 + 16 * len(pngs), b''
    for s, data in pngs:
        dirs += struct.pack('<BBBBHHII', s, s, 0, 0, 1, 32, len(data), off)
        off += len(data)
    (ROOT / 'assets/favicon.ico').write_bytes(head + dirs + b''.join(d for _, d in pngs))


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
    icons(a.chromium)
    print('escrito', a.out, 'favicon.ico, apple-touch-icon.png, icon-*.png', file=sys.stderr)


if __name__ == '__main__':
    main()
