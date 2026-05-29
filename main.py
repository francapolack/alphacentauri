"""
Platformer Game

python -m arcade.examples.platform_tutorial.01_open_window
"""
import arcade

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
START=0
END=2000
STEP=50
WINDOW_TITLE = "Platformer"


class GameView(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class to set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, resizable=True)
        self.player_texture = arcade.load_texture("placeholderastronaut.jpeg")
        self.player_sprite = arcade.Sprite(self.player_texture)
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 500

        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        self.wall_list=arcade.SpriteList(use_spatial_hash=True)


        self.background_color = arcade.csscolor.CORNFLOWER_BLUE


    def on_resize(self,WINDOW_WIDTH, WINDOW_HEIGHT):
        super().on_resize(WINDOW_WIDTH,WINDOW_HEIGHT)
        print(f"Tamaño de ventana cambiado a:{WINDOW_WIDTH} X {WINDOW_HEIGHT}")


    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self):
        """Render the screen."""
        # The clear method should always be called at the start of on_draw.
        # It clears the whole screen to whatever the background color is
        # set to. This ensures that you have a clean slate for drawing each
        # frame of the game.
        self.clear()

        # Code to draw other things will go here
        self.player_list.draw()


def main():
    """Main function"""
    window=GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()