import zipfile

# Leer archivo comprimido
with zipfile.ZipFile('archivo.zip', 'r') as zip_ref:
    zip_ref.extractall('directorio_destino')

# Crear archivo comprimido
with zipfile.ZipFile('nuevo_archivo.zip', 'w') as zip_ref:
    zip_ref.write('archivo_texto.txt')
