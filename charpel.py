import cairo
import math
surface =cairo.ImageSurface(cairo.FORMAT_RGB24, 1000, 1000)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

### Cross
ctx.set_source_rgb(0, 0, 0)
# Horizontal rectangle (top part of the cross)
ctx.rectangle(469, 178, 62, 17)
ctx.fill()
# Vertical rectangle (bottom part of the cross)
ctx.rectangle(494, 153, 12, 92)
ctx.fill()

### Cross Pillar
ctx.move_to(494, 245)
ctx.line_to(481, 270)
ctx.line_to(469, 403)
ctx.line_to(531, 403)
ctx.line_to(519, 270)
ctx.line_to(506, 245)
ctx.close_path()
ctx.fill()

### Top Window
ctx.rectangle(413, 403, 175, 17)
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

ctx.set_source_rgb(0,0,0)
ctx.rectangle(423, 420, 155, 155)
ctx.fill()

ctx.arc(500, 460, 31, math.pi, 0)
ctx.set_source_rgb(1,1,1)
ctx.fill()

ctx.rectangle(469, 460, 62, 100)
ctx.fill()

### Roof
ctx.rectangle(350, 570, 300, 28)
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Left Roof Section
ctx.move_to(350, 570)
ctx.line_to(245, 670)
ctx.line_to(260, 680)
ctx.line_to(350, 598)
ctx.set_source_rgb(0, 0, 0)
ctx.fill()

# Right Roof Section
ctx.move_to(650, 570)
ctx.line_to(755, 670)
ctx.line_to(740, 680)
ctx.line_to(650, 598)
ctx.set_source_rgb(0, 0, 0)
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

# Add a white circle in the middle of the polygon
ctx.set_source_rgb(1, 1, 1)  # Set color to white
ctx.arc(500, 660, 35, 0, 2 * math.pi)  # Draw the circle
ctx.fill()





surface.write_to_png('charpel.png')
