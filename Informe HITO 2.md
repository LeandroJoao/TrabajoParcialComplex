# SOPA DE LETRAS
### TRABAJO PARCIAL - COMPLEJIDAD ALGORITMICA WS6B

INTEGRANTES | CODIGO| 
-|-|
Carbajal Rojas, Andres Eduardo|   
Joao Rangel, Leandro| | 
Quintana Noa, Jimena Alexsandra|U20201F576|

# INTRODUCCIÓN 
El presente informe tiene como objetivo presentar el desarrollo de un proyecto de una sopa de letras implementada en Python.
En este proyecto, se ha utilizado una combinación de dos algoritmos para buscar las palabras en la sopa de letras: el algoritmo de `fuerza bruta`, el algoritmo de `backtracking` y `Programación Dinámica`. Estos algoritmos permiten explorar todas las posibles combinaciones de letras y direcciones en la sopa de letras de manera eficiente y determinar si una palabra se encuentra presente en ella

# DESCRIPCIÓN DEL PROBLEMA:

El juego de búsqueda de palabras, conocido como `sopa de letras`, es un entretenimiento muy popular en el que se disponen palabras en una cuadrícula de letras. El objetivo principal del juego consiste en encontrar palabras específicas ocultas entre las letras del tablero. Estas palabras pueden estar dispuestas en diversas direcciones: horizontal, vertical, diagonal, de izquierda a derecha o viceversa. Por lo general, las palabras a buscar se muestran como pistas en la parte inferior o lateral del tablero.

La sopa de letras es una actividad que evalúa la capacidad de observación, concentración y habilidad para encontrar palabras de los participantes. Con frecuencia, se utiliza como una herramienta educativa en entornos escolares para mejorar el vocabulario y la ortografía. (Castro, 2016)

Sin emabargo, ¿Qué pasa cuando el jugador pasa más de 10 minutos buscando una palabra? El juego puede llegara a ser tedioso cuando no se logra encontrar la palabra que se busca, más aun cuando la cuadrícula de letras es de una dimensión considerable. Por ello, nuestro proyecto busca ayudar a lo jugadores a encontrar con mayor facilidad la palabra que se busca. A través de la inteligencia artifical, proponemos desarrollar un bot que resuelva la sopa de letras cuando el jugador lo requiera. 

Como menciona Urbano (2023), la integración de la Inteligencia Artificial (IA) en los mecanismos de diseño de videojuegos ha ido en aumento, lo que ha mejorado el proceso de empatía e inmersión del jugador. Desde hace tiempo, se ha utilizado la IA en diferentes aspectos de los videojuegos, como la implementación de personajes no jugadores, el desarrollo de escenarios de forma procedural y el diseño de mecánicas de juego que se adaptan al jugador. Por lo que la combinación de el algoritmo de `fuerza bruta` y el algoritmo de `backtracking` permitirá que el jugador haga uso de la inteligencia artificial para encontrar una palabra rápidamente, para que así no se fruste por el juego y llegue a dejarlo inconcluso.

Este proyecto busca mantener al jugador enfocado en el juego, otorgandole una ayuda para cuando quiera abandonar el juego. A su vez, demostrar la capacidad de la inteligencia artificial al resolver problemas complejos. Con ello, los objetivos planteados para ste proyecto son:

- Implementar los algoritmos aprendidos en clase en el juego de la sopa de letras.
- Desarrollar algoritmos de búsqueda eficientes
- Realización de pruebas exhaustivas y con ello garantizar una experiencia satisfactoria del usuario.

# PROPUESTA

La propuesta del equipo tiene como objetivo realizar una sopa de letras la cual se resuelva de forma automática. Las técnicas a emplear serán los algoritmos `Fuerza Bruta`, `Backtracking` y `Programación Dinámica`.
El programa recibira un dataset que son las palabras a encontrar en la sopa de letras. Primero, separará las palabras y las almaceranará en una lista para luego separarlas por letra.

