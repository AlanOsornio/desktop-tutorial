import os

# Obtener ruta absoluta
ruta = os.path.abspath('archivo_texto.txt')
print(ruta)

# Verificar existencia de archivo
if os.path.exists('archivo_texto.txt'):
    print("El archivo existe.")
