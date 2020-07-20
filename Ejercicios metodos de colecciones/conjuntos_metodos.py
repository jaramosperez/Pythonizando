c = set()
c.add(1)
c.add(2)
c.add(3)
print(c)
c.discard(1)
print(c)

# Cuando se pasan por referencia los valores se borran en el original.
c1 = {1, 2, 3, 4}
c2 = c.copy()
print(c1, c2)
c2.discard(4)
print(c1, c2)

# Limpiar un conjunto
c2.clear()
print(c2)

# COMPARACION DE CONJUNTOS.
c1 = {1, 2, 3}
c2 = {3, 4, 5}
c3 = {-1, 99}
c4 = {1, 2, 3, 4, 5}

c1.isdisjoint(c3)
print(c1)
print(c2)

c3.issubset(c4)
c3.issuperset(c1)

# Métodos avanzados

c1 = {1,2,3}
c2 = {3,4,5}
c3 = c1.union(c2)
print(c1, "+", c2, "=", c3)

c1.update(c2)
print(c1)

c1 = {1,2,3}
c2 = {3,4,5}

print(c1.difference(c2))
c1.difference_update(c2)
print(c1)

c1 = {1,2,3}
c2 = {3,4,5}

print(c1.intersection(c2))

c1.intersection_update(c2)
print(c1)

c1 = {1, 2, 3}
c2 = {3, 4, 5}

print(c1.symmetric_difference(c2))