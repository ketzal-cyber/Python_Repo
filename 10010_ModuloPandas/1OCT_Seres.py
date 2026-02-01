#Indices en Series

import pandas as pd 

serie1 = pd.Series([3,5,7,11,13])
print(serie1)

#Salida
#0     3
#1     5
#2     7
#3    11
#4    13
#dtype: int64

#Para acceder a los elementos de la serie
print(serie1[1])
print(serie1[4])

#Salida
#5
#13

#Creando indices personalizados apartir de listas

lenguajes = ['Python', 'Java', 'C++', 'JavaScript', 'C#']
ranking = [2.328, 1.520, 1.474, 1.227, 1.116]


usoLenguajes = pd.Series(ranking, index=lenguajes)
print(usoLenguajes)

#Salida
#Python        2.328
#Java          1.520
#C++           1.474
#JavaScript    1.227
#C#            1.116
#dtype: float64

#Accediendo a los elementos de la serie con indices personalizados
print(usoLenguajes['Python'])
print(usoLenguajes['Java'])
print(usoLenguajes['C++'])
print(usoLenguajes['JavaScript'])
print(usoLenguajes['C#'])

#Salida
#2.328
#1.520
#1.474
#1.227
#1.116

#Agregando. name a la serie
usoLenguajes.name = "Uso de Lenguajes"
print(usoLenguajes)

#Agregando. name a los indices
usoLenguajes.index.name = "Lenguajes"
print(usoLenguajes)

#Filtrando elementos de la serie
print(usoLenguajes[usoLenguajes > 1.5])

#Salida
#Python    2.328
#Java      1.520
#Name: Uso de Lenguajes, dtype: float64

#Convirtiendo una serie a diccionario
diccionario = usoLenguajes.to_dict()
print(diccionario)

#Salida
#{'Python': 2.328, 'Java': 1.52, 'C++': 1.474, 'JavaScript': 1.227, 'C#': 1.116}

#Creando una serie a partir de un diccionario
diccionario2 = {'Python': 2.328, 'Java': 1.520, 'C++': 1.474, 'JavaScript': 1.227, 'C#': 1.116}
serie2 = pd.Series(diccionario2)
print(serie2)

#Salida
#Python        2.328
#Java          1.520
#C++           1.474
#JavaScript    1.227
#C#            1.116
#dtype: float64
