import pygame
import os
from configs import General
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(General.IMAGE_FOLDER, "player.gif")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (200, 300)

    def move(self, direction):
        if direction == 'north':
            self.rect.y -= 3
            if self.rect.top < 0:
                self.rect.top = 0
        if direction == 'south':
            self.rect.y += 3
            if self.rect.bottom > General.HEIGHT:
                self.rect.bottom = General.HEIGHT
        if direction == 'est':
            self.rect.x += 3
            if self.rect.right > General.WIDTH:
                self.rect.right = General.WIDTH
        if direction == 'west':
            self.rect.x -= 3
            if self.rect.left < 0:
                self.rect.left = 0

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[K_LEFT]:
            self.move('west')
        if keystate[K_UP]:
            self.move('north')
        if keystate[K_RIGHT]:
            self.move('est')
        if keystate[K_DOWN]:
            self.move('south')
