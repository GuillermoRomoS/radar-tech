#!/usr/bin/env python3
"""
Radar Tech — digest diario bilingüe (ES/EN) de robótica, espacio, informática e IA.
Daily bilingual (ES/EN) digest of robotics, space, computing and AI.

Principios / Principles
  * Solo fuentes reales y enlazadas (sources.json). Only real, linked sources.
  * Sin IA generativa: los extractos son literales de cada fuente.
    No generative AI: excerpts are quoted verbatim from each source.
  * Sin dependencias externas: solo biblioteca estándar de Python 3.9+.
    No third-party dependencies: Python 3.9+ standard library only.

Uso / Usage
  python radar.py                       # digest de hoy (UTC)
  python radar.py --date 2026-10-02     # fecha concreta
  python radar.py --fixtures tests/fixtures   # modo offline para tests
"""
from __future__ import annotations

import argparse
import datetime as dt
import email.utils
import hashlib
import html
import json
import os
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCES_FILE = ROOT / "sources.json"
SEEN_FILE = ROOT / "data" / "seen.json"
LATEST_FILE = ROOT / "data" / "latest.json"
DIGESTS_DIR = ROOT / "digests"
README_FILE = ROOT / "README.md"
FEED_FILE = ROOT / "feed.xml"

USER_AGENT = "radar-tech/1.0 (+https://github.com/GuillermoRomoS/radar-tech)"
SEEN_RETENTION_DAYS = 45
EXCERPT_CHARS = 320

CATEGORIES = {
    "robotica": ("🤖 Robótica", "Robotics"),
    "espacio": ("🚀 Espacio", "Space"),
    "informatica": ("💻 Informática", "Computing"),
    "ia": ("🧠 Inteligencia artificial", "Artificial intelligence"),
}
KINDS = {
    "research": "Investigación · Research",
    "news": "Noticia · News",
    "official": "Fuente oficial · Official",
}

NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "dc": "http://purl.org/dc/elements/1.1/",
    "arxiv": "http://arxiv.org/schemas/atom",
}

# --------------------------------------------------------------------------- #
# Utilidades / Helpers
# --------------------------------------------------------------------------- #
TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")
ARXIV_PREFIX_RE = re.compile(r"^arXiv:\S+\s+Announce Type:\s*\S+\s+Abstract:\s*", re.I)


def clean_text(raw: str | None, limit: int = EXCERPT_CHARS) -> str:
    """Quita HTML, normaliza espacios y recorta sin partir palabras."""
    if not raw:
        return ""
    text = html.unescape(TAG_RE.sub(" ", raw))
    text = ARXIV_PREFIX_RE.sub("", WS_RE.sub(" ", text).strip())
    text = text.replace("|", "\\|")  # no romper tablas Markdown
    if len(text) > limit:
        text = text[:limit].rsplit(" ", 1)[0].rstrip(",.;:") + "…"
    return text


def parse_date(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    value = value.strip()
    try:
        d = email.utils.parsedate_to_datetime(value)
    except (TypeError, ValueError, IndexError):
        d = None
    if d is None:
        try:
            d = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            return None
    if d.tzinfo is None:
        d = d.replace(tzinfo=dt.timezone.utc)
    return d.astimezone(dt.timezone.utc)


def item_id(link: str, title: str) -> str:
    return hashlib.sha1((link or title).strip().lower().encode()).hexdigest()[:16]


def md_escape(text: str) -> str:
    return text.replace("[", "\\[").replace("]", "\\]")


# --------------------------------------------------------------------------- #
# Descarga / Fetching
# --------------------------------------------------------------------------- #
def fetch(url: str, fixtures: Path | None, retries: int = 2) -> bytes:
    if fixtures is not None:
        name = re.sub(r"[^a-z0-9]+", "_", url.lower()).strip("_") + ".xml"
        path = fixtures / name
        if not path.exists():
            path = path.with_suffix(".json")
        if not path.exists():
            raise FileNotFoundError(f"fixture no encontrado: {name}")
        return path.read_bytes()
    last_err: Exception | None = None
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=25) as resp:
                return resp.read()
        except Exception as err:  # noqa: BLE001 — registramos y reintentamos
            last_err = err
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"{url}: {last_err}")


