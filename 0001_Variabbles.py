# Variables

# Variables incorrectas
'''
5variabble = 'cadena uno'
print(5variable)
'''

cadena = 'Cadena'
cadena2 = 'de caracteres'
cadenaNueva = cadena + cadena2
print(cadenaNueva)
# -> Cadena caracteres

Variable = 5
variable = 10
suma = Variable + variable
print(suma)
# -> 15

#Numeros
valor = 25
valor2 = 1.8

# Boolean
verdadero = True
falso = False

# Convertidor
numero = '25'
numero2 = int(numero)
numero3 = 10
result = numero2 + numero3
print(result)
# -> 35

cadena3 = '2.5'
numDecimal = float(cadena3)
result2 = numDecimal + 5.5
print(result2)
# -> 8.0

valor1 = 5
valor2 = 5.5
valor3 = 8
suma = valor1 + valor2 + valor3
print(suma)
# -> 18.5
print(type(suma))
# -> <class> float

text = str(suma)
print("El resultado es: "+ text)
# -> El resultado es: 18.5
print(type(text))
# -> <class> str 
