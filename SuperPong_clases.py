import pygame
import os

pygame.init()

# colores
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# Get current directory
current_directory = os.path.dirname(__file__)
# Load background image
PongClassic_Background = os.path.join(current_directory, "Assets/Background/PongClassic_Background.png")
PongClassic_Background = pygame.image.load(PongClassic_Background).convert_alpha()
sonido_raqueta = pygame.mixer.Sound("Arcade/Assets/Sound/Raqueta.mp3")
gol = pygame.mixer.Sound("Arcade/Assets/Sound/Gol.mp3")


class Proyectil:
    def __init__(self, x_coor, y_coor, speed_x, speed_y, radio):
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.radio = radio
        self.rect = pygame.Rect(self.x_coor - self.radio, self.y_coor - self.radio, 2 * self.radio, 2 * self.radio)

    def dibujar(self, screen):
        pygame.draw.circle(screen, white, [self.x_coor, self.y_coor], self.radio)
        self.rect = pygame.Rect(self.x_coor - self.radio, self.y_coor - self.radio, 2 * self.radio, 2 * self.radio)

    def mover(self):
        self.x_coor += self.speed_x
        self.y_coor += self.speed_y


class Player1:
    def __init__(self):
        self.width = 15
        self.height = 90
        self.x_coor = 50
        self.y_coor = 255
        self.y_speed = 0
        self.x_speed = 0
        self.puntos = 0
        self.proyectiles = []

    def dibujar(self, screen):
        pygame.draw.rect(screen, white, [self.x_coor, self.y_coor, self.width, self.height])

    def mover(self):
        self.y_coor += self.y_speed
        self.x_coor += self.x_speed
        for proyectil in self.proyectiles:
            proyectil.mover()

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
            if event.key == pygame.K_SPACE:  # Cambiar la tecla de disparo
                self.lanzar_proyectil()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.y_speed = 0
            if event.key == pygame.K_s:
                self.y_speed = 0
            if event.key == pygame.K_a:
                self.x_speed = 0
            if event.key == pygame.K_d:
                self.x_speed = 0

    def lanzar_proyectil(self):
        proyectil = Proyectil(self.x_coor + self.width // 2, self.y_coor + self.height // 2, 5, 0, 5)
        self.proyectiles.append(proyectil)

    def colision(self, linea):
        if self.y_coor > 510 or self.y_coor < 0:
            self.y_speed *= -1
        if self.x_coor > 385 or self.x_coor < 0:
            self.x_speed *= -1


class Player2:
    def __init__(self):
        self.width = 15
        self.height = 90
        self.x_coor = 735
        self.y_coor = 255
        self.y_speed = 0
        self.x_speed = 0
        self.puntos = 0
        self.proyectiles = []

    def dibujar(self, screen):
        pygame.draw.rect(screen, white, [self.x_coor, self.y_coor, self.width, self.height])

    def mover(self):
        self.y_coor += self.y_speed
        self.x_coor += self.x_speed
        for proyectil in self.proyectiles:
            proyectil.mover()

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
            if event.key == pygame.K_l:
                self.lanzar_proyectil()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.y_speed = 0
            if event.key == pygame.K_DOWN:
                self.y_speed = 0
            if event.key == pygame.K_LEFT:
                self.x_speed = 0
            if event.key == pygame.K_RIGHT:
                self.x_speed = 0

    def lanzar_proyectil(self):
        proyectil = Proyectil(self.x_coor + self.width // 2, self.y_coor + self.height // 2, -5, 0, 5)
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

    def colision(self, player1, player2, proyectil):
        if self.x < player1.x_coor + player1.width and player1.y_coor < self.y < player1.y_coor + player1.height:
            self.speed_x *= -1
            pygame.mixer.Sound.play(sonido_raqueta)
            if len(player1.proyectiles) > 0:
                proyectil = player1.proyectiles[0]
                proyectil.speed_y = self.speed_y

        if self.x > player2.x_coor and player2.y_coor < self.y < player2.y_coor + player2.height:
            self.speed_x *= -1
            pygame.mixer.Sound.play(sonido_raqueta)
            if len(player2.proyectiles) > 0:
                proyectil = player2.proyectiles[0]
                proyectil.speed_y = self.speed_y


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
            player1.movimientos(event)
            player2.movimientos(event)

        if pelota.x > 800:
            pelota.x = 400
            pelota.y = 300
            pelota.speed_x *= -1
            pelota.speed_y *= -1
            puntos1 += 1
            pygame.mixer.Sound.play(gol)

        # Si la pelota sale del lado izquierdo
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
        pelota.colision(player1, player2, Proyectil)  # Pasamos el objeto proyectil al método colision
        screen.fill(black)
        screen.blit(PongClassic_Background, (0, 0))
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


if __name__ == "__main__":
    juego_pong()
