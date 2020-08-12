import json

with open ('inventario/listado.json') as l:
    listado = json.loads(l.read())

cantidad = ''
for producto in listado:
    cantidad = input('Ingrese Cantidad')
print(cantidad)
