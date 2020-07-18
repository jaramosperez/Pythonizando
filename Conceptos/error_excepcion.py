# Errores de sintaxis (fijarnos en parentesis)
# print('Hola'  #Falta cerrar el parentesis

# NameError (escribimos mal el nombre de una funcion o metodo)
# pint('hola')

# ERRORES SEMANTICOS
# lista = [1, 2, 3]
# lista.pop()
# lista.pop()
# lista.pop()
# print(lista)
# lista.pop()  # IndexError, pues la lista ya se encuentra vacia y no puede sacar nada.
# lista = [1, 2, 3]
# if len(lista) > 0:
#     lista.pop()
#     print(lista)


# TypeError No podemos operar un str con un int
# ValueError no se puede convertir un string en float.
# n = input("Introduce un número: ")
# m = 4
# print("{}/{}={}".format(n, m, n / m))
# try:
#     n = float(input("Introduce un número: "))
#     m = 4
#     print("{}/{}={}".format(n, m, n / m))
# except:
#     print("Ha ocurrido un error, introduce un numero.")

while True:
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{}={}".format(n, m, n / m))
    except:
        print("Ha ocurrido un error, introduce un numero.")
    else:
        print("Todo a funcionado perfectamente")
        break  # Importante romper la iteracion si todo sale bien.
    finally:
        print('Fin de la iteración')