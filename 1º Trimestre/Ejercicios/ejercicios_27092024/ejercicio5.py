import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
        self.setFixedSize(100,100)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        
        self.colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "cyan", "magenta", "brown", "gray"]
        self.initialColor = 0
        
        layoutV = QVBoxLayout()
        layoutH = QHBoxLayout()
        
        button1 = QPushButton("Color Random")
        button2 = QPushButton("Cambiar al siguiente color")
        button3 = QPushButton("Cambiar al color anterior")

        layoutV.addWidget(button1)
        layoutV.addWidget(button2)
        layoutV.addWidget(button3)
        
        button1.pressed.connect(self.random)
        button2.pressed.connect(self.changeColor(True))
        button3.pressed.connect(self.changeColor(False))
        
        layoutH.addWidget(Color(self.changeColor(False)))

        layoutV.addItem(layoutH)
        
        widget = QWidget()
        widget.setLayout(layoutV)
        self.setCentralWidget(widget)
        
    def random(self):
        random_color = random.choice(self.colors)
        return random_color
        
    def changeColor(self, advance):
        cont = 0
        
        if advance:
            cont = (self.initialColor + 1) % len(self.colors)  # Avanzar al siguiente color
        else:
            cont = (self.initialColor - 1) % len(self.colors)
        
        return self.colors[cont]

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()