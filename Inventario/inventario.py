import json

#ingreso productos de .json
with open('inventario\inventory.json', 'r+') as f:
    inv_productos = json.load(f)

opcion = str(input("Elegir un Producto "))

productos = ""
cantidad = ""
for i in inv_productos.keys():
    productos = i
    if opcion.lower() == productos:
        print(productos)
    else: pass
