# Ejercicio 2
# Realiza un programa que lea un número impar por teclado.
# Si el usuario no introduce un número impar, debe repetise el proceso hasta que lo introduzca correctamente.

numero = 2
while(numero % 2 == 0):
    numero = int(input('Ingresa un numero: '))
    if numero % 2 != 0:
        print('Correcto! el número ', numero, ' es impar y has terminado!')
        break
    print('El numero ', numero, 'es par debe ingresar un numero impar para finalizar.')
