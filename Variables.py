# Asignación de un valor a una variable.
# Una variable es un espacio en memoria que almacena algún tipo de dato.
# No puede comenzar por un numero
# No puede contener espacios
# Tampoco puede contener simbolos especiales (áéñ?'¿!)
# Podemos utilizar _ para separar palabraas.
# UNA BUENA PRÁCTICA ES USAR LOS NOMBRES EN MINUSCULAS.

print('Muestra de variables numéricas', '\n')
primer_numero = 3
print(primer_numero)
segundo_numero = 39
print(segundo_numero, '\n')  # La expresión '\n' permmite realizar un salto de linea.

# Variable numéricas, se puede operar entre si.
resultado_suma = primer_numero + segundo_numero
resultado_resta = segundo_numero - primer_numero
resultado_multiplicacion = primer_numero * segundo_numero
resultado_potencia = primer_numero ** segundo_numero

# Se puede mostrar los resultado almacenados en una variable
# O se puede mostrar el resultado de la operacion sin almacenar

print('Resultados  de operaciones de variables numéricas', '\n')
print(resultado_suma)
print(primer_numero + segundo_numero)
print(resultado_resta)
print(segundo_numero - primer_numero)
print(resultado_multiplicacion)
print(primer_numero * segundo_numero)
print(resultado_potencia)
print(primer_numero ** segundo_numero)

# Al trabajar con las reglas de precedencia siempre tener que indicar parentesis entre los numeros a operar
promedio = (primer_numero + segundo_numero) / 2
print('El promedio entre 3 y 39 es: ', promedio)

# TRABAJAR VARIABLES CON CADENAS DE TEXTO

# Asignación de una cadena de caracteres a una variable
cadena = 'Esto es una cadena de caracteres\nCon dos lineas'
print(cadena)

# Concatenación o Suma de Cadenas.
segunda_cadena = '\nEsto continua el texto anterior '
print(cadena + segunda_cadena)

# Se pueden contenar cadenas de caracteres sin usar el operador + siempre que no se incluyan variables
# solo se permiten cadenas puras
# NO FUNCIONA CON VARIABLES
print("Esta cadena" " es parte " "de un ejemplo de " "concatenación de " "text")

# Siguiente el ejemplo anterior se puede almacenar esa cadena en una variable y mostrarla
concatenar_texto = "Esta cadena" " es parte " "de un ejemplo de " "concatenación de " "text"
print(concatenar_texto)

# Se pueden multiplicar cadenas por ejemplo necesitar varios espacios
diez_espacios = " " * 10
print(diez_espacios, 'Antes de iniciar este texto hay diez espacios')
