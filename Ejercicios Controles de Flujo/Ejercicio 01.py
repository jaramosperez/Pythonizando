# Ejercicio 1
# Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:
#
# Mostrar una suma de los dos números
# Mostrar una resta de los dos números (el primero menos el segundo)
# Mostrar una multiplicación de los dos números
# En caso de introducir una opción inválida, el programa informará de que no es correcta.

numero1 = float(input('Ingresa el primer número: '))
numero2 = float(input('Ingresa el segundo número: '))
print("""Selecciona que quieres hacer con los numeros ingresados
1) Sumar ambos números
2) Restar ambos números
3) Multiplicar ambos números""")
opcion = int(input('Ingresa la opción: '))
if opcion == 1:
    print('El resultado de la suma de ambos números es: ',numero1 + numero2)
elif opcion == 2:
    print('El resultado de la resta de ambos números es: ', numero1 - numero2)
elif opcion == 3:
    print('El resultado de la multiplicación es: ', numero1 * numero2)
else:
    print('Has ingresado una opción erronea')