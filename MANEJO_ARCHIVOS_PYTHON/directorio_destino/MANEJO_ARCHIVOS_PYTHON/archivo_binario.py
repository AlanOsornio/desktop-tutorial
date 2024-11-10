# Leer archivo binario
with open('imagen.jpg', 'rb') as file:
    data = file.read()

# Escribir archivo binario
with open('copia_imagen.jpg', 'wb') as file:
    file.write(data)
