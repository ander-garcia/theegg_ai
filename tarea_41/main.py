from text_analyzer import TextAnalyzer
TOP = 10

texto = input("Introduce texto a analizar:\n")
analizador = TextAnalyzer(texto)
caracteres = analizador.cuenta_caracteres()
palabras = analizador.cuenta_palabras()
ranking = analizador.ranking_palabras(TOP)

print(f"Texto =  {texto}")
print(f"Número caracteres =  {caracteres}")
print(f"Número palabras =  {palabras}")
print(f"Ranking de {TOP} palabras más repetidas =   {ranking}")
