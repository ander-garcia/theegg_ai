# TAREA 45: Algoritmos de búsqueda

## Requerimientos

Python

## Resumen

Para ejecutar, desde la línea de comandos y el directorio de la tarea_41:

        python main.py

En la consola se muestra la lista sin ordenar, la posición del número 874 y el número de iteraciones de búsaueda con el algoritmo secuencial. Luego se ordena la lista, se muestra ordenada y se muestra de nuevo el índice del mismo número y las iteraciones utilizadas con el algoritmo secucnial y el binario

        Lista original =  [3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56]
        Indice del número 874 e iteraciones de búsqueda con el algoritmo secuencial =  (4, 5)
        Lista ordenada =  [3, 21, 23, 33, 45, 56, 56, 65, 66, 123, 874, 1000]
        Indice del número 874 e iteraciones de búsqueda con el algoritmo secuencial =  (10, 11)
        Indice del número 874 e iteraciones de búsqueda con el algoritmo binario =  (10, 3)

## Explicación

Desde el fichero main.py se crea un objeto de Searcher con la lista. Desde este objeto se llaman a los métodos de ordenar y búsqueda y se muestran por pantalla los resultados. El código de los algoritmos está en la clase Searcher en el fichero searcher.py. La clase Searcher tiene un constructor en el que se indica la lista de números y los métodos de los algoritmos.

El método sort encapsula la llamada al algoritmo merge_sort.Se ha implementado este algoritmo por su buen rendimiento. El algoritmo divide la lista en mitades, hasta que se alcanzan listas de un elemento. Luego, estas listas se van uniendo y ordenando. La explicación de este algoritmo y otros algoritmos de búsqueda se puede consultar en https://www.geeksforgeeks.org/sorting-algorithms/

En las búsquedas, hay un método para la búsqueda secuencial y otro para la binaria. Ambos devuelven el índice del valor buscado y el número de iteraciones empleadas. En el caso de la búsqueda binaria, como la lista tiene que estar ordenada si no lo está se lanza una excepción y primero se comprueba que el valor está en el rango entre el primer y el último elemento. En caso contrario, el valor no va a estar dentro de la lista

## Paso adicional: Test

Para lanzar los test es necesario instalar la librería pytest (https://docs.pytest.org/en/stable/getting-started.html)

A continuación basta con ejecutar pytest. La consola debe mostar un mensaje en verde similar a "2 passed in 0.05s"

Los test se encuentra en el fichero "text_searcher.py". En este fichero hay tres tests, uno para cada algoritmo.

## Rendimiento: análisis Big 0

### Merge sort

Este algoritmo siempre se ejecuta el mismo número de veces para la misma longitud de entrada: siempre tiene que dividir la lista de entrada hasta dividirla en listas de longitud 1, y luego ir juntándolas hasta alcanzar la longitud final. Su complejidad es la misma en el mejor y en el peor de los casos.

Al dividr el array en mitades necesita log(n) iteraciones, y como luego es necesario hacer los merges, su complejidad es O(nlog(n)

### Búsqueda secuencial

En esta búsqueda, en el mejor de los casos el primer elemento será el de la búsqueda y sólo habrá una iteración. SI el elemento está al final (peor de los casos), se necesitarán n iteraciones. En el caso medio, se necesitarán n/2 iteraciones. Por tanto, su complejidad se considera O(n)

### Búsqueda binaria

En esta búsqueda, en el mejor de los casos el elemento de la mitad será el de la búsqueda y sólo habrá una iteración. Si el elemento está en otra posición, en el peor de los casos habrá que hacer log(n) iteraciones. En el caso medio también se necesitarán log(n) iteraciones, ya que en la mayoría de las posiciones es necesario hacer log(n) divisiones por la mitad. Por tanto, su complejidad se considera O(log(n))

### Comparación

A modo de ejemplo se ha ejecutado el algoritmo de búsqueda sobre arrays aleatorios de diferente longitud (desde 10 a 1000000), y se ha buscado el primer elemento, el último y el de la mitad. El fichero rendimiento.py muestra los resultados separados por ; en el formato longitud-índice del valor a buscar-iteraciones-tipo de algoritmo de búsqueda.

Para la búsqueda binaria, salvo cuando se busca el valor de la mitad (1 iteración),en el resto de casos las iteraciones se corresponden con log(n), necesitándose 20 iteraciones para 1000000 elementos

En el caso de la búsqueda secuencial, se necesitan 1 iteración (primer elemento), n/2 (elemento mitad) y n iteraciones (último elemento). En el caso del array de 1000000 elementos, en el peor caso se necesitan 1000000 iteraciones
