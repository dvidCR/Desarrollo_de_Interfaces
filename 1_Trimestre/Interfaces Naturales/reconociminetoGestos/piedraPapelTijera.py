# Este ejercicio lo hice en grupo con Dario

import cv2
import mediapipe as mp
import pygame
import sys
import random
import time

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Piedra, Papel o Tijera")

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1,
                       min_detection_confidence=0.5, min_tracking_confidence=0.5)

def detectar_gesto(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

    if (thumb_tip.y < index_finger_tip.y and 
        thumb_tip.y < middle_finger_tip.y and 
        pinky_tip.y < middle_finger_tip.y):
        return "Piedra"
    
    elif (thumb_tip.y > index_finger_tip.y and
          pinky_tip.y > index_finger_tip.y):
        return "Tijeras"
    
    elif (index_finger_tip.y < thumb_tip.y and
          middle_finger_tip.y < thumb_tip.y and
          pinky_tip.y > middle_finger_tip.y):
        return "Papel"
    
    return "Desconocido"

gesto_jugador = None
gesto_computadora = None
resultado = ""
countdown_active = False
countdown_start_time = 0

def determinar_ganador(gesto_jugador, gesto_computadora):
    if gesto_jugador == gesto_computadora:
        return "Empate"
    elif (gesto_jugador == "Piedra" and gesto_computadora == "Tijeras") or \
         (gesto_jugador == "Papel" and gesto_computadora == "Piedra") or \
         (gesto_jugador == "Tijeras" and gesto_computadora == "Papel"):
        return "Ganaste"
    else:
        return "Perdiste"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cap.release()
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            countdown_active = True
            countdown_start_time = time.time()

    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            gesto_jugador = detectar_gesto(hand_landmarks)

    screen.fill((255, 255, 255))

    font = pygame.font.Font(None, 36)

    text_jugador = font.render(f"Jugador: {gesto_jugador}", True, (0, 0, 0))
    screen.blit(text_jugador, (50, 50))

    if countdown_active:
        elapsed_time = time.time() - countdown_start_time
        countdown_time = 3 - int(elapsed_time)

        if countdown_time > 0:
            countdown_text = font.render(f"Cuenta regresiva: {countdown_time}", True, (255, 0, 0))
            screen.blit(countdown_text, (50, 200))
        else:
            opciones = ["Piedra", "Papel", "Tijeras"]
            gesto_computadora = random.choice(opciones)

            resultado = determinar_ganador(gesto_jugador, gesto_computadora)
            countdown_active = False

    text_computadora = font.render(f"Computadora: {gesto_computadora}", True, (0, 0, 0))
    text_resultado = font.render(f"Resultado: {resultado}", True, (0, 0, 255))

    screen.blit(text_computadora, (50, 100))
    screen.blit(text_resultado, (50, 150))

    pygame.display.flip()

    cv2.imshow("Camera Feed", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
pygame.quit()