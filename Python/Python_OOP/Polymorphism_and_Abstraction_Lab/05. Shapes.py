from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        return pi * self.r ** 2

    def calculate_perimeter(self):
        return 2 * pi * self.r


class Rectangle(Shape):
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def calculate_area(self):
        return self.h * self.w

    def calculate_perimeter(self):
        return 2 * (self.h + self.w)

circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

