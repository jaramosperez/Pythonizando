# LOS CONJUNTOS SON COLECCIONES DESORDENADAS DE ELEMENTOS UNICOS.
# SE UTILIZAN PARA HACER PRUEBAS DE PERTENENCIAS A GRUPOS.
# ELIMINACIÓN DE ELEMENTOS DUPLICADOS.
# SOPORTAN OPERACIONES MATEMATICAS AVANZADAS.
# NO PUEDE HABER DOS ELEMENTOS DUPLICADOS EN EL CONJUNTO.
# PODEMOS HACER USO DE LOS CONJUNTOS PARA ELIMINAR DUPLICADOS DE UNA LISTA

conjunto = set()
print(conjunto)

conjunto = {1, 2, 3}
print(conjunto)

conjunto.add(4)
print(conjunto)

conjunto.add(0)
print(conjunto)

conjunto.add('A')
print(conjunto)

conjunto.add('a')
print(conjunto)

conjunto.add('z')
print(conjunto)

conjunto.add('e')
print(conjunto)

grupo = {'Javier', 'Yanina', 'Claudia'}
print(grupo)

print('Yanina' in grupo)

prueba_repetidos = {'Javier', 'Javier', 'Javier', 'Javier'}
print(prueba_repetidos)

lista = [1, 2, 2, 3, 3, 3, 4, 5, 6, 7, 7]
print(lista)

conjunto_lista = set(lista)
print(conjunto_lista)

l = [1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 7, 7, 8, 9, 9]
print(l)
l = list(set(l))
print(l)

ultima = "No documentes el problema; arréglalo"
print(ultima)
set(ultima)
print(ultima)
