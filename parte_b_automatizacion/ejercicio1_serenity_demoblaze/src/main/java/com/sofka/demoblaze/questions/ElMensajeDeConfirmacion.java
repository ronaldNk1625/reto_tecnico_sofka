package com.sofka.demoblaze.questions;

import com.sofka.demoblaze.userinterfaces.ConfirmationModal;
import net.serenitybdd.screenplay.Actor;
import net.serenitybdd.screenplay.Question;
import net.serenitybdd.screenplay.questions.Text;

public class ElMensajeDeConfirmacion implements Question<String> {

    @Override
    public String answeredBy(Actor actor) {
        return Text.of(ConfirmationModal.TITULO_CONFIRMACION).answeredBy(actor).trim();
    }

    public static ElMensajeDeConfirmacion mostrado() {
        return new ElMensajeDeConfirmacion();
    }
}
