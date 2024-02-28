import json
from datetime import datetime
import pandas as pd

archivo = open('libraries-and-books.json', 'w')
nombres = ['a', 'b', 'c']
edades = [1, 2, 3]

df = pd.DataFrame({'ID Biblioteca': nombres, 'ID Libro': edades, 'Titulo': nombres, 'Editorial': nombres, 'Año de publicación': nombres, 'ID Usuario': nombres, 'Nombre completo': nombres})

print(df)

df.index.name = 'ID'

now = datetime.now()
day_month = now.strftime("%d-%m")

excel_file_name = f"{day_month}-libros-prestados.xlsx"
df.to_excel(excel_file_name, index=False)

print(f"\nArchivo Excel '{excel_file_name}' generado exitosamente.")
