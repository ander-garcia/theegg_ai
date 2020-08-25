
# invierte el orden de las palabras de cada frase de un array de frases
# devuelve un nuevo array con las frases invertidas, sin alterar el original
def invertir_palabras(frases):
    frases_invertidas = []
    for frase in frases:
        palabras = frase.split(" ")
        frase_invertida = " ".join(palabras[::-1])
        frases_invertidas.append(frase_invertida)
    return frases_invertidas


if __name__ == "__main__":
    # solo se ejecuta al llamar directmente al fichero, no al importarlo
    num_frases = int(input("Número de frases:\n"))
    frases = []
    while len(frases) < num_frases:
        frases.append(input("Siguiente frase:\n"))

    frases_invertidas = invertir_palabras(frases)
    for index, frase_invertida in enumerate(frases_invertidas):
        print(f"Case #{index+1}: {frase_invertida}")
