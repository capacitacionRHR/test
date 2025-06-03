## FUNCIONES

## DEFINICIONES

def saludar():
    return "Hola mundo!"

# saludo = saludar()

# print(saludar())

def sumar(x, y=2):
    """Retorna el resultado de la suma de dos números"""
    resultado = x + y
    return resultado

# print(sumar(4))

def saludar_con_valor_por_def(nombre, mensaje="Hola"):
    return f"{mensaje}, {nombre}"

# print(saludar_con_valor_por_def("Cecilia", "Chau"))

def receta(titulo, *args):
    print(f"Receta de {titulo}")
    print("Ingredientes: ")

    for i in args:
        print(i)

# receta("Torta","Harina", "Huevos", "Leche", "Azucar")

def suma(**kwargs):
    resultado = 0

    for clave, valor in kwargs.items():
        print(clave , "=", valor)
        resultado += valor

    return resultado

# print(suma(a = 2, b = 2, c = 3))


def operaciones(x, y):
    suma = x + y
    resta = x - y
    
    return suma, resta

variable_1 , variable_2 = operaciones(5, 4)

print(variable_1)
print(variable_2)