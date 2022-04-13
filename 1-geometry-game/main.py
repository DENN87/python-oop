"""
Development Steps for Geometry Game

    1. Writing down the objects on paper
            point, rectangle
    2. Writing a class for each object
            class Point, class Rectangle
    3. Writing methods for each class

    4. Calling the classes and their methods

"""

class Point:  # a class is a blueprint, it defines how a point object looks like and what it does

    # The special method __init__ is the Python constructor,
    # lets the class initialize the object's attributes
    def __init__(self, x, y):  # self - is a Point object
        self.x = x
        self.y = y


point1 = Point(10, 20)  # point1 is an object instance

