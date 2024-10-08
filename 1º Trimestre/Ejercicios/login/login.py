import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QLabel, QGridLayout, QDialog, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap

class Login(QMainWindow):
    
    def __init__(self, user, passw):
        super().__init__()
        
        self.user = user
        self.passw = passw
        
        self.setWindowTitle("Inicio de sesión")
        
        self.widget = QWidget()
        self.layoutG = QGridLayout()
        self.layoutH = QHBoxLayout()
        self.dlg = QDialog(self)
        
    def position(self):
        label = QLabel("Inicio de sesión")
        
        msgUser = QLabel("Usuario:")
        self.inputUser = QLineEdit()
        
        msgPassw = QLabel("Contraseña:")
        self.inputPassw = QLineEdit()
        self.inputPassw.setEchoMode(QLineEdit.EchoMode.Password)
        
        show = QPushButton("Mostrar")
        show.setCheckable(True)
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
        img_label = QLabel(self)

        if self.user == self.inputUser.text() and self.passw == self.inputPassw.text():
            self.dlg.setWindowTitle("Inicio de sesión correcto")
            self.dlg.setWindowIcon(QIcon("ok.ico"))
            
            img = QPixmap("ok.png")
            img_label.setPixmap(img)
            
            label = QLabel("Has iniciado sesión correctamente")
            label.setStyleSheet("QLabel {color: green}")
        else:
            self.inputUser.clear()
            self.inputPassw.clear()
            
            self.dlg.setWindowTitle("Inicio de sesión incorrecto")
            self.dlg.setWindowIcon(QIcon("error.ico"))
            
            img = QPixmap("error.png")
            img_label.setPixmap(img)
            
            label = QLabel("Usuario o contraseña incorrecto")
            label.setStyleSheet("QLabel {color: red}")

        img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.layoutH.addWidget(img_label)
        self.layoutH.addWidget(label)
        
        self.dlg.setLayout(self.layoutH)
        self.dlg.exec()
        
        self.layoutH.removeWidget(img_label)
        self.layoutH.removeWidget(label)
            
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