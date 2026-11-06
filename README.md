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

**Última edición · Latest issue: [2026-11-06](digests/2026/2026-11-06.md)** — 31 elementos/items

**🤖 Robótica · Robotics**
- [Curvature by Design: A Support Structure for Continuum Robots](https://arxiv.org/abs/2611.07091) — *arXiv cs.RO (Robotics)*
- [Spatial-UMI-Dream: Scaling World Action Models with Metric Geometry for UMI Manipulation](https://arxiv.org/abs/2611.07229) — *arXiv cs.RO (Robotics)*
- [Adaptive Hybrid Force-Vision Control with EMG-Derived References for Deformable Bottle Manipulation](https://arxiv.org/abs/2611.07235) — *arXiv cs.RO (Robotics)*

**🚀 Espacio · Space**
- [APOD: 2026 November 6 – A Farewell to Swift](https://science.nasa.gov/image-article/apod-2026-november-6-a-farewell-to-swift/) — *NASA · News Releases*
- [Taking a Gander at Utah’s Goosenecks](https://science.nasa.gov/earth/earth-observatory/taking-a-gander-at-utahs-goosenecks/) — *NASA · News Releases*
- [Midwestern City Lights](https://www.nasa.gov/image-article/midwestern-city-lights/) — *NASA · News Releases*

**🧠 Inteligencia artificial · Artificial intelligence**
- [Decoupled Predictive Decision Making: A Shared Conditional Predictor for Agents](https://arxiv.org/abs/2611.02075) — *Hugging Face Daily Papers*
- [VFlash: Fast, Accurate Visual Planning via Flash Primitive Decoding](https://arxiv.org/abs/2611.08449) — *Hugging Face Daily Papers*
- [Harness-S: Learning from Sibling Harnesses for Generalizable Agent Training](https://arxiv.org/abs/2611.04277) — *Hugging Face Daily Papers*

**Archivo reciente · Recent archive:** [2026-11-06](digests/2026/2026-11-06.md) · [2026-11-05](digests/2026/2026-11-05.md) · [2026-11-04](digests/2026/2026-11-04.md) · [2026-11-03](digests/2026/2026-11-03.md) · [2026-11-02](digests/2026/2026-11-02.md) · [2026-11-01](digests/2026/2026-11-01.md) · [2026-10-31](digests/2026/2026-10-31.md) · [2026-10-30](digests/2026/2026-10-30.md) · [2026-10-29](digests/2026/2026-10-29.md) · [2026-10-28](digests/2026/2026-10-28.md)

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
