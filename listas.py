# EN PYTHON EXISTEN LAS LISTAS DE DATOS COMO EN EL RESTO DE LOS LENGUAJES.
# PERO ESTAS PUEDEN CONTENER DENTRO DE ELLAS DIFERENTES TIPOS DE DATOS
# NO ES NECESARIO QUE SEAN DEL MISMO TIPO DE DATO.

# Podemos tener una lista numérica
numeros = [1, 2, 3, 4]
print("Cadena Numérica")
print(numeros)

# Podemos tener una lista con diferentes tipos de datos.
datos = [3, "una cadena de texto", -32, 3.14, "otra cadena"]
print("Cadena con diferentes tipos de datos")
print(datos)

# LAS LISTAS TAMBIEN PERMITEN USAR EL INDICE Y EL SLICING
print("Muestra el item en la posición 4")
print(datos[4])

# EJEMPLO DEL SLICING

print(datos[-2:])

# TAMBIÉN SE PUEDEN CONCATENAR LAS LISTAS CON OTRAS.
nueva_lista = numeros + [5, 6, 7, 8]
print(nueva_lista)
# LAS LISTAS A DIFERENCIA DE LAS CADENAS DE CARACTERES SI SON MUTABLES.
# POR LO QUE PODEMOS ASIGNAR UN NUEVO ITEM EN UN INDICE YA OCUPADO.
# EJEMPLO
pares = [0, 2, 4, 5, 8, 9]
print("Dejar solo numeros pares")
pares[3] = 6
pares[5] = 10
print("Solo números pares")
print(pares)

# LAS LISTAS TIENEN METODOS QUE PERMITEN TRABAJARLAS UNO DE ELLOS ES
# append = el cual permite agregar un item al final de la lista.
pares.append(12)
print("Esta es la nueva lista con un item agregado con append\n", pares)
# append  = permite agregar un resultado de una operacion directamente
pares.append(7+7)
print("Esta es la nueva lista con otro item agregado con append\n", pares)

# Ejemplo de reemplazos de letras minúsculas por mayúsculas en un listado de letras del abcdario
abecedario = ['a', 'b', 'c', 'd', 'e', 'f']
print(abecedario)
# Reemplazo
abecedario[:3] = ['A', 'B', 'C']
print('Abecedario reemplazado\n', abecedario)

# También podemos borrar items de una lista
abecedario[:3] = []
print("abecedario sin las tres primeras letras\n", abecedario)
# Borrado completo de una lista
abecedario = []
print("Lista vaciada\n", abecedario)

#La funcion len tambien funciona en las listas
print(len(abecedario))

# LISTAS ENLAZADAS
# Una lista puede contener varias listas.
# Se puede acceder a sus items de la misma forma que en las cadenas de texto.
# EJEMPLO
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
r = [a, b, c]

# Acceder a la segunda lista completa
print("Segunda lista completa\n", r[1])
print("el número en la pocición 1 de la lista 2 es: ", r[2][0])
