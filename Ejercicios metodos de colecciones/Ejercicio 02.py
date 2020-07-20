# Ejercicio 2
# Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:
#
# Borrar los elementos duplicados.
# Ordenar la lista de mayor a menor.
# Eliminar todos los números impares.
# Realizar una suma de todos los números que quedan.
# Añadir como primer elemento de la lista la suma realizada.
# Devolver la lista modificada.
# Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo,
# concuerda con el primer número de la lista, tal que así:
# Código
#
# nueva_lista = modificar(lista)
# print( nueva_lista[0] == sum(nueva_lista[1:]) )
# Resultado
# Recordatorio
#
# La función sum(lista) devuelve una suma de los elementos de una lista.
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

# Completa el ejercicio aquí

# Borrando duplicados, lo convierto en conjunto.
lista_copiada = list(set(lista))
print(lista_copiada)

# Ordenar la lista de mayor a menor.
lista_copiada.sort(reverse=True)
print(lista_copiada)

# Eliminar todos los números impares.
lista_pares = []
for numero in lista_copiada:
    if numero % 2 == 0:
        lista_pares.append(numero)

print(lista_pares)

# Realizar una suma de todos los números que quedan.
valor = sum(lista_pares)
print(valor)

# Añadir como primer elemento de la lista de pares la suma realizada
lista_pares.insert(0, valor)
print(lista_pares)
print(lista_pares[0] == sum(lista_pares[:1]))
