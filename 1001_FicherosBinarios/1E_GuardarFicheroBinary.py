# pickle - Modulo para guardar ficheros binarios
import pickle

lista_lenguajes = ["Java", "Python", "JavaScript", "C#", "Kotlin", "Go"]

#Guardamos la lista en un fichero binario
# w write b binario
fichero = open("fichero_lenguajes.pckl", "wb")

pickle.dump(lista_lenguajes, fichero)

fichero.close()