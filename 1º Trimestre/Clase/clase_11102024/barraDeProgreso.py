#importamos las librerías necesarias
import sys
from PyQt6 import QtWidgets, uic

#Carga la interfaz gráfica y conecta los botones
class Ventana(QtWidgets.QMainWindow):
    '''Esta es la clase principal'''
    #Inicializamos la ventana y conectamos los botones
    def __init__(self, padre=None):
        #Inicializa la ventana
        QtWidgets.QMainWindow.__init__(self, padre)
        uic.loadUi("barraDeProgresoqt.ui",self) #Lee el archivo de QtDesigner
        
        self.setWindowTitle("Progress Bar") #Título de la ventana
        
        #Conectar botón a función
        self.pushButton.clicked.connect(self.funcion)
        self.current_value = 0
        
    def funcion(self):
        if self.current_value != self.progressBar.maximum():
            self.current_value +=5
            self.progressBar.setValue(self.current_value)
        else:
            self.progressBar.reset()
            self.current_value = 0


# se crea la instancia de la aplicación
app = QtWidgets.QApplication(sys.argv)
# se crea la instancia de la ventana
miVentana = Ventana()
# se muestra la ventana 
miVentana.show()
# se entrega el control al sistema operativo
sys.exit(app.exec())