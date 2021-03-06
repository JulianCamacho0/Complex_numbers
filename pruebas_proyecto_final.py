
#Pruebas calculadora de complejos terminda
#Autor: Julian Camacho
#Febrero 2020

import unittest
import Proyecto_terminado

c_one = [1, -2]
c_two = [4, 5]
v_one = [[1, 2], [4, -4], [0,1]]
v_two = [[4, 5], [3, 2], [3, 2]]
v_thre =[[1,2],[3,4]]
m_one = [ [[1, 0] , [3, 4]] , [[3, -4], [-1, 0]] ]
m_two = [ [[-1, -2] , [-3, -4]] , [[4, -3], [1, 2]] ]



class TestStringMethods(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(Proyecto_terminado.suma(c_one, c_two), [5, 3])
    def test_multi(self):
        self.assertEqual(Proyecto_terminado.multi(c_one, c_two), [14, -3])
    def test_resta(self):
        self.assertEqual(Proyecto_terminado.resta(c_one, c_two), [-3, -7])
    def test_cociente(self):
        self.assertEqual(Proyecto_terminado.cociente(c_one, c_two), [-0.20689655172413793, -0.4482758620689655])
    def test_modulo(self):
        self.assertEqual(Proyecto_terminado.modulo(c_one), 2.23606797749979)
    def test_conju(self):
        self.assertEqual(Proyecto_terminado.conju(c_one),[1, 2])
    def test_polares(self):
        self.assertEqual(Proyecto_terminado.polares(c_one),[2.23606797749979, -1.1071487177940904])
    def test_fase_complex(self):
        self.assertEqual(Proyecto_terminado.fase_complex(c_one), -1.1071487177940904)

    def test_suma_vectores(self):
        self.assertEqual(Proyecto_terminado.suma_vectores(v_one, v_two), [[5, 7], [7, -2], [3, 3]])
    def test_inverso_vecom(self):
        self.assertEqual(Proyecto_terminado.inverso_vecom(v_one), [[-1, -2], [-4, 4], [0, -1]])
    def test_mult_vector_esca(self):
        self.assertEqual(Proyecto_terminado.mult_vector_esca(c_one, v_two), [[14, -3], [7, -4], [7, -4]])
    def test_conjugada_vector(self):
        self.assertEqual(Proyecto_terminado.conjugada_vector(v_one), [[1, -2], [4, 4], [0, -1]])
    def test_producto_interno(self):
        self.assertEqual(Proyecto_terminado.producto_interno(v_one, v_two), [20, 14])
    def test_norma_vector(self):
        self.assertEqual(Proyecto_terminado.norma_vector(v_one), 6.164414002968976)
    def test_distancia_vectores(self):
        self.assertEqual(Proyecto_terminado.distancia_vectores(v_one, v_two), 8.06225774829855)

    def test_suma_matrices(self):
        self.assertEqual(Proyecto_terminado.suma_matrices(m_one, m_two), [[[0, -2], [0, 0]], [[7, -7], [0, 2]]])
    def test_inver_matrix(self):
        self.assertEqual(Proyecto_terminado.inver_matrix(m_one), [[[-1, 0], [-3, -4]], [[-3, 4], [1, 0]]])
    def test_matrix_escalar(self):
        self.assertEqual(Proyecto_terminado.matrix_escalar(c_one, m_two), [[[-5, 0], [-11, 2]], [[-2, -11], [5, 0]]])
    def test_matrix_tranas(self):
        self.assertEqual(Proyecto_terminado.matrix_trans(m_one), [[[1, 0], [3, -4]], [[3, 4], [-1, 0]]])
    def test_matrix_conjugada(self):
        self.assertEqual(Proyecto_terminado.matrix_conjugada(m_one), [[[1, 0], [3, -4]], [[3, 4], [-1, 0]]])
    def test_matriz_adjunta(self):
        self.assertEqual(Proyecto_terminado.matriz_adjunta(m_one), [[[1, 0], [3, 4]], [[3, -4], [-1, 0]]])
    def test_producto_matrix(self):
        self.assertEqual(Proyecto_terminado.producto_matrix(m_one, m_two), [[[23, 5], [-8, 6]], [[-15, 1], [-26, -2]]])
    def test_accion_matrix(self):
        self.assertEqual(Proyecto_terminado.accion_matrix(v_thre, m_two), [[20, -56], [10, 30]])
    def test_matriz_unitaria(self):
        self.assertEqual(Proyecto_terminado.matriz_unitaria(m_one), False)
    def test_matriz_hermitiana(self):
        self.assertEqual(Proyecto_terminado.matriz_hermitiana(m_one), True)
    def test_p_tensor(self):
        self.assertEqual(Proyecto_terminado.p_tensor(m_one, m_two), [[[-1, -2], [-3, -4], [5, -10], [7, -24]], [[4, -3], [1, 2], [24, 7], [-5, 10]], [[-11, -2], [-25, 0], [1, 2], [3, 4]], [[0, -25], [11, 2], [-4, 3], [-1, -2]]])
        
    
    

if __name__ == '__main__':
    unittest.main()
    
def main():
    c_one = [1, -2]
    c_two = [4, 5]
    v_one = [[1, 2], [4, -4], [0,1]]
    v_two = [[4, 5], [3, 2], [3, 2]]
    v_thre =[[1,2],[3,4]]
    m_one = [ [[1, 0] , [3, 4]] , [[3, -4], [-1, 0]] ]
    m_two = [ [[-1, -2] , [-3, -4]] , [[4, -3], [1, 2]] ]


main()
