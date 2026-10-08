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

**Última edición · Latest issue: [2026-10-08](digests/2026/2026-10-08.md)** — 32 elementos/items

**🤖 Robótica · Robotics**
- [A Review Of Robotic World Models For Dynamic Environments Based On Factor And Scene Graphs](https://arxiv.org/abs/2610.08800) — *arXiv cs.RO (Robotics)*
- [SAFE: Unified Slip and Fracture Detection with Low-Cost Acoustic Sensing in Robotic Grasping](https://arxiv.org/abs/2610.08802) — *arXiv cs.RO (Robotics)*
- [Context-Aware Adaptive Pesticide Spraying for Agricultural Robots under Changing Weather and Terrain Using Vision-Language Models](https://arxiv.org/abs/2610.08807) — *arXiv cs.RO (Robotics)*

**🚀 Espacio · Space**
- [APOD: 2026 October 8 – The Saturn System Smörgåsbord](https://science.nasa.gov/image-article/apod-2026-october-8-the-saturn-system-smorgasbord/) — *NASA · News Releases*
- [Fighting Drought in Texas Cotton Country](https://science.nasa.gov/earth/earth-observatory/fighting-drought-in-texas-cotton-country/) — *NASA · News Releases*
- [NASA Sets Coverage for SpaceX 35th Station Resupply Launch, Arrival](https://www.nasa.gov/news-release/nasa-sets-coverage-for-spacex-35th-station-resupply-launch-arrival/) — *NASA · News Releases*

**💻 Informática · Computing**
- [The U.S. Just Bet $1 Billion on Quantum Chip Manufacturing](https://spectrum.ieee.org/anderon-quantum-fab) — *IEEE Spectrum · Computing*
- [As AI Closed In on ‘Unique Games’ Proof, Researchers Raced to Beat the Machines](https://www.quantamagazine.org/as-ai-closed-in-on-unique-games-proof-researchers-raced-to-beat-the-machines-20261007/) — *Quanta Magazine · Computer Science*

**🧠 Inteligencia artificial · Artificial intelligence**
- [STEPQuant: When and Where Errors Matter in Delta-Rule Recurrent State Quantization](https://arxiv.org/abs/2609.38169) — *Hugging Face Daily Papers*
- [Long-WAM: Scaling the Context of World-Action Models](https://arxiv.org/abs/2610.10528) — *Hugging Face Daily Papers*
- [Recursive Game Creator: An Agentic Product-Level Experience-Oriented Game Harness](https://arxiv.org/abs/2610.08621) — *Hugging Face Daily Papers*

**Archivo reciente · Recent archive:** [2026-10-08](digests/2026/2026-10-08.md) · [2026-10-07](digests/2026/2026-10-07.md) · [2026-10-06](digests/2026/2026-10-06.md) · [2026-10-05](digests/2026/2026-10-05.md) · [2026-10-04](digests/2026/2026-10-04.md) · [2026-10-03](digests/2026/2026-10-03.md) · [2026-10-02](digests/2026/2026-10-02.md)

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
