import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QStackedLayout
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
        
        self.layout()
        
    def layout(self):
        layout = QStackedLayout()
        self.layoutV = QVBoxLayout()
        self.layoutH = QHBoxLayout()
        
        button1 = QPushButton("Color Random")
        button2 = QPushButton("Cambiar al siguiente color")
        button3 = QPushButton("Cambiar al color anterior")
        button4 = QPushButton("Boton stacklayout")

        self.layoutV.addWidget(button1)
        self.layoutV.addWidget(button2)
        self.layoutV.addWidget(button3)
        self.layoutV.addWidget(button4)
        
        button1.pressed.connect(self.random)
        button2.pressed.connect(lambda: self.changeColor(True))
        button3.pressed.connect(lambda: self.changeColor(False))
        button4.pressed.connect(lambda: layout.setCurrentIndex(random.randint(0, 3)))
        
        self.mostrarColor = Color(self.colors[self.initialColor])
        
        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("yellow"))

        layout.setCurrentIndex(3)
        
        self.layoutH.addWidget(self.mostrarColor)

        self.layoutV.addItem(self.layoutH)
        self.layoutV.addItem(layout)
        
        self.widget()

    def widget(self):
        widget = QWidget()
        widget.setLayout(self.layoutV)
        self.setCentralWidget(widget)
        
    def random(self):
        self.layoutH.removeWidget(self.mostrarColor)
        
        random_color = random.randint(0, len(self.colors) - 1)
        self.initialColor = random_color
        
        self.layout()
        
    def changeColor(self, advance):
        self.layoutH.removeWidget(self.mostrarColor)
        
        if advance:
            self.initialColor = (self.initialColor + 1) % len(self.colors)
        else:
            self.initialColor = (self.initialColor - 1) % len(self.colors)
            
        self.layout()
            
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()