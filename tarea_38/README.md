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

Los test se encuentra en el fichero "biologo_test.py". En este fichero hay un array con datos de entrada (testdata), en el formato primera cadena de ADN, segunda cadena de ADN, y coincidencia esperada. Los test llaman a la funcion "comparar_adn" y comprueban que los resultados obtenidos son los esperados

## Invertir palabras

### Resumen invertir palabras

Para ejecutar:

        python palabras.py

El programa pide al usuario el número de frases y cada frase, y devuelve cada frase con el orden de las palabras invertido.

La inversión de las palabaras se hace en la función invertir_palabras del fichero palabras.py. Esta función recorre cada frase del array de frases de entrada. Separa cada frase en un array de palabras a partir de los espacios entre las palabras. Luego crea un nuevo array invertido recorriendo en orden inverso el array de palabras. Por último, genera una nueva frase juntando con espacios el array invertido. Esta nueva frase se añade al array de frases invertidas, que es devuelto por la función.

Ejemplos de entradas y salidas

        Número de frases:
        2

        Siguiente frase:
        qq ww ee rr

        Siguiente frase:
        aa

        Case #1: rr ee ww qq

        Case #2: aa

### Paso adicional: Test

Para lanzar los test es necesario instalar la librería pytest (https://docs.pytest.org/en/stable/getting-started.html)

A continuación basta con ejecutar pytest. La consola debe mostar un mensaje en verde similar a "4 passed in 0.05s"

Los test se encuentra en el fichero "palabras_test.py". En este fichero hay un array con datos de entrada (testdata), en el formato array de frases a invertir, y array con las frases invertidas. Los test llaman a la funcion "invertir_palabras" y comprueban que los resultados obtenidos son los esperados

## Palindromo

### Resumen palindromo

Para ejecutar:

        python palindromo.py

El programa pide al usuario un número N (1 <= N <= 1.000.000), y devuelve el palíndromo que a partir del número devuelve el menor entero M tal que M <= N que es primo y M es un palíndromo N. Por ejemplo, si N es 31, entonces la respuesta es 101.

El palíndromo se calcula en la función get_palindromo del fichero palindromo.py. Esta función tiene dos parámetros, el númeor y un número máximo de búsqueda optativo (valor por defecto de 100000000). Si no encuentra un palindromo primo mayor o igual que el número de entrada y menor que el número máximo devuelve -1. Comenzando por el número de entrada, comprueba si es palindromo y primo. Si lo es de sevuelve el valor, en caso contrario número se incrementa en 1 y se vuelve a probar hasta que lo sea o se supere el número máximo.

Ejemplos de entradas y salidas

        Número:
        31
        Palíndromo primo mayor más cercano es 101

### Paso adicional: Test

Para lanzar los test es necesario instalar la librería pytest (https://docs.pytest.org/en/stable/getting-started.html)

A continuación basta con ejecutar pytest. La consola debe mostar un mensaje en verde similar a "4 passed in 0.05s"

Los test se encuentra en el fichero "palindromo_test.py". En este fichero hay tres tests, cada uno con sus datos dentrada.

En el primero hay un array con datos de entrada (testdata), en el formato número de entrada y palíndromo esperado. Los test llaman a la funcion "get_palindromo" y comprueban que los resultados obtenidos son los esperados

En el segundo hay un array con datos de entrada (testdata_palindromo), en el formato número de entrada y si es palíndromoo no. Los test llaman a la funcion "is_palindromo" y comprueban que los resultados obtenidos son los esperados.

En el tercero hay un array con datos de entrada (testdata_primo), en el formato número de entrada y si es primo no. Los test llaman a la funcion "is_primo" y comprueban que los resultados obtenidos son los esperados
