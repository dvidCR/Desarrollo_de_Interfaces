# Cambia el setCurrentIndex a 1 - ¿Qué ocurre cómo funciona este layout?
# Cambia el color de amarillo a verde

from PyQt6.QtWidgets import QStackedLayout, QWidget, QMainWindow, QApplication  # add this import
from PyQt6.QtGui import QPalette, QColor
import sys

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QStackedLayout()

        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("yellow"))

        layout.setCurrentIndex(1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()