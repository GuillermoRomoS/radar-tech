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

**Última edición · Latest issue: [2026-10-12](digests/2026/2026-10-12.md)** — 21 elementos/items

**🤖 Robótica · Robotics**
- [Fly-by-Code: Embodied Coding Agents for Aerial Manipulation with Active Visual and Physical Feedback](https://arxiv.org/abs/2610.12549) — *arXiv cs.RO (Robotics)*
- [PanTact: Teaching Whole-Body Dexterity with a Wearable Contact Interface](https://arxiv.org/abs/2610.12558) — *arXiv cs.RO (Robotics)*
- [What Should Embodied Agents Remember? Benchmarking and Evaluating Memory Modality for Embodied Agents](https://arxiv.org/abs/2610.12561) — *arXiv cs.RO (Robotics)*

**🚀 Espacio · Space**
- [APOD: 2026 October 12 – Jupiter and the Moons](https://science.nasa.gov/image-article/apod-2026-october-12-jupiter-and-the-moons/) — *NASA · News Releases*
- [Antarctic Sea Ice Grows to Its 2026 Maximum](https://science.nasa.gov/earth/earth-observatory/antarctic-sea-ice-grows-to-its-2026-maximum/) — *NASA · News Releases*
- [Lunar Mission Will Explore Old Lava Tubes as Potential Habitats](https://spectrum.ieee.org/nasa-moon-mission-gimli-artemis) — *IEEE Spectrum · Aerospace*

**💻 Informática · Computing**
- [Learning to Play Like a Pro: Adaptive Motion Planning and Tracking for Humanoid Robots](https://content.knowledgehub.wiley.com/learning-to-play-like-a-pro-adaptive-motion-planning-and-tracking-for-humanoid-robots/) — *IEEE Spectrum · Computing*

**🧠 Inteligencia artificial · Artificial intelligence**
- [DiffusionART: Efficient, Stable and Scalable Reinforcement of Diffusion Models](https://arxiv.org/abs/2610.12572) — *Hugging Face Daily Papers*
- [S-Space: Exploring Spatial Workspace in Multimodal Language Models](https://arxiv.org/abs/2610.13527) — *Hugging Face Daily Papers*
- [Reflex: Visually Grounded Reactive Humanoid Control](https://arxiv.org/abs/2610.12772) — *Hugging Face Daily Papers*

**Archivo reciente · Recent archive:** [2026-10-12](digests/2026/2026-10-12.md) · [2026-10-11](digests/2026/2026-10-11.md) · [2026-10-10](digests/2026/2026-10-10.md) · [2026-10-09](digests/2026/2026-10-09.md) · [2026-10-08](digests/2026/2026-10-08.md) · [2026-10-07](digests/2026/2026-10-07.md) · [2026-10-06](digests/2026/2026-10-06.md) · [2026-10-05](digests/2026/2026-10-05.md) · [2026-10-04](digests/2026/2026-10-04.md) · [2026-10-03](digests/2026/2026-10-03.md)

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
