from subclases.bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, marca, modelo, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Color: {self.color}, Velocidad: {self.velocidad} km/h, Ruedas: {self.ruedas}, Cilindrada: {self.cilindrada}, Marca: {self.marca}, Modelo: {self.modelo}, Tipo: {self.tipo}"
     
    def catalogar(vehiculos):
        for vehiculo in vehiculos:
            print(f"{vehiculo.__class__.__name__} : {vehiculo}")