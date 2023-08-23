def sumar(numero1, numero2):
    """
    Esto es la documentacion de esta funcion
    Recibe dos parametros y devuelve la suma

    >>> sumar(4,3)
    7
    """
    return numero1 + numero2

resultado = sumar(2,4)
print(resultado)

import doctest
doctest.testmod()

#para ejecutar con la prueba seria 
## $python DocTest.py -v
# -> la salida seria 
"""
6
Trying:       
    sumar(4,3)
Expecting:    
    7
ok
1 items had no tests:
    __main__
1 items passed all tests:
   1 tests in __main__.sumar
1 tests in 2 items.
1 passed and 0 failed.
Test passed.
"""