import cairo

surface =cairo.ImageSurface(cairo.FORMAT_RGB24, 1000, 1000)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

#Cross
ctx.set_source_rgb(0,0,0)
ctx.move_to(400,50)
ctx.line_to(395,50)
ctx.line_to(395,65)
ctx.line_to(375,65)
ctx.line_to(375,75)
ctx.line_to(395,75)
ctx.line_to(395,105)
ctx.line_to(405,105)
ctx.line_to(405,75)
ctx.line_to(425,75)
ctx.line_to(425,65)
ctx.line_to(405,65)
ctx.line_to(405,50)
ctx.close_path()
ctx.fill()


#CrossPillar
ctx.move_to(395,105)
ctx.line_to(385,120)
ctx.line_to(375,200)
ctx.line_to(425,200)
ctx.line_to(415,120)
ctx.line_to(405,105)
ctx.close_path()
ctx.fill()

#Top window
ctx.rectangle(330,200,140,10)
ctx.set_source_rgb(1,1,1)
ctx.stroke_preserve()
ctx.set_source_rgb(0,0,0)
ctx.fill()


# Draw the house base (black rectangle)
ctx.set_source_rgb(0, 0, 0)  # Set color to black
ctx.rectangle(100, 800, 800, 150)  # (x, y, width, height)
ctx.fill()

# Draw the windows (white squares)
ctx.set_source_rgb(1, 1, 1)  # Set color to white
ctx.rectangle(130, 850, 50, 50)  # Left window
ctx.fill()

ctx.rectangle(200, 850, 50, 50)  # Right window
ctx.fill()

ctx.rectangle(820, 850, 50, 50)  # Right window
ctx.fill()

ctx.rectangle(750, 850, 50, 50)  # Right window
ctx.fill()



ctx.set_source_rgb(0, 0, 0)  # Set color to black

# Define the four points of the trapezium (x, y)
ctx.move_to(50, 796)  # Bottom-left point
ctx.line_to(950, 796)  # Bottom-right point
ctx.line_to(860, 700)  # Top-right point
ctx.line_to(140, 700)  # Top-left point
ctx.close_path()  # Connect back to the starting point

ctx.fill()




surface.write_to_png('charpel.png')
