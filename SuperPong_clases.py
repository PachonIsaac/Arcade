import pygame
import os

pygame.init()       #Inicializar pygame

black = (0, 0, 0)                       #Color negro en RGB
white = (255,255,255)                   #Blanco en RGB

size = (800, 600)                       #Variable size con las dimenesiones de la pantalla (Ancho, Alto)
screen = pygame.display.set_mode(size)  #Se crea la pantalla con las dimensiones de size
clock = pygame.time.Clock()             #

# Get current directory
current_directory = os.path.dirname(__file__)

# Load Assets
PongRetro_Background = os.path.join(current_directory, "Assets/Background/PongRetro_Background.png")
PongRetro_Background = pygame.image.load(PongRetro_Background).convert_alpha()
WinnerKen            = pygame.image.load(os.path.join(current_directory, "Assets/PongRetro/WinnerKen.png"))
WinnerRyu            = pygame.image.load(os.path.join(current_directory, "Assets/PongRetro/WinnerRyu.png"))
Proyectil_Image = pygame.image.load(os.path.join(current_directory, "Assets/PongRetro/Hadoken.png")).convert_alpha()
Sonido_Golpe = pygame.mixer.Sound("Arcade/Assets/Sound/Golpe.mp3")
gol = pygame.mixer.Sound("Arcade/Assets/Sound/Gol.mp3")                                                             

#Se carga la imagen que suena durante el juego
pygame.mixer.music.load("Arcade/Assets/Sound/Kens Theme.mp3")


#Clase Proyectil
class Proyectil:
    def __init__(self, x_coor, y_coor, speed_x, speed_y):           #Constructor de la clase
        self.image = Proyectil_Image                                # Usar la imagen del proyectil
        self.rect = self.image.get_rect()                           # Obtener el rectangulo de la imagen
        self.rect.center = (x_coor, y_coor)                         # Centrar el rectangulo en las coordenadas
        self.speed_x = speed_x                                      # Velocidad en X
        self.speed_y = speed_y                                      # Velocidad en Y

    def dibujar(self, screen):                                                      # Dibujar el proyectil
        if self.speed_x < 0:                                                        # Si la velocidad en X es negativa
            screen.blit(pygame.transform.flip(self.image, True, False), self.rect)  # Dibujar la imagen volteada horizontalmente
        else:                                                                       # Si la velocidad en X es positiva
            screen.blit(self.image, self.rect)                                      # Dibujar la imagen normalmente

    def mover(self):                                                                # Mover el proyectil
        self.rect.x += self.speed_x                                                 # Mover en X
        self.rect.y += self.speed_y                                                 # Mover en Y


