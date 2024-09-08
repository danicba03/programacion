class Calculadora():

    def __init__(self, operador1, operador2):
        self.operador1 = operador1
        self.operador2 = operador2

    def suma(self):
           return self.operador1 + self.operador2
    
    def resta(self):
         return self.operador1 - self.operador2
    
    def multiplicacion(self):
         return self.operador1 * self.operador2
    
    def divison(self):
         return self.operador1 / self.operador2
    

calculadora = Calculadora(200, 5)

print("El resultado es: ", calculadora.suma())
print("El resultado es: ", calculadora.resta())
print("El resultado es: ", calculadora.multiplicacion())
print("El resultado es: ", int(calculadora.divison()))


