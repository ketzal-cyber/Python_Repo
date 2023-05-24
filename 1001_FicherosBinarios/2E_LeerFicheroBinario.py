# pickle - Modulo para leer datos de un archivo binario
import pickle

datosFichero = open("fichero_lenguajes.pckl", "rb")

listaFichero = pickle.load(datosFichero)

print(listaFichero)