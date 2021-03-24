from searcher import Searcher
import random

lista = [3, 56, 21, 33, 874, 123, 66, 1000,
         23, 45, 65, 56]
numero = 874
tool = Searcher(lista)
print(f"Lista original =  {tool.lista}")
print(
    f"Indice del número {numero} e iteraciones de búsqueda con el algoritmo secuencial =  {tool.secuential_search(numero)}")
tool.sort()
print(f"Lista ordenada =  {tool.lista}")
print(
    f"Indice del número {numero} e iteraciones de búsqueda con el algoritmo secuencial =  {tool.secuential_search(numero)}")
print(
    f"Indice del número {numero} e iteraciones de búsqueda con el algoritmo binario =  {tool.binary_search(numero)}")