# --------------------------------------------------------------------------- #
# Parsers
# --------------------------------------------------------------------------- #
def parse_feed(raw: bytes) -> list[dict]:
    """Soporta RSS 2.0, RSS 1.0 (RDF) y Atom."""
    root = ET.fromstring(raw)
    items: list[dict] = []
    tag = root.tag.lower()

    if tag.endswith("feed"):  # Atom
        for entry in root.findall("atom:entry", NS):
            link_el = entry.find("atom:link[@rel='alternate']", NS)
            if link_el is None:  # ojo: un Element sin hijos es "falsy"
                link_el = entry.find("atom:link", NS)
            items.append({
                "title": (entry.findtext("atom:title", "", NS) or "").strip(),
                "link": link_el.get("href", "") if link_el is not None else "",
                "summary": entry.findtext("atom:summary", "", NS) or entry.findtext("atom:content", "", NS),
                "date": parse_date(entry.findtext("atom:published", None, NS) or entry.findtext("atom:updated", None, NS)),
                "announce": None,
            })
        return items

    # RSS 2.0 (<rss><channel><item>) o RSS 1.0 (<rdf:RDF><item>)
    for it in root.iter():
        if not it.tag.split("}")[-1] == "item":
            continue
        def child(name: str) -> str | None:
            for c in it:
                if c.tag.split("}")[-1] == name:
                    return c.text
            return None
        items.append({
            "title": WS_RE.sub(" ", (child("title") or "")).strip(),
            "link": (child("link") or "").strip(),
            "summary": child("description") or child("encoded"),
            "date": parse_date(child("pubDate") or child("date")),
            "announce": (child("announce_type") or "").strip().lower() or None,
        })
    return items


def parse_hf_daily(raw: bytes) -> list[dict]:
    data = json.loads(raw)
    data.sort(key=lambda e: e.get("paper", {}).get("upvotes", 0), reverse=True)
    items = []
    for entry in data:
        paper = entry.get("paper", {})
        pid = paper.get("id", "")
        items.append({
            "title": WS_RE.sub(" ", paper.get("title", "")).strip(),
            "link": f"https://arxiv.org/abs/{pid}" if pid else "",
            "summary": paper.get("summary", ""),
            "date": parse_date(entry.get("publishedAt") or paper.get("publishedAt")),
            "announce": None,
            "skip_window": True,  # la lista ya es "del día"; publishedAt es la fecha original del paper
            "extra": f"▲ {paper.get('upvotes', 0)} · [HF](https://huggingface.co/papers/{pid})" if pid else "",
        })
    return items


# --------------------------------------------------------------------------- #
# Núcleo / Core
# --------------------------------------------------------------------------- #
def collect(sources: list[dict], now: dt.datetime, window_h: int, seen: dict,
            fixtures: Path | None) -> tuple[list[dict], list[str]]:
    selected: list[dict] = []
    errors: list[str] = []
    cutoff = now - dt.timedelta(hours=window_h)

    for src in sources:
        try:
            raw = fetch(src["url"], fixtures)
            items = parse_hf_daily(raw) if src["type"] == "hf_daily" else parse_feed(raw)
        except Exception as err:  # noqa: BLE001
            errors.append(f"{src['name']}: {str(err)[:120]}")
            continue

        taken = 0
        for it in items:
            if taken >= src.get("limit", 5):
                break
            if not it["title"] or not it["link"]:
                continue
            if it.get("announce") and it["announce"] != "new":
                continue  # arXiv: solo envíos nuevos, no reemplazos ni cross-lists
            if it["date"] and not it.get("skip_window") and not (cutoff <= it["date"] <= now + dt.timedelta(hours=12)):
                continue
            iid = item_id(it["link"], it["title"])
            if iid in seen:
                continue
            seen[iid] = now.date().isoformat()
            selected.append({
                "id": iid,
                "title": it["title"],
                "link": it["link"],
                "excerpt": clean_text(it["summary"]),
                "date": it["date"].isoformat() if it["date"] else None,
                "source": src["name"],
                "category": src["category"],
                "kind": src["kind"],
                "extra": it.get("extra", ""),
            })
            taken += 1
    return selected, errors


