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


