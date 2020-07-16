#LA SETENCIA FOR (PARA)
# Puede hacer recorridos mas eficientes en codigo de listas.

#Ejemplo de Comparación con while.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
indice = 0
while(indice < len(numeros)):
    print(numeros[indice])
    indice += 1


#Ahora con FOR
for numero in numeros:
    print(numero)

#EJEMPLO
indice = 0
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    numeros[indice] *= 3
    indice += 1
print(numeros)

# EJEMPLO MEJORANDO EL ANTERIOR
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for indice, numero in enumerate(numeros):
    numeros[indice] *= 4
print(numeros)

# Otra forma de usar el for
for i in range(10):
    print(i)

