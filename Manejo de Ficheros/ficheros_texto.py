from io import open


texto = "Una linea de texto\nOtra linea de Texto"
fichero = open('fichero.txt', 'w')
fichero.write(texto)
fichero.close()
fichero = open('fichero.txt', 'r')
texto = fichero.read()
fichero.close()
print(texto)


