import EjercicioSeccion

nombre = "Frameworks.txt"

fichero = EjercicioSeccion.Ficheo(nombre)

texto = input("Introduce un Framework de desarrollo")

fichero.guardarFichero(texto)