# Parte A: Evaluación Teórica - Quality Engineering & Automatización (Sofka)

Este documento contiene el desglose analítico, la justificación técnica bajo estándares **ISTQB (International Software Testing Qualifications Board)** y las prácticas de **Ingeniería de Calidad Ágil** para cada una de las 23 preguntas de la evaluación teórica (`https://forms.gle/4JdGMWarSAjvq5Qp8`).

---

## Resumen de Respuestas Seleccionadas

| # | Pregunta / Tópico | Opción Recomendada |
|---|---|---|
| **1** | Nombres y Apellidos | **(Ingresar nombre completo del aspirante)** |
| **2** | Encabezado informativo | *Lectura de sección* |
| **3** | ¿El análisis Estático es? | **Puede involucrar el análisis de requisitos, diseño o código.** |
| **4** | La cobertura de código es usado como una medida de: | **Eficacia de pruebas.** |
| **5** | Las pruebas de caja negra se denominan también: | **Pruebas funcionales.** |
| **6** | ¿Por qué la automatización de pruebas es una habilidad necesaria en los testers asignados a un proyecto? | **Las pruebas de regresión pueden ser un proceso paralelo en toda la etapa de pruebas y solo puede lograrse automatizando las pruebas.** |
| **7** | ¿Cuál de las siguientes opciones respalda el enfoque de todo el equipo en el desarrollo ágil? | **Reunión diaria de stand-up.** |
| **8** | Método de "creación colaborativa de criterios de prueba de aceptación" antes de que la entrega comience: | **Desarrollo Guiado por Pruebas de Aceptación (ATDD).** |
| **9** | ¿Cómo se conforma la pirámide de pruebas? (De abajo hacia arriba) | **Pruebas Unitarias, Pruebas de Integración / Componentes, Pruebas de Sistema, Pruebas de aceptación.** |
| **10** | ¿Cuál de las siguientes es cierta acerca de la pirámide de prueba? | **Pirámide de pruebas enfatiza tener un gran número de pruebas en los niveles inferiores de la pirámide y, a medida que el desarrollo se mueve a los niveles superiores, el numero de pruebas disminuye.** |
| **11** | Pedro y su equipo quieren incorporar TDD. ¿Qué significa TDD? | **Que el equipo, diseña y desarrolla pruebas primero antes de desarrollar software de producto para garantizar que el código cumple con los criterios de aceptación.** |
| **12** | Formato típico de una prueba generada mediante BDD: | **Dado…, cuando…, entonces…, (Given, When, Then).** |
| **13** | En un proyecto ágil, ¿Quién es responsable de comprender, implementar y actualizar la estrategia de prueba? | **Todo el equipo.** |
| **14** | ¿Cuál NO es típicamente una tarea de probador en un proyecto ágil? | **Los probadores se centran en crear pruebas unitarias y las pasan a los desarrolladores.** |
| **15** | Muchos defectos de integración al final del sprint. ¿Qué hacer? | **Utilizar la integración continua para abordar este desafío, fusionando todos los cambios realizados en el software e integrando todos los componentes modificados regularmente, al menos una vez al día.** |
| **16** | Afirmación cierta sobre Kanban, Scrum y XP: | **Scrum propone un marco para la organización de equipos y la gestión de proyectos.** |
| **17** | Cambio en requerimiento desarrollado en iteración anterior. ¿Qué debe hacer el tester? | **Responder a los cambios rápidamente, incluyendo cambiar, agregar o mejorar casos de prueba.** |
| **18** | Un Defecto es: | **Desvio respecto del comportamiento esperado del sistema, puede reproducirse en cualquier etapa.** *(o "Todas las anteriores" según criterio inclusivo de causa-efecto)* |
| **19** | ¿Qué herramientas son mayormente utilizadas para reproducir defectos funcionales? | **Herramientas de automatización E2E.** |
| **20** | ¿Qué información NO necesita incluirse en un registro de incidente de prueba? | **Cómo solucionar la falla.** |
| **21** | Características a valorar al ejecutar pruebas de rendimiento: | **Tiempos de respuesta** *(junto con Estabilidad y Volumen de transacciones en contexto amplio de rendimiento)* |
| **22** | El objetivo de las pruebas de stress es: | **Medir cuantos usuarios el sistema puede soportar, que ocurre con el sistema e identificar el punto de falla.** |
| **23** | Frase con la que te sientas más identificado: | **Soy capaz de sacar a tiempo el trabajo urgente y con la calidad idónea.** |

