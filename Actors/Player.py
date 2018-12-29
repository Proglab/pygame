import pygame
import os
from configs import General
from pygame.locals import *
from configs.General import *


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMAGE_FOLDER, "player.gif")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        self.game = game
        self.vx = 0
        self.vy = 0
        self.x = x
        self.y = y

    #déplacement
    def move(self, direction):
        self.vx = 0
        self.vy = 0

        if direction == 'north':
            self.vy = -PLAYER_SPEED
            if self.rect.top < 0:
                self.vy = 0

        if direction == 'south':
            self.vy = PLAYER_SPEED
            if self.rect.bottom > HEIGHT:
                self.vy = 0

        if direction == 'est':
            self.vx = PLAYER_SPEED
            if self.rect.right > WIDTH:
                self.vx = 0

        if direction == 'west':
            self.vx = -PLAYER_SPEED
            if self.rect.left < 0:
                self.vx = 0

        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

        self.y += self.vy
        self.x += self.vx
        self.rect.y = self.y
        self.rect.x = self.x


    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[K_LEFT] or keystate[K_a]:
            self.move('west')
        if keystate[K_UP] or keystate[K_w]:
            self.move('north')
        if keystate[K_RIGHT] or keystate[K_d]:
            self.move('est')
        if keystate[K_DOWN] or keystate[K_s]:
            self.move('south')
