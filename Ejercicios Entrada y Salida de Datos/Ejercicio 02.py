# Ejercicio 2
# Crea un script llamado tabla.py que realice las siguientes tareas:
#
# Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.
# El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.
# En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.
# El script contendrá un bucle for que itere el número de veces del primer argumento.
# Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.
# Dentro del segundo for ejecuta una instrucción print(" * ", end=''), (end='' evita el salto de línea).
# Ejecuta el código y observa el resultado.
# Intenta deducir dónde y cómo añadir otra instruccion print() para dibujar una tabla.
# Recordatorio
#
# Recordatorio: Los argumentos se envían como cadenas separadas por espacios,
# si quieres enviar varias palabras como un argumento deberás indicarlas entre comillas dobles
# "esto es un argumento". Para capturar los argumentos debes utilizar el módulo sys y su lista argv:
#
#
# import sys
# print(sys.argv) # argumentos enviados
import sys

if len(sys.argv) == 3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])

    if filas < 1 or filas > 9 or columnas < 1 or columnas > 9:
        print("Error - Filas o columnas incorrectos")
        print("Ejemplo: tabla.py [1-9] [1-9]")
    else:
        # Aqui empieza la lógica
        for f in range(filas):
            print("")
            for c in range(columnas):
                print(" * ", end='')

else:
    print("Error - Argumentos incorrectos")
    print("Ejemplo: tabla.py [1-9] [1-9]")
