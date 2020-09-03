from abc import ABC, abstractmethod

class LogPeriod: 
    def __init__(self): 
        self.totalExpenses = None
        self.totalIncome = None
        self.netProfit = None
    
    def getTotalExpenses(self): 
        pass

    def getTotalIncome(self): 
        pass

    def getNetProfit(self): 
        pass