Para el desarrollo del juego, el algoritmo de backtracking se utiliza para realizar una búsqueda recursiva en la sopa de letras. La función verifica si la letra actual coincide con la primera letra de la palabra que se está buscando. Si es así, marca la letra como visitada y realiza una llamada recursiva para buscar el resto de la palabra en una dirección específica. Si la búsqueda recursiva es exitosa, se devuelve True, lo que indica que la palabra se ha encontrado. Si no es exitosa, se deshace el cambio y se continúa probando en otras direcciones.

Por otro lado, la inclusión de programación dinámica mejorar aún más el rendimiento y la eficiencia del juego, especialmente en tableros de sopa de letras más grandes o con un gran número de palabras a buscar. El uso de la programación dinámica se centra en el almacenamiento de resultados intermedios para evitar recálculos innecesarios. Esto acelerará el proceso y hará que la búsqueda de palabras en la sopa de letras sea más eficiente, lo que es beneficioso cuando se trata de resolver tableros más grandes o con muchas palabras.

# DESCRIPCIÓN DEL CONJUNTO DE DATOS (Dataset)

Para este proyecto, los datos que impulsan el análisis en este caso son las palabras que se encuentran en una sopa de letras. Estas palabras se derivan de la configuración del tablero y las restricciones que se aplican a la búsqueda.

Cada palabra en la sopa de letras representa un objetivo de búsqueda en el juego, y puede considerarse como un nodo en un grafo dirigido. Los nodos están conectados por aristas que representan la dirección y la ubicación de las letras en el tablero. Cada nodo se asocia con una palabra específica que se puede encontrar en la sopa de letras.

Dado que el número de posibles palabras en la sopa de letras es finito pero considerable, es posible explorar exhaustivamente todas las palabras. Sin embargo, debido a la cantidad de letras y disposiciones en una sopa de letras, se aplican técnicas para reducir la cantidad de exploraciones necesarias y hacer más eficiente el proceso de búsqueda. En promedio, se estima que hay un número significativo de palabras que se pueden encontrar en una sopa de letras.

Al crear un grafo que simula la búsqueda de palabras en la sopa de letras, se obtiene una estructura con nodos que representan las palabras encontradas en el juego. El número de nodos en el grafo depende del tamaño y la complejidad de la sopa de letras, pero permite una representación visual y organizada de las palabras objetivo.

# DISEÑO DE LA APLICACIÓN

Para el desarrollo del juego de sopa de letras, se ha propuesto utilizar una combinación de tecnologías y bibliotecas, como Python y PyQt, que permitirán la creación de una interfaz gráfica atractiva y funcional. PyQt es una biblioteca que ofrece una amplia variedad de herramientas para diseñar interfaces de usuario interactivas en Python, lo que resulta perfecto para crear la experiencia de juego.

El juego de sopa de letras se centrará en la generación aleatoria de tableros con letras dispuestas en una cuadrícula y un conjunto de palabras que los jugadores deben encontrar. La interfaz de usuario permitirá a los jugadores seleccionar letras y formar palabras haciendo clic y arrastrando, y se proporcionarán pistas o un temporizador para añadir emoción al juego.

El juego también incluirá características como la posibilidad de elegir diferentes niveles de dificultad, categorías de palabras y, posiblemente, la opción de competir contra otros jugadores en línea.

En resumen, la propuesta busca crear un juego de sopa de letras atractivo y entretenido, utilizando las capacidades de PyQt y Python para brindar una experiencia de juego interactiva y desafiante. La combinación de una interfaz gráfica atractiva y la mecánica del juego de sopa de letras ofrecerá a los jugadores una experiencia divertida y educativa.



# BIBLIOGRAFÍA

Urbano, A., D., & Cantos, R. (2023). El uso de la Inteligencia Artificial en el proceso de diseño del habla y el lenguaje de un personaje de videojuegos. Miguel Hernández Communication Journal, 14, 427–447. https://doi.org/10.21134/mhjournal.v14i.1985

Castro, M. (2016). LA HISTORIA DE LAS SOPAS DE LETRAS. https://www.academia.edu/22669826/LA_HISTORIA_DE_LAS_SOPAS_DE_LETRAS 


