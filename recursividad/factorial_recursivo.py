#factorial_recursivo recursivo

import unittest

def factorial_recursivo(value):
    #condicion de corte
    if value in (0,1):
        return 1
    #llamada recursiva
    return value * factorial_recursivo(value-1)

resultado = factorial_recursivo(5)
print(resultado)

class Test_factorial(unittest.TestCase):
    def test_5(self):
        resultado = factorial_recursivo(5)
        self.assertEqual(resultado, 120)

    def test_8(self):
        resultado = factorial_recursivo(8)
        self.assertEqual(resultado, 40320)

    def test_6(self):
        resultado = factorial_recursivo(6)
        self.assertEqual(resultado, 720)

    def test_4(self):
        resultado = factorial_recursivo(4)
        self.assertEqual(resultado, 24)
    
if __name__ == '__main__':
    unittest.main()
