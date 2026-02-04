
sumatoria = 0

limite = int(input('Ingresa el numero limite  del range de valores '))

for num in range(limite):

    print('El numero en el ciclo es: ', num)
    if num % 5 != 0 and num % 3 != 0:
        print('El numero no es multiplo de 3 ni de 5')
    else:
        print('El numero es multiplo de 3 o de 5')
        sumatoria += num

print('La sumatoria de los numeros es: ', sumatoria)


listaCadenas = ['Hola', 'Mundo', 'Python', 'Kali', 'Linux']

for indice,cadena in enumerate(listaCadenas):
    listaCadenas[indice] = listaCadenas[indice][0]
print(listaCadenas)

print('Bucle para pedir un numero dentro del 1 a l 9 ')
while True:
    numero = int(input("Introduce un numero nuevamente "))
    if numero >= 1 and numero <= 9:
        break
    else:
        print("El numero no esta dentro del rango")

multiplos = []
for num in range(1,100,numero):
    print(num)
    multiplos.append(num)
print(multiplos)
    

#matriz de 2 dimenciones
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("Editar valrores de la matriz")
for f, filas in enumerate(matriz):
    for c, columnas in enumerate(filas):
        if columnas % 2 == 0:
            matriz[f][c] = 0
        else:
            matriz[f][c] = 1
print(matriz)