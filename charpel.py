import cairo
import math
surface =cairo.ImageSurface(cairo.FORMAT_RGB24, 1000, 1000)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

### Cross
ctx.set_source_rgb(0, 0, 0)
# Horizontal rectangle (top part of the cross)
ctx.rectangle(469, 108, 62, 17)  # Width of 62 (from 469 to 531), height of 17 (from 108 to 125)
ctx.fill()
# Vertical rectangle (bottom part of the cross)
ctx.rectangle(494, 83, 12, 92)  # Width of 12 (from 494 to 506), height of 92 (from 83 to 175)
ctx.fill()


### Cross Pillar
ctx.move_to(494, 175)
ctx.line_to(481, 200)
ctx.line_to(469, 333)
ctx.line_to(531, 333)
ctx.line_to(519, 200)
ctx.line_to(506, 175)
ctx.close_path()
ctx.fill()

### Top Window
ctx.rectangle(413, 333, 175, 17)
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

ctx.set_source_rgb(0,0,0)
ctx.rectangle(423,350,155,155)
ctx.fill()

ctx.arc(500,390,31,math.pi,0)
ctx.set_source_rgb(1,1,1)
ctx.fill()

ctx.rectangle(469,390,62,100)
ctx.fill()

# Roof
ctx.rectangle(385, 500, 231, 20)
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Left Roof Section
ctx.move_to(386, 501)
ctx.line_to(285, 600)
ctx.line_to(285, 620)
ctx.line_to(386, 520)
ctx.set_source_rgb(0, 0, 0)
ctx.fill()

# Right Roof Section
ctx.move_to(615, 501)
ctx.line_to(715, 600)
ctx.line_to(715, 620)
ctx.line_to(615, 520)
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




surface.write_to_png('charpel.png')
