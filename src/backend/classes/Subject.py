from abc import ABC, abstractmethod

class Subject(ABC): 
    def notifyObservers(self): 
        pass
    def addObserver(self, o : Observer):
        pass
    def detachObserver(self, o : Observer): 
        pass