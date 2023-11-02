from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        self.color = None

    def draw(self):
        print(
            f"Drawing Circle: {self.center} with radius {self.radius}, Color: {self.color}")


class Triangle(Shape):
    def __init__(self, vertices):
        self.vertices = vertices
        self.color = None

    def draw(self):
        print(f"Drawing Triangle: {self.vertices}, Color: {self.color}")


class Rectangle(Shape):
    def __init__(self, position, width, height):
        self.position = position
        self.width = width
        self.height = height
        self.color = None

    def draw(self):
        print(
            f"Drawing Rectangle: {self.position} with width {self.width}, height {self.height}, Color: {self.color}")


class Engine2D:
    def __init__(self):
        self.canvas = []
        self.current_color = "White"

    def add_shape(self, shape):
        shape.color = self.current_color
        self.canvas.append(shape)

    def set_color(self, color):
        self.current_color = color

    def draw(self):
        print(self.canvas)
        for shape in self.canvas:
            shape.draw()
        self.canvas = []
