import pygame
import sys
import os
from pygame.locals import *
from Robot import Robot

pygame.init()
#Prueba
#Crear la ventana
screen = pygame.display.set_mode((800,600))

#Direccion de la ruta
current_directory = os.path.dirname(__file__)

#Backgrounds
Menu_Background = os.path.join(current_directory,"Assets/Background/Menu_Background.png")
Menu_Background = pygame.image.load(Menu_Background).convert_alpha()
#Buttons
Button_Robot_OFF = os.path.join(current_directory,"Assets/Buttons/Button_Robot_OFF.png")
Button_Robot_OFF = pygame.image.load(Button_Robot_OFF).convert_alpha()
Button_Robot_ON  = os.path.join(current_directory,"Assets/Buttons/Button_Robot_ON.png")
Button_Robot_ON  = pygame.image.load(Button_Robot_ON).convert_alpha()

Button_PongClassic_OFF = os.path.join(current_directory,"Assets/Buttons/Button_PongClassic_OFF.png")
Button_PongClassic_OFF = pygame.image.load(Button_PongClassic_OFF).convert_alpha()
Button_PongClassic_ON  = os.path.join(current_directory,"Assets/Buttons/Button_PongClassic_ON.png")
Button_PongClassic_ON  = pygame.image.load(Button_PongClassic_ON).convert_alpha()

Button_PongRetro_OFF = os.path.join(current_directory,"Assets/Buttons/Button_PongRetro_OFF.png")
Button_PongRetro_OFF = pygame.image.load(Button_PongRetro_OFF).convert_alpha()
Button_PongRetro_ON  = os.path.join(current_directory,"Assets/Buttons/Button_PongRetro_ON.png")
Button_PongRetro_ON  = pygame.image.load(Button_PongRetro_ON).convert_alpha()

Button_Triki_OFF = os.path.join(current_directory,"Assets/Buttons/Button_Triki_OFF.png")
Button_Triki_OFF = pygame.image.load(Button_Triki_OFF).convert_alpha()
Button_Triki_ON  = os.path.join(current_directory,"Assets/Buttons/Button_Triki_ON.png")
Button_Triki_ON  = pygame.image.load(Button_Triki_ON).convert_alpha()

Button_Termo_OFF = os.path.join(current_directory,"Assets/Buttons/Button_Termo_OFF.png")
Button_Termo_OFF = pygame.image.load(Button_Termo_OFF).convert_alpha()
Button_Termo_ON  = os.path.join(current_directory,"Assets/Buttons/Button_Termo_ON.png")
Button_Termo_ON  = pygame.image.load(Button_Termo_ON).convert_alpha()

Button_Exit_OFF = os.path.join(current_directory,"Assets/Buttons/Button_Exit_OFF.png")
Button_Exit_OFF = pygame.image.load(Button_Exit_OFF).convert_alpha()
Button_Exit_ON  = os.path.join(current_directory,"Assets/Buttons/Button_Exit_ON.png")
Button_Exit_ON  = pygame.image.load(Button_Exit_ON).convert_alpha()


class Menu:
    def __init__(self, screen, options):
        self.screen = screen
        self.options = options
        self.selected_option = 0
        self.font = pygame.font.Font(None, 36)
        self.buttons = [
            {"image": Button_Robot_OFF, "rect": pygame.Rect(225, 170, 150, 50), "game": "Robot"},
            {"image": Button_PongClassic_OFF, "rect": pygame.Rect(425, 170, 150, 50), "game": "Pong"},
            {"image": Button_PongRetro_OFF, "rect": pygame.Rect(225, 240, 150, 50), "game": "Pong Retro"},
            {"image": Button_Triki_OFF, "rect": pygame.Rect(425, 240, 150, 50), "game": "Triki"},
            {"image": Button_Termo_OFF, "rect": pygame.Rect(225, 310, 150, 50), "game": "Imagen Termográfica"},
            {"image": Button_Exit_OFF, "rect": pygame.Rect(425, 310, 150, 50), "game": "Exit"}
        ]
        self.Robot_Instance = Robot()


    def draw_menu(self):
        self.screen.blit(Menu_Background, (0, 0))
        for button in self.buttons:
            self.screen.blit(button["image"], button["rect"])
    
    def draw_robot(self):
        self.Robot_Instance.Run_Robot()
        pygame.display.update()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for button in self.buttons:
                        if button["rect"].collidepoint(mouse_pos):
                            selected_game = button["game"]
                            return selected_game

                self.draw_menu()

                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = event.pos
                    if 225 <= mouse_pos[0] <= 375 and 170 <= mouse_pos[1] <= 220:
                        self.screen.blit(Button_Robot_ON, (225, 170))
                    if 425 <= mouse_pos[0] <= 575 and 170 <= mouse_pos[1] <= 220:
                        self.screen.blit(Button_PongClassic_ON, (425, 170))
                    if 225 <= mouse_pos[0] <= 375 and 240 <= mouse_pos[1] <= 290:
                        self.screen.blit(Button_PongRetro_ON, (225, 240))
                    if 425 <= mouse_pos[0] <= 575 and 240 <= mouse_pos[1] <= 290:
                        self.screen.blit(Button_Triki_ON, (425, 240))
                    if 225 <= mouse_pos[0] <= 375 and 310 <= mouse_pos[1] <= 360:
                        self.screen.blit(Button_Termo_ON, (225, 310))
                    if 425 <= mouse_pos[0] <= 575 and 310 <= mouse_pos[1] <= 360:
                        self.screen.blit(Button_Exit_ON, (425, 310))
                
            pygame.display.update()

if __name__ == "__main__":
    options = ["Triki", "Pong", "Pong Retro", "Robot", "Imagen Termográfica","Exit"]

    menu = Menu(screen, options)
    while True:    
        selected_game = menu.run()
        if selected_game == "Robot":
            menu.draw_robot()
            pygame.display.update()
            pygame.time.delay(2000)

        #Pong clasixco
        if selected_game == "Pong":
            import Pong_clases
            Pong_clases.juego_pong()
        #Super pong
        if selected_game == "Pong Retro":
            import SuperPong_clases
            SuperPong_clases.juego_pong()
        #Exit
        if selected_game == "Exit":
            pygame.quit()
            sys.exit()

    
