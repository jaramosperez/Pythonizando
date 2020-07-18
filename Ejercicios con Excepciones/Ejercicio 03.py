# Ejercicio 3
# Localiza el error en el siguiente bloque de código.
# Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
# colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }
# colores['blanco']

colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }
try:
    print(colores['blanco'])
except KeyError:
    print("Error en la palabra clave, no se encuentra en el diccionario la clave 'blanco', prueba con otros colores")
except Exception as error:
    print(type(error).__name__)
