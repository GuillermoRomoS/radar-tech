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

**Última edición · Latest issue: [2026-11-14](digests/2026/2026-11-14.md)** — 13 elementos/items

**🤖 Robótica · Robotics**
- [Video Friday: NASA PROMISEs a New Moon Rover](https://spectrum.ieee.org/video-friday-moon-rover-promise) — *IEEE Spectrum · Robotics*
- [Six AGIBOT G2 Robots Complete 1,730 Tasks in 24-Hour Shanghai Convenience Store Trial](https://www.therobotreport.com/six-agibot-g2-robots-complete-1730-tasks-in-24-hour-shanghai-convenience-store-trial/) — *The Robot Report*
- [How Rhoda AI is using video data to create generalized AI models for robots](https://www.therobotreport.com/how-rhoda-ai-is-using-video-data-to-create-generalized-ai-models-for-robots/) — *The Robot Report*

**🚀 Espacio · Space**
- [Outbursts from a Massive Star](https://www.nasa.gov/image-article/outbursts-from-a-massive-star/) — *NASA · News Releases*
- [Gemini Astronaut Photos Inspired Early Earth Observation Program](https://www.nasa.gov/image-article/gemini-astronaut-photos-inspired-early-earth-observation-program/) — *NASA · News Releases*

**🧠 Inteligencia artificial · Artificial intelligence**
- [Open Vision Banana: A Fully Open Recipe for Generative Visual Perception](https://arxiv.org/abs/2611.15844) — *Hugging Face Daily Papers*
- [Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents](https://arxiv.org/abs/2611.17167) — *Hugging Face Daily Papers*
- [On the Design of Hyper-Connections: Simplification, Stability, and Scalability](https://arxiv.org/abs/2611.05984) — *Hugging Face Daily Papers*

**Archivo reciente · Recent archive:** [2026-11-14](digests/2026/2026-11-14.md) · [2026-11-13](digests/2026/2026-11-13.md) · [2026-11-12](digests/2026/2026-11-12.md) · [2026-11-11](digests/2026/2026-11-11.md) · [2026-11-10](digests/2026/2026-11-10.md) · [2026-11-09](digests/2026/2026-11-09.md) · [2026-11-08](digests/2026/2026-11-08.md) · [2026-11-07](digests/2026/2026-11-07.md) · [2026-11-06](digests/2026/2026-11-06.md) · [2026-11-05](digests/2026/2026-11-05.md)

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
