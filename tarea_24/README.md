# TAREA 24: Construye un simulador

## Requerimientos

Python

## Resumen

Para ejecutar, desde la línea de comandos y el directorio de la tarea_24:

        python main.py 65

Si el número (en el ejemplo 65) no es un entero devuelve un error

En caso contrario la salida muestra el numero en binario en este formato:

        65 = 1000001

## Explicación

### Paso 1: Leer parámetro de entrada

En este paso se lee el número de entrada y se convierte a un entero. Si no es correcto, porque no se ha podido convertir a entero, se lanza un error y se para el programa

### Paso 2: Calcular el equivalenge binario

El cálculo se hace en la función "decimal_to_binario" que se encuentra en el fichero "binario.py". Esta función tiene un parámetro de entrada, el número decimal

Para calcular el equivalente binario, mientras el número entre 2 sea mayor o igual que uno, se va añadiendo el resto de la división de atrás hacia adelante. Si el número entre 2 es menor que 1, se añade el número al equivalente binario (explicación detallada y alternativas en https://www.wikihow.com/Convert-from-Decimal-to-Binary)

La función devuelve el equiavalnete binario

### Paso 3: Visualizar salida

En este último paso se muestra salida en el formato "65 = 1000001"

## Paso adicional: Test

Para lanzar los test es necesario instalar la librería pytest (https://docs.pytest.org/en/stable/getting-started.html)

A continuación basta con ejecutar pytest. La consola debe mostar un mensaje en verde similar a "4 passed in 0.05s"

Los test se encuentra en el fichero "binario_test.py". En este fichero hay un array con datos de entrada (testdata),, en el formato número decimal, binario_esperado. Los test llaman a la funcion "decimal_to_biario" y comprueban que los resultados obtenidos son los esperados
