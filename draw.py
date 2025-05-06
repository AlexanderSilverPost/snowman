import arcade
import time
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class SnowmanWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.snowman_x = 150
        self.hat_y = 20
        self.hat_stop = False
        self.pause_start = 0

    def draw_snowman(self, x,y):
        # Snow
        arcade.draw_circle_filled(x, y, 40, arcade.csscolor.WHITE)
        arcade.draw_circle_filled(x, y + 50, 30, arcade.csscolor.WHITE)
        arcade.draw_circle_filled(x, y + 100, 20, arcade.csscolor.WHITE)
        # button
        arcade.draw_circle_filled(x, y, 2, arcade.csscolor.BLACK)
        arcade.draw_circle_filled(x, y + 50, 2, arcade.csscolor.BLACK)

        arcade.draw_triangle_filled(x,y + 105 ,x,y + 90,x + 20, y + 97.5,arcade.csscolor.ORANGE)
        # eyes
        arcade.draw_circle_filled(x - 10, y + 110, 3, arcade.csscolor.BLACK)
        arcade.draw_circle_filled(x + 10, y + 110, 3, arcade.csscolor.BLACK)
        # arm 1
        arcade.draw_line(x + 30, y + 50, x + 80, y + 80, arcade.color.DARK_BROWN, 3)
        arcade.draw_line(x + 80, y + 80, x + 90, y + 100, arcade.color.DARK_BROWN, 2)
        arcade.draw_line(x + 80, y + 80, x + 95, y + 80, arcade.color.DARK_BROWN, 2)
        arcade.draw_line(x + 80, y + 80, x + 90, y + 60, arcade.color.DARK_BROWN, 2)
        #arm 2
        arcade.draw_line(x - 30 , y + 50, x - 80, y + 80, arcade.color.DARK_BROWN, 3)
        arcade.draw_line(x - 80, y + 80, x - 90, y + 100, arcade.color.DARK_BROWN, 2)
        arcade.draw_line(x - 80, y + 80, x - 95, y + 80, arcade.color.DARK_BROWN, 2)
        arcade.draw_line(x - 80, y + 80, x - 90, y + 70, arcade.color.DARK_BROWN, 2)
        #tophat
        arcade.draw_polygon_filled([(x - 30,y + 120 + self.hat_y),(x + 30,y + 120+ self.hat_y),(x + 30,y + 140+ self.hat_y),(x + 20,y + 140+ self.hat_y),(x + 20,y + 180+ self.hat_y),(x - 10,y + 180+ self.hat_y),(x - 10,y + 140+ self.hat_y),(x - 30,y + 140+ self.hat_y),(x - 30,y + 80+ self.hat_y)],arcade.csscolor.BLACK)
    def on_draw(self):
        self.clear()
        self.draw_snowman(self.snowman_x, 140)
        self.snowman_x += 3
        if  self.hat_stop == False:
            if self.hat_y == 20:
                self.hat_y = 0
            else:
                self.hat_y = 20

            self.hat_stop = True
            self.pause_start = time.time()
        else:
            if time.time() - self.pause_start >= 0.5:
                self.hat_stop = False


def main():
    game = SnowmanWindow(SCREEN_WIDTH, SCREEN_HEIGHT, "snowman")

    # Call on_draw every 60th of a second.
    #arcade.schedule(game.on_draw, 5)
    game.set_update_rate(1/60)
    arcade.run()


# Call the main function to get the program started.
main()