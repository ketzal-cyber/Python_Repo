# Fichero de secuencia de bits
# Leer fichero de texto 

# r por read
# t por ser fichero con caracteres texto (no es binario ni imagen)
#Devuelve un puntero del fichero
fichero = open("fichero_text.txt","rt")

# para acceder a datos del fichero, mediante la función read()
datosFichero = fichero.read()

# Imprimir el contenido del fichero
print(datosFichero)