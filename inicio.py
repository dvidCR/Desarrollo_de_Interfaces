from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys


class Ventana(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Una Ventanita")
        self.button = QPushButton("Push Me!!")
        self.setCentralWidget(self.button)


app = QApplication(sys.argv)
ventana = Ventana()

ventana.show()

app.exec()