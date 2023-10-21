import pygame
from pygame.locals import *
from tictactoe import *

pygame.init()
# Configuración de la pantalla
ANCHO, ALTO = 600, 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Tic Tac Toe")

# Colores
LINE_COLOR = ("#3c0384")
CAJA = ("#e773ff")

screen = pygame.display.set_mode((ANCHO, ALTO))
ImgMenu = pygame.image.load("C:./img/inicio.png")
ImgButton = pygame.image.load("C:./img/inicioHover.png")
clock = pygame.time.Clock()

def main():
    current_image = ImgMenu  # Inicialmente, mostramos ImgMenu
    screen.blit(current_image, (0, 0))
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x >= 234 and x <= 365 and y >= 365 and y <= 398:
                    juego_triqui()
            
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if x >= 234 and x <= 365 and y >= 365 and y <= 398:
                    current_image = ImgButton  # Cambiamos a ImgButton cuando se detecta el movimiento
                else:
                    current_image = ImgMenu  # Volvemos a ImgMenu si no hay movimiento en la zona
                    
                screen.blit(current_image, (0, 0))  # Mostramos la imagen actual
                pygame.display.update()
                
            clock.tick(60)

# Ejecuta el juego:
main()
