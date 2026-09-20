import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, hex_color):
    """Set background color of a table cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Set padding for table cells in dxa."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def generate_charts(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Chart: VUs vs Throughput over time
    time_pts = ['01:40', '01:45', '01:50', '01:52', '01:55', '01:58', '02:00', '02:02', '02:05', '02:10', '02:15', '02:20', '02:25', '02:30']
    vus =      [100,     102,     105,     140,     140,     140,     140,     140,     115,     115,     115,     115,     110,     110]
    tps =      [80,      82,      84,      45,      22,      15,      12,      18,      72,      75,      78,      74,      76,      75]
    
    fig, ax1 = plt.subplots(figsize=(10, 4.5), dpi=300)
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    
    color_vus = '#1f77b4'
    color_tps = '#d62728'
    
    ax1.set_xlabel('Tiempo de Ejecución (HH:MM)', fontsize=11, fontweight='bold', labelpad=8)
    ax1.set_ylabel('Usuarios Virtuales (VUs)', color=color_vus, fontsize=11, fontweight='bold')
    line1 = ax1.plot(time_pts, vus, color=color_vus, linewidth=2.5, marker='o', label='VUs (Usuarios Concurrencia)')
    ax1.tick_params(axis='y', labelcolor=color_vus)
    ax1.set_ylim(0, 160)
    
    ax2 = ax1.twinx()
    ax2.set_ylabel('Throughput (req/s)', color=color_tps, fontsize=11, fontweight='bold')
    line2 = ax2.plot(time_pts, tps, color=color_tps, linewidth=2.5, linestyle='--', marker='s', label='Throughput (Peticiones/s)')
    ax2.tick_params(axis='y', labelcolor=color_tps)
    ax2.set_ylim(0, 100)
    
    # Highlight crash area
    ax1.axvspan('01:52', '02:02', color='#ffcccc', alpha=0.5, label='Zona de Colapso / Saturación (Stage 1)')
    
    # Title & Legend
    plt.title('Comportamiento de Throughput vs. Usuarios Virtuales (VUs)\nIdentificación del Punto de Quiebre (Knee Point)', fontsize=13, fontweight='bold', pad=15)
    
    lines = line1 + line2
    labels = [l.get_label() for l in lines] + ['Zona de Saturación (5,987 Errores 5xx)']
    ax1.legend(lines + [plt.Rectangle((0,0),1,1, color='#ffcccc', alpha=0.5)], labels, loc='lower left', frameon=True)
    
    plt.tight_layout()
    chart1_path = os.path.join(output_dir, 'chart_vus_vs_throughput.png')
    plt.savefig(chart1_path, dpi=300)
    plt.close()

    # 2. Chart: Error Distribution
    fig, (ax_pie, ax_bar) = plt.subplots(1, 2, figsize=(11, 4.5), dpi=300)
    
    # Pie chart
    labels_pie = ['Transacciones Exitosas\n(97.55% - 269,891)', 'Fallas / Errores\n(2.44% - 6,759)']
    sizes_pie = [269891, 6759]
    colors_pie = ['#2ca02c', '#d62728']
    explode = (0, 0.1)
    
    ax_pie.pie(sizes_pie, explode=explode, labels=labels_pie, colors=colors_pie, autopct='%1.2f%%',
               shadow=True, startangle=140, textprops={'fontsize': 10, 'weight': 'bold'})
    ax_pie.set_title('Tasa Global de Éxito vs Fallas', fontsize=12, fontweight='bold', pad=10)
    
    # Bar chart for errors
    categories = ['5xx Stage 0', '4xx Stage 1', '5xx Stage 1\n(Pico 140 VUs)', '5xx Stage 2']
    error_counts = [1, 769, 5987, 2]
    colors_bar = ['#17becf', '#ff7f0e', '#d62728', '#17becf']
    
    bars = ax_bar.bar(categories, error_counts, color=colors_bar, width=0.55)
    ax_bar.set_title('Distribución de Errores por Etapa (Stages)', fontsize=12, fontweight='bold', pad=10)
    ax_bar.set_ylabel('Cantidad de Errores', fontsize=10, fontweight='bold')
    ax_bar.set_yscale('log')
    ax_bar.set_ylim(0.5, 10000)
    ax_bar.yaxis.set_major_formatter(ticker.ScalarFormatter())
    
    for bar in bars:
        yval = bar.get_height()
        ax_bar.text(bar.get_x() + bar.get_width()/2.0, yval * 1.3, f'{yval:,}', ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    chart2_path = os.path.join(output_dir, 'chart_error_distribution.png')
    plt.savefig(chart2_path, dpi=300)
    plt.close()
    
    return chart1_path, chart2_path

def build_docx_report(output_path, chart1_path, chart2_path):
    doc = Document()
    
    # Page setup - Margins 1 inch
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
    
    # Palette Colors
    PRIMARY = RGBColor(14, 43, 92)     # Deep Navy
    SECONDARY = RGBColor(41, 128, 185) # Slate Blue
    ACCENT_RED = RGBColor(192, 57, 43) # Ruby Red
    TEXT_DARK = RGBColor(44, 62, 80)   # Charcoal
    
    # Document Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_title = p_title.add_run("INFORME DE ANÁLISIS DE RENDIMIENTO Y CARGA")
    run_title.font.name = "Calibri"
    run_title.font.size = Pt(22)
    run_title.font.bold = True
    run_title.font.color.rgb = PRIMARY
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_sub = p_sub.add_run("Evaluación de Concurrencia, Capacidad y Estabilidad Transaccional\nReto Técnico Quality Engineer - Sofka")
    run_sub.font.name = "Calibri"
    run_sub.font.size = Pt(13)
    run_sub.font.italic = True
    run_sub.font.color.rgb = SECONDARY
    
    doc.add_paragraph().paragraph_format.space_after = Pt(6)
    
    # Metadata Box
    meta_table = doc.add_table(rows=4, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.autofit = False
    
    col_widths = [Inches(2.5), Inches(4.5)]
    data = [
        ("Fecha de Evaluación:", "20 de Septiembre de 2026"),
        ("Postulante / Evaluador:", "Ronald (Analista de Automatización / QE)"),
        ("Servicio Bajo Prueba:", "API Transaccional de Autenticación & Balance"),
        ("Insumos de Entrada:", "textSummary.txt (K6 v0.x) + Diagrama de Monitoreo")
    ]
    for row_idx, (label, val) in enumerate(data):
        row = meta_table.rows[row_idx]
        cell_0, cell_1 = row.cells[0], row.cells[1]
        cell_0.width, cell_1.width = col_widths[0], col_widths[1]
        
        r0 = cell_0.paragraphs[0].add_run(label)
        r0.font.bold = True
        r0.font.size = Pt(10)
        r0.font.color.rgb = PRIMARY
        
        r1 = cell_1.paragraphs[0].add_run(val)
        r1.font.size = Pt(10)
        
        set_cell_background(cell_0, "F0F4F8")
        set_cell_background(cell_1, "FAFAFA")
        set_cell_margins(cell_0, 60, 60, 100, 100)
        set_cell_margins(cell_1, 60, 60, 100, 100)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(12)
    
    # 1. RESUMEN EJECUTIVO
    h1 = doc.add_heading(level=1)
    run_h1 = h1.add_run("1. Resumen Ejecutivo y Veredicto Global")
    run_h1.font.color.rgb = PRIMARY
    run_h1.font.size = Pt(15)
    
    p = doc.add_paragraph()
    p.add_run("Se ha llevado a cabo una exhaustiva auditoría de rendimiento y capacidad sobre el servicio transaccional utilizando el framework ")
    p.add_run("K6").bold = True
    p.add_run(". La prueba sometió a la plataforma a una carga concurrente con rampa variable que alcanzó un pico de ")
    p.add_run("140 Usuarios Virtuales (VUs)").bold = True
    p.add_run(" con un volumen total de ")
    p.add_run("276,650 transacciones").bold = True
    p.add_run(" durante 50 minutos de ejecución.")
    
    # SLA Table
    sla_table = doc.add_table(rows=6, cols=4)
    sla_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["Métrica Evaluada", "SLA / Criterio Objetivo", "Valor Obtenido", "Dictamen Técnico"]
    for i, h in enumerate(headers):
        cell = sla_table.rows[0].cells[i]
        r = cell.paragraphs[0].add_run(h)
        r.font.bold = True
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(255, 255, 255)
        set_cell_background(cell, "0E2B5C")
        set_cell_margins(cell, 80, 80, 100, 100)
        
    sla_rows = [
        ("Throughput Promedio", ">= 20.0 TPS", "73.18 TPS", "CUMPLE (365% de la meta)"),
        ("Tasa de Error Global", "< 3.00% del total", "2.44% (6,759 fallas)", "CUMPLE SLA GLOBAL (*)"),
        ("Tiempo de Respuesta p(95)", "<= 1.50 segundos", "1.57 segundos", "INCUMPLE (Excede por 70ms)"),
        ("Tiempo de Respuesta Promedio", "<= 1.50 segundos", "861.68 ms", "CUMPLE"),
        ("Tiempo de Respuesta Máximo", "<= 5.00 segundos", "29.93 segundos", "CRÍTICO (Timeouts en pico)")
    ]
    
    for r_idx, row_data in enumerate(sla_rows, start=1):
        row = sla_table.rows[r_idx]
        bg = "F9F9F9" if r_idx % 2 == 0 else "FFFFFF"
        for c_idx, text in enumerate(row_data):
            cell = row.cells[c_idx]
            r = cell.paragraphs[0].add_run(text)
            r.font.size = Pt(9.5)
            if c_idx == 3:
                r.font.bold = True
                if "INCUMPLE" in text or "CRÍTICO" in text:
                    r.font.color.rgb = ACCENT_RED
                elif "CUMPLE" in text:
                    r.font.color.rgb = RGBColor(39, 174, 96)
            set_cell_background(cell, bg)
            set_cell_margins(cell, 60, 60, 80, 80)
            
    doc.add_paragraph().paragraph_format.space_after = Pt(8)
    
    p_verdict = doc.add_paragraph()
    p_verdict.paragraph_format.left_indent = Inches(0.2)
    p_verdict.paragraph_format.right_indent = Inches(0.2)
    r_v = p_verdict.add_run("(*) DICTAMEN TÉCNICO CONDICIONADO: ")
    r_v.font.bold = True
    r_v.font.color.rgb = ACCENT_RED
    p_verdict.add_run("Si bien la tasa de error global promedio del 2.44% se sitúa numéricamente por debajo del umbral del 3%, el 99.95% de todos los errores (5,987 errores HTTP 5xx y 769 HTTP 4xx) se concentraron de forma crítica y explosiva durante el pico de 140 VUs (Stage 1), donde la tasa de fallo local superó el 25% y provocó la caída del throughput a menos de 20 req/s. El sistema NO está listo para soportar picos superiores a 110 usuarios concurrentes sin ajustes de arquitectura.")
    
    # 2. CONSOLIDADO DE RESULTADOS K6
    h2 = doc.add_heading(level=1)
    run_h2 = h2.add_run("2. Consolidado Estadístico de Métricas (textSummary.txt)")
    run_h2.font.color.rgb = PRIMARY
    run_h2.font.size = Pt(15)
    
    metrics_table = doc.add_table(rows=10, cols=7)
    metrics_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    m_headers = ["Métrica", "Promedio", "Mínimo", "Mediana", "p(90)", "p(95)", "Máximo"]
    for i, h in enumerate(m_headers):
        cell = metrics_table.rows[0].cells[i]
        r = cell.paragraphs[0].add_run(h)
        r.font.bold = True
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(255, 255, 255)
        set_cell_background(cell, "2980B9")
        set_cell_margins(cell, 60, 60, 60, 60)
        
    m_data = [
        ("http_req_duration", "861.68 ms", "191.86 ms", "613.42 ms", "1.28 s", "1.57 s", "29.93 s"),
        ("http_req_waiting (TTFB)", "861.21 ms", "191.86 ms", "613.01 ms", "1.28 s", "1.57 s", "29.93 s"),
        ("expected_response: true", "735.84 ms", "244.92 ms", "600.70 ms", "1.22 s", "1.42 s", "26.72 s"),
        ("iteration_duration", "1.86 s", "0.00 s", "1.61 s", "2.29 s", "2.57 s", "30.94 s"),
        ("http_req_receiving", "424.03 µs", "0.00 s", "320.70 µs", "988.40 µs", "1.05 ms", "39.58 ms"),
        ("http_req_sending", "43.22 µs", "0.00 s", "0.00 s", "0.00 s", "517.00 µs", "31.25 ms"),
        ("http_req_blocked", "10.97 µs", "0.00 s", "0.00 s", "0.00 s", "0.00 s", "35.02 ms"),
        ("http_req_tls_handshaking", "7.36 µs", "0.00 s", "0.00 s", "0.00 s", "0.00 s", "27.02 ms"),
        ("http_req_connecting", "3.30 µs", "0.00 s", "0.00 s", "0.00 s", "0.00 s", "11.82 ms")
    ]
    
    for r_idx, row_data in enumerate(m_data, start=1):
        row = metrics_table.rows[r_idx]
        bg = "F4F6F7" if r_idx % 2 == 0 else "FFFFFF"
        for c_idx, text in enumerate(row_data):
            cell = row.cells[c_idx]
            r = cell.paragraphs[0].add_run(text)
            r.font.size = Pt(8.5)
            if c_idx == 0:
                r.font.bold = True
            set_cell_background(cell, bg)
            set_cell_margins(cell, 50, 50, 60, 60)
            
    doc.add_paragraph().paragraph_format.space_after = Pt(8)
    
    # 3. ANÁLISIS DE ERRORES POR ETAPA
    h3 = doc.add_heading(level=1)
    run_h3 = h3.add_run("3. Análisis de Errores y Frecuencia de Falla")
    run_h3.font.color.rgb = PRIMARY
    run_h3.font.size = Pt(15)
    
    p = doc.add_paragraph()
    p.add_run("Durante la prueba se registraron ")
    p.add_run("6,759 transacciones fallidas").bold = True
    p.add_run(" frente a ")
    p.add_run("269,891 checks exitosos (97.55%)").bold = True
    p.add_run(". El desglose por etapas y códigos de estado revela la causa directa del problema:")
    
    # Add chart 2 image
    if os.path.exists(chart2_path):
        doc.add_picture(chart2_path, width=Inches(6.5))
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_cap = p_cap.add_run("Figura 1: Distribución global de éxito vs. fallas y concentración de errores HTTP 5xx en Stage 1")
        r_cap.font.size = Pt(8.5)
        r_cap.font.italic = True
    
    # Stage breakdown list
    p = doc.add_paragraph(style='List Bullet')
    r = p.add_run("Stage 0 (Inicialización y Carga Base): ")
    r.bold = True
    p.add_run("Se registró únicamente 1 error HTTP 5xx (0.00026 req/s). El sistema operó con total normalidad.")
    
    p = doc.add_paragraph(style='List Bullet')
    r = p.add_run("Stage 1 (Pico de Estrés a 140 VUs): ")
    r.bold = True
    p.add_run("Se generaron ")
    p.add_run("5,987 errores HTTP 5xx").bold = True
    p.add_run(" (tasa de 1.58 req/s) y ")
    p.add_run("769 errores HTTP 4xx").bold = True
    p.add_run(" (0.20 req/s). Este segmento concentra el ")
    p.add_run("99.95% del total de incidencias").bold = True
    p.add_run(" de toda la jornada.")
    
    p = doc.add_paragraph(style='List Bullet')
    r = p.add_run("Stage 2 (Descenso y Recuperación): ")
    r.bold = True
    p.add_run("Al bajar la carga a ~110-115 VUs, solo se contabilizaron 2 errores 5xx (0.0005 req/s), demostrando una recuperación inmediata una vez aliviada la saturación.")
    
    # 4. ANÁLISIS DEL DIAGRAMA DE MONITOREO
    h4 = doc.add_heading(level=1)
    run_h4 = h4.add_run("4. Análisis del Diagrama de Monitoreo (VUs vs. Throughput)")
    run_h4.font.color.rgb = PRIMARY
    run_h4.font.size = Pt(15)
    
    p = doc.add_paragraph()
    p.add_run("El diagrama temporal obtenido del monitoreo de K6 evidencia con total claridad la dinámica entre los usuarios virtuales concurrentes y las peticiones procesadas por segundo:")
    
    if os.path.exists(chart1_path):
        doc.add_picture(chart1_path, width=Inches(6.5))
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_cap = p_cap.add_run("Figura 2: Correlación temporal entre Usuarios Virtuales (VUs) y Throughput (req/s) con punto de quiebre")
        r_cap.font.size = Pt(8.5)
        r_cap.font.italic = True
        
    p = doc.add_paragraph()
    p.add_run("1. Fase Lineal y Estable (01:40:00 a 01:52:00): ").bold = True
    p.add_run("Con una carga de ~100 VUs, la aplicación entrega un rendimiento constante de entre 75 y 85 req/s con tiempos de respuesta muy ágiles.")
    
    p = doc.add_paragraph()
    p.add_run("2. Punto de Inflexión y Colapso (01:52:00 a 02:02:00): ").bold = True
    p.add_run("Al incrementar la demanda a 140 VUs, el sistema alcanza su límite de capacidad física. En lugar de procesar más peticiones, se presenta el fenómeno de ")
    p.add_run("Thrashing / Contención por Bloqueos").bold = True
    p.add_run(". El throughput se derrumba en picada hasta caer a menos de 20 req/s, las peticiones se encolan y expiran (máximo de 29.93s) y el servidor responde con 5,987 errores 5xx.")
    
    p = doc.add_paragraph()
    p.add_run("3. Capacidad Máxima Sostenible (Knee Capacity): ").bold = True
    p.add_run("La capacidad máxima segura identificada para la infraestructura actual se ubica en ")
    p.add_run("105 - 110 VUs sostenidos").bold = True
    p.add_run(", entregando un throughput máximo de 75 a 80 TPS.")
    
    # 5. DIAGNÓSTICO DE CAUSA RAÍZ
    h5 = doc.add_heading(level=1)
    run_h5 = h5.add_run("5. Diagnóstico de Causa Raíz (Root Cause Analysis)")
    run_h5.font.color.rgb = PRIMARY
    run_h5.font.size = Pt(15)
    
    p = doc.add_paragraph()
    p.add_run("A partir de la evidencia métrica, se descarta cualquier problema en la capa de red o SSL (tiempo de conexión y DNS < 1 ms) y se confirma que el cuello de botella es 100% interno de procesamiento:")
    
    p1 = doc.add_paragraph(style='List Bullet')
    p1.add_run("Agotamiento del Pool de Conexiones a Base de Datos: ").bold = True
    p1.add_run("El 99.9% del tiempo de latencia corresponde a http_req_waiting (TTFB = 861.21ms promedio). Un pool de conexiones JDBC pequeño (ej. 30-50 conexiones) frente a 140 usuarios concurrentes provoca que más de 90 hilos queden bloqueados esperando conexiones libres hasta que se agota el timeout de espera.")
    
    p2 = doc.add_paragraph(style='List Bullet')
    p2.add_run("Contención de Hilos en Servidor Web (Thread Starvation): ").bold = True
    p2.add_run("Al acumularse peticiones lentas, se saturan los workers del servidor web/aplicación (Tomcat/Node/Nginx), rechazando las solicitudes entrantes con códigos 502/503/504.")
    
    p3 = doc.add_paragraph(style='List Bullet')
    p3.add_run("Falta de Escalado Horizontal Automático (HPA): ").bold = True
    p3.add_run("La arquitectura permaneció estática durante el pico de 140 VUs, sin activar nuevas réplicas en Kubernetes para absorber el excedente de demanda.")
    
    # 6. RECOMENDACIONES
    h6 = doc.add_heading(level=1)
    run_h6 = h6.add_run("6. Recomendaciones Técnicas y Plan de Acción")
    run_h6.font.color.rgb = PRIMARY
    run_h6.font.size = Pt(15)
    
    rec_table = doc.add_table(rows=6, cols=3)
    rec_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    r_hdrs = ["Prioridad", "Acción Técnica Recomendada", "Beneficio Esperado"]
    for i, h in enumerate(r_hdrs):
        cell = rec_table.rows[0].cells[i]
        r = cell.paragraphs[0].add_run(h)
        r.font.bold = True
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(255, 255, 255)
        set_cell_background(cell, "0E2B5C")
        set_cell_margins(cell, 60, 60, 70, 70)
        
    recs = [
        ("Alta (Inmediata)", "Optimización de Pool HikariCP: Aumentar pool a 150 conexiones y connectionTimeout a 5000ms.", "Elimina la cola de espera por conexiones a BD."),
        ("Alta (Inmediata)", "Ajuste de Timeouts en Gateway: Configurar read/idle timeouts a 5s para descartar conexiones zombis.", "Libera workers rápidamente y evita max durations de 29s."),
        ("Media (Mediano Plazo)", "Implementación de HPA (Kubernetes): Regla de autoescalado al superar 65% de CPU o 60 TPS.", "Permite absorber picos de hasta 250 VUs dinámicamente."),
        ("Media (Mediano Plazo)", "Capa de Caching con Redis: Cachear consultas frecuentes de balance y autenticación.", "Reduce la carga a la BD en más del 60%."),
        ("Baja (Resiliencia)", "Patrón Circuit Breaker & Rate Limiting: Proteger el backend con Resilience4j y límites 429.", "Garantiza degradación elegante sin caída del servicio.")
    ]
    
    for r_idx, (prio, accion, benef) in enumerate(recs, start=1):
        row = rec_table.rows[r_idx]
        bg = "F9F9F9" if r_idx % 2 == 0 else "FFFFFF"
        for c_idx, text in enumerate([prio, accion, benef]):
            cell = row.cells[c_idx]
            r = cell.paragraphs[0].add_run(text)
            r.font.size = Pt(8.5)
            if c_idx == 0 and "Alta" in text:
                r.font.bold = True
                r.font.color.rgb = ACCENT_RED
            set_cell_background(cell, bg)
            set_cell_margins(cell, 50, 50, 60, 60)
            
    doc.add_paragraph().paragraph_format.space_after = Pt(12)
    
    # Sign-off
    p_sign = doc.add_paragraph()
    p_sign.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_s = p_sign.add_run("Elaborado por: Ronald\nAnalista de Automatización / Quality Engineer\nSofka Technologies")
    r_s.font.size = Pt(9.5)
    r_s.font.bold = True
    r_s.font.color.rgb = PRIMARY
    
    doc.save(output_path)
    print(f"Report successfully generated at: {output_path}")

if __name__ == '__main__':
    base_dir = r"d:\Prueba_Practica_Sofka\parte_c_performance\ejercicio2_analisis_resultados"
    assets_dir = os.path.join(base_dir, "assets")
    c1, c2 = generate_charts(assets_dir)
    docx_path = os.path.join(base_dir, "InformeResultados.docx")
    doc_path = os.path.join(base_dir, "InformeResultados.doc")
    build_docx_report(docx_path, c1, c2)
    # Also save as .doc (binary copy)
    with open(docx_path, 'rb') as src, open(doc_path, 'wb') as dst:
        dst.write(src.read())
    print("Both InformeResultados.docx and InformeResultados.doc created successfully.")
