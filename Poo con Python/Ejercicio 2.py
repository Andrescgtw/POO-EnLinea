class Persona:
    def __init__(self, nombre,edad):
        self.nombre =nombre
        self.edad = edad
    
    def mostrarDatos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        
class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado
    
    def ImprimirGrado(self):
        print(f"El grado del estudiante es : {self.grado}")

estudiante= Estudiante("Miguel", 12, "10mo")

estudiante.mostrarDatos()
estudiante.ImprimirGrado()