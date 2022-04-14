from models.canvas import Canvas
from models.square import Square
from models.rectangle import Rectangle


# Get canvas width & height from user input
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dictionary of color codes and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

# Create a canvas with the user data
canvas = Canvas(canvas_height, canvas_width, colors[canvas_color])

# Create shapes from user input
while True:
    shape_type = input("What would you like to draw (ex: rectangle, square or quit)? ")

    # Get data for rectangle
    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter x of rectangle: "))
        rec_y = int(input("Enter y of rectangle: "))
        rec_width = int(input("Enter the width of the rectangle: "))
        rec_height = int(input("Enter the height of the rectangle: "))
        r = int(input("Enter R color: "))
        g = int(input("Enter G color: "))
        b = int(input("Enter B color: "))

        # Create rectangle
        rec = Rectangle(rec_x, rec_y, rec_height, rec_width, (r, g, b))
        rec.draw(canvas)

    # Get data for square
    if shape_type.lower() == "square":
        sqr_x = int(input("Enter x of square: "))
        sqr_y = int(input("Enter y of square: "))
        sqr_side = int(input("Enter the side length of the square: "))
        r = int(input("Enter R color: "))
        g = int(input("Enter G color: "))
        b = int(input("Enter B color: "))

        # Create square
        sqr = Square(sqr_x, sqr_y, sqr_side, (r, g, b))
        sqr.draw(canvas)

    # Break the loop if the user entered 'quit'
    if shape_type == 'quit':
        break

canvas.make_image('canvas.png')

print("Canvas has been created and saved successfully.")
