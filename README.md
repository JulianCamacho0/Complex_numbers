# Conjunto de los números complejos
Trataremos los números complejos, matrices y vectores todas estas con entrada complejas. Operaciones básicas entre estos elementos.

# Empecemos
Encontrará dos calculadoras construidas desde Python, con sus respectivos programas de pruebas. Una netamente operaciones de números complejos, estos los representaremos mediante una lista ([,]) de dos posiciones, mientras que la otra calculadora trata además de los números complejos, matrices y vectores con entradas complejas.

# Prerrequisitos
Necesita un conocimiento básico del lenguaje Python además de saber sobre el cuerpo de los complejos y sus espacios vectoriales.

# Ejecutar o instalar
Para usar esta calculadora además de sus respectivas pruebas debe descargar sus respectivos códigos, para esto seleccione la opcion -Clone or download- que se encuentra en la pagina principal y se identifica por el color verde, a continuacion se descargara una carpeta comprimida con todos los programas (debe descomprimirla).

Además usted en la función principal de la calculadora (def main() ) puede modificar o editar los números complejos, vectores y/o matrices, siguiendo el respectivo formato que el programa utiliza.

ejemplo:

en la función principal puede encontrar lo siguiente:

los números complejos se representan por el siguiente formato
c_one=[1,4]
c_two=[3,-5]

Los vectores:
v_one[[2,4],[3-8],[2.-34]]

Matrices:
m_one=[[[2,4],[3-8],[2.-34]],[[3,-8],[0-8],[2.0]]]

usted puede editar todos estos elementos siempre y cuando sigan el respectivo formato.

# Ejemplo
En la carpeta -Projyecto_terminado- encontrara en la funcion principal (def main():) lo siguiente:
#
#
def main():
#numero complejo representado por una lista de dos posiciones
    c_one = [1, -2]
    c_two = [4, 5]

#Vectores complejos son representado por vectores usuales, pero con entradas (elemntos) complejos
    v_one = [[1, 2], [4, -4], [0,1]]
    v_two = [[4, 5], [3, 2], [3, 2]]
    v_thre =[[1,2],[3,4]]

#Matrices complejas son representados por matrices usuales pero sus filas son vectores complejos
    m_one = [ [[1, 0] , [3, 4]] , [[3, -4], [-1, 0]] ]
    m_two = [ [[-1, -2] , [-3, -4]] , [[4, -3], [1, 2]] ]
    
main()
#
#
Si desea usar la funcion de multiplicacion de complejos (def multi(v_one,v_two):) y que le aparesca en pantalla la respuesta debe hacer lo siguiente en la funcion principal:

def main():

  print(multi(c_one, c_two))
  
 donde c_one y c_two son los numeros complejos a multiplicar, print() funcion para que le apresca en pantalla el resultado. como dije anteriormente usted puede editar c_one y/o c_two.  


# Correr las pruebas
El siguiente paso después de el paso inmediatamente anterior (Ejecutar o instalar) simplemente debe darle a la tecla -F5- que usualmente se encuentra en la parte superior de su teclado, el programa inmediatamente se ejecutara. Tenga en cuenta que la calculadora debe ser guardada con el nombre Proyecto_terminado.

# Edite las pruebas
Importe una librería que me testea cada función, usted puede editar estas teniendo en cuenta que la respuesta la debe hacer mediante otra calculadora confiable y seguir el formato respectivo que requiere el programa. Tenga en cuenta que la calculadora debe ser guardada con el nombre Proyecto_terminado.

# Autor
Julián Felipe Camacho Rico
estudiante de la universidad: Escuela Colombiana de Ingeniería Julio Garavito.
Programa de Matemáticas.


