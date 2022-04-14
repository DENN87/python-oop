import turtle
from random import randint
from models.point import Point, GuiPoint
from models.rectangle import Rectangle, GuiRectangle

# GUI Rectangle instance
gui_rectangle = GuiRectangle(
    Point(
        randint(0, 50),
        randint(0, 50),
    ),
    Point(
        randint(100, 200),
        randint(100, 200),
    )
)

print(gui_rectangle)

# get user input for point
user_point = Point(int(input("Guess X: ")),
                   int(input("Guess Y: ")))

# get user input for area
user_area = int(input("Guess rectangle area: "))

# show user result feedback
if user_point.find_point_inside_rectangle(gui_rectangle):
    print(f"Well done, your point was inside the rectangle!")
else:
    print("Your point was outside the rectangle, try again!")

if gui_rectangle.area() - user_area == 0:
    print("You guessed the area!")
else:
    print(f"Your area was off by: {gui_rectangle.area() - user_area}.")

# Create a canvas instance
myturtle = turtle.Turtle()

# Set Canvas Window Size
screen = turtle.Screen()
screen.setup(500, 500)

# Draw user point
gui_point = GuiPoint(user_point.x, user_point.y)
gui_point.draw_point(canvas=myturtle)

# Draw the rectangle
gui_rectangle.draw_rectangle(canvas=myturtle)



