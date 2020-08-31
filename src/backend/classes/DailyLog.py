
class DailyLog():
    def __init__(self, day, month, year): 
        self._day = day
        self._month = month
        self._year = year
        self._logs = []
    
    def getLogs(self): 
        return self.logs