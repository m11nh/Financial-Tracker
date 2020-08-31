
class DailyLog():
    def __init__(self, day, month, year): 
        self._day = day
        self._month = month
        self._year = year
        self._logs = []


    def getDay(self): 
        return self._day

    def getMonth(self): 
        return self._month

    def getYear(self): 
        return self._year
    
    def getLogs(self): 
        return self.logs