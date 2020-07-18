# Ejercicio 2
# Localiza el error en el siguiente bloque de código.
# Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
# lista = [1, 2, 3, 4, 5]
# lista[10]

lista = [1, 2, 3, 4, 5]
try:
    print(lista[10])
except IndexError:
    print("La lista no tiene tantos elementos, solo contienen un máximo de 4")
except Exception as error:
    print(type(error).__name__)