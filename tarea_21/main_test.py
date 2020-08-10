import pytest
from main import fraccion_irreducible 

testdata = [
    (0.125,1,8),
    (0.25,1,4),
    (0.002,1,500),
    (0.376,47,125),
]
@pytest.mark.parametrize("numero,numerador,denominador", testdata)
def test_fraccion_irreducible(numero,numerador,denominador):
    result = fraccion_irreducible(numero)
    assert result["numerador"] == numerador
    assert result["denominador"] == denominador