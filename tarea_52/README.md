# TAREA 52: Estructura de datos

## Requerimientos

Python

## Resumen estructura numeros

Para ejecutar, desde la línea de comandos y el directorio de la tarea_52:

        python numeros.py

En la consola se muestra un mensaje para introducir números a la lista, o 0 para continuar. Al pulsar 0, se muestra la lista y un menu con las opciones del programa:

        C:\repos\theegg_ai\tarea_52>python numeros.py
        Introduce numero a añadir a la estructura, 0 para continuar:
        3
        Introduce numero a añadir a la estructura, 0 para continuar:
        2
        Introduce numero a añadir a la estructura, 0 para continuar:
        6
        Introduce numero a añadir a la estructura, 0 para continuar:
        12
        Introduce numero a añadir a la estructura, 0 para continuar:
        22
        Introduce numero a añadir a la estructura, 0 para continuar:
        0
        La lista es = [3, 2, 6, 12, 22]

    Elige tu opción:
    1- Eliminar primera ocurrencia de un número
    2 - Recorrer la lista para imprimir la sumatoria de todos los elementos.
    3 - Crear una lista eliminando los elementos que sean mayores que un número
    4 - Ocurrencias de la lista
    5 - Añadir nuevo número
    6 - Restaurar lista original ([3, 2, 6, 12, 22])
    0 - Salir

Las opciones son las siguientes:

### 1 Eliminar número

Se pide un número para eliminar y se muestra la nueva lista. Si el número no está en la lista se avisa al usuario

        Introduce numero a eliminar:
        11
        El numero 11 no está en la lista
        La lista es = [3, 6, 12, 22]

### 2 Sumatorio

Se devuelve el sumatorio de todos los elementos del array, y se muestra junto a la lista

        La suma de los elementos es = 43
        La lista es = [3, 6, 12, 22]

### 3 Elimianr elementos mayores que un número

Se pide el número y se muestra la nueva lista

        Introduce numero a comparar:
        7
        La lista es = [3, 6]

### 4 - Ocurrencias de la lista

Devuelve el número de ocurrencias de cada número

        Las ocurrencias son (numero,ocuurencias) = [(3, 1), (6, 1)]
        La lista es = [3, 6]

### 5 - Añadir nuevo número

Añade un número que se introduzca a la lista

        55
        La lista es = [3, 6, 55]

### 6 - Restaurar lista original

Carga en memoria la lista original introducida en el programa

    La lista es = [3, 2, 6, 12, 22]

### 0 - Salir

## Resumen estructura nombres

Para ejecutar, desde la línea de comandos y el directorio de la tarea_52:

        python nombres.py

En la consola se muestra un mensaje para introducir primero los nombres de primario y luego los de secundario. Para continuar hay que introducir el nombre "?x?". El sistema muestra los nombres de cada curso tras finalizar su introducción. Después de finalizar con los nombres de secundario, el programa muestra los nombres en base al enunciado:

        C:\repos\theegg_ai\tarea_52>python nombres.py
        Nombres de pila de los alumnos de nivel primario

        ---

        Introduce nombre a añadir , ?x? para continuar:
        Jon
        Introduce nombre a añadir , ?x? para continuar:
        Ander
        Introduce nombre a añadir , ?x? para continuar:
        Naia
        Introduce nombre a añadir , ?x? para continuar:
        Leire
        Introduce nombre a añadir , ?x? para continuar:
        ?x?
        Todos los nombres de primario ['Jon', 'Ander', 'Naia', 'Leire']

        ---

        Nombres de pila de los alumnos de nivel secundario

        ---

        Introduce nombre a añadir , ?x? para continuar:
        Leire
        Introduce nombre a añadir , ?x? para continuar:
        Ane
        Introduce nombre a añadir , ?x? para continuar:
        Mikel
        Introduce nombre a añadir , ?x? para continuar:
        Jon
        Introduce nombre a añadir , ?x? para continuar:
        ?x?
        Todos los nombres de secundario ['Leire', 'Ane', 'Mikel', 'Jon']

        ---

        Todos los nombres de primario y secundario sin duplicados ['Ander', 'Ane', 'Jon', 'Leire', 'Mikel', 'Naia']
        Todos los nombres comunes sin duplicados ['Jon', 'Leire']
        Todos los nombres que sólo están en primario sin duplicados ['Ander', 'Naia']

## Explicación números

Desde el fichero numeros.py se piden los números y las opciones necesarias, y se crea un objeto de EstructuraNumeros con la lista. Este objeto se encarga de hacer las operaciones sobre la lista. Las operaciones son inmutables, no alteran la lista original y devuelven una nueva lista en cada oepración. Aunque esto obligue a no utilizar los métodos de list de Python, tiene ventajas como que el código es más predecible y fácil de testear. Su desventaja es que pierde eficiencia al tener que crear duplicados de los objetos. Es algo personal, pero desde mi punto de vista si el rendimiento no es un problema, el mantenimiento del código mejora con la inmutabilidad. Para contar las ocurrencias se hace uso de la clase COunter de collections

Se ha considerado que el uso de listas era la mejor opción por el tipo de operaciones a realizar

## Explicación nombres

Desde el fichero nombres.py se piden los nombres de primario y secundario, y se crea un objeto de EstructuraNombres con la lista de los nombres de primario. Este objeto se encarga de hacer las operaciones del ejercicio. Las operaciones son inmutables, no alteran la lista original y devuelven una nueva lista en cada oepración. Aunque esto obligue a no utilizar los métodos de list de Python, tiene ventajas como que el código es más predecible y fácil de testear. Su desventaja es que pierde eficiencia al tener que crear duplicados de los objetos. Es algo personal, pero desde mi punto de vista si el rendimiento no es un problema, el mantenimiento del código mejora con la inmutabilidad. Para mostrar los resultados ordenados se hace uso de sorted, que es inmutable, en vez de lista.sorted() que altera la lista original.

Se ha considerado que el uso de sets era la mejor opción por el tipo de operaciones a realizar. Los sets se utilizan para realizar las operaciones, pero luego los resultados se devuelve como listas para dar flexibilidad al usuario. Se ha considerado que el rendimineto no va a ser un problema y esta opción simplifica la utilización de la estructura.

## Paso adicional: Test

Para lanzar los test es necesario instalar la librería pytest (https://docs.pytest.org/en/stable/getting-started.html)

A continuación basta con ejecutar pytest. La consola debe mostar un mensaje en verde similar a "2 passed in 0.05s"

Los test se encuentra en los ficheros "estructura_numeros_test.py" y "estructura_nombres_test.py". En estos ficheros hay un test para cada operación requerida.
