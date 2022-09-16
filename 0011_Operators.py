# Operadores
#Operadores de aritmétcos (+ , - , * , / , % , ** , //)
num1 = 5
num2 = 10
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
division = num1 / num2
resto = num1 % num2
cociente = num1 // num2
exponente = (num1 ** 2)

print('suma {}, resta {}, producto {}, division {}, resto {}, cociente {}, exponente {}'.format(
suma,resta,producto,division,resto, cociente,exponente))
# -> suma 15, resta -5, producto 50, division 0.5, resto 5, cociente 0, exponente 25

# Operadores de asignación  (= , += , -= , *= , /= , **=)
print('Operadores aritmétcos')
num3 = 5
# num3 = num3 + 5
num3 += 5
print(num3)
# -> 10

# num3 = num3 - 5
num3 -= 5
print(num3)
# -> 5

# num3 = num3 * 5
num3 *= 5
print(num3)
# -> 25

# num3 = num3 / 5
num3 /= 5
print(num3)
# -> 5.0

# num3 = num3 ** 2
num3 **= 2
print(num3)
# -> 25.0

# Operadores de Comparacion (== , != , > , < , >= , <= )
print('Operadores Comparacion')
num4 = 3
num5 = 7
print(num4 == num5)
# -> False

cadena3 = "hola"
cadena4 = "hola"
print(cadena3 == cadena4)
# -> True

print(num4 != num5)
# -> True
print(num4 > num5)
# -> False
print(num4 < num5)
# -> True
print(4 >= 4)
# -> True
print(num4 <= num5)
# -> True

# Operadores Logicos (and , or ,  not)
print("Operadores Logicos")
num1 = 10
num2 = 5
num3 = 7
num4 = 8
print((num1 > num2) and (num3 < num4))
# -> True
print((num1 > num2) and (num3 > num4))
# ->False
print((num1 > num2) or (num3 > num4))
# -> True

print(not(num3 > num4))
# -> True

# Operadores de Identidad (is , is not)
print('Operadores de Identidad')
frutas1 = ['Manana', 'Peras']
frutas2 = ['Manana', 'Peras']
frutas3 =  frutas1
print(frutas1 is frutas3)
# -> True
frutas3.append('naranja')
print(frutas1)
# -> ['Manana', 'Peras', 'naranja']
print(frutas1 is not frutas3)
# -> False
 # Operadores de Pertenencia (in , not in)
print('Operadores de Pertenencia')
frutas1 = ['Manana', 'Peras', 'naranja']
frutas2 = 'pera'
print(frutas2 in frutas1)
# -> False  pera no esta en frutas1
fruta3 = "melon"
print(frutas3 not in frutas1)
# -> True

numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)
numero = int(input('Introduce u dato '))
if numero in numeros:
    print('Si') # <- 7
    # -> Si
if numero not in numeros:
    print('No') # <- 20
    # -> No 
