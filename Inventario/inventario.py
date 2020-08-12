import json

with open ('inventario/listado.json', 'r+') as l:
    listado = json.loads(l.read())

print(type(listado))