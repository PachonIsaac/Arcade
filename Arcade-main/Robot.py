#Hecho por Jense David Martinez e Isaac Pachon Zuleta


#Import of libraries
import pygame
import sys
import math

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
ORANGE = (255, 165, 0)
LIGHT_GRAY = (220, 220, 220)

class Robot:
    def __init__(self):
            # Initialize Pygame
            pygame.init()


    def Run_Robot(self):
        # Configure the window
        screen_width, screen_height = 800, 600
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Robot")
        screen.fill(WHITE)
        #Sombra
        pygame.draw.ellipse(screen, LIGHT_GRAY, [178, 550, 484, 30], 0)

        #orejas
        #circulo negro de oreja izquierda
        pygame.draw.arc(screen,BLACK,[330,142,48,48],0,180,8)
        pygame.draw.arc(screen,BLACK,[340,152,28,28],0,180,2)

        #antena
        pygame.draw.line(screen,BLACK, [338, 74], [338, 148], 3)
        pygame.draw.arc(screen,BLACK,[328,56,20,20],0,180,3)
        #circulo negro de oreja derecha
        pygame.draw.arc(screen,BLACK,[453,142,48,48],0,180,8)
        pygame.draw.arc(screen,BLACK,[463,152,28,28],0,180,2)

        #corona
        pygame.draw.arc(screen,BLACK,[375,68,75,70],0,180,5)
        pygame.draw.arc(screen,BLACK,[385,78,55,55],0,180,5)
        #lineas
        pygame.draw.line(screen,BLACK, [380, 88], [387, 93], 4)
        pygame.draw.line(screen,BLACK, [386, 82], [392, 85], 4)
        pygame.draw.line(screen,BLACK, [406, 71], [406, 79], 4)
        pygame.draw.line(screen,BLACK, [414, 71], [414, 79], 4)
        pygame.draw.line(screen,BLACK, [437, 80], [430, 86], 4)
        pygame.draw.line(screen,BLACK, [435, 91], [440, 89], 4)

        # Cabeza del robot
        #cuadro principal negro
        pygame.draw.rect(screen, BLACK, [350, 120, 130, 100], 0)
        #circulo de la izquierda arriba de la cabeza
        pygame.draw.circle(screen, BLACK, (370, 120), 20)
        #circulo de la derecha arriba de la cabeza
        pygame.draw.circle(screen, BLACK, (460, 120), 20)
        #cuadro de arriba de la cabeza
        pygame.draw.rect(screen, BLACK, [365, 100, 90, 70], 0)
        #circulo de la izquierda de abajo de la cabeza
        pygame.draw.circle(screen, BLACK, (370, 220), 20)
        #circulo de la derecha de abajo de la cabeza
        pygame.draw.circle(screen, BLACK, (460, 220), 20)
        #cuadro de abajo de la cabeza
        pygame.draw.rect(screen, BLACK, [365, 170, 90, 70], 0)

        #cuadro secundario 
        pygame.draw.rect(screen, GRAY, [355, 120, 120, 100], 0)
        #circulo de la izquierda arriba de la cabeza
        pygame.draw.circle(screen, GRAY, (375, 125), 20)
        #circulo de la derecha arriba de la cabeza
        pygame.draw.circle(screen, GRAY, (455, 125), 20)
        #cuadro de arriba de la cabeza
        pygame.draw.rect(screen, GRAY, [365, 106, 90, 70], 0)
        #circulo de la izquierda de abajo de la cabeza
        pygame.draw.circle(screen, GRAY, (375, 215), 20)
        #circulo de la derecha de abajo de la cabeza
        pygame.draw.circle(screen, GRAY, (455, 215), 20)
        #cuadro de abajo de la cabeza
        pygame.draw.rect(screen, GRAY, [365, 164, 90, 70], 0)

        #ojos 
        #ojo izquierdo
        pygame.draw.circle(screen, BLACK, (390, 160), 24)
        #circulo gris
        pygame.draw.circle(screen, GRAY, (390, 160), 18)
        #circulo negro
        pygame.draw.circle(screen, BLACK, (390, 160), 16)
        #circulo naranja
        pygame.draw.circle(screen, RED, (390, 160), 14)

        #ojo derecho
        pygame.draw.circle(screen, BLACK, (442, 160), 20)
        #circulo gris
        pygame.draw.circle(screen, GRAY, (442, 160), 14)
        #circulo negro
        pygame.draw.circle(screen, BLACK, (442, 160), 12)
        #circulo naranja
        pygame.draw.circle(screen, RED, (442, 160), 10)

        #boca
        pygame.draw.circle(screen, BLACK, (384, 209), 10)
        pygame.draw.circle(screen, BLACK, (445, 209), 10)
        pygame.draw.rect(screen, BLACK, [384, 199, 58, 20], 0)

        pygame.draw.circle(screen, WHITE, (386, 209), 6)
        pygame.draw.circle(screen, WHITE, (442, 209), 6)
        pygame.draw.rect(screen, WHITE, [386, 203, 56, 12], 0)

        #dientes
        pygame.draw.line(screen,BLACK, [387, 201], [387, 215], 4)
        pygame.draw.line(screen,BLACK, [397, 201], [397, 215], 4)
        pygame.draw.line(screen,BLACK, [407, 201], [407, 215], 4)
        pygame.draw.line(screen,BLACK, [417, 201], [417, 215], 4)
        pygame.draw.line(screen,BLACK, [427, 201], [427, 215], 4)
        pygame.draw.line(screen,BLACK, [437, 201], [437, 215], 4)

        # cuello
        pygame.draw.rect(screen, BLACK, [425, 235, 8, 15], 0)
        pygame.draw.rect(screen, BLACK, [400, 235, 8, 15], 0)

        #brazos

        #brazo derecho
        pygame.draw.arc(screen, BLACK, [415, 105, 160, 170], math.radians(270), math.radians(370),5)
        pygame.draw.arc(screen, BLACK, [415, 135, 175, 170], math.radians(270), math.radians(380),5)

        pygame.draw.circle(screen, BLACK, (578, 192), 23)
        pygame.draw.polygon(screen, BLACK, [[557, 180],[ 545, 171], [545, 142],[563,138],[566,173]], 0)
        pygame.draw.polygon(screen, GRAY, [[547, 145],[ 559, 142], [561, 169],[562, 177],[549,168]], 0)
        pygame.draw.polygon(screen, BLACK, [[590, 172],[ 595, 171], [598, 142],[619,141],[618,174],[599,184]], 0)
        pygame.draw.polygon(screen, GRAY, [[591, 175],[ 598, 172], [601, 144],[614,145],[615,168],[597,178]], 0)
        pygame.draw.circle(screen, WHITE, (578, 192), 18)

        pygame.draw.arc(screen, BLACK, [563, 177, 30, 30], 0, 180,2)
        pygame.draw.circle(screen, BLACK, (578, 192), 5)

        #brazo izquierdo
        pygame.draw.arc(screen, BLACK, [230, 270, 160, 170], math.radians(80), math.radians(170),5)
        pygame.draw.arc(screen, BLACK, [230, 305, 175, 170], math.radians(80), math.radians(170),5)

        pygame.draw.circle(screen, BLACK, (230, 360), 23)
        pygame.draw.polygon(screen, BLACK, [[247, 373],[255, 380], [256, 410],[236,413],[236,378]], 0)
        pygame.draw.polygon(screen, GRAY, [[239, 380],[239, 408], [251, 405],[250,383],[244,375],], 0)
        pygame.draw.polygon(screen, BLACK, [[212, 373],[208, 373], [206, 407],[182,401],[188,371],[207,362]], 0)
        pygame.draw.polygon(screen, GRAY, [[208, 364],[193, 373], [187, 397],[202,400],[203,370],[210,369]], 0)

        pygame.draw.circle(screen, WHITE, (230, 360), 18)

        pygame.draw.arc(screen, BLACK, [215, 346, 30, 30], 0, 180,2)
        pygame.draw.circle(screen, BLACK, (230, 360), 5)
        
        #circulo negro del brazo izquierdo
        pygame.draw.circle(screen, BLACK, (337, 290), 25)
        #circulo gris del brazo izquierdo 
        pygame.draw.circle(screen, GRAY, (339, 290), 20)
        #circulo negro del brazo derecho
        pygame.draw.circle(screen, BLACK, (490, 290), 25)
        #circulo gris del brazo derecho 
        pygame.draw.circle(screen, GRAY, (488, 290), 20)

        #circulo negro de la pierna izquierda
        pygame.draw.circle(screen, BLACK, (374, 410), 25)
        #circulo gris de la pierna izquierda
        pygame.draw.circle(screen, GRAY, (373, 410), 20)
        #circulo negro de la pierna derecha 
        pygame.draw.circle(screen, BLACK, (451, 410), 25)
        #circulo gris de la pierna derecha
        pygame.draw.circle(screen, GRAY, (450, 410), 20)

        # cuerpo
        pygame.draw.rect(screen, BLACK, [335, 270, 157, 120], 0)
        #circulo de la izquierda arriba del cuerpo
        pygame.draw.circle(screen, BLACK, (355, 270), 20)
        #circulo de la derecha arriba del cuerpo
        pygame.draw.circle(screen, BLACK, (472, 270), 20)
        #cuadro de arriba del cuerpo
        pygame.draw.rect(screen, BLACK, [360, 250, 110, 70], 0)
        #circulo de la izquierda de abajo del cuerpo
        pygame.draw.circle(screen, BLACK, (355, 390), 20)
        #circulo de la derecha de abajo del cuerpo
        pygame.draw.circle(screen, BLACK, (472, 390), 20)
        #cuadro de abajo del cuerpo
        pygame.draw.rect(screen, BLACK, [360, 340, 110, 70], 0)

        
        #cuadro secundario
        pygame.draw.rect(screen, GRAY, [340, 270, 145, 120], 0)
        #circulo de la izquierda arriba del cuerpo
        pygame.draw.circle(screen, GRAY, (360, 275), 20)
        #circulo de la derecha arriba del cuerpo
        pygame.draw.circle(screen, GRAY, (465, 275), 20)
        #cuadro de arriba del cuerpo
        pygame.draw.rect(screen, GRAY, [360, 256, 110, 70], 0)
        #circulo de la izquierda de abajo del cuerpo
        pygame.draw.circle(screen, GRAY, (360, 385), 20)
        #circulo de la derecha de abajo del cuerpo
        pygame.draw.circle(screen, GRAY, (465, 385), 20)
        #cuadro de abajo del cuerpo
        pygame.draw.rect(screen, GRAY, [360, 344, 110, 60], 0)

        #cuadro terciario negro
        pygame.draw.rect(screen, BLACK, [345, 285, 135, 100], 0)
        #circulo de la izquierda arriba del cuerpo
        pygame.draw.circle(screen, BLACK, (365, 280), 20)
        #circulo de la derecha arriba del cuerpo
        pygame.draw.circle(screen, BLACK, (460, 280), 20)
        #cuadro de arriba del cuerpo
        pygame.draw.rect(screen, BLACK, [360, 260, 100, 70], 0)
        #circulo de la izquierda de abajo del cuerpo
        pygame.draw.circle(screen, BLACK, (365, 380), 20)
        #circulo de la derecha de abajo del cuerpo
        pygame.draw.circle(screen, BLACK, (460, 380), 20)
        #cuadro de abajo del cuerpo
        pygame.draw.rect(screen, BLACK, [360, 344, 107, 56], 0)

        #cuadro cuarto gris
        pygame.draw.rect(screen, GRAY, [348, 288, 129, 85], 0)
        #circulo de la izquierda arriba del cuerpo
        pygame.draw.circle(screen, GRAY, (368, 284), 20)
        #circulo de la derecha arriba del cuerpo
        pygame.draw.circle(screen, GRAY, (457, 284), 20)
        #cuadro de arriba del cuerpo
        pygame.draw.rect(screen, GRAY, [365, 263, 91, 40], 0)
        #circulo de la izquierda de abajo del cuerpo
        pygame.draw.circle(screen, GRAY, (368, 376), 20)
        #circulo de la derecha de abajo del cuerpo
        pygame.draw.circle(screen, GRAY, (457, 376), 20)
        #cuadro de abajo del cuerpo
        pygame.draw.rect(screen, GRAY, [365, 357, 91, 40], 0)

        #cuadro quinto 
        pygame.draw.rect(screen, BLACK, [350, 290, 125, 80], 0)
        #circulo de la izquierda arriba del cuerpo
        pygame.draw.circle(screen, BLACK, (370, 285), 20)
        #circulo de la derecha arriba del cuerpo
        pygame.draw.circle(screen, BLACK, (455, 285), 20)
        #cuadro de arriba del cuerpo
        pygame.draw.rect(screen, BLACK, [365, 265, 86, 35], 0)
        #circulo de la izquierda de abajo del cuerpo
        pygame.draw.circle(screen, BLACK, (370, 375), 20)
        #circulo de la derecha de abajo del cuerpo
        pygame.draw.circle(screen, BLACK, (455, 375), 20)
        #cuadro de abajo del cuerpo
        pygame.draw.rect(screen, BLACK, [365, 360, 86, 35], 0)

        #cuadro sexto gris
        pygame.draw.rect(screen, GRAY, [355, 295, 115, 75], 0)
        #circulo de la izquierda arriba del cuerpo
        pygame.draw.circle(screen, GRAY, (375, 290), 20)
        #circulo de la derecha arriba del cuerpo
        pygame.draw.circle(screen, GRAY, (450, 290), 20)
        #cuadro de arriba del cuerpo
        pygame.draw.rect(screen, GRAY, [368, 270, 80, 30], 0)
        #circulo de la izquierda de abajo del cuerpo
        pygame.draw.circle(screen, GRAY, (375, 370), 20)
        #circulo de la derecha de abajo del cuerpo
        pygame.draw.circle(screen, GRAY, (450, 370), 20)
        #cuadro de abajo del cuerpo
        pygame.draw.rect(screen, GRAY, [368, 360, 81, 30], 0)

        #botones
        pygame.draw.circle(screen, BLACK, (374, 294), 15)
        pygame.draw.circle(screen, BLACK, (450, 294), 15)
        pygame.draw.rect(screen, BLACK, [374, 279, 74, 30], 0)

        #boton naranja
        pygame.draw.circle(screen, ORANGE, (374, 294), 10)
        pygame.draw.circle(screen, ORANGE, (450, 294), 10)
        pygame.draw.rect(screen, ORANGE, [372, 284, 76, 20], 0)

        #boton azul
        pygame.draw.circle(screen, BLACK, (440, 360), 20)
        pygame.draw.circle(screen, BLUE, (440, 360), 15)

        #piernas
        #pierna izquierda
        pygame.draw.arc(screen, BLACK, [314, 410, 160, 220], math.radians(120), math.radians(190),5)
        pygame.draw.arc(screen, BLACK, [346, 410, 175, 230], math.radians(120), math.radians(190),5)

        #pie izquierdo
        pygame.draw.ellipse(screen, BLACK, [280, 530, 80, 60], 0)
        pygame.draw.ellipse(screen, GRAY, [285, 535, 70, 50], 0)
        pygame.draw.line(screen, BLACK, (285, 556), (355,556), 2)
        pygame.draw.rect(screen, BLACK, [280, 564, 80, 30], 0)
        pygame.draw.rect(screen, WHITE, [280, 570, 80, 30], 0)

        #pierna derecha
        pygame.draw.arc(screen, BLACK, [352, 410, 160, 220], math.radians(350), math.radians(60),5)
        pygame.draw.arc(screen, BLACK, [305, 410, 175, 230], math.radians(350), math.radians(60),5)

        #pie derecho
        pygame.draw.ellipse(screen, BLACK, [467, 530, 80, 60], 0)
        pygame.draw.ellipse(screen, GRAY, [473, 535, 70, 50], 0)
        pygame.draw.line(screen, BLACK, (473, 556), (543,556), 2)
        pygame.draw.rect(screen, BLACK, [467, 564, 80, 30], 0)
        pygame.draw.rect(screen, WHITE, [467, 570, 80, 30], 0)

        pygame.display.update()
        pygame.time.delay(3000)
        # pygame.quit()
        # sys.exit()


if __name__ == "__main__":
    Robot = Robot()
    Robot.Run_Robot()
                
