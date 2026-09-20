package com.sofka.demoblaze.tasks;

import com.sofka.demoblaze.interactions.AceptarAlerta;
import com.sofka.demoblaze.userinterfaces.HomePage;
import com.sofka.demoblaze.userinterfaces.ProductDetailPage;
import net.serenitybdd.screenplay.Actor;
import net.serenitybdd.screenplay.Task;
import net.serenitybdd.screenplay.Tasks;
import net.serenitybdd.screenplay.actions.Click;
import net.serenitybdd.screenplay.waits.WaitUntil;

import static net.serenitybdd.screenplay.matchers.WebElementStateMatchers.isClickable;
import static net.serenitybdd.screenplay.matchers.WebElementStateMatchers.isVisible;

public class AgregarProductoAlCarrito implements Task {

    private final String nombreProducto;

    public AgregarProductoAlCarrito(String nombreProducto) {
        this.nombreProducto = nombreProducto;
    }

    @Override
    public <T extends Actor> void performAs(T actor) {
        actor.attemptsTo(
                // 1. Asegurar que estamos en Home
                WaitUntil.the(HomePage.NAV_HOME, isClickable()).forNoMoreThan(10).seconds(),
                Click.on(HomePage.NAV_HOME),
                
                // 2. Seleccionar el producto por su nombre
                WaitUntil.the(HomePage.productoPorNombre(nombreProducto), isVisible()).forNoMoreThan(10).seconds(),
                Click.on(HomePage.productoPorNombre(nombreProducto)),

                // 3. En la página de detalle, hacer clic en "Add to cart"
                WaitUntil.the(ProductDetailPage.BOTON_AGREGAR_AL_CARRITO, isClickable()).forNoMoreThan(10).seconds(),
                Click.on(ProductDetailPage.BOTON_AGREGAR_AL_CARRITO),

                // 4. Aceptar la alerta emergente nativa
                AceptarAlerta.delNavegador(),

                // 5. Regresar al Home para continuar agregando
                Click.on(HomePage.NAV_HOME)
        );
    }

    public static AgregarProductoAlCarrito conNombre(String nombreProducto) {
        return Tasks.instrumented(AgregarProductoAlCarrito.class, nombreProducto);
    }
}
