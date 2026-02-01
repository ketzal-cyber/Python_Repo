#Sentencia Match
# version de python 3.10

opcion = input("Teclea una opcion ")

match opcion:
    case "A":
        print("Opcion A")
    case "B":
        print("Opcion B")
    case "C":
        print("Opcion C")
    case _:
        print("Opcion no valida")