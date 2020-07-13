# Ejercicio 5
# La siguiente matriz (o lista con listas anidadas) debe cumplir una condición,
# y es que en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros.
# ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?

matriz = [
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]
# Completa el ejercicio aquí
valor_0 = sum(matriz[0][0:3])
valor_1 = sum(matriz[1][0:3])
valor_2 = sum(matriz[2][0:3])
valor_3 = sum(matriz[3][0:3])

matriz[1] = matriz[1][0:3]
matriz[1].append(valor_1)

matriz[3] = matriz[3][0:3]
matriz[3].append(valor_3)

print(matriz)

# Me costo mas de una hora resolverlo.
