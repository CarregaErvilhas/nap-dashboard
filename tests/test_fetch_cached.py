"""fetch_cached (scripts/fetch_data.sh): conditional GET of the static NAP feed.

Runs the shell function itself with a stand-in `curl` on PATH, so no network.
"""
import os
import re
import stat
import subprocess
import tempfile
import unittest

SCRIPT = os.path.join(os.path.dirname(__file__), '..', 'scripts', 'fetch_data.sh')

# Answers with FAKE_CODE / FAKE_BODY / FAKE_ETAG and records the If-None-Match.
FAKE_CURL = r'''#!/usr/bin/env bash
while [ $# -gt 0 ]; do
  case "$1" in
    -H) printf '%s' "$2" > sent; shift ;;
    -D) headers="$2"; shift ;;
    -o) out="$2"; shift ;;
  esac
  shift
done
printf 'HTTP/2 301\r\netag: "redirect"\r\n\r\nHTTP/2 %s\r\n' "$FAKE_CODE" > "$headers"
[ -n "$FAKE_ETAG" ] && printf 'ETag: %s\r\n' "$FAKE_ETAG" >> "$headers"
[ -n "$FAKE_BODY" ] && printf '%s' "$FAKE_BODY" > "$out"
printf '%s' "$FAKE_CODE"
[ "$FAKE_CODE" -lt 400 ] || exit 22
'''

OLD = '<?xml version="1.0"?><old/>'
NEW = '<?xml version="1.0"?><new/>'


def functions():
    with open(SCRIPT, encoding='utf-8') as fh:
        text = fh.read()
    return '\n'.join(re.search(rf'^{name}\(\) \{{.*?^\}}$', text, re.M | re.S).group(0)
                     for name in ('check_content', 'fetch_cached'))


class FetchCached(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.dir = tmp.name
        curl = self.path('curl')
        with open(curl, 'w') as fh:
            fh.write(FAKE_CURL)
        os.chmod(curl, os.stat(curl).st_mode | stat.S_IXUSR)

    def path(self, name):
        return os.path.join(self.dir, name)

    def put(self, name, text):
        with open(self.path(name), 'w') as fh:
            fh.write(text)

    def get(self, name):
        if not os.path.exists(self.path(name)):
            return None
        with open(self.path(name)) as fh:
            return fh.read()

    def run_fetch(self, code, body='', etag=''):
        env = dict(os.environ, PATH=self.dir + os.pathsep + os.environ['PATH'],
                   FAKE_CODE=str(code), FAKE_BODY=body, FAKE_ETAG=etag)
        shell = f'set -euo pipefail\n{functions()}\nfetch_cached https://example.invalid/x feed.xml xml\n'
        return subprocess.run(['bash', '-c', shell], cwd=self.dir, env=env,
                              capture_output=True, text=True).returncode

    def test_cache_miss_downloads_and_stores_etag(self):
        self.assertEqual(self.run_fetch(200, NEW, 'W/"b"'), 0)
        self.assertEqual((self.get('feed.xml'), self.get('feed.xml.etag'), self.get('sent')),
                         (NEW, 'W/"b"\n', None))

    def test_304_keeps_the_copy(self):
        self.put('feed.xml', OLD)
        self.put('feed.xml.etag', 'W/"a"\n')
        self.assertEqual(self.run_fetch(304), 0)
        self.assertEqual((self.get('feed.xml'), self.get('feed.xml.etag'), self.get('sent')),
                         (OLD, 'W/"a"\n', 'If-None-Match: W/"a"'))

    def test_changed_feed_replaces_both(self):
        self.put('feed.xml', OLD)
        self.put('feed.xml.etag', 'W/"a"\n')
        self.assertEqual(self.run_fetch(200, NEW, 'W/"b"'), 0)
        self.assertEqual((self.get('feed.xml'), self.get('feed.xml.etag')), (NEW, 'W/"b"\n'))

    def test_no_etag_in_response_drops_the_old_one(self):
        self.put('feed.xml', OLD)
        self.put('feed.xml.etag', 'W/"a"\n')
        self.assertEqual(self.run_fetch(200, NEW), 0)
        self.assertIsNone(self.get('feed.xml.etag'))

    def test_broken_copy_is_not_revalidated(self):
        self.put('feed.xml', '<html>')
        self.put('feed.xml.etag', 'W/"a"\n')
        self.assertEqual(self.run_fetch(200, NEW, 'W/"b"'), 0)
        self.assertIsNone(self.get('sent'))

    def test_unasked_304_fails(self):
        self.assertNotEqual(self.run_fetch(304), 0)

    def test_bad_answers_fail_and_leave_the_copy(self):
        for code, body in ((500, ''), (200, ''), (200, '<html>error</html>')):
            self.put('feed.xml', OLD)
            self.put('feed.xml.etag', 'W/"a"\n')
            self.assertNotEqual(self.run_fetch(code, body, 'W/"b"'), 0, (code, body))
            self.assertEqual((self.get('feed.xml'), self.get('feed.xml.etag')), (OLD, 'W/"a"\n'))


if __name__ == '__main__':
    unittest.main()
