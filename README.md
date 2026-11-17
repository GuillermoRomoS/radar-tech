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

**Última edición · Latest issue: [2026-11-17](digests/2026/2026-11-17.md)** — 27 elementos/items

**🤖 Robótica · Robotics**
- [Robustness as a Transferable Skill: Cross-Task Adversarial Defense for Vision-Language-Action Policies](https://arxiv.org/abs/2611.18702) — *arXiv cs.RO (Robotics)*
- [Technical Report of Auriga's 1:10 Scale Autonomous Vehicle Robot](https://arxiv.org/abs/2611.18855) — *arXiv cs.RO (Robotics)*
- [Passage-Focused Soft Coordination for Hierarchical Multi-Robot Navigation in Bottleneck Environments](https://arxiv.org/abs/2611.18877) — *arXiv cs.RO (Robotics)*

**🚀 Espacio · Space**
- [APOD: 2026 November 17 – Milky Way versus Aurora](https://science.nasa.gov/image-article/apod-2026-november-17-milky-way-versus-aurora/) — *NASA · News Releases*
- [Tossing Fireworks from Cloud to Cloud](https://science.nasa.gov/earth/earth-observatory/tossing-fireworks-from-cloud-to-cloud/) — *NASA · News Releases*
- [Perseverance Update: The Ghostly Rocks of ‘Idubi’ — Bright Remnants of Aqueous Systems from Long Ago](https://science.nasa.gov/blog/perseverance-update-the-ghostly-rocks-of-idubi-bright-remnants-of-aqueous-systems-from-long-ago/) — *NASA · News Releases*

**🧠 Inteligencia artificial · Artificial intelligence**
- [Sage S2.1 Flash Technical Report](https://arxiv.org/abs/2611.21072) — *Hugging Face Daily Papers*
- [AllocFlow: End-to-End Portfolio Trading Action Generation from Raw Market Data](https://arxiv.org/abs/2611.19937) — *Hugging Face Daily Papers*
- [K2-Horizon: A Frontier Fleet of Open Source Language Models](https://arxiv.org/abs/2611.21003) — *Hugging Face Daily Papers*

**Archivo reciente · Recent archive:** [2026-11-17](digests/2026/2026-11-17.md) · [2026-11-16](digests/2026/2026-11-16.md) · [2026-11-15](digests/2026/2026-11-15.md) · [2026-11-14](digests/2026/2026-11-14.md) · [2026-11-13](digests/2026/2026-11-13.md) · [2026-11-12](digests/2026/2026-11-12.md) · [2026-11-11](digests/2026/2026-11-11.md) · [2026-11-10](digests/2026/2026-11-10.md) · [2026-11-09](digests/2026/2026-11-09.md) · [2026-11-08](digests/2026/2026-11-08.md)

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
