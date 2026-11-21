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

**Última edición · Latest issue: [2026-11-21](digests/2026/2026-11-21.md)** — 15 elementos/items

**🤖 Robótica · Robotics**
- [Video Friday: Drone Squeezes Itself to Fit Through Tight Spaces](https://spectrum.ieee.org/video-friday-morphing-robots-quadrotor) — *IEEE Spectrum · Robotics*
- [Medtronic’s Hugo surgical robot ready for bigger operation](https://www.therobotreport.com/medtronics-hugo-surgical-robot-ready-for-bigger-operation/) — *The Robot Report*
- [MassRobotics launching marine robotics facility on Boston Harbor](https://www.therobotreport.com/massrobotics-launching-marine-robotics-facility-on-boston-harbor/) — *The Robot Report*

**🚀 Espacio · Space**
- [APOD: 2026 November 21 – Voyager’s Neptune](https://science.nasa.gov/image-article/apod-2026-november-21-voyagers-neptune/) — *NASA · News Releases*
- [Curiosity Spots Drifting Twilight Clouds](https://science.nasa.gov/photojournal/curiosity-spots-drifting-twilight-clouds/) — *NASA · News Releases*
- [New NASA Seed Funding Primes Small Businesses for Innovation](https://www.nasa.gov/directorates/rtmd/new-nasa-seed-funding-primes-small-businesses-for-innovation/) — *NASA · News Releases*

**💻 Informática · Computing**
- [Network Researchers Nail Down Theory of ‘Perfect Resilience’](https://www.quantamagazine.org/network-researchers-nail-down-theory-of-perfect-resilience-20261120/) — *Quanta Magazine · Computer Science*

**🧠 Inteligencia artificial · Artificial intelligence**
- [Posterior Matching Distillation](https://arxiv.org/abs/2611.26629) — *Hugging Face Daily Papers*
- [Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth](https://arxiv.org/abs/2611.26603) — *Hugging Face Daily Papers*
- [HiUni: Harmonizing Understanding and Generation in Shared Visual Space](https://arxiv.org/abs/2611.26107) — *Hugging Face Daily Papers*

**Archivo reciente · Recent archive:** [2026-11-21](digests/2026/2026-11-21.md) · [2026-11-20](digests/2026/2026-11-20.md) · [2026-11-19](digests/2026/2026-11-19.md) · [2026-11-18](digests/2026/2026-11-18.md) · [2026-11-17](digests/2026/2026-11-17.md) · [2026-11-16](digests/2026/2026-11-16.md) · [2026-11-15](digests/2026/2026-11-15.md) · [2026-11-14](digests/2026/2026-11-14.md) · [2026-11-13](digests/2026/2026-11-13.md) · [2026-11-12](digests/2026/2026-11-12.md)

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
