class Persona:
    def __init__(self,nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Hola, estoy hablando")

class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
    
    def mostrarHabilidad(self):
        return f"Mi habilidad es: {self.habilidad}"
        
class EmpleadoArtista(Persona, Artista):
    def __init__ (self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa
    
    def presentarse (self):
        print(f'Hola, soy {self.nombre}, {self.mostrarHabilidad()} y trabajo en {self.empresa}')
       

luis = EmpleadoArtista("Luis", 24,"Ecuatoriana", "Bailar", 800, "TICS")
roberto= Artista("Cantar")

herencia=issubclass(EmpleadoArtista, Artista)
instancia = isinstance(luis,EmpleadoArtista)

print(instancia)

instancia2 = isinstance(roberto,EmpleadoArtista)
print(instancia2)