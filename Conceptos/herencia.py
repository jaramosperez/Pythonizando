class Producto:
    def __init__(self, referencia, tipo, nombre,
                 pvp, descripcion, productor=None,
                 distribuidor=None, isbn=None, autor=None):
        self.referencia = referencia
        self.tipo = tipo
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
        self.productor = productor
        self.distribuidor = distribuidor
        self.isbn = isbn
        self.autor = autor


adorno = Producto('000A', 'ADORNO', 'Vaso Adornado', 15,
                  'Vaso de porcelana con dibujos')

print(adorno)
print(adorno.tipo)


class Producto:
    def __init__(self, referencia, nombre, pvp, descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion

    def __str__(self):
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t {self.pvp}\n" \
               f"DESCRIPCIÓN\t {self.descripcion}\n"


class Adorno(Producto):
    pass


adorno = Adorno(2034, "Vaso adornado", 15, "Vaso de porcelana")
print(adorno)


class Alimento(Producto):
    productor = ""
    distribuidor = ""

    def __str__(self):
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t {self.pvp}\n" \
               f"DESCRIPCIÓN\t {self.descripcion}\n" \
               f"PRODUCTOR\t\t {self.productor}\n" \
               f"DISTRIBUIDOR\t\t {self.distribuidor}\n"


class Libro(Producto):
    isbn = ""
    autor = ""

    def __str__(self):
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t {self.pvp}\n" \
               f"DESCRIPCIÓN\t {self.descripcion}\n" \
               f"ISBN\t\t {self.isbn}\n" \
               f"AUTOR\t\t {self.autor}\n"


alimento = Alimento(2035, "Botella de Aceite de Oliva", 5, "250 ML")
alimento.productor = "La Aceitera"
alimento.distribuidor = "Distribuciones SA"
print(alimento)

libro = Libro(2036, "Cocina Mediterránea", 9, "Recetas sanas y buenas")
libro.isbn = "0-123456-78-9"
libro.autor = "Doña Juana"
print(libro)

productos = [adorno, alimento]
productos.append(libro)

print(productos)

for producto in productos:
    print(producto, "\n")

for producto in productos:
    print(producto.referencia, producto.nombre)

# for producto in productos:       Esto genera error pues no todos los productos cuentan con el atributo autor.
#     print(producto.autor)


# Por suerte podemos hacer una comprobación con la función isinstance()
# para determinar si una instancia es de una determinado clase y así mostrar unos atributos u otros:

for producto in productos:
    if (isinstance(producto, Adorno)):
        print(producto.referencia, producto.nombre)
    elif (isinstance(producto, Alimento)):
        print(producto.referencia, producto.nombre, producto.productor)
    elif (isinstance(producto, Libro)):
        print(producto.referencia, producto.nombre, producto.isbn)

def rebajar_producto(producto, rebaja):
    producto.pvp = producto.pvp - (producto.pvp/100 * rebaja)

print(alimento, "\n")
rebajar_producto(alimento, 10)
print(alimento)