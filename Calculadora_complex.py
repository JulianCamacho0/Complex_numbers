#Operaciones con numeros complejos
#Autor: Julian Camacho
#Enero de 2019

import sys
import math

#--------------------------------------------------------------------------------
#---------------------------- Operaciones numeros complejos -----------------------------
#--------------------------------------------------------------------------------

def suma(cu, cd):   
    """(list, list) -> list 
    Suma entre dos numeros complejos"""

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
    gra = math.atan2(c[1],c[0])
    r = [p, gra]
    
    return r

def fase_complex(c):
    """(list) -> list
    Fase de un numero complejo"""

    fase = math.atan2(c[1],c[0])

    return fase

def main():

#numero complejo representado por una lista de dos posiciones
    c_one = [1, -2]
    c_two = [4, 5]
  
main()
