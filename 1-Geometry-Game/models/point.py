class Point:  # a class is a blueprint, it defines how a point object looks like and what it does

    # The special method __init__ is the Python constructor,
    # lets the class initialize the object's attributes
    def __init__(self, x, y):  # self - is a Point object
        self.x = x
        self.y = y

    def __repr__(self):  # special method used to represent a class’s objects as a string
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


class GuiPoint(Point):

    def draw_point(self, canvas):
        canvas.hideturtle()
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.dot(7.5, "red")