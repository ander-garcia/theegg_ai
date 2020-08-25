
# compara dos cadenas y devuelve la coincidencia más larga
# si no hay coincidencia se devuelve un string vacio
def comparar_adn(cadena1,  cadena2):
    longitud = min(len(cadena1), len(cadena2))
    coincidencia = ""
    while len(coincidencia) == 0 and longitud > 0:
        inicio = 0
        # se buscan las subcadenas de la longitud dentro de la primera cadena de adn
        # si cadena1 es acata y longitud es 5se buscaría acata,
        # si es 4 se buscaría acata y cata,
        # si es 3 se buscaría aca, cat, y ata
        while (inicio+longitud) <= len(cadena1):
            indice_coincidencia = cadena2.find(
                cadena1[inicio:(longitud+inicio)])
            # si hay coincidencia se almacena la subcadena y se interrumpe la búsqueda
            if (indice_coincidencia >= 0):
                coincidencia = cadena1[inicio:(longitud+inicio)]
                break
            # si no hay coincidencia se genera otra subcadena
            inicio = inicio + 1
        # si no hay coincidencia se intenta con una subcadena más corta
        longitud = longitud - 1
    return coincidencia


if __name__ == "__main__":
    # solo se ejecuta al llamar directmente al fichero, no al importarlo
    cadena1 = input("Primera cadena de ADN:\n")
    cadena2 = input("Segunda cadena de ADN:\n")
    coincidencia = comparar_adn(cadena1, cadena2)
    if len(coincidencia) > 0:
        print(f"La coincidencia más larga es {coincidencia}")
    else:
        print(f"No hay coincidencias entre las cadenas de entrada")
