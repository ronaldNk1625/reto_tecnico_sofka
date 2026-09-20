package com.sofka.demoblaze.tasks;

import com.sofka.demoblaze.models.Cliente;
import com.sofka.demoblaze.userinterfaces.CartPage;
import com.sofka.demoblaze.userinterfaces.CheckoutModal;
import net.serenitybdd.screenplay.Actor;
import net.serenitybdd.screenplay.Task;
import net.serenitybdd.screenplay.Tasks;
import net.serenitybdd.screenplay.actions.Click;
import net.serenitybdd.screenplay.actions.Enter;
import net.serenitybdd.screenplay.waits.WaitUntil;

import static net.serenitybdd.screenplay.matchers.WebElementStateMatchers.isClickable;
import static net.serenitybdd.screenplay.matchers.WebElementStateMatchers.isVisible;

public class CompletarFormularioCompra implements Task {

    private final Cliente cliente;

    public CompletarFormularioCompra(Cliente cliente) {
        this.cliente = cliente;
    }

    @Override
    public <T extends Actor> void performAs(T actor) {
        actor.attemptsTo(
                // 1. Clic en botón "Place Order" en la página del carrito
                WaitUntil.the(CartPage.BOTON_REALIZAR_PEDIDO, isClickable()).forNoMoreThan(10).seconds(),
                Click.on(CartPage.BOTON_REALIZAR_PEDIDO),

                // 2. Esperar que el modal de checkout sea visible
                WaitUntil.the(CheckoutModal.CAMPO_NOMBRE, isVisible()).forNoMoreThan(10).seconds(),

                // 3. Diligenciar cada uno de los campos
                Enter.theValue(cliente.getNombre()).into(CheckoutModal.CAMPO_NOMBRE),
                Enter.theValue(cliente.getPais()).into(CheckoutModal.CAMPO_PAIS),
                Enter.theValue(cliente.getCiudad()).into(CheckoutModal.CAMPO_CIUDAD),
                Enter.theValue(cliente.getTarjetaCredito()).into(CheckoutModal.CAMPO_TARJETA),
                Enter.theValue(cliente.getMes()).into(CheckoutModal.CAMPO_MES),
                Enter.theValue(cliente.getAnio()).into(CheckoutModal.CAMPO_ANIO)
        );
    }

    public static CompletarFormularioCompra conDatosDe(Cliente cliente) {
        return Tasks.instrumented(CompletarFormularioCompra.class, cliente);
    }
}
