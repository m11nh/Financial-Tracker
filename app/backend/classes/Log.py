class Log:

    def __init__(self, day: int, month: int, year: int, amount: float, notes: str): 
        self._day = day
        self._month = month
        self._year = year
        self._amount = amount
        self._notes = notes

    def getDay(self) -> int: 
        return self._day

    def getMonth(self) -> int: 
        return self._month

    def getYear(self) -> int: 
        return self._year

    def getAmount(self) -> float: 
        return self._amount

    def getNotes(self) -> str:
        return self._notes

    