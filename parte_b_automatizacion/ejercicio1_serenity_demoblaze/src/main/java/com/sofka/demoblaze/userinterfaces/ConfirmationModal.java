package com.sofka.demoblaze.userinterfaces;

import net.serenitybdd.screenplay.targets.Target;
import org.openqa.selenium.By;

public class ConfirmationModal {

    public static final Target TITULO_CONFIRMACION = Target.the("Mensaje de éxito de la compra")
            .located(By.xpath("//div[contains(@class,'sweet-alert')]//h2"));

    public static final Target DETALLES_COMPRA = Target.the("Detalles de la transacción (ID, Amount, etc.)")
            .located(By.xpath("//div[contains(@class,'sweet-alert')]//p[contains(@class,'lead')]"));

    public static final Target BOTON_CONFIRMACION_OK = Target.the("Botón OK de confirmación")
            .located(By.xpath("//button[contains(@class,'confirm') and text()='OK']"));
}
