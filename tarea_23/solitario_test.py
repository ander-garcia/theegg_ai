import pytest
from solitario import (normalizar_texto, convertir_a_numeros,
                       convertir_a_numero, convertir_a_letras, convertir_a_letra, sumar_numeros, restar_numeros)

testdata_normalizar = [("a b, c ü", "ABCU"), (" .á b ñ ", "ABN")]


@pytest.mark.parametrize("texto, texto_normalizado", testdata_normalizar)
def test_normalizar_texto(texto, texto_normalizado):
    result = normalizar_texto(texto)
    assert result == texto_normalizado


testdata_convertir_a_numeros = [(["A", "B", "Z"], [1, 2, 26]),
                                (['D', 'O', 'N', 'O', 'T', 'U', 'S',
                                  'E', 'P', 'C'], [4, 15, 14, 15, 20, 21, 19, 5, 16, 3])
                                ]


@ pytest.mark.parametrize("letras, numeros", testdata_convertir_a_numeros)
def test_convertir_a_numeros(letras, numeros):
    result = convertir_a_numeros(letras)
    assert result == numeros


@ pytest.mark.parametrize("letras, numeros", testdata_convertir_a_numeros)
def test_convertir_a_letras(letras, numeros):
    result = convertir_a_letras(numeros)
    assert result == letras


testdata_sumar_numeros = [([4, 15, 14, 15, 20,  21, 19, 5, 16, 3], [11, 4, 23, 21, 16, 15, 14, 15, 23, 20], [15, 19, 11, 10, 10, 10, 7, 20, 13, 23])

                          ]


@ pytest.mark.parametrize("array1, array2,suma", testdata_sumar_numeros)
def test_sumar_numeros(array1, array2, suma):
    result = sumar_numeros(array1, array2)
    assert result == suma


@ pytest.mark.parametrize("resta, array2,array1", testdata_sumar_numeros)
def test_restar_numeros(resta, array2, array1):
    result = restar_numeros(array1, array2)
    assert result == resta
