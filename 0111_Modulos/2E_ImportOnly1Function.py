# Utilizando mi Modulo pero solo una determinda funcion no todo sera cargado
from OE_Modulo1 import ingresaFloat as floats

valor = int(input('Ingresa cantidad de datos tipo Float '))
listaFloat = floats(valor)
print(listaFloat)


# instalar modulos con pip
# pip --version
# veremos si esta instalado y que version esta  usando
# -> pip 22.2.2 from  lib\site-packages\pip (python 3.10)
# pip list  - ver pauetes instalados
# pip install camelcase  - nombre del modulo
# pip uninstall camelcase - para desinstalar
