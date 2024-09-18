from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys

app = QApplication(sys.argv)

window = QWidget()
button = QPushButton("Push me!!", window)
window.show()

app.exec()