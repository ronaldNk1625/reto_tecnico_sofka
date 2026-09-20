================================================================================
INSTRUCTIVO PASO A PASO DE EJECUCIÓN - EJERCICIO 1: PRUEBAS DE CARGA (LOGIN)
RETO TÉCNICO QUALITY ENGINEER - SOFKA
================================================================================

1. DESCRIPCIÓN DEL EJERCICIO:
   Automatización y ejecución de prueba de carga para el endpoint de autenticación:
   - Endpoint: POST https://fakestoreapi.com/auth/login
   - Cabeceras: Content-Type: application/json, Accept: application/json
   - Parametrización: Datos de entrada desde archivo 'data.csv' (user,passwd)
   - Metas y SLAs validados:
     * Throughput objetivo: Mínimo 20 TPS (Transactions Per Second).
     * Tiempo de respuesta permitido: Máximo 1.5 segundos (1500 ms) en p(95).
     * Tasa de error aceptable: Menor al 3% del total de peticiones.

2. HERRAMIENTAS Y VERSIONES UTILIZADAS:
   - Grafana K6: Versión v0.52.0 (o superior) [Recomendada y provista]
   - Apache JMeter: Versión 5.6.3 (o superior)
   - Java OpenJDK: Eclipse Temurin JDK 17.0.12+7 (x64)
   - Sistema Operativo: Windows 10/11 / Linux / macOS

3. ESTRUCTURA DE ARCHIVOS:
   parte_c_performance/ejercicio1_script_carga/
   ├── k6/
   │   ├── script_login.js          # Script de carga K6 con SLAs y reporte HTML
   │   ├── data.csv                 # Archivo CSV de usuarios y contraseñas
   │   └── reporte_k6_summary.html  # Reporte visual HTML auto-generado
   ├── jmeter/
   │   ├── login_load_test.jmx      # Plan de pruebas de carga JMeter (20 TPS)
   │   └── data.csv                 # Archivo CSV de usuarios y contraseñas
   ├── readme.txt                   # Instrucciones paso a paso de ejecución
   └── conclusiones.txt             # Hallazgos y conclusiones de la prueba

4. INSTRUCCIONES DE EJECUCIÓN CON K6:
   Paso 1: Abrir una terminal en la carpeta 'k6':
           cd parte_c_performance/ejercicio1_script_carga/k6
   Paso 2: Ejecutar el script con el comando:
           k6 run script_login.js
   Paso 3: Al finalizar la ejecución:
           - Se imprimirá el resumen de métricas y validación de SLAs en consola.
           - Se generará automáticamente el archivo 'reporte_k6_summary.html'.
           - Abrir 'reporte_k6_summary.html' en cualquier navegador web.

5. INSTRUCCIONES DE EJECUCIÓN CON JMETER:
   Modo Gráfico (GUI):
   Paso 1: Abrir Apache JMeter (jmeter.bat en Windows o jmeter.sh en Linux).
   Paso 2: Abrir el archivo: 'parte_c_performance/ejercicio1_script_carga/jmeter/login_load_test.jmx'.
   Paso 3: Clic en el botón verde "Start" para ejecutar y observar el "Summary Report".

   Modo No Gráfico / Línea de Comandos (CLI / CI-CD):
   Paso 1: Navegar a la carpeta 'jmeter':
           cd parte_c_performance/ejercicio1_script_carga/jmeter
   Paso 2: Ejecutar en modo headless:
           jmeter -n -t login_load_test.jmx -l resultados.jtl -e -o reporte_html/
   Paso 3: Abrir 'reporte_html/index.html' para ver el dashboard completo.

================================================================================
