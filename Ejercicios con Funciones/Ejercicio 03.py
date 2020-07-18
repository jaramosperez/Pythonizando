# Ejercicio 3
# Realiza una función llamada relacion(a, b) que a partir de dos números cumpla lo siguiente:
#
# Si el primer número es mayor que el segundo, debe devolver 1.
# Si el primer número es menor que el segundo, debe devolver -1.
# Si ambos números son iguales, debe devolver un 0.
# Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'.
def relacion(n1,n2):
    if n1>n2:
        print('1')
    elif n1<n2:
        print('-1')
    else:
        print('0')

relacion(5, 10)
relacion(10, 5)
relacion(5, 5)