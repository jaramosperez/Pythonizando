# FUNCIONES RECURSIVAS CON O SIN RETORNO.

def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print('Game over')
    print('Fin de la funcion: ', num)
cuenta_atras(10)

# FUNCION RECURSIVA CON RETORNO
def factorial(num):
    print('Valor del numero actualmente: ', num)
    if num > 1:
        num = num * factorial(num - 1)
        print('valor final ->', num)
    return num

print(factorial(8))