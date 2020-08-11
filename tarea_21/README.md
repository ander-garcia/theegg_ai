# TAREA 21: Fracción irreducible

## Requerimientos

Python

## Resumen

Para ejecutar:

        python main.py 0.0050

Si el número no está entre 0 y 1 se muestra un error

En caso contrario la salida muestra la fracción irreducible en este formato:

        0.005 = 1 / 200

## Explicación

### Paso 1: Leer parámetro de entrada

En este paso se lee el número de entrada y se valida que es correcto. Si no es correcto, bien porque no está en el rango de 0 a 1 o no se ha podido convertir a float, se lanza un error y se para el programa

### Paso 2: Calcular fracción irreducible

El cálculo se hace en la función "fraccion_irreducible" que se encuentra en el fichero "fraccion.py". Esta función tien dos parámetros de entrada, el número decimal y un número de referencia opcional. El número de referencia sirve para poder personalizar el número de decimales con el que queremos trabajar. POr defecto es 10000, pero se podría actualizar en el futuro con este parámetro.

Para calcular esta fracción, en primer lugar se genera el numerador y el denominador multiplicando el número decimal por el número de referencia. Con los datos del ejemplo (0.005), el numerador sería 500 y el denominador 10000. A partir de aqui, se van buscando divisores comunes del numerador y el denominador. La búsqueda comienza con el 2. Si se encuentra un divisor, se divide tanto el numerador como el divisor. En caso contrario, se aumenta en 1 el numero de búsqueda. La búsqueda sigue hasta que el valor actualizado del numerador es mayor que el número de búsqueda.

La función devuelve dos valores, el denominador y el numerador

### Paso 3: Visualizar salida

En este último paso se muestra salida en el formato "0.005 = 1 / 200"

## Paso adicional: Test

Para lanzar los test es necesario instalar la librería pytest (https://docs.pytest.org/en/stable/getting-started.html)

A continuación basta con ejecutar pytest. La consola debe mostar un mensaje en verde similar a "4 passed in 0.05s"

Los test se encuentra en el fichero "fraccion_test.py". En este fichero hay un array con datos de entrada (testdata),, en el formato número decimal, numerador_esperado, denominador_esperado. Los test llaman a la funcion "fraccion_irreducible" y comprueban que los resultados obtenidos son los esperados
