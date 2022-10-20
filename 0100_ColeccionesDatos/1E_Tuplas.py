# Tuplas Coleccion de elementos ordenada pero que no se puede Modificar
# tupla ( 0 ,1 , 2 ,3, 4, ...)
colores = ("rojo","verde","amarillo","rosa")
print(colores)

for color in colores:
    print(color)

posision = colores[2]
print("La posicion 2 de la tupla {} ".format(posision))
# -> La posicion 2 de la tupla amarillo
# ---------------------------------------------------------------------------
# numeros de elementos de la tupla
print(len(colores))
# -> 4
# ---------------------------------------------------------------------------
# tucla con varios tipos de datos
t = (1,"one",2,"two",3,"three",4,"four",5,"five",0.5)
print(type(t))
# -> <class 'tuple'>
# ---------------------------------------------------------------------------
# tutplas inmutale
#####   t[10] = 6

# ->   t[10] = 6
# TypeError: 'tuple' object does not support item assignment
# ---------------------------------------------------------------------------
# Embalar  desembalar una Tupla
num = "uno","dos","tres","cuatro"
print(type(num))
# -> <class 'tuple'>

a, b, c, d = num
print(a)
# -> uno
print(b)
# -> dos
print(c)
# -> tres
print(d)
# -> cuatro

inicial, *faltantes = num
print(inicial)
# -> uno
print(faltantes)
# -> ['dos', 'tres', 'cuatro']
# ---------------------------------------------------------------------------
#Metodos de las Tuplas
tupla = (1,2,3,4,5,6,7,8,9,0,11)
# cuenta el numero de veces del elemento 1
print(tupla.count(1))
# -> 3
# retorna la posision del elemento
print(tupla.index(3))
# -> 2
# ---------------------------------------------------------------------------
#Conversión entre listas y Tuplas
lista = [1,2,3,4,5]
t = tuple(lista)
print(t)
# -> (1, 2, 3, 4, 5)
print(type(t))
# -> <class 'tuple'>

t = (1,3,5,7,9,11)
l = list(t)
print(t)
# -> (1, 3, 5, 7, 9, 11)
print(type(l))
# -> <class 'list'>
