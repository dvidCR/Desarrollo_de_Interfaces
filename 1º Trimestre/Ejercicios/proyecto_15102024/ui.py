import sys
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QCalendarWidget, QVBoxLayout, QComboBox
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QDate, QEvent

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Calendario")
        self.setGeometry(100, 100, 600, 400)
        
        self.date = datetime
        self.widget = QWidget()
        self.calendar = QCalendarWidget(self)
        self.setCalendar()
        
    def setCalendar(self):
        self.calendar.setGeometry(10, 10, 400, 250)
        date = QDate(self.date.now().date())
        self.calendar.setSelectedDate(date)
        
    def setTask(self):
        pass
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = MainWindow()
    m.show()
    sys.exit(app.exec())