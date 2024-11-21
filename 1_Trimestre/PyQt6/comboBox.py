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


class main(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widgets App")
        
        self.desplegable = QComboBox()
        self.setMenuWidget(self.desplegable)

        self.desplegable.addItems(["", "App", "Layout", "Img", "Checkbox"])
        
        self.desplegable.currentIndexChanged.connect(self.updateWidget)

    def updateWidget(self):
        selection = self.desplegable.currentText()

        match selection:
            case "":
                self.setCentralWidget(None)
            case "App":
                self.arrayObject()
            case "Layout":
                self.layouts()
            case "Img":
                self.img()
            case "Checkbox":
                self.checkbox()
        
    def arrayObject(self):
        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        for w in widgets:
            layout.addWidget(w())
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
    def layouts(self):
        layout = QVBoxLayout()
        widget = QLabel("Hello")
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
    
        widget2 = QLabel("Chao")
        font2 = widget2.font()
        font2.setPointSize(30)
        widget2.setFont(font2)
        widget2.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        
        layout.addWidget(widget)
        layout.addWidget(widget2)
        
        wg = QWidget()
        wg.setLayout(layout)
        
        self.setCentralWidget(wg)
        
    def img(self):
        label = QLabel(self)
        pixmap = QPixmap('imagen.jpeg')
        label.setPixmap(pixmap)
        self.setCentralWidget(label)

        # Optional, resize window to image size
        self.resize(pixmap.width(),pixmap.height())
    
    def checkbox(self):
        widget = QCheckBox()
        widget.setCheckState(Qt.CheckState.Checked)

        # For tristate: widget.setCheckState(Qt.CheckState.PartiallyChecked)
        # Or: widget.setTristate(True)
        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)

    def show_state(self, s):
        print(s == Qt.CheckState.Checked.value)
        
app = QApplication(sys.argv)
window = main()
window.show()
app.exec()