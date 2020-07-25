# Sublcase del diccionario y nos sirve para contar objetos.
# Para saber cuantos elemento se repiten en una lista, o la cantidad de caracteres de una listat
from collections import Counter

listado = [1, 1, 2, 2, 3, 4, 4, 4, 5, 5, 6, 6, 4]

print(Counter(listado))

p = "palabra"
print(Counter(p))

animales = "gato perro león león Gato gato canario perro oveja perro"

print(Counter(animales))


print(animales)
print(Counter(animales.split()))

c = Counter(animales.split())

# Metodo most_common para ver cual es el elemento que mas se repite podemos buscar el segundo o tercero ....
print(c.most_common(2))
print(c.most_common())

lista = {10, 20, 30, 40, 30, 30, 20, 40}

c = Counter(lista)

print(c.items())
print(c.keys())
print(c.values())

print(sum(c.values()))

print(dict(c))
print(set(c))