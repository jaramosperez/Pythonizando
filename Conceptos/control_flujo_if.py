# SENTENCIA IF (SI): Permite dividir el flujo de un programa en diferentes caminos.

if True:
    print('Se esta cumpliendo la condición')
    print('Se mostrará todo lo que esta dentro de este bloque')

a = 5
if a == 2:
    print('a vale 2')
if a == 5:
    print('a vale 5')

a = 5
b = 15
if a == 5:
    print('a vale', a)
    a *= 3
    if a == b:
        print('Ambos valores valen', b)


if a == 15 and b == 15:
    print('Los valores son los siguientes', a, ' y ', b)

# ELSE (SINO) Se encadena a un if para indicar el caso contrario cuando no se cumple la condición.
n = 111
if n % 2:
    print(n, ' Es un número par')
else:
    print(n, 'Es un número impar')


# ELIF (SINO SI) se encadena a un if para comprobar otra posible condición, siempre que la anterior no se cumpla.

comando = 'SALIR'
if comando == 'ENTRAR':
    print('Bienvenido al Sistema Pythonizado')
elif comando == 'SALUDAR':
    print('Hola amigo!, espero te guste Python')
elif comando == 'SALIR':
    print('Saliendo del sistema... te extrañaré')
else:
    print('El comando ingresado es erroneo, fin del universo')


nota = float(input('Ingresa una nota de 1 a 10: '))
if nota == 10:
    print('Perfecto')
elif nota >= 8:
    print('Sobresaliente')
elif nota >= 7:
    print('Notable')
elif nota >= 6:
    print('bien')
elif nota >= 5:
    print('suficiente')
else:
    print('Insuficiente, debes mejorar!')


nota1 = float(input('Ingresa una nota de 1 a 10: '))
if nota1 >= 9:
    print('Perfecto')
elif nota1 >= 8 and nota1 < 9:
    print('Sobresaliente')
elif nota1 >= 7 and nota1 < 8:
    print('Notable')
elif nota1 >= 6 and nota1 < 7 :
    print('bien')
elif nota1 >= 5:
    print('suficiente')
else:
    print('Insuficiente, debes mejorar!')
