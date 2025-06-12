"""Ejercicio 1: Promedio móvil de cotizaciones
Enunciado:

Desarrollá una clase ActivoFinanciero que permita almacenar un historial de precios de un activo (por ejemplo, una acción o un bono).

La clase debe permitir:

Agregar nuevos precios al historial.

Calcular el promedio móvil de N días sobre el historial.

"""

class ActivoFinanciero:
    def __init__(self,nombre, historial_precios):
        self.nombre = nombre
        self.historial_precios = historial_precios

    def nuevo_precio(self, precio):
        if precio <= 0:
            raise ValueError("El precio debe ser positivo.")
        self.historial_precios.append(float(precio))
        print(f"Los precios guardados para el activo {self.nombre} son: {self.historial_precios}")

    def promedio_movil(self, n):

        if n <= 0:
            print("La cantidad de días debe ser mayor que cero.")
            return []

        if len(self.historial_precios) < n:
            print("No hay suficientes datos para calcular el promedio móvil.")
            return []

        promedios = []
        for i in range(n - 1, len(self.historial_precios)):
            ventana = self.historial_precios[i+1-n : i+1]
            promedio = sum(ventana) / n
            promedios.append(promedio)
        return promedios
             
activo_x = ActivoFinanciero("Accion X", [100,105,110,115,95,102,110])
activo_x.nuevo_precio(120)
print(activo_x.promedio_movil(3))

"""Ejercicio 2: Simulador de préstamo con sistema francés
Enunciado:
Modelá una clase Prestamo que calcule el valor de la cuota mensual de un préstamo bajo el sistema francés de amortización, usando como datos:

Capital solicitado.

Tasa de interés anual.

Cantidad de cuotas.

La clase debe:

Calcular el valor fijo de la cuota.

Mostrar un plan de pagos mensual, detallando: número de cuota, monto total, capital amortizado, interés pagado y saldo restante.

"""



"""Ejercicio 3: Validación y resumen de transacciones
Enunciado:
Dado un conjunto de transacciones en forma de diccionarios (con campos cliente, monto, categoría), se pide:

Modelar cada transacción como una instancia de una clase Transaccion.

Validar cada transacción (monto positivo y categoría válida).

Agrupar las transacciones válidas por cliente.

Mostrar el total de gasto por cliente.

"""


"""Ejercicio 4: Sistema de alertas de precios
Enunciado:
Diseñá un sistema de monitoreo de precios para activos financieros. Implementá dos clases:

Alerta: Representa una alerta de precio, con un umbral mínimo.

Monitor: Mantiene varias alertas registradas, y verifica si hay alguna que se dispara.

Se debe poder:

Registrar múltiples alertas por activo.

Verificar si un precio actual cae por debajo del umbral y mostrar un mensaje de alerta.

"""



"""Ejercicio 5: Carrito de compras con IVA y descuentos
Enunciado:
Simulá un sistema de facturación. Creá una clase Producto que almacene nombre, precio unitario y cantidad. Luego, creá una clase Carrito que:

Permita agregar productos.

Calcule el total bruto de la compra.

Aplique un descuento del 10% si el total supera los $10.000.

Aplique un IVA del 21% sobre el total (descontado o no, según corresponda).

"""