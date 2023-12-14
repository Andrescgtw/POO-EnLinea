/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package pooespe.deber_vehiculos;

/**
 *
 * @author Andres
 */
public class Deber_Vehiculos {

    public static void main(String[] args) {
        Moto moto1 = new Moto ("blanco", "HB35", "HONDA");
        
        moto1.SubirPasajero();
        moto1.Correr();
      
        Carro car1 = new Carro ("Rojo", "PCA3544", "CHEVROLET");
        
        car1.SubirPasajero();
        car1.conducir();
    }
   
    
}
