import json

#ingreso productos de .json
with open('inventario\inventory.json', 'r+') as f:
    inv_productos = json.load(f)
