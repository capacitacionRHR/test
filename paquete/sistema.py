import csv

from paquete.transaccion import Transaccion

class Sistema:

    def __init__(self):
        self.transacciones = []

    def mostrar_menu(self):
        print(f"\n --- MENÚ DE OPERACIONES ---")
        print("1. Ver transacciones.")
        print("2. Agregar una nueva transaccion.")
        print("3. Validar transacciones.")
        print("4. Salir.")
        print("5. Importar desde CSV")
        print("6. Exportar a CSV")

    def ver_transacciones(self):
        if not self.transacciones:
            print("No hay transacciones registradas.")
        else:
            print("Lista de transacciones:")
            for t in self.transacciones:
                print(t)

    def agregar_transaccion(self):
        try:
            monto= float(input("Ingrese el monto de la transaccion: "))
            moneda = input("Ingrese la moneda (ARS/USD):").upper()
            if moneda not in ("ARS", "USD"):
                print("Moneda ingresada incorrecta")
                return
            nueva_transaccion = Transaccion(id=len(self.transacciones) + 1, monto=monto , moneda=moneda)
            self.transacciones.append(nueva_transaccion)
            print("Transaccion agregada correctamente!")
        except ValueError:
            print("Error: el monto debe ser un número")

    def validar_transacciones(self):
        if not self.transacciones:
            print("No hay transacciones registradas.")
        else:
            print("Validacion de transacciones: ")
            for t in self.transacciones:
                estado = t.validar()
                print(f"{t} -> {estado}")

    def importar_csv(self, ruta):
        try:
            with open(ruta, mode='r', newline="", encoding='utf-8') as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    nueva_transaccion = Transaccion(
                        id=int(fila["id"]),
                        monto=float(fila["monto"]),
                        moneda=fila["moneda"]
                    )
                    self.transacciones.append(nueva_transaccion)
            print("Transacciones importadas exitosamente!")
        except FileNotFoundError:
            print("Archivo no encontrado")
        except Exception as e:
            print(f"Error al importar archivo: {e}")

    def exportar_csv(self, ruta):
        try:
            with open(ruta, mode='w', newline="", encoding='utf-8') as archivo:
                campos =["id", "monto", "moneda"]
                escritor = csv.DictWriter(archivo, fieldnames=campos)
                escritor.writeheader()
                for t in self.transacciones:
                    escritor.writerow(
                        {
                            "id": t.id,
                            "monto": t.monto,
                            "moneda": t.moneda
                        }
                    )
            print("Transacciones exportadas exitosamente!")
        except Exception as e:
            print(f"Error al exportar: {e}")
                