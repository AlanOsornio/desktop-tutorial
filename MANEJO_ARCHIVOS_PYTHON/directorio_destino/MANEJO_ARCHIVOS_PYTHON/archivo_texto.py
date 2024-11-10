# Leer archivo
with open('archivo_texto.txt', 'r') as file:
    data = file.read()
print(data)

# Escribir en archivo
with open('archivo_texto.txt', 'w') as file:
    file.write("Este es un texto de ejemplo.")

# Anexar información
with open('archivo_texto.txt', 'a') as file:
    file.write("\nAgregando nueva línea.")
