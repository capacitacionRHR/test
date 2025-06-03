
# Función para mostrar menú
def mostrar_menu():
    """Retorna con un print las opciones disponibles"""
    print(f"\n --- MENÚ DE OPERACIONES ---")
    print("1. Ver transacciones.")
    print("2. Agregar una nueva transaccion.")
    print("3. Validar transacciones.")
    print("4. Salir.")

# Función para ver transacciones(1)
def ver_transacciones(transacciones):
    """Retorna la lista de transacciones formateada"""
    if not transacciones:
        print("No hay transacciones registradas.")
    else:
        print("Lista de transacciones: ")
        for t in transacciones:
            print(f"ID: {t["id"]}|Monto: {t["monto"]} |Moneda: {t["moneda"]}")
            
#Funcion para agregar una nueva transaccion
def agregar_transaccion(transacciones):
    """Agrega una transaccion a la lista"""
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

#Funcion para validar las transacciones
def validar_transacciones(transacciones):
    """Valida las transacciones dentro de la lista"""
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