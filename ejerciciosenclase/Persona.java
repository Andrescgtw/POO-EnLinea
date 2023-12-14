/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.ejerciciosenclase;

/**
 *
 * @author Andres
 */
public class Persona {
    String nombre;
    String apellido;
    int edad;
    private int cedula;


    public Persona(String _nombre, String _apellido, int _edad){
    nombre = _nombre;
    apellido = _apellido;
    edad = _edad;
    }
    public int getCI(){
        return cedula;
    }
    
    public void setCI(int cedula){
        this.cedula = cedula;
    }
        
    
}
