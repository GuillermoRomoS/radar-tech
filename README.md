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

**Última edición · Latest issue: [2026-10-09](digests/2026/2026-10-09.md)** — 30 elementos/items

**🤖 Robótica · Robotics**
- [Does Dynamic-Point Filtering Help When Texture Is Scarce? A Controlled Study of ORB-SLAM2 Front-Ends in Synthetic Indoor Scenes](https://arxiv.org/abs/2610.10564) — *arXiv cs.RO (Robotics)*
- [Teaching a Robot Dog New Tricks: Diverse Quadruped Skills via Combined Reinforcement and Imitation Learning with Adversarial Task Selection](https://arxiv.org/abs/2610.10601) — *arXiv cs.RO (Robotics)*
- [TacHair: Tactile Contact-Distribution Guided Online Correction for Robotic Hair Stroking and Perception](https://arxiv.org/abs/2610.10637) — *arXiv cs.RO (Robotics)*

**🚀 Espacio · Space**
- [APOD: 2026 October 9 – Stickney Crater](https://science.nasa.gov/image-article/apod-2026-october-9-stickney-crater/) — *NASA · News Releases*
- [Floodwaters Overwhelm Thailand](https://science.nasa.gov/earth/earth-observatory/floodwaters-overwhelm-thailand/) — *NASA · News Releases*
- [NASA Briefing to Highlight Contributions to Martian Moons Mission](https://www.nasa.gov/news-release/nasa-briefing-to-highlight-contributions-to-martian-moons-mission/) — *NASA · News Releases*

**🧠 Inteligencia artificial · Artificial intelligence**
- [From Traces to Agentic Worlds: Agentic Language World Models for Interactive Environment Simulation](https://arxiv.org/abs/2610.06100) — *Hugging Face Daily Papers*
- [Learn2Play Bench: How Well Do LLM Agents Learn from Experience in Unfamiliar Environments?](https://arxiv.org/abs/2610.08215) — *Hugging Face Daily Papers*
- [TokenRouter: Efficient Serving System for Token-Level LLM Routing](https://arxiv.org/abs/2610.12242) — *Hugging Face Daily Papers*

**Archivo reciente · Recent archive:** [2026-10-09](digests/2026/2026-10-09.md) · [2026-10-08](digests/2026/2026-10-08.md) · [2026-10-07](digests/2026/2026-10-07.md) · [2026-10-06](digests/2026/2026-10-06.md) · [2026-10-05](digests/2026/2026-10-05.md) · [2026-10-04](digests/2026/2026-10-04.md) · [2026-10-03](digests/2026/2026-10-03.md) · [2026-10-02](digests/2026/2026-10-02.md)

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
