import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QLabel, QGridLayout
from PyQt6.QtCore import Qt

class Login(QMainWindow):
    
    def __init__(self, user, passw):
        super().__init__()
        
        self.user = user
        self.passw = passw
        
        self.setWindowTitle("Inicio de sesión")
        self.widget = QWidget()
        self.layoutG = QGridLayout()
        
    def position(self):
        label = QLabel("Inicio de sesión")
        
        msgUser = QLabel("Usuario:")
        self.inputUser = QLineEdit()
        
        msgPassw = QLabel("Contraseña:")
        self.inputPassw = QLineEdit()
        self.inputPassw.setEchoMode(QLineEdit.EchoMode.Password)
        
        show = QPushButton("Mostrar")
        show.setCheckable(True)
        show.setChecked(True)
        show.clicked.connect(self.showPass)
        
        login = QPushButton("Iniciar Sesion")
        login.clicked.connect(self.login)
        
        self.layoutG.addWidget(label, 0, 1)
        
        self.layoutG.addWidget(msgUser, 1, 0)
        self.layoutG.addWidget(self.inputUser, 1, 1)
        
        self.layoutG.addWidget(msgPassw, 2, 0)
        self.layoutG.addWidget(self.inputPassw, 2, 1)
        self.layoutG.addWidget(show, 2, 2)
        
        self.layoutG.addWidget(login, 3, 1)
        
        self.window()
        
    def login(self):
        if self.user == self.inputUser.text() and self.passw == self.inputPassw.text():
            label = QLabel("Has iniciado sesión correctamente")
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.setCentralWidget(label)
        else:
            self.inputUser.clear()
            self.inputPassw.clear()
            label = QLabel("Usuario o contraseña incorrecto")
            self.layoutG.addWidget(label, 4, 1)
            self.window()
            
    def showPass(self, s):
        if s:
            self.inputPassw.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.inputPassw.setEchoMode(QLineEdit.EchoMode.Password)
        
    def window(self):
        self.layoutG.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget.setLayout(self.layoutG)
        self.setCentralWidget(self.widget)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login("a", "s")
    window.position()
    window.show()
    sys.exit(app.exec())