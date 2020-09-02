class YearlyLog():
    def __init__(self, year): 
        self._year = year
        self._monthlyLogs= {} 
    
    def getMonthlyLogs(self): 
        return self._monthlyLogs

    def getYear(self): 
        return self._year

    def totalExpenses(self): 
        s = 0
        for l in self._monthlyLogs: 
            s+=l.totalExpenses()
        return s

    def totalIncome(self): 
        s = 0
        for l in self._monthlyLogs: 
            s+=l.totalIncome()
        return s
    
    def netProfit(self): 
        return self.totalIncome() - self.totalExpenses()