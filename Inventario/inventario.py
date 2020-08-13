import json

#ingreso productos de .json
with open('inventario\inventory.json', 'r+') as f:
    inv_productos = json.load(f)

opcion = str(input("Elegir un Producto "))
producto = ""
cantidad = "3"
for i in inv_productos.keys():
    producto = i
    if opcion.lower() == producto:
        print(f"existen {cantidad} unidades de {producto}")
        want_input = input("Desea ingresar nueva cantidad? ")
        if want_input.upper() == "SI":
            new_q = int(input("Ingrese nueva cantidad "))
            print(f"La cantidad de {producto} ha sido actualizada a {new_q} unidades")
        else:pass
    else: pass

