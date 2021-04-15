# TAREA 48: Algoritmos de compresión-descompresión

## Requerimientos

Python

## Resumen

Para ejecutar, desde la línea de comandos y el directorio de la tarea_48:

        python main.py

En la consola se pide una cadena de entrada y se muestra la cadena comprimida, descomprimida y los tamaños en cada caso

        python main.py
        Introduce cadena para comprimir, se recomienda no superar los 30 caracteres:
        hello eggers
        COMPRIMIDO  = [(0, 1, 'h'), (0, 1, 'e'), (0, 1, 'l'), (1, 1, ''), (0, 1, 'o'), (0, 1, ' '), (5, 1, ''), (0, 1, 'g'), (1, 1, ''), (3, 1, ''), (0, 1, 'r'), (0, 1, 's')]
        DESCOMPRIMIDO  = hello eggers
        tamaño texto original 61, comprimido 192, descomprimido 61

## Explicación

Desde el fichero main.py se crea un objeto Compressor que se encarga de comprimir y descomprimir el texto. Para calcular el espacio en memoria se utiliza la librería sys.

La implementación del compresor se basa en la explicación de https://timguite.github.io/jekyll/update/2020/03/15/lz77-in-python.html

La implementación sigue los pasos lógicos, pero al ser un ejercicio práctico no optimiza el espacio de la representación comprimida. La clase Compress tiene dos métodos, uno para comprimir y otra para descomprimir. El cosntructor acepta un parámetro, el tamaño máximo de ventana que representa con cuantos caracteres previos se va a comparar el caracter actual como máximo.

Al comprimir, en el array output se van guardando tuplas en el formato offset,length,caracter. Si el offset es mayor que 0 (es una repetición), el caracter se deja vacío.

Para cada caracter de la cadena original se van mirando los caracteres previos para ver si hay coincidencias. Si hay una coincidencia, se miran si los caracteres sigueintes tambien coinciden. La búsqueda va a hasta el tamaño máximo de ventana y selecciona la repetición de mayor longitud. Si dos repeticiones tienen la misma longitud, se selecciona la más cercana.

A la hora de descomprimir la cadena, se leen las tuplas y se va generando la cadena original.

La explicación completa está en el enlace al inicio del README y en el vídeo de la descripción de la tarea.

## Paso adicional: Test

Para lanzar los test es necesario instalar la librería pytest (https://docs.pytest.org/en/stable/getting-started.html)

A continuación basta con ejecutar pytest. La consola debe mostar un mensaje en verde similar a "2 passed in 0.05s"

Los test se encuentra en el fichero "compressor_test.py". En este fichero hay un array con datos de entrada (testdata), en el formato texto,representación comprimida. Los test llaman a la funcion compress y decompress de la clase Compress y comprueban que el texto descomprimido es igual que el original y que la representación comprimida es correcta (los ejemplos se han cogido de la explicación de https://timguite.github.io/jekyll/update/2020/03/15/lz77-in-python.html)
