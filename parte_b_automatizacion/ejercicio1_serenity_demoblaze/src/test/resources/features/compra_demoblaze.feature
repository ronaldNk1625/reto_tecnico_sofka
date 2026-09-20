#language: es
@compra @demoblaze
Característica: Flujo de Compra E2E en la tienda virtual Demoblaze
  Como un cliente de la tienda online Demoblaze
  Quiero seleccionar dos productos, agregarlos al carrito de compras y completar el formulario de pedido
  Para realizar una compra exitosa y recibir la confirmación de la orden con su identificador

  Antecedentes:
    Dado que Ronald ingresa a la página principal de Demoblaze

  @FlujoCompletoExitoso
  Escenario: Realizar compra exitosa de dos productos tecnológicos
    Cuando Ronald agrega los siguientes dos productos al carrito de compras:
      | producto            | categoria |
      | Samsung galaxy s6   | Phones    |
      | Nokia lumia 1520    | Phones    |
    Y visualiza el carrito de compras para verificar los productos seleccionados
    Y completa el formulario de compra con los datos del cliente:
      | nombre       | pais    | ciudad     | tarjetaCredito   | mes | anio |
      | Ronald Sofka | Ecuador | Guayaquil  | 4532890123456789 | 12  | 2027 |
    Y finaliza la compra
    Entonces debería visualizar el mensaje de confirmación "Thank you for your purchase!"
    Y la orden debe contener un identificador y el monto total de la transacción