def render_digest(day: dt.date, items: list[dict], errors: list[str], n_sources: int) -> str:
    counts = {c: sum(1 for i in items if i["category"] == c) for c in CATEGORIES}
    lines = [
        f"# Radar Tech · {day.isoformat()}",
        "",
        "> **ES** · Selección automática de publicaciones de las últimas horas en robótica, espacio, informática e IA. "
        "Los extractos son **literales de cada fuente** (sin IA generativa); el análisis editorial está en [`/editorial`](../../editorial).",
        ">",
        "> **EN** · Automated selection of the latest publications in robotics, space, computing and AI. "
        "Excerpts are **quoted verbatim from each source** (no generative AI); editorial analysis lives in [`/editorial`](../../editorial).",
        "",
        "| Área · Area | Elementos · Items |",
        "|---|---|",
    ]
    for c, (es, en) in CATEGORIES.items():
        lines.append(f"| {es} · {en} | {counts[c]} |")
    lines.append(f"| **Total** | **{len(items)}** (de/from {n_sources} fuentes/sources) |")
    lines.append("")

    for c, (es, en) in CATEGORIES.items():
        group = [i for i in items if i["category"] == c]
        if not group:
            continue
        lines += [f"## {es} · {en}", ""]
        for i in group:
            date = i["date"][:10] if i["date"] else "s/f"
            meta = f"*{i['source']}* · {KINDS[i['kind']]} · {date}"
            if i["extra"]:
                meta += f" · {i['extra']}"
            lines.append(f"### [{md_escape(i['title'])}]({i['link']})")
            lines.append(meta)
            if i["excerpt"]:
                lines += ["", f"> {i['excerpt']}"]
            lines.append("")

    lines += [
        "---",
        "**Método · Method** — "
        f"generado por [`radar.py`](../../radar.py) el {dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC. "
        "Fuentes en [`sources.json`](../../sources.json). Los títulos y extractos pertenecen a sus autores; "
        "aquí solo se citan y enlazan. · Titles and excerpts belong to their authors; quoted and linked only.",
    ]
    if errors:
        lines += ["", "<details><summary>Fuentes no disponibles hoy · Unavailable sources</summary>", ""]
        lines += [f"- {e}" for e in errors]
        lines += ["", "</details>"]
    return "\n".join(lines) + "\n"


def update_readme(day: dt.date, items: list[dict], digest_rel: str) -> None:
    if not README_FILE.exists():
        return
    text = README_FILE.read_text(encoding="utf-8")
    start, end = "<!-- RADAR:START -->", "<!-- RADAR:END -->"
    if start not in text or end not in text:
        return
    block = [start, "", f"**Última edición · Latest issue: [{day.isoformat()}]({digest_rel})** — {len(items)} elementos/items", ""]
    for c, (es, en) in CATEGORIES.items():
        top = [i for i in items if i["category"] == c][:3]
        if not top:
            continue
        block.append(f"**{es} · {en}**")
        block += [f"- [{md_escape(i['title'])}]({i['link']}) — *{i['source']}*" for i in top]
        block.append("")
    recent = sorted(DIGESTS_DIR.glob("*/*.md"), reverse=True)[:10]
    if recent:
        block.append("**Archivo reciente · Recent archive:** " +
                     " · ".join(f"[{p.stem}](digests/{p.parent.name}/{p.name})" for p in recent))
        block.append("")
    block.append(end)
    pre, rest = text.split(start, 1)
    post = rest.split(end, 1)[1]
    README_FILE.write_text(pre + "\n".join(block) + post, encoding="utf-8")


