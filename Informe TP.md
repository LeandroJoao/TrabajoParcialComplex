# SOPA DE LETRAS
### TRABAJO PARCIAL - COMPLEJIDAD ALGORITMICA WS6B

INTEGRANTES | CODIGO| 
-|-|
Carbajal Rojas, Andres Eduardo|U202218811   
Joao Rangel, Leandro|U202011073 | 
Quintana Noa, Jimena Alexsandra|U20201F576|

# INTRODUCCIÓN 
El presente informe tiene como objetivo presentar el desarrollo de un proyecto de una sopa de letras implementada en Python.
En este proyecto, se ha utilizado una combinación de dos algoritmos para buscar las palabras en la sopa de letras: el algoritmo de `fuerza bruta` y el algoritmo de `backtracking`. Estos algoritmos permiten explorar todas las posibles combinaciones de letras y direcciones en la sopa de letras de manera eficiente y determinar si una palabra se encuentra presente en ella

# DESCRIPCIÓN DEL PROBLEMA:
El problema a resolver es Sopa de letras. Este famoso juego consiste en buscar palabras en un acomodo de letras, el cual a simple vista aparenta no tener sentido. Las palabras se pueden encontrar de forma horizontal, vertical o diagonal.El juego requiere concetración, conocimiento o experiencia. Además, las palabras a encontrar pueden pertenecer a una temática en específico. (Castro, 2016). 

# PROPUESTA
La propuesta del equipo tiene como objetivo realizar una sopa de letras la cual se resuelva de forma automática. Las técnicas a emplear serán los algoritmos Fuerza Bruta y Backtracking.
El programa recibira un dataset que son las palabras a encontrar en la sopa de letras. Primero, separará las palabras y las almaceranará en una lista para luego separarlas por letra.

## TÉCNICAS Y METODOLOGÍAS USADAS

## FUERZA BRUTA
La `fuerza bruta` es un enfoque directo y sencillo que consiste en probar todas las posibles soluciones de un problema de manera exhaustiva, sin aplicar ninguna estrategia de optimización o reducción del espacio de búsqueda. Este método implica generar todas las combinaciones o permutaciones posibles y evaluar cada una de ellas hasta encontrar la solución correcta. 
Muchos problemas resueltos en la vida cotidiana utilizan la estrategia de fuerza bruta, por ejemplo, explorar todos los caminos hacia un mercado cercano para encontrar el camino más corto mínimo. De hecho, las actividades de la vida diaria tienen una naturaleza de fuerza bruta, aunque también sean posibles algoritmos óptimos (Follow, 2021).

## BACKTRACKING
El `backtracking` se puede definir como una técnica algorítmica general que considera la búsqueda de todas las posibles combinaciones para resolver un problema computacional (GeeksforGeeks, 2017). Se basa en la exploración sistemática de un espacio de búsqueda, tomando decisiones parciales y retrocediendo cuando se alcanza un punto sin salida.

# DISEÑO DE LA APLICACIÓN

## LEER DATASET
En el código, se lee cada línea del archivo txt y separa las palabras por comas. Finalmente, se almacena en la lista `palabras_a_buscar` y se convierten a mayúsculas con la función `upper()`.

    palabras_a_buscar = []
    with open("dataset.txt") as file:
        for line in file: #Leer cada linea del archivo
            line = line.rstrip() #Almacenar sin el salto de linea
            aux = line.split(',') #Separar por comas
            for element in aux: 
                palabras_a_buscar.append(element.upper())

## FUERZA BRUTA 
### APLICACIÓN EN EL CÓDIGO
En el código, se recorren todas las posiciones posibles en la sopa de letras y se prueban todas las direcciones (horizontal, vertical, diagonal) para buscar una palabra específica. Esto se realiza mediante los bucles anidados que recorren las filas, las columnas y las direcciones en el código.

    # Movimientos posibles (arriba, abajo, izquierda, derecha, diagonales)
     movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
     
     for df, dc in movimientos:
                if buscar_palabra(sopa_letras, palabra[1:], fila + df, columna + dc, visitados):
                    return True

## BACKTRACKING
### APLICACIÓN EN EL CÓDIGO
El algoritmo de backtracking se utiliza en la función `buscar_palabra` para realizar una búsqueda recursiva en la sopa de letras. La función verifica si la letra actual coincide con la primera letra de la palabra que se está buscando. Si es así, marca la letra como visitada y realiza una llamada recursiva para buscar el resto de la palabra en una dirección específica. Si la búsqueda recursiva es exitosa, se devuelve True, lo que indica que la palabra se ha encontrado. Si no es exitosa, se deshace el cambio y se continúa probando en otras direcciones.

    def buscar_palabra(sopa_letras, palabra, fila, columna, visitados):
        if not palabra:
            return True
        if (
            0 <= fila < len(sopa_letras) and
            0 <= columna < len(sopa_letras[0]) and
            sopa_letras[fila][columna] == palabra[0] and
            not visitados[fila][columna]
        ):
            visitados[fila][columna] = True

            # Movimientos posibles (arriba, abajo, izquierda, derecha, diagonales)
            movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

            for df, dc in movimientos:
                if buscar_palabra(sopa_letras, palabra[1:], fila + df, columna + dc, visitados):
                    return True

            visitados[fila][columna] = False

        return False

# VALIDACIÓN DE RESULTADOS Y PRUEBAS
A continuación, se muestra la matriz generada aleatoriamente. Además, el resultado de la búsqueda con las coordenadas de la primera letra de la palabra. 

![image](https://github.com/LeandroJoao/TrabajoParcialComplex/assets/107333230/c7522ff5-d133-4407-8b39-b48ac1f18a8d)

# CONCLUCIONES 
Con esta entrega hemos reforzado los conocimientos respecto a los algoritmos `Fuerza Bruta` y `Backtracking`. Los cuales, nos ayudan a solucionar problemas de búsqueda sistemática. Además, con el trabajo realizado ahondamos más en el lenguaje de programacion `Python` ,el cuál, hasta el principio del semestre era nuevo para los integrantes del equipo. Finalmente el uso de herramientas como Github nos permitió conocer más acerca del uso de Issues y commit, lo cual nos ayudará en futuros proyectos.

# REFERENCIAS BIBLIOGRAFICAS
Backtracking algorithms. (2017, agosto 10). GeeksforGeeks. https://www.geeksforgeeks.org/backtracking-algorithms/
Castro, M. (2016). LA HISTORIA DE LAS SOPAS DE LETRAS. https://www.academia.edu/22669826/LA_HISTORIA_DE_LAS_SOPAS_DE_LETRAS
Follow, S. (2021). Brute Force Approach and its pros and cons. GeeksforGeeks. https://www.geeksforgeeks.org/brute-force-approach-and-its-pros-and-cons/
