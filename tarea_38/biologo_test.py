import pytest
from biologo import comparar_adn

testdata = [
    ("ctgactga", "actgagc", "actga"),
    ("cgtaattgcgat", "cgtacagtagc", "cgta"),
    ("ctgggccttgaggaaaactg", "gtaccagtactgatagt", "actg")
]


@pytest.mark.parametrize("cadena1,cadena2, comun", testdata)
def test_biologo(cadena1, cadena2, comun):
    result = comparar_adn(cadena1, cadena2)
    assert result == comun
