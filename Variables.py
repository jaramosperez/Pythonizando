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
