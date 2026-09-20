package com.sofka.demoblaze.userinterfaces;

import net.serenitybdd.core.pages.PageObject;
import net.serenitybdd.screenplay.targets.Target;
import org.openqa.selenium.By;

public class HomePage extends PageObject {

    public static final Target NAV_HOME = Target.the("Enlace de inicio en la barra de navegación")
            .located(By.xpath("//a[contains(@class,'nav-link') and contains(text(),'Home')]"));

    public static final Target NAV_CART = Target.the("Enlace del carrito de compras")
            .located(By.id("cartur"));

    public static final Target CATEGORY_PHONES = Target.the("Categoría Celulares / Phones")
            .located(By.xpath("//a[text()='Phones']"));

    public static final Target CATEGORY_LAPTOPS = Target.the("Categoría Laptops")
            .located(By.xpath("//a[text()='Laptops']"));

    public static final Target CATEGORY_MONITORS = Target.the("Categoría Monitores")
            .located(By.xpath("//a[text()='Monitors']"));

    public static Target productoPorNombre(String nombreProducto) {
        return Target.the("Producto: " + nombreProducto)
                .located(By.xpath("//a[contains(@class,'hrefch') and normalize-space(text())='" + nombreProducto + "']"));
    }
}
