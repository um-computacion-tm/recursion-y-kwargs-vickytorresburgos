import unittest

def escribir_nombre(*args,**kwargs):
    # print("inicio")
    for arg in args:
        print(arg)
        for key, value in kwargs.items():
            print(key,value)

escribir_nombre('Francisco, Facundo ,Emiliana',nombre1='Maria',nombre2='Victoria',apellido1='Torres',apellido2='Burgos')
escribir_nombre('Mercedes',nombre1='Valentina',apellido1='Artola')
escribir_nombre('Paula',nombre1='Celina',nombre2='Anahi',apellido1='Guerra Diaz')

class TestEscribirNombre(unittest.TestCase):

    def test_multiple_argumentos_multiple_keywords(self):
        self.assertEqual(escribir_nombre('Francisco, Facundo, Emiliana', nombre1='Maria', nombre2='Victoria', apellido1='Torres', apellido2='Burgos'), None)

    def test_un_argumento_un_keyword(self):
        self.assertEqual(escribir_nombre('Mercedes', nombre1='Valentina'), None)

    def test_un_argumento_multiple_keywords(self):
        self.assertEqual(escribir_nombre('Paula', nombre1='Celina', nombre2='Anahi', apellido1='Guerra Diaz'), None)

if __name__ == '__main__':
    unittest.main()  


