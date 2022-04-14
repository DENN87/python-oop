from models.canvas import Canvas
from models.square import Square
from models.rectangle import Rectangle

# main()
canvas = Canvas(height=800, width=800, color=(255, 255, 255))

rec_1 = Rectangle(x=250, y=400, height=200, width=300, color=(100, 200, 255))

rec_1.draw(canvas)

square_1 = Square(x=250, y=300, side=100, color=(0, 100, 222))

square_1.draw(canvas)

canvas.make_image('img.png')



