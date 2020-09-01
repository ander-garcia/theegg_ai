import random
import re


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
        ("Ü", "U")
    )
    for a, b in replacements:
        texto = texto.replace(a, b).replace(a.upper(), b.upper())
    return texto


def eliminar_no_alfanumericos(texto):
    # Given a text string, remove all non-alphanumeric
    # characters (using Unicode definition of alphanumeric).
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
    for i in range(len(suma)):
        if suma[i] == 0:
            suma[i] = 26
    return suma


def restar_numeros(array1, array2):
    resta = [(array1[i]-array2[i]) % 26 for i in range(len(array1))]
    for i in range(len(resta)):
        if resta[i] == 0:
            resta[i] = 26
    return resta


def nueva_baraja():
    # crea una nueva baraja ordenada
    baraja = list([*range(1, 55)])
    return baraja


def barajear(baraja):
    return random.sample(baraja, len(baraja))


def get_index_carta(valor_carta, baraja):
    return baraja.index(53)


def mover_carta(valor_carta, posiciones, baraja):
    indice = baraja.index(valor_carta)
    if indice+posiciones > len(baraja) - 1:
        nuevo_indice = (indice+posiciones) % len(baraja) + 1
    else:
        nuevo_indice = (indice+posiciones) % len(baraja)
    baraja.pop(indice)
    baraja.insert(nuevo_indice, valor_carta)
    return baraja


def get_indice_primer_comodin(baraja):
    return min(baraja.index(53), baraja.index(54))


def get_indice_segundo_comodin(baraja):
    return max(baraja.index(53), baraja.index(54))


def cortar_entre_comodines(baraja):
    indice_primer_comodin = get_indice_primer_comodin(baraja)
    indice_segundo_comodin = get_indice_segundo_comodin(baraja)
    baraja_tras_segundo_comodin = baraja[indice_segundo_comodin +
                                         1:len(baraja)]
    baraja_entre_comodines = baraja[indice_primer_comodin:indice_segundo_comodin+1]
    baraja_antes_primer_comodin = baraja[0:indice_primer_comodin]
    baraja = baraja_tras_segundo_comodin + \
        baraja_entre_comodines + baraja_antes_primer_comodin
    return baraja


def cortar_tras_valor_ultima_carta(baraja):
    valor_ultima_carta = min(baraja[len(baraja)-1], 53)
    if valor_ultima_carta < 53:
        primer_corte = baraja[0:valor_ultima_carta]
        segundo_corte_sin_carta_final = baraja[valor_ultima_carta:len(
            baraja)-1]
        ultima_carta = [baraja[len(baraja)-1]]
        baraja = segundo_corte_sin_carta_final + primer_corte
        baraja = baraja + ultima_carta
    return baraja


def generar_clave(longitud):
    clave = []
    baraja = nueva_baraja()
    for i in range(1, longitud+1):
        valor_clave = 54
        while valor_clave >= 53:
            baraja = mover_carta(53, 1, baraja)
            baraja = mover_carta(54, 2, baraja)
            baraja = cortar_entre_comodines(baraja)
            baraja = cortar_tras_valor_ultima_carta(baraja)
            valor_primera_carta = min(baraja[0], 53)
            valor_clave = baraja[valor_primera_carta]
        letra_clave = convertir_a_letra(valor_clave % 26)
        clave.append(letra_clave)
    return clave


def cifrar(mensaje):
    texto = normalizar_texto(mensaje)
    texto_cifrado = ""
    clave = generar_clave(len(texto))
    texto_numeros = convertir_a_numeros(texto)
    clave_numeros = convertir_a_numeros(clave)
    cifrado_numeros = sumar_numeros(texto_numeros, clave_numeros)
    texto_cifrado = convertir_a_letras(cifrado_numeros)
    texto_cifrado = "".join(texto_cifrado)
    return texto_cifrado


def descifrar(mensaje):
    texto_descifrado = ""
    clave = generar_clave(len(mensaje))
    mensaje_numeros = convertir_a_numeros(mensaje)
    clave_numeros = convertir_a_numeros(clave)
    descifrado_numeros = restar_numeros(mensaje_numeros, clave_numeros)
    texto_descifrado = convertir_a_letras(descifrado_numeros)
    texto_descifrado = "".join(texto_descifrado)
    return texto_descifrado
