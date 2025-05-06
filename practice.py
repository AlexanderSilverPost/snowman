



"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade
import random

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color((191, 0, 125))


# Get ready to draw
arcade.start_render()
# arcade.draw_lrbt_rectangle_filled(0, 600, 0, 300, arcade.csscolor.GREEN)
# arcade.draw_rect_filled(arcade.rect.XYWH(100, 320, 20, 60), arcade.csscolor.SIENNA)
# arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)
# arcade.draw_circle_filled(90, 340, 5, arcade.csscolor.RED)
# arcade.draw_rect_filled(arcade.rect.XYWH(300, 320, 20, 60), arcade.csscolor.SIENNA)
# arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)
def draw_tree(x):
    arcade.draw_text("Alex printed this text",
                 150, 230,
                 arcade.color.BLACK, 24)
    # Draw the trunk.
    triange_radius = random.randint(5,25)
    arcade.draw_rect_filled(arcade.rect.XYWH(x, 320, 15, 60), arcade.csscolor.SIENNA)
    random_num = random.randint(1,4)
    if random_num == 1:
        arcade.draw_circle_filled(x, 350, 10 + random.randint(5,20), arcade.csscolor.DARK_GREEN)
    elif random_num == 2:
        arcade.draw_arc_filled(x, 350, random.randint(30,60),random.randint(50,150),arcade.csscolor.DARK_GREEN, 0, 180)
    elif random_num == 3:
        arcade.draw_triangle_filled(
            x - triange_radius, 350, # first point
            x + triange_radius, 350, # second point
            x, 400 + random.randint(5,25), # third point 
            arcade.csscolor.DARK_GREEN)
    elif random_num == 4:
        arcade.draw_polygon_filled([(x - 40,  350), (x - 25, 370), (x, 450), (x + 25, 370),
                            (x + 40, 350),                            ],
                           arcade.csscolor.DARK_GREEN)
for i in range(10):
    x = 47 + i * 65
    draw_tree(x)

draw_tree(75)        
# (The drawing code will go here.)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
