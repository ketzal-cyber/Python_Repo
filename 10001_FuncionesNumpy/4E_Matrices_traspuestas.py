# Arrays o Matrices transpuestas cambiar ordenadamente las filas por las columnas

import numpy as np

matriz = np.array(([1,2,3],[4,5,6],[7,8,9]))
print("Matriz original")
print(matriz)

matriz_traspuesta = matriz.T
print("Matriz traspuesta")
print(matriz_traspuesta)


array = np.arange(15).reshape(3,5)
print("Array original")
print(array)

array_traspuesto = array.T
print("Array traspuesto")
print(array_traspuesto)
