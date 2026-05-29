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
TILE_SCALING=0.5
PLAYER_VELOCIDAD_MOVIMIENTO=5
PLAYER_VELOCIDAD_SALTO=20

GRAVEDAD=1


class GameView(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class to set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, resizable=True)
        self.scene=arcade.Scene()
        self.player_texture = None
        self.player_sprite = None
        self.player_list = None
        self.wall_list = None
        self.camara=None

        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")
        


    def on_resize(self,WINDOW_WIDTH, WINDOW_HEIGHT):
        super().on_resize(WINDOW_WIDTH,WINDOW_HEIGHT)
        print(f"Tamaño de ventana cambiado a:{WINDOW_WIDTH} X {WINDOW_HEIGHT}")


    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.player_texture = arcade.load_texture("placeholderastronaut.jpeg")
        self.player_sprite = arcade.Sprite(self.player_texture)
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 500

        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        self.wall_list=arcade.SpriteList(use_spatial_hash=True)
        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", scale=TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        coordinate_list = [[512, 96], [256, 96], [768, 96]]
        for coordinate in coordinate_list:
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", scale=TILE_SCALING)
            wall.position = coordinate
            self.wall_list.append(wall)
        
        self.physics_engine=arcade.PhysicsEnginePlatformer(self.player_sprite, walls=self.wall_list,gravity_constant=GRAVEDAD)

        self.camara=arcade.Camera2D()


        self.background_color = arcade.csscolor.CORNFLOWER_BLUE


    def on_draw(self):
        """Render the screen."""
        # The clear method should always be called at the start of on_draw.
        # It clears the whole screen to whatever the background color is
        # set to. This ensures that you have a clean slate for drawing each
        # frame of the game.
        self.clear()
        self.camara.use()

        # Code to draw other things will go here
        self.player_list.draw()
        self.wall_list.draw()
    def on_key_press(self, tecla, modifiers):
        if tecla==arcade.key.UP or tecla==arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y= PLAYER_VELOCIDAD_SALTO
                arcade.play_sound(self.jump_sound)

        elif tecla==arcade.key.DOWN or tecla==arcade.key.S:
             self.player_sprite.change_y=-PLAYER_VELOCIDAD_MOVIMIENTO
        elif tecla==arcade.key.LEFT or tecla==arcade.key.A:
             self.player_sprite.change_x=-PLAYER_VELOCIDAD_MOVIMIENTO
        elif tecla==arcade.key.RIGHT or tecla==arcade.key.D:
             self.player_sprite.change_x=PLAYER_VELOCIDAD_MOVIMIENTO

        if tecla==arcade.key.ESCAPE:
                self.setup()

    def on_key_release(self, tecla, modifiers):
        if tecla==arcade.key.UP or tecla==arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y=PLAYER_VELOCIDAD_SALTO
        elif tecla==arcade.key.DOWN or tecla==arcade.key.S:
            self.player_sprite.change_y=0
        elif tecla==arcade.key.LEFT or tecla==arcade.key.A:
            self.player_sprite.change_x=0
        elif tecla==arcade.key.RIGHT or tecla==arcade.key.D:
            self.player_sprite.change_x=0

    def on_update(self, delta_time):
        self.physics_engine.update()
        self.camara.position=self.player_sprite.position
def main():
    """Main function"""
    window=GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()