# Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos
# (es suficiene con mostrar True o False):
#
# Si los dos números son iguales
# Si los dos números son diferentes
# Si el primero es mayor que el segundo
# Si el segundo es mayor o igual que el primero

a = float(input('Ingrese un número: '))
b = float(input('Ingrese otro número: '))
print('Los numeros son iguales: ', a == b)
print('Los números son diferentes', a != b)
print('El primero es mayor que el segundo', a > b)
print('El segundo numero es mayor o igual al primero', b >= a)
