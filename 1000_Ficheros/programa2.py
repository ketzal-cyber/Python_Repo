import EjercicioSeccion

# Pido el nombre del fichero
# Regreso el apuntador fichero
def nameFile():
    nombreFile = input("Ingresa el nombre del Fichero ")
    return EjercicioSeccion.Fichero(nombreFile+".txt")

def guardarArchivo(apuntador):
    apuntador.guardarFichero(input("Introduce un texto para agregar al fichero "))

def writeMoreLine(apuntador):
    textIncluir = input("Introduce una linea más para agregar al fichero ")
    apuntador.agregarTexto("\n"+textIncluir)

def readFile(apuntador):
    print(apuntador.leerFichero())

def run():
    apuntador = nameFile()
    guardarArchivo(apuntador)
    writeMoreLine(apuntador)
    readFile(apuntador)

run()



#fichero = EjercicioSeccion.Fichero(nombre)
#nombre = "LenguajesProgramacion.txt"
#texto = input("Introduce un Framework de desarrollo ")
#fichero.guardarFichero(texto)
#textIncluir = "\n Texto incluido en la 2da linea"
#fichero.agregarTexto(textIncluir)
#leerFichero = fichero.leerFichero()
#print(leerFichero)