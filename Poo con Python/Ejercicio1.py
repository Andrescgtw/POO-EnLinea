class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre=nombre
        self.edad=edad
        self.grado=grado
    
luis =Estudiante ("Luis", 12, "10mo")

print(luis.nombre)
print(luis.edad)
print(luis.grado)