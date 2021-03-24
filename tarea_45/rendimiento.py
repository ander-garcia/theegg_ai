from searcher import Searcher
import random

sizes = [10, 50, 100, 500, 1000, 2000, 5000, 10000, 50000, 100000, 1000000]

for index, size in enumerate(sizes):
    max_int = 100000000
    random_list = random.sample(range(1, max_int), size)

    tool = Searcher(random_list)
    tool.sort()
    numero = tool.lista[0]
    print(
        f"{size};0;{tool.secuential_search(numero)[1]};'secuential'")
    print(
        f"{size};0;{tool.binary_search(numero)[1]};'binary_search'")

    numero = tool.lista[len(tool.lista)//2]
    print(
        f"{size};{len(tool.lista)//2};{tool.secuential_search(numero)[1]};'secuential'")
    print(
        f"{size};{len(tool.lista)//2};{tool.binary_search(numero)[1]};'binary_search'")
    numero = tool.lista[-1]
    print(
        f"{size};-1;{tool.secuential_search(numero)[1]};'secuential'")
    print(
        f"{size};-1;{tool.binary_search(numero)[1]};'binary_search'")
