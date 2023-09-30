# SOPA DE LETRAS
### TRABAJO PARCIAL - COMPLEJIDAD ALGORITMICA WS6B

INTEGRANTES | CODIGO| 
-|-|
Carbajal Rojas, Andres Eduardo|   
Joao Rangel, Leandro| | 
Quintana Noa, Jimena Alexsandra|U20201F576|

# INTRODUCCIÓN 
El presente informe tiene como objetivo presentar el desarrollo de un proyecto de una sopa de letras implementada en Python.
En este proyecto, se ha utilizado una combinación de dos algoritmos para buscar las palabras en la sopa de letras: el algoritmo de `fuerza bruta` y el algoritmo de `backtracking`. Estos algoritmos permiten explorar todas las posibles combinaciones de letras y direcciones en la sopa de letras de manera eficiente y determinar si una palabra se encuentra presente en ella

# DESCRIPCIÓN DEL PROBLEMA:

El problema a resolver es Sopa de letras. Este famoso juego consiste en buscar palabras en un acomodo de letras, el cual a simple vista aparenta no tener sentido. Las palabras se pueden encontrar de forma horizontal, vertical o diagonal.El juego requiere concetración, conocimiento o experiencia. Además, las palabras a encontrar pueden pertenecer a una temática en específico. (Castro, 2016). 

# OBJETIVOS

- Implementar los algoritmos aprendidos en clase para el desarrollo y solución del porblema escogido.
- 

# PROPUESTA

La propuesta del equipo tiene como objetivo realizar una sopa de letras la cual se resuelva de forma automática. Las técnicas a emplear serán los algoritmos Fuerza Bruta y Backtracking.
El programa recibira un dataset que son las palabras a encontrar en la sopa de letras. Primero, separará las palabras y las almaceranará en una lista para luego separarlas por letra.

# MARCO TEORICO 

## FUERZA BRUTA
La `fuerza bruta` es un enfoque directo y sencillo que consiste en probar todas las posibles soluciones de un problema de manera exhaustiva, sin aplicar ninguna estrategia de optimización o reducción del espacio de búsqueda. Este método implica generar todas las combinaciones o permutaciones posibles y evaluar cada una de ellas hasta encontrar la solución correcta.

### APLICACIÓN EN EL CÓDIGO
En el código, se recorren todas las posiciones posibles en la sopa de letras y se prueban todas las direcciones (horizontal, vertical, diagonal) para buscar una palabra específica. Esto se realiza mediante los bucles anidados que recorren las filas, las columnas y las direcciones en el código.



## BACKTRACKING
El `Backtracking` es una técnica algorítmica utilizada para resolver problemas de búsqueda exhaustiva y encontrar todas las soluciones posibles. Se basa en la exploración sistemática de un espacio de búsqueda, tomando decisiones parciales y retrocediendo cuando se alcanza un punto sin salida.

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

# DESARROLLO



# BIBLIOGRAFÍA
Castro, M. (2016). LA HISTORIA DE LAS SOPAS DE LETRAS. https://www.academia.edu/22669826/LA_HISTORIA_DE_LAS_SOPAS_DE_LETRAS 

