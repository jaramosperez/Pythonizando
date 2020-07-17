# Ejercicio 2
# Durante el desarrollo de un pequeño videojuego se te encarga configurar y balancear cada clase de personaje jugable.
# Partiendo que la estadística base es 2, debes cumplir las siguientes condiciones:
#
# El caballero tiene el doble de vida y defensa que un guerrero.
# El guerrero tiene el doble de ataque y alcance que un caballero.
# El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance.
# Muestra como quedan las propiedades de los tres personajes.

caballero = {'vida': 2, 'ataque': 2, 'defensa': 2, 'alcance': 2}
guerrero = {'vida': 2, 'ataque': 2, 'defensa': 2, 'alcance': 2}
arquero = {'vida': 2, 'ataque': 2, 'defensa': 2, 'alcance': 2}


# Completa el ejercicio aquí
caballero['vida'] = 4
caballero['defensa'] = 4
guerrero['ataque'] = 4
guerrero['alcance'] = 4
arquero['ataque'] = 4
arquero['defensa'] = 1
arquero['alcance'] = 8

print(caballero)
print(guerrero)
print(arquero)
