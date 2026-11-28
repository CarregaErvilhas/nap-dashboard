"""Testes das páginas de partilha /posto-<id>.html (scripts/share_pages.py).

Cada página só tem as etiquetas de pré-visualização do posto e o posto.js, que
leva para /?posto=<id>. Nomes, operadores e créditos vêm de terceiros: têm de
sair escapados, e cada página tem de passar as regras do validate_site.
Corre com `venv/bin/python -m unittest discover -s tests`.
"""
import json
import os
import sys
import tempfile
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.insert(0, os.path.join(ROOT, 'scripts'))

import share_pages  # noqa: E402

PHOTO = 'photos/0123456789abcdef.jpg'


def site(**kw):
    s = {'ext': 'AMD-00051', 'oop': 'EZC-AMD-00051', 'name': 'Alfragide', 'city': 'Amadora',
         'op': 'EZC', 'npts': 2, 'kw': 50.0,
         'ph': [{'src': PHOTO, 'credit': 'Ana', 'license': 'CC-BY-SA-4.0'}]}
    s.update(kw)
    return s


class SharePages(unittest.TestCase):
    def setUp(self):
        cwd = os.getcwd()
        os.chdir(ROOT)  # build_site.OG_IMAGE is relative to the repo root
        self.addCleanup(os.chdir, cwd)
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.public = tmp.name
        os.makedirs(os.path.join(self.public, 'photos'))
        with open(os.path.join(self.public, PHOTO), 'wb') as fh:
            fh.write(b'\xff\xd8jpeg')

    def test_photo_with_credit_and_hash(self):
        page = share_pages.render(site(), self.public)
        self.assertIn('<meta property="og:image" content="https://nap.ocarroeletrico.com/' + PHOTO + '?v=', page)
        self.assertIn('content="Foto do posto AMD-00051 · © Ana, CC BY-SA 4.0"', page)
        self.assertIn('<meta property="og:url" content="https://nap.ocarroeletrico.com/posto-EZC-AMD-00051.html">', page)
        self.assertIn('<meta name="description" content="EZC · Amadora · 2 tomadas · até 50 kW">', page)
        self.assertIn('<title>Alfragide (AMD-00051) · Postos PT</title>', page)
        self.assertIn('<a href="/?posto=EZC-AMD-00051">', page)
        self.assertEqual(share_pages.check('p', page), [])

    def test_no_photo_file_falls_back_to_og_png(self):
        for s in (site(ph=[]), site(ph=[{'src': 'photos/ffffffffffffffff.jpg'}]),
                  site(ph=[{'src': '../etc/passwd'}])):
            page = share_pages.render(s, self.public)
            self.assertIn('content="https://nap.ocarroeletrico.com/og.png?v=', page)
            self.assertIn('content="image/png"', page)

    def test_third_party_text_is_escaped(self):
        evil = '"><script>alert(1)</script>'
        page = share_pages.render(site(name=evil, op=evil, city=evil,
                                       ph=[{'src': PHOTO, 'credit': evil}]), self.public)
        self.assertNotIn('<script>alert', page)
        self.assertEqual(share_pages.check('p', page), [])

    def test_only_safe_unique_ids(self):
        made = share_pages.pages([site(), site(), site(oop='../x'), site(oop='a/b'), site(oop=None),
                                  site(oop='OSM-w123')], self.public)
        self.assertEqual(sorted(made), ['EZC-AMD-00051', 'OSM-w123'])

    def test_check_rejects_inline_script(self):
        page = share_pages.render(site(), self.public).replace(
            '<script src="/posto.js"></script>', '<script>alert(1)</script>')
        self.assertTrue(share_pages.check('p', page))

    def test_write(self):
        sdir = os.path.join(self.public, 'site')
        os.makedirs(os.path.join(sdir, 'data'))
        with open(os.path.join(sdir, 'data', 'sites.json'), 'w') as fh:
            json.dump({'sites': [site()]}, fh)
        with self.assertRaises(SystemExit):  # posto.js not staged yet
            share_pages.write(sdir, self.public)
        open(os.path.join(self.public, 'posto.js'), 'w').close()
        open(os.path.join(self.public, 'posto-OLD-1.html'), 'w').close()  # a site that left
        share_pages.write(sdir, self.public)
        self.assertEqual(sorted(f for f in os.listdir(self.public) if f.startswith('posto')),
                         ['posto-EZC-AMD-00051.html', 'posto.js'])


if __name__ == '__main__':
    unittest.main()
