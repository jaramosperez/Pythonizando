v = 'otro texto'
n = 10
print('un texto', v, ' y un numero ', n)
c = "Un texto '{}' y un número '{}'".format(v, n)
print(c)

print("Un texto '{}' y un numero '{}'".format(v, n))

print("Un texto '{texto}' y un número '{numero}'".format(texto=v, numero=n))

print("{:>30}".format('palabra')) # Aliniamiento a la derecha
print("{:30}".format('palabra')) # Aliniamiento a la izquierda
print("{:^30}".format('palabra')) # Aliniamiento al centro.

# TRUNCAR
print("{:.3}".format('palabra'))
print("{:^30.4}".format('palabra')) # Aliniamiento al centro.

# formateo de numeros enteros.
print('{}'.format(10))
print('{}'.format(100))
print('{}'.format(1000))

print('{:4d}'.format(10))
print('{:4d}'.format(100))
print('{:4d}'.format(1000))
# Rellenar con 0.
print('{:04d}'.format(10))
print('{:04d}'.format(100))
print('{:04d}'.format(1000))

# Formateo de números flotantes, rellenados con espacios
print('{:8.3f}'.format(3.1415926))
print('{:8.3f}'.format(1333.1))

print('{:08.3f}'.format(3.1415926))
print('{:08.3f}'.format(1333.1))
