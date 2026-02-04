# Bucle FOR
impares = [3,5,7,9,11,13,15]

for impar in impares:
    print(impar)

# ------------------------------------------------------------------------------
cadena = 'Aprendiendo Python en Kali Linux'
for caracter in cadena:
    print(caracter)

# ------------------------------------------------------------------------------
rangos  = range(9)
for rango in rangos:
    print(rango)

# ------------------------------------------------------------------------------
print('Rango del 3 al 20 de 2 en 2')
for valor in range(3,20,2):
    print(valor)

# ------------------------------------------------------------------------------
print('Break para parar el bucle')
# Break para parar el bucle
for num0 in range(10):
    if num0 == 5:
        break
    print(num0)

# ------------------------------------------------------------------------------
print('continue para parar la interaccion')
for num1 in range(10):
    if num1 == 5:
        continue
    print(num1)

# ------------------------------------------------------------------------------
numeros = [1,2,3,4,5,6,7,8,9,10]
for indice,numero in enumerate(numeros):
    numeros[indice] = numero * 10
print(numeros)