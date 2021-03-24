# TAREA 44: Análisis del rendimiento de las aplicaciones de IA

## Requerimientos

Python

## Resumen

Para ejecutar, desde la línea de comandos y el directorio de la tarea_41:

        python main.py

En la consola se muestra el sumatorio y el tiempo de cálculo del proceso, primero con el sumatorio lineal y luego con el constante. La primera suma parte de n=100000, y se hacen 6 iteraciones, aumentando n\*10 en cada una de ellas. Las instrucciones, el ejemplo y la guía están en los videos asociados a la tarea https://www.youtube.com/watch?v=akEkFs45uA8

Se aprecia que la suma constante se ejecuta en 0.0, pero la lineal aumenta y ya en la 4 iteración necesita casi 5 segundos, en la 5 iteración necesita 47 segundos, y en la 6 tras más de 10 minutos mi PC no ha finalizado.

        C:\repos\theegg_ai\tarea_44>python main.py
        5000050000;0.005057573318481445
        5000050000.0;0.0
        500000500000;0.0559999942779541
        500000500000.0;0.0
        50000005000000;0.47004270553588867
        50000005000000.0;0.0
        5000000050000000;4.913200616836548
        5000000050000000.0;0.0
        500000000500000000;47.33550000190735
        5.000000005e+17;0.0

## Explicación

Desde el fichero main.py se crea un objeto de Sumatorio. Desde este objeto se llaman a los métodos de suma lineal y suma constante. La clase Sumatrio tiene un constructor vacío.

## Paso adicional: Test

Para lanzar los test es necesario instalar la librería pytest (https://docs.pytest.org/en/stable/getting-started.html)

A continuación basta con ejecutar pytest. La consola debe mostar un mensaje en verde similar a "2 passed in 0.05s"

Los test se encuentra en el fichero "text_sumatorio.py". En este fichero hay dos tests, uno para cada tipo de suma. Se comprueban los casos extremos cuando n es 0 y 1.
