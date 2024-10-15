import sys
import calendar

class manageCalendar():
    
    def __init__(self):
        self.calendar = calendar.Calendar()
        
    def perMonth(self):
        print(self.calendar.yeardatescalendar(1))
    
    def perYear(self):
        pass
    
    
class Events():
    pass

m = manageCalendar().perMonth()