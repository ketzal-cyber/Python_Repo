# Cadenas de texto

# H o l a   M u n d o
# 0 1 2 3 4 5 6 7 8 9
cadena1  = "Hola Mundo"
print(cadena1[5])
# -> u
print(cadena1[-1])
# -> o
print(cadena1[2:7])
# -> la Mu
print(cadena1[2:])
# -> la Mundo

# Funciones de cadenas

# contar caracteres
print(len(cadena1))
# -> 10

# canvertir MAYUS
MAYUSCULAS = cadena1.upper()
print(MAYUSCULAS)

# convertir minus
minisculas = MAYUSCULAS.lower()
print(minisculas)

# crear lista de palabras
print(cadena1.split())
# -> ['Hola', 'Mundo']
# separa por caracter
cadena2 = "uva,naranja,fresa,limon,mango,platano"
print(cadena2.split(","))
# -> ['uva', 'naranja', 'fresa', 'limon', 'mango', 'platano']

# imprimir variables en cadena de texto
nombre = "Python"
print('Lenguaje '+ nombre)
# -> Lenguaje Python

lenguaje = "JAVA"
framework = "Spring"
print('Tecnología {} con Framework {}'.format(lenguaje, framework))
# -> Tecnología JAVA con Framework Spring

resultado = 10 / 3
print('El resultado es: {r}'.format(r=resultado))
# -> El resultado es: 3.3333333333333335

print('El resultado es: {r:1.4f}'.format(r=resultado))
# -> El resultado es: 3.3333

# imprimir por f-strings  py -> 3.6
mascota = "perro"
mascota2 = "gato"
print(f'Tu mascota es un {mascota}, y un {mascota2} nada mas')
# -> Tu mascota es un perro, y un gato nada mas

# Entrada de texto por teclado
print('Introduce un tecnología')
tec = input()  # <- Mongo
print('Tu tecnología es: '+ tec)
# -> Tu tecnología es: Mongo
