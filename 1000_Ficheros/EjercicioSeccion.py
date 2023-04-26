# Creación de modulo con las funciones de manejo de fichero
import os
class Ficheo:

    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion

    def leerFichero():
        fichero = open(self.nombre,"rt")
        texto = fichero.read()
        return texto

    def guardarFichero(self, texto):
        fichero = open(self.nombre, "wt")
        fichero.write(texto)
        fichero.close()

    def agregarTexto(self, texto):
        fichero = open(self.nombre, "at")
        fichero.write(texto)
        fichero.close()

    def eliminarFichero(self, nombre):
        os.remove(self.nombre)
