from abc import ABC, abstractclassmethod

class VerificadorOrtografico(ABC):
    @abstractclassmethod
    def verificar_palabra(self, palabra):
        pass
    
class Diccionario (VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #logica para verificar palabras si esta en el diccionario
        pass

class ServicioOnLine(VerificadorOrtografico):
       def verificar_palabra(self, palabra):
        #logica para verificar palabras desde el servicio web
        pass
    
class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador
        
    def corregir_texto(self, texto):
        pass
        #Usamos e4l verificador para corregir texto
        
corrector= CorrectorOrtografico()