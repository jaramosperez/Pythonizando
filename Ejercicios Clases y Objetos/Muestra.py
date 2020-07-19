class Pelicula:
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula", self.titulo)

    # Redefinimos el metodo String
    def __str__(self):
        return "{} lanzada en {} con una duración de {} minutos".format(self.titulo, self.lanzamiento, self.duracion)

    # Redefinimos el método Length
    def __len__(self):
        return self.duracion


class Catalogo:
    peliculas = []

    def __init__(self, peliculas=[]):
        self.peliculas = peliculas

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)

    def mostrar_catalogo(self):
        print("El Catalogo Contiene las siguientes preguntas:")
        for p in self.peliculas:
            print(p)


p = Pelicula("El Padrino", 175, 1972)
c = Catalogo([p])
c.agregar_pelicula(Pelicula("Interestelar", 2015, 280))
c.mostrar_catalogo()
