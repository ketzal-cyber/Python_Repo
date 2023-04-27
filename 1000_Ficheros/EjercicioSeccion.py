# Creación de modulo con las funciones de manejo de fichero
import os
class Fichero:

    def __init__(self, nombre):
        self.nombre = nombre

    #metodo para leer ficheros
    def leerFichero():
        fichero = open(self.nombre,"rt")
        texto = fichero.read()
        return texto

    # metodo para guardar nuevo fichero
    def guardarFichero(self, texto):
        fichero = open(self.nombre, "wt")
        fichero.write(texto)
        fichero.close()

    # metodo para agregar texto al fichero
    def agregarTexto(self, texto):
        fichero = open(self.nombre, "at")
        fichero.write(texto)
        fichero.close()

    # metodo para eliminar un fichero
    def eliminarFichero(self, nombre):
        os.remove(self.nombre)
