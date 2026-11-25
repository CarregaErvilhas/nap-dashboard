"""As fotos principais do olh'o'posto em scripts/charger_photos.py."""
import json
import os
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import charger_photos as cp  # noqa: E402

JPEG = b'\xff\xd8\xff\xe0' + b'0' * 100
PIC = 'https://pictures.ocarroeletrico.com/'


def feed(published='2000-01-02T00:00:00Z', extra=()):
    return {'license': 'CC-BY-SA-4.0', 'photos': [
        {'target': 'EZC-AMD-00051', 'station': {'id': 'EZC-AMD-00051', 'code': 'AMD-00051'}, 'credit': 'Ana',
         'thumb': PIC + 'EZC-AMD-00051.thumb.jpg', 'page': 'https://olhaoposto.ocarroeletrico.com/postos/EZC-AMD-00051',
         'panoramax': 'abc-1', 'publishedAt': published},
        # Foto de uma tomada: fica no olh'o'posto.
        {'target': 'PTEZCEAMD000511', 'station': {'id': 'EZC-AMD-00051', 'code': 'AMD-00051'},
         'thumb': PIC + 'PTEZCEAMD000511.thumb.jpg', 'publishedAt': published},
        # Miniatura fora do pictures.*: não se descarrega.
        {'target': 'X-1', 'station': {'id': 'X-1'}, 'thumb': 'https://example.org/x.jpg', 'publishedAt': published},
        *extra]}


class OlhaOPostoPhotosTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        d = self.tmp.name
        self.patches = [mock.patch.multiple(cp, DUMP=os.path.join(d, 'none.json'), MODEL_PHOTOS=os.path.join(d, 'none.json'),
                                            DIR=os.path.join(d, 'photos'), INDEX=os.path.join(d, 'photos.json')),
                        mock.patch.object(cp.time, 'sleep')]
        for p in self.patches:
            p.start()
        self.calls = []

    def tearDown(self):
        for p in self.patches:
            p.stop()
        self.tmp.cleanup()

    def run_with(self, api):
        def get(url, tries=3):
            self.calls.append(url)
            if url == cp.OLHAOPOSTO_API:
                if isinstance(api, Exception):
                    raise api
                return json.dumps(api).encode()
            return JPEG
        with mock.patch.object(cp, 'get', get), mock.patch('builtins.print'):
            cp.main()
        with open(cp.INDEX) as f:
            return json.load(f)

    def test_station_main_photo_is_copied_with_credit_licence_and_map(self):
        index = self.run_with(feed())
        self.assertEqual(list(index), ['olhaoposto:EZC-AMD-00051'])
        e = index['olhaoposto:EZC-AMD-00051']
        self.assertTrue(os.path.exists(os.path.join(cp.DIR, os.path.basename(e['src']))))
        self.assertEqual(e['credit'], 'Ana')
        self.assertEqual(e['license'], 'CC BY-SA 4.0')
        self.assertEqual(e['map'], 'https://panoramax.ocarroeletrico.com/viewer?focus=map&pic=abc-1')
        self.assertEqual(self.calls, [cp.OLHAOPOSTO_API, PIC + 'EZC-AMD-00051.thumb.jpg'])

    def test_same_photo_is_not_downloaded_again_but_a_new_one_is(self):
        self.run_with(feed())
        self.calls.clear()
        self.run_with(feed())
        self.assertEqual(self.calls, [cp.OLHAOPOSTO_API])
        self.calls.clear()
        index = self.run_with(feed(published='2000-02-01T00:00:00Z'))
        self.assertEqual(self.calls, [cp.OLHAOPOSTO_API, PIC + 'EZC-AMD-00051.thumb.jpg'])
        self.assertEqual(index['olhaoposto:EZC-AMD-00051']['published'], '2000-02-01T00:00:00Z')

    def test_olhaoposto_down_keeps_the_photos_it_had(self):
        self.run_with(feed())
        index = self.run_with(OSError('down'))
        self.assertIn('olhaoposto:EZC-AMD-00051', index)
        self.assertTrue(os.listdir(cp.DIR))

    def test_a_photo_no_longer_listed_leaves_the_site(self):
        self.run_with(feed())
        index = self.run_with({'license': 'CC-BY-SA-4.0', 'photos': []})
        self.assertEqual(index, {})
        self.assertEqual(os.listdir(cp.DIR), [])


if __name__ == '__main__':
    unittest.main()
