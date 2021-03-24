from sumatorio import Sumatorio
import time


sumatorio = Sumatorio()

cantidad = 100000
for i in range(6):
    t0 = time.time()
    suma1 = sumatorio.suma_lineal(cantidad)
    t1 = time.time()
    suma2 = sumatorio.suma_constante(cantidad)
    t2 = time.time()
    print(f"{suma1};{t1-t0}")
    print(f"{suma2};{t2-t1}")
    cantidad = cantidad * 10
