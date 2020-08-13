# TAREA 22: El algoritmo del lechero

## Requerimientos

Python

## Resumen

Para ejecutar:

        python main.py

Entrada, 4 parámetros:
Número de vacas sdisponibles para la venta, por ejemplo, 6
Peso límite del camión en kilogramos, por ejemplo , 700
Lista separada por comas de pesos de vacas, por ejemplo, 360,250,400,180,50,90
Lista separada por comas de producción de leche de vaca, por ejemplo, 40,35,43,28,12,13

Salida 93

Ejemplo de entrada
6 700 360,250,400,180,50,90 40,35,43,28,12,13
8 1000 223,243,100,200,200,155,300,150 30,34,28,45,31,50,29,1
10 2000 340,355,223,243,130,240,260,155,302,130 45,50,34,39,29,40,30,52,31,1

Ejemplo de salida
93
188
320

## Explicación

## Paso adicional: Test

Para lanzar los test es necesario instalar la librería pytest (https://docs.pytest.org/en/stable/getting-started.html)

A continuación basta con ejecutar pytest. La consola debe mostar un mensaje en verde similar a "4 passed in 0.05s"

Los test se encuentra en el fichero "fraccion_test.py". En este fichero hay un array con datos de entrada (testdata),, en el formato número decimal, numerador_esperado, denominador_esperado. Los test llaman a la funcion "fraccion_irreducible" y comprueban que los resultados obtenidos son los esperados
