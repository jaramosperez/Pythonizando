# LOS DICCIONARIOS Y LAS LISTAS SON LAS COLECCIONES DE DATOS MAS UTILIZADOS
# SE BASAN EN UNA ESTRUCTURA MAPEADA
# CADA ELEMENTO DE LA COLECCION ESTA IDENTIFICADO CON CLAVE ÚNICA.
# NO PUEDEN HABER DOS CLAVES IGUALES EN EL MISMO DICCIONARIO.
# EN OTROS LENGUAJES SE LES PODRIAN LLAMAR ARREGLOS ASOCIATIVOS.
# SI SE PUEDEN MODIFICAR LOS REGISTROS DE UN DICCIONARIO.
vacio = {}
print(vacio)
print(type(vacio))
colores = {'Amarillo': 'Yellow', 'Rojo': 'Red', 'Azul': 'Blue', 'Gris': 'Grey'}
print(colores)
print(colores['Rojo'])
colores['Amarillo'] = 'yellow'
print(colores)
# Eliminacion de Clave y valor
del(colores['Amarillo'])
print(colores)
# Asignación directa
edades = {'Javier': 34, 'Claudia': 29, 'Yanina': 29}
print(edades)
edades['Javier'] += 1
print(edades)

# Se pueden sumar
print(edades['Javier'] + edades['Claudia'])

# Operando con Ciclo FOR
for edad in edades:
    print(edades[edad])
for edad in edades:
    print(edad)
for edad in edades:
    print(edad, edades[edad])

# Otra forma mas correcta
for nombre, edad in edades.items():
    print(nombre, edad)

# OTRO EJEMPLO
personajes = []
p = {'Nombre': 'Bruno Diaz', 'NickName': 'Batman', 'Ciudad': 'Gotica'}
personajes.append(p)
print(personajes)
p = {'Nombre': 'Matt Murdock', 'NickName': 'Daredevil', 'Ciudad': 'Nueva York'}
personajes.append(p)
print(personajes)
p = {'Nombre': 'Clark Kent', 'NickName': 'Superman', 'Ciudad': 'Metrópolis'}
personajes.append(p)
print(personajes)

for personaje in personajes:
    print(personaje['Nombre'], personaje['NickName'], personaje['Ciudad'])

