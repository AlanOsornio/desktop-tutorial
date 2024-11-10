import csv

# Leer CSV
with open('archivo.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Escribir CSV
with open('archivo.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Nombre", "Edad"])
    writer.writerow(["Alan", 19])
