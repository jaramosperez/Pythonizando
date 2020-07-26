#Modulo que realiza cuatro operaciones matemáticas


def suma(a, b):
    try:
        resultado = a + b
    except TypeError:
        print("Ocurrio un error, Ingresaste un dato mal, debe ser solo números")
    else:
        return resultado


def resta(a, b):
    try:
        resultado = a + b
    except TypeError:
        print("Ocurrio un error, Ingresaste un dato mal, debe ser solo números")
    else:
        return resultado


def producto(a, b):
    try:
        resultado = a * b
    except TypeError:
        print(resultado)
    else:
        return resultado


def division(a, b):
    try:
        resultado = a / b
    except TypeError:
        print("Ocurrio un error, Ingresaste un dato mal, debe ser solo números")
    except ZeroDivisionError:
        print("Ocurrio un error, No existe la división por 0.")
    else:
        return resultado


