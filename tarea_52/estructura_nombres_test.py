import pytest
from estructura_nombres import EstructuraNombres


def test_union_sin_duplicados():
    estructura = EstructuraNombres(["a", "b", "a", "c", "d"])
    lista = sorted(estructura.union_sin_duplicados(
        ["a", "e"]))
    assert lista == ["a", "b", "c", "d", "e"]
    lista = sorted(estructura.union_sin_duplicados(
        ["a", "a"]))
    assert lista == ["a", "b", "c", "d"]


def test_interseccion():
    estructura = EstructuraNombres(["a", "b", "a", "c", "d"])
    lista = sorted(estructura.interseccion(
        ["a", "e", "f"]))
    assert lista == ["a"]
    lista = sorted(estructura.interseccion(
        ["a", "a", "c"]))
    assert lista == ["a", "c"]
    lista = sorted(estructura.interseccion(
        ["af", "af"]))
    assert lista == []
    lista = sorted(estructura.interseccion(
        ["a", "b", "a", "c", "d"]))
    assert lista == ["a", "b", "c", "d"]


def test_diferentes_sin_duplicados():
    estructura = EstructuraNombres(["a", "b", "a", "c", "d"])
    lista = sorted(estructura.diferentes_sin_duplicados(
        ["a", "e", "f"]))
    assert lista == ["b", "c", "d"]
    lista = sorted(estructura.diferentes_sin_duplicados(
        ["a", "a", "c"]))
    assert lista == ["b", "d"]
    lista = sorted(estructura.diferentes_sin_duplicados(
        ["af", "af"]))
    assert lista == ["a", "b", "c", "d"]
    lista = sorted(estructura.diferentes_sin_duplicados(
        []))
    assert lista == ["a", "b", "c", "d"]
    lista = sorted(estructura.diferentes_sin_duplicados(
        ["a", "b", "c", "d"]))
    assert lista == []
