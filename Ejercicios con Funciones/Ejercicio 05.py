# Ejercicio 5
# Realiza una función llamada recortar(numero, minimo, maximo) que reciba tres parámetros.
# El primero es el número a recortar,
# el segundo es el límite inferior y el tercero el límite superior.
# La función tendrá que cumplir lo siguiente:
#
# Devolver el límite inferior si el número es menor que éste
# Devolver el límite superior si el número es mayor que éste.
# Devolver el número sin cambios si no se supera ningún límite.
# Comprueba el resultado de recortar 15 entre los límites 0 y 10.
#
# Solución

def recortar(numero, minimo, maximo):
    if minimo > numero:
        return print(minimo)
    elif maximo < numero:
        return print(maximo)
    elif maximo > numero and minimo < numero:
        return print(numero)

recortar(15, 0, 10)