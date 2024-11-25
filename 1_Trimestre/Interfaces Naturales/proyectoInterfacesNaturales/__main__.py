from menu import MainMenu
import pygame

if __name__ == "__main__":
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Menú Principal")

    menu = MainMenu(screen, WIDTH, HEIGHT)
    menu.run()