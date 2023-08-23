# UnitTest sirve para  crear pruebas dentro del codigo

def multiplicar(num1,num2):
    return num1 * num2

result = multiplicar(2,4)
print(result)

import unittest
# clase que tiene como parametro
class puebas(unittest.TestCase):

    def test(self):
        # test 2*4 = 8
        self.assertEqual(multiplicar(2,4),8)
if __name__== '__main__':
    unittest.main()

## -> resultado de salida de la ejecucion
"""
8
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
"""