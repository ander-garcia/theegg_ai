import pytest
from solitario import (normalizar_texto, convertir_a_numeros,
                       convertir_a_numero, convertir_a_letras,
                       convertir_a_letra, sumar_numeros, restar_numeros,
                       mover_carta, nueva_baraja, get_indice_primer_comodin,
                       get_indice_segundo_comodin, cortar_entre_comodines,
                       cortar_tras_valor_ultima_carta, generar_clave, cifrar, descifrar)

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


def test_mover_carta():
    baraja = nueva_baraja()
    assert baraja.index(53) == 52
    assert baraja.index(5) == 4
    assert get_indice_primer_comodin(baraja) == 52
    assert get_indice_segundo_comodin(baraja) == 53
    baraja = mover_carta(53, 3, baraja)
    assert baraja.index(53) == 2
    assert baraja.index(5) == 5
    assert get_indice_primer_comodin(baraja) == 2
    assert get_indice_segundo_comodin(baraja) == 53


testdata_cortar_entre_comodines = [
    ([2, 4, 6, 54, 5, 8, 7, 1, 53, 3, 9], [3, 9, 54, 5, 8, 7, 1, 53, 2, 4, 6]),
    ([2, 4, 6, 53, 5, 8, 7, 1, 54, 3, 9], [3, 9, 53, 5, 8, 7, 1, 54, 2, 4, 6]),
    ([53, 5, 8, 7, 1, 54, 3, 9], [3, 9, 53, 5, 8, 7, 1, 54]),
    ([53, 5, 8, 7, 1, 54], [53, 5, 8, 7, 1, 54])
]


@ pytest.mark.parametrize("baraja, resultado", testdata_cortar_entre_comodines)
def test_cortar_entre_comodines(baraja, resultado):
    assert cortar_entre_comodines(baraja) == resultado


testdata_cortar_tras_valor_ultima_carta = [
    ([7, 1, 2, 3, 11, 12, 13, 21,  4, 5, 31, 32, 32, 34, 8, 9],
     [5, 31, 32, 32, 34, 8, 7, 1, 2, 3, 11, 12, 13, 21,  4, 9]),
    ([1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9,
      10,
      11,
      12,
      13,
      14,
      15,
      16,
      17,
      18,
      19,
      20,
      21,
      22,
      23,
      24,
      25,
      26,
      27,
      28,
      29,
      30,
      31,
      32,
      33,
      34,
      35,
      36,
      37,
      38,
      39,
      40,
      41,
      42,
      43,
      44,
      45,
      46,
      47,
      48,
      49,
      50,
      51,
      52,
      53,
      54], [1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
            43,
            44,
            45,
            46,
            47,
            48,
            49,
            50,
            51,
            52,
            53,
            54]),


]


@pytest.mark.parametrize("baraja, resultado", testdata_cortar_tras_valor_ultima_carta)
def test_cortar_tras_valor_ultima_carta(baraja, resultado):
    assert cortar_tras_valor_ultima_carta(baraja) == resultado


def test_generar_clave_baraja_ordenada():
    clave = generar_clave(20)
    clave = "".join(clave)
    assert clave == "DWJXHYRFDGTMSHPUURXJ"


testdata_cifrar = [("aaaaa aaaaa", "EXKYIZSGEH", ""),
                   ("Code in Ruby, live longer!", "GLNCQMJAFFFVOMBJIYCB", ""),
                   ("SOLIT AIREX", "KIRAKSFJAN", "CRYPTONOMICON"),
                   ("AAAAA AAAAA AAAAA", "ITHZUJIWGRFARMW", "FOO")]


@ pytest.mark.parametrize("mensaje, cifrado,clave", testdata_cifrar)
def test_cifrar(mensaje, cifrado, clave):
    result = cifrar(mensaje, clave)
    assert result == cifrado
    result_descifrado = descifrar(result, clave)
    assert result_descifrado == normalizar_texto(mensaje)


def test_nueva_baraja():
    assert nueva_baraja("SOLITAIRE") == [49, 50, 51, 3, 4, 5, 6, 7, 8, 18, 11, 12, 13, 14, 17, 52, 19, 37, 53, 44, 45, 27, 28,
                                         15, 16, 9, 10, 54, 20, 1, 23, 24, 25, 26, 22, 29, 30, 31, 32, 33, 34, 35, 36, 2, 39, 40, 41, 42, 43, 21, 46, 47, 48, 38]
