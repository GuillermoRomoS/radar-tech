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

**Última edición · Latest issue: [2026-10-02](digests/2026/2026-10-02.md)** — 28 elementos/items

**🤖 Robótica · Robotics**
- [Optimize, Learn, Refine: Whole-Body Grasping and Pick-and-Throw with a Spiral Soft Robot](https://arxiv.org/abs/2609.38202) — *arXiv cs.RO (Robotics)*
- [Fiatlux: A Long-Horizon Benchmark for Humanoid Ladder Climbing and Light-Bulb Replacement](https://arxiv.org/abs/2609.38216) — *arXiv cs.RO (Robotics)*
- [SynIL: Leveraging Synergy for Offline Imitation Learning from Imperfect Demonstration Datasets](https://arxiv.org/abs/2609.38225) — *arXiv cs.RO (Robotics)*

**🚀 Espacio · Space**
- [NASA Awards Enterprise Logistics Support Services Agreements](https://www.nasa.gov/news-release/nasa-awards-enterprise-logistics-support-services-agreements/) — *NASA · News Releases*
- [NASA’s SpaceX Crew-13 Launches](https://www.nasa.gov/image-article/nasas-spacex-crew-13-launches/) — *NASA · News Releases*
- [What’s Up: October 2026 Skywatching Tips from NASA](https://science.nasa.gov/solar-system/skywatching/whats-up-october-2026-skywatching-tips-from-nasa/) — *NASA · News Releases*

**💻 Informática · Computing**
- [A Brief History of the Bloomberg Terminal](https://spectrum.ieee.org/bloomberg-terminal) — *IEEE Spectrum · Computing*

**🧠 Inteligencia artificial · Artificial intelligence**
- [Gemini 4 Argon: our next era of frontier intelligence](https://deepmind.google/blog/gemini-4-argon-our-next-era-of-frontier-intelligence/) — *Google DeepMind Blog*
- [Introducing SynthID Bio](https://deepmind.google/blog/introducing-synthid-bio/) — *Google DeepMind Blog*

**Archivo reciente · Recent archive:** [2026-10-02](digests/2026/2026-10-02.md)

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
