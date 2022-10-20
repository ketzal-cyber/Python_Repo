# Funciones

# definicion de Funcion
def saludar():
    print('Hola Devs')

# definir funcion con parametros
def numeros(uno,dos):
    result = uno + dos
    return result

# Llamar a funciones
saludar()
resultado = numeros(7,8)
print(resultado)

# paso de valor por refetencia la funcion puede modificar la lista
colores = ["Azul","Rojo","Plata"]
def incluirColor(colores,color):
    colores.append(color)

nuevo = "Lima"
incluirColor(colores,nuevo)
print(colores)
