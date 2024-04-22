import unittest

def fibonacci_no_recursivo(value):
    values = [0,1]

    for _ in range(value-1):
        values.append(values[-1]+values[-2])
  
    return values[value]

resultado = fibonacci_no_recursivo(13)
print(resultado)

class Test_fibonacci_no_recursivo(unittest.TestCase):
    def test_12(self):
        resultado = fibonacci_no_recursivo(12)
        self.assertEqual(resultado, 144)

    def test_10(self):
        resultado = fibonacci_no_recursivo(10)
        self.assertEqual(resultado, 55)

    def test_5(self):
        resultado = fibonacci_no_recursivo(5)
        self.assertEqual(resultado, 5)

    def test_7(self):
        resultado = fibonacci_no_recursivo(7)
        self.assertEqual(resultado, 13)

if __name__ == '__main__':
    unittest.main()