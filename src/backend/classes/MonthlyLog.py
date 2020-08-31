class MonthlyLog():
    def __init__(self, month, year): 
        self._month = month
        self._year = year
        self._dailyLogs = [] 
    
    def getDailyLogs(self): 
        return self.dailyLogs