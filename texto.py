# Cadena de caracteres
print('Hola Mundo')

# Se puede usar comillas dobles y simples, depende del contexto
print("Hola Mundo")

# Si queremos introducir dentro de la  cadena de caracteres comillas dobles comenzamos con comillas simples
print('Este text incluye unas comillas dobles " " ')

# También se puede utilizar en caso contrario
print("La siguiente 'palabra' esta dentro de comillas simples")

# CARÁCTERES DE ESCAPE PARA TEXTO
# \" COMILLA DOBLE DENTRO DE UNA CADENA CON COMILLAS DOBLES
print("Esta \"palabra\" esta dentro de comillas dobles")

# \' COMILLA SIMPLE DENTRO DE UNA CADENA CON COMILLAS SIMPLES
print("Esta \'palabra\' esta dentro de comillas dobles")

# \n 'SALTO DE LINEA
print('Este es una salgo de linea\nÁca comienza una nueva linea\nY áca otra mas')

# \t TABULACION
print('Esta es \tuna tabulacion')

# Cuando nos interese mostrar un directorio similar a los de windows C:\Carpeta\Usuario
print(r'C:\Carpeta\Usuario')
# A esto se le llama entregar una cadena de texto en bruto o raw.

# Otra forma de usar saltos de linea sin usar los caracteres de escape es usar el tripe """
print("""Esto es la primera linea
esto es la segunda linea
esto es \t una tabulacion
y esta es la última linea""")


# INDICES
# NOS PERMITE ACCEDER A CADA CARACTER DE UN CONJUNTO DE ELLOS POR EL INDICE QUE OCUPAN
# SE COMIENZA POR EL INDICE 0

palabra = "Python"
print("INDICES CORRELATIVOS\n")
print(palabra[0])  # Caracter de la posición 0 corresponderia a la letra P
print(palabra[1])  # Caracter de la posición 4 correspondería a la letra y
print(palabra[2])  # Caracter de la posición 4 correspondería a la letra t
print(palabra[3])  # Caracter de la posición 4 correspondería a la letra h
print(palabra[4])  # Caracter de la posición 4 correspondería a la letra o
print(palabra[5])  # Caracter de la posición 4 correspondería a la letra n

# LOS INDICES TAMBIÉN SE PUEDE TRABAJAR CON LOS NUMEROS EN NEGATIVOS
print("\nINDICES INVERTIDOS : \n")
print(palabra[-1])  # Caracter de la posición 4 correspondería a la letra n
print(palabra[-2])  # Caracter de la posición 4 correspondería a la letra o
print(palabra[-3])  # Caracter de la posición 4 correspondería a la letra t
print(palabra[-4])  # Caracter de la posición 4 correspondería a la letra h
print(palabra[-5])  # Caracter de la posición 4 correspondería a la letra y
print(palabra[-6])  # Caracter de la posición 4 correspondería a la letra p


