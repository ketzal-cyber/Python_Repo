#Tratamiento de errores en Python
# Try ... except ... else ... finally

try:
    num = 3
    num2 = 0
    division = num / num2
    print(division) 
except ZeroDivisionError:
    print('Error al dividir entre cero')
except TypeError:
    print('Error al dividir número y  caracter')
else:
    print('La divicion funciono correctamente.')
finally:
    print('Siempre se ejecuta al final ')