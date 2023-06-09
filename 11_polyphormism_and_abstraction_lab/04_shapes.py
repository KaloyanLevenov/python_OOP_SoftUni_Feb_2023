from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, height: int, width: int):
        self.__height = height
        self.__width = width

    def calculate_area(self):
        return self.__height * self.__width

    def calculate_perimeter(self):
        return 2 * (self.__width + self.__height)


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_perimeter(self):
        return pi * self.__radius * 2

    def calculate_area(self):
        return pi * (self.__radius ** 2)



c = Circle(5)
print(c.calculate_area())
print(c.calculate_perimeter())