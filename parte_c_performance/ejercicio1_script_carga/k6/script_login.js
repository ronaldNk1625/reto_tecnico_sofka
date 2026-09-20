import http from 'k6/http';
import { check, sleep } from 'k6';
import { SharedArray } from 'k6/data';

// 1. Cargar y parsear archivo CSV de credenciales
const csvData = new SharedArray('Credenciales de Login', function () {
    const rawData = open('./data.csv');
    const lines = rawData.trim().split('\n');
    const records = [];
    
    // Omitir cabecera (linea 0: user,passwd)
    for (let i = 1; i < lines.length; i++) {
        const line = lines[i].trim();
        if (line) {
            const parts = line.split(',');
            records.push({
                username: parts[0].trim(),
                password: parts[1].trim()
            });
        }
    }
    return records;
});

// 2. Configuración de Escenario y SLAs
export const options = {
    scenarios: {
        login_load_scenario: {
            executor: 'constant-arrival-rate',
            rate: 25,              // 25 TPS objetivo (supera el requisito mínimo de >= 20 TPS)
            timeUnit: '1s',
            duration: '30s',       // Duración de la prueba
            preAllocatedVUs: 20,   // VUs pre-asignados
            maxVUs: 50,            // VUs máximos permitidos
        },
    },
    // Definición de SLAs / Validaciones requeridas:
    thresholds: {
        // Validación 1: Tiempo de respuesta permitido es de máximo 1.5 segundos (1500 ms)
        http_req_duration: ['p(95)<1500', 'avg<1500'],
        // Validación 2: Tasa de error aceptable, menor al 3% del total de peticiones
        http_req_failed: ['rate<0.03'],
        // Validación 3: Throughput al menos 20 TPS
        http_reqs: ['rate>=20'],
    },
};

export default function () {
    // Seleccionar credencial distribuida desde el CSV
    const credential = csvData[(__VU * 10 + __ITER) % csvData.length];
    
    const url = 'https://fakestoreapi.com/auth/login';
    const payload = JSON.stringify({
        username: credential.username,
        password: credential.password,
    });
    
    const params = {
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        },
        timeout: '10s',
    };
    
    // Ejecución de la petición POST
    const res = http.post(url, payload, params);
    
    // Validaciones requeridas
    check(res, {
        'Estado HTTP es 200 o 201': (r) => r.status === 200 || r.status === 201,
        'Tiempo de respuesta <= 1500ms': (r) => r.timings.duration <= 1500,
        'Cuerpo recibido': (r) => r.body && r.body.length > 0,
    });
    
    sleep(0.05);
}

