from Log import Log
class Expense(Log): 
    def __init__(self, day: int, month: int, year: int, amount: float, notes: str,isNecessary : bool): 
        super().__init__(day, month, year, amount, notes)
        self._isNecessary = isNecessary 
    
    def getIsNecessary(self) -> bool: 
        return self._isNecessary
    
