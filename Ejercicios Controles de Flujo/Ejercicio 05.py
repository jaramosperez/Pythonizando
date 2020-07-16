# Ejercicio 5
# Realiza un programa que pida al usuario un número entero del 0 al 9,
# y que mientras el número no sea correcto se repita el proceso.
# Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
#
# Concepto útil
#
# La sintaxis [valor] in [lista] permite comprobar si un valor se encuentra en una lista (devuelve True o False).
valor = True
numeros = [1, 3, 6, 9]
while valor:
    numero = int(input('Ingresa un número entero entre 0 y 9: '))
    if numero in numeros:
        print('Tu numero se encuentra en el listado, has acertado')
        valor = False
    else:
        print('Tu número no esta dentro de la lista, intenta nuevamente.')
