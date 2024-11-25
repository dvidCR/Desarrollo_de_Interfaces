import pygame
import random
import sys
import cv2
import mediapipe as mp

class HandGame:
    def __init__(self, screen, width, height, ballColor):
        # Configuración básica
        self.screen = screen
        self.width = width
        self.height = height
        self.ballColor = ballColor
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Juego de la mano")

        # Mediapipe para la detección de manos
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
        self.cap = cv2.VideoCapture(0)

        # Configuración del juego
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        self.ball_radius = 20
        self.ball_pos = [self.width // 2, self.height // 2]
        self.obstacle_width = 50
        self.obstacle_height = 50
        self.max_obstacles = 50
        self.obstacles = []
        self.game_time = 0
        self.obstacle_speed = 5

    def generate_obstacle(self):
        x = self.width + random.randint(10, 100)
        y = random.randint(0, self.height - self.obstacle_height)
        return pygame.Rect(x, y, self.obstacle_width, self.obstacle_height)

    def detect_collision(self):
        ball_rect = pygame.Rect(
            self.ball_pos[0] - self.ball_radius,
            self.ball_pos[1] - self.ball_radius,
            self.ball_radius * 2,
            self.ball_radius * 2
        )
        for obs in self.obstacles:
            if ball_rect.colliderect(obs):
                return True
        return False

    def game_over_screen(self):
        while True:
            self.screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 90)

            # Texto "GAME OVER"
            text = font.render("GAME OVER", True, self.RED)
            self.screen.blit(
                text,
                (self.width // 2 - text.get_width() // 2, self.height // 2 - text.get_height() // 2 - 100)
            )
            
            # Texto de puntuación
            puntuacion_text = pygame.font.Font(None, 40).render(f"Puntuación: {self.puntiacion}", True, (255, 255, 255))
            self.screen.blit(
                puntuacion_text,
                (self.width // 2 - puntuacion_text.get_width() // 2, self.height // 2 - puntuacion_text.get_height() // 2 - 170)
            )

            # Botón de Reiniciar
            button_reiniciar = pygame.Rect(self.width // 2 - 200, self.height // 2, 400, 50)
            pygame.draw.rect(self.screen, (200, 200, 200), button_reiniciar)
            pygame.draw.rect(self.screen, (100, 100, 100), button_reiniciar, 3)
            reiniciar_text = pygame.font.Font(None, 40).render("Reiniciar", True, (0, 0, 0))
            self.screen.blit(
                reiniciar_text,
                (button_reiniciar.x + (button_reiniciar.width - reiniciar_text.get_width()) // 2,
                button_reiniciar.y + (button_reiniciar.height - reiniciar_text.get_height()) // 2)
            )

            # Botón de Seleccionar otro juego
            button_seleccionar = pygame.Rect(self.width // 2 - 200, self.height // 2 + 70, 400, 50)
            pygame.draw.rect(self.screen, (200, 200, 200), button_seleccionar)
            pygame.draw.rect(self.screen, (100, 100, 100), button_seleccionar, 3)
            seleccionar_text = pygame.font.Font(None, 40).render("Seleccionar otro juego", True, (0, 0, 0))
            self.screen.blit(
                seleccionar_text,
                (button_seleccionar.x + (button_seleccionar.width - seleccionar_text.get_width()) // 2,
                button_seleccionar.y + (button_seleccionar.height - seleccionar_text.get_height()) // 2)
            )

            # Botón de Salir
            button_salir = pygame.Rect(self.width // 2 - 200, self.height // 2 + 140, 400, 50)
            pygame.draw.rect(self.screen, (200, 200, 200), button_salir)
            pygame.draw.rect(self.screen, (100, 100, 100), button_salir, 3)
            salir_text = pygame.font.Font(None, 40).render("Salir", True, (0, 0, 0))
            self.screen.blit(
                salir_text,
                (button_salir.x + (button_salir.width - salir_text.get_width()) // 2,
                button_salir.y + (button_salir.height - salir_text.get_height()) // 2)
            )

            pygame.display.flip()

            # Manejar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_reiniciar.collidepoint(event.pos):
                        self.run()  # Reiniciar el juego
                    elif button_seleccionar.collidepoint(event.pos):
                        self.stop_camera()
                        return # Vuelve al selector de juegos
                    elif button_salir.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                        
    def stop_camera(self):
        """Detener el uso de la cámara."""
        self.cap.release()  # Liberar la cámara
        cv2.destroyAllWindows()  # Cerrar cualquier ventana de OpenCV
        print("Cámara detenida.")

    def run(self):
        # Reiniciar el juego
        self.puntiacion = 0
        self.ball_pos = [self.width // 2, self.height // 2]
        self.obstacles.clear()
        self.game_time = 0
        self.obstacle_speed = 5

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

            # Leer la cámara y detectar la mano
            success, img = self.cap.read()
            if not success:
                break
            img = cv2.flip(img, 1)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = self.hands.process(img_rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Obtener la posición del índice
                    index_finger_tip = hand_landmarks.landmark[8]
                    new_x = int(index_finger_tip.x * self.width)
                    new_y = int(index_finger_tip.y * self.height)
                    self.ball_pos[0] = max(self.ball_radius, min(self.width - self.ball_radius, new_x))
                    self.ball_pos[1] = max(self.ball_radius, min(self.height - self.ball_radius, new_y))

            # Generar y mover obstáculos
            if len(self.obstacles) < self.max_obstacles and random.random() < 0.09:
                self.obstacles.append(self.generate_obstacle())
            self.obstacles = [obs.move(-self.obstacle_speed, 0) for obs in self.obstacles if obs.x + self.obstacle_width > 0]

            # Detectar colisión
            if self.detect_collision():
                self.game_over_screen()
                return
            
            # Sumar puntiacion
            self.puntiacion = self.game_time // 10  # Divido para controlar el aumento de la puntuación


            # Aumentar velocidad con el tiempo
            self.game_time += 1
            if self.game_time % 100 == 0:
                self.obstacle_speed += 1

            # Dibujar la pantalla
            self.screen.fill(self.WHITE)
            pygame.draw.circle(self.screen, self.ballColor, self.ball_pos, self.ball_radius)
            for obs in self.obstacles:
                pygame.draw.rect(self.screen, self.RED, obs)
            
            # Dibuja la puntuacion
            puntuacion_text = pygame.font.Font(None, 40).render(f"Puntuación: {self.puntiacion}", True, (0, 0, 0))
            self.screen.blit(puntuacion_text, (10, 10))

            pygame.display.flip()
            self.clock.tick(60)