# EJERCICIO 01
# Crea una clase llamada Punto con sus dos coordenadas X e Y.
# Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será cero.
# Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
# Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto,
# teniendo en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y,
# si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.
# Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.
# (Optativo) Añade un método llamado distancia,
# que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla.
# La fórmula es la siguiente:
import math


class Punto:
    coordenada_x = 0
    coordenada_y = 0
    vector_x = 0
    vector_y = 0

    # Método Constructor
    def __init__(self, x=0, y=0):
        self.coordenada_x = x
        self.coordenada_y = y

    # Sobreescribir el metodo string
    def __str__(self):
        return "el punto es ({},{})".format(self.coordenada_x,self.coordenada_y)

    def cuadrante(self):
        if self.coordenada_x > 0 and self.coordenada_y > 0:
            print("El punto ({},{}) se sitúa en el primer cuadrante".format(self.coordenada_x, self.coordenada_y))
        elif self.coordenada_x < 0 and self.coordenada_y > 0:
            print("El punto ({},{}) se sitúa en el segundo cuadrante".format(self.coordenada_x, self.coordenada_y))
        elif self.coordenada_x < 0 and self.coordenada_y < 0:
            print("El punto ({},{}) se situa en el tercer cuadrante".format(self.coordenada_x, self.coordenada_y))
        elif self.coordenada_x > 0 and self.coordenada_y < 0:
            print("El punto ({},{}) se situa en el cuarto cuadrante".format(self.coordenada_x, self.coordenada_y))
        else:
            print("está sobre el origen")

    def vector(self, punto):
        a = (punto.coordenada_x - self.coordenada_x)
        b = (punto.coordenada_y - self.coordenada_y)
        print("El punto del vector es ({},{})".format(a, b))

    def distancia(self, punto):
        a = (punto.coordenada_x - self.coordenada_x)**2
        b = (punto.coordenada_y - self.coordenada_y)**2
        distancia = math.sqrt(a + b)
        print("la distancia es {}".format(distancia))


a = Punto(2, 3)
b = Punto(5, 5)
c = Punto(-3, -1)
d = Punto(0, 0)

print("Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.")
print(str(a))
print(str(b))
print(str(c))
print(str(d))
print("Consulta a que cuadrante pertenecen el punto A, C y D")
a.cuadrante()
c.cuadrante()
d.cuadrante()
print("Consulta los vectores AB y BA.")
a.vector(b)
b.vector(a)
print("Consulta la distancia entre los puntos 'A y B' y 'B y A'.")
a.distancia(b)
b.distancia(a)
print("Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto")
a.distancia(d)
b.distancia(d)
c.distancia(d)
