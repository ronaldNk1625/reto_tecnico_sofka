package com.sofka.demoblaze.userinterfaces;

import net.serenitybdd.screenplay.targets.Target;
import org.openqa.selenium.By;

public class ProductDetailPage {

    public static final Target PRODUCT_TITLE = Target.the("Título del Producto")
            .located(By.xpath("//h2[@class='name']"));

    public static final Target PRODUCT_PRICE = Target.the("Precio del Producto")
            .located(By.xpath("//h3[@class='price-container']"));

    public static final Target BOTON_AGREGAR_AL_CARRITO = Target.the("Botón Agregar al Carrito (Add to cart)")
            .located(By.xpath("//a[contains(@class,'btn-success') and contains(text(),'Add to cart')]"));
}
