# UN OBJETO ES UNA INSTANCIA DE UNA CLASE.
class Galleta:
    chocolate = False

    def __init__(self, sabor=None, color=None):
        self.sabor = sabor
        self.color = color
        if sabor is not None and color is not None:
            print("Se acaba de crear una galleta {} y {}".format(sabor, color))
        else:
            print("No se ha podido crear la galleta, necesita especificar el sabor y color")

    def chocolatear(self):
        self.chocolate = True

    def tiene_chocolate(self):
        if(self.chocolate):
            print("Soy una galleta chocolateada!")
        else:
            print("Soy una galleta sin chocolate")


g = Galleta("Menta", "Verde")


class Pelicula:
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula", self.titulo)

    # Destructor de clase
    def __del__(self):
        print("Se ha borrado la pelicula", self.titulo)

    # Redefinimos el metodo String
    def __str__(self):
        return "{} lanzada el en {} con una duración de {} minutos".format(self.titulo, self.lanzamiento, self.duracion)

    # Redefinimos el método Length
    def __len__(self):
        return self.duracion


p = Pelicula("El Padrino", 175, 1972)
print(len(p))
print(str(p))
print(p)
