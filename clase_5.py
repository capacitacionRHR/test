## POO

class Coche:

    ruedas = 4

    # Constructor
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    def __str__(self):
        return f"Coche {self.marca} , {self.modelo} de color {self.color}"

    # Método de instancia acelerar
    def acelerar(self):
        print(f"El {self.marca} {self.modelo} está acelerando")

    # Método de clase incrementar ruedas
    @classmethod
    def incrementar_ruedas(cls):
        cls.ruedas += 1

    #Método estático
    @staticmethod
    def calcular_distancia(velocidad, tiempo):
        return velocidad * tiempo


# Creamos objetos a partir de una clase
coche_1 = Coche("Toyota", "Corolla", "Rojo")

coche_2 = Coche("Peugeot", "308", "Rojo")

# Acceder al estado de los atributos 

# print("Primer coche:")
# print(coche_1.marca)
# print(coche_1.modelo)
# print(coche_1.color)
# print(coche_1.ruedas)

# print("Segundo coche:")
# print(coche_2.marca)
# print(coche_2.modelo)
# print(coche_2.color)
# print(coche_2.ruedas)

# coche_1.acelerar()
# coche_2.acelerar()

# Coche.incrementar_ruedas()

# print("Primer coche:")
# print(coche_1.marca)
# print(coche_1.modelo)
# print(coche_1.color)
# print(coche_1.ruedas)

# print("Segundo coche:")
# print(coche_2.marca)
# print(coche_2.modelo)
# print(coche_2.color)
# print(coche_2.ruedas)

# print(coche_2)
