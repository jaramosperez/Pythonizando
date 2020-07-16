# TRABAJANDO LOS OPERADORES LOGICOS

# OPERADOR NOT = Sirve para negar algo

print(not True)
# False

print(not True == False)
# True

# CONJUNCIÓN
# Viene de Conjunto
# Sinónimo de unido, contiguo o cercano
# Agrupa Uniendo

print(True and True)
# True

print(True and False)
# False

print(False and True)
# False

print(False and False)
# False

a = 13
print(a > 10 and a < 20)
# True

c = "Hola Javier"
print(len(c) >= 5 and c[0] == 'H')
# True


#DISYUNCIÓN
# Viene de disyunto
# Sinónimo de separado, apartado o distante
# Agrupa separando

print(True or True)
# True

print(True or False)
# True

print(False or False)
# False

c = 'Salir'
print(c == 'Exit' or c == 'Fin' or c == 'Salir')
