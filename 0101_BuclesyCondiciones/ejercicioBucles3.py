num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))

while true:
    print('''
    1. Sumar los dos numeros
    2. Restar los dos numeros
    3. Multiplicar los dos numeros
    4. Salir
    ''')
    opcion = int(input("Ingresa una opcion: "))
    if opcion == 1:
        print("La suma es: ", num1 + num2)
    elif opcion == 2:
        print("La resta es: ", num1 - num2)
    elif opcion == 3:
        print("La multiplicacion es: ", num1 * num2)
    elif opcion == 4:
        break
    else:
        print("Opcion no valida")


#Encontrar las letras en comun de dos listas
list1 = ["H","o","l","a"," ", "P","y","t","h","o","n"]
list2 = ["H","o","l","a"," ", "J","a","v","a"]

list3 = []

for letra in list1:
    if letra in list2 and letra not in list3:
        list3.append(letra)
print(list3)
          