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

**Última edición · Latest issue: [2026-10-06](digests/2026/2026-10-06.md)** — 27 elementos/items

**🤖 Robótica · Robotics**
- [TACET: Context-Appropriate Acoustic-Social Navigation for Quadrupeds](https://arxiv.org/abs/2610.03828) — *arXiv cs.RO (Robotics)*
- [GOTT: Object-centric Dexterous Manipulation with a Reusable Cross-Embodiment Primitive](https://arxiv.org/abs/2610.03861) — *arXiv cs.RO (Robotics)*
- [MOSAIC-SV: Real-Time Adaptive Identification of Vessel Dynamics for the Control and Deployment of Aquatic Robots](https://arxiv.org/abs/2610.03898) — *arXiv cs.RO (Robotics)*

**🚀 Espacio · Space**
- [APOD: 2026 October 6 – A Complete Auroral Oval from SMILE](https://science.nasa.gov/image-article/apod-2026-october-6-a-complete-auroral-oval-from-smile/) — *NASA · News Releases*
- [The Beaver Brown Waters of Rupert Bay](https://science.nasa.gov/earth/earth-observatory/the-beaver-brown-waters-of-rupert-bay/) — *NASA · News Releases*
- [Curiosity Blog, Sols 5029-5035: Back in the Lab](https://science.nasa.gov/blog/curiosity-blog-sols-5029-5035-back-in-the-lab/) — *NASA · News Releases*

**🧠 Inteligencia artificial · Artificial intelligence**
- [Kandinsky 6.0 Video: Foundation Models for Synchronized Video and Audio Generation](https://arxiv.org/abs/2610.05608) — *Hugging Face Daily Papers*
- [PointWAM: 3D World Action Modeling for Dexterous Robotic Manipulation](https://arxiv.org/abs/2610.02840) — *Hugging Face Daily Papers*
- [ALoDLM: Adaptively Looped Diffusion Language Models](https://arxiv.org/abs/2610.04198) — *Hugging Face Daily Papers*

**Archivo reciente · Recent archive:** [2026-10-06](digests/2026/2026-10-06.md) · [2026-10-05](digests/2026/2026-10-05.md) · [2026-10-04](digests/2026/2026-10-04.md) · [2026-10-03](digests/2026/2026-10-03.md) · [2026-10-02](digests/2026/2026-10-02.md)

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
