import cv2
import numpy as np

class ArucoMarkerDetector:
    def __init__(self, camera_index=0):
        # Carga el diccionario de marcadores ArUco
        self.dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)
        self.parameters = cv2.aruco.DetectorParameters()
        self.detector = cv2.aruco.ArucoDetector(self.dictionary, self.parameters)

        # Configura la cámara
        self.cap = cv2.VideoCapture(camera_index)

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

        return frame

    def start_detection(self):
        while True:
            frame = self.process_frame()
            if frame is None:
                break

            # Muestra la imagen con los marcadores detectados y el cubo
            cv2.imshow('Aruco Color Detection', frame)

            # Salir con 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

# Si el script se ejecuta directamente
if __name__ == "__main__":
    detector = ArucoMarkerDetector()
    detector.start_detection()