import random
import string

# Función para generar una sopa de letras aleatoria de tamaño filas x columnas
def generar_sopa_letras(filas, columnas):
    # Definimos el alfabeto en mayúsculas
    alfabeto = string.ascii_uppercase

    # Creamos la sopa de letras como una lista de listas
    sopa = [[random.choice(alfabeto) for _ in range(columnas)] for _ in range(filas)]

    return sopa

# Función para encontrar palabras en la sopa de letras
def encontrar_palabras(sopa_letras, palabras):
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

    resultados = {}
    for palabra in palabras:
        encontrada = False
        visitados = [[False for _ in range(len(sopa_letras[0]))] for _ in range(len(sopa_letras))]

        # Recorremos la sopa de letras para buscar la palabra
        for i in range(len(sopa_letras)):
            for j in range(len(sopa_letras[0])):
                if buscar_palabra(sopa_letras, palabra, i, j, visitados):
                    resultados[palabra] = (i, j)
                    sopa_letras[i][j] = "*"  # Marcar la letra como visitada
                    encontrada = True
                    break
            if encontrada:
                break

    return resultados

# Generar una sopa de letras aleatoria de 10x10
filas = 39
columnas = 39
sopa_letras = generar_sopa_letras(filas, columnas)

# Palabras a buscar en la sopa de letras
palabras_a_buscar = []
with open("dataset.txt") as file:
    for line in file: #Leer cada linea del archivo
        line = line.rstrip() #Almacenar sin el salto de linea
        aux = line.split(',') #Separar por comas
        for element in aux: 
            palabras_a_buscar.append(element.upper()) 


# Encontrar las palabras en la sopa de letras
resultados = encontrar_palabras(sopa_letras, palabras_a_buscar)

# Imprimir la sopa de letras
print("Sopa de letras:")
for fila in sopa_letras:
    print(' '.join(fila))

# Imprimir los resultados
print("\nPalabras encontradas:")
for palabra, posicion in resultados.items():
    print(f'Palabra "{palabra}" encontrada en la posición {posicion}')



