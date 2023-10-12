class Calculadora:
    def __init__(self, operand1, operand2, operacion):
        self.operand1 = operand1
        self.operand2 = operand2
        self.operacion = operacion

    def calcular(self):
        if self.operacion == "sumar":
            return self.operand1 + self.operand2
        elif self.operacion == "restar":
            return self.operand1 - self.operand2
        # Aquí se viola el OCP al modificar la clase existente
        elif self.operacion == "multiplicar":
            return self.operand1 * self.operand2
        else:
            raise ValueError("Operación no válida")


# Uso de la calculadora
calc = Calculadora(5, 3, "sumar")
print(calc.calcular())  # Output: 8



