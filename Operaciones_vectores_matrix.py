#Operaciones con vectores y matricen en los complejos
#Autor: Julian Camacho
#Enero de 2019

import sys
import math

def suma(cu, cd):   
    """(list, list) -> list 
    Suma entre dos numero complejos"""

    a = cu[0] + cd[0]
    b = cu[1] + cd[1] 
    r= [a,b]
    
    return r

def multi(cu, cd):  
    """(list, list) -> list 
    Producto entre dos numero complejos"""

    a = cu[0]*cd[0] - cu[1]*cd[1]
    b =  cu[0]*cd[1] + cu[1]*cd[0]
    r = [a,b]

    return r


def resta(cu, cd): 
    """(list, list) -> list 
    Resta entre dos numero complejos"""

    a = cu[0] - cd[0]
    b = cu[1] - cd[1]
    r= [a,b]

    return r

def  cociente(cu, cd):
    """(list, list) -> list 
    Cociente entre dos numero complejos"""

    a = (cu[0]*cd[0] + cu[1]*cd[1]) / (cu[1] ** 2 + cd[1] ** 2 )
    b = (cu[1]*cd[0] - cu[0]*cd[1]) / (cu[1] ** 2 + cd[1] ** 2)
    r = [a,b]

    return r
def modulo(c):
    """(list) -> list 
    Modulo de un número complejo"""

    r = (c[0] ** 2 + c[1] ** 2) ** 0.5

    return r

def conju(c):
    """(list) -> list 
    Conjugado de un número complejo"""

    r = [c[0], c[1] * -1]

    return r

def suma_vectores(v_one, v_two):
    """(list, list) -> list
    Suma de dos vectores de la misma longitud cuyos elementos so numeros complejos"""

    r = []
    for i in range(len(v_one)):
        r = r + [suma(v_one[i], v_two[i])]
        
    return r

def inverso_vecom (v):
    """(list) -> list
    Inverso de un vector con numeros complejos"""

    r = []
    for i in v:
        f = []
        for j in i:
            f = f + [-j]
        r = r + [f]

    return r

def mult_vector_esca (c, v):
    """(list, list) -> list
    Multiplicacion de un vector complejo por un numero complejo"""

    r = []
    for i in v:
        r = r + [multi(c, i)]

    return r

def suma_matrices(m_one, m_two):
    """(list,list) -> list
    Suma de matrices cmplejas"""

    r = []
    for i in range(len(m_one)):
        r = r + [suma_vectores(m_one[i], m_two[i])]

    return r
        
def inver_matrix(m):
    """(list) -> list
    Inversa de un matriz"""

    r = []
    for i in m:
        r = r + [inverso_vecom(i)]

    return r
            
def matrix_escalar(c, m):
    """(list, list) -> list
    Multiplicacion de un numero complejo con una matriz compleja"""

    r = []
    for i in m:
        r = r + [mult_vector_esca(c,i)]

    return r

def matrix_trans(m):
    """(lista) -> list
    Matris transpuesta"""

    n = len(m)
    r = []
    for i in range(n):
        f = []
        for j in range(n):
            f = f + [m[j][i]]
        r = r + [f]

    return r

def matrix_conjugada(m):
    """(list) -> list
    La conjugada de una matris"""

    r = []
    for i in m:
        f = []
        for j in i:
            f = f + [conju(j)]
        r = r + [f]

    return r

def matriz_adjunta(m):

    r = matrix_conjugada(matrix_trans(m))
    return r
    
    
    
def main():
    
    c = [1, -2]
    
    v_one = [[1, 2], [4, -4], [0, 1]]
    v_two = [[4, 5], [3, 2], [3, 2]]
    
    m_one = [ [[1, 2] , [3, 4]] , [[-4, 3], [-1, -2]] ]
    m_two = [ [[-1, -2] , [-3, -4]] , [[4, -3], [1, 2]] ]

    print(suma_vectores(v_one, v_two))
    print(inverso_vecom(v_one))
    print(mult_vector_esca(c, v_one))
    print(suma_matrices(m_one, m_two))
    print(inver_matrix(m_one))
    print(matrix_escalar(c, m_one))
    print(matrix_trans(m_one))
    print(matrix_conjugada(m_one))
    print(matriz_adjunta(m_one))



main()
