package com.sofka.demoblaze.userinterfaces;

import net.serenitybdd.screenplay.targets.Target;
import org.openqa.selenium.By;

public class CartPage {

    public static final Target TABLA_PRODUCTOS_CARRITO = Target.the("Filas de productos en el carrito")
            .located(By.xpath("//tbody[@id='tbodyid']/tr"));

    public static final Target TITULO_PRODUCTO_EN_FILA = Target.the("Nombre del producto en carrito")
            .located(By.xpath("//tbody[@id='tbodyid']/tr/td[2]"));

    public static final Target PRECIO_TOTAL = Target.the("Monto total de la compra")
            .located(By.id("totalp"));

    public static final Target BOTON_REALIZAR_PEDIDO = Target.the("Botón Realizar Pedido (Place Order)")
            .located(By.xpath("//button[contains(@class,'btn-success') and contains(text(),'Place Order')]"));
}
