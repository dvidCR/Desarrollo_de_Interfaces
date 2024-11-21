#importamos las librerías necesarias
import sys
import random
from PyQt6 import QtWidgets, uic

#Carga la interfaz gráfica y conecta los botones
class Ventana(QtWidgets.QMainWindow):
    '''Esta es la clase principal'''
    #Inicializamos la ventana y conectamos los botones
    def __init__(self, padre=None):
        #Inicializa la ventana
        QtWidgets.QMainWindow.__init__(self, padre)
        uic.loadUi("Ejercicio1.ui",self) #Lee el archivo de QtDesigner
        
        self.setWindowTitle("Ejercicio1") #Título de la ventana
        
        #Conectar botón a función
        self.pushButton.clicked.connect(self.function_1)
        self.pushButton_2.clicked.connect(self.function_2)
        
        self.label = QtWidgets.QLabel()
        self.layoutV = QtWidgets.QVBoxLayout()
        self.widget = QtWidgets.QWidget()
        
    def function_1(self):
        self.pushButton.resize(random.randint(1, 100), random.randint(1, 100))
    
    def function_2(self):
        self.pushButton_2.move(random.randint(0, self.x()), random.randint(0, self.y()))

# se crea la instancia de la aplicación
app = QtWidgets.QApplication(sys.argv)
# se crea la instancia de la ventana
miVentana = Ventana()
# se muestra la ventana 
miVentana.show()
# se entrega el control al sistema operativo
sys.exit(app.exec())