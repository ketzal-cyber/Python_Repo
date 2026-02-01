#Funciones con arrays

import numpy as np

numAleatorios = np.random.rand(5)
print(numAleatorios)

print("Media:", np.mean(numAleatorios))
print("Mediana:", np.median(numAleatorios))
print("Varianza:", np.var(numAleatorios))
print("Desviación estándar:", np.std(numAleatorios))