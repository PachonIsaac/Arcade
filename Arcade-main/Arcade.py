import pygame
import sys
import os

class Ventana:
    def __init__(self, screen):
        self.screen = screen
        self.state = "MENU"

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.state == "MENU":
                    if event.type == pygame.MOUSEMOTION:
                        mouse_pos = event.pos
                        if 325 <= mouse_pos[0] <= 475 and 540 <= mouse_pos[1] <= 590:
                            screen.blit(Button_Robot_ON, (325, 540))
                        else:
                            screen.blit(Button_Robot_OFF, (325, 540))

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos
                        if 325 <= mouse_pos[0] <= 475 and 540 <= mouse_pos[1] <= 590:
                            self.state = "GAME_1"

                # Agrega lógica para otros estados y eventos aquí

                elif self.state == "GAME_1":
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.state = "MENU"

            self.render()

    def render(self):
        self.screen.fill((0, 0, 0))  # Fondo negro

        if self.state == "MENU":
            screen.blit(Menu_Background, (0, 0))
            pass
        elif self.state == "GAME_1":
            # Llama a la función que ejecuta el juego 1 (por ejemplo, run_game_1())
            pass
        # Agrega lógica para otros estados aquí

        pygame.display.flip()

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
Screen_Size = (800, 600)

# Crear la pantalla
screen = pygame.display.set_mode(Screen_Size)
pygame.display.set_caption("Arcade")

#Direccion de la ruta
current_directory = os.path.dirname(__file__)

#Cargar las imagenes
#Backgrounds
Menu_Background = os.path.join(current_directory,"Assets/Background/Menu_Background.png")
Menu_Background = pygame.image.load(Menu_Background).convert_alpha

#Buttons
Button_Robot_OFF = os.path.join(current_directory,"Assets/Buttons/Button_Robot_OFF.png")
Button_Robot_OFF = pygame.image.load(Button_Robot_OFF).convert_alpha
Button_Robot_ON  = os.path.join(current_directory,"Assets/Buttons/Button_Robot_ON.png")
Button_Robot_ON  = pygame.image.load(Button_Robot_ON).convert_alpha

# Crea un objeto "ventana" para gestionar los estados y la lógica
ventana = Ventana(screen)

# Inicia el bucle principal del juego
ventana.run()
