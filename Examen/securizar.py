# Hacer un script de nombre securizar.py en el que se cree un nuevo JSON a partir de users.json de nombre secure-users.json en el que las contraseñas estén hasheadas
import hashlib
import json
import pandas as pd

f = open('users.json', )
data = json.load(f)


def cargarusuarios():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


for item in data:
    hashcode = hashlib.sha256(item['password'].encode()).hexdigest()
    item["password"] = hashcode
    file = open('users.json', )
    with open('secure-users.json', "w") as f:
        json.dump(data, f)

f.close()
