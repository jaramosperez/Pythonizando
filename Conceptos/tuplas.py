# LAS TUPLAS SON COLECCIONES SIMILARES A LAS LISTAS CON LA DIFERENCIA QUE ESTAS SON INMUTABLES.
# NOS SIRVEN PARA ASEGURARNOS QUE CIERTOS DATOS NO SE PUEDAN MODIFICAR.
tupla = (100, "Hola", [1, 2, 3], -50)
print(tupla)
print(tupla[1])
print(tupla[2][1])
print(len(tupla))

# Podemos buscar con index en la tupla, pero entregará un error si no  lo encuentprra
print(tupla.index('Hola'))

# Podemos usar count para buscar elementos repetidos
tupla_repetida = (10, 10, 10, 20, 20, 50, 70, 40, 100)
print(tupla_repetida.count('algo'))

# NO ACEPTA EL METODO APPEND. PUES NO SE PUEDE MODIFICAR LA TUPLA.