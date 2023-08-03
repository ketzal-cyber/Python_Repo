# Crear una función buscar  que mediante una expresion regular indique si una palara
# esta en la frase
#En caso de encontrarla indicar en que posicion inicia y finaliza
import re

def buscar(texto, frase):
    encontrada = re.search(frase, texto)
    if (encontrada):
        print(encontrada)
        inicia = encontrada.start()
        final = encontrada.end()
        print("Posision inicial {}, final {} ".format(inicia,final))
        return True
    # -> <re.Match object; span=(92, 99), match='tiendas'>
    # -> Posision inicial 92, final 99 
    else:
        return False
    
text = "La digitalización enfocada a dispositivos móviles lleva creciendo desde que se abrieron las tiendas de aplicaciones móviles"
print(buscar(text, "tiendas"))