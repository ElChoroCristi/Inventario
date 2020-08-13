import json
#declaro diccionarios de cada producto
higiene = {
'pasta_dientes': {
    'nombre' : 'pasta_dientes',
    'cantidad' : "",
    'pt_critico' : '3',
    'pedir' : False},
'papel_confort' : {
    'nombre' : 'papel_confort',
    'cantidad' : "",
    'pt_critico' : '6',
    'pedir' : False},
'jabon' : {
    'nombre' : 'jabon',
    'cantidad' : "",
    'pt_critico' : '3',
    'pedir' : False},
'shampoo' : {
    'nombre' : 'shampoo',
    'cantidad' : "",
    'pt_critico' : '3',
    'pedir' : False},
}
#inicio nuevo archivo .json para guardar inventarios
with open('Inventario\inventory.json', 'w+') as json_file:
    #cargo dict en archivo .json, ordenado por filas y alfabeticamente
    json.dump(higiene, json_file, indent = 4, sort_keys=True,)
