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

print("Guardar 2 arrays")
np.savez('arrays', x=array1, y=array2)

print("Recuperando 2 arrays")
arrays = np.load('arrays.npz')
print(arrays['x'])
print(arrays['y'])

print("Guardar array en csv")
np.savetxt('array1.csv', array1, delimiter=',')

print("Cargar array desde csv")
array3 = np.loadtxt('array1.csv', delimiter=',')
print(array3)