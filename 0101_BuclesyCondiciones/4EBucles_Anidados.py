# Bucles Anidados


lista = ["Hola",10, "Mundo", [50,100,150]]

#Imprimir dato de la ultima lista
print(lista[-1][0])

#Salida
#50

listColecciones = [
    "Hola Mundo de Python",  #cadena
    (1,5, 10,15,20,25),      #tupla
    ["backend", "frontend", "fullstack"], #lista
    #{"Python", "Java", "Rust", "JavaScript", "C"} #set
]

print("Recorriendo los elementos de la primera coleccion")
for coleccion in listColecciones:
    print(coleccion)

print("Recorriendo los elementos de las colecciones")
for coleccion in listColecciones:
    for elemento in coleccion:
        print(elemento)


#Recorer por indices de las colecciones
print("Recorriendo cada volor por indices")
for indice_collecion,coleccion in enumerate(listColecciones):
    for indice_elemento,elemento in enumerate(coleccion):
        print(listColecciones[indice_collecion][indice_elemento])
        

tabla = [
    [0,0,0],
    [1,1,1],
    [2,2,2]
]
print("Recorriendo la tabla tipo cubo")
for fila in tabla:
    for columna in fila:
        print(columna, end=" ")
    print()

#Recorriendo la tabla tipo cubo por indices
for i, fila in enumerate(tabla):
    for k, columna in enumerate(fila):
        print(tabla[i][k], end=" ")
    print()


cubo = [
    tabla,tabla,tabla
]

print("Recorriendo el cubo")
for capa in cubo:
    for fila in capa:
        for columna in fila:
            print(columna, end=" ")
        print()
    print()

#Recorriendo el cubo por indices
print("Recorriendo el cubo por indices")
print("Profundidad altura columna")
for p, capa in enumerate(cubo):
    for h, fila in enumerate(capa):
        for c, columna in enumerate(fila):
            print(cubo[p][h][c], end=" ")
        print()
    print()