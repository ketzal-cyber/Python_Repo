# Bucle While

inicio = int(input('Introduzca valor inicial '))     # <- 3
fin = int(input('Introduzca valor fin '))            # <- 9
contador=0
while(inicio < fin):
    print(inicio)
    contador += 1
    inicio += 1
# -> 3
# -> 4
# -> 5
# -> 6
# -> 7
# -> 8
suma=0
while (contador != 0):
    suma += contador
    contador -= 1
else:
    print('La suma es {}'.format((suma)))
