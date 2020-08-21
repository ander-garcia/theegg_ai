# TAREA 22: El algoritmo del lechero

## Requerimientos

Python

## Biólogo

### Resumen biologo

Para ejecutar:

        python biologo.py

El programa pide al usuario las dos cadenas de ADN, y devuelve la coincidencia más larga.

La comparación se hace en la función comparar adn del fichero biologo.py. La comparación comienza con la longitud máxima (una cadena estaría totalmente contenida en la otra), y si no hay coincidencias busca subcadenas que en cada paso de búsqueda son una unidad más cortas, hasta que encuentre una coincidencia o la subcadena de búsqueda sea de longitud 0.

En primer lugar se considera que la longitud máxima de la coincidencia va a ser la longitud de la cadena más corta. Entonces, se buscan en la primera cadena subcadenas de esa longitud. Cada subcadena se busca en la segunda cadena de ADN. Si hay alguna coincidencia, se para la búsqueda. En caso contrario, se repite el proceso con una longitud una unidad más pequeña, hasta que haya una coincidencia, o la longitud se reduzca a 0.

Ejemplos de entradas y salidas

Primera cadena de ADN:
ctgggccttgaggaaaactg

Segunda cadena de ADN:
gtaccagtactgatagt

La coincidencia más larga es actg

Primera cadena de ADN:
asdasd

Segunda cadena de ADN:
nvnvbn

No hay coincidencias entre las cadenas de entrada

### Paso adicional: Test

Para lanzar los test es necesario instalar la librería pytest (https://docs.pytest.org/en/stable/getting-started.html)

A continuación basta con ejecutar pytest. La consola debe mostar un mensaje en verde similar a "4 passed in 0.05s"

Los test se encuentra en el fichero "biolog_test.py". En este fichero hay un array con datos de entrada (testdata), en el formato primera cadena de ADN, segunda cadena de ADN, y coincidencia esperada. Los test llaman a la funcion "comparar_adn" y comprueban que los resultados obtenidos son los esperados
