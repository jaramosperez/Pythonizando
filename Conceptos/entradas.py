# Si queremos convertir un dato obtenido con la funcion input() debemos hacer un cast.
decimal = float(input('Ingresa un número flotante: '))
print(decimal)

# Llenando una colección.
listado = []
print('Ingresa 5 letras')
for i in range(5):
    listado.append(input('Ingresa una letra: '))
print(listado)
