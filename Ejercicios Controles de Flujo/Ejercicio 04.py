# Ejercicio 4
# Realiza un programa que pida al usuario cuantos números quiere introducir.
# Luego lee todos los números y realiza una media aritmética.

indice = 0
suma = 0
media = 0
numeros = int(input('Ingrese la canitdad de numero que desea Ingresar: '))
while numeros > indice:
    numero = int(input('Ingrese un numero: '))
    suma += numero
    indice += 1
print('La media aritmetica es: ', suma / numeros)




suma = 0
num = int(input('Ingrese la cantidad de numeros a ingresar: '))
for i in range(0, num):
    numero = int(input('Ingrese un numero: '))
    suma += numero
    print(suma)
print(suma / num)