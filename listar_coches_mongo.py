from pymongo import MongoClient
from prettytable import PrettyTable

# Conectar a MongoDB usando el usuario y contraseña que definimos
client = MongoClient("mongodb://admin:secreta@127.0.0.1:27017/")
db = client["concesionario"]
coleccion = db["coches"]

# Obtener todos los documentos
coches = coleccion.find()

# Formatear la salida estéticamente
tabla = PrettyTable()
tabla.field_names = ["ID", "Marca", "Modelo", "Color", "KM", "Precio"]

for coche in coches:
    tabla.add_row([
        coche["id"], 
        coche["marca"], 
        coche["modelo"], 
        coche["color"], 
        coche["km"], 
        coche["precio"]
    ])

print(tabla)
