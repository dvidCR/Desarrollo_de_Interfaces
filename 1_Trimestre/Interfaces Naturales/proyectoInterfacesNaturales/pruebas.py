import pygame
import random
import sys
import cv2
import mediapipe as mp

# Inicializar Mediapipe y Pygame
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

pygame.init()

# Configuraciones de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de la bola y obstáculos")
clock = pygame.time.Clock()

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Configuración de la bola
ball_radius = 20
ball_pos = [WIDTH // 2, HEIGHT // 2]

# Configuración de los obstáculos
obstacle_width = 50
obstacle_height = 50
max_obstacles = 50  # Máximo número de obstáculos
obstacles = []

# Cámara
cap = cv2.VideoCapture(0)

# Variables del juego
game_time = 0
obstacle_speed = 5

# Función para generar un obstáculo
def generate_obstacle():
    x = WIDTH + random.randint(10, 100)  # Fuera de la pantalla
    y = random.randint(0, HEIGHT - obstacle_height)
    return pygame.Rect(x, y, obstacle_width, obstacle_height)

# Función para detectar colisiones
def detect_collision(ball_pos, ball_radius, obstacles):
    ball_rect = pygame.Rect(ball_pos[0] - ball_radius, ball_pos[1] - ball_radius, ball_radius * 2, ball_radius * 2)
    for obs in obstacles:
        if ball_rect.colliderect(obs):
            return True
    return False

# Pantalla de Game Over con botón de reinicio
def game_over_screen():
    while True:
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 74)
        text = font.render("GAME OVER", True, RED)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2 - 50))
        reiniciar = font.render("Presiona la tecla 'r' para reiniciar", True, RED)
        screen.blit(reiniciar, (WIDTH - reiniciar.get_width(), HEIGHT - reiniciar.get_height() - 50))
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                return  # Reiniciar el juego

# Loop principal del juego
def main():
    global ball_pos, obstacles, game_time, obstacle_speed
    running = True

    # Reiniciar posiciones
    ball_pos = [WIDTH // 2, HEIGHT // 2]
    obstacles.clear()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        # Leer la cámara y procesar la posición de la mano
        success, img = cap.read()
        if not success:
            break
        img = cv2.flip(img, 1)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Obtener el punto del índice (landmark 8)
                index_finger_tip = hand_landmarks.landmark[8]
                new_x = int(index_finger_tip.x * WIDTH)
                new_y = int(index_finger_tip.y * HEIGHT)
                ball_pos[0] = max(ball_radius, min(WIDTH - ball_radius, new_x))
                ball_pos[1] = max(ball_radius, min(HEIGHT - ball_radius, new_y))

        # Generar nuevos obstáculos si es necesario
        if len(obstacles) < max_obstacles and random.random() < 0.05:  # Probabilidad del 5% por frame
            obstacles.append(generate_obstacle())

        # Mover los obstáculos y eliminarlos si están fuera de la pantalla
        obstacles = [obs.move(-obstacle_speed, 0) for obs in obstacles if obs.x + obstacle_width > 0]

        # Detectar colisión
        if detect_collision(ball_pos, ball_radius, obstacles):
            game_over_screen()
            return

        # Aumentar la velocidad de los obstáculos con el tiempo
        game_time += 1
        if game_time % 500 == 0:  # Incrementar cada 500 frames
            obstacle_speed += 1

        # Dibujar la pantalla
        screen.fill(WHITE)
        pygame.draw.circle(screen, BLUE, ball_pos, ball_radius)
        for obs in obstacles:
            pygame.draw.rect(screen, RED, obs)

        pygame.display.flip()
        clock.tick(60)

# Loop infinito para reiniciar el juego
while True:
    main()