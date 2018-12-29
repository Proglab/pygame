import pygame
from pygame.locals import *
from Actors.Player import *
from Actors.Wall import *
from configs.General import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.key.set_repeat(400, 30)
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.player = Player(self, 200, 200)
        self.all_sprites.add(self.player)

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
        self.window.fill(DARKGREY)
        self.draw_grid()
        self.all_sprites.draw(self.window)
        pygame.display.flip()

    def show_start_screen(self):
        pass

    def show_game_over_screen(self):
        pass

