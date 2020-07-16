# Ejercicio 7
# Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas,
# pero no debe repetirse ningún elemento en la nueva lista:

lista_1 = ["h", 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o']
lista_2 = ["h", 'o', 'l', 'a', ' ', 'l', 'u', 'n', 'a']
lista_3 = []
# Completa el ejercicio aquí
print(lista_1)
print(lista_2)
print(lista_1[1])

for i in range(len(lista_1)):
    if lista_1[i] not in lista_3:
        if lista_1[i] in lista_2:
            lista_3.append(lista_1[i])
print(lista_3)

