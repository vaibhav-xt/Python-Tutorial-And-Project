from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle:
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 5

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())