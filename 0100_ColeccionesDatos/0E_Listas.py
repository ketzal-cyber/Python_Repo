# Listas
# Coleccion ordenada   cambiante

#Variales tipo Listas
listaUno = list()
listaDos = []

listaUno.append(1)
print("Lista uno {} ".format(listaUno))
# -> Lista uno [1]

listaDos = [2,4,6,8,10]
print(listaDos)
# -> [2, 4, 6, 8, 10]

# Indexación negativa
print(listaDos[-1])
# -> 10
print(listaDos[-2])
# -> 8

# Rango de indices  rangos negaticos
print(listaDos[2:])
# -> [6,8,10]
print(listaDos[-4:-1])
# -> [4, 6, 8]


colores = ["rojo","amarillo", "verde"]
print(colores)
# -> ['rojo', 'amarillo', 'verde']

#Modificar elemento de la Listas
colores[1] = "azul"

print(len(colores))
# -> 3

colores.append("naranja")
print(colores)
# -> ['rojo', 'azul', 'verde', 'naranja']

# borrar elemento
colores.remove("rojo")
print(colores)
# -> ['azul', 'verde', 'naranja']

# recorrer la lista con un bucle
for color in colores:
    print(color)
# -> Azul
# -> verde
# -> naranja

# limpiar la Listas
colores.clear()
print("La lista ha sidi eliminada {} ".format(colores))
# -> La lista ha sidi eliminada []

numeracion = [1,2,5,25,33,56,75,21,56,89,43,13,62,24]
n = 21
if n in numeracion:
    print('Si esta en la lista')
else:
    print('No esta en la lista')
