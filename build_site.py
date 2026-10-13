#!/usr/bin/env python3
"""
Radar Tech — genera la web pública (GitHub Pages) a partir de los digests y las ediciones.
Builds the public website (GitHub Pages) from the daily digests and editorial issues.

  * La fuente de verdad son los Markdown de digests/ y editorial/; la web no guarda estado propio.
    Source of truth is the Markdown in digests/ and editorial/; the site keeps no state of its own.
  * Una sola página estática con los datos embebidos y buscador en el navegador. Solo biblioteca estándar.
    One static page with embedded data and in-browser search. Standard library only.

Uso / Usage
  python build_site.py                 # escribe site/index.html
  python build_site.py --out otra/     # otra carpeta de salida
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import radar

ROOT = Path(__file__).resolve().parent
TEMPLATE_FILE = ROOT / "site_template.html"
REPO = "GuillermoRomoS/radar-tech"

TITLE_RE = re.compile(r"^### \[(?P<title>.+)\]\((?P<link>\S+)\)\s*$")
SECTION_RE = re.compile(r"^## (?P<label>.+?) · ")
META_RE = re.compile(r"^\*(?P<source>.+?)\* · (?P<kind>" + "|".join(map(re.escape, radar.KINDS.values()))
                     + r") · (?P<date>\S+)(?: · (?P<extra>.*))?$")
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

LABEL_TO_CAT = {es: key for key, (es, _en) in radar.CATEGORIES.items()}
KIND_TO_KEY = {label: key for key, label in radar.KINDS.items()}


def parse_digest(text: str, day: str) -> list[dict]:
    """Recupera los elementos de un digest Markdown generado por radar.render_digest."""
    items: list[dict] = []
    category = None
    current: dict | None = None
    for line in text.splitlines():
        if m := SECTION_RE.match(line):
            category = LABEL_TO_CAT.get(m["label"])
            current = None
            continue
        if m := TITLE_RE.match(line):
            current = {
                "day": day,
                "title": m["title"].replace("\\[", "[").replace("\\]", "]"),
                "link": m["link"],
                "category": category,
                "source": "", "kind": "", "excerpt": "", "votes": None,
            }
            items.append(current)
            continue
        if current is None:
            continue
        if not current["source"] and (m := META_RE.match(line)):
            current["source"] = m["source"]
            current["kind"] = KIND_TO_KEY.get(m["kind"], "")
            if m["extra"] and (v := re.search(r"▲ (\d+)", m["extra"])):
                current["votes"] = int(v.group(1))
        elif line.startswith("> ") and not current["excerpt"]:
            current["excerpt"] = line[2:].replace("\\|", "|")
        elif line.startswith("---"):
            current = None
    return [i for i in items if i["category"]]


def load_items(digests_dir: Path, excluded: list[str]) -> list[dict]:
    items: list[dict] = []
    for path in sorted(digests_dir.glob("*/*.md"), reverse=True):
        for it in parse_digest(path.read_text(encoding="utf-8"), path.stem):
            if not radar.is_excluded(it["link"], excluded):
                items.append(it)
    return items


def load_editorials(editorial_dir: Path) -> list[dict]:
    out = []
    for path in sorted(editorial_dir.glob("*.md"), reverse=True):
        if path.name.lower() in {"readme.md", "plantilla.md"} or not re.match(r"\d{4}-\d{2}-\d{2}-", path.name):
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        title = lines[0].lstrip("# ").strip() if lines else path.stem
        issue = next((MD_LINK_RE.sub(r"\1", l).strip("*") for l in lines[1:6] if l.startswith("**Edición")), "")
        out.append({
            "day": path.name[:10],
            "title": title,
            "issue": issue.split("·")[0].strip(" *"),
            "link": f"https://github.com/{REPO}/blob/main/editorial/{path.name}",
        })
    return out


def build(out_dir: Path, fragment: bool = False) -> Path:
    cfg = json.loads(radar.SOURCES_FILE.read_text(encoding="utf-8"))
    items = load_items(radar.DIGESTS_DIR, cfg.get("exclude_link_domains", []))
    data = {
        "items": items,
        "editorials": load_editorials(ROOT / "editorial"),
        "categories": {k: {"es": es.split(" ", 1)[1], "en": en, "icon": es.split(" ", 1)[0]}
                       for k, (es, en) in radar.CATEGORIES.items()},
        "kinds": {k: v for k, v in radar.KINDS.items()},
        "sources": len(cfg["sources"]),
        "repo": REPO,
    }
    # "</" dentro de un <script> cerraría la etiqueta: se escapa
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = TEMPLATE_FILE.read_text(encoding="utf-8").replace("/*__DATA__*/null", payload)
    if fragment:  # para previsualizar dentro de otro documento
        page = "\n".join(l for l in page.splitlines() if not l.rstrip().endswith("<!--doc-->"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "index.html"
    out.write_text(page, encoding="utf-8")
    (out_dir / ".nojekyll").write_text("", encoding="utf-8")
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, default=ROOT / "site")
    ap.add_argument("--fragment", action="store_true", help=argparse.SUPPRESS)
    args = ap.parse_args(argv)
    out = build(args.out, args.fragment)
    print(f"[site] Escrito {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
