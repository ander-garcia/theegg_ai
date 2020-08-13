def elegir_vacas(vacas_venta, kg_camion, peso_vacas, litros_leche_vacas):
    max_leche = 0
    vacas = []

    for x in range(0, len(peso_vacas)):
        vacas.append({'id': (x+1), 'peso': peso_vacas[x], 'litros': litros_leche_vacas[x],
                      'productividad': litros_leche_vacas[x]/peso_vacas[x]})
    vacas_disponibles = sorted(
        vacas,  key=lambda vaca: vaca["productividad"], reverse=True)

    vacas_camion = []
    peso_disponible = kg_camion

    max_solution = get_greedy_solution(
        vacas_camion.copy(), vacas_disponibles.copy(), peso_disponible)
    max_leche = max_solution["leche"]
    for vaca in vacas:
        vacas_camion = []
        vacas_camion.append(vaca)
        resto_vacas = vacas_disponibles.copy()
        resto_vacas.remove(vaca)
        peso_disponible = kg_camion - vaca["peso"]

        new_solution = get_greedy_solution(
            vacas_camion.copy(), resto_vacas.copy(), peso_disponible)
        if new_solution["leche"] > max_leche:
            max_solution = new_solution
            max_leche = max_solution["leche"]

    return max_leche


def get_greedy_solution(vacas_camion, vacas_disponibles, peso_disponible):
    peso_vaca_min = 100000
    for vaca in vacas_disponibles:
        if (vaca["peso"] < peso_vaca_min):
            peso_vaca_min = vaca["peso"]
    while peso_disponible > peso_vaca_min:
        siguiente_vaca = 0
        while peso_disponible < vacas_disponibles[siguiente_vaca]["peso"]:
            if siguiente_vaca == len(vacas_disponibles):
                siguiente_vaca = siguiente_vaca - 1
                break
            siguiente_vaca = siguiente_vaca + 1
        vacas_camion.append(vacas_disponibles[siguiente_vaca])
        peso_disponible = peso_disponible - \
            vacas_disponibles[siguiente_vaca]["peso"]
        vacas_disponibles[siguiente_vaca]["peso"]
        vacas_disponibles.remove(vacas_disponibles[siguiente_vaca])
        if len(vacas_disponibles) == 0:
            break
        peso_vaca_min = 100000
        for vaca in vacas_disponibles:
            if (vaca["peso"] < peso_vaca_min):
                peso_vaca_min = vaca["peso"]
    leche_camion = 0
    for vaca in vacas_camion:
        leche_camion = leche_camion + vaca["litros"]
    return {"leche": leche_camion, "vacas": vacas_camion}
