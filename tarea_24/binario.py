def decimal_to_binario(decimal):
    binario = ""
    while(decimal/2 >= 1):
        binario = binario + str(int(decimal % 2))
        decimal = decimal/2
    binario = binario + str(int(decimal))
    return binario
