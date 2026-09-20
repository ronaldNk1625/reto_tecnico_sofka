================================================================================
INSTRUCTIVO PASO A PASO DE EJECUCIÓN - EJERCICIO 1: AUTOMATIZACIÓN E2E (SERENITY BDD)
RETO TÉCNICO QUALITY ENGINEER - SOFKA
================================================================================

1. DESCRIPCIÓN DEL PROYECTO:
   Automatización funcional de prueba E2E (End-to-End) del flujo de compra en la tienda
   virtual Demoblaze (https://www.demoblaze.com/) implementando el patrón de diseño
   Screenplay Pattern sobre Serenity BDD con Cucumber en lenguaje Java.

   Flujo de Negocio Automatizado:
   - Navegación a la página principal de Demoblaze.
   - Selección y adición de dos productos al carrito de compras (Samsung galaxy s6 y Nokia lumia 1520).
   - Manejo automático de alertas JavaScript de confirmación ("Product added.").
   - Visualización y verificación del carrito de compras (productos y monto).
   - Diligenciamiento completo del formulario de orden de pedido ("Place Order").
   - Finalización de compra ("Purchase") y validación del mensaje "Thank you for your purchase!" y del ID de transacción.

2. ARQUITECTURA Y PATRÓN SCREENPLAY:
   El proyecto sigue la arquitectura estándar de Screenplay Pattern:
   - Actor: 'Ronald' (entidad que interactúa con el sistema).
   - Abilities: BrowseTheWeb (capacidad de interactuar con el navegador web).
   - UserInterfaces / Targets: Localizadores limpios desacoplados de la lógica.
   - Tasks: Tareas de alto nivel de negocio (AbrirPagina, AgregarProductoAlCarrito, NavegarAlCarrito, CompletarFormularioCompra, FinalizarCompra).
   - Interactions: Acciones atómicas de bajo nivel (AceptarAlerta).
   - Questions: Consultas sobre el estado del sistema para aserciones (ElMensajeDeConfirmacion, LosDetallesDeLaOrden).

3. HERRAMIENTAS Y VERSIONES:
   - Framework de Automatización: Serenity BDD 4.1.20
   - Motor BDD: Cucumber 7.x (serenity-cucumber 4.1.20)
   - Lenguaje y JDK: Java OpenJDK 17 (Eclipse Temurin 17.0.12)
   - Gestor de Dependencias: Apache Maven 3.9.6
   - Navegador: Google Chrome (Headless / Normal vía WebDriverManager)

4. ESTRUCTURA DE ARCHIVOS:
   ejercicio1_serenity_demoblaze/
   ├── pom.xml                                     # Dependencias y plugin de Serenity
   ├── src/main/java/com/sofka/demoblaze/
   │   ├── models/Cliente.java                     # POJO con datos del cliente
   │   ├── userinterfaces/                         # Targets y localizadores
   │   ├── tasks/                                  # Tareas de negocio Screenplay
   │   ├── interactions/AceptarAlerta.java         # Interacción de alerta del browser
   │   └── questions/                              # Questions para validaciones
   ├── src/test/java/com/sofka/demoblaze/
   │   ├── stepdefinitions/                        # Step Definitions de Cucumber
   │   └── runners/CompraDemoblazeRunner.java      # Runner JUnit de Serenity
   ├── src/test/resources/
   │   ├── features/compra_demoblaze.feature       # Escenario BDD en español
   │   └── serenity.conf                           # Configuración de WebDriver y Chrome
   ├── target/site/serenity/                       # Reportes generados (Living Documentation)
   ├── readme.txt                                  # Instrucciones de ejecución
   └── conclusiones.txt                            # Hallazgos y conclusiones

5. INSTRUCCIONES DE EJECUCIÓN:

   Opción A: Ejecución desde Línea de Comandos (Maven)
   --------------------------------------------------
   Paso 1: Abrir una terminal en el directorio del ejercicio:
           cd parte_b_automatizacion/ejercicio1_serenity_demoblaze
   Paso 2: Ejecutar las pruebas y generar el reporte agregado con el comando:
           mvn clean verify
   Paso 3: Para forzar la agregación del reporte visual de Serenity en cualquier momento:
           mvn serenity:aggregate

   Opción B: Ejecución desde IDE (IntelliJ IDEA / Eclipse / VS Code)
   ----------------------------------------------------------------
   Paso 1: Abrir la carpeta 'ejercicio1_serenity_demoblaze' como proyecto Maven.
   Paso 2: Navegar a 'src/test/java/com/sofka/demoblaze/runners/CompraDemoblazeRunner.java'.
   Paso 3: Clic derecho sobre la clase y seleccionar "Run 'CompraDemoblazeRunner'".

6. VISUALIZACIÓN DE REPORTES SERENITY BDD:
   Una vez finalizada la ejecución, Serenity genera el reporte interactivo (Living Documentation)
   en la siguiente ruta:
   target/site/serenity/index.html

   Para abrirlo:
   - En Windows: start target/site/serenity/index.html
   - O abrir 'target/site/serenity/index.html' en cualquier navegador.

================================================================================
