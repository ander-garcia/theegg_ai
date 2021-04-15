import pytest
from compressor import Compressor

testdata = [
    ("aba", [(0, 1, 'a'), (0, 1, 'b'), (2, 1, '')]),
    ("word word", [(0, 1, 'w'), (0, 1, 'o'),
                   (0, 1, 'r'), (0, 1, 'd'), (0, 1, ' '), (5, 4, '')]),
    ("abababab", [(0, 1, 'a'), (0, 1, 'b'), (2, 6, '')])
]


@pytest.mark.parametrize("texto,texto_comprimido", testdata)
def test_compress_decompress(texto, texto_comprimido):
    compressor = Compressor()
    comprimido = compressor.compress(texto)
    descomprimido = compressor.decompress(comprimido)
    assert texto == descomprimido
    assert comprimido == texto_comprimido
