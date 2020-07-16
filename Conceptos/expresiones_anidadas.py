# SIEMPRE SE RESUELVEN LAS EXPRESIONES EN ORDEN DE PRECEDENCIA.
# Primero los paréntesis porque tienen prioridad
# Segundo, expresiones aritméticas por sus propias reglas: Exponentes y Raices,
# Multiplicaciones y divisiones, Sumas y restas. Izquierda a Derecha.
# Tercero, debemos continuar con los relacionales de Izquierda a Derecha.
# Finalmente los lógicos. (Not tienen prioridad)
a = 10
b = 5
print(a * b - 2**b <= 10 and not (a % b) != 0)


