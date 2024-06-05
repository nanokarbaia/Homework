
class Animals:
    alive = True

    def __init__(self, weight):
        self.weight = weight

    @staticmethod
    def sleeping():
        print("ZZZZZZzzzzzZZzzz...")

animal1 = Animals(100)

class Cats(Animals):

    def __init__(self, type, weight, color):
        self.type=type
        Animals.__init__(self, weight)
        self.color = color
    @staticmethod
    def eating():
        print("eats...")

animal2 = Cats('Cat', 20, 'grey')

class Lion(Cats):

    def __init__(self, type, weight, color, gender):
        Cats.__init__(self, type, weight, color)
        self.gender = gender
    @staticmethod
    def eating():
        print("eats...")
animal3 = Lion('Lion', 130, 'Orange', 'Male')

animal3.eating()

from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circle(Polygon):

    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        print(2 * 3.14 * self.radius)

    def area(self):
        print(3.14 * self.radius ** 2)


circle1 = Circle(2)
circle1.perimeter()
circle1.area()








