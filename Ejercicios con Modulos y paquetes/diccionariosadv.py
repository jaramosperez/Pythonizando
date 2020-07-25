
# No es necesario que todos los elementos de un diccionario sean del mismo tipo
# Cuando creamos un diccionario y le vamos pasando valores para llenarlo
# al mostrar el contenido del diccionario se muestra en un orden aleatoreo.
from collections import OrderedDict, namedtuple

n = OrderedDict()
n['uno'] = 'one'
n['dos'] = 'two'
n['tres'] = 'three'
print(n)

n1 = {'uno': 'one', 'dos': 'two', 'tres': 'three'}

n2 = {'tres': 'three', 'uno': 'one', 'dos': 'two'}

print('Sin OrderedDirect', n1 == n2)

# En los diccionarios ordenados si se tiene en cuenta el orden, y se consideran objetos distintos.
n1 = OrderedDict()
n1['uno'] = 'one'
n1['dos'] = 'two'
n1['tres'] = 'three'

n2 = OrderedDict()
n2['uno'] = 'one'
n2['dos'] = 'two'
n2['tres'] = 'three'

print('Con OrderedDict', n1 == n2)

# TUPLAS Recordar que esto no se puede cambiar, queda tal cual.

Persona = namedtuple('Persona', 'nombre apellido edad nickname')
p = Persona(nombre="Javier", apellido='Ramos', edad=34, nickname='ZoDuX')
print(p.nombre, p.apellido, p.edad, p.nickname)
print(p[0])
print(p[1])
print(p[-1])