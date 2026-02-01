#Crear Lista con valores de 10 al 19
#Crear Lista con numeros 40 al 49
#Crear una matriz de 2x10 con las listas anteriores
#Crear otra matriz apartir de la anterior pero estos valores multiplicados por 2

import numpy as np

lista1 = [10,11,12,13,14,15,16,17,18,19]
lista2 = [40,41,42,43,44,45,46,47,48,49]

matriz = np.array([lista1, lista2])
print(matriz)

print("Matriz de tipo 2 x 10")
print(matriz.shape)

matriz2 = matriz * 2
print(matriz2)

np.Suma