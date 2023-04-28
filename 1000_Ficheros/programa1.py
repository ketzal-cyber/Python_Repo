import EjercicioSeccion

nombre = "Frameworks.txt"

fichero = EjercicioSeccion.Fichero(nombre)

texto = input("Introduce un Framework de desarrollo ")

fichero.guardarFichero(texto)

textIncluir = "\n Texto incluido en la 2da linea"
fichero.agregarTexto(textIncluir)

leerFichero = fichero.leerFichero()

print(leerFichero)