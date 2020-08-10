import sys


def fraccion_irreducible (numero, referencia_decimales = 10000):
    denominador = referencia_decimales
    numerador = int(numero*denominador)
    max_numero = numerador
    divisor_comun = 2
    while max_numero >= divisor_comun:
        if (numerador%divisor_comun) == 0 and (denominador%divisor_comun) == 0:
            numerador = numerador/divisor_comun
            denominador = denominador/divisor_comun
            max_numero = numerador
        else:
            divisor_comun = divisor_comun +1
    numerador = int (numerador)
    denominador = int (denominador)
    return {"numerador" : numerador,"denominador":denominador}

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
