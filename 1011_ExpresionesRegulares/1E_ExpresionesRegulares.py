# Expresiones Regulares ( search, findall, split, sub)
import re

cadena = "Tienes algo que contar. Te enseñaremos a hacerlo con estilo en tu propio blog."

#Buscar una palabera dentro de la cadena
expresion = re.search("contar",cadena)
# Retornaria 
    # -> <re.Match object; span=(16, 22), match='contar'>

#evaluacion de match
if(expresion):
    print("Expresion encontrada en la cadena")
else:
    print("No se ha encontrado palabra")

#Buscar que la cadena termine con estos caraaxteres
termina = re.search("blog.$",cadena)
# -> <re.Match object; span=(73, 78), match='blog.'>

#Buscar que la cadena empiece con estos caraaxteres
inicia = re.search("^Tienes",cadena)
# -> <re.Match object; span=(0, 6), match='Tienes'>

#Buscar que la cadena contengs caracteres o palabras 
# . cualquier caracter  * la cantidad  que sean
contenga = re.search("Te.*tu",cadena)
# -> <re.Match object; span=(24, 65), match='Te enseñaremos a hacerlo con estilo en tu'>

#findall
texto = """
Este mes, estamos encantados de ofrecer un seminario web sobre blogs,
fondo de color negro
¡impartido por completo por nuestros Happiness Engineers hispanoparlantes!
 Acompaña a nuestros expertos de WordPress en este webinar gratuito negro
 donde te enseñarán a crear, diseñar y gestionar un blog en WordPress.​com. 
En estas sesiones de 60 minutos de duración, 
fondo de color negro
aprenderás nuevas habilidades que harán que estés un paso más cerca de conseguir
 los objetivos que tienes para tu sitio, y también podrás hacer todas las preguntas
 fondo que quieras a nuestros expertos.negro
"""
# busca todas las concidencias y las develve en una lista
buscaTodo = re.findall("fondo.*negro", texto)
# -> ['fondo de color negro', 'fondo de color negro', 'fondo que quieras a nuestros expertos.negro']

#split
# separa el texto pasandole un patron \s espacio en blanco
texto2 = "El ordenador es roja  cuesta 6000"
patron = re.split("\s", texto2)
## -> ['El', 'ordenador', 'es', 'rojo', '', 'cuesta', '6000']

# sub sustituir todas las coincidencias de una cadena
sustitue = re.sub("roja","gris", texto2)
print(sustitue)
