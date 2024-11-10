import json
import os

# Datos iniciales para el archivo JSON
new_data = {
    "nombre": "Ana",
    "edad": 30,
    "profesion": "Ingeniera",
    "ciudad": "Madrid"
}

# Verificar si el archivo existe
if os.path.exists('archivo.json') and os.path.getsize('archivo.json') > 0:
    # Si el archivo ya existe y tiene datos, cargar los datos existentes
    with open('archivo.json', 'r') as file:
        data = json.load(file)
    # Agregar nuevos datos al diccionario
    data.update(new_data)
else:
    # Si el archivo no existe o está vacío, iniciar un nuevo diccionario
    data = new_data

# Escribir (o sobrescribir) el archivo con los datos actualizados
with open('archivo.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Archivo JSON actualizado correctamente.")
