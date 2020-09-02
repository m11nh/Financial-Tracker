from YearlyLog import YearlyLog
from MonthlyLog import MonthlyLog
from DailyLog import DailyLog
from Log import Log

class FinanceTrackingSystem: 
    def __init__(self):
        self._yearlyLogs = {} # list of yearlyLogs
    
    def addLog(self, l : Log): 
        # find the year
        if l.getYear() not in self._yearlyLogs: 
            self._yearlyLogs[l.getYear()] = YearlyLog(l.getYear())
        yearLog = self._yearlyLogs[l.getYear()]

        # find the month
        if l.getMonth() not in yearLog.getMonthlyLogs(): 
            yearLog.getMonthlyLogs()[l.getMonth()] = MonthlyLog(l.getMonth(), l.getYear())
        monthLog = yearLog.getMonthlyLogs()[l.getMonth()] 
            
        # find the day
        if l.getDay() not in monthLog.getDailyLogs(): 
            monthLog.getDailyLogs()[l.getDay()] = DailyLog(l.getDay(), l.getMonth(), l.getYear())
        dailyLog = monthLog.getDailyLogs()[l.getDay()]

        # add 
        dailyLog.addLog(l)

    def removeLog(self, l : Log): 
        dailyLog = self.getDailyLog(l.getDay(), l.getMonth(), l.getYear())
        dailyLog.removeLog(l)

    def getDailyLog(self, day, month, year): 
        if day not in self.getMonthlyLog(month, year).getDailyLogs():
            self.getMonthlyLog(month, year).getDailyLogs()[day] = DailyLog(day, month, year)
        return self.getMonthlyLog(month, year).getDailyLogs()[day]

    def getMonthlyLog(self, month, year): 
        if month not in self.getYearlyLog(year).getMonthlyLogs(): 
            self.getYearlyLog(year).getMonthlyLogs()[month] = MonthlyLog(year, month)
        return self.getYearlyLog(year).getMonthlyLogs()[month]

    def getYearlyLog(self, year): 
        if year not in self._yearlyLogs: 
            self._yearlyLogs[year] = YearlyLog(year)
        return self._yearlyLogs[year]