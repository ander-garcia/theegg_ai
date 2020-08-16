# convierte un número decimal a binario
def decimal_to_binario(decimal):
    binario = ""
    # mientras el numero entre 2 sea mayor que 1
    while(decimal/2 >= 1):
        # añadir el resto entre 2 de atrás hacia adelante
        binario = str(int(decimal % 2)) + binario
        # dividir el numero entre 2
        decimal = decimal/2
    # por último añadir el número al principio del equiavlente binario
    binario = str(int(decimal)) + binario
    return binario
