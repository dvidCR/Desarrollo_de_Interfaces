# Ejercicios del 27 de SEPTIEMBRE del 2024

## Ejercicio 1

```python
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QCheckBox, QPushButton, QRadioButton
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()

        layout.addWidget(QCheckBox())
        layout.addWidget(QPushButton("Presiona Aqui"))
        layout.addWidget(QRadioButton())

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
```

`../../IMG/ejercicio1.png`

## Ejercicio 2

```python
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layoutH = QHBoxLayout()
        layoutV = QVBoxLayout()
        
        label = QLabel("Hola, esto es un layout")
        le = QLineEdit()

        layoutV.addWidget(Color('red'))
        layoutV.addWidget(Color('yellow'))
        layoutV.addWidget(Color('red'))
        
        
        layoutH.addWidget(label)
        layoutH.addWidget(le)

        widget = QWidget()
        layoutV.addItem(layoutH)
        widget.setLayout(layoutV)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
```

`../../IMG/ejercicio2.png`

## Ejercicio 3

```python
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QHBoxLayout()

        layout2.setContentsMargins(0,0,0,0)
        layout2.setSpacing(20)

        layout1.addWidget(Color('red'))
        layout1.addWidget(Color('yellow'))
        layout1.addWidget(Color('purple'))

        layout2.addLayout( layout1 )

        layout2.addWidget(Color('green'))
        layout2.addWidget(Color('pink'))

        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('purple'))

        layout2.addLayout( layout3 )

        widget = QWidget()
        widget.setLayout(layout2)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
```

`../../IMG/ejercicio3.png`

## Ejercicio 4

```python
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout = QGridLayout()

        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(QPushButton("Press Me Please"), 0, 1)
        layout.addWidget(Color('green'), 1, 0)
        layout.addWidget(Color('blue'), 1, 1)
        layout.addWidget(QPushButton("Lo mismo que el otro pero en español"), 2, 0)
        layout.addWidget(Color('purple'), 2, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
```

`../../IMG/ejercicio4.png`