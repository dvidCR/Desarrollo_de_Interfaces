from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit, QVBoxLayout
import sys


class Ventana(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Una Ventanita")
        
        self.label = QLabel()
        
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)
        
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label) 
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        
        # self.button = QPushButton("Push Me!!")
        # self.button.setCheckable(True)
        # self.button.clicked.connect(self.the_button_was_clicked)
        # self.button.clicked.connect(self.the_button_was_toogled)
        # self.setCentralWidget(self.button)
        
    def the_button_was_clicked(self):
        print("Has hecho click")

    def the_button_was_toogled(self, checked):
        print("Check", checked)
        if checked:
            print("Hola quien seas")
        else:
            print("Quien eres")
        
    
app = QApplication(sys.argv)
ventana = Ventana()

ventana.show()

app.exec()