# TAREA 33: El juego de Pikachu

## Requerimientos

Python

## Resumen

Para ejecutar, desde la línea de comandos y el directorio de la tarea_33:

        python main.py

En la consola se mostrán mensajes de la evolución del combate hasta que finalice:

Comienza el combate entre Pikachu y Jigglypuff
Ataque de Pikachu, Jigglypuff tiene 45 puntos de vida
Ataque de Jigglypuff, Pikachu tiene 55 puntos de vida
Ataque de Pikachu, Jigglypuff tiene -10 puntos de vida
Pikachu ha ganado
Enhorabuena Pikachu !!

## Explicación

Desde el fichero main.py se crean los dos pokemon y se lanza el combate. El código de los pokemon está en la clase Pokemon en el fichero pokemon.py. La clase pokemon tiene un constructor en el que se indica el nombre, la vida, el ataque y el turno del pokemon; y una función de combate.

La función de combate es estática (es compartida por todas las instancias Pokemon, se marca con el @staticmethod en python). Sus parámetros son el primer y el segundo pokemon, y el parámetro opcional turno inicial (0 o 1, si no se indica se inicializa a 1). En la función se sigue el diagrama de flujo adjunto, mostrando por pantalla la evolución del combate y devolviendo el pokemon ganador y perdedor.

Desde el fichero main se felicita al pokemon ganador, en este caso Pikachu

## Paso adicional: Test

Para lanzar los test es necesario instalar la librería pytest (https://docs.pytest.org/en/stable/getting-started.html)

A continuación basta con ejecutar pytest. La consola debe mostar un mensaje en verde similar a "2 passed in 0.05s"

Los test se encuentra en el fichero "pokemon_test.py". En este fichero hay dos tests, en uno el combate lo empieza Pikachu y enel otro JigglyPuff. Cada test comprueba quien es el ganador, y los puntos de vida restantes de cada Pokemon.
