import math

class Calculadora:
    def __init__(self):
        self.resultado = None

    def sumar(self, a, b):
        self.resultado = a + b
        return self.resultado

    def restar(self, a, b):
        self.resultado = a - b
        return self.resultado

    def multiplicar(self, a, b):
        self.resultado = a * b
        return self.resultado

    def dividir(self, a, b):
        if b != 0:
            self.resultado = a / b
        else:
            self.resultado = "Error: Division por cero"
        return self.resultado

    def raiz(self, a):
        if a >= 0:
            self.resultado = math.sqrt(a)
        else:
            self.resultado = "Error: No se puede calcular la raiz de un numero negativo"
        return self.resultado

    def mostrar_resultado(self, operacion):
        print(f'El resultado de la {operacion} es: {self.resultado}')

# Ejemplo de uso
calculadora = Calculadora()

# Sumar
calculadora.sumar(5, 3)
calculadora.mostrar_resultado("suma")

# Restar
calculadora.restar(10, 4)
calculadora.mostrar_resultado("resta")

# Multiplicar
calculadora.multiplicar(6, 7)
calculadora.mostrar_resultado("multiplicacion")

# Dividir
calculadora.dividir(15, 3)
calculadora.mostrar_resultado("division")

# Raiz cuadrada
calculadora.raiz(9)
calculadora.mostrar_resultado("raiz cuadrada")
