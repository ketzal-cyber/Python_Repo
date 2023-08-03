#JSON
#Convertir un diccionesrio a un JSON
import json

persona = {"nombre":"Sandra", "edad":30,"ocupacion":"Cajera"}
estructuraJSon = json.dumps(persona)
# -> {"nombre": "Sandra", "edad": 30, "ocupacion": "Cajera"}
# en formato cadena de caracteres
#Para acceder seria 
print(estructuraJSon[2:8])
# nombre

# Convertir uns estructura json a un diccionario de python
nuevoDiccionario = json.loads(estructuraJSon)
print(nuevoDiccionario["nombre"])


