#Guardar un diccionario en un archivo binario
import pickle

def guardarDatos():
    datos = {"Nombre":"Agent", "ocupacion":"Técnico", "edad":30, "Ubicacion":"Oeste"}
    fichero = open("datos.pckl","wb")
    pickle.dump(datos,fichero)
    fichero.close()

def leerDatosFichero():
    fichero = open("datos.pckl", "rb")
    dic = pickle.load(fichero)
    print(dic)

guardarDatos()
leerDatosFichero()


