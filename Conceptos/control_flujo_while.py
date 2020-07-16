# ¿QUE ES LA ITERACION?
# Iterar es realizar una determinada acción varias veces.
# Cada vez que se repite la acción se denomina iteración.
# LA MAGIA DE LAS ITERACIONES.
# Para encontrar un elemento, la computadora debe recorrer los registros
# y compararlos hasta encontrar el que se buscar.

#SENTENCIA WHILE (MIENTRAS)
# Se basa en repetir un bloque a partir de evaluar una condición lógica, siempre que ésta sea True.
# Nosotros como programadores, debemos planificar un momento en que la condición cambie a False y Finalice.
# Si no tiene una indicación las iteraciones no terminarian y entrariamos en un loop infinito.

# EJEMPLO 01
c = 0
while c <= 5:
    c += 1
    print('c Vale', c)
else:
    print('Se han completado las iteraciones y el valor final para c es: ', c)

#EJEMPLO 02
numero = 0
while numero <= 10:
    numero += 1
    if (numero == 4):
        print('Se rompe la iteración en: ', numero)
        break
    print('Numero vale: ', numero)
else:
    print('Se ha completado la iteracion hasta el final con ', numero)

# EJEMPLO 03
otro_numero = 0
while otro_numero <= 10:
    otro_numero += 1
    if (otro_numero == 4):
        print('Continuamos con las iteraciones ', otro_numero)
        continue
    print('Numero vale: ', otro_numero)
else:
    print('Se ha completado la iteracion hasta el final con ', otro_numero)


# EJEMPLO 04
print("Bienvenido al menú interactivo")
while(True):
    print("""¿Qué quieres hacer? Escribe el número de la opción
    1) Quiero que me saludes
    2) Quiero que me muestres los numeros del 1 al 10
    3) Quiero irme a mi casa.""")
    opcion = int(input('Ingresa el número de la opción'))
    if opcion == 1:
        print('Hola estimado!, espero que te guste Python\n')
    elif opcion == 2:
        n = 0
        while(n <= 10):
            print(n)
            n += 1
    elif opcion == 3:
        print('Hasta la vista Baby!')
        break
    else:
        print('Has seleccionado mal el comando, intentan nuevamente')
