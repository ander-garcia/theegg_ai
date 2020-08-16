import pytest
from binario import decimal_to_binario

testdata = [
    (65, "1000001"),
    (0, "0"),
    (1, "1"),
    (2, "10"),
    (5, "101")
]


@pytest.mark.parametrize("decimal,binario", testdata)
def test_fraccion_irreducible(decimal, binario):
    result = decimal_to_binario(decimal)
    assert result == binario
