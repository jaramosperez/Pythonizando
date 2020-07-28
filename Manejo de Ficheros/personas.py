from io import open

fichero = open('personas.txt', 'r', encoding='utf8')
lineas = fichero.readlines()
fichero.close()

personas = []

for linea in lineas:
    campos = linea.replace("\n", "").split(";")
    persona = {"id":campos[0], "Nombre": campos[1], "apellido": campos[2], "fecha_nacimiento": campos[3]}
    personas.append(persona)


for p in personas:
    print('(id={}) {} {} => {}'.format(p['id'], p['Nombre'], p['apellido'], p['fecha_nacimiento']))
