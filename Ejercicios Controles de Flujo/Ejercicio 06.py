# Ejercicio 6
# Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:
#
# Todos los números del 0 al 10 [0, 1, 2, ..., 10]
# Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
# Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
# Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
# Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
# Concepto útil
#
# Se pueden generar saltos en el range() estableciendo su tercer parámetro range(inicio, fin, salto), experimenta.

numeros = []
for i in range(0, 11, 1):
    numeros.append(i)
print(numeros)

numeros = []
for i in range(-10, 1, 1):
    numeros.append(i)
print(numeros)

numeros = []
for i in range(0, 21, 2):
    numeros.append(i)
print(numeros)


numeros = []
for i in range(-19, 0, 2):
    numeros.append(i)
print(numeros)

numeros = []
for i in range(0, 55, 5):
    numeros.append(i)
print(numeros)