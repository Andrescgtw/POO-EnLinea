class Auto():
    def __init__(self):
        self.posicion = 0
        self.combustible =100
        
    def mover(self, distancia):
        if self.vombustible >= distancia / 2:
            self.posicion += distancia
            self.combustible -= distancia /2
        else:
            print("No hay suficiente combustible")
    def agrerar_combustible (self, cantidad):
        self.combustible += cantidad
    
    def obtener_combustible (self):
        return self.combustible