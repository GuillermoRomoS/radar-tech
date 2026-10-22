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

**Última edición · Latest issue: [2026-10-22](digests/2026/2026-10-22.md)** — 28 elementos/items

**🤖 Robótica · Robotics**
- [Real-Time Ground Normal Vector Estimation for Spherical Mobile 3D Mapping using LiDAR-Inertial Odometry](https://arxiv.org/abs/2610.28701) — *arXiv cs.RO (Robotics)*
- [Warping the Workspace: Expanding Visual Access with Adjustable Reach Mapping for Humanoid Teleoperation](https://arxiv.org/abs/2610.28712) — *arXiv cs.RO (Robotics)*
- [Human-Robot Interaction via Meta-Learning Based Mode Recognition and Adaptive Control](https://arxiv.org/abs/2610.28761) — *arXiv cs.RO (Robotics)*

**🚀 Espacio · Space**
- [APOD: 2026 October 22 – The First Green Star, WD J1330+6435](https://science.nasa.gov/image-article/apod-2026-october-22-the-first-green-star-wd-j13306435/) — *NASA · News Releases*
- [Fires Char New Guinea](https://science.nasa.gov/earth/earth-observatory/fires-char-new-guinea/) — *NASA · News Releases*
- [Faster to Science: A Letter to the Science Community](https://science.nasa.gov/directorates/smd/faster-to-science-a-letter-to-the-science-community/) — *NASA · News Releases*

**🧠 Inteligencia artificial · Artificial intelligence**
- [Cache Engineering for Agents](https://arxiv.org/abs/2610.28577) — *Hugging Face Daily Papers*
- [SpatialScout: Can VLM Agents Actively Explore and Map 3D Scenes?](https://arxiv.org/abs/2610.26659) — *Hugging Face Daily Papers*
- [Looking Ahead: Modeling Future Evolution in Autoregressive Video Generation](https://arxiv.org/abs/2610.29989) — *Hugging Face Daily Papers*

**Archivo reciente · Recent archive:** [2026-10-22](digests/2026/2026-10-22.md) · [2026-10-21](digests/2026/2026-10-21.md) · [2026-10-20](digests/2026/2026-10-20.md) · [2026-10-19](digests/2026/2026-10-19.md) · [2026-10-18](digests/2026/2026-10-18.md) · [2026-10-17](digests/2026/2026-10-17.md) · [2026-10-16](digests/2026/2026-10-16.md) · [2026-10-15](digests/2026/2026-10-15.md) · [2026-10-14](digests/2026/2026-10-14.md) · [2026-10-13](digests/2026/2026-10-13.md)

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
