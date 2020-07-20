colores = { "amarillo":"yellow", "azul":"blue", "verde":"green" }

print(colores.get('Negro'))

print(colores.keys())
print(colores.values())

colores.items()

for clave, valor in colores.items():
    print(clave, valor)

print(colores.pop("amarillo", "no se ha encontrado"))
print(colores.pop("Negro", "no se ha encontrado"))

colores.clear()
print(colores)