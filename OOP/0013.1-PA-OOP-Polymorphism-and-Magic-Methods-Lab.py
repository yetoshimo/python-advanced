# 01. Execute
# def execute(func, *args):
#     return func(*args)

# 02. Instruments
# def play_instrument(instrument):
#     return instrument.play()

# 03. Shapes
# from abc import ABC, abstractmethod
# from math import pi
#
#
# class Shape(ABC):
#     @abstractmethod
#     def calculate_area(self):
#         return
#
#     @abstractmethod
#     def calculate_perimeter(self):
#         return
#
#
# class Circle(Shape):
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculate_area(self):
#         return pi * self.radius ** 2
#
#     def calculate_perimeter(self):
#         return pi * self.radius * 2
#
#
# class Rectangle(Shape):
#
#     def __init__(self, height, wight):
#         self.height = height
#         self.width = wight
#
#     def calculate_area(self):
#         return self.height * self.width
#
#     def calculate_perimeter(self):
#         return 2 * (self.height + self.width)

# 04. ImageArea
# class ImageArea:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_area(self):
#         return self.width * self.height
#
#     def __eq__(self, other):
#         return self.get_area() == other.get_area()
#
#     def __ne__(self, other):
#         return self.get_area() != other.get_area()
#
#     def __gt__(self, other):
#         return self.get_area() > other.get_area()
#
#     def __ge__(self, other):
#         return self.get_area() >= other.get_area()
#
#     def __lt__(self, other):
#         return self.get_area() < other.get_area()
#
#     def __le__(self, other):
#         return self.get_area() <= other.get_area()