def write_feed(repo: str) -> None:
    """RSS de las ediciones, para que cualquiera pueda suscribirse."""
    base = f"https://github.com/{repo}/blob/main"
    entries = []
    for p in sorted(DIGESTS_DIR.glob("*/*.md"), reverse=True)[:30]:
        day = p.stem
        pub = email.utils.format_datetime(dt.datetime.fromisoformat(day).replace(hour=7, tzinfo=dt.timezone.utc))
        url = f"{base}/digests/{p.parent.name}/{p.name}"
        entries.append(
            f"<item><title>Radar Tech {day}</title><link>{url}</link><guid>{url}</guid>"
            f"<pubDate>{pub}</pubDate></item>")
    for p in sorted((ROOT / "editorial").glob("*.md"), reverse=True)[:30]:
        if p.name.lower() == "readme.md":
            continue
        title = p.read_text(encoding="utf-8").splitlines()[0].lstrip("# ").strip()
        day = p.name[:10]
        try:
            pub = email.utils.format_datetime(dt.datetime.fromisoformat(day).replace(hour=8, tzinfo=dt.timezone.utc))
        except ValueError:
            continue
        url = f"{base}/editorial/{p.name}"
        entries.append(f"<item><title>{html.escape(title)}</title><link>{url}</link><guid>{url}</guid>"
                       f"<pubDate>{pub}</pubDate></item>")
    FEED_FILE.write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel>'
        f"<title>Radar Tech · Robótica, Espacio, Informática e IA</title>"
        f"<link>https://github.com/{repo}</link>"
        "<description>Digest diario bilingüe ES/EN con fuentes verificables.</description>"
        + "".join(entries) + "</channel></rss>\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--date", help="YYYY-MM-DD (UTC). Por defecto, hoy.")
    ap.add_argument("--window-hours", type=int, default=48)
    ap.add_argument("--fixtures", type=Path, help="Carpeta con feeds de prueba (modo offline).")
    ap.add_argument("--dry-run", action="store_true", help="Imprime el digest sin escribir archivos.")
    args = ap.parse_args(argv)

    now = dt.datetime.now(dt.timezone.utc)
    if args.date:
        day = dt.date.fromisoformat(args.date)
        now = dt.datetime.combine(day, dt.time(23, 59), tzinfo=dt.timezone.utc)
    day = now.date()

    sources = json.loads(SOURCES_FILE.read_text(encoding="utf-8"))["sources"]
    seen: dict = json.loads(SEEN_FILE.read_text(encoding="utf-8")) if SEEN_FILE.exists() else {}
    if args.dry_run:
        seen = {}

    items, errors = collect(sources, now, args.window_hours, seen, args.fixtures)
    print(f"[radar] {len(items)} elementos nuevos · {len(errors)} fuentes con error", file=sys.stderr)
    for e in errors:
        print(f"[radar]   ! {e}", file=sys.stderr)

    if not items:
        print("[radar] Nada nuevo; no se genera edición.", file=sys.stderr)
        return 0 if len(errors) < len(sources) else 1

    # Si ya hubo una ejecución hoy, se fusiona en vez de sobrescribir la edición del día
    if not args.dry_run and LATEST_FILE.exists():
        prev = json.loads(LATEST_FILE.read_text(encoding="utf-8"))
        if prev.get("date") == day.isoformat():
            items = prev.get("items", []) + items

    digest = render_digest(day, items, errors, len(sources))
    if args.dry_run:
        print(digest)
        return 0

    out = DIGESTS_DIR / f"{day:%Y}" / f"{day.isoformat()}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(digest, encoding="utf-8")

    cutoff = (day - dt.timedelta(days=SEEN_RETENTION_DAYS)).isoformat()
    seen = {k: v for k, v in seen.items() if v >= cutoff}
    SEEN_FILE.parent.mkdir(parents=True, exist_ok=True)
    SEEN_FILE.write_text(json.dumps(seen, indent=0, sort_keys=True), encoding="utf-8")
    LATEST_FILE.write_text(json.dumps({"date": day.isoformat(), "items": items, "errors": errors},
                                      ensure_ascii=False, indent=2), encoding="utf-8")

    update_readme(day, items, f"digests/{day:%Y}/{day.isoformat()}.md")
    write_feed(os.environ.get("GITHUB_REPOSITORY", "GuillermoRomoS/radar-tech"))
    print(f"[radar] Escrito {out.relative_to(ROOT)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
