from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def printArea(self):
        return 0

class Rectangle(shape):
    type="Rectangle"
    sides=4
    def __init__(self):
        self.length=6
        self.bredth=7

    def printArea(self):
        return self.length * self.bredth

rect1=Rectangle()
print(rect1.printArea())
