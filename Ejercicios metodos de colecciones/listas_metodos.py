lista = [1, 2, 3, 4, 5]
lista.append(6)
print(lista)

lista.clear()
print(lista)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)
print(l1)

print(["Hola", "mundo", "mundo"].count("mundo"))

print(["Hola", "mundo", "mundo"].index("mundo"))

lista = [1, 2, 3]
lista.insert(0,0)
print(lista)

lista = [5, 10, 15, 25]
lista.insert(-1,20)
print(lista)

lista = [5, 10, 15, 25]
n = len(lista)
lista.insert(n, 30)
print(lista)

lista.insert(999, 35)
print(lista)

lista = [10, 20, 30, 40, 50]
print(lista.pop())
print(lista)

print(lista.pop(0))
print(lista)

lista.reverse()
print(lista)

lista = list("Hola Mundo")
lista.reverse()
cadena = "".join(lista)
print(cadena)

lista = [5, -10, 35, 0, -65, 100]
lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)