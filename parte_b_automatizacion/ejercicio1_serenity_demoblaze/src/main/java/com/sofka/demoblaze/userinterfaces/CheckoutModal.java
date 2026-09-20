package com.sofka.demoblaze.userinterfaces;

import net.serenitybdd.screenplay.targets.Target;
import org.openqa.selenium.By;

public class CheckoutModal {

    public static final Target MODAL_TITULO = Target.the("Título del modal de compra")
            .located(By.id("orderModalLabel"));

    public static final Target CAMPO_NOMBRE = Target.the("Campo Nombre del Cliente")
            .located(By.id("name"));

    public static final Target CAMPO_PAIS = Target.the("Campo País")
            .located(By.id("country"));

    public static final Target CAMPO_CIUDAD = Target.the("Campo Ciudad")
            .located(By.id("city"));

    public static final Target CAMPO_TARJETA = Target.the("Campo Tarjeta de Crédito")
            .located(By.id("card"));

    public static final Target CAMPO_MES = Target.the("Campo Mes de Vencimiento")
            .located(By.id("month"));

    public static final Target CAMPO_ANIO = Target.the("Campo Año de Vencimiento")
            .located(By.id("year"));

    public static final Target BOTON_COMPRAR = Target.the("Botón Finalizar Compra (Purchase)")
            .located(By.xpath("//button[text()='Purchase']"));

    public static final Target BOTON_CERRAR = Target.the("Botón Cerrar Modal")
            .located(By.xpath("//div[@id='orderModal']//button[text()='Close']"));
}
