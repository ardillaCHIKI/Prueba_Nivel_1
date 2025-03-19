from subclases import Vehiculo

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def catalogar(vehiculos):
        for vehiculo in vehiculos:
            print(f"{vehiculo.__class__.__name__} : {vehiculo}")
        