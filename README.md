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

**Última edición · Latest issue: [2026-11-11](digests/2026/2026-11-11.md)** — 24 elementos/items

**🤖 Robótica · Robotics**
- [Maze Runner: Autonomous Maze Navigation with Line-Based Localization and Control Barrier Functions](https://arxiv.org/abs/2611.12949) — *arXiv cs.RO (Robotics)*
- [CAFE: Closed-Loop Autonomous Task Formulation and Execution without Instance-Specific Instructions](https://arxiv.org/abs/2611.12983) — *arXiv cs.RO (Robotics)*
- [RoboACE: Adversarial Co-Evolution for Robot Self-Improvement](https://arxiv.org/abs/2611.13034) — *arXiv cs.RO (Robotics)*

**🚀 Espacio · Space**
- [APOD: 2026 November 11 – NGC 4449: Small Galaxy, Big Impact](https://science.nasa.gov/image-article/apod-2026-november-11-ngc-4449-small-galaxy-big-impact/) — *NASA · News Releases*
- [Water Surges Into Navajo Reservoir](https://science.nasa.gov/earth/earth-observatory/water-surges-into-navajo-reservoir/) — *NASA · News Releases*
- [NASA Invites Media, Public to Join Voyager 1 One-Light Day Activities](https://www.nasa.gov/news-release/nasa-invites-media-public-to-join-voyager-1-one-light-day-activities/) — *NASA · News Releases*

**🧠 Inteligencia artificial · Artificial intelligence**
- [World In-Context Learning for Agentic Robot Manipulation](https://arxiv.org/abs/2611.12885) — *Hugging Face Daily Papers*
- [Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents](https://arxiv.org/abs/2611.14320) — *Hugging Face Daily Papers*
- [Tree-Ising: Repairing Language Models with Bit-Level Ising Edits](https://arxiv.org/abs/2611.14210) — *Hugging Face Daily Papers*

**Archivo reciente · Recent archive:** [2026-11-11](digests/2026/2026-11-11.md) · [2026-11-10](digests/2026/2026-11-10.md) · [2026-11-09](digests/2026/2026-11-09.md) · [2026-11-08](digests/2026/2026-11-08.md) · [2026-11-07](digests/2026/2026-11-07.md) · [2026-11-06](digests/2026/2026-11-06.md) · [2026-11-05](digests/2026/2026-11-05.md) · [2026-11-04](digests/2026/2026-11-04.md) · [2026-11-03](digests/2026/2026-11-03.md) · [2026-11-02](digests/2026/2026-11-02.md)

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
