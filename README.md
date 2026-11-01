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

**Última edición · Latest issue: [2026-11-01](digests/2026/2026-11-01.md)** — 8 elementos/items

**🤖 Robótica · Robotics**
- [Unusual robotic animals can prove their utility](https://www.therobotreport.com/unusual-robotic-animals-can-prove-their-utility/) — *The Robot Report*

**🚀 Espacio · Space**
- [APOD: 2026 November 1 – Colors of the Moon](https://science.nasa.gov/image-article/apod-2026-november-1-colors-of-the-moon/) — *NASA · News Releases*

**🧠 Inteligencia artificial · Artificial intelligence**
- [HairDeck: Animation-Ready Stylized Hair Cards from a Single Image](https://arxiv.org/abs/2610.40599) — *Hugging Face Daily Papers*
- [Co-Design Bench: Multimodal Collaborative Coding Evaluation for Agentic Models](https://arxiv.org/abs/2610.35138) — *Hugging Face Daily Papers*
- [WeVisCut: The Whole Editing Room in One Agent From Narration to Long-Form Video](https://arxiv.org/abs/2610.38352) — *Hugging Face Daily Papers*

**Archivo reciente · Recent archive:** [2026-11-01](digests/2026/2026-11-01.md) · [2026-10-31](digests/2026/2026-10-31.md) · [2026-10-30](digests/2026/2026-10-30.md) · [2026-10-29](digests/2026/2026-10-29.md) · [2026-10-28](digests/2026/2026-10-28.md) · [2026-10-27](digests/2026/2026-10-27.md) · [2026-10-26](digests/2026/2026-10-26.md) · [2026-10-25](digests/2026/2026-10-25.md) · [2026-10-24](digests/2026/2026-10-24.md) · [2026-10-23](digests/2026/2026-10-23.md)

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
