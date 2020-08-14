import json

#ingreso productos de .json
with open('inventario\inventory.json', 'r+') as f:
    inv_productos = json.load(f)

opcion = str(input("Elegir un Producto --> "))
producto = ""
cantidad = ""

#desglosar el diccionario

for i in inv_productos.keys():
    producto = [i]

    #mostrar al usuario la cantidad de x restante
    if opcion.lower() == producto:
        print(f"existen {cantidad} unidades de {producto}")
        #preguntar si quiere o no cambiar el valor de la cantidad
        want_input = input("Desea ingresar nueva cantidad? ")
        if want_input.upper() == "SI":
            #pedir nuevo valor y mostrarlo en un mensaje
            new_q = int(input("Ingrese nueva cantidad "))
            print(f"La cantidad de {producto} ha sido actualizada a {new_q} unidades")

        else: 
            print("Gracias por Participar")
            pass

    else: 
        print("El producto ingresado no existe, por favor volver a intentar")
        pass
