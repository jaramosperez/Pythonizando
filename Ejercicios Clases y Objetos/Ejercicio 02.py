# Crea una clase llamada Rectangulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.
# Añade un método constructor para crear ambos puntos fácilmente,
# si no se envían se crearán dos puntos en el origen por defecto.
# Añade al rectángulo un método llamado base que muestre la base.
# Añade al rectángulo un método llamado altura que muestre la altura.
# Añade al rectángulo un método llamado area que muestre el area.


class Rectangulo:
    inicial = 0
    final = 0

    def __init__(self, inicial=0, final=0):
        self.inicial = inicial
        self.final = final

    def base(self):
        print("La base del rectangulo es: {}".format(self.inicial))

    def altura(self):
        print("La altura del rectangulo es: {}".format(self.final))

    def area(self):
        print("El área del rectangulo es: {}".format(self.inicial*self.final))


r = Rectangulo(3, 2)
r.base()
r.altura()
r.area()