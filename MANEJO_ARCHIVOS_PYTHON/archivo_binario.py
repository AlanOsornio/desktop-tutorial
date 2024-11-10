
with open('imagen.jpg', 'rb') as file:
    data = file.read()


with open('copia_imagen.jpg', 'wb') as file:
    file.write(data)
