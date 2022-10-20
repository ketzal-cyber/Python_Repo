# Diccionarios
dic = {1:"uno",2:"dos",3:"tres",4:"cuatro",5:"cinco"}
print(dic)
# -> {1: 'uno', 2: 'dos', 3: 'tres', 4: 'cuatro', 5: 'cinco'}

#acceder
print(dic[3])
# -> tres
# agregar
dic[6] ="seis"
print(dic)
# -> {1: 'uno', 2: 'dos', 3: 'tres', 4: 'cuatro', 5: 'cinco', 6: 'seis'}

#eliminar
dic.pop(4)
print(dic)
# -> {1: 'uno', 2: 'dos', 3: 'tres', 5: 'cinco', 6: 'seis'}
del(dic[6])
print(dic)
# -> {1: 'uno', 2: 'dos', 3: 'tres', 5: 'cinco'}
# ---------------------------------------------------------------------------
#mostrar claves
for number in dic:
    print(number)
# 1
# 2
# 3
# 5

for clave,valor in dic.items():
    print(clave,valor)
# 1 uno
# 2 dos
# 3 tres
# 5 cinco

# ---------------------------------------------------------------------------
