#Funciones generadoras

#range(0,11) genera rangos del 0 al 10
rango = range(0,11)
# funcion equivalente empieza del 0 al 10
for num in range(11):
    print(num)

def numPares(maximo):
    for numero in range(maximo):
        if (numero % 2 == 0):
            yield numero    # yield pone en pausa la iteraccion y crea un iterable

maximo = 11
for pares in numPares(maximo):
    print(pares)
