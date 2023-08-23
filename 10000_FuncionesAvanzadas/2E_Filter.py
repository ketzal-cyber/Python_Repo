# Filter   función para filtrar resultados segun una condicion

def positivo(numero):
    if(numero > 0):
        return True
    else:
        return False
    
listaNumeros = [4, -2,8, -3, -5, -7, 1, 9]

#obtener una lista de los valores positivos
# atraves de un filter con una funcion condicional y unalista
filtro = filter(positivo,listaNumeros)
resultado = list(filtro)
print(resultado)