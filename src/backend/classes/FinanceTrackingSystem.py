from msa3.src.backend.classes.YearlyLog import YearlyLog, MonthlyLog, DailyLog

class FinanceTrackingSystem: 
    def __init__(self):
        self._yearlyLogs = {} # list of yearlyLogs
    
    def addExpense(self, e : Expense): 
        # find the year
        if e.getYear() not in self._yearlyLogs: 
            self._yearlyLogs[e.getYear()] = YearlyLog(e.getYear())
        yearLog = self._yearlyLogs()[e.getYear]

        # find the month
        if e.getMonth() not in yearLog.getMonthlyLog: 
            year.getMonthlyLog[e.getMonth()] = MonthlyLog(e.getMonth(), e.getYear())
        monthLog = yearLog.getMonthlyLog()[e.getMonth()] 
            
        # find the day
        if e.getDay() not in monthLog.getDailyLog: 
            monthLog.getDailyLog[e.getDay()] = DailyLog(e.getDay(), e.getMonth(), e.getYear())
        dailyLog = monthLog.getDailyLog()[e.getDay()]

        # add 
        dailyLog.append(e)

    def removeExpense(self, e : Expense): 
        l = getDailyLog(e.getDay(), e.getMonth(), e.getYear())

    def addIncome(self, i : Income): 
        pass

    def removeIncome(self, i : Income):
        pass

    def getDailyLog(self, day, month, year): 
        pass

    def getMonthlyLog(self, day, month, year): 
        pass

    def getYearlyLog(self, year): 
        pass