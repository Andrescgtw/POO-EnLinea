/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package pooespe.deber_vehiculos;

/**
 *
 * @author Andres
 */
public class Carro extends Vehiculos {
    public void SubirPasajero(){
      System.out.println("Solo se puede subir hasta 4 pasajeros");
    }
    public void conducir(){
      System.out.println("Conduciendo carro");  
    }
    public Carro (String _color, String _placa, String _marca){
        super.placa =_placa;
        super.color =_color;
        super.marca= _marca;
    }
    
}


    
    
