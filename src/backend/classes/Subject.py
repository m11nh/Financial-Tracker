from abc import ABC, abstractmethod

class Subject(ABC): 
    def notifyObservers(self): 
        pass
    def addObserver(o : Observer)