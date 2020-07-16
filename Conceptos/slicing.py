# SLICING
# EXTRAER TROZOS DE TEXTOS DE CADENAS
# UNA CADENA DE CARACTERES EN PYTHON ES INMUTABLE
# POR LO QUE NO SE PUEDE SUSTITUIR NINGUN DE SUS CARACTERES INDIVIDUALMENTE.


palabra = 'Python'
print(palabra[0:2])
# COMO FUNCIONA: EL PRIMER INDICE LE DICE DESDE DONDE COMIENZA Y EL SIGUIENTE CUANTOS MOSTRARA DESDE CONTANTO EL INICIO
print(palabra[:3])
print(palabra[2:])
# SI NO SE INDICA INDICE DE INICIO NI DE FIN TOMARÁ EL PRIMER Y ULTIMO INDICE

# Si no se inidican indices mostrará la cadena de texto completa
print(palabra[:])

# EJEMPLO DE CONCATENAR UNA CADENA COMPLETA
print("\nPalabra concatenada con la técnica de slicing")
print(palabra[:3] + palabra[3:])


# También se puede trabajar con números negativos.
print("\nComienzo desde una posición de un número negativo")
print(palabra[-2:])

# NO SE PUEDE TRABAJAR CON INDICES SUPERIORES A LA LONGITUD  DE LA CADENA.
# print(palabra[99])

# SE PUEDE USAR UN INDICE MAYOR PERO SOLO NOS MOSTRARÁ HASTA EL PUNTO DONDE LLEGUE LA CADENA.
print("Usando un Indice mayor al que contiene una cadena como final!")
print(palabra[:99])

# SE PUEDEN HACER USO DE OTRAS ESTRATEGIAS PARA MODIFICAR UNA CADENA DE CARACTERES.
print("Modificando una letra de la cadena")
palabra = 'W' + palabra[1:]
print(palabra)

# PARA FINALIZAR SE PUEDE CONOCER LA CANTIDAD DE CARACTERES DE UNA CADENA
print(len(palabra))