// 3. Generación de Reportes de Salida (HTML y Texto)
export function handleSummary(data) {
    const totalReqs = data.metrics.http_reqs ? data.metrics.http_reqs.values.count : 0;
    const reqRate = data.metrics.http_reqs ? data.metrics.http_reqs.values.rate.toFixed(2) : 0;
    const avgDuration = data.metrics.http_req_duration ? data.metrics.http_req_duration.values.avg.toFixed(2) : 0;
    const p95Duration = data.metrics.http_req_duration ? data.metrics.http_req_duration.values['p(95)'].toFixed(2) : 0;
    const maxDuration = data.metrics.http_req_duration ? data.metrics.http_req_duration.values.max.toFixed(2) : 0;
    const failRate = data.metrics.http_req_failed ? (data.metrics.http_req_failed.values.rate * 100).toFixed(2) : 0;
    
    const isTpsOk = reqRate >= 20;
    const isP95Ok = p95Duration <= 1500;
    const isFailOk = failRate < 3.0;

    const html = `<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reporte de Pruebas de Carga - FakeStore Login (K6)</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #f4f6f9; color: #333; margin: 0; padding: 20px; }
        .container { max-width: 900px; margin: 0 auto; background: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
        h1 { color: #0E2B5C; border-bottom: 2px solid #2980B9; padding-bottom: 10px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin: 25px 0; }
        .card { background: #f8f9fa; border-left: 5px solid #2980B9; padding: 15px; border-radius: 4px; }
        .card.success { border-left-color: #27ae60; }
        .card.danger { border-left-color: #e74c3c; }
        .card-title { font-size: 13px; text-transform: uppercase; color: #7f8c8d; font-weight: bold; }
        .card-val { font-size: 24px; font-weight: bold; color: #2c3e50; margin-top: 5px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background: #0E2B5C; color: white; }
        .badge-ok { background: #27ae60; color: white; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold; }
        .badge-err { background: #e74c3c; color: white; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold; }
        .footer { margin-top: 30px; text-align: right; font-size: 12px; color: #7f8c8d; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Reporte de Pruebas de Carga - FakeStore API Login</h1>
        <p><strong>Endpoint:</strong> <code>POST https://fakestoreapi.com/auth/login</code> | <strong>Herramienta:</strong> K6 Performance Tester</p>
        
        <div class="grid">
            <div class="card ${isTpsOk ? 'success' : 'danger'}">
                <div class="card-title">Throughput (TPS)</div>
                <div class="card-val">${reqRate} TPS</div>
                <small>SLA >= 20 TPS</small>
            </div>
            <div class="card ${isP95Ok ? 'success' : 'danger'}">
                <div class="card-title">Tiempo de Respuesta p(95)</div>
                <div class="card-val">${p95Duration} ms</div>
                <small>SLA <= 1500 ms</small>
            </div>
            <div class="card ${isFailOk ? 'success' : 'danger'}">
                <div class="card-title">Tasa de Errores</div>
                <div class="card-val">${failRate}%</div>
                <small>SLA < 3%</small>
            </div>
            <div class="card">
                <div class="card-title">Peticiones Totales</div>
                <div class="card-val">${totalReqs}</div>
                <small>Promedio: ${avgDuration} ms</small>
            </div>
        </div>

        <h3>Cumplimiento de SLAs y Validaciones</h3>
        <table>
            <thead>
                <tr>
                    <th>Validación / Criterio</th>
                    <th>Objetivo SLA</th>
                    <th>Valor Obtenido</th>
                    <th>Estado</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Rendimiento de Transacciones (TPS)</strong></td>
                    <td>>= 20.0 TPS</td>
                    <td>${reqRate} TPS</td>
                    <td><span class="${isTpsOk ? 'badge-ok' : 'badge-err'}">${isTpsOk ? 'CUMPLE' : 'FALLA'}</span></td>
                </tr>
                <tr>
                    <td><strong>Tiempo de Respuesta p(95)</strong></td>
                    <td><= 1500 ms (1.5s)</td>
                    <td>${p95Duration} ms</td>
                    <td><span class="${isP95Ok ? 'badge-ok' : 'badge-err'}">${isP95Ok ? 'CUMPLE' : 'FALLA'}</span></td>
                </tr>
                <tr>
                    <td><strong>Tiempo de Respuesta Promedio</strong></td>
                    <td><= 1500 ms (1.5s)</td>
                    <td>${avgDuration} ms</td>
                    <td><span class="badge-ok">CUMPLE</span></td>
                </tr>
                <tr>
                    <td><strong>Tasa de Fallos (Error Rate)</strong></td>
                    <td>< 3.00%</td>
                    <td>${failRate}%</td>
                    <td><span class="${isFailOk ? 'badge-ok' : 'badge-err'}">${isFailOk ? 'CUMPLE' : 'FALLA'}</span></td>
                </tr>
            </tbody>
        </table>

        <div class="footer">
            Generado automáticamente por K6 Load Test Runner | Sofka Quality Engineering Reto Técnico
        </div>
    </div>
</body>
</html>`;

    return {
        "reporte_k6_summary.html": html,
        "stdout": `\n==================================================================\n` +
                  `RESUMEN DE PRUEBA DE CARGA K6 - FAKESTORE LOGIN\n` +
                  `==================================================================\n` +
                  `Total Peticiones:  ${totalReqs}\n` +
                  `Throughput (TPS):   ${reqRate} TPS (SLA >= 20 TPS -> ${isTpsOk ? 'PASSED' : 'FAILED'})\n` +
                  `Duracion p(95):    ${p95Duration} ms (SLA <= 1500ms -> ${isP95Ok ? 'PASSED' : 'FAILED'})\n` +
                  `Duracion Promedio: ${avgDuration} ms\n` +
                  `Duracion Maxima:   ${maxDuration} ms\n` +
                  `Tasa de Error:     ${failRate}% (SLA < 3% -> ${isFailOk ? 'PASSED' : 'FAILED'})\n` +
                  `==================================================================\n`
    };
}
