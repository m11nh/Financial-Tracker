from FinanceTrackingSystem import FinanceTrackingSystem
from Expense import Expense
from Income import Income

# test for adding an expense - 1 january 2020
sys = FinanceTrackingSystem()
exp = Expense(1, 1, 2020, 205, "good shit", True)
sys.addLog(exp)
print(sys._yearlyLogs)
print(sys.getDailyLog(1, 1, 2020)._logs[0].getAmount())
print(sys.getMonthlyLog(10, 1997))

# test for removing the expense created above - 1 january 2020 
sys.removeLog(exp)
print(sys.getDailyLog(1, 1, 2020)._logs)

#  getting a daily log and getting the correct total expense and income 

sys = FinanceTrackingSystem()
sys.addLog(Expense(1, 1, 2020, 200, "good shit", True))
sys.addLog(Expense(1, 1, 2020, 300, "shit", True))
sys.addLog(Income(1, 1, 2020, 100, "god shit"))
sys.addLog(Expense(1, 1, 2020, 100, "gd shit", True))
print(sys.getDailyLog(1, 1, 2020).netProfit())
print(sys.getMonthlyLog(1, 2020).netProfit())
print(sys.getYearlyLog(2020).netProfit())
print(sys.getMonthlyLog(1, 2020).totalExpenses())



