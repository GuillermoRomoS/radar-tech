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

**Última edición · Latest issue: [2026-11-12](digests/2026/2026-11-12.md)** — 18 elementos/items

**🤖 Robótica · Robotics**
- [Viam Launchpad aims to accelerate robotics deployments](https://www.therobotreport.com/viam-launchpad-aims-to-accelerate-robotics-deployments/) — *The Robot Report*
- [Runway’s Praxis-1 world action model for robotics is now available](https://www.therobotreport.com/runways-praxis-1-world-action-model-for-robotics-is-now-available/) — *The Robot Report*
- [Serve Robotics opens robot delivery network for others to build on](https://www.therobotreport.com/serve-robotics-opens-robot-delivery-network-for-others-to-build-on/) — *The Robot Report*

**🚀 Espacio · Space**
- [NASA’s Hubble Offers Cosmic Sampler of Targets for Roman](https://science.nasa.gov/missions/hubble/nasas-hubble-offers-cosmic-sampler-of-targets-for-roman/) — *NASA · News Releases*
- [Through NASA’s Lens: Capturing Space Shuttle Endeavour’s Move to LA](https://www.nasa.gov/centers-and-facilities/armstrong/through-nasas-lens-capturing-space-shuttle-endeavours-move-to-la/) — *NASA · News Releases*
- [APOD: 2026 November 12 – Moon, Venus and Spica Meet](https://science.nasa.gov/image-article/apod-2026-november-12-moon-venus-and-spica-meet/) — *NASA · News Releases*

**💻 Informática · Computing**
- [NSF’s X-Labs Program Draws Support From Charities and Investors](https://spectrum.ieee.org/national-science-foundation-x-labs) — *IEEE Spectrum · Computing*

**🧠 Inteligencia artificial · Artificial intelligence**
- [One Table, Many Queries: Benchmarking Generalist Tabular Models Across Generation, Imputation, and Prediction](https://arxiv.org/abs/2611.13001) — *Hugging Face Daily Papers*
- [Scaling Mathematical Proof Supervision from Structured Textbooks](https://arxiv.org/abs/2610.40394) — *Hugging Face Daily Papers*
- [Embodied First Exam](https://arxiv.org/abs/2611.12177) — *Hugging Face Daily Papers*

**Archivo reciente · Recent archive:** [2026-11-12](digests/2026/2026-11-12.md) · [2026-11-11](digests/2026/2026-11-11.md) · [2026-11-10](digests/2026/2026-11-10.md) · [2026-11-09](digests/2026/2026-11-09.md) · [2026-11-08](digests/2026/2026-11-08.md) · [2026-11-07](digests/2026/2026-11-07.md) · [2026-11-06](digests/2026/2026-11-06.md) · [2026-11-05](digests/2026/2026-11-05.md) · [2026-11-04](digests/2026/2026-11-04.md) · [2026-11-03](digests/2026/2026-11-03.md)

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
