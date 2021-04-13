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

El problema a resolver es un problema que a medida que tenemos más datos de entrada (vacas), no se puede resoler por fuerza bruta en un ordenador (explicación simplificada de problemas NP-hard), su complejidad aumenta de forma exponencial con el número de entradas. Se ha optado por un algoritmo "greedy" (avaricioso), que intenta elegir en cada paso la mejor opción (la vaca más productiva que quep en el camión) hasta que no hay más opciones válidas. Como la solución que se obtiene de forma directa no es la mejor, se ejecuta este algoritmo varias veces. La primera sin haber elegido ninguna vaca, el resto preseleccionando una vaca para subirla al camión antes de ejecutar el algoritmo. Al final se selecciona la solución con la que se obtengan más litros de leche a partir de las vacas que estén en el camión.

### Paso 1: Leer parámetro de entrada

En este paso se leen los parámetros de entrada y se llama a la función "elegir_vacas" del fichero "lechero.py". Esta función tiene los mismos parámetros de entrada que el problema (vacas_venta, kg_camion, peso_vacas, litros_leche_vacas) y devuelve los litros de leche esperados de las vacas que se han elegido

### Paso 2:Elegir vacas

En primer lugar se crea una lista de vacas. Cada vaca tiene su peso, los litros de leche que produce y un valor de productividad medido como litros/kilogramos de peso.

### Paso 3: Buscar solución sin haber preseleccionado ninguna vaca

La función "get_greedy_solution" cuenta con tres parámetros (vacas_camion, vacas_disponibles, peso_disponible) y aplica el algoritmo para encontrar una solución. Como la lista con las vacas disponibles está ordenada en base a la productividad de las vacas, intenta subir al camión la primera vaca disponible. Si no cabe la siguiente, y así hasta que encuentra alguna que entre o lo haya intentado con todas.

Tras subir una vaca, lo intenta con la siguiente. Para agilizar el cálculo, se compara el peso disponible en el camión con el peso de la vaca más ligera para evitar comprobaciones innecesarias.

Cuando no se pueden subir más vacas se devuelven los litros de leche de las vacas elegidas, y una lista con las vacas elegidas.

En este paso se llama a esta función con la lista vacas_camion vacia

## Paso 4: Buscar solución preseleccionando vacas

En este paso, antes de llamar a la función "get_greedy_solution", se sube al camión a una vaca. Se hacen tantan pruebas como número de vacas, subiendo en cada prueba a una vaca diferente. A partir de esta preselección, el algoritmo aplica la lógica anterior para generar una solución.

Si la solución es mejor que la mejor solución previa, se guarda como nueva mejor solución

### Paso 3: Visualizar salida

En este último paso se muestra salida con los litros de leche de la mejor solución

## Paso adicional: Test

Para lanzar los test es necesario instalar la librería pytest (https://docs.pytest.org/en/stable/getting-started.html)

A continuación basta con ejecutar pytest. La consola debe mostar un mensaje en verde similar a "4 passed in 0.05s"

Los test se encuentra en el fichero "lechero_test.py". En este fichero hay un array con datos de entrada (testdata), en el formato vacas_venta, kg_camion, peso_vacas (array), litros_leche_vacas (array),produccion_maxima. Los test llaman a la funcion "elegir_vacas" y comprueban que la producción máxima calculada es la que se ha indicado en el array testdata.
