from io import open
import pickle


class Personaje:

    def __init__(self, nombre, vida, ataque, defesa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defesa
        self.alcance = alcance

    def __str__(self):
        return "{} => {} de vida, {} de ataque, {} de defemsa, {} de alcance"


class Gestor:
    personajes = []

    def __init__(self):
        self.cargar()

    def agregar(self, p):
        for pTemporal in self.personajes:
            if pTemporal.nombre == p.nombre:
                return
            self.personajes.append(p)
            self.guardar()

    def borrar(self, nombre):
        for pTemporal in self.personajes:
            if pTemporal.nombre == nombre:
                self.personajes.remove(pTemporal)
                self.guardar()
                print("\nPersonaje {} borrado".format(nombre))
                return

    def mostrar(self):
        if len(self.personajes) == 0:
            print("El gestor esta vacio")
            return
        for p in self.personajes:
            print(p)

    def cargar(self):
        fichero = open('personajes.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.personajes = pickle.load(fichero)
        except:
            pass
        finally:
            fichero.close()
            print("Se ha cargado {} personajes".format(len(self.personajes)))

    def guardar(self):
        fichero = open('personajes.pckl', 'wb')
        pickle.dump(self.personajes, fichero)
        fichero.close()


# Realizamos las pruebas

G = Gestor()
G.mostrar()
G.agregar(Personaje("Caballero", 4, 2, 4, 2))
G.agregar(Personaje("Guerrero", 2, 4, 2, 4))
G.agregar(Personaje("Arquero", 2, 4, 1, 8))
G.mostrar()
G.borrar("Arquero")
G.mostrar()