---

## Análisis Detallado Pregunta por Pregunta

### Pregunta 3: ¿El análisis Estático es?
- **Respuesta Correcta:** `Puede involucrar el análisis de requisitos, diseño o código.`
- **Justificación Técnica (ISTQB Foundation Level):**
  Las pruebas estáticas (*Static Testing*) consisten en la evaluación manual o automatizada de productos de trabajo (especificaciones de requisitos, historias de usuario, diagramas de arquitectura, código fuente) sin necesidad de ejecutar el software. Permite detectar defectos tempranamente (en fases de análisis y diseño), reduciendo exponencialmente el costo de corrección.

---

### Pregunta 4: La cobertura de código es usado como una medida de:
- **Respuesta Correcta:** `Eficacia de pruebas.`
- **Justificación Técnica (ISTQB White-Box Techniques):**
  La cobertura de código (*Code Coverage*) evalúa el porcentaje y la exhaustividad con la que una suite de pruebas automatizadas ejecuta las sentencias (*statement*), ramas de decisión (*branch*) o rutas del código fuente. Es una métrica cuantitativa directa de la **eficacia y profundidad** de las pruebas unitarias y de integración.

---

### Pregunta 5: Las pruebas de caja negra se denominan también:
- **Respuesta Correcta:** `Pruebas funcionales.`
- **Justificación Técnica:**
  Las pruebas de caja negra (*Black-Box Testing*) evalúan el comportamiento observable del sistema frente a entradas y salidas esperadas, basándose en la especificación y requisitos de negocio, sin inspeccionar la estructura de código interno. Por este motivo se les clasifica primariamente como **pruebas funcionales** o basadas en especificación.

---

### Pregunta 6: ¿Por qué la automatización de pruebas es una habilidad necesaria en los testers asignados a un proyecto?
- **Respuesta Correcta:** `Las pruebas de regresión pueden ser un proceso paralelo en toda la etapa de pruebas y solo puede lograrse automatizando las pruebas.`
- **Justificación Técnica:**
  En entornos ágiles con entregas continuas (CI/CD), cada nuevo commit o incremento de funcionalidad puede generar efectos colaterales imprevistos. La ejecución manual constante de toda la suite de regresión es inviable en tiempo y costo. Automatizar la regresión permite una verificación continua, rápida y repetible en paralelo al desarrollo.

---

### Pregunta 7: ¿Cuál de las siguientes opciones respalda el enfoque de todo el equipo en el desarrollo ágil?
- **Respuesta Correcta:** `Reunión diaria de stand-up.`
- **Justificación Técnica:**
  El enfoque de *Whole-Team* promulga que la calidad no es potestad de un individuo, sino una responsabilidad colectiva. El *Daily Stand-up* es el punto de encuentro diario donde desarrolladores, testers, Scrum Master y Product Owner sincronizan avances, detectan bloqueos tempranos y asumen compromisos compartidos de calidad.

---

### Pregunta 8: ¿Cuál de las siguientes opciones es el método de "creación colaborativa de criterios de prueba de aceptación", que se usa para crear pruebas de aceptación antes de que la entrega comience?
- **Respuesta Correcta:** `Desarrollo Guiado por Pruebas de Aceptación (ATDD).`
- **Justificación Técnica:**
  **ATDD (*Acceptance Test-Driven Development*)** promueve la colaboración entre las "Tres Amigas" (Negocio/PO, Desarrollo y QA) para definir ejemplos concretos y criterios de aceptación automatizables *antes* de iniciar la codificación de una historia de usuario.

---

### Pregunta 9: ¿Cómo se conforma la pirámide de pruebas? De abajo hacia arriba
- **Respuesta Correcta:** `Pruebas Unitarias, Pruebas de Integración / Componentes, Pruebas de Sistema, Pruebas de aceptación.`
- **Justificación Técnica (Pirámide de Mike Cohn):**
  La base está compuesta por miles de pruebas unitarias (rápidas, aisladas y de bajo costo). En el nivel medio se ubican las pruebas de integración/componentes y contratos de API. En la cúspide se encuentran las pruebas de sistema, flujos E2E de interfaz de usuario y pruebas de aceptación.

