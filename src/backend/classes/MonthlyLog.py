class MonthlyLog():
    def __init__(self, month, year): 
        self.month = month
        self.year = year
        self.dailyLogs = [] 
    
    def getDailyLogs(self): 
        return self.dailyLogs