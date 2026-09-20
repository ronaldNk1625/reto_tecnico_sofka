package com.sofka.demoblaze.tasks;

import com.sofka.demoblaze.userinterfaces.CartPage;
import com.sofka.demoblaze.userinterfaces.HomePage;
import net.serenitybdd.screenplay.Actor;
import net.serenitybdd.screenplay.Task;
import net.serenitybdd.screenplay.Tasks;
import net.serenitybdd.screenplay.actions.Click;
import net.serenitybdd.screenplay.waits.WaitUntil;

import static net.serenitybdd.screenplay.matchers.WebElementStateMatchers.isClickable;
import static net.serenitybdd.screenplay.matchers.WebElementStateMatchers.isVisible;

public class NavegarAlCarrito implements Task {

    @Override
    public <T extends Actor> void performAs(T actor) {
        actor.attemptsTo(
                WaitUntil.the(HomePage.NAV_CART, isClickable()).forNoMoreThan(10).seconds(),
                Click.on(HomePage.NAV_CART),
                WaitUntil.the(CartPage.BOTON_REALIZAR_PEDIDO, isVisible()).forNoMoreThan(10).seconds()
        );
    }

    public static NavegarAlCarrito deCompras() {
        return Tasks.instrumented(NavegarAlCarrito.class);
    }
}
