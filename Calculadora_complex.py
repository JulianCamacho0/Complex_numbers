#Operaciones con vectores y matricen en los complejos
#Autor: Julian Camacho
#Enero de 2019

import sys
import math

#----------------------------------------------- Operaciones complejos -------------------------------------------------------

def suma(cu, cd):   
    """(list, list) -> list 
    Suma entre dos numero complejos"""

    a = cu[0] + cd[0]
    b = cu[1] + cd[1] 
    r= [a,b]
    
    return r

def multi(cu, cd):  
    """(list, list) -> list 
    Producto entre dos numeros complejos"""

    a = cu[0]*cd[0] - cu[1]*cd[1]
    b =  cu[0]*cd[1] + cu[1]*cd[0]
    r = [a,b]
    
    return r

def resta(cu, cd): 
    """(list, list) -> list 
    Resta entre dos numeros complejos"""
    
    a = cu[0] - cd[0]
    b = cu[1] - cd[1]
    r= [a,b]
    
    return r

def  cociente(cu, cd):
    """(list, list) -> list 
    Cociente entre dos numeros complejos"""

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

def polares(c):
    """(list) -> list 
    Dado un numero complejo (Representacion en coordenadas cartecianas)
    se convertira a cordenadas polares de la forma (p,o°)"""

    p = (c[0] ** 2 + c[1] ** 2) ** 0.5
    gra = math.atan2(c[1] / c[0])
    r = [p, gra]
    
    return r

def nice_print(rst):
    """(list) -> none 
    Funcion para inprimir en su forma estandas (a+bi) las operaciones entre complejos"""

    for i in rst:

        if i[0] == "Modulo":  
            print("Modulo de " +str(i[1][0]) + " + (" + str(i[1][1]) + ")i" " = " + str(i[2]))
            
        elif i[0] == "Conjugado":
            print( i[0] + " de " + str(i[1][0]) + " + (" + str(i[1][1]) + ")i" + " = "  + str(i[2][0]) + " + (" + str(i[2][1]) + ")i" )

        elif i[0] == "Conversion a polares":
            print( i[0] + " de " + str(i[1][0]) + " + (" + str(i[1][1]) + ")i" + " seria "  + "(" + str(i[2][0]) + ", " + str(i[2][1]) + ")" )

        else:
            print( "(" +str(i[1][0]) + "+(" + str(i[1][1]) + ")i) " + i[0] + " (" + str(i[2][0]) + "+(" + str(i[2][1]) + ")i)" + " = " + str(i[3][0]) + "+(" + str(i[3][1]) + ")i")

#----------------------------------------------------- Operaciones Vectores complejos-----------------------------------------------------------

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

def producto_interno(v_one, v_two):
    """(list, list) -> list
    Calcula el producto interno de dos vectores"""

    r = [0,0]
    conju_v_one = []
    for i in v_one:
        conju_v_one = conju_v_one + [conju(i)]
    for j in range(len(v_one)):
        r = suma( r,multi(conju_v_one[j], v_two[j]) )
        

    return r
    

#----------------------------------------------- Operacion Matrices complejas --------------------------------------------

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
    La conjugada de una matriz"""

    r = []
    for i in m:
        f = []
        for j in i:
            f = f + [conju(j)]
        r = r + [f]
        
    return r

def matriz_adjunta(m):
    """(list) -> list
    Dada una matriz cuadrada, le calcula su conjugado"""
    
    r = matrix_conjugada(matrix_trans(m))
    return r

def producto_matrix(m,n):
    """(list, list) -> list
    Funcion que calcula el prodcto de dos matrices"""
    
    ma = [[[0,0] for j in range(len(n[0][0]))] for i in range(len(m))]

    for i in range(len(m)):
        for j in range(len(n[0])):
            for k in range(len(n)):
                ma[i][j] = suma(ma[i][j], multi(m[i][k], n[k][j]))
    return ma

def accion_matrix(m,n):
    """(list, list) -> list
    Calcula la accion de una matriz sobre un vector"""
    
    ma = [[0,0] for j in range(len(n))]

    for i in range(len(m)):
        for j in range(len(n)):
            for k in range(len(n)):
                ma[i] = suma(ma[i], multi(m[i][k], n[k]))

    return(ma)
    

    
def main():
    
    c = [1, -2]

    v_one = [[1, 2], [4, -4]]
    v_two = [[4, 5], [3, 2], [3, 2]]
    
    m_one = [ [[1, 2] , [3, 4]] , [[-4, 3], [-1, -2]] ]
    m_two = [ [[-1, -2] , [-3, -4]] , [[4, -3], [1, 2]] ]
    

##    print(suma_vectores(v_one, v_two))
##    print(inverso_vecom(v_one))
##    print(mult_vector_esca(c, v_one))
##    print(suma_matrices(m_one, m_two))
##    print(inver_matrix(m_one))
##    print(matrix_escalar(c, m_one))
##    print(matrix_trans(m_one))
##    print(matrix_conjugada(m_one))
##    print(matriz_adjunta(m_one))
##    print(producto_matrix(m_one, m_two))
##    print(accion_matrix(m_one, v_one))
##    print(producto_interno(v_one, v_one))

main()
