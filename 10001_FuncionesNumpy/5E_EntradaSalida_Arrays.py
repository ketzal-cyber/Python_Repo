#Entrada y salida de arrays con numpy

import numpy as np

array1 = np.arange(8)
print("Array original")
print(array1)

np.save("array1", array1)

print("Array guardado")

array2 = np.load("array1.npy")

print("Array cargado")
print(array2)