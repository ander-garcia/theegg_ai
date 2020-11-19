from regulares import Pokemon


pikachu = Pokemon("Pikachu", 100, 55, 1)
jiggly = Pokemon("Jigglypuff", 100, 45, 0)
turno = 1
ganador = Pokemon.combate(pikachu, jiggly, turno)
print(f"Enhorabuena {ganador.nombre} !!")
