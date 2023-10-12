class Operacion:
    def calcular(self, operand1, operand2):
        raise NotImplementedError("Método abstracto")


class Suma(Operacion):
    def calcular(self, operand1, operand2):
        return operand1 + operand2


class Resta(Operacion):
    def calcular(self, operand1, operand2):
        return operand1 - operand2


class Multiplicacion(Operacion):
    def calcular(self, operand1, operand2):
        return operand1 * operand2


# Uso de las operaciones
suma = Suma()
resta = Resta()
multiplicacion = Multiplicacion()

print(suma.calcular(5, 3))  # Output: 8
print(resta.calcular(5, 3))  # Output: 2
print(multiplicacion.calcular(5, 3))  # Output: 15





