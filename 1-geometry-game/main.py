"""
Development Steps for Geometry Game

    1. Writing down the objects on paper
            point, rectangle
    2. Writing a class for each object
            class Point, class Rectangle
    3. Writing methods for each class

    4. Calling the classes and their methods

"""
import math
from random import randint


class Point:  # a class is a blueprint, it defines how a point object looks like and what it does

    # The special method __init__ is the Python constructor,
    # lets the class initialize the object's attributes
    def __init__(self, x, y):  # self - is a Point object
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    # Function that will return True if the given point(x, y) is
    # in the given rectangle coordinates
    def find_point_inside_rectangle(self, rectangle):
        if rectangle.p1.x < self.x < rectangle.p2.x \
                and rectangle.p1.y < self.y < rectangle.p2.y:
            return True
        else:
            return False

    def distance_from_point(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5


class Rectangle:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):  # special method used to represent a class’s objects as a string
        return "Rectangle Coordinates: \n" \
               f"({self.p1.x}, {self.p1.y}) \n" \
               f"({self.p2.x}, {self.p2.y}) \n" \



# creating random points for a rectangle using 'randint' library
rectangle = Rectangle(
    Point(
        randint(0, 9),
        randint(0, 9),
    ),
    Point(
        randint(10, 19),
        randint(10, 19),
    )
)

print(rectangle)


user_point = Point(int(input("Guess X: ")),
                   int(input("Guess Y: ")))

if user_point.find_point_inside_rectangle(rectangle):
    print(f"Well done, your point was inside the rectangle!")
else:
    print("Your point was outside the rectangle, try again!")
