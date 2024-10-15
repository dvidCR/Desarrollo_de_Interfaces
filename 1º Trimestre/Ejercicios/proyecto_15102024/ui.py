import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QCalendarWidget, QVBoxLayout, QComboBox
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QDate

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Calendario")
        self.setGeometry(100, 100, 600, 400)
        
        self.widget = QWidget()
        self.calendar = QCalendarWidget(self)
        self.prueba()
        
    def prueba(self):
        # setting geometry to the calendar
        self.calendar.setGeometry(10, 10, 400, 250)
 
        # date
        date = QDate(2021, 1, 1)
 
        # setting selected date
        self.calendar.setSelectedDate(date)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = MainWindow()
    m.show()
    sys.exit(app.exec())