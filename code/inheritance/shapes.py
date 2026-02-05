from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def areaaa(self):
        return 3.14*self.r**2


my_square = Rectangle(3, 3)
print(my_square.area()) # 9
my_circle = Circle(3)
