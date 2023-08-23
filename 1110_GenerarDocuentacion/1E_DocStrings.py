# Docstring -> cadenas para documentación
# funcion con mentario que servira para la documentación
def saludar(nombre):
    """
    Este es un comentario de la funcion 
    Esta funcion recibira como parametro una cadena con el nombre e
    imprimira por pantalla un saludo con el nombre concatenada
    """
    print("Buenos dias {}"+nombre)

saludar("María")

# para conocer la documentacion atraves del comentario agregado seria:
help(saludar)
# -> definicion de la función con las lineas del comentario 

# Clase con comentario para documentación
class Animal:
    """
    Esta clase tiene dos funciones comer y dormir

    """
    def comer(self,comida):
        """Esta funcion sirve para saber que come el animal """
        print("El animal esta comiendo {}".format(comida))

    def dormir():
        """Esta funcion sirve para saber que el animal esta durmiendo """
        print("El animal esta durmiendo ")

# con help para conocer la documentacion de funciones en python
help(Animal)