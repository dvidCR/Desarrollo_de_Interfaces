import pygame
import speech_recognition as sp
import time
import sys
import random
import threading


class VoiceGame:
    def __init__(self, screen, width, height, ballColor):
        # Configuración básica
        pygame.init()
        self.width = width
        self.height = height
        self.screen = screen
        self.ballColor = ballColor
        pygame.display.set_caption("Juego controlado por voz")
        self.clock = pygame.time.Clock()

        # Colores
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)

        # Bola
        self.ball_pos = [width // 2, height // 2]
        self.ball_radius = 20
        self.speed = 2.5
        self.movement = [0, 0]  # Movimiento en x, y (detener por defecto)

        # Obstáculos
        self.obstacle_width = 50
        self.obstacle_height = 50
        self.obstacle_speed = 2.5
        self.max_obstacles = 5
        self.obstacles = []

        # Puntos
        self.score = 0

        # Reconocimiento de voz
        self.recognizer = sp.Recognizer()
        self.last_command_time = time.time()
        self.voice_active = True  # Variable para controlar si el hilo de voz está activo
        self.voice_thread = threading.Thread(target=self.listen_to_voice_continuously, daemon=True)
        self.voice_thread.start()

    def generate_obstacle(self):
        """Genera un obstáculo en una posición aleatoria."""
        x = self.width + random.randint(50, 200)
        y = random.randint(0, self.height - self.obstacle_height)
        return pygame.Rect(x, y, self.obstacle_width, self.obstacle_height)

    def detect_collision(self):
        """Detecta si la bola colisiona con algún obstáculo."""
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

    def process_voice_command(self, command):
        """Procesa un comando de voz y ajusta el movimiento."""
        command = command.lower()
        if "arriba" in command:
            self.movement = [0, -self.speed]
        elif "abajo" in command:
            self.movement = [0, self.speed]
        elif "izquierda" in command:
            self.movement = [-self.speed, 0]
        elif "derecha" in command:
            self.movement = [self.speed, 0]
        elif "detente" in command:
            self.movement = [0, 0]

    def listen_to_voice_continuously(self):
        """Bucle continuo para escuchar comandos de voz."""
        with sp.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)  # Ajuste inicial para ruido de fondo
            while self.voice_active:  # El hilo continuará solo si la voz está activa
                current_time = time.time()
                if current_time - self.last_command_time > 1.5:  # Escuchar cada 1.5 segundos
                    self.last_command_time = current_time
                    try:
                        print("Escuchando...")
                        audio = self.recognizer.listen(source, timeout=3, phrase_time_limit=2)
                        command = self.recognizer.recognize_google(audio, language="es-ES")
                        print(f"Has dicho: {command}")
                        self.process_voice_command(command)
                    except sp.UnknownValueError:
                        print("No entendí el comando.")
                    except Exception as e:
                        print(f"Error de voz: {e}")
                time.sleep(0.2)

    def game_over_screen(self):
        """Pantalla de Game Over."""
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
            puntuacion_text = pygame.font.Font(None, 40).render(f"Puntuación: {self.score}", True, (255, 255, 255))
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
                        self.stop_voice_recognition()  # Detener el reconocimiento de voz
                        return  # Salir al menú principal u otra sección
                    elif button_salir.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

    def stop_voice_recognition(self):
        """Detener el reconocimiento de voz."""
        self.voice_active = False  # Cambiar el flag para detener el hilo
        print("Reconocimiento de voz detenido.")

    def run(self):
        """Bucle principal del juego."""
        self.score = 0
        self.ball_pos = [self.width // 2, self.height // 2]
        self.obstacles.clear()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

            # Mover la bola
            self.ball_pos[0] += self.movement[0]
            self.ball_pos[1] += self.movement[1]

            # Restringir los movimientos dentro de la pantalla
            self.ball_pos[0] = max(self.ball_radius, min(self.width - self.ball_radius, self.ball_pos[0]))
            self.ball_pos[1] = max(self.ball_radius, min(self.height - self.ball_radius, self.ball_pos[1]))

            # Generar obstáculos
            if len(self.obstacles) < self.max_obstacles and random.random() < 0.1:
                self.obstacles.append(self.generate_obstacle())

            # Mover obstáculos
            for obs in self.obstacles:
                obs.x -= self.obstacle_speed
            self.obstacles = [obs for obs in self.obstacles if obs.x + self.obstacle_width > 0]

            # Detectar colisiones
            if self.detect_collision():
                self.game_over_screen()
                return

            # Incrementar puntuación
            self.score += 1

            # Dibujar la pantalla
            self.screen.fill(self.WHITE)
            pygame.draw.circle(self.screen, self.ballColor, self.ball_pos, self.ball_radius)
            for obs in self.obstacles:
                pygame.draw.rect(self.screen, self.RED, obs)

            # Mostrar la puntuación
            font = pygame.font.Font(None, 36)
            score_text = font.render(f"Puntos: {self.score}", True, (0, 0, 0))
            self.screen.blit(score_text, (10, 10))

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()
        sys.exit()