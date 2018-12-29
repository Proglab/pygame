import pygame
import os
from configs import General
from pygame.locals import *
from configs.General import *
vector = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMAGE_FOLDER, "player.gif")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        self.game = game
        self.velocity = vector(0, 0)
        self.position = vector(x, y)

    def move(self, direction):
        self.velocity = vector(0, 0)

        if direction == 'north':
            self.velocity.y = -PLAYER_SPEED
            if self.rect.top < 0:
                self.velocity.y = 0

        if direction == 'south':
            self.velocity.y = PLAYER_SPEED
            if self.rect.bottom > HEIGHT:
                self.velocity.y = 0

        if direction == 'est':
            self.velocity.x = PLAYER_SPEED
            if self.rect.right > WIDTH:
                self.velocity.x = 0

        if direction == 'west':
            self.velocity.x = -PLAYER_SPEED
            if self.rect.left < 0:
                self.velocity.x = 0

        if self.velocity.x != 0 and self.velocity.y != 0:   # patch vertical movement
            self.velocity = vector(0.7071, 0.7071)

        self.position += self.velocity
        self.rect.y = self.position.y
        self.rect.x = self.position.x

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[K_LEFT] or keystate[K_a] or keystate[K_q]:
            self.move('west')
        if keystate[K_UP] or keystate[K_w] or keystate[K_z]:
            self.move('north')
        if keystate[K_RIGHT] or keystate[K_d]:
            self.move('est')
        if keystate[K_DOWN] or keystate[K_s]:
            self.move('south')

