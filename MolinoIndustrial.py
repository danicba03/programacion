class MolinoIndustrial:
    def __init__(self, capacidad_maxima, material_acumulado=0):
        self.capacidad_maxima = capacidad_maxima
        self.material_acumulado = material_acumulado
        self.encendido = False
    
    def encender(self):
        '''Enciende el molino si no está encendido'''
        self.encendido = True
        print("Molino encendido")

    def agregar_material(self, cantidad):
        if self.material_acumulado + cantidad > self.capacidad_maxima:
            print("No se puede agregar mas material, el molino llegó a su capacidad máxima")
        else:
            self.material_acumulado += cantidad
            print(f"Material agregado: {cantidad}. Total acumulado: {self.material_acumulado}")

    def moler(self):
        if self.material_acumulado > 0:
            print(f"Se ha molido {self.material_acumulado} unidades de material.")
        else:
            print("No hay más material")

    def __str__(self):
        estado = "encendido" if self.encendido else "apagado"
        return f"Molino {estado}, Material acumulado: {self.material_acumulado}/{self.capacidad_maxima}"

# Ej de uso
molino = MolinoIndustrial(capacidad_maxima=100)
molino.encender()
molino.agregar_material(50)
molino.moler()
print(molino) 



