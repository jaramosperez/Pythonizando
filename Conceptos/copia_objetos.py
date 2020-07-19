from copy import copy


class Test:
    pass


test1 = Test()
test2 = test1

test1.algo = "Prueba"

print(test2 == test1)  # ¿Son el mismo objeto?

try:
    print(test2.algo)
except Exception as e:
    print(e)




class Test:
    pass

test1 = Test()
test2 = copy(test1)

test1.algo = "Prueba"

print(test2 == test1)  # ¿Son el mismo objeto?

try:
    print(test2.algo)
except Exception as e:
    print(e)


lista1 = [1,2,3]
lista2 = copy(lista1)
lista1 = None

print(lista1)
print(lista2)