import turtle


class Rectangle:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return ("Rectangle Coordinates: \n"
                f"({self.p1.x}, {self.p1.y}) \n"
                f"({self.p2.x}, {self.p2.y}) \n")

    def area(self):
        return (self.p2.x - self.p1.x) * (self.p2.y - self.p1.y)


class GuiRectangle(Rectangle):  # class inheritance, GuiRectangle will inherit from parent class Rectangle

    def draw_rectangle(self, canvas):
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
