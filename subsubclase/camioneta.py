from subclases.coche import Coche

class Camioneta(Coche):

    def __init__(self, color, ruedas, velocidad, cilindrada, marca, modelo, capacidad_carga):
        super().__init__(color, ruedas, velocidad, cilindrada, marca, modelo)
        self.capacidad_carga = capacidad_carga
        
    def __str__(self):
        return f"Color: {self.color}, Velocidad: {self.velocidad} km/h, Ruedas: {self.ruedas}, Cilindrada: {self.cilindrada}, Marca: {self.marca}, Modelo: {self.modelo}, Capacidad de carga: {self.capacidad_carga}"
    
    def catalogar(vehiculos):
        for vehiculo in vehiculos:
            print(f"{vehiculo.__class__.__name__} : {vehiculo}")