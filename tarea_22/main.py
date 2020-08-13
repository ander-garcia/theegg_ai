import sys
from lechero import elegir_vacas

vacas_venta = int(input("Número de vacas disponibles para la venta\n"))
kg_camion = int(input("Peso límite del camión en kilogramos\n"))
peso_vacas = input(
    "lista separada por comas de pesos de vacas, por ejemplo, 360,250,400,180,50,90\n").split(",")
litros_leche_vacas = input(
    "Lista separada por comas de producción de leche de vaca, por ejemplo, 40,35,43,28,12,13\n").split(",")

peso_vacas = [float(i) for i in peso_vacas]
litros_leche_vacas = [float(i) for i in litros_leche_vacas]
result = elegir_vacas(vacas_venta, kg_camion, peso_vacas, litros_leche_vacas)
print(f"{result}")
