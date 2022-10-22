# Ejercicio par el uso de Modulos y Clases
import OE_Modulo1
class Dispositivo:
    listaDisp = []

    def __init__(self,nombre,modelo,memoria,precio):
        self.nombre = nombre
        self.modelo = modelo
        self.memoria = memoria
        self.precio = precio

    def __str__(self):
        return f'Dispositivo {self.nomre} con modelo {self.modelo} y memoria {self.memoria} y con un precio {self.precio}'


    def agregar(self):
        cantidad = int(input('Ingresa la cantidad de elementos a ingresar '))
        listaDisp = OE_Modulo1.ingresa(cantidad)
        #print(listaDisp)

disp = Dispositivo("Watch", "AW22","4GB",2500)
disp.agregar()
