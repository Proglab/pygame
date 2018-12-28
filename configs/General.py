import os

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# game settings
WIDTH = 1024
HEIGHT = 768
FPS = 60
GAME_FOLDER = os.path.join(os.path.dirname(__file__), "..")
IMAGE_FOLDER = os.path.join(GAME_FOLDER, "img")
TITLE = "My Game"

TILESIZE = 32 # taille des carré en pxl
GRID_WIDTH = WIDTH / TILESIZE
GRID_HEIGHT = HEIGHT / TILESIZE


#player settings
PLAYER_SPEED = 6
