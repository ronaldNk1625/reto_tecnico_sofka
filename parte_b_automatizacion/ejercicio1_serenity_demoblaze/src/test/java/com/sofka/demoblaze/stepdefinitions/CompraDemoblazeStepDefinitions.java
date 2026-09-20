package com.sofka.demoblaze.stepdefinitions;

import com.sofka.demoblaze.models.Cliente;
import com.sofka.demoblaze.questions.ElMensajeDeConfirmacion;
import com.sofka.demoblaze.questions.LosDetallesDeLaOrden;
import com.sofka.demoblaze.tasks.AbrirPagina;
import com.sofka.demoblaze.tasks.AgregarProductoAlCarrito;
import com.sofka.demoblaze.tasks.CompletarFormularioCompra;
import com.sofka.demoblaze.tasks.FinalizarCompra;
import com.sofka.demoblaze.tasks.NavegarAlCarrito;
import io.cucumber.datatable.DataTable;
import io.cucumber.java.es.Cuando;
import io.cucumber.java.es.Dado;
import io.cucumber.java.es.Entonces;
import io.cucumber.java.es.Y;
import net.serenitybdd.screenplay.actors.OnStage;

import java.util.List;
import java.util.Map;

import static net.serenitybdd.screenplay.GivenWhenThen.seeThat;
import static org.hamcrest.Matchers.containsString;
import static org.hamcrest.Matchers.equalTo;

public class CompraDemoblazeStepDefinitions {

    @Dado("que Ronald ingresa a la página principal de Demoblaze")
    public void queRonaldIngresaALaPaginaPrincipalDeDemoblaze() {
        OnStage.theActorCalled("Ronald").wasAbleTo(
                AbrirPagina.en("https://www.demoblaze.com/")
        );
    }

    @Cuando("Ronald agrega los siguientes dos productos al carrito de compras:")
    public void ronaldAgregaLosSiguientesDosProductosAlCarritoDeCompras(DataTable dataTable) {
        List<Map<String, String>> productos = dataTable.asMaps(String.class, String.class);
        for (Map<String, String> fila : productos) {
            String nombreProducto = fila.get("producto");
            OnStage.theActorInTheSpotlight().attemptsTo(
                    AgregarProductoAlCarrito.conNombre(nombreProducto)
            );
        }
    }

    @Y("visualiza el carrito de compras para verificar los productos seleccionados")
    public void visualizaElCarritoDeComprasParaVerificarLosProductosSeleccionados() {
        OnStage.theActorInTheSpotlight().attemptsTo(
                NavegarAlCarrito.deCompras()
        );
    }

    @Y("completa el formulario de compra con los datos del cliente:")
    public void completaElFormularioDeCompraConLosDatosDelCliente(DataTable dataTable) {
        List<Map<String, String>> datos = dataTable.asMaps(String.class, String.class);
        Map<String, String> primerFila = datos.get(0);
        
        Cliente cliente = new Cliente(
                primerFila.get("nombre"),
                primerFila.get("pais"),
                primerFila.get("ciudad"),
                primerFila.get("tarjetaCredito"),
                primerFila.get("mes"),
                primerFila.get("anio")
        );

        OnStage.theActorInTheSpotlight().attemptsTo(
                CompletarFormularioCompra.conDatosDe(cliente)
        );
    }

    @Y("finaliza la compra")
    public void finalizaLaCompra() {
        OnStage.theActorInTheSpotlight().attemptsTo(
                FinalizarCompra.deLaOrden()
        );
    }

    @Entonces("debería visualizar el mensaje de confirmación {string}")
    public void deberiaVisualizarElMensajeDeConfirmacion(String mensajeEsperado) {
        OnStage.theActorInTheSpotlight().should(
                seeThat(ElMensajeDeConfirmacion.mostrado(), equalTo(mensajeEsperado))
        );
    }

    @Y("la orden debe contener un identificador y el monto total de la transacción")
    public void laOrdenDebeContenerUnIdentificadorYElMontoTotalDeLaTransaccion() {
        OnStage.theActorInTheSpotlight().should(
                seeThat(LosDetallesDeLaOrden.mostrados(), containsString("Id:")),
                seeThat(LosDetallesDeLaOrden.mostrados(), containsString("Amount:"))
        );
    }
}
