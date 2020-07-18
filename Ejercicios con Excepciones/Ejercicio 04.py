# Ejercicio 4
# Localiza el error en el siguiente bloque de código.
# Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
# resultado = 15 + "20"

try:
    resultado = 15 + "20"
    print(resultado)
except TypeError:
    print("No se pueden operar un entero con una cadena de caracteres, intenta poner dos numeros")
except Exception as error:
    print(type(error).__name__)
