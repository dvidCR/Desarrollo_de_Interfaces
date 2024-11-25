import pygame
import cv2
import numpy as np

class ArucoChangeColor:
    def __init__(self, screen, width, height, ballColor):
        self.width = width
        self.height = height
        self.screen = screen
        self.ballColor = ballColor
        
        # Carga el diccionario de marcadores ArUco
        self.dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)
        self.parameters = cv2.aruco.DetectorParameters()

        # Configura la cámara
        self.cap = cv2.VideoCapture(0)

        # Dimensiones de la cámara
        self.frame_width = int(self.cap.get(3))
        self.frame_height = int(self.cap.get(4))

        # Matrices de la cámara y coeficientes de distorsión (ajustados para un uso real)
        self.camera_matrix = np.array([[self.frame_width, 0, self.frame_width / 2],
                                       [0, self.frame_height, self.frame_height / 2],
                                       [0, 0, 1]], dtype="double")
        self.dist_coeffs = np.zeros((4, 1))  # Asumiendo sin distorsión

        # Asociar colores a los IDs de los marcadores
        self.marker_colors = {
            1: (255, 0, 0),      # Rojo
            2: (0, 255, 0),      # Verde
            3: (0, 0, 255),      # Azul
            4: (255, 255, 0),    # Amarillo
            5: (0, 255, 255),    # Cian
            6: (255, 0, 255),    # Magenta
        }

    def draw_cube(self, img, corners, imgpts):
        imgpts = np.int32(imgpts).reshape(-1, 2)
        
        # Conecta las líneas para crear el cubo
        img = cv2.drawContours(img, [imgpts[:4]], -1, (0, 255, 0), 3)
        for i, j in zip(range(4), range(4, 8)):
            img = cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]), (255), 3)
        img = cv2.drawContours(img, [imgpts[4:]], -1, (0, 0, 255), 3)
        return img
    
    def process_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None  # Retorna None si no se obtiene un frame válido

        # Convierte la imagen a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detecta los marcadores ArUco
        corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, self.dictionary, parameters=self.parameters)

        # Si se detectan marcadores
        if np.all(ids is not None):
            for i, corner in enumerate(corners):
                marker_id = ids[i][0]  # Obtén el ID del marcador
                
                # Asocia un color al marcador
                color = self.marker_colors.get(marker_id, (255, 255, 255))  # Color predeterminado: blanco

                # Estima la pose del marcador
                rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(corner, 5, self.camera_matrix, self.dist_coeffs)
                (rvec - tvec).any()  # Evita un bug en OpenCV
                
                # Dibuja el marcador en la imagen
                cv2.aruco.drawDetectedMarkers(frame, corners)

                # Calcula la proyección de los puntos del cubo
                axis = np.float32([[0, 0, 0], [0, 5, 0], [5, 5, 0], [5, 0, 0],
                                   [0, 0, -5], [0, 5, -5], [5, 5, -5], [5, 0, -5]])  # Definir un cubo de 5x5x5 cm
                imgpts, _ = cv2.projectPoints(axis, rvec, tvec, self.camera_matrix, self.dist_coeffs)
                frame = self.draw_cube(frame, corner, imgpts)

                # Escribir el color del marcador en la imagen
                cv2.putText(frame, f"Color: {color}", tuple(corner[0][0].astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)

                # Detectar un marcador específico y abrir la ventana de Pygame
                if marker_id >= 1 and marker_id <= 6:  # Aquí puedes cambiar el ID del marcador que abrirá la ventana
                    print(f"Detected marker with ID: {marker_id}")
                    if self.run_pygame_window(color):
                        self.ballColor = color
                        return None

        return frame  # Devuelve el frame para mostrarlo en la ventana de OpenCV

    def run_pygame_window(self, color):
        pygame.init()

        # Crear ventana de Pygame
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Cambiar color")
        running = True

        # Definir fuente para el texto
        font = pygame.font.Font(None, 36)

        # Definir botones
        button_width = 150
        button_height = 50
        button_y_offset = 350  # Espacio para los botones debajo de la bola
        button_gap = 20  # Espacio entre los botones
        yes_button = pygame.Rect((self.width // 2) - button_width - button_gap, button_y_offset, button_width, button_height)
        no_button = pygame.Rect((self.width // 2) + button_gap, button_y_offset, button_width, button_height)

        # Colores personalizados para los botones
        GRAY = (200, 200, 200)  # Gris claro
        DARK_GREY = (100, 100, 100)  # Gris oscuro
        WHITE = (255, 255, 255)  # Blanco para el texto

        # Bucle de Pygame
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if yes_button.collidepoint(event.pos):
                        print("Color cambiado")
                        return True
                    elif no_button.collidepoint(event.pos):
                        print("No se cambió el color")
                        return False

            # Fondo blanco para Pygame
            self.screen.fill(WHITE)  

            # Dibujar la bola en el centro con el color recibido del marcador ArUco
            pygame.draw.circle(self.screen, color, (self.width // 2, 150), 100)  # Círculo en el centro

            # Dibujar el texto centrado debajo de la bola
            text = font.render("¿Quieres cambiar el color de tu bola por este?", True, (0, 0, 0))
            text_rect = text.get_rect(center=(self.width // 2, 250))
            self.screen.blit(text, text_rect)

            # Dibujar los botones 'Sí' y 'No' con bordes
            pygame.draw.rect(self.screen, GRAY, yes_button)
            pygame.draw.rect(self.screen, DARK_GREY, yes_button, 3)  # Borde alrededor del botón
            pygame.draw.rect(self.screen, GRAY, no_button)
            pygame.draw.rect(self.screen, DARK_GREY, no_button, 3)  # Borde alrededor del botón

            # Crear el texto dentro de los botones
            yes_text = font.render("Sí", True, WHITE)
            no_text = font.render("No", True, WHITE)

            # Posicionar el texto dentro de los botones (centrado)
            yes_text_rect = yes_text.get_rect(center=yes_button.center)
            no_text_rect = no_text.get_rect(center=no_button.center)

            # Dibujar el texto en los botones
            self.screen.blit(yes_text, yes_text_rect)
            self.screen.blit(no_text, no_text_rect)

            # Actualizar la pantalla
            pygame.display.flip()

        pygame.quit()
        return False  # Si el usuario cierra la ventana sin elegir, devolvemos False

    def start_detection(self):
        while True:
            frame = self.process_frame()
            if frame is None:
                break

            # Muestra la imagen con los marcadores detectados y el cubo
            cv2.imshow('Aruco Change Color', frame)

            # Salir con 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()
        return self.ballColor