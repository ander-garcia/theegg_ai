# TAREA 45: Algoritmos de búsqueda

## Requerimientos

Python

## Resumen

Para ejecutar, desde la línea de comandos y el directorio de la tarea_41:

        python main.py

En la consola es necesario introducir un texto. Tras pulsar enter, se muestra el número de caracteres y palabras del texto, y las 10 palabras que más aparecen en el formato (palabra, número de apariciones)

Introduce texto a analizar:
er er er trersafasdfasd sdfasf 77 fdadf 77 sdfaf 77 sdf a8 i k j u y h hhh sdfdf sfasd fa asdf adsf adsf
Texto = er er er trersafasdfasd sdfasf 77 fdadf 77 sdfaf 77 sdf a8 i k j u y h hhh sdfdf sfasd fa asdf adsf adsf
Número caracteres = 80
Número palabras = 25
Ranking de 10 palabras más repetidas = [('er', 3), ('77', 3), ('adsf', 2), ('trersafasdfasd', 1), ('sdfasf', 1), ('fdadf', 1), ('sdfaf', 1), ('sdf', 1), ('a8', 1), ('i', 1)]

## Explicación

Desde el fichero main.py se pide el texto a analizar, se crea un objeto de TextAnalyzer y se cuentan los caracteres, palabras y el ranking para mostrarlos por consola. El código de análisis del texto está en la clase TextAnalyzer en el fichero text_analyzer.py. La clase TextAnalyzer tiene un constructor en el que se indica el texto, y dos variables estáticas con los patrones para contar caracteres y palabaras.

Estos patrones se utilizan para contar los caracteres, y las palabras. Para generar el ranking de palabras se utiliza el apoyo de Counter de collections (https://docs.python.org/3/library/collections.html#collections.Counter.most_common)

## Paso adicional: Test

Para lanzar los test es necesario instalar la librería pytest (https://docs.pytest.org/en/stable/getting-started.html)

A continuación basta con ejecutar pytest. La consola debe mostar un mensaje en verde similar a "2 passed in 0.05s"

Los test se encuentra en el fichero "text_analyzer_test.py". En este fichero hay tres tests, uno para cada método de la clase TextAnalyzer. En este fichero hay un array con datos de entrada (testdata), en el formato texto, número de caracteres, número de palabras, y raking de las primeras palabras.
