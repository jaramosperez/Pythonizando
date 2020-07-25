# Sublcase del diccionario y nos sirve para contar objetos.
# Para saber cuantos elemento se repiten en una lista, o la cantidad de caracteres de una listat
from collections import Counter

listado = [1, 1, 2, 2, 3, 4, 4, 4, 5, 5, 6, 6, 4]

print(Counter(listado))

p = "palabra"
print(Counter(p))
