def decimal_to_binario(decimal):
    binario = ""
    while(decimal/2 >= 1):
        binario = str(int(decimal % 2)) + binario
        decimal = decimal/2
    binario = str(int(decimal)) + binario
    return binario
