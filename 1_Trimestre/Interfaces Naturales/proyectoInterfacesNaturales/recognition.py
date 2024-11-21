import cv2
import pyautogui
import mediapipe as mp

def is_aligned(points, tolerance=0.07):
    y_values = [point.y for point in points]
    return max(y_values) - min(y_values) < tolerance

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1,
                       min_detection_confidence=0.5, min_tracking_confidence=0.5)

mp_drawing = mp.solutions.drawing_utils

while True:
    ret, frame = cap.read()
    if not ret:
        break

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            index_finger_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
            thumb_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
            
            # thumb_ip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y
            # index_finger_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y
            # middle_finger_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
            # ring_finger_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y
            # pinky_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y

            if is_aligned([hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP],
                           hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP],
                           hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP],
                           hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP],
                           hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP]]):
                hand_gesture = 'saludo_militar'
            elif index_finger_y < thumb_y:
                hand_gesture = 'pointing up'
            else:
                hand_gesture = 'other'

            if hand_gesture == 'pointing up':
                print("pointing up")
                # pyautogui.press('volumeup')
            elif hand_gesture == 'pointing down':
                print("pointing down")
                # pyautogui.press('volumedown')
            elif hand_gesture == 'saludo_militar':
                print("Saludo militar")

    cv2.imshow('Hand Gesture', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()