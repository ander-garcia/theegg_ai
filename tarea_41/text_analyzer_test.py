import pytest
from text_analyzer import TextAnalyzer

testdata = [
    ("hola egger", 9, 2, [('hola', 1), ('egger', 1)]),
    ("hola egger hola egger hola egg", 25, 6,
     [('hola', 3), ('egger', 2), ('egg', 1)]),
    ("""En Strandhill, Irlanda, se cruzó en mi camino Chris, un señor de los que inspiran y se posicionan como referente. Fue una pieza fundamental en un momento de pura congelación. Te cuento…
     Strandhill es una playa donde el mar ruge muy bien, siempre está lleno de surfistas en busca de buenas olas. Y allí estaba yo también. Después de unos meses viviendo en una ciudad sin costa, mis ganas por hacer un poco de surfing estaban por las nubes. Aunque tenía un «pequeño» problema: no tenía equipo, ni tabla, ni neopreno, y tampoco había ninguna tienda para alquilarlo.
     Todo se puso a rodar enseguida. Escribí a un famoso surfista de la zona y recibí una respuesta increíble. «Mi casa está en la calle x, la puerta está abierta y tienes la tabla en la esquina. Ven cuando quieras», me dijo.
     Y eso hice, fui para allá y la cogí. Aunque el neopreno no me lo pudo prestar, y no porque se negara… Lamentablemente le sacaba unos 15 cm de altura.
     Luego, en la playa, un alemán me solucionó el tema del neopreno. Me prestó uno que había por su maletero, uno muy fino, de los que uso yo en el Mediterráneo en otoño o primavera. Y claro, era invierno y estábamos en Irlanda.
     El caso es que salí del agua más pronto de lo previsto y con las manos, la cabeza y los labios congelados. Me empecé a cambiar en el mismo paseo que contorneaba la costa y, estando semidesnudo, se me acercó Chris. «Está fría el agua, eh», apuntó este fenómeno.
     Chris superaba los 65 años y todos los días hacía un recorrido de decenas de kilómetros para llegar hasta allí. Sus gracietas y su buena conversación me hicieron apartar el frío de la parte de mi cabeza que se encarga de pensar, y hasta cantamos juntos la canción de Annie.
     Sé que esto último puede sonar raro, ¿quién canta Annie semidesudo y congelado en un paseo de Irlanda con un señor que acaba de conocer? Pero… seguro que a ti también te han pasado cosas así.""",
     1538, 348, [('de', 18), ('y', 17), ('en', 13), ('la', 11)])
]


@pytest.mark.parametrize("texto,caracteres,palabras,ranking", testdata)
def test_cuenta_caracteres(texto, caracteres, palabras, ranking):
    analizador = TextAnalyzer(texto)
    contador = analizador.cuenta_caracteres()
    assert contador == caracteres


@pytest.mark.parametrize("texto,caracteres,palabras,ranking", testdata)
def test_cuenta_palabras(texto, caracteres, palabras, ranking):
    analizador = TextAnalyzer(texto)
    contador = analizador.cuenta_palabras()
    assert contador == palabras


@pytest.mark.parametrize("texto,caracteres,palabras,ranking", testdata)
def test_ranking_palabras(texto, caracteres, palabras, ranking):
    analizador = TextAnalyzer(texto)
    ranking_palabras = analizador.ranking_palabras(len(ranking))
    assert ranking_palabras == ranking
