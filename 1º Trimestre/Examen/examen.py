import sys
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets, uic

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, padre = None):
        QtWidgets.QMainWindow.__init__(self, padre)
        uic.loadUi("examen.ui", self)
        
        self.setWindowTitle("Examen PyQt6")
                
        self.pushButton.clicked.connect(self.añadir)
        self.pushButton_2.clicked.connect(self.borrar)
        
    def añadir(self):
        edad = int(self.lineEdit_3.text())
        
        if edad != int:
            if edad >= 18:
                self.message("Se le va a añadir a la base de datos")
            else:
                self.message("Usted es menor 18 años, no se le puede añadir a la base de datos")
        else:
            self.message("La edad se escribela por numeros")
    
    def borrar(self):
        self.message("Se le borraran los datos introducidos")
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
    
    def message(self, message):
        self.mw = messageWindow()
        self.mw.view(message)
        self.mw.show()
    
class messageWindow(QtWidgets.QMessageBox):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Examen PyQt6")
        
        self.label = QtWidgets.QLabel
        self.qlayout = QtWidgets.QLayout
        self.widget = QtWidgets.QWidget
        
    def view(self, message):
        self.label.setText(message)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.qlayout.addWidget(self.label)
        self.widget.setLayout(self.qlayout)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())