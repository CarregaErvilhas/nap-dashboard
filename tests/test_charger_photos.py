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


class PanoramaxFallbackTest(unittest.TestCase):
    """Um `panoramax=` que a pesquisa federada não conhece procura-se no
    Panoramax do olh'o'posto (fora da federação)."""

    def feature(self, uid, host, semantics=()):
        return {'id': uid, 'assets': {'thumb': {'href': f'{host}/api/pictures/{uid}/thumb.jpg'}},
                'providers': [{'name': 'OlhaOPosto', 'roles': ['producer']}],
                'properties': {'license': 'CC-BY-SA-4.0', 'datetime': '2026-11-20T10:00:00Z',
                               'semantics': list(semantics)}}

    def run_with(self, federated, ours):
        calls = []

        def get(url, tries=3):
            calls.append(url)
            if url.startswith(cp.PANORAMAX_API):
                if isinstance(federated, Exception):
                    raise federated
                return json.dumps({'features': federated}).encode()
            if url.startswith(cp.PANORAMAX_OOP + '/api/search?'):
                return json.dumps({'features': ours}).encode()
            raise AssertionError(url)
        with mock.patch.object(cp, 'get', get), mock.patch('builtins.print'):
            return cp.panoramax(['fed-1', 'oop-1']), calls

    def test_missing_from_the_federation_is_asked_to_our_server(self):
        fed = self.feature('fed-1', 'https://other.example')
        fed['providers'] = [{'name': 'mapcomplete', 'roles': ['producer']}, {'name': 'Rui', 'roles': ['producer']}]
        ours = self.feature('oop-1', cp.PANORAMAX_OOP, [{'key': 'OlhaOPosto|author', 'value': 'Ana'}])
        out, calls = self.run_with([fed], [ours])
        self.assertEqual(out['fed-1']['credit'], 'Rui')
        self.assertEqual(out['oop-1']['credit'], 'Ana')
        self.assertEqual(out['oop-1']['page'], f'{cp.PANORAMAX_OOP}/viewer?focus=map&pic=oop-1')
        self.assertEqual(out['oop-1']['taken'], '2026-11-20')
        # Só o que faltou vai ao nosso servidor.
        self.assertIn('ids=oop-1&', calls[1])
        self.assertEqual(len(calls), 2)

    def test_federation_down_still_asks_our_server(self):
        out, _ = self.run_with(OSError('down'), [self.feature('oop-1', cp.PANORAMAX_OOP)])
        self.assertEqual(list(out), ['oop-1'])
        self.assertEqual(out['oop-1']['credit'], 'OlhaOPosto')

    def test_a_thumb_off_our_server_is_ignored(self):
        out, _ = self.run_with([], [self.feature('oop-1', 'https://elsewhere.example')])
        self.assertEqual(out, {})


if __name__ == '__main__':
    unittest.main()
