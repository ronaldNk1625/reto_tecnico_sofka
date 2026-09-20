package com.sofka.demoblaze.models;

public class Cliente {
    private final String nombre;
    private final String pais;
    private final String ciudad;
    private final String tarjetaCredito;
    private final String mes;
    private final String anio;

    public Cliente(String nombre, String pais, String ciudad, String tarjetaCredito, String mes, String anio) {
        this.nombre = nombre;
        this.pais = pais;
        this.ciudad = ciudad;
        this.tarjetaCredito = tarjetaCredito;
        this.mes = mes;
        this.anio = anio;
    }

    public String getNombre() {
        return nombre;
    }

    public String getPais() {
        return pais;
    }

    public String getCiudad() {
        return ciudad;
    }

    public String getTarjetaCredito() {
        return tarjetaCredito;
    }

    public String getMes() {
        return mes;
    }

    public String getAnio() {
        return anio;
    }
}
