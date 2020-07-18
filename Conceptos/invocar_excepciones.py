# def mi_funcion(algo=None):
#     if algo is None:
#         print("Error! no se permite un valor nulo")
#
# mi_funcion()


def mi_funcion(algo=None):
    try:
        if algo is None:
            raise ValueError("Error! no se permite un valor nulo")
    except ValueError:
            print("Error! no se permite un valor nulo")

mi_funcion()
