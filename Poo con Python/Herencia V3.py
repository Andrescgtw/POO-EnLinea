class Persona:
    def __init__(self,nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Hola, estoy hablando")
        
class Empleado(Persona):
    def __init__(self,nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo =trabajo
        self.salario = salario
        
class Estudiante(Persona):
    def __init__(self,nombre, edad, nacionalidad, universidad, notas):
        super().__init__(nombre,edad,nacionalidad)
        self.universidad =universidad
        self.notas = notas
        
  