class Player1:                      
    def __init__(self):             #Constructor de la clase
        self.width = 60             #Ancho del jugador
        self.height = 130           #Alto del jugador
        self.x_coor = 50            #Coordenada X del jugador
        self.y_coor = 255           #Coordenada Y del jugador
        self.y_speed = 0            #Velocidad en Y del jugador
        self.x_speed = 0            #Velocidad en X del jugador
        self.puntos = 0             #Puntos del jugador
        self.proyectiles = []       #Lista de proyectiles

        # Cargar la imagen del jugador
        self.image = pygame.image.load(os.path.join(current_directory, "Assets/PongRetro/Ryu.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))  #Escalar la imagen
        self.rect = self.image.get_rect()                                           #Obtener el rectangulo de la imagen       
        self.rect.topleft = (self.x_coor, self.y_coor)                              #Centrar el rectangulo en las coordenadas

    def dibujar(self, screen):              
        screen.blit(self.image, self.rect)      #Dibujar el jugador

    def mover(self):
        self.y_coor += self.y_speed             #Mover en Y
        self.x_coor += self.x_speed             #Mover en X
        for proyectil in self.proyectiles:      #Mover los proyectiles
            proyectil.mover()                   # llamado al metodo mover de la clase proyectil
        self.rect.topleft = (self.x_coor, self.y_coor) #Centrar el rectangulo en las coordenadas
        
        #Restringir las posiciones del jugador
        if self.y_coor < 0:
            self.y_coor = 0
        elif self.y_coor > 470:
            self.y_coor = 470
        if self.x_coor < 0:
            self.x_coor = 0
        elif self.x_coor > 350:
            self.x_coor = 350

    def lanzar_proyectil(self):
        proyectil = Proyectil(self.x_coor + self.width // 2, self.y_coor + self.height // 2, 5, 0)
        self.proyectiles.append(proyectil)

    def colision(self, linea):
        if self.y_coor > 510 or self.y_coor < 0:
            self.y_speed *= -1
        if self.x_coor > 385 or self.x_coor < 0:
            self.x_speed *= -1


class Player2:
    def __init__(self):
        self.width = 60
        self.height = 130
        self.x_coor = 735
        self.y_coor = 255
        self.y_speed = 0
        self.x_speed = 0
        self.puntos = 0
        self.proyectiles = []

        # Cargar la imagen del jugador
        self.image = pygame.image.load(os.path.join(current_directory, "Assets/PongRetro/Ken.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x_coor, self.y_coor)

    def dibujar(self, screen):
        screen.blit(self.image, self.rect)

    def mover(self):
        self.y_coor += self.y_speed
        self.x_coor += self.x_speed
        for proyectil in self.proyectiles:
            proyectil.mover()
        self.rect.topleft = (self.x_coor, self.y_coor)

        #Restringir las posiciones del jugador
        if self.y_coor < 0:
            self.y_coor = 0
        elif self.y_coor > 470:
            self.y_coor = 470

        if self.x_coor < 400:
            self.x_coor = 400
        elif self.x_coor > 735:
            self.x_coor = 735

    def lanzar_proyectil(self):
        proyectil = Proyectil(self.x_coor + self.width // 2, self.y_coor + self.height // 2, -5, 0)
        self.proyectiles.append(proyectil)

    def colision(self, linea):
        if self.y_coor > 510 or self.y_coor < 0:
            self.y_speed *= -1
        if self.x_coor > 785 or self.x_coor < 400:
            self.x_speed *= -1

class Pelota:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.speed_x = 4
        self.speed_y = 4
        self.image = pygame.image.load(os.path.join(current_directory, "Assets/PongRetro/Ball.png")).convert_alpha()
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def dibujar(self, screen):
        screen.blit(self.image, self.rect)

    def mover(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.rect.center = (self.x, self.y)

    def movimiento(self):
        if self.y > 590 or self.y < 10:
            self.speed_y *= -1

    def colision(self, player1, player2):
        proyectiles_eliminar = []
        for proj in player1.proyectiles:
            if self.rect.colliderect(proj.rect):
                self.speed_y *= -1  # Invertir la dirección en Y de la pelota
                pygame.mixer.Sound.play(Sonido_Golpe)
                proyectiles_eliminar.append(proj)
                #Ajustar la posicion del jugador para evitar que se superposiciones
                

        for proj in player2.proyectiles:
            if self.rect.colliderect(proj.rect):
                self.speed_y *= -1  # Invertir la dirección en Y de la pelota
                self.x += self.speed_x
                pygame.mixer.Sound.play(Sonido_Golpe)
                proyectiles_eliminar.append(proj)
        
        #Colision jugador-pelota
        if self.rect.colliderect(player1.rect):
            self.speed_x = abs(self.speed_x)  # Invierte la dirección en X
            self.x = player1.rect.right + self.rect.width // 2  # Alinea con el lado derecho de player1
            pygame.mixer.Sound.play(Sonido_Golpe)

        if self.rect.colliderect(player2.rect):
            self.speed_x = -abs(self.speed_x)  # Invierte la dirección en X
            self.x = player2.rect.left - self.rect.width // 2  # Alinea con el lado izquierdo de player2
            pygame.mixer.Sound.play(Sonido_Golpe)

        for proj in proyectiles_eliminar:
            for proj in player1.proyectiles:
                player1.proyectiles.remove(proj)
            for proj in player2.proyectiles:
                player2.proyectiles.remove(proj)
        


def juego_pong():
    puntos1 = 0
    puntos2 = 0
    game_over = False
    Winner = None
    Puntaje_Ganador= 5
    pelota = Pelota()
    player1 = Player1()
    player2 = Player2()
    fuente = pygame.font.SysFont("Arial", 60)
    pygame.mixer.music.play(-1)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()

        if puntos1 >= Puntaje_Ganador:
            game_over = True
            Winner = "Player 1"
            pygame.mixer.music.stop()
        elif puntos2 >= Puntaje_Ganador:
            game_over = True
            Winner = "Player 2"
            pygame.mixer.music.stop()

        

        # Mover player1
        if keys[pygame.K_w]:
            player1.y_speed = -3
        elif keys[pygame.K_s]:
            player1.y_speed = 3
        else:
            player1.y_speed = 0

        if keys[pygame.K_a]:
            player1.x_speed = -3
        elif keys[pygame.K_d]:
            player1.x_speed = 3
        else:
            player1.x_speed = 0

        if keys[pygame.K_SPACE]:
            player1.lanzar_proyectil()

        # Mover player2
        if keys[pygame.K_UP]:
            player2.y_speed = -3
        elif keys[pygame.K_DOWN]:
            player2.y_speed = 3
        else:
            player2.y_speed = 0

        if keys[pygame.K_LEFT]:
            player2.x_speed = -3
        elif keys[pygame.K_RIGHT]:
            player2.x_speed = 3
        else:
            player2.x_speed = 0

        if keys[pygame.K_l]:
            player2.lanzar_proyectil()

        if pelota.x > 800:
            pelota.x = 400
            pelota.y = 300
            pelota.speed_x *= -1
            pelota.speed_y *= -1
            puntos1 += 1
            pygame.mixer.Sound.play(gol)

        if pelota.x < 0:
            pelota.x = 400
            pelota.y = 300
            pelota.speed_x *= -1
            pelota.speed_y *= -1
            puntos2 += 1
            pygame.mixer.Sound.play(gol)


        

        player1.mover()
        player2.mover()
        pelota.mover()
        pelota.movimiento()
        pelota.colision(player1, player2)
        screen.fill(black)
        screen.blit(PongRetro_Background, (0, 0))
        linea = pygame.draw.line(screen, white, (400, 0), (400, 600), 5)
        player1.dibujar(screen)
        player2.dibujar(screen)
        pelota.dibujar(screen)
        for proj in player1.proyectiles:
            proj.dibujar(screen)
        for proj in player2.proyectiles:
            proj.dibujar(screen)
        player1.colision(linea)
        player2.colision(linea)
        Texto1 = fuente.render(str(puntos1), False, white)
        Texto2 = fuente.render(str(puntos2), False, white)
        screen.blit(Texto1, (350, 10))
        screen.blit(Texto2, (450, 10))
        pygame.display.update()
        clock.tick(60)

    if game_over == True:
        if Winner:
            if Winner == "Player 1":
                screen.fill(black)
                screen.blit(WinnerRyu, (0, 0))
            if Winner == "Player 2":
                screen.fill(black)
                screen.blit(WinnerKen, (0, 0))    
            pygame.display.update()
        
    
