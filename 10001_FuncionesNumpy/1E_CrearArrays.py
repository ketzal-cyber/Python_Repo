#Creacion de arrays en numpy

import numpy as np

print(np.zeros(5))

print(np.ones(5))
# creacion de arrays de 5 elementos con valore 5
print(np.full(5, 5))
# creacion de arrays con valores entre ciertos limites y de 5 en 5 
print(np.arange(5,50,5))

print('creacion de arrays con valores de una lista')

array1 = [ 1,2,3,4,5]
print(np.array(array1))

lista1 = [1,2,3,4,5]
lista2 = ["a","b","c","d","e"]
listadoble = (lista1,lista2)
print('Lista doble')
print(listadoble)

print('Array doble  con numpy')
arrayDoble = np.array(listadoble)
print(arrayDoble)

print('Array doble  numpy shape')
print(arrayDoble.shape)

print('Array doble  numpy dtype')
print(arrayDoble.dtype)

print('Array doble  numpy size')
print(arrayDoble.size)

