# CONSEGUIR EL TIPO  DEL ERROR FACILITA SOLUCIONAR EL PROBLEMA.
try:
    n = input("Introduce un número: ")
    5/n
except Exception as error:
    print(type(error).__name__)

# CONSEGUIR EL TIPO  DEL ERROR FACILITA SOLUCIONAR EL PROBLEMA.
try:
    n = float(input("Introduce un número: "))
    5/n
except TypeError:
    print("No se puede divivir un numero por una letra o palabra")
except ValueError:
    print("Debes ingresar un numero")
except ZeroDivisionError:
    print("no se puede didivir por 0")
except Exception as error:
    print(type(error).__name__)