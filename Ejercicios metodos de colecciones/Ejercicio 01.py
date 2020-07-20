texto = "un día que el viento soplaba con fuerza#" \
        "mira como se mueve aquella banderola -dijo un monje#" \
        "lo que se mueve es el viento -respondió otro monje#" \
        "ni las banderolas ni el viento, " \
        "lo que se mueve son vuestras mentes -dijo el maestro"

# Completa el ejercicio aquí
original = 'un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro'

original.capitalize()
original.replace('...', '#\n')

print(texto)
print(original)

lineas = texto.split("#")
for i, linea in enumerate(lineas):
    lineas[i] = linea.capitalize()
    if i == 0:
        lineas[i] = lineas[i] + "..."
    else:
        lineas[i] = "- " + lineas[i] + "."

# Mostramos el texto final
for linea in lineas:
    print(linea)