# Ejercicio 2
# Utilizando operadores lógicos,
# determina si una cadena de texto introducida por el usuario
# tiene una longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiene con mostrar True o False).

cadena = input('Ingresa una cita o palabra que te guste: ')
print('La palabra o cita ingresada tiene mas de 3 caracteres y menos de 10? ', 3 < len(cadena) < 10)
