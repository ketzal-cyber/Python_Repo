# Guardar un fichero de texto 

# w es write
# t es texto
# guarda nuevo fichero de texto 
# si existe nos dara un error si no lo creara
fichero = open("GuardarNuevoFichero.txt","wt")

cadenaFichero = "Se agregara una nueva cadena de texto y se guardara en el fichero"

fichero.write(cadenaFichero)

fichero.close()
