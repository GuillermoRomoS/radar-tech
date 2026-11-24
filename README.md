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

**Última edición · Latest issue: [2026-11-24](digests/2026/2026-11-24.md)** — 25 elementos/items

**🤖 Robótica · Robotics**
- [5G NR Sensing of Robotic Arm Motion in Indoor Factory Environments](https://arxiv.org/abs/2611.28053) — *arXiv cs.RO (Robotics)*
- [FlowPAC: Flow-Guided Visual Pruning and Action Caching for Efficient VLA Inference](https://arxiv.org/abs/2611.28256) — *arXiv cs.RO (Robotics)*
- [Neural Fidelity Calibration: Turning Field Anomalies into Simulation Fine-Tuning](https://arxiv.org/abs/2611.28260) — *arXiv cs.RO (Robotics)*

**🚀 Espacio · Space**
- [NASA Hubble’s New View of NGC 4394 Raises the Bar](https://science.nasa.gov/missions/hubble/nasa-hubbles-new-view-of-ngc-4394-raises-the-bar/) — *NASA · News Releases*
- [APOD: 2026 November 24 – Galaxies Battle in the NGC 7771 Group](https://science.nasa.gov/image-article/apod-2026-november-24-galaxies-battle-in-the-ngc-7771-group/) — *NASA · News Releases*
- [Eruption Extends Iwo Jima’s Beach](https://science.nasa.gov/earth/earth-observatory/eruption-extends-iwo-jimas-beach/) — *NASA · News Releases*

**🧠 Inteligencia artificial · Artificial intelligence**
- [Motion Mamba 2.0: Autoregressive Diffusion Mamba for Long-Horizon Humanoid Control](https://arxiv.org/abs/2611.29897) — *Hugging Face Daily Papers*
- [Embo-Harness: Towards Understanding Frontier-Model-as-Policy Harness](https://arxiv.org/abs/2611.31201) — *Hugging Face Daily Papers*
- [WorldLeague: Benchmarking Physical Agency](https://arxiv.org/abs/2611.30989) — *Hugging Face Daily Papers*

**Archivo reciente · Recent archive:** [2026-11-24](digests/2026/2026-11-24.md) · [2026-11-23](digests/2026/2026-11-23.md) · [2026-11-22](digests/2026/2026-11-22.md) · [2026-11-21](digests/2026/2026-11-21.md) · [2026-11-20](digests/2026/2026-11-20.md) · [2026-11-19](digests/2026/2026-11-19.md) · [2026-11-18](digests/2026/2026-11-18.md) · [2026-11-17](digests/2026/2026-11-17.md) · [2026-11-16](digests/2026/2026-11-16.md) · [2026-11-15](digests/2026/2026-11-15.md)

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
