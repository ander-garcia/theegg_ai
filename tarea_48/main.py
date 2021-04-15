
import sys
from compressor import Compressor

texto = input(
    "Introduce cadena para comprimir, se recomienda no superar los 30 caracteres:\n")

compressor = Compressor()

comprimido = compressor.compress(texto)
print(f"COMPRIMIDO  = {comprimido}")
descomprimido = compressor.decompress(comprimido)
print(f"DESCOMPRIMIDO  = {descomprimido}")
print(
    f" tamaño texto original {sys.getsizeof(texto)}, comprimido {sys.getsizeof(comprimido)}, descomprimido {sys.getsizeof(descomprimido)}")
