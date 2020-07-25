
# No es necesario que todos los elementos de un diccionario sean del mismo tipo
# Cuando creamos un diccionario y le vamos pasando valores para llenarlo
# al mostrar el contenido del diccionario se muestra en un orden aleatoreo.
from collections import OrderedDict
n = OrderedDict()
n['uno'] = 'one'
n['dos'] = 'two'
n['tres'] = 'three'
print(n)

n1 = {}
n1['uno'] = 'one'
n1['dos'] = 'two'
n1['tres'] = 'three'

n2 = {}
n2['tres'] = 'three'
n2['uno'] = 'one'
n2['dos'] = 'two'


print(n1 == n2)

# En los diccionarios ordenados si se tiene en cuenta el orden, y se consideran objetos distintos.
n1 = OrderedDict()
n1['uno'] = 'one'
n1['dos'] = 'two'
n1['tres'] = 'three'

n2 = OrderedDict()
n2['dos'] = 'two'
n2['tres'] = 'three'
n2['uno'] = 'one'
print(n1 == n2)
