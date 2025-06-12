  ## HERENCIA ##

class Vehiculo:

    def __init__(self, ruedas, marca, modelo, color):
        self.ruedas = ruedas
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def acelerar(self):
        print(f"El {self.marca} {self.modelo} está acelerando")

class Coche(Vehiculo):
    pass

class Bicicleta(Vehiculo):
    pass

coche_1 = Coche(4,"Ford", "Focus", "Rojo")

bici_1 = Bicicleta(2, "SLP", "100pro", "Gris")


class A :

    def __init__(self):
        super().__init__()
        print("Soy la clase A")

class B :

    def __init__(self):
        super().__init__()
        print("Soy la clase B")
class C(A,B):

    def __init__(self):
        super().__init__()
        print("Soy la clase C")


# test = C()

# print(f"MRO: {C.__mro__}")


## Ejercicio 1

"""Crearemos una clase Persona en la cual guardaremos la información general de cada persona, y una clase estudiante que heredará los
atributos y métodos de la clase anterior con información más precisa sobre la carrera que está estudiando."""

"""class Persona:
    def __init__(self, nombre, apellido, nro_tel, email):
        self.nombre = nombre
        self.apellido = apellido
        self.nro_tel = nro_tel
        self.email = email

    def nombre_completo(self):
        print(f"El nombre de esta persona es {self.nombre} y su apellido {self.apellido}")

class Estudiante(Persona):
    def __init__(self, nombre, apellido, nro_tel, email, carrera):
        super().__init__(nombre, apellido, nro_tel, email)
        self.carrera = carrera

    def mostrar_carrera(self):
        print(f"Está estudiando {self.carrera}")

estudiante_1 = Estudiante("Juan", "Perez", "123123", "asdasd@ads.com", "Medicina")
persona_1 = Persona("Maria", "Gomez", 123123, "asdasd@asd.com")

estudiante_1.nombre_completo()
estudiante_1.mostrar_carrera()
"""

"""Similar al ejemplo anterior, definiremos las clases Universidad() y Carrera() para posteriormente ser heredadas en la clase Estudiante()
donde reuniremos el nombre de la universidad y la carrera que nuestro estudiante objeto estudia además de requerir sus datos
personales"""


# class Universidad():
#     def __init__(self, nombre_universidad):
#         self.nombre_universidad = nombre_universidad

# class Carrera():
#     def __init__(self, especialidad):
#         self.especialidad = especialidad

# class Estudiante(Universidad, Carrera):
#     def __init__(self, nombre, apellido, nro_tel, email, nombre_universidad, especialidad):
#         Universidad.__init__(self, nombre_universidad)
#         Carrera.__init__(self,especialidad)
#         self.nombre = nombre
#         self.apellido = apellido
#         self.nro_tel = nro_tel
#         self.email = email


#     def mostrar_datos(self):
#         print(f"""
#             El nombre del estudiante es {self.nombre} , su apellido es {self.apellido}
#             Está estudiando la carrera de {self.especialidad} en {self.nombre_universidad}
# """)

# estudiante_1 = Estudiante("Juan", "Perez", "123123", "asdasd@ads.com", "UBA","Medicina")

# estudiante_1.mostrar_datos()


## Ejercicio 3

"""Crearemos un sistema bancario que nos permita crear una cuenta, depositar, retirar y consultar la misma. Como son datos sensibles que
deseamos proteger su integridad por fuera de esta clase, es prioritario utilizar encapsulamiento en este ejemplo."""

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

        print(f"Cuenta creada exitosamente! \nTitular: {self.__titular}\nSaldo: {self.__saldo}")
        

    def depositar(self, monto):
        if type(monto) == int or type(monto) == float:
            if monto > 0:
                self.__saldo += monto
                print(f"Se depositó con éxito ${monto}. \nSaldo Actual: {self.__saldo}")
            else:
                print("El monto ingresado es menor o igual a 0")
        else:
            print("Error. El monto debe ser un número o flotante.")
    
    def retirar(self, monto):
        if type(monto) == int or type(monto) == float:
            if monto > 0:
                if monto <= self.__saldo:
                    self.__saldo -= monto
                    print(f"Se retiró correctamente ${monto}. \nSaldo Actual: {self.__saldo}")
                else:
                    print("Fondo insuficiente")
            else:
                print("El monto ingresado es debe ser mayor a 0")
        else:
            print("Error. El monto debe ser un número o flotante.")
        
    def consultar_saldo(self):
        print(f"El saldo de su cuenta es de ${self.__saldo}")
        
    def consultar_datos(self):
        print(f"El titular de la cuenta es {self.__titular}")
        
cliente = CuentaBancaria("Juan", 100000)

cliente.depositar(200)
cliente.retirar(10000)

cliente.consultar_saldo()
cliente.consultar_datos()