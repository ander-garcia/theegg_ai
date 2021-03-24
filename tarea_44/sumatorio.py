

class Sumatorio():

    def __init__(self):
        pass

    def suma_constante(self, n):
        suma = (n/2)*(n+1)
        return suma

    def suma_lineal(self, n):
        suma = 0
        for i in range(1, n+1):
            suma = suma + i
        return suma
