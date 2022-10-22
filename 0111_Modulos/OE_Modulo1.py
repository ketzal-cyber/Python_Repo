# Modulo  creacion de un modulo propio

# Funcion para ingresar n datos de tipo String
def ingresa(cantidad):
    listaDatos = []
    cont = 1
    while(True):
        cadena = input(f' Ingresa el dato de tipo String {cont} ')
        listaDatos.append(cadena)
        if (cont == cantidad):
            break
        cont += 1
    return listaDatos

# Funcion para ingresar n datos de tipo Entero
def ingresaEnteros(cantidad):
    listaEnteros = []
    cont = 1
    while(True):
        valor = int(input('Ingresa el dato de tipo String '))
        listaEnteros.append(valor)
        if cont == cantidad:
            break
        cont += 1
    return listaEnteros

# Funcion para ingresar n datos de tipo Decimales Float
def ingresaFloat(cantidad):
    listaFloat = []
    cont = 1
    while(True):
        valor = float(input('Ingresa el dato de tipo String '))
        listaFloat.append(valor)
        if cont == cantidad:
            break
        cont += 1
    return listaFloat
