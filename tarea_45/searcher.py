import collections


class Searcher():

    def __init__(self, lista):
        self.lista = lista

    def sort(self):
        # ordena la lista con el algoritmo merge sort
        # y la devuelve
        self.merge_sort(self.lista)
        return self.lista

    def is_sorted(self, lista):
        is_sorted = True
        if len(lista) == 0:
            return True
        previous_value = lista[0]
        for index, value in enumerate(lista):
            if previous_value > value:
                is_sorted = False
                break
            previous_value = value
        return is_sorted

    def binary_search(self, number, iteraciones=0, index_offset=0, lista=None):
        # busca un valor en la lista (TIENE QUE ESTAR ORDENADA) con el algoritmo binario
        # y devuelve su índice y el número de iteraciones
        # si no lo encuentra devuelve -1
        if lista is None:
            # el parametro lista será None sólo cuando se llama desde fuera
            lista = self.lista
            if not self.is_sorted(lista):
                raise Exception(
                    "la búsqueda binaria necesita que el array este ordenado")
        if len(lista) == 0:
            return (-1, iteraciones)

        iteraciones = iteraciones + 1
        if lista[0] > number or lista[len(lista)-1] < number:
            return (-1, iteraciones)
        mitad = len(lista)//2
        if lista[mitad] > number:
            return self.binary_search(number, iteraciones, index_offset, lista[:mitad])
        elif lista[mitad] < number:
            return self.binary_search(number, iteraciones, index_offset+mitad, lista[mitad:])
        elif lista[mitad] == number:
            return (index_offset + mitad, iteraciones)
        else:
            return (-1, iteraciones)

    def secuential_search(self, number):
        # busca un valor en la lista (NO TIENE PORQUE ESTAR ORDENADA) con el algoritmo secuencial
        # y devuelve su índice y el número de iteraciones
        # si no lo encuentra devuelve -1
        number_index = -1
        iteraciones = 0
        for index, value in enumerate(self.lista):
            iteraciones = iteraciones + 1
            if value == number:
                number_index = index
                break
        return number_index, iteraciones

    def merge_sort(self, lista):
        if len(lista) > 1:
            # dividir por la mitad
            mitad = len(lista)//2
            izquierda = lista[:mitad]
            derecha = lista[mitad:]
            # ordenar cada mitad
            self.merge_sort(izquierda)
            self.merge_sort(derecha)
            # juntar mitades de forma ordenada
            indice_izquierdo = indice_derecho = indice_ordenado = 0
            while indice_izquierdo < len(izquierda) and indice_derecho < len(derecha):
                if (izquierda[indice_izquierdo] <= derecha[indice_derecho]):
                    lista[indice_ordenado] = izquierda[indice_izquierdo]
                    indice_ordenado = indice_ordenado + 1
                    indice_izquierdo = indice_izquierdo + 1
                else:
                    lista[indice_ordenado] = derecha[indice_derecho]
                    indice_ordenado = indice_ordenado + 1
                    indice_derecho = indice_derecho + 1
            # añadir elementos restantes
            while indice_izquierdo < len(izquierda):
                lista[indice_ordenado] = izquierda[indice_izquierdo]
                indice_ordenado = indice_ordenado + 1
                indice_izquierdo = indice_izquierdo + 1
            while indice_derecho < len(derecha):
                lista[indice_ordenado] = derecha[indice_derecho]
                indice_ordenado = indice_ordenado + 1
                indice_derecho = indice_derecho + 1
            return
        else:
            return
