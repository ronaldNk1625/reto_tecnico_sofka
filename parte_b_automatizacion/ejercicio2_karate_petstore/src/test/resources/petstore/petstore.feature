@petstore
Feature: Automatización de Servicios REST PetStore - Gestión del Ciclo de Vida de Mascotas
  Como Analista de Automatización / Quality Engineer en Sofka
  Quiero probar los servicios REST de la API PetStore (Swagger)
  Para validar la correcta creación, consulta por ID, actualización y filtrado por estatus de mascotas

  Background:
    * url baseUrl
    * header Accept = 'application/json'
    * header Content-Type = 'application/json'
    # Generar un ID único dinámico basado en timestamp para evitar colisiones
    * def generateId = function() { return Math.floor(Math.random() * 90000000) + 10000000 }
    * def petId = generateId()
    * def initialPetName = 'Firulais-Sofka-' + petId
    * def updatedPetName = 'Firulais-Sofka-Adopted-' + petId

  @CrearMascota
  Scenario: 1. Añadir una nueva mascota a la tienda (POST /pet)
    Given path '/pet'
    And request
    """
    {
      "id": #(petId),
      "category": {
        "id": 1,
        "name": "Perros"
      },
      "name": "#(initialPetName)",
      "photoUrls": [
        "https://example.com/photos/firulais1.jpg",
        "https://example.com/photos/firulais2.jpg"
      ],
      "tags": [
        {
          "id": 101,
          "name": "sofka-test"
        },
        {
          "id": 102,
          "name": "automatizacion"
        }
      ],
      "status": "available"
    }
    """
    When method POST
    Then status 200
    And match response.id == petId
    And match response.name == initialPetName
    And match response.status == 'available'
    And match response.category.name == 'Perros'
    And match response.tags[0].name == 'sofka-test'
    # Validación de Schema JSON
    And match response ==
    """
    {
      "id": '#number',
      "category": { "id": '#number', "name": '#string' },
      "name": '#string',
      "photoUrls": '#[] #string',
      "tags": '#[] #object',
      "status": '#string'
    }
    """
    * print 'Mascota creada exitosamente con ID:', response.id

  @ConsultarPorId
  Scenario: 2. Consultar la mascota ingresada previamente por su ID (GET /pet/{petId})
    # Paso 1: Crear la mascota primero para garantizar idempotencia y estado previo
    Given path '/pet'
    And request
    """
    {
      "id": #(petId),
      "category": { "id": 1, "name": "Perros" },
      "name": "#(initialPetName)",
      "photoUrls": ["https://example.com/firulais.jpg"],
      "tags": [{ "id": 1, "name": "qa-sofka" }],
      "status": "available"
    }
    """
    When method POST
    Then status 200

    # Paso 2: Consultar la mascota por ID
    Given path '/pet', petId
    When method GET
    Then status 200
    And match response.id == petId
    And match response.name == initialPetName
    And match response.status == 'available'
    And match response.category.id == 1
    * print 'Mascota consultada correctamente por ID:', response

  @ActualizarMascota
  Scenario: 3. Actualizar el nombre de la mascota y su estatus a "sold" (PUT /pet)
    # Paso 1: Crear la mascota
    Given path '/pet'
    And request
    """
    {
      "id": #(petId),
      "category": { "id": 1, "name": "Perros" },
      "name": "#(initialPetName)",
      "photoUrls": ["https://example.com/firulais.jpg"],
      "tags": [{ "id": 1, "name": "qa-sofka" }],
      "status": "available"
    }
    """
    When method POST
    Then status 200

    # Paso 2: Actualizar la mascota con PUT
    Given path '/pet'
    And request
    """
    {
      "id": #(petId),
      "category": { "id": 1, "name": "Perros" },
      "name": "#(updatedPetName)",
      "photoUrls": ["https://example.com/firulais.jpg"],
      "tags": [{ "id": 1, "name": "qa-sofka" }, { "id": 2, "name": "vendido" }],
      "status": "sold"
    }
    """
    When method PUT
    Then status 200
    And match response.id == petId
    And match response.name == updatedPetName
    And match response.status == 'sold'
    * print 'Mascota actualizada correctamente a estatus sold:', response

  @ConsultarPorEstatus
  Scenario: 4. Consultar las mascotas filtradas por estatus "sold" y verificar la mascota modificada (GET /pet/findByStatus)
    # Paso 1: Crear mascota con estatus sold directamente
    Given path '/pet'
    And request
    """
    {
      "id": #(petId),
      "category": { "id": 1, "name": "Perros" },
      "name": "#(updatedPetName)",
      "photoUrls": ["https://example.com/firulais.jpg"],
      "tags": [{ "id": 1, "name": "qa-sofka" }],
      "status": "sold"
    }
    """
    When method POST
    Then status 200

    # Paso 2: Consultar por estatus "sold"
    Given path '/pet/findByStatus'
    And param status = 'sold'
    When method GET
    Then status 200
    And match response == '#[]'
    # Verificar que la lista contenga un objeto con el ID y estatus 'sold'
    And match response contains deep { id: #(petId), status: 'sold', name: '#(updatedPetName)' }
    * print 'Mascota verificada con éxito dentro del listado de estatus sold'

  @FlujoCompletoE2E
  Scenario: 5. Flujo Integrado E2E del Ciclo de Vida Completo de la Mascota
    # 1. Crear mascota
    Given path '/pet'
    And request { id: #(petId), name: '#(initialPetName)', status: 'available', photoUrls: ['https://example.com/p1.jpg'] }
    When method POST
    Then status 200
    And match response.status == 'available'

    # 2. Consultar por ID
    Given path '/pet', petId
    When method GET
    Then status 200
    And match response.name == initialPetName

    # 3. Actualizar nombre y estatus a "sold"
    Given path '/pet'
    And request { id: #(petId), name: '#(updatedPetName)', status: 'sold', photoUrls: ['https://example.com/p1.jpg'] }
    When method PUT
    Then status 200
    And match response.name == updatedPetName
    And match response.status == 'sold'

    # 4. Consultar por estatus y verificar
    Given path '/pet/findByStatus'
    And param status = 'sold'
    When method GET
    Then status 200
    And match response contains deep { id: #(petId), status: 'sold' }
