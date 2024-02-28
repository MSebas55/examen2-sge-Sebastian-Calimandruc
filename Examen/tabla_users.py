# Hacer un script tabla_users.py que introduzca a los usuarios con sus contraseñas hasheadas en un excel llamado usuarios.xlsx
# usando pandas y openpyxl (integrado en pandas)
import hashlib
import pandas as pd
import json


def cargarusuarios():
    try:
        with open("secure-users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


df = pd.DataFrame(cargarusuarios())
excel_file_name = f"usuarios.xlsx"
df.to_excel(excel_file_name, index=False)
print(f"\nArchivo Excel '{excel_file_name}' generado exitosamente.")
