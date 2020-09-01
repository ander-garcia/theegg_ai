import random
import re

COMODIN_A = 53
COMODIN_B = 54
VALOR_COMODINES = 53
LETRAS_ABECEDARIO = 26
TAMAÑO_GRUPO = 5
CARACTER_RELLENO = "X"


def print_con_espacios(texto, tamaño_grupo):
    return " ".join(texto[i:i+tamaño_grupo] for i in range(0, len(texto), tamaño_grupo))


def normalizar_texto(texto):
    normalizado = eliminar_no_alfanumericos(texto).upper()
    normalizado = remplazar_letras(normalizado)
    normalizado = rellenar(normalizado, TAMAÑO_GRUPO, CARACTER_RELLENO)
    return normalizado


def rellenar(texto, tamaño_grupo, caracter_relleno):
    return texto.ljust(len(texto)+(tamaño_grupo-len(texto)) % tamaño_grupo, caracter_relleno)


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
    suma = [(array1[i]+array2[i]) %
            LETRAS_ABECEDARIO for i in range(len(array1))]
    for i in range(len(suma)):
        if suma[i] == 0:
            suma[i] = LETRAS_ABECEDARIO
    return suma


def restar_numeros(array1, array2):
    resta = [(array1[i]-array2[i]) %
             LETRAS_ABECEDARIO for i in range(len(array1))]
    for i in range(len(resta)):
        if resta[i] == 0:
            resta[i] = LETRAS_ABECEDARIO
    return resta


def nueva_baraja(clave=""):
    # crea una nueva baraja ordenad
    if clave == "":
        baraja = list([*range(1, 55)])
    else:
        baraja = list([*range(1, 55)])
        for i in range(len(clave)):
            baraja = mover_carta(COMODIN_A, 1, baraja)
            baraja = mover_carta(COMODIN_B, 2, baraja)
            baraja = cortar_entre_comodines(baraja)
            baraja = cortar_tras_valor_ultima_carta(baraja)
            baraja = cortar_tras_valor_letra(clave[i], baraja)
    return baraja


def barajear(baraja):
    return random.sample(baraja, len(baraja))


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
    return min(baraja.index(COMODIN_A), baraja.index(COMODIN_B))


def get_indice_segundo_comodin(baraja):
    return max(baraja.index(COMODIN_A), baraja.index(COMODIN_B))


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
    valor_ultima_carta = min(baraja[len(baraja)-1], VALOR_COMODINES)
    if valor_ultima_carta < VALOR_COMODINES:
        primer_corte = baraja[0:valor_ultima_carta]
        segundo_corte_sin_carta_final = baraja[valor_ultima_carta:len(
            baraja)-1]
        ultima_carta = [baraja[len(baraja)-1]]
        baraja = segundo_corte_sin_carta_final + primer_corte
        baraja = baraja + ultima_carta
    return baraja


def cortar_tras_valor_letra(letra, baraja):
    valor_letra = convertir_a_numero(letra)
    primer_corte = baraja[0:valor_letra]
    segundo_corte_sin_carta_final = baraja[valor_letra:len(
        baraja)-1]
    ultima_carta = [baraja[len(baraja)-1]]
    baraja = segundo_corte_sin_carta_final + primer_corte
    baraja = baraja + ultima_carta
    return baraja


def generar_clave(longitud, clave_inicial=""):
    clave = []
    baraja = nueva_baraja(clave_inicial)
    for i in range(1, longitud+1):
        valor_clave = COMODIN_B
        while valor_clave >= COMODIN_A:
            baraja = mover_carta(COMODIN_A, 1, baraja)
            baraja = mover_carta(COMODIN_B, 2, baraja)
            baraja = cortar_entre_comodines(baraja)
            baraja = cortar_tras_valor_ultima_carta(baraja)
            valor_primera_carta = min(baraja[0], VALOR_COMODINES)
            valor_clave = baraja[valor_primera_carta]
        letra_clave = convertir_a_letra(valor_clave % LETRAS_ABECEDARIO)
        clave.append(letra_clave)
    return clave


def cifrar(mensaje, clave_inicial):
    texto = normalizar_texto(mensaje)
    texto_cifrado = ""
    clave = generar_clave(len(texto), clave_inicial)
    texto_numeros = convertir_a_numeros(texto)
    clave_numeros = convertir_a_numeros(clave)
    cifrado_numeros = sumar_numeros(texto_numeros, clave_numeros)
    texto_cifrado = convertir_a_letras(cifrado_numeros)
    texto_cifrado = "".join(texto_cifrado)
    return texto_cifrado


def descifrar(mensaje, clave_inicial):
    texto_descifrado = ""
    clave = generar_clave(len(mensaje), clave_inicial)
    mensaje_numeros = convertir_a_numeros(mensaje)
    clave_numeros = convertir_a_numeros(clave)
    descifrado_numeros = restar_numeros(mensaje_numeros, clave_numeros)
    texto_descifrado = convertir_a_letras(descifrado_numeros)
    texto_descifrado = "".join(texto_descifrado)
    return texto_descifrado


if __name__ == "__main__":
    # solo se ejecuta al llamar directmente al fichero, no al importarlo
    mensaje = input("Mensaje a cifrar:\n")
    clave = input("Clave (opcional, se convertirá a mayúsculas):\n")
    cifrado = cifrar(mensaje, clave)
    descifrado = descifrar(cifrado, clave)
    print(f"Mensaje cifrado {print_con_espacios(cifrado,TAMAÑO_GRUPO)}")
    print(f"Mensaje descifrado {print_con_espacios(descifrado,TAMAÑO_GRUPO)}")
