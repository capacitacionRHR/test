## Inversiones
from abc import ABC,abstractmethod
from random import uniform


class Inversion(ABC):
    def __init__(self,nombre, monto_invertido):
        self.nombre = nombre
        self.monto_invertido = monto_invertido

    @abstractmethod
    def calcular_rendimiento(self):
        pass

    def resumen(self):
        return f"{self.nombre}: Invertido ${self.monto_invertido:2f}"

class PlazoFijo(Inversion):
    def __init__(self,nombre,monto_invertido, tasa, meses):
        super().__init__(nombre,monto_invertido)
        self.__tasa = tasa
        self._meses = meses

    def calcular_rendimiento(self):
        return self.monto_invertido * (1 + self.__tasa/100) ** (self._meses/12)
    

class Accion(Inversion):
    def calcular_rendimiento(self):
        # simulamos una variacion de mercado con uniform
        return self.monto_invertido * uniform(0.9,1.3)
    

cartera = [
    PlazoFijo("PF Banco Nación", 100000, 80, 12),
    Accion("YPF", 500000),
    Accion("AAPL", 700000)
]

total_invertido = sum(inv.monto_invertido for inv in cartera)
ganancia = sum(inv.calcular_rendimiento() for inv in cartera)

# print(f"Total invertido : {total_invertido}\nRendimiento estimado: {ganancia}")

import matplotlib.pyplot as plt

nombres = [inv.nombre for inv in cartera]
valores = [inv.calcular_rendimiento() for inv in cartera]

plt.bar(nombres,valores)
plt.title("Rendimiento estimado por inversión")
plt.ylabel("Valor final ($)")
plt.show()