# Ejercicio 2
# Realiza una función llamada area_circulo(radio) que devuelva el área de un círculo a partir de un radio.
# Calcula el área de un círculo de 5 de radio:
# Recordatorio
# El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi.
# Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math:
# Código
# import math
# print(math.pi)
import math
def area_circulo(radio):
    print('El area de un circulo con radio ', radio, 'es: ', (radio**2) * math.pi)

area_circulo(5)