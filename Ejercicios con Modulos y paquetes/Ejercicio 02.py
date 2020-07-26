# Ejercicio 2
# ¿Eres capaz de desarrollar un reloj de horas, minutos y segundos utilizando el módulo datetime con la hora actual?
# Hazlo en un script llamado reloj.py y ejecútalo en la terminal:
#
# Ayuda
#
# El módulo time integra una función llamada sleep(segundos)
# que puede pausar la ejecución de un programa durante un tiempo.
# Así mismo el módulo os integra la función system('cls') y system('clear')
# para limpiar la pantalla de la terminal en sistemas Windows y Linux/Unix respecticamente.
import datetime
import time
import os

while True:
    os.system('cls')  # Limpiamos la pantalla
    dt = datetime.datetime.now()
    print("{}:{}:{}".format(dt.hour, dt.minute, dt.second))
    time.sleep(1)  # Esperar 1 segundo