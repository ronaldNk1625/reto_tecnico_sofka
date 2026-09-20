function fn() {
    var env = karate.env; // obtener variable de entorno (e.g., karate.env = 'dev')
    karate.log('Iniciando ejecución de pruebas Karate en ambiente:', env);

    if (!env) {
        env = 'prod';
    }

    var config = {
        env: env,
        baseUrl: 'https://petstore.swagger.io/v2'
    };

    // Configurar timeouts globales
    karate.configure('connectTimeout', 10000);
    karate.configure('readTimeout', 10000);
    karate.configure('ssl', true);

    return config;
}
