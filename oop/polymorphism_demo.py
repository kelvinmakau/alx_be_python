import math

class Shape:
    def area(self):
       raise NotImplementedError("Subclasses must inherit the area method")

class Rectangle(Shape): # Inherits from shape class
    def __init__(self, length, width):
       super().__init__()
       self.length = length
       self.width = width

    # override the area class to calculate area
    def area(self):
        return self.length * self.width

class Circle(Shape): # Inherits from shape class
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    # override the area class to calculate area
    def area(self):
        return math.pi * (self.radius ** 2)