import datetime
import locale
import pytz

#Trabajando datetime NOW
dt = datetime.datetime.now()
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.second)
print(dt.microsecond)
print(dt.tzinfo)

# Ejemplo de como Mostrar la fecha

print('{}:{}:{}'.format(dt.hour, dt.minute, dt.second))
print('{}/{}/{}'.format(dt.day, dt.month, dt.year))

# Formas fáciles de trabajar las fechas y horas.

#FORMA INTERNACIONAL DE ENTREGAR LOS DATOS
print(dt.isoformat())

# FORMATEAR MANUALMENTE
print(dt.strftime("%A %d %B %Y %I %M"))

# FORMATEAR CON DATOS LOCALES O MANUALMENTE CONFIGURADO
# SE DEBE IMPORTAR LA LIBRERIA LOCALE
locale.setlocale(locale.LC_ALL, 'es-CL')
print(dt.strftime("%A %d %B %Y %I %M"))

# Poner la fecha en formato 24 horas
dt.strftime("%A %d de %B del %Y - %H:%M")
print(dt.strftime("%A %d de %B del %Y - %H:%M"))

# OPERACIONES MATEMÁTICAS CON FECHA.
print(dt, 'Nuevamente con operaciones')
t = datetime.timedelta(days=14, hours=12)
en_dos_semanas = dt + t
print('En dos semanas mas sera: ', en_dos_semanas)
dos_semanas_formateado = en_dos_semanas.strftime('En dos semanas mas sera:  %A %d de %B del %Y - %H:%M')
print(dos_semanas_formateado)
print('******* restando dias *****')
hace_dos_semanas = dt - t
print(hace_dos_semanas)

# MODULO DE ZONAS HORARIAS.
# SE DEBE UNA IMPORTAR CON PIP INSTALL PYTZ
#print(pytz.all_timezones) #Muestra todas las zonas horarias
dt = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
print(dt.strftime("%A %d de %B del %Y - %H:%M"))

