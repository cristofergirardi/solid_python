
from abc import ABC, abstractmethod

# Define an abstract class 'Shape'
class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    # Make the 'description' base implementation
    def description(self):
        print(f"{self.__class__.__name__} has the color: {self.color}")    

# Define a concrete class 'Rectangle' that inherits from 'Shape'
class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Define a concrete class 'Circle' that inherits from 'Shape'
class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.141592653589793 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.141592653589793 * self.radius

# Interface contract method
def process_my_color(obj: Shape):
    obj.description()

# Create instances of concrete classes and use their methods
rectangle = Rectangle(4, 5, "red")
print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")
print(f"Rectangle color: {rectangle.color}")

circle = Circle(3, "blue")
print(f"Circle area: {circle.area()}")
print(f"Circle perimeter: {circle.perimeter()}")
print(f"Circle color: {circle.color}")

process_my_color(rectangle)
process_my_color(circle)

