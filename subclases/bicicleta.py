from subclases import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, marca, modelo, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"Color: {self.color}, Ruedas: {self.ruedas}, Marca: {self.marca}, Modelo: {self.modelo}, Tipo: {self.tipo}"
    
    def catalogar(vehiculos):
        for vehiculo in vehiculos:
            print(f"{vehiculo.__class__.__name__} : {vehiculo}")


