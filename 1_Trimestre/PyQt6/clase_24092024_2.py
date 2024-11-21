from PyQt6.QtWidgets import QApplication,QLineEdit,QWidget,QFormLayout
from PyQt6.QtGui import QIntValidator,QDoubleValidator,QFont
from PyQt6.QtCore import Qt
import sys

class lineEditDemo(QWidget):
        def __init__(self,parent=None):
                super().__init__(parent)
                e1 = QLineEdit()
                e1.setValidator(QIntValidator())
                e1.setMaxLength(4)
                e1.setAlignment(Qt.AlignmentFlag.AlignRight)
                e1.setFont(QFont("Arial",20))

                e2 = QLineEdit()
                e2.setValidator(QDoubleValidator(0.99,99.99,2))
                e3 = QLineEdit()
                e3.setInputMask("+99_9999_999999")

                e4 = QLineEdit()
                e4.textChanged.connect(self.textchanged)

                e5 = QLineEdit()
                e5.setEchoMode(QLineEdit.EchoMode.Password)

                e6 = QLineEdit("Hello PyQt6")
                e6.setReadOnly(True)
                e5.editingFinished.connect(self.enterPress)

                flo = QFormLayout()
                flo.addRow("integer validator",e1)
                flo.addRow("Double validator",e2)
                flo.addRow("Input Mask",e3)
                flo.addRow("Text changed",e4)
                flo.addRow("Password",e5)
                flo.addRow("Read Only",e6)

                self.setLayout(flo)
                self.setWindowTitle("QLineEdit Example")

        def textchanged(self,text):
                print("Changed: " + text)

        def enterPress(self):
                print("Enter pressed")

if __name__ == "__main__":
        app = QApplication(sys.argv)
        win = lineEditDemo()
        win.show()
        sys.exit(app.exec())