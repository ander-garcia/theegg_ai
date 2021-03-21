import collections


class EstructuraNumeros():

    def __init__(self):
        pass

    def crea_lista(self, lista=[]):
        return lista.copy()

    def insertar(self, lista=[], numero=0):
        return lista + [numero]

    def eliminar_si_existe(self, lista=[], numero=0):
        try:
            index = lista.index(numero)
        except ValueError:
            print(f"El numero {numero} no está en la lista")
            return self.crea_lista(lista)
        return lista[0:index]+lista[index+1:]

    def sumatorio(self, lista=[]):
        return sum(lista)

    def eliminar_mayores(self, lista=[], numero=0):
        menores_iguales = [i for i in lista if i <= numero]
        return menores_iguales

    def numero_ocurrencias(self, lista=[]):
        ocurrencias = list(collections.Counter(lista).items())
        return ocurrencias
