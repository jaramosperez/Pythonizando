# Ejercicio 1
# Localiza el error en el siguiente bloque de código.
# Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
# resultado = 10/0

try:
    print(resultado = 10 / 0)
except ZeroDivisionError:
    print("no se puede didivir por 0, intenta con otro numero")
except Exception as error:
    print(type(error).__name__)


