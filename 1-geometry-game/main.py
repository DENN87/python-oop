"""
Development Steps for Geometry Game

    1. Writing down the objects on paper
            point, rectangle
    2. Writing a class for each object
            class Point, class Rectangle
    3. Writing methods for each class

    4. Calling the classes and their methods

"""
import turtle
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
        return ("Rectangle Coordinates: \n"
                f"({self.p1.x}, {self.p1.y}) \n"
                f"({self.p2.x}, {self.p2.y}) \n")

    def area(self):
        return (self.p2.x - self.p1.x) * (self.p2.y - self.p1.y)


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        # rectangle height, width
        rectangle_height = self.p2.y - self.p1.y
        rectangle_width = self.p2.x - self.p1.x

        # Go to coordinate
        canvas.penup()
        canvas.goto(self.p1.x, self.p1.y)

        canvas.pendown()
        canvas.forward(rectangle_width)
        canvas.left(90)

        canvas.forward(rectangle_height)
        canvas.left(90)

        canvas.forward(rectangle_width)
        canvas.left(90)

        canvas.forward(rectangle_height)

        turtle.done()


# creating random points for a rectangle object using 'randint' library
rectangle = Rectangle(
    Point(
        randint(0, 9),
        randint(0, 9),
    ),
    Point(
        randint(100, 190),
        randint(100, 190),
    )
)

print(rectangle)

# GUI Rectangle
gui_rectangle = GuiRectangle(
    Point(
        randint(0, 0),
        randint(0, 0),
    ),
    Point(
        randint(100, 200),
        randint(100, 200),
    )
)
# Create a canvas instance
myturtle = turtle.Turtle()

# Set Canvas Window Size
screen = turtle.Screen()
screen.setup(500, 500)

# Draw the rectangle
gui_rectangle.draw(canvas=myturtle)

# get user input for point
user_point = Point(int(input("Guess X: ")),
                   int(input("Guess Y: ")))

# get user input for area
user_area = int(input("Guess rectangle area: "))

# show user result feedback
if user_point.find_point_inside_rectangle(rectangle):
    print(f"Well done, your point was inside the rectangle!")
else:
    print("Your point was outside the rectangle, try again!")

if rectangle.area() - user_area == 0:
    print("You guessed the area!")
else:
    print(f"Your area was off by: {rectangle.area() - user_area}.")
