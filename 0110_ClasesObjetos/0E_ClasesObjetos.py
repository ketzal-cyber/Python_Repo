# Clases y Objetos en python

# deinicion de Clase
class Comida:
# variables de clase cmpartida entre todas las instancias son para metodos y atributos
    tiempo = ("Primer","Segundo","Tercer")

    def __init__(self,nombre,precio):
    #Variable de instancia unica para cada  instancia
        self.nombre = nombre
        self.precio = precio
    def cambiarAtributos(self, newNombre, newPrice):
        self.nombre = newNombre
        self.precio = newPrice

    def __str__(self):
        return f'La comida {self.nombre} con precio {self.precio}'


# Primer objeto de la clase Comida
# *****************************************************************************
print('*****************************************************************************')
foot = Comida("Mole",100)
print(foot.tiempo)  #Compartido para todoas las Comidas
print(foot.nombre)  # unico para foot
# -> Mole
print(foot.precio)  # unico para foot
# -> 100
foot.cambiarAtributos("Sopa",60)
print(f'Los datos modificados {foot}')
# ->

# Segundo objeto de la clase Comida
# *****************************************************************************
# definir nuevos valores de un Objeto
foot2 = Comida("Tacos dorados",80)
print(foot2.tiempo)  #Compartido para todoas las Comidas
print(foot2.nombre)  # unico para foot
# -> Tacos dorados
print(foot2.precio)  # unico para foot
# -> 80

# Tercer objeto de la clase Comida
foot3 = Comida("Enchiladas",150)
print(foot3.tiempo)  #Compartido para todoas las Comidas
print(foot3.nombre)  # unico para foot
# -> Enchiladas
print(foot3.precio)  # unico para foot
# -> 150
# *****************************************************************************

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
# -> Hola te llamas Lucia de edad 35
