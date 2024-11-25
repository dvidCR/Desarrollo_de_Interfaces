from handRecognition import HandGame
from speachRecognition import VoiceGame
from ra_changeColor import ArucoChangeColor
import pygame
import sys

class MainMenu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

        # Inicializamos el reloj para controlar la velocidad de refresco
        self.clock = pygame.time.Clock()

        self.WHITE = (255, 255, 255)
        self.GRAY = (200, 200, 200)
        self.DARK_GRAY = (100, 100, 100)
        self.BLACK = (0, 0, 0)
        self.BALL_COLOR = (255, 0, 0)  # Color de la bola (rojo)

        self.font_large = pygame.font.Font(None, 60)
        self.font_small = pygame.font.Font(None, 40)

        self.buttons_text = ["Jugar con la mano", "Jugar con la voz", "Cambiar el color"]
        self.instructions_text = "Instrucciones"

        self.buttons_main = []
        self.button_instructions = None

        self.setup_buttons()

        # Propiedades de la bola
        self.ball_radius = 30  # Radio de la bola
        self.ball_x = self.width // 2  # Posición X centrada
        self.ball_y = 50  # Posición Y en la parte superior

    # Método para dibujar texto centrado en un rectángulo
    def draw_text_centered(self, text, font, color, rect):
        text_surface = font.render(text, True, color)  # Crear la superficie del texto
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    # Método para calcular el tamaño de un botón basado en el texto
    def get_button_rect_centered(self, text, font, center_x, y, padding=20):
        text_surface = font.render(text, True, self.BLACK)  # Crear la superficie del texto
        text_width, text_height = text_surface.get_size()
        x = center_x - (text_width + 2 * padding) // 2
        return pygame.Rect(x, y, text_width + 2 * padding, text_height + 2 * padding)

    # Método para dibujar un botón
    def draw_button(self, rect, text, font, backgrounColor=None, border_color=None):
        backgrounColor = backgrounColor or self.GRAY
        border_color = border_color or self.DARK_GRAY
        pygame.draw.rect(self.screen, backgrounColor, rect)  # Dibujar el botón
        pygame.draw.rect(self.screen, border_color, rect, 3)  # Dibujar el borde
        self.draw_text_centered(text, font, self.BLACK, rect)

    # Método para configurar las posiciones y tamaños de los botones
    def setup_buttons(self):
        button_height = 80
        gap = 20  # Espacio entre botones
        start_y = self.height // 2 - (len(self.buttons_text) * button_height + (len(self.buttons_text) - 1) * gap) // 2

        # Crear los botones para jugar
        for i, text in enumerate(self.buttons_text):
            rect = self.get_button_rect_centered(text, self.font_large, self.width // 2, start_y + i * (button_height + gap))
            self.buttons_main.append((rect, text))

        # Crea el botón de "Instrucciones"
        self.button_instructions = self.get_button_rect_centered(
            self.instructions_text,
            self.font_small,
            self.width // 2,
            start_y + len(self.buttons_text) * (button_height + gap * 2)
        )

    # Método para dibujar la bola
    def draw_ball(self):
        pygame.draw.circle(self.screen, self.BALL_COLOR, (self.ball_x, self.ball_y + 30), self.ball_radius)

    # Método para dibujar el texto "Tu bola:"
    def draw_ball_text(self):
        text = "Tu bola:"
        text_surface = self.font_small.render(text, True, self.BLACK)  # Crear la superficie del texto
        text_rect = text_surface.get_rect(center=(self.ball_x, self.ball_y - 30))  # Posicionar sobre la bola
        self.screen.blit(text_surface, text_rect)

    def run(self):
        running = True
        while running:
            self.screen.fill(self.WHITE)

            # Dibujar el texto "Tu bola:"
            self.draw_ball_text()

            # Dibujar la bola en la parte superior centrada
            self.draw_ball()

            # Dibujar los botones para jugar
            for rect, text in self.buttons_main:
                self.draw_button(rect, text, self.font_large)

            # Dibujar el botón de instrucciones
            self.draw_button(self.button_instructions, self.instructions_text, self.font_small)

            # Actualiza la pantalla
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for rect, text in self.buttons_main:
                        if rect.collidepoint(event.pos): 
                            if text == "Jugar con la mano":
                                game = HandGame(self.screen, self.width, self.height, self.BALL_COLOR)
                                game.run()
                            elif text == "Jugar con la voz":
                                game = VoiceGame(self.screen, self.width, self.height, self.BALL_COLOR)
                                game.run()
                            elif text == "Cambiar el color":
                                detector = ArucoChangeColor(self.screen, self.width, self.height, self.BALL_COLOR)
                                self.BALL_COLOR = detector.start_detection()
                            

                    if self.button_instructions.collidepoint(event.pos):
                        print("Instrucciones seleccionado.")

            self.clock.tick(60)