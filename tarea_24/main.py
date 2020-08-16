import sys
from binario import decimal_to_binario

try:
    num = int(sys.argv[1])

except:
    print("Error de lectura de parámetros de entrada. Es necesario un parámetro que se pueda convertir a un número entero")
    exit(0)
result = decimal_to_binario(num)
print(f"{num} = {result}")
