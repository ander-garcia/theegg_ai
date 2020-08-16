import pytest
from binario import decimal_to_binario

testdata = [
    (65, "1000001"),
    (128, "10000000"),
    (0, "0"),
    (1, "1"),
    (4, "100"),
    (3, "11"),
    (2, "10"),
    (5, "101")
]


@pytest.mark.parametrize("decimal,binario", testdata)
def test_decimal_to_binario(decimal, binario):
    result = decimal_to_binario(decimal)
    assert result == binario
