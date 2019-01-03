import pygame
from pygame.locals import *
from Actors.Player import *
from Actors.Map import *
from Actors.Wall import *
from configs.General import *
from os import path


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.key.set_repeat(400, 30)
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.load_data()

    def load_data(self):
        game_folder = path.join(path.dirname(__file__), '..')
        map_folder = path.join(game_folder, 'map')
        self.map = Map(path.join(map_folder, 'map.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        for tile_object in self.map.tmx.objects:
            if tile_object.name == 'player':
                self.player = Player(self, tile_object.x, tile_object.y)
                self.all_sprites.add(self.player)
            if tile_object.name == 'wall':
                wall = Wall(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
                self.walls.add(wall)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

    def events(self):
        for event in pygame.event.get():
                if event.type == QUIT:
                    if self.playing:
                        self.playing = False
                self.running = False
        pass

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.window, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.window, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        #self.window.fill(DARKGREY)
        self.window.blit(self.map_img, (0, 0))

        #self.draw_grid()
        self.all_sprites.draw(self.window)
        pygame.display.flip()

    def show_start_screen(self):
        pass

    def show_game_over_screen(self):
        pass

