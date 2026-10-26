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

**Última edición · Latest issue: [2026-10-26](digests/2026/2026-10-26.md)** — 20 elementos/items

**🤖 Robótica · Robotics**
- [See What I Need, Dream What I Want: A Navigation Foundation Model on a Self-Constructed Representation Space](https://arxiv.org/abs/2610.31762) — *arXiv cs.RO (Robotics)*
- [FLORA: An Open Model Suite for Scaling Robotics Data Engines](https://arxiv.org/abs/2610.31779) — *arXiv cs.RO (Robotics)*
- [KiRoSe: Using Kinematic Data for Efficient Segmentation of Robot Demonstrations](https://arxiv.org/abs/2610.31801) — *arXiv cs.RO (Robotics)*

**🚀 Espacio · Space**
- [2026 October 26 – M42: The Great Nebula in Orion](https://science.nasa.gov/image-article/2026-october-26-m42-the-great-nebula-in-orion/) — *NASA · News Releases*
- [Hunting Red Leaves with Satellites](https://science.nasa.gov/earth/earth-observatory/hunting-red-leaves-with-satellites/) — *NASA · News Releases*
- [A Study of the 30 May 2026 Meteor Event Employing Data from Raspberry Boom Infrasound Sensors in the Boston Area](https://arxiv.org/abs/2610.31742) — *arXiv astro-ph.IM (Instrumentation)*

**💻 Informática · Computing**
- [Poetry for Engineers: Of Code and Shortleaf Pine](https://spectrum.ieee.org/poetry-for-engineers-of-code-and-shortleaf-pine) — *IEEE Spectrum · Computing*

**🧠 Inteligencia artificial · Artificial intelligence**
- [Reading, Writing, Sharing, and Interacting with the World through Video](https://arxiv.org/abs/2610.31668) — *Hugging Face Daily Papers*
- [UserArena: Benchmarking Interactive User Simulation for Long-Horizon Shopping Agents](https://arxiv.org/abs/2610.30932) — *Hugging Face Daily Papers*
- [HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games](https://arxiv.org/abs/2610.31162) — *Hugging Face Daily Papers*

**Archivo reciente · Recent archive:** [2026-10-26](digests/2026/2026-10-26.md) · [2026-10-25](digests/2026/2026-10-25.md) · [2026-10-24](digests/2026/2026-10-24.md) · [2026-10-23](digests/2026/2026-10-23.md) · [2026-10-22](digests/2026/2026-10-22.md) · [2026-10-21](digests/2026/2026-10-21.md) · [2026-10-20](digests/2026/2026-10-20.md) · [2026-10-19](digests/2026/2026-10-19.md) · [2026-10-18](digests/2026/2026-10-18.md) · [2026-10-17](digests/2026/2026-10-17.md)

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
