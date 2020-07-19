class Vehiculo:

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {} y ruedas {}".format(self.color, self.ruedas)


v = Vehiculo('Verde', 4)
print(v)


class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "El color es {} tiene {} ruedas, cuenta con una velocidad de {} km, y la cilindrada de {}".format(
            self.color, self.ruedas, self.velocidad, self.cilindrada
        )


c = Coche('Verde', 4, 150, '12')
print(c)