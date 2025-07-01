# import mysql.connector
# from dotenv import load_dotenv
# import os

# load_dotenv()

# conn = mysql.connector.connect(
#     host = os.getenv("DB_HOST"),
#     user= os.getenv("DB_USER"),
#     password = os.getenv("DB_PASS"),
#     database = os.getenv("DB_NAME")
# )

# cursor = conn.cursor()

# Sentencia para la lectura de registros
# cursor.execute("SELECT * FROM empleados;")
# for row in cursor.fetchall():
#     print(row)

# Sentencia para insercion de datos
# sql = "INSERT INTO empleados (nombre, puesto, sueldo ) VALUES (%s,%s,%s)"
# data = ("Juan", "puesto2", 2500)
# cursor.execute(sql, data)
# conn.commit()

#Manejo de errores
# try:
#     conn = mysql.connector.connect(
#         host = os.getenv("DB_HOST"),
#         user= os.getenv("DB_USER"),
#         password = os.getenv("DB_PASS"),
#         database = os.getenv("DB_NAME")
#     )

#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM empleados WHERE sueldo > 1000;")
#     for row in cursor.fetchall():
#         print(row)
# except mysql.connector.Error as err:
#     print("Error:", err)

# finally:
#     cursor.close()
#     conn.close()

# Transacciones
# try:
#     conn.start_transaction()
#     cursor.execute("UPDATE empleados SET sueldo = sueldo * 1.1 WHERE puesto = 'puesto1'")
#     cursor.execute("INSERT INTO empleados(nombre,puesto,sueldo) VALUES ('Error','interno',2000)") # Generar un error
#     conn.commit()
# except Exception as e:
#     print("Revirtiendo cambios", e)
#     conn.rollback()