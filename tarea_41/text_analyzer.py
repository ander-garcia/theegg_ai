import re
import collections


class TextAnalyzer():

    # cualquier caracter menos un espacio
    patron_caracteres = re.compile(r'\S')
    # cualquier grupo formado por uno o mas caracteres alfanumericos
    patron_palabras = re.compile(r'\w+')

    def __init__(self, texto):
        self.texto = texto

    def cuenta_caracteres(self):
        caracteres = len(TextAnalyzer.patron_caracteres.findall(self.texto))
        return caracteres

    def cuenta_palabras(self):
        palabras = len(TextAnalyzer.patron_palabras.findall(self.texto))
        return palabras

    def ranking_palabras(self, top=None):
        palabras = TextAnalyzer.patron_palabras.findall(self.texto.lower())
        ranking = collections.Counter(palabras).most_common(top)
        return ranking
