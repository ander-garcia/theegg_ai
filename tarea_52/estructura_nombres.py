import collections


class EstructuraNombres():

    def __init__(self, nombres=[]):
        self.nombres = nombres.copy()
        pass

    def union_sin_duplicados(self, segunda_lista=[]):
        return list(set(self.nombres).union(set(segunda_lista)))

    def interseccion(self, segunda_lista=[]):
        return list(set(self.nombres).intersection(set(segunda_lista)))

    def diferentes_sin_duplicados(self, segunda_lista=[]):
        return list(set(self.nombres).difference(set(segunda_lista)))
