# Reto Técnico Quality Engineer / Analista de Automatización - Sofka

¡Bienvenido al repositorio con la resolución completa del **Reto Técnico de Calidad de Software y Automatización** para **Sofka Technologies**, desarrollado por **Ronald**.

Este repositorio contiene la solución integral a las tres dimensiones evaluadas:

⚙️ **Parte B: Automatización de Flujos Funcionales**

- **Ejercicio 1:** Automatización E2E Frontend en [Demoblaze](https://www.demoblaze.com/) con **Serenity BDD + Cucumber (Screenplay Pattern)**.
- **Ejercicio 2:** Automatización de Servicios REST en [Swagger Petstore](https://petstore.swagger.io/) con **Karate DSL**.
  📊 **Parte C: Análisis y Pruebas de Rendimiento**
- **Ejercicio 1:** Script de Pruebas de Carga en [FakeStore Login](https://fakestoreapi.com/auth/login) parametrizado con CSV (>= 20 TPS, p95 <= 1.5s, Error < 3%) con **K6** y **Apache JMeter**.
- **Ejercicio 2:** **Informe Técnico y Ejecutivo de Rendimiento (`InformeResultados.doc` / `InformeResultados.docx`)** con análisis de saturación, fallas 5xx y diagrama de monitoreo (VUs vs. Throughput).

---

## 📁 Estructura del Repositorio

```
d:/Prueba_Practica_Sofka/

├── parte_b_automatizacion/                             # Parte B: Automatización Funcional
│   ├── ejercicio1_serenity_demoblaze/                 # Ejercicio 1: E2E Frontend Demoblaze
│   │   ├── pom.xml                                    # Dependencias Serenity BDD 4.x + Cucumber 7.x
│   │   ├── src/main/java/com/sofka/demoblaze/
│   │   │   ├── models/                                # Modelos (Cliente)
│   │   │   ├── userinterfaces/                        # Targets (HomePage, ProductDetailPage, CartPage, etc.)
│   │   │   ├── tasks/                                 # Tasks Screenplay (AgregarProducto, NavegarAlCarrito, etc.)
│   │   │   ├── interactions/                          # Interactions (AceptarAlerta)
│   │   │   └── questions/                             # Questions (ElMensajeDeConfirmacion, LosDetallesDeLaOrden)
│   │   ├── src/test/java/com/sofka/demoblaze/
│   │   │   ├── stepdefinitions/                       # Step Definitions y Hooks
│   │   │   └── runners/                               # CompraDemoblazeRunner
│   │   ├── src/test/resources/
│   │   │   ├── features/compra_demoblaze.feature      # Escenario BDD Gherkin en español
│   │   │   └── serenity.conf                          # Configuración WebDriver y Chrome Headless
│   │   ├── readme.txt                                 # Instrucciones de ejecución paso a paso
│   │   └── conclusiones.txt                           # Hallazgos y conclusiones de Demoblaze
│   │
│   └── ejercicio2_karate_petstore/                    # Ejercicio 2: API REST Swagger PetStore
│       ├── pom.xml                                    # Dependencias Karate DSL 1.4.1
│       ├── src/test/java/
│       │   ├── karate-config.js                       # Configuración global y timeouts
│       │   └── petstore/
│       │       ├── petstore.feature                   # 5 Escenarios (POST, GET id, PUT, GET status, E2E)
│       │       ├── PetStoreTest.java                  # Runner JUnit 5
│       │       └── PetStoreRunner.java                # Runner secundario
│       ├── target/karate-reports/                     # Reportes interactivos HTML de Karate
│       ├── readme.txt                                 # Instrucciones de ejecución paso a paso
│       └── conclusiones.txt                           # Hallazgos y conclusiones de la API
│
├── parte_c_performance/                                # Parte C: Rendimiento y Análisis
│   ├── ejercicio1_script_carga/                       # Ejercicio 1: Scripts de Carga
│   │   ├── k6/
│   │   │   ├── script_login.js                        # Script K6 con SLAs (20 TPS, p95 <= 1.5s, err < 3%)
│   │   │   ├── data.csv                               # Credenciales parametrizadas
│   │   │   └── reporte_k6_summary.html                # Reporte visual HTML auto-generado
│   │   ├── jmeter/
│   │   │   ├── login_load_test.jmx                    # Plan de pruebas JMeter (20 TPS / 1200 TPM)
│   │   │   └── data.csv                               # Credenciales parametrizadas
│   │   ├── readme.txt                                 # Instrucciones de ejecución K6 y JMeter
│   │   └── conclusiones.txt                           # Hallazgos de la prueba de carga
│   │
│   └── ejercicio2_analisis_resultados/                # Ejercicio 2: Análisis de Resultados
│       ├── InformeResultados.doc                      # Entregable requerido en formato Word (.doc)
│       ├── InformeResultados.docx                     # Entregable en formato Word moderno (.docx)
│       ├── InformeResultados.md                       # Versión Markdown completa para GitHub
│       ├── generar_informe_word.py                    # Script automatizado con gráficos generados
│       └── assets/                                    # Gráficos y diagramas de monitoreo generados
│
└── README.md                                          # Este documento
```

---

## 🚀 Instrucciones Generales de Ejecución

### Prerrequisitos

- **Java JDK:** OpenJDK 17 o superior.
- **Apache Maven:** 3.8 o superior.
- **Node.js / Python 3:** Para utilitarios y reportería.
- **K6:** v0.50+ (o Apache JMeter 5.6+).

---

### 1. Ejecución de Pruebas de API REST (Karate DSL - PetStore)

```bash
cd parte_b_automatizacion/ejercicio2_karate_petstore
mvn clean test
```

_Reporte visual generado en:_ `target/karate-reports/karate-summary.html`

---

### 2. Ejecución de Pruebas E2E (Serenity BDD - Demoblaze)

```bash
cd parte_b_automatizacion/ejercicio1_serenity_demoblaze
mvn clean verify
```

_Reporte visual generado en:_ `target/site/serenity/index.html`

---

### 3. Ejecución de Pruebas de Carga (K6 - Login FakeStore)

```bash
cd parte_c_performance/ejercicio1_script_carga/k6
k6 run script_login.js
```

_Reporte visual generado en:_ `parte_c_performance/ejercicio1_script_carga/k6/reporte_k6_summary.html`

---

### 4. Consulta del Informe de Rendimiento (Análisis de Resultados)

- **Documento Word (.doc / .docx):** `parte_c_performance/ejercicio2_analisis_resultados/InformeResultados.doc`
- **Documento Markdown:** `parte_c_performance/ejercicio2_analisis_resultados/InformeResultados.md`

---

## Checklist de Entrega para Sofka ✅

- [x] **Parte A:** Formulario de Google completado y respaldado en `parte_a_teoria/Respuestas_Evaluacion_Teorica.md`.
- [x] **Parte B - Ejercicio 1:** Proyecto Serenity BDD con Screenplay Pattern + `readme.txt` + `conclusiones.txt`.
- [x] **Parte B - Ejercicio 2:** Proyecto Karate DSL para Swagger PetStore + `readme.txt` + `conclusiones.txt`.
- [x] **Parte C - Ejercicio 1:** Scripts de Carga K6 & JMeter parametrizados con `data.csv` + `readme.txt` + `conclusiones.txt`.
- [x] **Parte C - Ejercicio 2:** `InformeResultados.doc` y `InformeResultados.docx` con análisis de saturación a 140 VUs, diagnóstico de causas raíz y recomendaciones.
- [x] **Repositorio Público:** Código fuente versionado y listo para ser compartido.
