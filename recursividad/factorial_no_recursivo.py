import unittest

# def sumatoria(value):
#     if value > 0:
#         resultado = value + sumatoria(value-1)
#         return resultado
#     else:
#         return 0
    
# resultado = sumatoria(8)

# print(sumatoria)


# def sumatoria(value):
#     #condicion de corte
#     if value == 0:
#         return 0
#     #proceso recursivo
#     return value + sumatoria(value-1)
    
# resultado = sumatoria(8)

# print(sumatoria)

#factorial while (no recursivo)

def factorial_no_recursivo(value): 
    resultado = 1 
    while value > 1: 
        resultado *= value
        value -= 1
    return resultado
    
class Test_factorial_no_recursivo(unittest.TestCase):
    def test_5(self):
        resultado = factorial_no_recursivo(5)
        self.assertEqual(resultado,120)
    
    def test_10(self):
        resultado = factorial_no_recursivo(10)
        self.assertEqual(resultado, 3628800)
    
    def test_3(self):
        resultado = factorial_no_recursivo(3)
        self.assertEqual(resultado, 6)

    def test_7(self):
        resultado = factorial_no_recursivo(7)
        self.assertEqual(resultado, 5040)

    

if __name__ == '__main__':
    unittest.main()