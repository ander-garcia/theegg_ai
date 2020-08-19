import pytest
from pokemon import Pokemon


def test_combate_pokemon_1():
    pikachu = Pokemon("Pikachu", 100, 55, 1)
    jiggly = Pokemon("Jigglypuff", 100, 45, 0)
    turno = 1
    ganador = Pokemon.combate(pikachu, jiggly, turno)
    assert ganador == pikachu
    assert pikachu.vida == 55
    assert jiggly.vida == -10


def test_combate_pokemon_2():
    pikachu = Pokemon("Pikachu", 100, 55, 1)
    jiggly = Pokemon("Jigglypuff", 100, 45, 0)
    turno = 0
    ganador = Pokemon.combate(pikachu, jiggly, turno)
    assert ganador == pikachu
    assert pikachu.vida == 10
    assert jiggly.vida == -10
