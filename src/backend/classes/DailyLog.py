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
        return self._logs

    def addLog(self, log): 
        self._logs.append(log)
    
    def removeLog(self, log): 
        self._logs.remove(log)
    
    def totalExpenses(self): 
        s = 0
        for l in self._logs: 
            if type(l).__name__ == "Expense": 
                s+=l.getAmount()
        return s

    def totalIncome(self): 
        s = 0
        for l in self._logs: 
            if type(l).__name__ == "Income": 
                s+=l.getAmount()
        return s

    def netProfit(self): 
        return self.totalIncome() - self.totalExpenses()
