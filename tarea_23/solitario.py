def normalizar_texto(texto):
    normalizado = eliminar_no_alfanumericos(texto).upper()
    normalizado = remplazar_letras(normalizado)
    return normalizado


def remplazar_letras(texto):
    replacements = (
        ("Á", "A"),
        ("É", "E"),
        ("Í", "I"),
        ("Ó", "O"),
        ("Ú", "U"),
        ("Ñ", "N"),
        ("Ü", "U"),
        (",", ""),
        (".", "")
    )
    for a, b in replacements:
        texto = texto.replace(a, b).replace(a.upper(), b.upper())
    return texto


def eliminar_no_alfanumericos(texto):
    # Given a text string, remove all non-alphanumeric
    # characters (using Unicode definition of alphanumeric).
    import re
    sin_alfanumericos = "".join(re.compile(r'\W+', re.UNICODE).split(texto))
    return sin_alfanumericos


def convertir_a_numeros(letras):
    numeros = []
    for letra in letras:
        numeros.append(convertir_a_numero(letra))
    return numeros


def convertir_a_numero(letra):
    # @ es el caracter anterior a "A"
    numero_letra_anterior_A = ord('@')
    numero = ord(letra) - numero_letra_anterior_A
    return numero


def convertir_a_letras(numeros):
    letras = []
    for numero in numeros:
        letras.append(convertir_a_letra(numero))
    return letras


def convertir_a_letra(numero):
    # @ es el caracter anterior a "A"
    numero_letra_anterior_A = ord('@')
    letra = chr(numero_letra_anterior_A+numero)
    return letra


def sumar_numeros(array1, array2):
    suma = [(array1[i]+array2[i]) % 26 for i in range(len(array1))]
    return suma


def restar_numeros(array1, array2):
    resta = [(array1[i]-array2[i]) % 26 for i in range(len(array1))]
    return resta
