# TAREA 23: Cifrado y descifrado con el solitario

## Requerimientos

Python

## Resumen

Para ejecutar:

        python solitario.py

Entrada, 2 parámetros:
Mensaje a cifrar
Clave (opcional)
Muestra como salida el mensaje cifrado y descifrado

Ejemplo

        Mensaje a cifrar (se añadirán X para que su longitud sea múltiplo de 5):
        Eureka funciona

        Clave (opcional, se normalizará y convertirá a mayúsculas):
        the egg

        Mensaje cifrado XKGXR LEWWU PDPAY

        Mensaje descifrado EUREK AFUNC IONAX

## Explicación

El programa utiliza el algoritmo del solitario para generar una baraja, cifrar y descifrar el mensaje. Además de en la explicación de la tarea, en Internet hay varias entradas que explican en detalle el algoritmo. Recomiendo dos entradas con explicaciones paso a paso del algoritmo:
https://www.dcode.fr/solitaire-cipher-schneier
http://jnicholl.org/Cryptanalysis/Ciphers/Solitaire.php

El código divide el algoritmo del solitario en funciones asociadas a los pasos del solitario y en funciones de apoyo para llevar a cabo estos pasos. Las funciones principales son cifrar y descifrar, que aceptan dos parámetros. El primero es el mensaje a cifrar o descifar, y el segundo es una clave opcional que se utiliza para generar la baraja. Sin esta clave, se parte de una baraja ordenada (1...52,A,B).

Si se ejecuta el programa, se pide un mensaje, y una clave que se puede dejar en blanco. Con estos datos se muestra el mensaje cifrado y descifrado. En este proceso, tanto el mensaje original como la clave se normalizan (eliminación de espacios y caracteres no alfanuméricos, conversión a mayúsculas). En el caso del mensaje, se completa con "X" hasta que su longitus es múltiplo de 5. La salida se formatea en grupos de 5 caracteres para facilitar su lectura.

El fichero solitario.py incluye las siguientes funciones principales:
-nueva_baraja: genera una nueva baraja. Se parte de una baraja ordenada. Si se utiliza una clave, esta baraja inicial se transforma con la clave siguiendo los pasos del algoritmo
-cifrar
-descifrar

Las funciones están comentadas, y en el fichero de tests se puede ver su funcionamiento.

Las cartas de la baraja se representan con valores del 1 al 52 para las cartas regulares, 53 para el comodín A y 54 para el comodín B.

## Paso adicional: Test

Para lanzar los test es necesario instalar la librería pytest (https://docs.pytest.org/en/stable/getting-started.html)

A continuación basta con ejecutar pytest. La consola debe mostar un mensaje en verde similar a "28 passed in 0.05s"

Los test se encuentra en el fichero "solitario_test.py". En este fichero hay un array con datos de entrada para cada función testeada. Los test llaman a la funcion asociada (cifrar, nueva_baraja_cortar....) y comprueban que los resultados obtenidos son los esperados
