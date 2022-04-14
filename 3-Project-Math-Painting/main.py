import numpy as np
from PIL import Image


class Square:
    """A square shape that can be drawn on a Canvas object"""

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        """Draws itself into the canvas"""
        # Changes a slice of the array with new values
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color


class Rectangle:
    """A rectangle shape that can be drawn on a Canvas object"""

    def __init__(self, x, y, height, width,  color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        """Draws itself into the canvas"""
        # Changes a slice of the array with new values
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color


class Canvas:
    """Object where all shapes are being drawn"""

    def __init__(self, height, width, color):
        self.width = width
        self.height = height
        self.color = color

        # Create a 3d numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # change [0, 0, 0] with user given values for color
        self.data[:] = self.color

    def make_image(self, image_path):
        """Converts the current array into an image file"""
        img = Image.fromarray(self.data, 'RGB')
        img.save(image_path)


# main()
canvas = Canvas(height=800, width=800, color=(255, 255, 255))

rec_1 = Rectangle(x=250, y=400, height=200, width=300, color=(100, 200, 255))

rec_1.draw(canvas)

square_1 = Square(x=250, y=300, side=100, color=(0, 100, 222))

square_1.draw(canvas)

canvas.make_image('img.png')



