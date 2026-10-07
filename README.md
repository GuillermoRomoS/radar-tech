# 📡 Radar Tech: robótica, espacio, informática e IA

**ES** · Un radar diario y **verificable** de lo que se publica en robótica, espacio, informática e inteligencia artificial: artículos de investigación (arXiv, Hugging Face Papers), fuentes oficiales (NASA, ESA, Google DeepMind) y medios especializados (IEEE Spectrum, The Robot Report, Quanta). Además, una **edición editorial** con análisis crítico.

**EN** · A daily, **verifiable** radar of new work in robotics, space, computing and AI: research papers, official sources and specialised media, plus an **editorial issue** with critical analysis.

[![Radar diario](https://github.com/GuillermoRomoS/radar-tech/actions/workflows/radar.yml/badge.svg)](https://github.com/GuillermoRomoS/radar-tech/actions/workflows/radar.yml)
· 📰 [Ediciones editoriales · Editorials](editorial/) · 🗂️ [Archivo diario · Daily archive](digests/) · 🔔 [RSS](feed.xml)

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

**Última edición · Latest issue: [2026-10-07](digests/2026/2026-10-07.md)** — 30 elementos/items

**🤖 Robótica · Robotics**
- [Generalizable Robustness Testing of DNN-Based Robotic Navigation Systems via XAI-Guided Search](https://arxiv.org/abs/2610.06862) — *arXiv cs.RO (Robotics)*
- [RMRRT: Riemannian Barrier Metric RRT for Inequality-Aware Steering on Equality Manifolds](https://arxiv.org/abs/2610.06863) — *arXiv cs.RO (Robotics)*
- [Geometric Coherence via Weighted Matching for 3D Heterogeneous Multi-Agent Reach-Avoid Games](https://arxiv.org/abs/2610.06882) — *arXiv cs.RO (Robotics)*

**🚀 Espacio · Space**
- [APOD: 2026 October 7 – Supernova Remnant Pa 30](https://science.nasa.gov/image-article/apod-2026-october-7-supernova-remnant-pa-30/) — *NASA · News Releases*
- [Arctic Sea Ice Shrinks to Its 2026 Minimum](https://science.nasa.gov/earth/earth-observatory/arctic-sea-ice-shrinks-to-its-2026-minimum/) — *NASA · News Releases*
- [NASA to Cover Northrop Grumman CRS-24 Spacecraft Departure](https://www.nasa.gov/news-release/nasa-to-cover-northrop-grumman-crs-24-spacecraft-departure/) — *NASA · News Releases*

**🧠 Inteligencia artificial · Artificial intelligence**
- [Rethinking Cross-Tokenizer On-Policy Distillation: From Alignment Coverage to Supervision Reliability](https://arxiv.org/abs/2610.08448) — *Hugging Face Daily Papers*
- [DuoMatching: Joint-Marginal Distribution Matching for Few-Step Video Generation](https://arxiv.org/abs/2610.03543) — *Hugging Face Daily Papers*
- [TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models](https://arxiv.org/abs/2610.07767) — *Hugging Face Daily Papers*

**Archivo reciente · Recent archive:** [2026-10-07](digests/2026/2026-10-07.md) · [2026-10-06](digests/2026/2026-10-06.md) · [2026-10-05](digests/2026/2026-10-05.md) · [2026-10-04](digests/2026/2026-10-04.md) · [2026-10-03](digests/2026/2026-10-03.md) · [2026-10-02](digests/2026/2026-10-02.md)

<!-- RADAR:END -->

## Cómo funciona · How it works

```
sources.json ──► radar.py ──► digests/AAAA/AAAA-MM-DD.md
 (12 feeds)      │  ├─ RSS 2.0 / Atom / API Hugging Face
                 │  ├─ ventana de 48 h + deduplicación (data/seen.json)
                 │  ├─ arXiv: solo envíos nuevos (announce_type = new)
                 │  └─ README.md (este bloque) + feed.xml + data/latest.json
GitHub Actions (cron diario 05:17 UTC) ──► commit automático
```

```bash
python radar.py --dry-run          # previsualizar sin escribir · preview only
python radar.py                    # generar la edición de hoy · build today's issue
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