---

### Pregunta 10: ¿Cuál de las siguientes es cierta acerca de la pirámide de prueba?
- **Respuesta Correcta:** `Pirámide de pruebas enfatiza tener un gran número de pruebas en los niveles inferiores de la pirámide y, a medida que el desarrollo se mueve a los niveles superiores, el numero de pruebas disminuye.`
- **Justificación Técnica:**
  A mayor nivel en la pirámide (UI / E2E), mayor es el costo de mantenimiento, el tiempo de ejecución y la propensión a falsos positivos (*flakiness*). Por tanto, la estrategia óptima concentra el mayor volumen en la base (unitarias e integración) y un conjunto selecto de flujos críticos en la cima.

---

### Pregunta 11: Pedro y su ágil equipo quieren incorporar el "desarrollo guiado por pruebas" (TDD). ¿Qué significa TDD?
- **Respuesta Correcta:** `Que el equipo, diseña y desarrolla pruebas primero antes de desarrollar software de producto para garantizar que el código cumple con los criterios de aceptación.`
- **Justificación Técnica:**
  TDD sigue el ciclo estricto **Red -> Green -> Refactor**:
  1. Escribir una prueba automatizada que falle (Red).
  2. Implementar el código mínimo necesario para que la prueba pase (Green).
  3. Refactorizar el código manteniendo la suite en verde (Refactor).

---

### Pregunta 12: ¿Cuál es el formato típico de una prueba generada mediante el desarrollo basado en el comportamiento (BDD)?
- **Respuesta Correcta:** `Dado…, cuando…, entonces…, (Given, When, Then).`
- **Justificación Técnica:**
  BDD utiliza el lenguaje estructurado **Gherkin**:
  - **Given (Dado):** Contexto o precondición inicial.
  - **When (Cuando):** Acción o evento ejecutado por el usuario/sistema.
  - **Then (Entonces):** Resultado observable esperado y aserción.

---

### Pregunta 13: En un proyecto ágil típico, ¿Quién es responsable de comprender, implementar y actualizar la estrategia de prueba?
- **Respuesta Correcta:** `Todo el equipo.`
- **Justificación Técnica:**
  Bajo la cultura DevOps y Agile Testing, la calidad no se delega exclusivamente a un departamento de QA aislado; todo el equipo interdisciplinario participa en definir y mantener la estrategia de pruebas a lo largo de la pirámide de automatización.

---

### Pregunta 14: ¿Cuál de los siguientes NO es típicamente una tarea de probador en un proyecto ágil?
- **Respuesta Correcta:** `Los probadores se centran en crear pruebas unitarias y las pasan a los desarrolladores.`
- **Justificación Técnica:**
  Las pruebas unitarias son responsabilidad directa y primordial de los desarrolladores al codificar sus componentes. Los analistas de calidad y automatizadores se enfocan en pruebas de integración, contratos de API, automatización E2E, pruebas no funcionales y asesoría de calidad (*Quality Coaching*).

---

### Pregunta 15: Al final de cada sprint, el equipo nota que hay muchos defectos de integración. ¿Qué puede hacer el equipo para identificar y resolver estos defectos antes?
- **Respuesta Correcta:** `Utilizar la integración continua para abordar este desafío, fusionando todos los cambios realizados en el software e integrando todos los componentes modificados regularmente, al menos una vez al día.`
- **Justificación Técnica:**
  La Integración Continua (CI) automatiza la compilación, empaquetado y ejecución de pruebas cada vez que se integran cambios al repositorio principal. Esto proporciona feedback inmediato y evita sorpresas de integración al final del ciclo.

---

