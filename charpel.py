import cairo

# Create the surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 1000, 1000)
ctx = cairo.Context(surface)

# Set background to white
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

ctx.rectangle(200, 850, 50, 50)  # Second window
ctx.fill()

ctx.rectangle(820, 850, 50, 50)  # Third window
ctx.fill()

ctx.rectangle(750, 850, 50, 50)  # Fourth window
ctx.fill()

# Draw the trapezium for the roof
ctx.set_source_rgb(0, 0, 0)  # Set color to black
ctx.move_to(50, 796)  # Bottom-left point
ctx.line_to(950, 796)  # Bottom-right point
ctx.line_to(860, 700)  # Top-right point
ctx.line_to(140, 700)  # Top-left point
ctx.close_path()  # Connect back to the starting point
ctx.fill()

# Draw the polygon structure on top (the additional shape)
ctx.set_source_rgb(0, 0, 0)  # Set color to black

# Define points for the polygon shape
ctx.move_to(300, 980)  # Bottom-left corner of the polygon
ctx.line_to(300, 650)  # Left vertical
ctx.line_to(350, 600)  # Slant left
ctx.line_to(650, 600)  # Top horizontal
ctx.line_to(700, 650)  # Slant right
ctx.line_to(700, 980)  # Right vertical
ctx.line_to(300, 980)  # Bottom horizontal

# Fill the shape
ctx.fill()

# Add white stroke around the polygon
ctx.set_source_rgb(1, 1, 1)  # Set color to white
ctx.set_line_width(5)  # Set stroke width
ctx.move_to(300, 980)  # Bottom-left corner of the polygon
ctx.line_to(300, 650)  # Left vertical
ctx.line_to(350, 600)  # Slant left
ctx.line_to(650, 600)  # Top horizontal
ctx.line_to(700, 650)  # Slant right
ctx.line_to(700, 980)  # Right vertical
ctx.line_to(300, 980)
ctx.close_path()

# Stroke the polygon
ctx.stroke()

# Save the final image
surface.write_to_png('charpel.png')
