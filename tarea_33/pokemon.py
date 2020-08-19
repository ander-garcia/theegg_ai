class Pokemon():
    def __init__(self, nombre, vida, ataque, turno):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.turno = turno

    @staticmethod
    def combate(pokemon1, pokemon2, turno_inicial=1):

        print(
            f"Comienza el combate entre {pokemon1.nombre} y {pokemon2.nombre}")
        turno = turno_inicial
        while pokemon1.vida > 0 and pokemon2.vida > 0:
            if turno == pokemon1.turno:
                pokemon2.vida = pokemon2.vida - pokemon1.ataque
                print(
                    f"Ataque de {pokemon1.nombre},  {pokemon2.nombre} tiene {pokemon2.vida} puntos de vida")
                turno = pokemon2.turno
            else:
                pokemon1.vida = pokemon1.vida - pokemon2.ataque
                turno = pokemon1.turno
                print(
                    f"Ataque de {pokemon2.nombre},  {pokemon1.nombre} tiene {pokemon1.vida} puntos de vida")
        if pokemon1.vida <= 0:
            ganador = pokemon2
            perdedor = pokemon1
        else:
            ganador = pokemon1
            perdedor = pokemon2
        print(f"{ganador.nombre} ha ganado")
        return ganador
