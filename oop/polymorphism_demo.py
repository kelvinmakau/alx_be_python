import math

class Shape:
    def area(self):
       raise NotImplementedError("Subclasses must inherit the area method")

class Rectangle(Shape):
    def __init__(self, length, width):
       super().__init__()
       self.length = length
       self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)