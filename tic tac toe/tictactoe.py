import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 600, 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Tic Tac Toe")

# Colores
LINE_COLOR = ("#3c0384")
CAJA = ("#e773ff")

# Función para dibujar el tablero
def dibujar_tablero(tablero):
    for fila in range(3):
        for columna in range(3):
            pygame.draw.rect(PANTALLA, CAJA, (columna * 200, fila * 200, 200, 200))
            pygame.draw.rect(PANTALLA, LINE_COLOR, (columna * 200, fila * 200, 200, 200), 10)
            if tablero[fila][columna] == "X":
                x_image = pygame.image.load("C:./img/x.png")
                PANTALLA.blit(x_image, (columna * 200 + 10, fila * 200 + 10))
            elif tablero[fila][columna] == "O":
                o_image = pygame.image.load("C:./img/o.png")
                PANTALLA.blit(o_image, (columna * 200 + 10, fila * 200 + 10))

# Función para verificar el ganador
def verificar_ganador(tablero, jugador):
    # Verificar filas, columnas y diagonales
    for i in range(3):
        if all(tablero[i][j] == jugador for j in range(3)) or all(tablero[j][i] == jugador for j in range(3)):
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador or tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    return False

# Función principal del juego
def juego_triqui():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"
    juego_terminado = False

    while not juego_terminado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if jugador_actual == "X":
                if evento.type == pygame.MOUSEBUTTONDOWN and not juego_terminado:
                    x, y = evento.pos
                    fila, columna = y // 200, x // 200
                    if tablero[fila][columna] == " ":
                        tablero[fila][columna] = "X"
                        jugador_actual = "O"
            else:
                # Simulación del movimiento del computador
                fila, columna = movimiento_computador(tablero)
                if tablero[fila][columna] == " ":
                    tablero[fila][columna] = "O"
                    jugador_actual = "X"

            # Verificar el estado del juego
            if verificar_ganador(tablero, "X"):
                juego_terminado = True
                ganador = "Jugador"
            elif verificar_ganador(tablero, "O"):
                juego_terminado = True
                ganador = "Computadora"
            elif all(all(casilla != " " for casilla in fila) for fila in tablero):
                juego_terminado = True
                ganador = "Empate"

            PANTALLA.fill(CAJA)
            dibujar_tablero(tablero)
            pygame.display.update()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Mostrar mensaje de resultado
        if ganador == "Empate":
            resultado_imagen = pygame.image.load("C:./img/empate.png")
        elif ganador == "Jugador":
            resultado_imagen = pygame.image.load("C:./img/p1Win.png")
        else:
            resultado_imagen = pygame.image.load("C:./img/p2Win.png")

        PANTALLA.blit(resultado_imagen, (columna, fila))
        pygame.display.update()

#Función para el movimiento de la computadora
def movimiento_computador(tablero):
    casillas_vacias = [(fila, columna) for fila in range(3) for columna in range(3) if tablero[fila][columna] == " "]

    if casillas_vacias:
        return random.choice(casillas_vacias)
