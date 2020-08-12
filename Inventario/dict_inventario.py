import json

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

with open('inventory.json', 'w+') as json_file:
    json.dump(higiene, json_file, indent = 4, sort_keys=True,)
