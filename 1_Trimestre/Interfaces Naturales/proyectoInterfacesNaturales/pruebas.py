import cv2
import speech_recognition as sr
import pyttsx3
from transformers import pipeline
import os
 
class SistemaDeteccion:
    def __init__(self):
        # Inicializar síntesis de voz
        self.engine = pyttsx3.init()
        # Iniciar reconocimiento por voz
        self.reconocedor = sr.Recognizer()
        # Cargar el modelo de IA
        self.modeloIA = self.cargarModeloIA()
        # Activae la camara
        self.camara = cv2.VideoCapture(0)
        # Dar nombre al archivo que se creara cuando se haga una imagen
        self.nombreImagen = "captura.jpg"
        # El sistema esta completamente iniciado y se inicia
        self.hablar("Sistema iniciado. Di '¿Qué ves?' para analizar la imagen o 'salir' para salir.")
 
    def cargarModeloIA(self):
        """Carga el modelo de IA para detección de objetos."""
        print("Cargando el modelo de detección de objetos...")
        return pipeline("object-detection", model="facebook/detr-resnet-50")
 
    def hablar(self, mensaje):
        """Convierte texto en voz."""
        self.engine.say(mensaje)
        self.engine.runAndWait()
 
    def escucharComando(self):
        """Escucha un comando de voz y lo devuelve como texto."""
        with sr.Microphone() as source:
            print("Escuchando...")
            try:
                audio = self.reconocedor.listen(source)
                comando = self.reconocedor.recognize_google(audio, language="es-ES")
                return comando.lower()
            except sr.UnknownValueError:
                self.hablar("No he podido oirte bien.")
                return None
            except sr.RequestError:
                self.hablar("Error en el servicio de reconocimiento de voz.")
                return None
 
    def analizarImagen(self):
        """Captura una imagen, la analiza y describe los objetos detectados."""
        ret, frame = self.camara.read()
        if not ret:
            self.hablar("No se pudo acceder a la cámara.")
            return
 
        # Guardar la imagen capturada
        cv2.imwrite(self.nombreImagen, frame)
 
        # Usar el modelo de IA para detectar objetos
        try:
            detecciones = self.modeloIA(self.nombreImagen)
            objetos_detectados = [
                (obj["label"], int(obj["score"] * 100)) for obj in detecciones if obj["score"] > 0.5
            ]
        except Exception as e:
            self.hablar("Error al analizar la imagen.")
            print("Error:", e)
            return
 
        # Dice los objetos detectados en la imagen analizada
        if objetos_detectados:
            for objeto, probabilidad in objetos_detectados:
                self.hablar(f"Veo un {objeto} con una probabilidad del {probabilidad} por ciento.")
        else:
            self.hablar("No detecto objetos relevantes en la imagen.")
 
    def eliminarImagen(self):
        """Elimina la imagen capturada si existe."""
        if os.path.exists(self.nombreImagen):
            os.remove(self.nombreImagen)
            print(f"Imagen '{self.nombreImagen}' eliminada.")
 
    def ejecutar(self):
        """Ejecuta el sistema en un bucle principal."""
        while True:
            comando = self.escucharComando()
            if not comando:
                continue
 
            if "que ves" in comando or "qué ves" in comando or "que vez" in comando:
                self.analizarImagen()
            elif "salir" in comando:
                self.hablar("Saliendo del programa. Adiós.")
                break
            else:
                self.hablar("No te entiendo.")
 
        # Limpiar recursos
        self.limpiar()
 
    # Liberar recursos abiertos
    def limpiar(self):
        """Libera los recursos utilizados."""
        self.camara.release()
        cv2.destroyAllWindows()
        self.eliminarImagen()
 
 
if __name__ == "__main__":
    sistema = SistemaDeteccion()
    sistema.ejecutar()