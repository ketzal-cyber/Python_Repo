# Coleccion de elementos que esta desordenada no ha indice para acceder a los elementos
conjunto = {"black","green","silver","red","white","yellow","orange"}
print(conjunto)
# -> {'green', 'black', 'white', 'yellow', 'red', 'orange', 'silver'}
print(type(conjunto))
# -> <class 'set'>

conjunt = set()
conjunt.add("bit")
conjunt.add("byte")
conjunt.add("kilobyte")
print(conjunt)
# -> {'byte', 'bit', 'kilobyte'}

#recorrer con for
for color in conjunto:
    print(color)
# yellow
# green
# silver
# black
# orange
# red
# white
# ---------------------------------------------------------------------------
# no soporta indexacion
#print(conjunto[0])
#   print(conjunto[0])
#   TypeError: 'set' object is not subscriptable
# ---------------------------------------------------------------------------
print(len(conjunto))
# -> 7
# ---------------------------------------------------------------------------
# Funciones de los conjuntos
conjunto.add("blue")
print(conjunto)
# -> {'silver', 'orange', 'yellow', 'white', 'green', 'blue', 'red', 'black'}
conjunto.remove("green")
print(conjunto)
# -> {'yellow', 'orange', 'black', 'blue', 'white', 'silver', 'red'}
#
conj = set(["pink","gray","brown","purple","green","blue"])
print("diferencias")
print(conjunto.difference(conj))
# -> {'black', 'orange', 'silver', 'red', 'white', 'yellow'}

print(conj.issubset(conjunto)) # comprobar si un conunto es subconjunto de otro
# -> False

print(conjunto.issuperset(conj)) # si un conjunto es superconjunto de otro conjunto

print(conjunto.intersection(conj))  # para inerceptar dos conjuntos

conjunto.clear() # limpia el conjunto de elementos
print(conjunto)
# -> set()
