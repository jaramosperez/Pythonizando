#PASANDO ARGUMENTOS INDETERMINADOS. RETORNAN UNA TUPLA.
def indeterminados_posicion(*args):
    print(args)

indeterminados_posicion(5, "Python", [2, 3, 4, 5])

#PASANDO ARGUMENTOS INDETERMINADOS. RETORNAR CADA VALOR.
def indeterminados_posicion(*args):
    for arg in args:
        print(arg)

indeterminados_posicion(5, "Python", [2, 3, 4, 5])

# TRABAJAR CON DICCIONARIOS
def  indeterminados_nombre(**kwargs):
    print(kwargs)
indeterminados_nombre(c = "python", n = 7, l = [1, 2, 3])

# OTRO EJEMPLO
def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg)
indeterminados_nombre(c = "python", n = 7, l = [1, 2, 3])


# OTRO EJEMPLO
def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg, ' ', kwargs[kwarg])
indeterminados_nombre(c = "python", n = 7, l = [1, 2, 3])

# OTRO EJEMPLO
def super_funcion(*args, **kwargs):
    total = 0
    for arg in args:
        total += arg
    print('La sumatoria es igual a :', total)
    for karg in kwargs:
        print(karg, ' es ', kwargs[karg])

super_funcion(32,243,524,712,2, nombre='Bruce Wayne', nickname='Batman')
