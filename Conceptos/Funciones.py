# LAS FUNCIONES SON FRAGMENTOS DE CÓDIGO QUE SE PUEDE EJECUTAR MULTIPLES VECES.
# PUEDEN RECIBIR Y DEVOLVER INFORMACION PARA COMUNICARSE CON EL PROCESO QUE LOS LLAMO.
# EJEMPLO 01


def saludar():
    print("Hola desde python!")


saludar()


# EJEMPLO 02
def dibujar_tabla_del_7():
    for i in range(11):
        print("7 * ", i, "= ", i * 7)


dibujar_tabla_del_7()

# Ejemplo 03
m = 10


def test():
    print(m + 1)


test()


# EJEMPLO 04
def test1():
    print(l)


l = 10
test1()


# EJEMPLO 05
def test2():
    o = 5
    print(o)


test2()
o = 10
test2()
print(o)


# EJEMPLO 06
def test3():
    return "Una cadena retornada"

test3()
print(test3())


# EJEMPLO 07
def test4():
    return [1, 2, 3, 4]

print(test4())


# EJEMPLO 08
def test5():
    return "hola", 44, [1, 2]

print(test5())


# ENVIO DE VALORES
def suma(a,b):
    return a+b
r = suma(4,9)
print(r)
