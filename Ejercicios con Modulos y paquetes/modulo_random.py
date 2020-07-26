import random

print(random.random())

print(random.uniform(1, 10))  # >= 1 y <10.0

print(random.randrange(10))  # >= 0 y <10.0

print(random.randrange(0, 101))

print(random.randrange(0, 101, 2))

c = "Hola mundo"

print(random.choice(c))

l = [1, 2, 3, 4, 5]
print(random.choice(l))

print(l)

random.shuffle(l)
print(l)

lista_de_dos = random.sample(l, 2)
print(lista_de_dos)
