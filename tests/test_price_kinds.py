"""Os tipos de preço de uma tomada (scripts/price_kinds.py)."""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import price_kinds as pk  # noqa: E402

MOBIE = {'regime': 'mobie', 'fees': {
    'REGULAR': {'flat': [0.4], 'energy': [0.13],
                'time': [{'eur': 0.18, 'from': 30, 'to': None}, {'eur': 0.0, 'from': 0, 'to': 30}]},
    'AD_HOC_PAYMENT': {'energy': [0.55]}}}
DIRECT = {'regime': 'sem_ceme', 'fees': None, 'nap': 0.37}
NAP_ONLY = {'regime': 'mobie_sem_tarifa', 'fees': None, 'nap_fees': {'kwh': 0.1, 'min': 0.02, 'flat': 0.26}}


class KindsTest(unittest.TestCase):
    def test_mobie_socket_has_the_operator_fee_and_the_no_contract_price(self):
        k = pk.kinds(MOBIE)
        self.assertEqual(sorted(k), ['adhoc', 'opc'])
        self.assertEqual(k['opc'], {'kwh': 0.13, 'min': 0.0, 'flat': 0.4})   # 1.º escalão por minuto
        self.assertEqual(k['adhoc'], {'kwh': 0.55, 'min': None, 'flat': None})

    def test_outside_mobie_is_one_price_and_nothing_else(self):
        self.assertEqual(pk.kinds(DIRECT), {'direct': {'kwh': 0.37, 'min': None, 'flat': None}})
        # Um plano que venha agarrado a uma tomada sem CEME não é taxa do operador.
        self.assertEqual(sorted(pk.kinds(dict(DIRECT, fees=MOBIE['fees']))), ['direct'])
        self.assertEqual(pk.kinds({'regime': 'sem_ceme', 'nap': None}), {})

    def test_nap_fee_only_where_mobie_has_no_tariff(self):
        self.assertEqual(pk.kinds(NAP_ONLY), {'napfee': {'kwh': 0.1, 'min': 0.02, 'flat': 0.26}})
        self.assertEqual(sorted(pk.kinds(dict(MOBIE, nap_fees={'kwh': 0.6}))), ['adhoc', 'opc'])
        self.assertEqual(pk.kinds({'regime': 'mobie_sem_tarifa', 'fees': None, 'nap_fees': None}), {})

    def test_nan_is_not_a_price(self):
        self.assertEqual(pk.kinds({'regime': 'sem_ceme', 'nap': float('nan')}), {})

    def test_stats_keep_the_kinds_apart(self):
        s = pk.stats([MOBIE, MOBIE, DIRECT, NAP_ONLY, {'regime': 'mobie', 'fees': {'REGULAR': {'flat': [0.26]}}}])
        self.assertEqual(s['opc'], {'n': 3, 'kwh_n': 2, 'mean': 0.13, 'max': 0.13})   # uma só tem parte fixa
        self.assertEqual(s['adhoc'], {'n': 2, 'kwh_n': 2, 'mean': 0.55, 'max': 0.55})
        self.assertEqual(s['direct']['mean'], 0.37)
        self.assertEqual(s['napfee']['kwh_n'], 1)

    def test_energy_included_is_known_for_three_kinds_only(self):
        self.assertEqual(pk.WITH_ENERGY, {'opc': False, 'adhoc': True, 'direct': True, 'napfee': None})


class NapFeesTest(unittest.TestCase):
    def test_reads_the_three_policies(self):
        rows = [('pricePerDeliveryUnit', '0.10'), ('flatRate', '0.26'), ('pricePerChargingTime', '0.02')]
        self.assertEqual(pk.nap_fees(rows), {'kwh': 0.1, 'flat': 0.26, 'min': 0.02})

    def test_ignores_what_it_does_not_know(self):
        self.assertIsNone(pk.nap_fees([('other', '1'), ('flatRate', 'x'), ('flatRate', 'nan')]))
        self.assertIsNone(pk.nap_fees(()))

    def test_first_value_of_a_policy_wins(self):
        self.assertEqual(pk.nap_fees([('flatRate', '0.26'), ('flatRate', '0.5')]), {'flat': 0.26})


if __name__ == '__main__':
    unittest.main()
