'''
Crea un diccionario con los siguiente pares de valor
"manzana":"apple", "naranja": "orange","platano":"banana","limon":"lemon"
muestra la traduccion de la palabra naranja
añade un nuevo elemento piña, pineapple
haz un bucle para mostrar todos los elemetos del diccionario
crear una funcion para buscar un elemento  por su clave
'''
# creacion de diccionario
frutas = {"manzana":"apple", "naranja": "orange","platano":"banana","limon":"lemon"}
print(frutas)

# mostrar la traduccion de la palabra naranja
print('La traduccion de la palabra naranja es: {} '.format(frutas['naranja']))

# funcion para agregar fruta
def agregarFruta(clave, valor):
    frutas[clave] = valor

# funcion para recorrer los elementos de un diccionario mediante un bucle
def recorrerDic():
    for clav, val in frutas.items():
        print('Clave {}, Valor {} '.format(clav,val))

# variables para agregarFruta
print('Agregar una nueva fruta al diccionaro')
clave = ""
valor = ""
clave = input('Teclea la clave ')
valor = input('Teclea el valor ')
agregarFruta(clave,valor)

# recorrer diccionario con un bucle
recorrerDic()

# funcion para hacer una busqueda de un elemento  con su clave
def buscaElement(clave):
    try:
        pass
        print(frutas[clave])
    except KeyError:
        print('La clave introducida no coincide con ninguna existente')


clav = input('Ingresa la clave para buscar en diccionario ')
buscaElement(clav)

# ------------------------------------------------------------------------------
print('------------------------------------------------------------------------------')
'''
1- Crea una Lista de notas que reciba n notas por teclado
2- Crea una una tupla con 6 trabajos a calificar y muestre por pantalla
agrega Conunto con apellidos=set() para ingresar n apellidos
Calcula el valor de la variable nota final, teniendo en cuenta que si
entonces nota final sera igual a aprobado
en caso contrario sera igual a suspendido
'''
print('**********************************************************************')
# listas orden, indexadas, duplicados, modificable
listaNotas = []
# Tuplas orden, indexadas, duplicados, inmutable
aspectosCalif = ("Asistencia","Tareas","Presentacion","Analisis","proyecto2","proyecto3")

# Conjuntos Set() sin orden, sin indices, no duplicados, modificable
apellidos = set()
# Diccionarios sin orden,indexadas por clave, duplicados valores modificables
# nombre = {}
alumnos = dict()

# definir cantidad de notas a ingresar
def ingresaCantidad():
    cantidad = int(input('Ingresa la cantidad de notas a ingresar '))
    return cantidad

# funcion para ingresar notas y retornar la suma de las mismas
def notas(cantidad):
    cont = 1
    suma = 0
    while(True):
        nota = float(input('Introduce una Nota '))
        listaNotas.append(nota)
        suma += nota
        if(cont == cantidad):
            break
        cont += 1
    #print(suma)
    return suma

# agrega apellidos de alumnos en un conjunto
def ingresarAlumnos(cantidad):
	cont = 1
	while(True):
		apellido = input('Ingresa apellidos de alumnos ')
		apellidos.add(apellido)
		if(cont == cantidad):
			break
		cont += 1

def definirApellidoValores():
	jobs = {}
	alumnos = dict.fromkeys(apellidos)
	for clave in alumnos:
         forClave = int(input('Ingrese el valor para '+ clave + ''))
         alumnos[clave] = forClave
	print(alumnos)

#Ingresa  alumno y nota
def capturaTrabajos(cantidad):
    print('Ingrese alumno como clave y nota como valor')
    cont = 1
    while(True):
        try:
            pass
            clave = input('{} Ingresa la clave '.format(cont))
            valor = int(input('Ingresa el valor '+ clave + " "))
            alumnos[clave] = valor
            if(cont == cantidad):
                break
            cont += 1
        except ValueError:
            print('Error en el valor introducido')


numero = ingresaCantidad()

print('***********************************************************************')
print('Ingrese las {} notas'.format(numero))
sumaNotas = notas(numero)

print('*********************************************************************** \nMostrar Tupla')
print(aspectosCalif)

print('*********************************************************************** \n Agregar Apellidos')
ingresarAlumnos(numero)

print('*********************************************************************** \n Definir apea dict y valores')
definirApellidoValores()
print('***********************************************************************')
print(sumaNotas)
#capturaTrabajos(numero)
print(alumnos)

print('***********************************************************************')
print(type(alumnos))
print(type(aspectosCalif))
print(type(apellidos))
