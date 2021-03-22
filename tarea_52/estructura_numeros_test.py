import pytest
from estructura_numeros import EstructuraNumeros

estructura = EstructuraNumeros()


def test_crea_lista():
    lista = estructura.crea_lista()
    assert lista == []
    lista = estructura.insertar(lista, 5)
    assert lista == [5]
    lista = estructura.insertar(lista, 5)
    assert lista == [5, 5]
    lista = estructura.insertar(lista, 1)
    assert lista == [5, 5, 1]
    lista = estructura.insertar(lista, 2)
    assert lista == [5, 5, 1, 2]
    lista = estructura.insertar(lista, 1)
    assert lista == [5, 5, 1, 2, 1]


def test_eliminar_si_existe():
    lista = estructura.crea_lista([5, 16, 2, 5, 57, 5, 2])
    assert lista == [5, 16, 2, 5, 57, 5, 2]
    lista = estructura.eliminar_si_existe(lista, 12)
    assert lista == [5, 16, 2, 5, 57, 5, 2]
    lista = estructura.eliminar_si_existe(lista, 5)
    assert lista == [16, 2, 5, 57, 5, 2]
    lista = estructura.eliminar_si_existe(lista, 5)
    assert lista == [16, 2, 57, 5, 2]
    lista = estructura.eliminar_si_existe(lista, 5)
    assert lista == [16, 2, 57, 2]
    lista = estructura.eliminar_si_existe(lista, 5)
    assert lista == [16, 2, 57, 2]


def test_sumatorio():
    lista = estructura.crea_lista()
    assert estructura.sumatorio(lista) == 0
    lista = estructura.crea_lista([5, 16, 2, 5, 57, 5, 2])
    assert estructura.sumatorio(lista) == 92
    lista = estructura.crea_lista([5])
    assert estructura.sumatorio(lista) == 5


def test_eliminar_mayores():
    lista = estructura.crea_lista()
    assert estructura.eliminar_mayores(lista, 2) == []
    lista = estructura.crea_lista([5, 16, 2, 5, 57, 5, 2])
    assert estructura.eliminar_mayores(lista, 40) == [5, 16, 2, 5, 5, 2]
    assert estructura.eliminar_mayores(lista, 10) == [5, 2, 5, 5, 2]
    assert estructura.eliminar_mayores(lista, 2) == [2, 2]
    assert estructura.eliminar_mayores(lista, 1) == []


def test_numero_ocurrencias():
    lista = estructura.crea_lista()
    assert estructura.numero_ocurrencias(lista) == []
    lista = estructura.crea_lista([5])
    assert estructura.numero_ocurrencias(lista) == [(5, 1)]
    lista = estructura.crea_lista([5, 16, 2, 5, 57, 5, 2])
    assert estructura.numero_ocurrencias(
        lista) == [(5, 3), (16, 1), (2, 2), (57, 1)]
