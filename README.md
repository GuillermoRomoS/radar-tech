# 📡 Radar Tech: robótica, espacio, informática e IA

**ES** · Un radar diario y **verificable** de lo que se publica en robótica, espacio, informática e inteligencia artificial: artículos de investigación (arXiv, Hugging Face Papers), fuentes oficiales (NASA, ESA, Google DeepMind) y medios especializados (IEEE Spectrum, The Robot Report, Quanta). Además, una **edición editorial** con análisis crítico.

**EN** · A daily, **verifiable** radar of new work in robotics, space, computing and AI: research papers, official sources and specialised media, plus an **editorial issue** with critical analysis.

[![Radar diario](https://github.com/GuillermoRomoS/radar-tech/actions/workflows/radar.yml/badge.svg)](https://github.com/GuillermoRomoS/radar-tech/actions/workflows/radar.yml)
· 🌐 **[Web con buscador · Searchable site](https://guillermoromos.github.io/radar-tech/)** · 📰 [Ediciones editoriales · Editorials](editorial/) · 🗂️ [Archivo diario · Daily archive](digests/) · 🔔 [RSS](feed.xml)

## Principios · Principles

| | ES | EN |
|---|---|---|
| 🔗 | Cada elemento enlaza a su fuente original. | Every item links to its original source. |
| 🧾 | Los extractos del digest son **literales**: no se generan con IA. | Digest excerpts are **verbatim**, not AI-generated. |
| 🔍 | Las ediciones editoriales separan **hechos** de **análisis** y señalan las discrepancias entre fuentes. | Editorials separate **facts** from **analysis** and flag source discrepancies. |
| 🟢🟡 | Se distingue entre fuente primaria y medio especializado. | Primary vs. secondary sources are labelled. |
| 🛠️ | Solo Python estándar y GitHub Actions: coste 0 €. | Standard-library Python + GitHub Actions: zero cost. |

## Hoy en el radar · Today on the radar

<!-- RADAR:START -->

**Última edición · Latest issue: [2026-10-19](digests/2026/2026-10-19.md)** — 20 elementos/items

**🤖 Robótica · Robotics**
- [DriveWorld3D Evidence Constrained 3D World Modeling and Generative Simulation for Real-World Autonomous Driving](https://arxiv.org/abs/2610.22450) — *arXiv cs.RO (Robotics)*
- [Mothership: A Two Tier Autonomous Refuse Collection System for Pedestrian Campuses](https://arxiv.org/abs/2610.22461) — *arXiv cs.RO (Robotics)*
- [Has GPT-6-Astra Achieved Embodied Intelligence?](https://arxiv.org/abs/2610.22471) — *arXiv cs.RO (Robotics)*

**🚀 Espacio · Space**
- [APOD: 2026 October 19 – Treble Clef: Unusual X-ray Hot Radio Source](https://science.nasa.gov/image-article/apod-2026-october-19-treble-clef-unusual-x-ray-hot-radio-source/) — *NASA · News Releases*
- [Autumn Paints Poland’s Bieszczady Mountains](https://science.nasa.gov/earth/earth-observatory/autumn-paints-polands-bieszczady-mountains/) — *NASA · News Releases*
- [Hera Mission Prepares for Follow-Up Asteroid Imaging](https://spectrum.ieee.org/esa-hera-dimorphos-rendezvous) — *IEEE Spectrum · Aerospace*

**🧠 Inteligencia artificial · Artificial intelligence**
- [BizBench: Unveiling Hidden Challenges in Deploying Long-Horizon Agents for Real-World Business](https://arxiv.org/abs/2610.20424) — *Hugging Face Daily Papers*
- [Learning to Think and Explore in 3D World](https://arxiv.org/abs/2610.21783) — *Hugging Face Daily Papers*
- [Into the Unknown: Benchmarking AI agents on open scientific research problems](https://arxiv.org/abs/2610.19159) — *Hugging Face Daily Papers*

**Archivo reciente · Recent archive:** [2026-10-19](digests/2026/2026-10-19.md) · [2026-10-18](digests/2026/2026-10-18.md) · [2026-10-17](digests/2026/2026-10-17.md) · [2026-10-16](digests/2026/2026-10-16.md) · [2026-10-15](digests/2026/2026-10-15.md) · [2026-10-14](digests/2026/2026-10-14.md) · [2026-10-13](digests/2026/2026-10-13.md) · [2026-10-12](digests/2026/2026-10-12.md) · [2026-10-11](digests/2026/2026-10-11.md) · [2026-10-10](digests/2026/2026-10-10.md)

<!-- RADAR:END -->

## Cómo funciona · How it works

```
sources.json ──► radar.py ──► digests/AAAA/AAAA-MM-DD.md
 (12 feeds)      │  ├─ RSS 2.0 / Atom / API Hugging Face
                 │  ├─ ventana de 48 h + deduplicación (data/seen.json)
                 │  ├─ arXiv: solo envíos nuevos (announce_type = new)
                 │  └─ README.md (este bloque) + feed.xml + data/latest.json
digests/ + editorial/ ──► build_site.py ──► site/index.html (GitHub Pages, buscador)
GitHub Actions (cron diario 05:17 UTC) ──► commit automático + despliegue de la web
```

```bash
python radar.py --dry-run          # previsualizar sin escribir · preview only
python radar.py                    # generar la edición de hoy · build today's issue
python build_site.py               # web estática en site/ · static site in site/
python -m unittest discover -s tests   # tests
```

Para añadir una fuente basta con editar [`sources.json`](sources.json): nombre, URL, tipo (`rss`/`atom`/`hf_daily`), categoría (`robotica`/`espacio`/`informatica`/`ia`), naturaleza (`research`/`news`/`official`) y límite diario.

## Fuentes · Sources

| Área | Fuentes |
|---|---|
| 🤖 Robótica | arXiv cs.RO · IEEE Spectrum Robotics · The Robot Report |
| 🚀 Espacio | NASA · ESA · IEEE Spectrum Aerospace · arXiv astro-ph.IM |
| 💻 Informática | IEEE Spectrum Computing · Quanta Magazine CS |
| 🧠 IA | Hugging Face Daily Papers · Google DeepMind · IEEE Spectrum AI |

## Licencia · License

Código bajo MIT ([LICENSE](LICENSE)). Los textos editoriales propios se publican bajo CC BY 4.0. Los títulos y extractos citados pertenecen a sus autores y fuentes, y aquí solo se citan y enlazan.

Autor · Author: **Guillermo Romo Sánchez**, estudiante de Robótica e IA (UCJC). ¿Has visto un error? [Abre un issue](../../issues).
