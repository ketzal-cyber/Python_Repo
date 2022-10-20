'''
crear una clase Coche que tenga estos atributos
marca, color, combustible, puertas,
crear la funcion __init__
'''

class Coche:

    def __init__(self,modelo,color, combustible, puertas):
        self.modelo = modelo
        self.color = color
        self.combustible = combustible
        self.puertas = puertas

    def arrancar(self):
        print('Esta avanzando')
    def __str__(self):
        return f'El modelo es: {self.modelo} su color es: {self.color} su combustible es: {self.combustible} Litros y con {self.puertas} puertas'

auto = Coche('Ford', 'Negro', 10, 4)

print(auto)

# ------------------------------------------------------------------------------
print('------------------------------------------------------------------------------')
'''
1-
'''
print('**********************************************************************')
