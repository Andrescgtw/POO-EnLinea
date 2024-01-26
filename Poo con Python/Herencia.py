class Persona:
    def __init__(self,nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

class Empleado(Persona):
    pass

miguel = Empleado("Miguel", 27, "Ecuatoriano")

print(miguel.nombre)
print(miguel.edad)
print(miguel.nacionalidad)
