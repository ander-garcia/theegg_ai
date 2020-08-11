def fraccion_irreducible (numero, referencia_decimales = 10000):
    denominador = referencia_decimales
    numerador = int(numero*denominador)
    max_numero = numerador
    divisor_comun = 2
    while max_numero >= divisor_comun:
        if (numerador%divisor_comun) == 0 and (denominador%divisor_comun) == 0:
            numerador = numerador/divisor_comun
            denominador = denominador/divisor_comun
            max_numero = numerador
        else:
            divisor_comun = divisor_comun +1
    numerador = int (numerador)
    denominador = int (denominador)
    return {"numerador" : numerador,"denominador":denominador}