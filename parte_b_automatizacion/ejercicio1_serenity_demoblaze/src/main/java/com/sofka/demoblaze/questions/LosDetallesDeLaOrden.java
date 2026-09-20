package com.sofka.demoblaze.questions;

import com.sofka.demoblaze.userinterfaces.ConfirmationModal;
import net.serenitybdd.screenplay.Actor;
import net.serenitybdd.screenplay.Question;
import net.serenitybdd.screenplay.questions.Text;

public class LosDetallesDeLaOrden implements Question<String> {

    @Override
    public String answeredBy(Actor actor) {
        return Text.of(ConfirmationModal.DETALLES_COMPRA).answeredBy(actor).trim();
    }

    public static LosDetallesDeLaOrden mostrados() {
        return new LosDetallesDeLaOrden();
    }
}
