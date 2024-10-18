import cairo

surface =cairo.ImageSurface(cairo.FORMAT_RGB24, 1000, 1000)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

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

# Draw the roof (black triangle)
ctx.set_source_rgb(0, 0, 0)  # Set color to black
ctx.move_to(80, 200)  # Starting point of the triangle
ctx.line_to(250, 100)  # Peak of the roof
ctx.line_to(420, 200)  # Right end of the roof
ctx.close_path()  # Connect back to the starting point
ctx.fill()



surface.write_to_png('charpel.png')
