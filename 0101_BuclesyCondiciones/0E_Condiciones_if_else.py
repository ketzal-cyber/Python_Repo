# Tema pra tratar las condiciones if else

a = 9
b = 4
c = 7
d = 5
print(a>b)
# -> True

if (a>d):
    print('A {} es mayor a D {}'.format(a,d))
else:
    print('D {} es mayor a A {}'.format(d,a))


if (a > b) and (c > d):
    print('La condicion a {} > b {} AND c {} > d {}  es verdadera'.format(a,b,c,d))
else:
    print(False)

# ------------------------------------------------------------------------------
num0 = int(input('Introduce un valor '))
num1 = int(input('Introduce un valor '))
if num0 > num1:
    print('El primer valor {}  es mayor que el segundo valor {} '.format(num0,num1))
elif num0 == num1:
    print('Los valores {} , {}  son iguales '.format(num0,num1))
else:
    print('El segundo valor {}  es mayor  que el primer valor {} '.format(num1,num0))
