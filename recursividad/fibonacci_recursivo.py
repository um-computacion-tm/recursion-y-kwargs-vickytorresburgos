import unittest

def fibonacci_recursivo(value):
    #condicion de corte
    if value == 0:
        return 0
    if value == 1:
        return 1
    #llamada recursiva
    return fibonacci_recursivo(value-1) + fibonacci_recursivo(value-2)

resultado = fibonacci_recursivo(2)
print(resultado)

class Test_fibonacci_recursivo(unittest.TestCase):
    def test_9(self):
        resultado = fibonacci_recursivo(9)
        self.assertEqual(resultado, 34)
 
    def test_5(self):
        resultado = fibonacci_recursivo(5)
        self.assertEqual(resultado, 5)

    def test_11(self):
        resultado = fibonacci_recursivo(11)
        self.assertEqual(resultado, 89)

    def test_12(self):
        resultado = fibonacci_recursivo(12)
        self.assertEqual(resultado, 144)

    def test_7(self):
        resultado = fibonacci_recursivo(7)
        self.assertEqual(resultado, 13)




if __name__ == '__main__':
    unittest.main()  
