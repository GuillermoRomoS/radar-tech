"""Tests offline de radar.py (datos de prueba ficticios, no se publican).
Ejecutar: python -m unittest discover -s tests -v
"""
import datetime as dt
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import radar  # noqa: E402

NOW = dt.datetime(2026, 10, 2, 12, 0, tzinfo=dt.timezone.utc)

RSS2 = b"""<?xml version="1.0"?>
<rss version="2.0" xmlns:arxiv="http://arxiv.org/schemas/atom" xmlns:dc="http://purl.org/dc/elements/1.1/">
<channel><title>t</title>
<item><title>TEST paper new</title><link>https://arxiv.org/abs/0000.00001</link>
<description>arXiv:0000.00001v1 Announce Type: new Abstract: A &lt;b&gt;bold&lt;/b&gt; test abstract.</description>
<pubDate>Thu, 01 Oct 2026 04:00:00 -0400</pubDate><arxiv:announce_type>new</arxiv:announce_type></item>
<item><title>TEST paper replaced</title><link>https://arxiv.org/abs/0000.00002</link>
<description>arXiv:0000.00002v2 Announce Type: replace Abstract: old</description>
<pubDate>Thu, 01 Oct 2026 04:00:00 -0400</pubDate><arxiv:announce_type>replace</arxiv:announce_type></item>
<item><title>TEST old news</title><link>https://example.org/old</link><description>old</description>
<pubDate>Wed, 21 Jan 2026 13:54:00 +0100</pubDate></item>
</channel></rss>"""

ATOM = b"""<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"><title>t</title>
<entry><title>TEST atom entry</title><link href="https://example.org/a"/>
<summary>Atom summary</summary><updated>2026-10-02T08:00:00Z</updated></entry>
</feed>"""

HF = json.dumps([
    {"publishedAt": "2026-10-01T10:00:00.000Z", "paper": {"id": "0000.10001", "title": "TEST low", "summary": "s", "upvotes": 3}},
    {"publishedAt": "2026-10-01T10:00:00.000Z", "paper": {"id": "0000.10002", "title": "TEST high", "summary": "s", "upvotes": 90}},
]).encode()


class TestParsers(unittest.TestCase):
    def test_clean_text_strips_html_and_arxiv_prefix(self):
        self.assertEqual(radar.clean_text("arXiv:1v1 Announce Type: new Abstract: <b>Hola</b>  mundo"), "Hola mundo")

    def test_clean_text_truncates_on_word(self):
        out = radar.clean_text("palabra " * 100, limit=30)
        self.assertTrue(out.endswith("…"))
        self.assertLessEqual(len(out), 31)

    def test_rss2(self):
        items = radar.parse_feed(RSS2)
        self.assertEqual(len(items), 3)
        self.assertEqual(items[0]["announce"], "new")
        self.assertEqual(items[0]["date"], dt.datetime(2026, 10, 1, 8, 0, tzinfo=dt.timezone.utc))

    def test_atom_link(self):
        items = radar.parse_feed(ATOM)
        self.assertEqual(items[0]["link"], "https://example.org/a")

    def test_hf_sorted_by_upvotes(self):
        items = radar.parse_hf_daily(HF)
        self.assertEqual(items[0]["title"], "TEST high")
        self.assertEqual(items[0]["link"], "https://arxiv.org/abs/0000.10002")


class TestCollect(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        def fx(url, data, ext):
            name = re.sub(r"[^a-z0-9]+", "_", url.lower()).strip("_") + ext
            (self.tmp / name).write_bytes(data)
        self.sources = [
            {"name": "A", "url": "https://x.test/rss", "type": "rss", "category": "robotica", "kind": "research", "limit": 5},
            {"name": "B", "url": "https://x.test/atom", "type": "atom", "category": "espacio", "kind": "news", "limit": 5},
            {"name": "C", "url": "https://x.test/hf", "type": "hf_daily", "category": "ia", "kind": "research", "limit": 1},
            {"name": "D", "url": "https://x.test/missing", "type": "rss", "category": "informatica", "kind": "news", "limit": 5},
        ]
        fx("https://x.test/rss", RSS2, ".xml")
        fx("https://x.test/atom", ATOM, ".xml")
        fx("https://x.test/hf", HF, ".json")

    def test_filters_dedup_and_errors(self):
        seen = {}
        items, errors = radar.collect(self.sources, NOW, 48, seen, self.tmp)
        titles = [i["title"] for i in items]
        self.assertEqual(titles, ["TEST paper new", "TEST atom entry", "TEST high"])  # sin replace, sin antiguo, limit=1
        self.assertEqual(len(errors), 1)  # fuente D sin fixture
        again, _ = radar.collect(self.sources, NOW, 48, seen, self.tmp)
        self.assertEqual([i["title"] for i in again], ["TEST low"])  # lo ya visto se salta; entra el siguiente
        third, _ = radar.collect(self.sources, NOW, 48, seen, self.tmp)
        self.assertEqual(third, [])  # deduplicado

    def test_render_is_bilingual_and_links(self):
        items, errors = radar.collect(self.sources, NOW, 48, {}, self.tmp)
        md = radar.render_digest(NOW.date(), items, errors, len(self.sources))
        for needle in ("**ES**", "**EN**", "Robótica · Robotics", "(https://arxiv.org/abs/0000.00001)", "Unavailable sources"):
            self.assertIn(needle, md)


if __name__ == "__main__":
    unittest.main()
