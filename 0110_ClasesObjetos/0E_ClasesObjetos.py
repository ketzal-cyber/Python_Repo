# Clases y Objetos en python

# deinicion de Clase
class Comida:
    nombre = "Consome"
    precio = 25

foot = Comida()
print(foot.nombre)
# -> Consome
print(foot.precio)
# -> 25

# definir nuevos valores de un Objeto
foot2 = Comida()
foot2.nombre = "Arroz"
foot2.precio = 30
print(foot2.nombre)
# -> Arroz
print(foot2.precio)
# -> 30

# definicion de clase Persona
class Persona:
    # metodo constructor de un objeto con atributos como parametros
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    # funcion de clase
    def mostrar(self):
        print('Hola te llamas {} de edad {} '.format(self.nombre, self.edad))

persona1 = Persona("Lucia", 35)
print(persona1.nombre)
print(persona1.edad)
persona1.mostrar()
