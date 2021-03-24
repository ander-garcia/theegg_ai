import pytest
from sumatorio import Sumatorio


def test_suma_lineal():
    sumatorio = Sumatorio()
    assert sumatorio.suma_lineal(0) == 0
    assert sumatorio.suma_lineal(1) == 1
    assert sumatorio.suma_lineal(10) == 55
    assert sumatorio.suma_lineal(100) == 5050


def test_suma_constante():
    sumatorio = Sumatorio()
    assert sumatorio.suma_constante(0) == 0
    assert sumatorio.suma_constante(1) == 1
    assert sumatorio.suma_constante(10) == 55
    assert sumatorio.suma_constante(100) == 5050
