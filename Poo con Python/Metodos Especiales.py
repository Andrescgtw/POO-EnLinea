class  Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'
    
    def __repr__(self):
        return f'Persona ("{self.nombre}",{self.edad})'
        
andres = Persona("Andres", 27)
print(andres)

repre =repr(andres)
resultado = eval(repre)

print(repre)
print(resultado.edad)