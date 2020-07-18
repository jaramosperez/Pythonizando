# Ejercicio 6
# Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas.
# La primera con los números pares y la segunda con los números impares.
#
# Por ejemplo:
#
# Código
#
# pares, impares = separar([6,5,2,1,7])
# print(pares)
# print(impares)
# Resultado
# Sugerencia
#
# Para ordenar una lista automáticamente puedes utilizar el método .sort().


separar = ([6, 5, 2, 1, 7])
numeros = [-12, 84, 13, 20, -33, 101, 9]
separar.sort()
pares = []
impares = []


def separar_lista(lista):
    for n in lista:
        if (n % 2) == 0:
            pares.append(n)
        else:
            impares.append(n)

separar_lista(numeros)
print(pares)
print(impares)
