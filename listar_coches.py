import json
import mysql.connector
from prettytable import PrettyTable

# Leer credenciales desde el archivo JSON (Reto 6)
with open('config.json', 'r') as file:
    config = json.load(file)

# Conectar a la base de datos MySQL (Reto 5)
conexion = mysql.connector.connect(**config)
cursor = conexion.cursor()

# Obtener todos los registros
cursor.execute("SELECT * FROM coches")
coches = cursor.fetchall()

# Formatear la salida estéticamente (Reto 7)
tabla = PrettyTable()
tabla.field_names = ["ID", "Marca", "Modelo", "Color", "KM", "Precio"]

for coche in coches:
    tabla.add_row(coche)

print(tabla)

cursor.close()
conexion.close()
