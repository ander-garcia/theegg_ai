
import pytest
from palindromo import get_palindromo, is_primo, is_palindromo

testdata = [
    (2, 2),
    (3, 3),
    (4, 5),
    (31, 101),
    (456789, 1003001)
]

testdata_is_palindromo = [
    (2, True),
    (44, True),
    (54, False),
    (5445, True),
    (31, False),
    (1003001, True)
]

testdata_is_primo = [
    (2, True),
    (44, False),
    (54, False),
    (5445, False),
    (101, True),
    (1003001, True)
]


@pytest.mark.parametrize("numero,palindromo", testdata)
def test_palindromo(numero, palindromo):
    result = get_palindromo(numero)
    assert result == palindromo


@pytest.mark.parametrize("numero,palindromo", testdata_is_palindromo)
def test_is_palindromo(numero, palindromo):
    result = is_palindromo(numero)
    assert result == palindromo


@pytest.mark.parametrize("numero,primo", testdata_is_primo)
def test_is_primo(numero, primo):
    result = is_primo(numero)
    assert result == primo
