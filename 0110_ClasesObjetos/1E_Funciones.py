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

# definicion de funcion para ambito de variables
def scopeTest():
    def enLocal():
        local = " var local"

    def nonLocal():
        nonlocal local
        local = "Non local"

    def enGlobal():
        global local
        local = "global varible"

    local = "test local"
    enLocal()
    print('despues de asignacion enlocal', local)
    #despues de asignacion enlocal test local
    nonLocal()
    print('despues de asignacion nonLocal', local)
    #despues de asignacion nonLocal Non local
    enGlobal()
    print('despues de asignacion enGlobal', local)
    #despues de asignacion enGlobal Non local

scopeTest()
print('En ambito Global', local)
#En ambito Global global varible
