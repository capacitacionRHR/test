## LISTAS ##

# lista = [ "Python", 2025, True ]

# print(lista)
# print(lista[0])
# print(lista[1])
# print(lista[2])

# lista = ["Hola", "Chau", 2025]

# print(lista)

lista1 = ["Hola", "Chau", 2025]
lista2 = ["manzana", "banana", "pera"]
lista3 = [ "Cecilia", 230, lista1 , True, lista2]
# print(lista3)

colores  = ["blanco", "azul", "negro", "rojo", "verde", "rojo"]

colores_2 = ["Hola", 2025]
# colores_2.append(123)

colores.insert(0,"colores")

# print(colores)
# print(id(colores_2))


# print(colores[2:4])
# print(colores[-1])
# colores[-1] = "morado"
# print(colores)

# colores.append(123)
# print(colores)

# # colores.remove("rojo")
# # print(colores)

# valor_1= colores.pop(0)
# print(colores)
# print(valor_1)

## Ejercicio : Gestion de compras - Solucion

compras = ["pan", "leche", "huevos", "naranjas"]
# print(compras)

# compras.append("manzanas")
# print(compras)

# compras.remove("leche")
# print(compras)

# ultimo_item = compras.pop()
# print(compras)
# print(ultimo_item)


## TUPLAS ## 

# tupla = (1,2,3)

# print(tupla)

# tupla = ("hola", "chau")
# print(tupla)

# Ejercicio : Encuentro un elemento - Solución

frutas = ("manzana", "naranja", "uva", "manzana", "uva" )

posicion = frutas.index("uva")

# print(f"La primera aparicion de 'uva' se da en la posición : {posicion}")


## CONJUNTOS O SETS

frutas = { "manzana", "naranja", "uva", "manzana", "uva"  }
verduras= { "lechuga", "tomate", "cebolla"}

fruta_y_verduras = frutas | verduras

# print(fruta_y_verduras)

# print(conjunto)

# if "pera" in conjunto:
#     print("Manzana se encuentra en el conjunto")
# else : 
#     print("Manzana no se encuentra en el conjunto")

# for fruta in conjunto:
#     print(fruta)
    

## DICCIONARIOS ##

agenda = { "Ana" : 1234566 , "Jose" : 123333, "Juan" : True}

# print(agenda)

lugar = {
    "pais" : "Argentina",
    "provincia" : "Chaco",
    "cp" : 3500
}

# for clave , valor in lugar.items():
#     print(f"Clave: {clave} Valor : {valor}")

claves = list(lugar.keys())
valores = list(lugar.values())

# print(f"Las claves son : {claves}, y los valores son : {valores}")

## Ejercicio Agenda - Solucion

contactos = {
    "Ana":"ana@example.com",
"Luis": "luis@example.com"}

print(contactos)

contactos["Marta"] = "marta@example.com"
contactos["Luis"] ="luis2023@example.com"
correoEliminado = contactos.pop("Ana")

print(f"Diccionario final : {contactos}\nCorreo eliminado de Ana: {correoEliminado}")


