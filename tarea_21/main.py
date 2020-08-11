import sys
from fraccion import fraccion_irreducible 

try:
    num = float(sys.argv[1])
    if (num<0 or num>1):
        print ("El número de entrada debe ser mayor qe 0 y menor que 1")
        exit(0)
except:
    print ("Error de lectura de parámetros de entrada. Es necesario un parámetro de un número decimal entre 0 y 1 de no más de 4 decimales. Ejemplo python main.py 0.5")
    exit(0)
result = fraccion_irreducible(num)
print (f"{num} = {result['numerador']} / {result['denominador']}")
