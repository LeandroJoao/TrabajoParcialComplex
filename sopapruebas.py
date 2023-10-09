import random
import string

def generar_sopa_letras(filas, columnas):
    alfabeto = string.ascii_uppercase
    sopa = [[random.choice(alfabeto) for _ in range(columnas)] for _ in range(filas)]
    return sopa

def encontrar_palabras(sopa_letras, palabras):
    def buscar_palabra(fila, columna, palabra, direccion):
        if len(palabra) == 0:
            return True

        if (
            0 <= fila < len(sopa_letras) and
            0 <= columna < len(sopa_letras[0]) and
            sopa_letras[fila][columna] == palabra[0]
        ):
            letra_temporal = sopa_letras[fila][columna]
            sopa_letras[fila][columna] = "*"  # Marcar la letra como visitada

            df, dc = direcciones[direccion]

            if buscar_palabra(fila + df, columna + dc, palabra[1:], direccion):
                return True

            sopa_letras[fila][columna] = letra_temporal  # Deshacer el cambio

        return False

    def buscar_en_sopa(palabra):
        for i in range(len(sopa_letras)):
            for j in range(len(sopa_letras[0])):
                for direccion in range(8):
                    if buscar_palabra(i, j, palabra, direccion):
                        return True
        return False

    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    resultados = {}

    for palabra in palabras:
        encontrada = buscar_en_sopa(palabra)
        if encontrada:
            resultados[palabra] = "Palabra encontrada en la sopa de letras"

    return resultados

# Generar una sopa de letras aleatoria de 10x10
filas = 30
columnas = 30
sopa_letras = generar_sopa_letras(filas, columnas)

# Palabras a buscar en la sopa de letras
palabras_a_buscar = ["PYTHON", "COLAB", "IA", "BACKTRACKING", "AGUA","POLLO","ola","TECLADO","NUTRIA"
                     "manzana","polo","patas","camiseta","LOMPA"
                     "PANTALLA","PARLANTE","MEDIAS","PIZARRA","AZUCAR"
                     "HOLA", "SOCU", "NAME", "JNO", "NMV", "DAGO"
                     "RIP", "BUO", "NOA", "ROE", "AOD", "AS"]

# Encontrar las palabras en la sopa de letras
resultados = encontrar_palabras(sopa_letras, palabras_a_buscar)

# Imprimir la sopa de letras
print("Sopa de letras:")
for fila in sopa_letras:
    print(' '.join(fila))

# Imprimir los resultados
for palabra, resultado in resultados.items():
    print(f'Palabra "{palabra}": {resultado}')