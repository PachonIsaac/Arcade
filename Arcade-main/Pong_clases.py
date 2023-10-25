import pygame
import os
from Menu import main_menu
pygame.init()

#colores
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)

size = (800,600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#Get current directory
current_directory = os.path.dirname(__file__)
#Load background image
PongClassic_Background = os.path.join(current_directory,"Assets/Background/PongClassic_Background.png")
PongClassic_Background = pygame.image.load(PongClassic_Background).convert_alpha()
sonido_raqueta = pygame.mixer.Sound("Assets/Sound/Raqueta.mp3")
gol = pygame.mixer.Sound("Assets/Sound/Gol.mp3")


class Player1():
    def __init__(self):
        self.width = 15
        self.height = 90
        self.x_coor = 50
        self.y_coor = 255
        self.y_speed = 0
        self.x_speed = 0
        self.puntos = 0

    def dibujar(self, screen):
        pygame.draw.rect(screen, white, [self.x_coor, self.y_coor, self.width, self.height])

    def mover(self):
        self.y_coor += self.y_speed
        self.x_coor += self.x_speed
    
    def movimientos(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.y_speed = -3
            if event.key == pygame.K_s:
                self.y_speed = 3
            if event.key == pygame.K_a:
                self.x_speed = -3
            if event.key == pygame.K_d:
                self.x_speed = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.y_speed = 0
            if event.key == pygame.K_s:
                self.y_speed = 0
            if event.key == pygame.K_a:
                self.x_speed = 0
            if event.key == pygame.K_d:
                self.x_speed = 0
    def colision(self, linea):
        if self.y_coor > 510 or self.y_coor < 0:
            self.y_speed *= -1
        if self.x_coor > 385 or self.x_coor < 0:
            self.x_speed *= -1

class Player2():
    def __init__(self):
        self.width = 15
        self.height = 90
        self.x_coor = 735
        self.y_coor = 255
        self.y_speed = 0
        self.x_speed = 0
        self.puntos = 0

    def dibujar(self, screen):
        pygame.draw.rect(screen, white, [self.x_coor, self.y_coor, self.width, self.height])

    def mover(self):
        self.y_coor += self.y_speed
        self.x_coor += self.x_speed
    
    def movimientos(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.y_speed = -3
            if event.key == pygame.K_DOWN:
                self.y_speed = 3
            if event.key == pygame.K_LEFT:
                self.x_speed = -3
            if event.key == pygame.K_RIGHT:
                self.x_speed = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.y_speed = 0
            if event.key == pygame.K_DOWN:
                self.y_speed = 0
            if event.key == pygame.K_LEFT:
                self.x_speed = 0
            if event.key == pygame.K_RIGHT:
                self.x_speed = 0
    
    def colision(self, linea):
        if self.y_coor > 510 or self.y_coor < 0:
            self.y_speed *= -1
        if self.x_coor > 785 or self.x_coor < 400:
            self.x_speed *= -1


    
class Pelota():
    def __init__(self):
        self.x = 400
        self.y = 300
        self.speed_x = 3
        self.speed_y = 3
        self.radio = 10

    def dibujar(self, screen):
        pelota = pygame.draw.circle(screen, white, [self.x, self.y], self.radio)
        return pelota

    def mover(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def movimiento(self):
        if self.y > 590 or self.y < 10:
            self.speed_y *= -1
    
    def colision(self, player1, player2):
        if self.x < player1.x_coor + player1.width and self.y < player1.y_coor + player1.height and self.y > player1.y_coor:
            self.speed_x *= -1
            pygame.mixer.Sound.play(sonido_raqueta)
        if self.x > player2.x_coor and self.y < player2.y_coor + player2.height and self.y > player2.y_coor:
            self.speed_x *= -1
            pygame.mixer.Sound.play(sonido_raqueta)
        
    

def juego_pong():
    puntos1 = 0
    puntos2 = 0
    game_over = False
    pelota = Pelota()  # Crear la pelota como una instancia de la clase Pelota
    player1 = Player1()
    player2 = Player2()
    fuente = pygame.font.SysFont("Arial", 60)
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                    main_menu()
            player1.movimientos(event)
            player2.movimientos(event)

        if pelota.x > 800:
            pelota.x = 400
            pelota.y = 300
            pelota.speed_x *= -1
            pelota.speed_y *= -1
            puntos1 += 1
            pygame.mixer.Sound.play(gol)

    #si la pelota sale del lado izquierdo
        if pelota.x < 0:
            pelota.x = 400
            pelota.y = 300
            pelota.speed_x *= -1
            pelota.speed_y *= -1
            puntos2 += 1
            pygame.mixer.Sound.play(gol)

        if puntos1 == 5 or puntos2 == 5:
            game_over = True

        player1.mover()
        player2.mover()
        pelota.mover()
        pelota.movimiento()
        pelota.colision(player1, player2)
        screen.fill(black)
        screen.blit(PongClassic_Background, (0, 0))
        linea = pygame.draw.line(screen, white, (400, 0), (400, 600), 5)
        player1.dibujar(screen)
        player2.dibujar(screen)
        pelota.dibujar(screen)
        player1.colision(linea)
        player2.colision(linea)
        Texto1 = fuente.render(str(puntos1),False,white)
        Texto2 = fuente.render(str(puntos2),False,white)
        screen.blit(Texto1,(350,10))
        screen.blit(Texto2,(450,10))
        pygame.display.update()
        pygame.time.Clock().tick(60)

