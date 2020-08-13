import json

#ingreso productos de .json
with open('inventario\inventory.json', 'r+') as f:
    inv_productos = json.load(f)

#inv_productos['prod_higiene']["jabon"]["cantidad"] = int(input(f'Ingrese Cantidad de {inv_productos["prod_higiene"]["jabon"]["nombre"]} - '))
#print(inv_productos["prod_higiene"]["jabon"])

for n in inv_productos['prod_higiene']:
    print(type(n))
