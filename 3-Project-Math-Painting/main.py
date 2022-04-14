from models.canvas import Canvas
from models.square import Square
from models.rectangle import Rectangle

# main()
canvas = Canvas(height=800, width=800, color=(255, 255, 255))

rec_1 = Rectangle(x=250, y=400, height=200, width=300, color=(100, 200, 255))

# rec_1.draw(canvas)

square_1 = Square(x=250, y=300, side=100, color=(0, 100, 222))

# square_1.draw(canvas)

# canvas.make_image('img.png')


# Get canvas width & height from user input
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dictionary of color codes and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

# Create a canvas with the user data
canvas = Canvas(canvas_height, canvas_width, colors[canvas_color])







