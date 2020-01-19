import unittest
import Calculadora_complex
c1 = [1, 2]
c2 = [3, -4]
c3 = [-4, -5]
c4 = [6, 5]

class TestStringMethods(unittest.TestCase):
    
    def test_suma(self):
        self.assertEqual(Calculadora_complex.suma(c1, c2), [4,-2])
        
    def test_suma_dos(self):
        self.assertEqual(Calculadora_complex.suma(c3, c4), [2,0])

    def test_resta(self):
        self.assertEqual(Calculadora_complex.resta(c1, c2), [-2,6])

    def test_resta_dos(self):
        self.assertEqual(Calculadora_complex.resta(c3, c4), [-10,-10])

    
    def test_producto(self):
        self.assertEqual(Calculadora_complex.multi(c1, c2), [11,2])

    def test_producto_dos(self):
        self.assertEqual(Calculadora_complex.multi(c3, c4), [1,-50])

    def test_cociente(self):
        self.assertEqual(Calculadora_complex.cociente(c1, c2), [-0.25,0.5])

    def test_cociente_dos(self):
        self.assertEqual(Calculadora_complex.cociente(c3, c4), [-0.98,-0.2])

    def test_modulo(self):
        self.assertEqual(Calculadora_complex.modulo(c1),2.23606797749979 )

    def test_modulo_dos(self):
        self.assertEqual(Calculadora_complex.modulo(c4),7.810249675906654 )

    def test_conjugado(self):
        self.assertEqual(Calculadora_complex.conju(c1) , [1, -2])

    def test_conjugado_dos(self):
        self.assertEqual(Calculadora_complex.conju(c4), [6, -5])

    def test_polares(self):
        self.assertEqual(Calculadora_complex.polares(c1), [2.23606797749979, 1.1071487177940904])

    def test_polares_dos(self):
        self.assertEqual(Calculadora_complex.polares(c4), [7.810249675906654, 0.6947382761967033])
        
if __name__ == '__main__':
    unittest.main()
    
def main():
    c1 = [1, 2]
    c2 = [3, 4]
    c3 = [-4, -5]
    c4 = [6, 5]
main()
