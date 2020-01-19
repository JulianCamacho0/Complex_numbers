import sys
import math

def suma(cu, cd):

    a = cu[0] + cd[0]
    b = cu[1] + cd[1]

    r= [a,b]
    
    return r
    
def multi(cu, cd):

    a = cu[0]*cd[0] - cu[1]*cd[1]
    b =  cu[0]*cd[1] + cu[1]*cd[0]
    
    r = [a,b]
    
    return r

def resta(cu, cd):

    a = cu[0] - cd[0]
    b = cu[1] - cd[1]

    r= [a,b]
    
    return r

def  cociente(cu, cd):

    a = (cu[0]*cd[0] + cu[1]*cd[1]) / (cu[1] ** 2 + cd[1] ** 2 )
    b = (cu[1]*cd[0] - cu[0]*cd[1]) / (cu[1] ** 2 + cd[1] ** 2)
    
    r = [a,b]
    
    return r

def modulo(c):
    
    r = (c[0] ** 2 + c[1] ** 2) ** 0.5
    
    return r

def conju(c):
    
    r = [c[0], c[1] * -1]
    return r

def polares(c):
    
    p = (c[0] ** 2 + c[1] ** 2) ** 0.5
    gra = math.atan(c[1] / c[0])
    
    r = [p, gra]
    
    return r

def nice_print(rst):

    for i in rst:

        if i[0] == "Modulo":  
            print("Modulo de " +str(i[1][0]) + " + (" + str(i[1][1]) + ")i" " = " + str(i[2]))
            
        elif i[0] == "Conjugado":
            print( i[0] + " de " + str(i[1][0]) + " + (" + str(i[1][1]) + ")i" + " = "  + str(i[2][0]) + " + (" + str(i[2][1]) + ")i" )

        elif i[0] == "Conversion a polares":
            print( i[0] + " de " + str(i[1][0]) + " + (" + str(i[1][1]) + ")i" + " seria "  + "(" + str(i[2][0]) + ", " + str(i[2][1]) + ")" )
            
        else:
            print( "(" +str(i[1][0]) + "+(" + str(i[1][1]) + ")i) " + i[0] + " (" + str(i[2][0]) + "+(" + str(i[2][1]) + ")i)" + " = " + str(i[3][0]) + "+(" + str(i[3][1]) + ")i")

        

def main():
    
    a = [1, -2]
    b = [4, -3]

    resultados = [["+", a,b,suma(a,b)],["X", a,b, multi(a,b)],["-", a, b, resta(a,b)],["/", a, b, cociente(a,b)], [ "Modulo", b, modulo(b)],["Conjugado", a, conju(a)], ["Conversion a polares", b, polares(b)]] 
    nice_print(resultados)
    
main()
