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

**Última edición · Latest issue: [2026-10-17](digests/2026/2026-10-17.md)** — 16 elementos/items

**🤖 Robótica · Robotics**
- [Video Friday: When Two Robots Become One](https://spectrum.ieee.org/video-friday-reconfigurable-robots) — *IEEE Spectrum · Robotics*
- [Why opportunity charging is winning as robot fleets scale](https://www.therobotreport.com/why-opportunity-charging-is-winning-as-robot-fleets-scale/) — *The Robot Report*
- [MassRobotics opens applications for Healthcare Robotics Startup Catalyst Program](https://www.therobotreport.com/massrobotics-opens-applications-healthcare-robotics-startup-catalyst-program/) — *The Robot Report*

**🚀 Espacio · Space**
- [APOD: 2026 October 17 – 3D 67P](https://science.nasa.gov/image-article/apod-2026-october-17-3d-67p/) — *NASA · News Releases*
- [NASA Names Stephen Cash Marshall Space Flight Center Director](https://www.nasa.gov/news-release/nasa-names-stephen-cash-marshall-space-flight-center-director/) — *NASA · News Releases*
- [Artemis II Heat Shield After Splashdown](https://www.nasa.gov/image-article/artemis-ii-heat-shield-after-splashdown/) — *NASA · News Releases*

**💻 Informática · Computing**
- [He Wants AI Benchmarking To Be a Science, Not a Dark Art](https://www.quantamagazine.org/he-wants-ai-benchmarking-to-be-a-science-not-a-dark-art-20261016/) — *Quanta Magazine · Computer Science*

**🧠 Inteligencia artificial · Artificial intelligence**
- [FDE-Gym: The Last Mile of AI Delivery](https://arxiv.org/abs/2610.22350) — *Hugging Face Daily Papers*
- [Behavioral Compositionality of Sparse Autoencoder Representations](https://arxiv.org/abs/2610.21261) — *Hugging Face Daily Papers*
- [MAI-Gym: An Open All-in-One Platform for GUI Agent Evaluation and RL Training across Mobile and Computer Environments](https://arxiv.org/abs/2610.20939) — *Hugging Face Daily Papers*

**Archivo reciente · Recent archive:** [2026-10-17](digests/2026/2026-10-17.md) · [2026-10-16](digests/2026/2026-10-16.md) · [2026-10-15](digests/2026/2026-10-15.md) · [2026-10-14](digests/2026/2026-10-14.md) · [2026-10-13](digests/2026/2026-10-13.md) · [2026-10-12](digests/2026/2026-10-12.md) · [2026-10-11](digests/2026/2026-10-11.md) · [2026-10-10](digests/2026/2026-10-10.md) · [2026-10-09](digests/2026/2026-10-09.md) · [2026-10-08](digests/2026/2026-10-08.md)

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
