import json

with open ('inventario/listado.json') as l:
    listado = json.load(l)

print(listado, indent=2)

