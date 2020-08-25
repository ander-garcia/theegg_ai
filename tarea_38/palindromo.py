# encuentra el palindromo que a partir de unn número N, 1 <= N <= numero_max (por defecto 100.000.000
# devuelve el menor entero M tal que M <= N que es primo y M es un palíndromo N.
# Por ejemplo, si N es 31, entonces la respuesta es 101.
# Si no hay un palindromo que cumpla la condición devuelve un -1

def get_palindromo(numero, numero_max=100000000):
    palindromo = -1
    while palindromo < 0 and numero <= numero_max:
        if is_palindromo(numero) and is_primo(numero):
            palindromo = numero
        else:
            numero = numero + 1
    return palindromo


def is_palindromo(numero):
    palindromo = False
    entrada = str(numero)
    if entrada == entrada[::-1]:
        palindromo = True
    return palindromo


def is_primo(numero):
    primo = True
    for x in range(2, numero):
        if numero % x == 0:
            primo = False
            break
    return primo


if __name__ == "__main__":
    # solo se ejecuta al llamar directmente al fichero, no al importarlo
    numero = int(input("Número:\n"))
    palindromo = get_palindromo(numero)

    print(f"Palíndromo primo mayor más cercano es {palindromo}")
