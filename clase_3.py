## CONDICIONALES

## IF 

"""color_1 = "Blanco"
color_2 = "Negro"

if color_1 == color_2:
    print("Los colores son iguales")"""


## IF - ELSE

"""if color_1 == color_2:
    print("Los colores son iguales")
else:
    print("Los colores NO son iguales")"""

## PROBLEMA

""" En el siguiente ejemplo vamos a plantear la entrada
 de un auto a un estacionamiento.
 El programa debe ser capaz de simular la orden de
 levantar la barrera para que el auto pase si este paga
 el 
monto correcto que sale el ingreso al
 estacionamiento.
 En este caso, el monto será de $1.000 y una vez
 simulamos que el usuario ingresa el dinero, la barrera
 se levantará o no"""

##SOLUCIÓN

# valor_estacionamiento = 1000

# print("Bienvenido! Para ingresar al estacionamiento debe abonar el monto de $1000")

# monto_ingresado = int(input("Por favor , ingrese el monto: "))

"""if monto_ingresado == valor_estacionamiento:
    print("La barrera se levantará para que pueda ingresar, muchas gracias!")
elif monto_ingresado > valor_estacionamiento:
    vuelto = monto_ingresado - valor_estacionamiento
    print(f"Puede pasar, su vuelto es de: {vuelto}, muchas gracias!")
else:
    print("El monto ingresado no es correcto, no puede pasar.")"""

"""while monto_ingresado != valor_estacionamiento:
    print("El monto ingresado no es correcto. El valor es de $1000")

    monto_ingresado = int(input("Por favor, ingrese nuevamente el monto a pagar: "))

print("La barrera se levantará para que pueda ingresar, muchas gracias!")"""

"""clave_correcta = "clave123"
intentos = 3

while intentos > 0:
    clave_ingresada = input("Ingrese su clave: ")
    if clave_ingresada == clave_correcta:
        print("Acceso concedido, puede ingresar!")
        break
    else:
        intentos -= 1
        print(f"Clave incorrecta. Intentos restantes: {intentos}")
else:
    print("Acceso bloqueado!")"""

# while True: - break

# bandera = True
# while bandera: -> bandera = False

# for a in range(0,11,2):
#     print(a)


transacciones = []

while True:
    print(f"\n --- MENÚ DE OPERACIONES ---")
    print("1. Ver transacciones.")
    print("2. Agregar una nueva transaccion.")
    print("3. Validar transacciones.")
    print("4. Salir.")

    opcion = input("Seleccione una opcion (1-4): ")

    if opcion == "1":
        if not transacciones:
            print("No hay transacciones registradas.")
        else:
            print("Lista de transacciones:")
            for t in transacciones:
                print("ID:", t["id"], "|MONTO: ", t["monto"], "|Moneda: ", t["moneda"])
    elif opcion == "2":
        try:
            monto = float(input("Ingrese el monto de la transaccion: "))
            moneda = input("Ingrese la moneda (ARS/USD): ").upper()
            if moneda != "ARS" and moneda != "USD":
                print("Moneda ingresada incorrecta.")
            else:
                nueva = {
                    "id" : len(transacciones) + 1,
                    "monto" : monto,
                    "moneda" : moneda
                }
                transacciones.append(nueva)
                print("Transaccion fue agregada con éxito!")
        except ValueError:
            print("Error: el monto debe ser un número.")
    elif opcion == "3":
        if not transacciones:
            print("No hay transacciones registradas.")
        else:
            print("Validacion de transacciones: ")
            for t in transacciones:
                if t["monto"] <= 0:
                    estado = "Monto invalido"
                elif t["moneda"] == "ARS" and t["monto"] > 100000:
                    estado = "Requiere una autorizacion adicional"
                elif t["moneda"] == "USD" and t["monto"] > 10000:
                    estado = "Requiere una autorizacion adicional por monto en divisa USD"
                else:
                    estado = "Transaccion válida!"
                print(f"ID: {t["id"]}, : {estado}")
    elif opcion == "4":
        print("Saliendo del sistema. Gracias por utilizar nuestro servicio!")
        break
    else:
        print("Opción no válida. Intente nuevamente.")