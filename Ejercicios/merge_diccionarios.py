# Como importar diccionarios en Python 3.5+

diccionario_x = {'nombre': 'Javier', 'Edad': 34, 'Ciudad': 'Santiago'}
diccionario_y = {'nombre': 'Claudia', 'Edad': 29}
merge_diccionarios = {**diccionario_x, **diccionario_y}
print(merge_diccionarios)
