"""apply_archive_origin: a origem do AmpereArchive vai para a CSP e para a meta nap-live-origin."""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
import dashboard_payload as dp  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), '..')


class ArchiveOriginTest(unittest.TestCase):
    def tmpl(self):
        # O <head> comum a todas as páginas do site (build_site.py aplica a troca).
        with open(os.path.join(ROOT, 'assets', 'site', '_head.html'), encoding='utf-8') as fh:
            return fh.read()

    def test_unset_keeps_template(self):
        t = self.tmpl()
        self.assertEqual(dp.apply_archive_origin(t, None), t)
        self.assertEqual(dp.apply_archive_origin(t, ''), t)

    def test_replaces_csp_and_live_origin(self):
        out = dp.apply_archive_origin(self.tmpl(), 'https://Archive.Example.org/')
        self.assertIn("connect-src 'self' https://archive.example.org;", out)
        self.assertIn('<meta name="nap-live-origin" content="https://archive.example.org">', out)
        self.assertNotIn(dp.ARCHIVE_ORIGIN_DEFAULT, out)

    def test_rejects_anything_but_a_clean_https_origin(self):
        for bad in ('http://x.org', 'https://x.org/path', "https://x.org';alert(1)//",
                    'https://x.org; script-src *', 'https://localhost', 'javascript:alert(1)',
                    'https://x.org"><script>'):
            with self.assertRaises(ValueError, msg=bad):
                dp.apply_archive_origin(self.tmpl(), bad)


if __name__ == '__main__':
    unittest.main()
