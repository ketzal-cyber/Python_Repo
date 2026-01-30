# Indexacion con arrays con numpy

import numpy as np

arrays1 = np.arange(0,11)
print("Arrays con arange de 0 a 10")
print(arrays1)

print("Indexacion del array")
print(arrays1[2:5])

array_copia = arrays1.copy()
print("Copia del array")
print(array_copia)

array_copia[0] = 100
print("Copia del array modificada")
print(array_copia)

print("Array original")
print(arrays1)

array_copia[5:8]= 15
print("Copia del array modificada")
print(array_copia)

array2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Array 2")
print(array2)

print("Indexacion del array de 3 dimensiones")
print(array2[1][0])


array3 = np.array(([2,4,6],[8,10,12],[14,16,18]))
print("Array 3")
print(array3)
