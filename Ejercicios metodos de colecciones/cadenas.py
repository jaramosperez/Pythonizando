print('Hola Mundo'.upper()) # Mayusculas
print('Hola Mundo'.lower()) # Minusculas
print('hola mundo'.capitalize()) # Primer caracter de la cadena en mayuscula
print('hola mundo'.title())# Mayusculas en el primer caracter de cada palabra
print('hola mundo'.count('mundo'))
print('hola mundo'.find('mundo'))  # Encontrar el indice donde comienza la palabra.
print('hola mundo mundo mundo'.rfind('mundo'))  # Encontrar el indice donde comienza la ultima palabra si esta repetida.
c = '1000'
print(c.isdigit())
c2 = "3q479y"
print(c2.isalnum())
print("ola mundo".islower())
print('     '.isspace())
print("Hola Mundo".startswith("Hola"))
print("Hola Mundo".endswith('Mundo'))
print('Hola Mundo desde Python!'.split())
print('hola,hola,hola,hola'.split(','))
print(",".join('Hola'))
print(' '.join('Hola mundo desde python'))
print('    hola estoy solito    '.strip(' '))
print('----hola estoy casi solito---'.strip('-'))
print('Hola Mundo desde java!'.replace('java', 'Python'))