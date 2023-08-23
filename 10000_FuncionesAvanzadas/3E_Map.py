# Map aplicar una funcion a una lista

def multiplicar(numero):
    return numero*2

listNumeros = [2,4,6,8]

## aplicar la función a cada uno de los elementos de la lista
#   devuelve un objeto
mapeo = map(multiplicar, listNumeros)

result = list(mapeo)
print(result)
# -> [4, 8, 12, 16]

# forma de hacerlo con una lambda
lista_resultado = list(map(lambda numero: numero * 2, listNumeros))
print("Mediante lambda")
print(lista_resultado)