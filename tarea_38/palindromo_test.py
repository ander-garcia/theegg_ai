
import pytest
from palindromo import get_palindromo

testdata = [
    (31, 101),
    (456789, 1003001)
]


@pytest.mark.parametrize("numero,palindromo", testdata)
def test_palindromo(numero, palindromo):
    result = get_palindromo(numero)
    assert result == palindromo
