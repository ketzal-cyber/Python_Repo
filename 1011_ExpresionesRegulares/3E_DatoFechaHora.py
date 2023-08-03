# Dato de fecha y Hora

# importamos desde el modulo datetime la clase datetime
from datetime import datetime

# Muestra la fecha y la hora actual
fecha = datetime.now()
# -> 2025-12-27 00:12:30.823171

print(datetime.year) # año
print(datetime.month) # mes
print(datetime.day) # dia

# hora
hora = fecha.hour # hora
minutos = fecha.minute # minutos
segundos = fecha.second  # sundos
microsegundos = fecha.microsecond # microseunos   
print("La hora es {}:{}:{}:{}".format(hora,minutos,segundos,microsegundos))
# -> La hora es 1:1:34:731987