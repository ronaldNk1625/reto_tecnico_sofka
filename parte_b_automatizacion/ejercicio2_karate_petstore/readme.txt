================================================================================
INSTRUCTIVO PASO A PASO DE EJECUCIÓN - EJERCICIO 2: AUTOMATIZACIÓN API (KARATE DSL)
RETO TÉCNICO QUALITY ENGINEER - SOFKA
================================================================================

1. DESCRIPCIÓN DEL PROYECTO:
   Automatización de pruebas de servicios REST sobre la API de PetStore (Swagger):
   - Documentación: https://petstore.swagger.io/
   - Base URL: https://petstore.swagger.io/v2
   - Casos automatizados:
     1. Añadir una mascota a la tienda (POST /pet)
     2. Consultar la mascota ingresada previamente por su ID (GET /pet/{id})
     3. Actualizar el nombre de la mascota y el estatus a "sold" (PUT /pet)
     4. Consultar las mascotas modificadas por estatus (GET /pet/findByStatus?status=sold)
     5. Flujo E2E integrado del ciclo de vida completo.

2. HERRAMIENTAS Y VERSIONES:
   - Framework: Karate DSL 1.4.1 (io.karate:karate-junit5)
   - Lenguaje / JDK: Java OpenJDK 17 (Eclipse Temurin 17.0.12)
   - Gestor de Dependencias: Apache Maven 3.9.6
   - Motor de Pruebas: JUnit 5 (Jupiter 5.10.2)
   - Formato BDD: Gherkin / Karate Native DSL

3. ESTRUCTURA DEL PROYECTO:
   ejercicio2_karate_petstore/
   ├── pom.xml                               # Dependencias Maven y configuración del build
   ├── src/test/java/
   │   ├── karate-config.js                  # Configuración global, timeouts y ambientes
   │   └── petstore/
   │       ├── petstore.feature              # Escenarios BDD con validaciones y JSON Matchers
   │       └── PetStoreRunner.java           # Runner JUnit 5 para ejecución
   ├── target/karate-reports/                # Reportes visuales HTML generados por Karate
   │   └── karate-summary.html               # Dashboard principal interactivo
   ├── readme.txt                            # Instrucciones paso a paso
   └── conclusiones.txt                      # Hallazgos y conclusiones de las pruebas de API

4. INSTRUCCIONES DE EJECUCIÓN:

   Opción A: Ejecución desde Línea de Comandos (Maven)
   --------------------------------------------------
   Paso 1: Abrir una terminal en el directorio del ejercicio:
           cd parte_b_automatizacion/ejercicio2_karate_petstore
   Paso 2: Ejecutar todos los escenarios con Maven:
           mvn test
   Paso 3: Para ejecutar un tag específico (ejemplo @CrearMascota o @FlujoCompletoE2E):
           mvn test -Dkarate.options="--tags @FlujoCompletoE2E"

   Opción B: Ejecución desde IntelliJ IDEA / Eclipse / VS Code
   ----------------------------------------------------------
   Paso 1: Abrir la carpeta del proyecto como proyecto Maven.
   Paso 2: Localizar la clase 'PetStoreRunner.java' en 'src/test/java/petstore/'.
   Paso 3: Clic derecho -> 'Run PetStoreRunner'.

5. VISUALIZACIÓN DE REPORTES:
   Al finalizar la ejecución, Karate genera un reporte HTML interactivo completo en:
   target/karate-reports/karate-summary.html
   
   Para abrirlo en el navegador:
   - En Windows: start target/karate-reports/karate-summary.html
   - O abrir directamente el archivo en Chrome/Edge/Firefox.

================================================================================
