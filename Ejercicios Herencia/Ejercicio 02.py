# Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehiculos.
# Realiza una función llamada catalogar() que reciba la lista de vehiculos y los recorra mostrando el nombre de su clase y sus atributos.
# Modifica la función catalogar() para que reciba un argumento optativo ruedas,
# haciendo que muestre únicamente los que su número de ruedas concuerde con el valor del argumento.
# También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:"
# únicamente si se envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.
# Recordatorio
#
# Puedes utilizar el atributo especial de clase name para recuperar el nombre de la clase de un objeto:
#
#
# type(objeto).__name__


class Vehiculo:

    def __init__(self, color, ruedas=0):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas)


class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "Color {}, {} ruedas, {}km y cilindrada de {}".format(self.color, self.ruedas, self.velocidad, self.cilindrada)


class Caminoneta(Coche):

    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return "Color {}, {} ruedas, {}km y cilindrada de {} y peso de {}".format(self.color, self.ruedas,
                                                                                self.velocidad, self.cilindrada,
                                                                                self.carga)


class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return "color {}, {} ruedas y de tipo {}".format(self.color, self.ruedas, self.tipo)


class Motocicleta(Bicicleta):

    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        Bicicleta.__init__(self, color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "color {}, {} ruedas y de tipo {} a {}km y cilindrada {}".format(self.color,
                                                                                self.ruedas,
                                                                                self.tipo,
                                                                                self.velocidad,
                                                                                self.cilindrada)


coche = Coche('Blanco', 4, 120, 1200)
camioneta = Caminoneta('Negra', 4, 100, 1000, 2000)
bicicleta = Bicicleta('Blanquita', 2, 'Urbana')
motocicleta = Motocicleta('Azul', 3, 'Deportiva', 150, 12000)
vehiculos = []
vehiculos.append(coche)
vehiculos.append(camioneta)
vehiculos.append(bicicleta)
vehiculos.append(motocicleta)

def catalogar(vehiculos,ruedas):
    #Primera parte del ejercicio
    if ruedas != None:
        contador = 0
        for vehiculo in vehiculos:
            if vehiculo.ruedas == ruedas:
                contador += 1
        print("\nSe han encontrado {} vehículos con {} ruedas:".format(
            contador, ruedas))

    # Segunda parte del ejercicio
    for vehiculo in vehiculos:
        if ruedas != None:
            print(type(vehiculo).__name__, vehiculo)
        else:
            if vehiculo.ruedas == ruedas:
                print(print(type(vehiculo).__name__, vehiculo))


catalogar(vehiculos, 2)
catalogar(vehiculos, 3)
catalogar(vehiculos, 2)
catalogar(vehiculos, 4)
catalogar(vehiculos, 0)