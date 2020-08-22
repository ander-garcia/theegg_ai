# encuentra el palindromo que a partir de unn número N, 1 <= N <= 1.000.000
# devuelve el menor entero M tal que M <= N que es primo y M es un palíndromo N.
# Por ejemplo, si N es 31, entonces la respuesta es 101.

def get_palindromo(numero):
    return 1


if __name__ == "__main__":
    # solo se ejecuta al llamar directmente al fichero, no al importarlo
    numero = int(input("Número de frases:\n"))
    palindromo = get_palindromo(numero)

    print(f"{palindromo}")
