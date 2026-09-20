package com.sofka.demoblaze.tasks;

import com.sofka.demoblaze.userinterfaces.CheckoutModal;
import com.sofka.demoblaze.userinterfaces.ConfirmationModal;
import net.serenitybdd.screenplay.Actor;
import net.serenitybdd.screenplay.Task;
import net.serenitybdd.screenplay.Tasks;
import net.serenitybdd.screenplay.actions.Click;
import net.serenitybdd.screenplay.waits.WaitUntil;

import static net.serenitybdd.screenplay.matchers.WebElementStateMatchers.isClickable;
import static net.serenitybdd.screenplay.matchers.WebElementStateMatchers.isVisible;

public class FinalizarCompra implements Task {

    @Override
    public <T extends Actor> void performAs(T actor) {
        actor.attemptsTo(
                WaitUntil.the(CheckoutModal.BOTON_COMPRAR, isClickable()).forNoMoreThan(10).seconds(),
                Click.on(CheckoutModal.BOTON_COMPRAR),
                WaitUntil.the(ConfirmationModal.TITULO_CONFIRMACION, isVisible()).forNoMoreThan(12).seconds()
        );
    }

    public static FinalizarCompra deLaOrden() {
        return Tasks.instrumented(FinalizarCompra.class);
    }
}
