import pytest
from lechero import elegir_vacas

testdata = [
    (6, 700, [360, 250, 400, 180, 50, 90], [40, 35, 43, 28, 12, 13], 93),
    (8, 1000, [223, 243, 100, 200, 200, 155, 300, 150],
     [30, 34, 28, 45, 31, 50, 29, 1], 188),
    (10, 2000, [340, 355, 223, 243, 130, 240, 260, 155, 302, 130],
     [45, 50, 34, 39, 29, 40, 30, 52, 31, 1], 320)
]


@pytest.mark.parametrize("vacas_venta, kg_camion, peso_vacas, litros_leche_vacas,produccion_maxima", testdata)
def test_fraccion_irreducible(vacas_venta, kg_camion, peso_vacas, litros_leche_vacas, produccion_maxima):
    result = elegir_vacas(vacas_venta, kg_camion,
                          peso_vacas, litros_leche_vacas)
    assert result == produccion_maxima
