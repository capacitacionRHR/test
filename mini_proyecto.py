import random 
from datetime import datetime, timedelta

clientes = ["Juan", "Jose", "Ana", "Cecilia", "Pablo", "Laura"]
tipo = ["ingreso","egreso","inversion","transferencia"]
fecha_inicio = datetime(2025, 6, 1)

transacciones = []

for dia in range(7): # 7 dias
    fecha_actual = fecha_inicio + timedelta(days=dia)
    for t in range(100): # 100 transacciones por dia
        transaccion = {
            'fecha'  : fecha_actual.strftime('%Y-%m-%d'),
            'hora' : f"{random.randint(8,18)}:{random.randint(0,59):02d}",
            'cliente' : random.choice(clientes),
            'tipo' : random.choice(tipo),
            'monto' : round(random.uniform(1000, 100000), 2)
        }
        transacciones.append(transaccion)

import pandas as pd

df = pd.DataFrame(transacciones)

# Ingresos totales
ingresos = df[df['tipo'] == 'ingreso']['monto'].sum()

# Total por tipo
total_por_tipo = df.groupby('tipo')['monto'].sum()

# Total por cliente
total_por_cliente = df.groupby('cliente')['monto'].sum()

#Total por dia
total_por_dia = df.groupby('fecha')['monto'].sum()

import os

os.makedirs("reportes/diarios", exist_ok= True)

# for fecha in df['fecha'].unique():
#     df_dia = df[df['fecha'] == fecha]
#     df_dia.to_csv(f'reportes/diarios/{fecha}_reporte.csv', index=False)

# Exportar analisis
# with pd.ExcelWriter("reportes/reporte_general.xlsx") as writer:
#     df.to_excel(writer, sheet_name="transacciones", index=False)
#     total_por_tipo.to_excel(writer, sheet_name="Total por tipo", index=False)
#     total_por_dia.to_excel(writer, sheet_name="Total por dia", index=False)
#     total_por_cliente.to_excel(writer, sheet_name="Total por cliente", index=False)

# Top 3 de clientes que mas dinero movieron
# top_clientes = total_por_cliente.sort_values(ascending=False).head(3)
# print(f"Top 3 clientes que mas dinero movieron :\n{top_clientes}")


import matplotlib.pyplot as plt

# total_por_tipo.plot(kind="bar", title="Total por tipo de transaccion", ylabel='Monto($)', xlabel="Tipo")
# plt.tight_layout()
# plt.savefig("reportes/monto_por_tipo.png")
# plt.show()

# total_por_dia.plot(kind="line", marker = "o", title="Total por dia", ylabel="Monto($)", xlabel="Fecha")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.savefig("reportes/monto_por_dia.png")
# plt.show()

# df.groupby('cliente')['monto'].sum().plot(kind="pie", autopct="%1.1f%%", startangle=90, title="Montos por clientes")
# plt.ylabel("")
# plt.tight_layout()
# plt.savefig("reportes/monto_por_clientes.png")
# plt.show()