# Órbita, código abierto y lupa: la semana 21 sep – 2 oct 2026 en robótica, espacio, informática e IA

**Edición nº 1 · 2 de octubre de 2026** · [English version below ↓](#english-version)

> **Cómo leer esta edición.** Cada noticia separa **hechos** (lo que dicen las fuentes, con enlace) de **análisis** (mi lectura, marcada como tal). Junto a cada fuente se indica su tipo: 🟢 *primaria* (la propia organización o la revista científica) · 🟡 *medio especializado*. Cuando dos fuentes no coinciden, se dice.

---

## 🚀 Espacio

### 1. Starship alcanza la órbita por primera vez (Flight 14, 28 sep)

**Hechos.** El 28 de septiembre de 2026 a las 8:49 EDT, SpaceX lanzó el Booster 21 con la Ship 41 desde el Pad 2 de Starbase (Texas). La Ship 41 completó su encendido de inserción orbital a T+25 min 17 s y alcanzó una órbita de unos 275 km. Desplegó 26 satélites Starlink V3, tres de ellos con cámaras para inspeccionar las losetas del escudo térmico de la nave, y amerizó en el Pacífico Norte hacia las 11:58 EDT. SpaceX adelantó el regreso: la misión duró unas 3 h 9 min frente a las ~10 h previstas. El propulsor realizó su encendido de aterrizaje sobre la zona de amerizaje del Golfo. 🟡 [Space.com](https://www.space.com/news/live/spacex-starship-flight-14-live-updates-sept-28-2026-starship-first-orbital-launch-attempt)

**Análisis.** Es el hito que faltaba: hasta ahora los vuelos de Starship eran suborbitales. Usar satélites con cámara para fotografiar el escudo térmico desde fuera es una idea de ingeniería muy reutilizable: convierte la carga útil en un instrumento de inspección. La vuelta anticipada queda abierta: las fuentes consultadas no explican el motivo, así que conviene esperar al informe de SpaceX.

### 2. Crew-13 bate el récord estadounidense de llegada a la ISS (1 oct)

**Hechos.** El 1 de octubre a las 11:10 EDT despegó un Falcon 9 con la Crew Dragon *Grace*: Jessica Watkins (NASA, comandante), Luke Delaney (NASA, piloto), Joshua Kutryk (Agencia Espacial Canadiense) y Sergey Teteryatnikov (Roscosmos). Se acopló a la ISS a las 19:05 EDT, **7 h 55 min** después del lanzamiento: el viaje más rápido hasta la estación de una nave estadounidense. La ISS queda con 11 personas a bordo para la Expedición 75. 🟡 [Space.com](https://space.com/news/live/spacex-nasa-crew-13-astronauts-launch-to-iss-september-30-2026)

**Análisis.** Que la tripulación incluya a NASA, CSA y Roscosmos en la misma cápsula muestra que la cooperación operativa en la ISS sigue funcionando. Un acoplamiento más rápido se consigue con trayectorias de encuentro más directas, y para la tripulación significa menos horas encerrada en la cápsula.

### 3. Navegación autónoma europea: Blackswan Space levanta 2,5 M€ (30 sep)

**Hechos.** La lituana Blackswan Space (fundada en 2019, 25 empleados entre Vilna, Londres y Denver) cerró una Serie A de 2,5 M€ liderada por Iron Wolf Capital (3,2 M€ en total). Desarrolla un simulador de diseño de misiones y el **RPO Kit**, una carga útil de visión para operaciones de encuentro y proximidad. Prevé probarlo en órbita en el 4T de 2027 y dar soporte en 2028 a ASTRAL, la primera misión europea de repostaje en órbita, que cuenta con 3,3 M€ de la UK Space Agency y la ESA. 🟡 [Tech.eu](https://tech.eu/2026/09/30/blackswan-space-raises-eur25m-to-take-autonomous-spacecraft-navigation-into-orbit)

**Análisis.** Aquí se juntan robótica y espacio: la visión por computador y el control para acercarse a otro objeto en órbita son los mismos problemas que la manipulación móvil, pero en microgravedad. Para un perfil de Robótica + IA es un nicho europeo con demanda real.

---

## 🤖 Robótica

### 4. Qualcomm compra PickNik y promete mantener MoveIt abierto (23 sep)

**Hechos.** Qualcomm anunció la compra de PickNik Robotics (Boulder, 2015), la empresa que mantiene **MoveIt**, el framework de manipulación de ROS. No se han hecho públicos los términos. Qualcomm se compromete a mantener MoveIt 1 y 2 como código abierto, con sus licencias actuales y una hoja de ruta comunitaria. El producto comercial MoveIt Pro se integrará con sus plataformas Dragonwing y con Arduino, que Qualcomm compró en octubre de 2025, incluida la nueva placa VENTUNO Q. 🟡 [The Robot Report](https://www.therobotreport.com/qualcomm-acquires-picknik-robotics-keep-moveit-open-source/)

**Análisis.** Qualcomm ya tiene el chip (Dragonwing), la placa para *makers* (Arduino) y ahora el software de manipulación más usado de ROS: es una integración vertical. La promesa de mantenerlo abierto es verificable: basta con vigilar el ritmo de commits y la gobernanza del [repositorio de MoveIt](https://github.com/moveit/moveit2) en los próximos meses.

### 5. Intrinsic (Alphabet) libera *Intrinsic Core* bajo Apache 2.0 (22 sep)

**Hechos.** Intrinsic presentó en ROSCon 2026 (Toronto) **Intrinsic Core**, un conjunto de capacidades compatibles con ROS: control en tiempo real independiente del hardware, estimación de pose con FoundationPose de NVIDIA, planificación de movimiento con evitación de colisiones, planificación de agarre, simulación con Gazebo, calibración de cámaras y drivers ROS preconfigurados. También publicó una solución de referencia para la carga de máquinas CNC (OMTS). Licencia Apache 2.0. Brian Gerkey, CTO de Intrinsic, explicó que es el núcleo de su propio stack. 🟡 [The Robot Report](https://www.therobotreport.com/intrinsic-open-sources-key-parts-platform-easier-development/) · 🟢 [Repositorio](https://github.com/intrinsic-ai/intrinsic-core)

**Análisis.** Junto con la noticia anterior, se ve que el software de robótica industrial se está consolidando en torno a ROS 2 con licencias permisivas. Para estudiantes, la parte de carga de máquinas CNC es un caso de uso cerrado y bien documentado, adecuado para un proyecto de portfolio.

### 6. Boston Dynamics abre una "fábrica de comportamientos" para Atlas (21 sep)

**Hechos.** Boston Dynamics inauguró el *Robotics Metaplant Application Center* (RMAC) en la Metaplant de Hyundai cerca de Savannah (Georgia). Allí se entrena y prueba Atlas en tareas reales de automoción: secuenciar piezas, manipulación bimanual de componentes pesados o frágiles y desembalaje. Prevén ampliarlo a montaje de componentes hacia 2030. Entrenan con teleoperación, aprendizaje por refuerzo en simulación y dispositivos UMI. Hyundai plantea desplegar **25.000 Atlas** en sus plantas y las de Kia "en los próximos años" y una fábrica en EE. UU. de 30.000 robots/año para 2028. 🟡 [The Robot Report](https://www.therobotreport.com/boston-dynamics-opens-metaplant-application-center-train-atlas-humanoid-robots/)

**Análisis.** El cuello de botella de los humanoides ya no es el hardware, sino los **datos de comportamiento**, y el RMAC está pensado para producirlos. Las cifras de 25.000 unidades y 30.000/año son planes declarados, todavía por validar.

### 7. Unitree: −53 % desde su máximo tras la OPV (dato del 9 sep)

**Hechos.** Unitree salió a bolsa el 19 de agosto en el STAR Market de Shanghái (688836) a 150,80 yuanes. Cerró su primer día a 845 y llegó a un máximo de 1.100. El 9 de septiembre cotizaba a 513,93 yuanes: un 39 % menos que el cierre del debut y un 53 % menos que el máximo. Ingresó 1.700 M de yuanes en 2025, el 51,78 % por humanoides, y cotizaba a unas 125 veces esos ingresos. 🟡 [The Robot Report](https://www.therobotreport.com/unitree-shares-down-53-from-ipo-debut/)

**Análisis · lectura crítica.** El titular original habla de "−53 % desde el debut", pero según los datos del propio artículo ese 53 % se mide **desde el máximo**; desde el cierre del primer día la caída es del 39 %. Aun así, la acción sigue muy por encima del precio de la OPV. Al contrario que muchos competidores occidentales, Unitree factura de verdad, pero 125 veces los ingresos sigue siendo una valoración de expectativas.

---

## 🧠 Inteligencia artificial

### 8. Google presenta Gemini 4 Argon (30 sep)

**Hechos (fuente primaria).** Google lo presenta como su nuevo modelo de frontera para tareas largas de ingeniería de software, trabajo empresarial y ciberseguridad. Admite hasta **1 millón de tokens de salida** (antes, 64K). Resultados que publica Google: DeepSWE v1.1 77,9 %, AutomationBench 51,3 % (n.º 1), CWE-bench v1 68 % (empatado en primer puesto), LVBench 91,7 %. Precio introductorio de 2 $/10 $ por millón de tokens de entrada/salida, que pasará a 4 $/20 $. El despliegue empieza por defensores de ciberseguridad de confianza (programa *Fairwind*). 🟢 [Blog de Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)

**Lectura crítica.** Algunos boletines secundarios publicaron cifras distintas: por ejemplo, un 77,5 % en AutomationBench que no aparece en la fuente primaria. Aquí usamos las de Google y recordamos que son **autodeclaradas**: falta una evaluación independiente.

### 9. SynthID Bio: marcas de agua en proteínas diseñadas por IA, publicado en *Nature* (30 sep)

**Hechos.** Google DeepMind publica en *Nature* un método para marcar con una "firma" imperceptible las proteínas diseñadas por IA. Funciona tanto en la **secuencia**, guiando la elección de aminoácidos, como en la **estructura 3D**, con un AlphaFold 3 ajustado para que sus predicciones lleven la marca. En *binders* contra VEGF-A, el RBD del SARS-CoV-2 y PD-L1, los diseños marcados igualaron a los no marcados en afinidad y tasa de acierto. Liberan código, datos *in vitro* y pesos. Los autores reconocen como limitación la robustez frente a manipulación deliberada. 🟢 [Google DeepMind](https://deepmind.google/blog/introducing-synthid-bio/)

**Análisis.** Es una pieza de bioseguridad pensada para las empresas de síntesis de ADN, que podrían comprobar el origen de un diseño. No resuelve el problema si alguien elimina la marca a propósito, y los autores lo dicen expresamente.

### 10. La FTC abre una investigación sobre OpenAI y Anthropic (30 sep)

**Hechos.** La Comisión Federal de Comercio de EE. UU. abrió una investigación sobre Anthropic y OpenAI por posibles prácticas desleales o engañosas y daños a consumidores. Un alto cargo indicó que podría exigir formalmente información a las empresas. 🟡 [ABC News](https://abcnews.com/Politics/ftc-opens-probe-safety-ai-including-anthropic-open/story?id=136896227)

**Análisis.** La regulación de la IA en EE. UU. se está haciendo **a través de la protección del consumidor** más que con una ley específica. *Nota de transparencia: esta edición se redactó con ayuda de un modelo de Anthropic; los hechos proceden solo de la fuente enlazada.*

---

## 💻 Informática

### 11. Infleqtion anuncia 30 qubits lógicos entrelazados… con letra pequeña (24–27 sep)

**Hechos (empresa).** Infleqtion afirma haber entrelazado 30 qubits lógicos con 80 qubits físicos en su ordenador de átomos neutros Sqale, con unas 1.000 operaciones físicas y una señal unas 1.000 veces por encima del ruido. Su hoja de ruta: 100 qubits lógicos en 2028 y 1.000 en 2030. 🟢 [Infleqtion](https://infleqtion.com/infleqtion-achieves-30-entangled-logical-qubits-on-its-sqale-quantum-computer/)

**Hechos (análisis independiente).** PostQuantum señala que se usa un código de **distancia 2**, que **detecta** errores pero no los **corrige** (para eso hace falta distancia ≥ 3). Además, los resultados dependen de la **post-selección**, es decir, de descartar las ejecuciones fallidas, y la fracción útil cae al crecer el circuito. 🟡 [PostQuantum](https://postquantum.com/industry-news/infleqtion-30-logical-qubits)

**Análisis.** Es un buen ejemplo de por qué conviene leer más allá del comunicado. Para comparar anuncios cuánticos, la pregunta clave es si el código **corrige** errores o solo los **detecta**.

---

## 🎓 Qué hacer con esto (para estudiantes de Robótica e IA)

1. **Probar Intrinsic Core o MoveIt 2** en simulación (Gazebo) y documentar una tarea de *pick-and-place* o de carga de máquinas CNC → pieza de portfolio en ROS 2.
2. **Reproducir una métrica** de un artículo de arXiv cs.RO del digest diario → práctica de lectura crítica y de reproducibilidad.
3. **Seguir el RPO** (encuentro y proximidad) como nicho europeo donde se cruzan visión, control y espacio.

---

<a id="english-version"></a>

# English version: Orbit, open source and scrutiny (Sept 21 – Oct 2, 2026)

> **How to read this issue.** Each story separates **facts** (what the linked sources say) from **analysis** (my reading, labelled). Source type: 🟢 *primary* · 🟡 *specialised media*. Discrepancies between sources are flagged.

## 🚀 Space

**1. Starship reaches orbit for the first time (Flight 14, Sept 28).** Booster 21 and Ship 41 lifted off from Starbase Pad 2 at 8:49 a.m. EDT. The ship reached a ~275 km orbit, deployed 26 Starlink V3 satellites (three of them carrying cameras to inspect the ship's heat-shield tiles) and splashed down in the North Pacific about 3 h 9 min after launch. About 10 h had been planned; the sources reviewed don't say why it came back early. 🟡 [Space.com](https://www.space.com/news/live/spacex-starship-flight-14-live-updates-sept-28-2026-starship-first-orbital-launch-attempt) — *Analysis:* until now every Starship flight was suborbital. Using the payload itself as an inspection tool is a smart, reusable engineering pattern.

**2. Crew-13 sets a US record to the ISS (Oct 1).** The Falcon 9 / Crew Dragon *Grace* crew (Watkins and Delaney of NASA, Kutryk of CSA, Teteryatnikov of Roscosmos) docked **7 h 55 min** after launch, the fastest trip to the station by a US spacecraft. The ISS now has 11 people aboard. 🟡 [Space.com](https://space.com/news/live/spacex-nasa-crew-13-astronauts-launch-to-iss-september-30-2026)

**3. European autonomy: Blackswan Space raises €2.5M (Sept 30).** The Lithuanian startup is building a vision-based rendezvous-and-proximity-operations (RPO) kit. In-orbit testing is planned for Q4 2027, and the kit will support ASTRAL, Europe's first in-space refuelling mission, in 2028. 🟡 [Tech.eu](https://tech.eu/2026/09/30/blackswan-space-raises-eur25m-to-take-autonomous-spacecraft-navigation-into-orbit)

## 🤖 Robotics

**4. Qualcomm acquires PickNik and pledges to keep MoveIt open (Sept 23).** MoveIt 1 and 2 stay under their current licences. MoveIt Pro will be integrated with Dragonwing and Arduino (including the VENTUNO Q board). Deal terms weren't disclosed. 🟡 [The Robot Report](https://www.therobotreport.com/qualcomm-acquires-picknik-robotics-keep-moveit-open-source/) — *Analysis:* Qualcomm now owns everything from the chip and the maker board up to the manipulation software. Whether it keeps the open-source pledge can be checked in the [MoveIt repo](https://github.com/moveit/moveit2).

**5. Intrinsic open-sources *Intrinsic Core* under Apache 2.0 (Sept 22, ROSCon 2026).** The release includes real-time control, FoundationPose pose estimation, motion and grasp planning, Gazebo simulation, camera calibration and ROS drivers, plus a CNC machine-tending reference design. 🟡 [The Robot Report](https://www.therobotreport.com/intrinsic-open-sources-key-parts-platform-easier-development/) · 🟢 [Repo](https://github.com/intrinsic-ai/intrinsic-core)

**6. Boston Dynamics opens a "behavior factory" for Atlas (Sept 21).** The RMAC sits at Hyundai's Metaplant near Savannah and trains Atlas with teleoperation, simulation-based RL and UMI devices. Hyundai's stated plans are 25,000 Atlas units and a US factory building 30,000 robots a year by 2028 (*plans, not yet validated*). 🟡 [The Robot Report](https://www.therobotreport.com/boston-dynamics-opens-metaplant-application-center-train-atlas-humanoid-robots/)

**7. Unitree down 53% from its peak (Sept 9 data).** *Critical note:* the headline says "from IPO debut", but the article's own figures put the drop at **53% from the 1,100-yuan peak** and **39% from the first-day close**. The stock is still well above the 150.80-yuan IPO price. 🟡 [The Robot Report](https://www.therobotreport.com/unitree-shares-down-53-from-ipo-debut/)

## 🧠 AI

**8. Gemini 4 Argon (Sept 30).** Up to 1M output tokens (previously 64K). Google reports DeepSWE v1.1 77.9%, AutomationBench 51.3%, CWE-bench 68% and LVBench 91.7%. Introductory pricing is $2/$10 per million input/output tokens, rising later to $4/$20. The rollout starts with vetted cyber defenders (Fairwind). 🟢 [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) — *Critical note:* some secondary newsletters printed figures that differ from the primary source. All of these numbers are self-reported.

**9. SynthID Bio in *Nature* (Sept 30).** Imperceptible watermarks for AI-designed proteins, applied at both the sequence and the 3D-structure level (via a fine-tuned AlphaFold 3). Watermarked binders matched unwatermarked ones in affinity. Code, in vitro data and weights are released, and the authors acknowledge that robustness to deliberate tampering is still an open problem. 🟢 [Google DeepMind](https://deepmind.google/blog/introducing-synthid-bio/)

**10. FTC opens a probe into OpenAI and Anthropic (Sept 30)** over possible unfair or deceptive practices and consumer harm. 🟡 [ABC News](https://abcnews.com/Politics/ftc-opens-probe-safety-ai-including-anthropic-open/story?id=136896227) — *Transparency note: this issue was drafted with help from an Anthropic model; the facts come only from the linked source.*

## 💻 Computing

**11. Infleqtion's 30 logical qubits, with caveats (Sept 24–27).** The company reports 30 entangled logical qubits on 80 physical neutral-atom qubits. 🟢 [Infleqtion](https://infleqtion.com/infleqtion-achieves-30-entangled-logical-qubits-on-its-sqale-quantum-computer/) An independent analysis notes that the code is distance-2: it **detects** errors but doesn't **correct** them, and the results rely on post-selection. 🟡 [PostQuantum](https://postquantum.com/industry-news/infleqtion-30-logical-qubits)

---

*Fuentes consultadas el 2 oct 2026 · Sources accessed Oct 2, 2026. ¿Has visto un error? Abre un issue · Spotted an error? Open an issue.*
