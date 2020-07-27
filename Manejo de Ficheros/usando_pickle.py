import pickle

lista = [1, 2, 3, 4, 5]
fichero = open('lista.pckl', 'wb') #WB escritura en binario.
pickle.dump(lista,fichero)
fichero.close()

fichero = open('lista.pckl', 'rb') # Lectura Binaria
lista = pickle.load(fichero)
print(lista)

fichero.seek(0)
lista = pickle.load(fichero)
print(lista)
fichero.close()


class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


nombres = ["Hector", "Javier", "Maria"]

personas = []
for n in nombres:
    p = Persona(n)
    personas.append(p)

print(personas)

fichero = open('personas.pckl', 'wb')
pickle.dump(personas, fichero)
fichero.close()

fichero = open('personas.pckl', 'rb')
personas = pickle.load(fichero)
fichero.close()

for p in personas:
    print(p)