class MonthlyLog():
    def __init__(self, month, year): 
        self._month = month
        self._year = year
        self._dailyLogs = {} 
    
    def getDailyLogs(self): 
        return self._dailyLogs

    def getMonth(self): 
        return self._month

    def getYear(self): 
        return self._year

    def totalExpenses(self): 
        s = 0
        for l in self._dailyLogs: 
            s+=l.totalExpenses()
        return s


    def totalIncome(self): 
        s = 0
        # fix this as dailylogs is a dictionary
        for l in self._dailyLogs: 
            s+=l.totalIncome()
        return s

    def netProfit(self): 
        return self.totalIncome() - self.totalExpenses()