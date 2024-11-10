import pandas as pd

# Leer archivo de Excel
df = pd.read_excel('archivo.xlsx')
print(df)

# Escribir archivo de Excel
df.to_excel('archivo_guardado.xlsx', index=False)
