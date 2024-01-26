class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad =edad
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,nuevoNombre):
        self._nombre = nuevoNombre
        
    @nombre.deleter
    def nombre(self):
        del self._nombre
    
marce = Persona("Marcela",26)

nombre = marce.nombre
print (nombre)

marce.nombre = "Marce"
nombre = marce.nombre

print (nombre)

