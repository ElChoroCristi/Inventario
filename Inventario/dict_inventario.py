import json
#declaro diccionarios de cada producto
higiene = {'prod_higiene' : { 'pasta_dientes': {
    'cantidad' : "",
    'pt_critico' : '3',
    'pedir' : False},
'papel_confort' : {
    'cantidad' : "",
    'pt_critico' : '6',
    'pedir' : False},
'jabon' : {
    'cantidad' : "",
    'pt_critico' : '3',
    'pedir' : False},
'shampoo' : {'cantidad' : "",
    'pt_critico' : '3',
    'pedir' : False},
}}
#inicio nuevo archivo .json para guardar inventarios
with open('inventory.json', 'w+') as json_file:
    #cargo dict en archivo .json, ordenado por filas y alfabeticamente
    json.dump(higiene, json_file, indent = 4, sort_keys=True,)
