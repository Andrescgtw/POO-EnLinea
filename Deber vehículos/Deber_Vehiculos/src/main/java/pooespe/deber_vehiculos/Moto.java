/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package pooespe.deber_vehiculos;

/**
 *
 * @author Andres
 */

public class Moto extends Vehiculos{
  
    
    public void SubirPasajero(){
      System.out.println("Solo se puede subir 2 pasajeros");
              }
     public void Correr(){
      System.out.println("Carrera de motos"); 
     }
    public Moto (String color_, String placa_, String marca_){
        super.color=color_;
        super.placa=placa_;
        super.marca=marca_;
    }
}

    
    

  