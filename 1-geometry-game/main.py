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

    # function that will return True if the given point(x, y) is in the given rectangle coordinates
    def find_point_inside_rectangle(self, lower_left, upper_right):
        if lower_left[0] < self.x < upper_right[0] \
                and lower_left[1] < self.y < upper_right[1]:
            return True
        else:
            return False


point1 = Point(2, 5)  # point1 is an object instance

print(point1.find_point_inside_rectangle((1, 1), (3, 6)))
