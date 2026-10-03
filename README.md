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

**Última edición · Latest issue: [2026-10-03](digests/2026/2026-10-03.md)** — 18 elementos/items

**🤖 Robótica · Robotics**
- [Video Friday: Albatross Falls, Spins, Self-Rights, and Sails Away](https://spectrum.ieee.org/video-friday-bioinspired-robotics) — *IEEE Spectrum · Robotics*
- [Inside Omron’s next-generation LD mobile robots](https://www.therobotreport.com/inside-omrons-next-generation-ld-mobile-robots/) — *The Robot Report*
- [Eli Lilly, Purdue to share field learnings on human robot interaction at RoboBusiness](https://www.therobotreport.com/eli-lilly-purdue-to-share-field-learnings-on-human-robot-interaction-at-robobusiness/) — *The Robot Report*

**🚀 Espacio · Space**
- [APOD: 2026 October 3 – Selfie at Vera Rubin Ridge](https://science.nasa.gov/image-article/apod-2026-october-3-selfie-at-vera-rubin-ridge/) — *NASA · News Releases*
- [NASA Astronaut Christina Koch to Join NFL Fans in Philadelphia](https://www.nasa.gov/news-release/nasa-astronaut-christina-koch-to-join-nfl-fans-in-philadelphia/) — *NASA · News Releases*
- [Heading Home: NASA’s SpaceX Crew-12 Concludes Station Science Mission](https://www.nasa.gov/missions/station/iss-research/heading-home-nasas-spacex-crew-12-concludes-station-science-mission/) — *NASA · News Releases*

**🧠 Inteligencia artificial · Artificial intelligence**
- [On-Policy or Off-Policy Learning? A Systematic Study of Distillation Dynamics](https://arxiv.org/abs/2609.35259) — *Hugging Face Daily Papers*
- [Transformers Stop Thinking Too Early, and a Tiny LoRA Fixes It](https://arxiv.org/abs/2609.36585) — *Hugging Face Daily Papers*
- [E-MoE: Enhanced Mixture-of-Experts for Non-Factorized Diffusion Language Models](https://arxiv.org/abs/2609.37533) — *Hugging Face Daily Papers*

**Archivo reciente · Recent archive:** [2026-10-03](digests/2026/2026-10-03.md) · [2026-10-02](digests/2026/2026-10-02.md)

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