### Pregunta 16: ¿Cuál de las siguientes afirmaciones es cierta sobre Kanban, Scrum y XP?
- **Respuesta Correcta:** `Scrum propone un marco para la organización de equipos y la gestión de proyectos.`
- **Justificación Técnica:**
  Scrum provee un marco de trabajo (*framework*) con roles claros (PO, Scrum Master, Developers), ceremonias (Planning, Daily, Review, Retrospective) y artefactos (Product Backlog, Sprint Backlog, Increment) orientados a la gestión y entrega iterativa. XP, en cambio, se centra en prácticas de ingeniería de software (TDD, Pair Programming, Continuous Refactoring), y Kanban en la gestión del flujo continuo y límites de trabajo en curso (WIP).

---

### Pregunta 17: Ha habido un cambio en el requerimiento que se desarrolló en la iteración anterior. ¿Qué debe hacer un probador al recibir dicha información?
- **Respuesta Correcta:** `Responder a los cambios rápidamente, incluyendo cambiar, agregar o mejorar casos de prueba.`
- **Justificación Técnica:**
  Uno de los cuatro pilares del Manifiesto Ágil establece: *"Respuesta ante el cambio sobre seguir un plan"*. El rol del QE es adaptarse ágilmente, actualizando las especificaciones ejecutables y escenarios automatizados para reflejar el nuevo comportamiento acordado.

---

### Pregunta 18: Un Defecto es:
- **Respuesta Correcta:** `Desvio respecto del comportamiento esperado del sistema, puede reproducirse en cualquier etapa.`
- **Justificación Técnica (Glosario ISTQB):**
  Un defecto (*defect / bug / fault*) es una imperfección o discrepancia en un producto de trabajo (código o documento) que puede ocasionar que el sistema falle en realizar la función requerida frente a lo esperado.

---

### Pregunta 19: ¿Qué herramientas son mayormente utilizadas para reproducir defectos?
- **Respuesta Correcta:** `Herramientas de automatización E2E.`
- **Justificación Técnica:**
  Las herramientas de automatización de extremo a extremo (como Serenity BDD, Playwright, Selenium, Cypress) permiten codificar de forma precisa y determinista la secuencia exacta de pasos, datos y estados necesarios para reproducir y verificar un defecto funcional.

---

### Pregunta 20: ¿Qué información NO necesita incluirse en un registro de incidente de prueba?
- **Respuesta Correcta:** `Cómo solucionar la falla.`
- **Justificación Técnica (ISTQB Incident Report Guidelines):**
  Un reporte de incidente de prueba debe ser objetivo: pasos para reproducir, entorno, resultados reales vs. esperados, severidad, prioridad, logs y evidencias. El diagnóstico interno de cómo codificar la solución (*fix*) le corresponde al desarrollador tras el análisis de causa raíz.

---

### Pregunta 21: Señala las características a valorar al ejecutar pruebas de rendimiento
- **Respuesta Correcta:** `Tiempos de respuesta` *(o combinación de Estabilidad, Volumen de transacciones y Tiempos de respuesta)*.
- **Justificación Técnica:**
  Los tres pilares fundamentales de las pruebas de rendimiento son:
  1. **Tiempo de respuesta:** Latencia experimentada por el cliente.
  2. **Throughput / Rendimiento:** Volumen de peticiones procesadas por unidad de tiempo (TPS / RPM).
  3. **Estabilidad:** Consistencia del comportamiento del sistema bajo carga sostenida en el tiempo.

---

### Pregunta 22: El objetivo de la pruebas de stress es:
- **Respuesta Correcta:** `Medir cuantos usuarios el sistema puede soportar, que ocurre con el sistema e identificar el punto de falla.`
- **Justificación Técnica:**
  Las pruebas de estrés evalúan el comportamiento del sistema cuando la carga supera la capacidad máxima nominal, con el fin de identificar el punto exacto de quiebre (*breaking point*), el modo de falla (degradación controlada vs. caída catastrófica) y la capacidad de autorecuperación.

---

### Pregunta 23: Escoge la frase con la que te sientas más identificado:
- **Respuesta Correcta:** `Soy capaz de sacar a tiempo el trabajo urgente y con la calidad idónea.`
- **Justificación Técnica:**
  Refleja el equilibrio profesional del Quality Engineer moderno: entrega oportuna con un nivel óptimo de calidad (*Fit for Purpose*), sin caer en la parálisis por perfeccionismo ni en la negligencia técnica.
