import xml.etree.ElementTree as ET
import os

# Verificar si el archivo XML existe y tiene contenido válido
if not os.path.exists('archivo.xml') or os.path.getsize('archivo.xml') == 0:
    # Crear y escribir la estructura básica de XML
    with open("archivo.xml", "w", encoding="utf-8") as file:
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n<root>\n</root>')
    print("Archivo 'archivo.xml' creado e inicializado con estructura básica.")

# Leer XML
tree = ET.parse('archivo.xml')
root = tree.getroot()
for child in root:
    print(child.tag, child.text)

# Escribir en el XML
new_element = ET.Element("nuevo_elemento")
new_element.text = "Texto de ejemplo"
root.append(new_element)
tree.write('archivo_actualizado.xml')
print("Archivo 'archivo_actualizado.xml' actualizado con el nuevo elemento.")
