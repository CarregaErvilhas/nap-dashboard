"""Testes dos códigos NAP que a comunidade escreve num posto em construção.

osm_planned.codes_of lê-os no `ref` e no nome do OSM. É o que deixa o
?posto=ALM-00114 encontrar um posto que ainda não está no NAP, e o olh'o'posto
fundi-lo no posto do NAP quando ele chega. Os casos são nomes reais do dump.
Corre com `venv/bin/python -m unittest discover -s tests`.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from osm_planned import codes_of  # noqa: E402


class Codes(unittest.TestCase):
    def test_slash_replaces_the_last_digits(self):
        self.assertEqual(codes_of('SXL-00085/86'), ['SXL-00085', 'SXL-00086'])
        self.assertEqual(codes_of('ALM-00114/155'), ['ALM-00114', 'ALM-00155'])
        self.assertEqual(codes_of('LSB-01181/1182'), ['LSB-01181', 'LSB-01182'])
        self.assertEqual(codes_of('GDM-00074/75/76'), ['GDM-00074', 'GDM-00075', 'GDM-00076'])

    def test_ellipsis_is_an_inclusive_range(self):
        self.assertEqual(codes_of('MLD-00036…39'), ['MLD-00036', 'MLD-00037', 'MLD-00038', 'MLD-00039'])
        self.assertEqual(len(codes_of('ABF-00100…108')), 9)
        self.assertEqual(codes_of('ABF-00100...102'), ['ABF-00100', 'ABF-00101', 'ABF-00102'])

    def test_a_long_range_keeps_only_its_first_code(self):
        self.assertEqual(codes_of('LSB-00100…199'), ['LSB-00100'])

    def test_ref_and_name_together_without_repeats(self):
        self.assertEqual(codes_of('ALM-00114', 'Posto ALM-00114/155'), ['ALM-00114', 'ALM-00155'])
        self.assertEqual(codes_of('MOBI-CHV-00002', ''), ['CHV-00002'])

    def test_text_without_a_code(self):
        self.assertEqual(codes_of('', None, 'Supercharger Leiria', 'A-1234', 'ABC-123456'), [])


if __name__ == '__main__':
    unittest.main()
