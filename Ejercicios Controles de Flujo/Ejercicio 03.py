# Ejercicio 3
# Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100.
#
# Sugerencia
#
# Puedes utilizar la funciones sum() y range() para hacerlo más fácil.
# El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números, pruébalo.

# UNA DE LAS FORMAS DE HACERLO
numero = []
for i in range(0, 102, 2):
    numero.append(i)
print(sum(numero))

# OTRA FORMA DE HACERLO
suma = sum(range(0, 101, 2))
print(suma)
