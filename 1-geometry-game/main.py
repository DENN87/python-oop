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


class Point:  # a class is a blueprint, it defines how a point object looks like and what it does

    # The special method __init__ is the Python constructor,
    # lets the class initialize the object's attributes
    def __init__(self, x, y):  # self - is a Point object
        self.x = x
        self.y = y

    # Function that will return True if the given point(x, y) is
    # in the given rectangle coordinates
    def find_point_inside_rectangle(self, lower_left, upper_right):
        if lower_left[0] < self.x < upper_right[0] \
                and lower_left[1] < self.y < upper_right[1]:
            return True
        else:
            return False

    def distance_from_point(self, x, y):
        return math.sqrt(math.pow(self.x - x, 2) + math.pow(self.y - y, 2))


point1 = Point(2, 5)  # create object instance 'point1'

print(point1.find_point_inside_rectangle((1, 1), (3, 6)))

print(Point(1, 1).distance_from_point(2, 2))
