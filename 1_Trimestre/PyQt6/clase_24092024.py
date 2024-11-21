import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        #Añadir un array de objetos
        # layout = QVBoxLayout()
        # widgets = [
        #     QCheckBox,
        #     QComboBox,
        #     QDateEdit,
        #     QDateTimeEdit,
        #     QDial,
        #     QDoubleSpinBox,
        #     QFontComboBox,
        #     QLCDNumber,
        #     QLabel,
        #     QLineEdit,
        #     QProgressBar,
        #     QPushButton,
        #     QRadioButton,
        #     QSlider,
        #     QSpinBox,
        #     QTimeEdit,
        # ]

        # for w in widgets:
        #     layout.addWidget(w())

        # Añadir labels y moverlos
        # widget = QLabel("Hello")
        # font = widget.font()
        # font.setPointSize(30)
        # widget.setFont(font)
        # widget.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
    
        # widget2 = QLabel("Chao")
        # font2 = widget2.font()
        # font2.setPointSize(30)
        # widget2.setFont(font2)
        # widget2.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        
        # layout.addWidget(widget)
        # layout.addWidget(widget2)
        
        # wg = QWidget()
        # wg.setLayout(layout)
        
        # self.setCentralWidget(wg)
        
        # Añadir imagenes
        # label = QLabel(self)
        # pixmap = QPixmap('imagen.jpeg')
        # label.setPixmap(pixmap)
        # self.setCentralWidget(label)

        # # Optional, resize window to image size
        # self.resize(pixmap.width(),pixmap.height())
        
    # Añadimos un checkbox
    #     widget = QCheckBox()
    #     widget.setCheckState(Qt.CheckState.Checked)

    #     # For tristate: widget.setCheckState(Qt.CheckState.PartiallyChecked)
    #     # Or: widget.setTristate(True)
    #     widget.stateChanged.connect(self.show_state)

    #     self.setCentralWidget(widget)

    # def show_state(self, s):
    #     print(s == Qt.CheckState.Checked.value)
        
    # # creamos un desplegable
    # desplegable = QComboBox()
    # self.setCentralWidget(desplegable)

    # desplegable.addItems(["Opción 1", "Opción 2", "Opción 3"])
        
        
        
        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()