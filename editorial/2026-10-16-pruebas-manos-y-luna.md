# Pruebas, manos y Luna: la semana 3 – 16 oct 2026 en robótica, espacio, informática e IA

**Edición nº 2 · 16 de octubre de 2026** · [English version below ↓](#english-version)

> **Cómo leer esta edición.** Cada noticia separa **hechos** (lo que dicen las fuentes, con enlace) de **análisis** (mi lectura, marcada como tal). Junto a cada fuente se indica su tipo: 🟢 *primaria* (la propia organización o la revista científica) · 🟡 *medio especializado*. Cuando dos fuentes no coinciden, se dice.

---

## 🧠 Inteligencia artificial

### 1. OpenAI publica de golpe cientos de demostraciones, entre ellas la conjetura de los juegos únicos (6 oct)

**Hechos (fuente primaria).** El 6 de octubre OpenAI publicó en GitHub un paquete de resultados matemáticos producidos por "un modelo interno de frontera" que no ha nombrado. Según su registro del 7 de octubre, **300 de los 719 resultados principales (~42 %) están formalizados**, es decir, comprobados paso a paso por un verificador automático. Ese mismo día retiró 3 manuscritos por un error de signo y corrigió otros 14. OpenAI dice que el resultado medio usó el equivalente a unas **tres horas de razonamiento de ChatGPT Pro** y publica 10 resúmenes del razonamiento del modelo, pero no los *prompts*. 🟢 [OpenAI](https://openai.com/index/sharing-ai-progress-in-mathematics/) · 🟢 [Registro de formalizaciones](https://github.com/openai/math/blob/main/history.md)

**Hechos (contexto).** Entre los resultados está una demostración de la **conjetura de los juegos únicos** (Khot, 2002), central en la teoría de la aproximación. Un equipo humano (Dor Minzer y sus coautores Fei y Wang) había colgado el 14 de septiembre, a toda prisa tras oír rumores, un artículo de 95 páginas en ECCC con un resultado más débil pero cercano: una variante de la conjetura 2-a-1. Según *Quanta*, el manuscrito de OpenAI no tenía edición humana ni revisión independiente, y su verificación formal cubre la conjetura 2-a-1, sin que quede claro si cubre la demostración completa de los juegos únicos. 🟡 [Quanta Magazine](https://www.quantamagazine.org/as-ai-closed-in-on-unique-games-proof-researchers-raced-to-beat-the-machines-20261007/)

**Hechos (antecedente).** El 8 de septiembre OpenAI ya había anunciado que el mismo tipo de sistema, con "del orden de 10.000 agentes concurrentes", demostraba la **formación de singularidades en Navier–Stokes**, uno de los problemas del Milenio, con una formalización en Lean. El Clay Mathematics Institute habla de un problema "aparentemente resuelto" y de un proceso de evaluación "deliberadamente pausado". OpenAI dice que no reclamará el premio. 🟢 [OpenAI](https://openai.com/index/navier-stokes-solution/) · 🟢 [Clay Mathematics Institute](https://www.claymath.org/news/navier-stokes-announcement/) · 🟡 [IEEE Spectrum](https://spectrum.ieee.org/millennium-prize-ai)

**Análisis.** La parte formalizada es lo más sólido del paquete: un verificador como Lean no se deja convencer por una prosa bonita. Lo demás está "por validar", y la propia OpenAI lo reconoce al retirar y corregir manuscritos al día siguiente. Lo que más me interesa es el cambio de flujo de trabajo: si producir una demostración cuesta tres horas de cómputo, el cuello de botella pasa a ser **entenderla y revisarla**, y eso sigue siendo trabajo humano. Mark Braverman (Princeton) lo resume en *Quanta*: "Las matemáticas por nota de prensa no son muy sanas para las matemáticas". *Nota de transparencia: esta edición se redactó con ayuda de un modelo de Anthropic, competidor de OpenAI; los hechos proceden solo de las fuentes enlazadas.*

### 2. EmbeddingGemma 2: embeddings multimodales que caben en un móvil (6 oct)

**Hechos.** Google publica EmbeddingGemma 2 bajo **Apache 2.0**. Tiene 740 M de parámetros (270 M si solo se usa texto), con codificadores opcionales de visión (170 M) y audio (300 M), y proyecta texto, código, imágenes, vídeo y audio en un mismo espacio vectorial. Contexto de 8K tokens y vectores recortables de 768 a 128 dimensiones (Matryoshka). Cifras de Google: MTEB Code sube de 68,76 a 78,68, y en un Pixel 11 Pro cuantizado ocupa unos 191 MB de RAM solo con texto y 567 MB con todo. Pesos en Hugging Face y Kaggle. 🟢 [Blog de Google](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/)

**Análisis.** No es un titular vistoso, pero es de lo más útil de la quincena: permite montar búsqueda semántica o RAG multimodal **sin servidor ni API de pago**. Las métricas son autodeclaradas; antes de usarlo en serio conviene medirlo con datos propios.

---

## 🤖 Robótica

### 3. AWS lanza un "Physical AI Toolchain" de código abierto (8 oct)

**Hechos.** AWS presentó una cadena de herramientas que une sus servicios (SageMaker para entrenar, IoT Greengrass para desplegar en el robot) con el stack de NVIDIA (Isaac Sim, Isaac Lab, Isaac GR00T y Cosmos). Cubre cinco fases: datos sintéticos, entrenamiento, simulación y validación, despliegue en el borde y mejora continua. Se define como neutral respecto al hardware. AWS recuerda que Amazon opera más de 1 millón de robots. 🟡 [The Robot Report](https://www.therobotreport.com/aws-launches-open-source-physical-ai-toolchain-for-robotics/) · 🟢 [AWS](https://aws.amazon.com/solutions/physical-ai-for-robotics-on-aws/)

**Lectura crítica.** El artículo dice que es *open source*, pero no indica la licencia ni enlaza el repositorio. Y aunque el código sea abierto, el flujo está pensado para ejecutarse en la nube de AWS con el software de NVIDIA: abierto no significa independiente del proveedor. AWS cerró RoboMaker, su anterior plataforma de simulación, en 2025.

### 4. Boston Dynamics cambia de CEO y enseña la nueva mano de Atlas (6 y 9 oct)

**Hechos.** Rohit Prasad, que dirigió la ciencia de Alexa y la familia de modelos Amazon Nova, es el nuevo CEO desde el 7 de octubre. Sustituye a la directora financiera Amanda McMaster, interina desde la salida de Robert Playter en febrero. Su prioridad declarada es llevar la "IA física" a productos comerciales. 🟡 [The Robot Report](https://www.therobotreport.com/boston-dynamics-appoints-former-amazon-executive-rohit-prasad-new-ceo/)

Tres días después, Alberto Rodriguez, responsable de comportamiento de Atlas, explicó la mano rediseñada: **cuatro dedos, 13 grados de libertad, 13 actuadores idénticos encapsulados** y accionamiento directo, sin cables que crucen articulaciones. Quitaron el meñique y descartaron un diseño de dos pulgares por coste y complejidad. Priorizan que sea *backdrivable* y "transparente" para que las políticas aprendidas en simulación pasen directamente al hardware. Sigue levantando más de 45 kg (100 lb). Todavía no está en toda la flota. 🟡 [The Robot Report](https://www.therobotreport.com/boston-dynamics-gives-more-insight-into-its-redesigned-humanoid-hand/)

**Análisis.** Las dos noticias cuentan lo mismo: el reto de los humanoides ya es más de IA y de fabricación que de mecánica pura. Una mano con 13 actuadores iguales es una mano pensada para producirse en serie y para simularse bien, y elegir a un perfil de modelos fundacionales como CEO apunta en la misma dirección.

### 5. Runway presenta Praxis-1, un "modelo de acción del mundo" entrenado con vídeo (2 oct)

**Hechos.** La empresa de vídeo generativo Runway anunció Praxis-1, que convierte su preentrenamiento en vídeo en control de robots. Se entrena sobre todo con vídeo en tercera persona, para depender menos de las escasas demostraciones con robots. Runway afirma que simular políticas en su modelo predice el resultado real con una **correlación de 0,95**. Está en pruebas con Noble Machines, Standard Bots y Ultra, y promete pesos abiertos "en los próximos meses". 🟡 [The Robot Report](https://www.therobotreport.com/runway-introduces-praxis-1-world-action-model-robotics/)

**Lectura crítica.** El 0,95 es una cifra de la empresa, sin benchmark independiente ni detalle de cuántas tareas o robots incluye. La promesa de pesos abiertos, por ahora, también está por validar.

### 6. EE. UU. veta la autorización de robots avanzados fabricados fuera (julio; análisis del 5 oct)

**Hechos.** En julio de 2026 la FCC añadió los robots avanzados de fabricación extranjera, incluidos humanoides y cuadrúpedos capaces de recoger información detallada del entorno, a su lista de tecnologías de riesgo para la seguridad nacional. Eso impide nuevas autorizaciones para importarlos o venderlos en EE. UU. 🟡 [The Robot Report](https://www.therobotreport.com/fcc-robot-restrictions-could-accelerate-shift-to-local-ai/)

**Lectura crítica.** El artículo que lo cuenta es una **tribuna de opinión** firmada por la directora general de un fabricante de controladores, que termina recomendando proveedores "trazables". Su tesis (más procesamiento local y modelos pequeños en fábrica) es razonable, pero es una predicción interesada, no un hecho. Tampoco nombra qué países o empresas quedan afectados.

---

## 🚀 Espacio

### 7. Despega Otter, el "inspector" autónomo de basura espacial (1 oct)

**Hechos.** La misión SSPICY de la NASA lanzó desde Vandenberg la nave **Otter**, de Starfish Space y del tamaño de una lavadora. A partir de principios de 2027 se acercará a "cientos de yardas" de hasta cuatro objetos estadounidenses inactivos en órbita baja, sin tocarlos, para medir su giro, orientación y estado. Navega de forma autónoma con visión por computador, usa propulsión eléctrica y prueba un brazo articulado para orientar los propulsores. 🟢 [NASA](https://www.nasa.gov/centers-and-facilities/ames/nasas-sspicy-mission-to-demonstrate-in-space-inspection-technologies/)

**Análisis.** Es la continuación natural de lo que contamos en la edición nº 1 sobre operaciones de encuentro y proximidad (RPO). Antes de reparar o retirar un satélite muerto hay que saber cómo gira, y eso es un problema de estimación de pose con visión, el mismo que en manipulación robótica.

### 8. La NASA pide propuestas formales para las estaciones que sustituirán a la ISS (9 oct)

**Hechos.** La NASA publicó la solicitud de propuestas definitiva para estaciones espaciales comerciales en órbita baja. Habrá contratos de precio fijo con varios adjudicatarios: al menos dos en la fase de desarrollo y uno o más en la fase final de certificación y servicio. Plazo de propuestas: **8 de diciembre de 2026**. Adjudicación prevista: primavera de 2027. La nota no da importes ni fecha de retirada de la ISS. 🟢 [NASA](https://www.nasa.gov/news-release/nasa-seeks-us-industry-plans-for-commercial-space-stations/)

**Análisis.** El modelo es el mismo que funcionó con la carga y las tripulaciones comerciales: la NASA compra un servicio en vez de construir la estación. La incógnita es el dinero, porque sin cifras es difícil saber cuántas empresas podrán competir de verdad.

### 9. Unos 70 alunizajes en diez años y una misión para explorar un tubo de lava (30 sep – 12 oct)

**Hechos.** Según los documentos de la NASA que cita *IEEE Spectrum*, el plan para una base lunar prevé unos **70 alunizajes en diez años, 45 de ellos antes de 2032**, con siete en 2027 y siete en 2028. Los contratos suelen rondar entre 100 y 200 M$ por misión. Desde el Apolo solo ha habido un alunizaje estadounidense intacto (Blue Ghost 1, marzo de 2025). 🟡 [IEEE Spectrum](https://spectrum.ieee.org/nasa-moon-base-landings)

Dentro de ese plan, la NASA seleccionó tres cargas científicas, entre ellas **GIMLI**, del Planetary Science Institute, que estudiará con radar de penetración, sismómetros y un gravímetro el pozo de Marius Hills, una posible entrada a un tubo de lava que podría servir de refugio. Honeybee Robotics construirá gran parte del equipo. 🟢 [NASA](https://www.nasa.gov/news-release/nasa-adds-new-science-investigations-for-moon-base/) · 🟡 [IEEE Spectrum](https://spectrum.ieee.org/nasa-moon-mission-gimli-artemis)

**Lectura crítica.** *IEEE Spectrum* sitúa el pozo de Marius Hills "cerca del polo sur", pero está en Oceanus Procellarum, en la cara visible y a unos 14° de latitud norte. Y sobre el plan: pasar de un alunizaje intacto en medio siglo a siete por año es un salto enorme. Las cifras son objetivos, no hitos.

### 10. Vuelve la Crew-12 tras 237 días; Sentinel-3C manda sus primeros datos (8–9 oct)

**Hechos.** La misión εpsilon (Crew-12) amerizó el 8 de octubre a las 15:34 GMT tras **237 días** en el espacio, con la astronauta de la ESA Sophie Adenot, Jessica Meir y Jack Hathaway (NASA) y Andrei Fedyaev (Roscosmos). Adenot dedicó unas 218 horas a 35 experimentos europeos. 🟢 [ESA](https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/epsilon/ESA_astronaut_Sophie_Adenot_returns_from_her_first_mission_to_the_International_Space_Station)

El satélite Copernicus **Sentinel-3C**, lanzado el 15 de septiembre, publicó sus primeras imágenes de color del océano y medidas de altura del hielo de Groenlandia. Le quedan unos cinco meses de puesta en servicio. 🟢 [ESA](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-3/Sentinel-3C_returns_its_first_views_of_Earth)

---

## 💻 Informática

### 11. Anderon, la "TSMC de los chips cuánticos" de IBM, recibe hasta 1.000 M$ (16 sep; análisis del 7 oct)

**Hechos.** El Departamento de Comercio de EE. UU. cerró una ayuda de I+D de la Ley CHIPS de **hasta 1.000 M$** para Anderon, filial de IBM creada este año, e IBM pone otros 1.000 M$. Anderon fabricará chips cuánticos superconductores en una línea de obleas de 300 mm en Albany (Nueva York) para terceros, con kits de diseño como una fundición convencional: "Ellos diseñan, nosotros fabricamos", dice su CEO, Mukesh Khare. Promete entregar obleas a clientes externos antes de fin de 2026. 🟡 [IEEE Spectrum](https://spectrum.ieee.org/anderon-quantum-fab)

**Lectura crítica.** El rendimiento de una fábrica cuántica se mide en qubits que funcionan, no en obleas. Rigetti cuenta que su fábrica manual ronda el 50 % de rendimiento y que habrá que comprobar si la automatización de Anderon lo mejora. Que una filial de IBM trabaje de forma neutral para los competidores de IBM también está por ver.

---

## 🎓 Qué hacer con esto (para estudiantes de Robótica e IA)

1. **Leer una demostración formalizada.** Elegir uno de los resultados de OpenAI que tenga prueba en Lean y seguirla con el verificador. Es la mejor forma de distinguir lo comprobado de lo anunciado.
2. **Montar un buscador multimodal local con EmbeddingGemma 2** (por ejemplo, sobre los PDF y vídeos de una asignatura). Es un proyecto de portfolio pequeño, gratuito y demostrable.
3. **Reproducir un problema de estimación de pose de un objeto que gira** en simulación (Gazebo o Isaac Sim), el mismo que resolverá Otter en órbita.

---

<a id="english-version"></a>

# English version: Proofs, hands and the Moon (Oct 3 – 16, 2026)

> **How to read this issue.** Each story separates **facts** (what the linked sources say) from **analysis** (my reading, labelled). Source type: 🟢 *primary* · 🟡 *specialised media*. Discrepancies between sources are flagged.

## 🧠 AI

**1. OpenAI releases hundreds of AI-generated proofs, including the Unique Games Conjecture (Oct 6).** The results come from an unnamed internal model. As of Oct 7, **300 of 719 top-line results (~42%) were formalized**; 3 manuscripts were withdrawn over a sign error and 14 revised. The average result used roughly three hours of ChatGPT Pro–equivalent compute; prompts were not released. 🟢 [OpenAI](https://openai.com/index/sharing-ai-progress-in-mathematics/) · 🟢 [Formalization log](https://github.com/openai/math/blob/main/history.md) A human team (Minzer, Fei, Wang) had rushed out a 95-page paper on a weaker 2-to-1 variant on Sept 14. *Quanta* reports that OpenAI's manuscript had no human editing or independent review. 🟡 [Quanta](https://www.quantamagazine.org/as-ai-closed-in-on-unique-games-proof-researchers-raced-to-beat-the-machines-20261007/) Background: OpenAI's Sept 8 Navier–Stokes blow-up claim, which the Clay Institute calls "apparently settled" and is reviewing slowly. 🟢 [OpenAI](https://openai.com/index/navier-stokes-solution/) · 🟢 [Clay](https://www.claymath.org/news/navier-stokes-announcement/) — *Analysis:* the formalized part is the solid part; the rest is unverified. When a proof costs three hours of compute, the bottleneck becomes understanding and reviewing it. *Transparency note: drafted with help from an Anthropic model, an OpenAI competitor; facts come only from the linked sources.*

**2. EmbeddingGemma 2 (Oct 6).** Apache 2.0, 740M parameters (270M text-only), one embedding space for text, code, images, video and audio, 8K context, Matryoshka vectors (768→128). Google reports MTEB Code rising from 68.76 to 78.68 and about 191 MB of RAM for text-only on a Pixel 11 Pro. 🟢 [Google](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/) — *Analysis:* multimodal semantic search or RAG with no server and no paid API.

## 🤖 Robotics

**3. AWS open-sources a Physical AI Toolchain (Oct 8)** combining SageMaker and IoT Greengrass with NVIDIA Isaac Sim, Isaac Lab, GR00T and Cosmos. 🟡 [The Robot Report](https://www.therobotreport.com/aws-launches-open-source-physical-ai-toolchain-for-robotics/) — *Critical note:* no licence or repo is named, and open code built around one cloud and one GPU stack is not vendor-neutral.

**4. Boston Dynamics: new CEO and a new Atlas hand (Oct 6 & 9).** Former Amazon Alexa/Nova chief scientist Rohit Prasad is CEO. 🟡 [The Robot Report](https://www.therobotreport.com/boston-dynamics-appoints-former-amazon-executive-rohit-prasad-new-ceo/) The redesigned hand has four fingers, 13 DoF and 13 identical encapsulated actuators, built for mass production and sim-to-real transfer. 🟡 [The Robot Report](https://www.therobotreport.com/boston-dynamics-gives-more-insight-into-its-redesigned-humanoid-hand/)

**5. Runway's Praxis-1 world action model (Oct 2)** is trained mostly on third-person video. Runway claims a 0.95 sim-to-real correlation (*self-reported*) and promises open weights "in the coming months". 🟡 [The Robot Report](https://www.therobotreport.com/runway-introduces-praxis-1-world-action-model-robotics/)

**6. FCC restrictions on foreign-made advanced robots (July; analysis Oct 5).** *Critical note:* the coverage is an op-ed by a controller vendor, so its "shift to local AI" thesis is a prediction, not a fact. 🟡 [The Robot Report](https://www.therobotreport.com/fcc-robot-restrictions-could-accelerate-shift-to-local-ai/)

## 🚀 Space

**7. Otter launches (Oct 1).** NASA's SSPICY mission will autonomously inspect up to four defunct US objects in LEO from early 2027, without touching them. 🟢 [NASA](https://www.nasa.gov/centers-and-facilities/ames/nasas-sspicy-mission-to-demonstrate-in-space-inspection-technologies/)

**8. Final RFP for commercial LEO stations (Oct 9).** Proposals are due Dec 8, 2026, with awards expected in spring 2027. No dollar figures are given. 🟢 [NASA](https://www.nasa.gov/news-release/nasa-seeks-us-industry-plans-for-commercial-space-stations/)

**9. About 70 Moon landings in ten years, plus GIMLI.** 🟡 [IEEE Spectrum](https://spectrum.ieee.org/nasa-moon-base-landings) · 🟢 [NASA](https://www.nasa.gov/news-release/nasa-adds-new-science-investigations-for-moon-base/) — *Critical note:* *Spectrum* places the Marius Hills pit "near the south pole", but it lies in Oceanus Procellarum at about 14°N.

**10. Crew-12 returns after 237 days (Oct 8)** 🟢 [ESA](https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/epsilon/ESA_astronaut_Sophie_Adenot_returns_from_her_first_mission_to_the_International_Space_Station), **and Sentinel-3C sends its first data** 🟢 [ESA](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-3/Sentinel-3C_returns_its_first_views_of_Earth).

## 💻 Computing

**11. Anderon, IBM's quantum foundry, gets up to $1B in CHIPS funding**, matched by IBM. It builds superconducting chips on a 300 mm line in Albany. 🟡 [IEEE Spectrum](https://spectrum.ieee.org/anderon-quantum-fab) — *Critical note:* what counts is working qubits, not wafers, and the neutrality toward IBM's rivals is still to be shown.

---

*Fuentes consultadas el 13 oct 2026 · Sources accessed Oct 13, 2026. ¿Has visto un error? Abre un issue · Spotted an error? Open an issue.*
