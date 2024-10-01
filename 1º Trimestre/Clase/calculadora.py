import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QGridLayout

class Calculadora(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.resultado = QLineEdit()
        layout = QGridLayout()
        layout.addWidget(self.resultado, 0, 0, 1, 5)
        
        nombreBoton = [["(", ")", "cls", "<-"],
                       ["1", "2", "3", "-"],
                       ["4", "5", "6", "+"],
                       ["7", "8", "9", "*"],
                       ["0", "/", ".", "="]]
        
        for i in range (1,6):
            for j in range (4):
                boton = QPushButton(nombreBoton[i-1][j])
                layout.addWidget(boton,i,j)
                boton.clicked.connect(self.press_button)
        
        self.setWindowTitle("La Calculadora")
        self.setGeometry(600, 300, 300, 300)
        
        self.setLayout(layout)
        
    def press_button(self):
        sender = self.sender()
        try:
            if sender.text() == "=":
                self.resultado.setText(str(eval(self.resultado.text())))
            elif sender.text() == "cls":
                self.resultado.clear()
            elif sender.text() == "<-":
                print(self.resultado.text())
            else:
                self.resultado.setText(self.resultado.text() + sender.text())
        except SyntaxError as e:
            print(e)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    sys.exit(app.exec())